#!/usr/bin/env python3
"""Gera a edição impressa da apostila (PDF) a partir dos mesmos Markdown da versão digital.

O conteúdo não é duplicado: o script lê as aulas, as fichas e as questões e aplica só
transformações de apresentação (seção 10 do plano de implementação):

- remove a navegação (🏠 ⬅️ ➡️) e as linhas de separação;
- links internos viram texto ("aula 3.10"); links externos viram nota de rodapé;
- as respostas em <details> vão para o gabarito no fim do volume, com o número da página;
- emojis de legenda viram marcadores de texto, explicados uma vez no início;
- o bloco "Minhas anotações" vira linhas pautadas;
- os diagramas Mermaid são renderizados em SVG com o mermaid-cli (mmdc).

Saem três volumes em build/impressa/: Rumo à Cloud Practitioner (as aulas), caderno de consulta (fichas núcleo e
resumos) e caderno de exercícios (questões e gabarito comentado).

Requisitos: Pandoc, WeasyPrint (python3 -m pip install weasyprint) e mermaid-cli
(npm install @mermaid-js/mermaid-cli). Variáveis opcionais: MMDC (caminho do mmdc) e
CHROMIUM_PATH (navegador usado pelo mmdc).

Uso: python3 scripts/gerar_impressa.py [--volume rumo|consulta|exercicios] [--so-html]
"""
import argparse
import datetime
import glob
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = os.path.join(RAIZ, "build", "impressa")
FIGURAS = os.path.join(SAIDA, "figuras")
CSS = os.path.join(RAIZ, "assets", "impressao.css")

DOMINIOS = [
    ("docs/fundamentos", "Capítulo 0 — Fundamentos de TI", "Não corresponde a um domínio da prova; prepara para os quatro domínios."),
    ("docs/01-conceitos-de-nuvem", "Domínio 1 — Conceitos de Nuvem", "24% das questões pontuadas"),
    ("docs/02-seguranca-e-conformidade", "Domínio 2 — Segurança e Conformidade", "30% das questões pontuadas"),
    ("docs/03-tecnologia-e-servicos", "Domínio 3 — Tecnologia e Serviços de Nuvem", "34% das questões pontuadas"),
    ("docs/04-cobranca-precos-e-suporte", "Domínio 4 — Cobrança, Preços e Suporte", "12% das questões pontuadas"),
]

# Marcadores de texto que substituem os emojis de legenda. A legenda sai no início de cada volume.
MARCADORES = {"✅": "✓", "❌": "✗", "⚪": "○", "🔀": "◐", "⚠": "⚠"}
LEGENDA = "✓ no escopo da prova · ✗ fora do escopo · ○ não aparece na lista oficial · ◐ parte no escopo, parte fora"
EMOJIS_REMOVIDOS = "📖🔎📝❓🧠🧭🗺️🎯⚖️🔑📌🧊🔄✔️️"

LINHAS_PAUTADAS = 10


def ler(caminho):
    with open(os.path.join(RAIZ, caminho), encoding="utf-8") as f:
        return f.read()


def aulas(pasta):
    return sorted(os.path.relpath(p, RAIZ) for p in glob.glob(os.path.join(RAIZ, pasta, "[0-9]*.md")))


def titulo(texto):
    m = re.search(r"^# (.+)$", texto, re.M)
    assert m, "arquivo sem título"
    return limpar_emojis(m.group(1)).strip()


def limpar_emojis(texto):
    for emoji, marcador in MARCADORES.items():
        texto = texto.replace(emoji, marcador)
    for emoji in EMOJIS_REMOVIDOS:
        texto = texto.replace(emoji, "")
    texto = re.sub("[\U0001F000-\U0001FAFF]", "", texto)
    texto = re.sub("[\u2600-\u27BF]", lambda m: m.group(0) if m.group(0) in "✓✗⚠" else "", texto)
    return re.sub(r"[ \t]{2,}", " ", texto)


def ancora(caminho):
    return "f-" + re.sub(r"[^a-z0-9]+", "-", caminho.lower().removesuffix(".md")).strip("-")


class Volume:
    """Junta os arquivos de um volume e guarda o que precisa ir para o gabarito."""

    def __init__(self, nome, titulo_volume, subtitulo, rotulos):
        self.nome = nome
        self.titulo = titulo_volume
        self.subtitulo = subtitulo
        self.rotulos = rotulos  # caminho -> rótulo usado nos links ("aula 2.1")
        self.partes = []
        self.sumario = []
        self.gabarito = []  # (título do grupo, [(id, pergunta, resposta)])
        self.diagramas = {}

    # --- transformações de apresentação ---

    def links(self, texto, origem):
        def trocar(m):
            rotulo, alvo = m.group(1), m.group(2)
            if re.match(r"https?://", alvo):
                if rotulo.strip("<>") == alvo:
                    return alvo
                return f'{rotulo}<span class="nota">{html.escape(alvo)}</span>'
            if alvo.startswith(("#", "mailto:")):
                return rotulo
            caminho = os.path.normpath(os.path.join(os.path.dirname(origem), alvo.split("#")[0]))
            extra = self.rotulos.get(caminho)
            if extra and extra.split()[-1] not in rotulo:
                return f"{rotulo} ({extra})"
            return rotulo
        return re.sub(r"(?<!!)\[([^\]\n]+)\]\(([^)\s]+)\)", trocar, texto)

    def respostas(self, texto, prefixo, perguntas):
        """Troca cada <details> pela referência ao gabarito e guarda a resposta."""
        itens = []

        def trocar(m):
            n = len(itens) + 1
            ident = f"r-{prefixo}-{n}"
            corpo = m.group(1).strip()
            antes = texto[:m.start()]
            pergunta = re.findall(r"^#{3,4} (.+)$", antes, re.M)
            itens.append((ident, pergunta[-1] if pergunta and perguntas else f"Questão {n}", corpo))
            return f'\n<p class="ver-gabarito">Resposta no gabarito, página <a href="#{ident}"></a>.</p>\n'
        novo = re.sub(r"<details>\s*<summary>.*?</summary>(.*?)</details>", trocar, texto, flags=re.S)
        return novo, itens

    def mermaid(self, texto):
        def trocar(m):
            codigo = m.group(1).strip() + "\n"
            nome = hashlib.sha1(codigo.encode()).hexdigest()[:16] + ".svg"
            self.diagramas[nome] = codigo
            return f'\n<div class="diagrama"><img src="figuras/{nome}" alt="Diagrama"></div>\n'
        return re.sub(r"```mermaid\n(.*?)```", trocar, texto, flags=re.S)

    def preparar(self, texto, origem, nivel, prefixo, perguntas=True, anotacoes=True):
        texto = re.sub(r"<!-- notas:inicio -->.*?<!-- notas:fim -->", "<!--ANOTACOES-->" if anotacoes else "", texto, flags=re.S)
        texto = re.sub(r" · \[ver lista\]\([^)]*\)", "", texto)
        texto = re.sub(r"<!-- (?!ANOTACOES).*?-->\n?", "", texto, flags=re.S)
        texto = self.mermaid(texto)
        linhas = []
        for linha in texto.split("\n"):
            if "🏠" in linha or "⬅️" in linha or re.fullmatch(r"\s*---\s*", linha):
                continue
            if linha.startswith("# "):
                continue  # o título sai como cabeçalho do volume
            if linha.startswith("#"):
                linha = "#" * nivel + linha
            linhas.append(linha)
        texto = "\n".join(linhas)
        texto, itens = self.respostas(texto, prefixo, perguntas)
        texto = self.links(texto, origem)
        texto = re.sub(r'antes de abrir "Ver resposta"|antes de abrir cada resposta', "antes de consultar o gabarito", texto)
        texto = limpar_emojis(texto)
        pauta = "".join('<div class="linha"></div>' for _ in range(LINHAS_PAUTADAS))
        texto = texto.replace("<!--ANOTACOES-->", f'<section class="anotacoes"><p class="titulo-anotacoes">Anotações</p>{pauta}</section>')
        return texto.strip() + "\n", itens

    # --- montagem ---

    def parte(self, titulo_parte, descricao=""):
        ident = "p-" + re.sub(r"[^a-z0-9]+", "-", titulo_parte.lower()).strip("-")
        self.sumario.append((1, ident, titulo_parte))
        desc = f'<p class="descricao-parte">{html.escape(descricao)}</p>' if descricao else ""
        self.partes.append(f'<h1 class="parte" id="{ident}">{html.escape(titulo_parte)}</h1>\n{desc}\n')

    def arquivo(self, caminho, classe="aula", grupo_gabarito=None, perguntas=True, titulo_arquivo=None, nivel_sumario=2, anotacoes=True):
        texto = ler(caminho)
        nome = titulo_arquivo or titulo(texto)
        ident = ancora(caminho)
        self.sumario.append((nivel_sumario, ident, nome))
        prefixo = ident.removeprefix("f-")
        corpo, itens = self.preparar(texto, caminho, 1, prefixo, perguntas, anotacoes)
        if itens:
            self.gabarito.append((grupo_gabarito or nome, itens))
        self.partes.append(f'<h2 class="{classe}" id="{ident}">{html.escape(nome)}</h2>\n\n{corpo}\n')

    def secao_gabarito(self, titulo_secao, introducao):
        if not self.gabarito:
            return
        self.parte(titulo_secao)
        blocos = [f"<p>{html.escape(introducao)}</p>\n"]
        for grupo, itens in self.gabarito:
            blocos.append(f'<h3 class="grupo-gabarito">{html.escape(grupo)}</h3>\n')
            for ident, pergunta, resposta in itens:
                blocos.append(f'<div class="resposta" id="{ident}">\n\n**{pergunta.strip()}**\n\n{resposta}\n\n</div>\n')
        self.partes.append("\n".join(blocos))

    # --- saída ---

    def html_sumario(self):
        itens = []
        for nivel, ident, nome in self.sumario:
            itens.append(f'<li class="nivel-{nivel}"><a href="#{ident}">{html.escape(nome)}</a></li>')
        return '<nav class="sumario"><h1 class="titulo-sumario">Sumário</h1><ul>' + "".join(itens) + "</ul></nav>"

    def html_inicio(self, colofao):
        return f"""<section class="capa">
<p class="serie">Apostila AWS Certified Cloud Practitioner (CLF-C02)</p>
<h1 class="titulo-capa">{html.escape(self.titulo)}</h1>
<p class="subtitulo-capa">{html.escape(self.subtitulo)}</p>
</section>
<section class="colofao">
{colofao}
<p class="legenda"><strong>Legenda dos marcadores:</strong> {html.escape(LEGENDA)}.</p>
</section>
"""


def colofao(arquivos):
    datas = []
    for caminho in arquivos:
        for d, m, a in re.findall(r"[Vv]erificad[ao]s? em (\d{2})/(\d{2})/(\d{4})", ler(caminho)):
            datas.append(datetime.date(int(a), int(m), int(d)))
    try:
        commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=RAIZ, capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        commit = "desconhecido"
    hoje = datetime.date.today().strftime("%d/%m/%Y")
    verificacao = ""
    if datas:
        periodo = (f"em {min(datas):%d/%m/%Y}" if min(datas) == max(datas)
                   else f"entre {min(datas):%d/%m/%Y} e {max(datas):%d/%m/%Y}")
        verificacao = (f"<p>As informações sobre a AWS foram conferidas nas páginas oficiais {periodo}. "
                       f"A AWS muda preços, limites e nomes com frequência: "
                       f"antes da prova, confira as fontes citadas em cada aula e ficha.</p>")
    return (f"<p>Edição impressa gerada em {hoje} a partir do commit <code>{commit[:12]}</code> do repositório "
            f"github.com/tuanyfortunato/aws-cloud-practitioner.</p>{verificacao}"
            "<p>O material não é oficial da AWS. Os exemplos, os casos e as questões são autorais e não reproduzem questões da prova.</p>")


def rotulos_aulas():
    rotulos = {}
    for pasta, _, _ in DOMINIOS:
        for caminho in aulas(pasta):
            m = re.match(r"(\d+\.\d+)", titulo(ler(caminho)))
            if m:
                rotulos[caminho] = f"aula {m.group(1)}"
    return rotulos


def fichas_nucleo():
    """Fichas núcleo na ordem e nas categorias do índice servicos/README.md."""
    categorias = []
    for linha in ler("servicos/README.md").split("\n"):
        if linha.startswith("## ") and "começar" not in linha:
            categorias.append((limpar_emojis(linha[3:]).strip(), []))
        m = re.match(r"\| \[[^\]]+\]\(([^)]+)\) \| [^|]+ \| núcleo \|", linha)
        if m and categorias:
            categorias[-1][1].append(os.path.join("servicos", m.group(1)))
    return [(c, fs) for c, fs in categorias if fs]


def volume_livro(rotulos):
    v = Volume("rumo-a-cloud-practitioner", "Rumo à Cloud Practitioner", "Capítulo 0 e aulas 1.1 a 4.6", rotulos)
    arquivos = ["docs/00-guia-do-exame/estrutura-da-apostila.md", "docs/00-guia-do-exame/caso-da-escola.md"]
    for caminho in arquivos:
        v.arquivo(caminho, classe="apresentacao")
    for pasta, nome, descricao in DOMINIOS:
        v.parte(nome, descricao)
        for caminho in aulas(pasta):
            v.arquivo(caminho)
            arquivos.append(caminho)
    v.arquivo("glossario.md", classe="apendice glossario", titulo_arquivo="Glossário", nivel_sumario=1)
    v.secao_gabarito("Gabarito das revisões", "Respostas às perguntas da seção Revisão de cada aula. Tente responder antes de consultar.")
    return v, arquivos


def volume_consulta(rotulos):
    v = Volume("caderno-de-consulta", "Caderno de consulta", "Fichas dos serviços mais cobrados e resumos de revisão", rotulos)
    arquivos = []
    for categoria, fichas in fichas_nucleo():
        v.parte(categoria)
        for caminho in fichas:
            v.arquivo(caminho, classe="ficha", anotacoes=False)
            arquivos.append(caminho)
    v.parte("Revisão rápida")
    for caminho in ["resumos/comparativos.md", "resumos/palavras-chave.md", "resumos/numeros-ancora.md"]:
        v.arquivo(caminho, classe="apendice", anotacoes=False)
        arquivos.append(caminho)
    return v, arquivos


def volume_exercicios(rotulos):
    v = Volume("caderno-de-exercicios", "Caderno de exercícios", "Questões por domínio e gabarito comentado", rotulos)
    arquivos = []
    for n in range(1, 5):
        caminho = f"simulados/questoes/dominio-{n}.md"
        nome = titulo(ler(caminho)).replace("Questões — ", "")
        v.arquivo(caminho, classe="questoes", titulo_arquivo=nome, perguntas=False, grupo_gabarito=nome)
        arquivos.append(caminho)
    v.secao_gabarito("Gabarito comentado", "A explicação de cada questão diz por que a alternativa certa atende ao requisito e por que as outras não servem.")
    return v, arquivos


def renderizar_diagramas(diagramas):
    pendentes = {n: c for n, c in diagramas.items() if not os.path.exists(os.path.join(FIGURAS, n))}
    if not pendentes:
        return
    mmdc = os.environ.get("MMDC") or shutil.which("mmdc")
    if not mmdc:
        sys.exit("mmdc não encontrado: instale o mermaid-cli (npm install @mermaid-js/mermaid-cli) ou defina MMDC.")
    config = os.path.join(SAIDA, "mermaid.json")
    with open(config, "w") as f:
        json.dump({"theme": "neutral", "htmlLabels": False, "flowchart": {"htmlLabels": False}}, f)
    puppeteer = os.path.join(SAIDA, "puppeteer.json")
    opcoes = {"args": ["--no-sandbox"]}
    if os.environ.get("CHROMIUM_PATH"):
        opcoes["executablePath"] = os.environ["CHROMIUM_PATH"]
    with open(puppeteer, "w") as f:
        json.dump(opcoes, f)

    def gerar(item):
        nome, codigo = item
        origem = os.path.join(FIGURAS, nome.replace(".svg", ".mmd"))
        with open(origem, "w", encoding="utf-8") as f:
            f.write(codigo)
        r = subprocess.run([mmdc, "-q", "-i", origem, "-o", os.path.join(FIGURAS, nome), "-c", config, "-p", puppeteer],
                           capture_output=True, text=True)
        os.remove(origem)
        return nome, r

    with ThreadPoolExecutor(max_workers=4) as executor:
        for nome, r in executor.map(gerar, pendentes.items()):
            if r.returncode != 0:
                sys.exit(f"Falha ao renderizar o diagrama {nome}:\n{r.stderr}")
    print(f"{len(pendentes)} diagrama(s) renderizado(s).")


def escrever_volume(v, arquivos, so_html):
    renderizar_diagramas(v.diagramas)
    markdown = "\n\n".join(v.partes)
    origem = os.path.join(SAIDA, v.nome + ".md")
    with open(origem, "w", encoding="utf-8") as f:
        f.write(markdown)
    corpo = subprocess.run(["pandoc", "-f", "gfm", "-t", "html5", "--wrap=none", origem],
                           capture_output=True, text=True, check=True).stdout
    documento = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="utf-8"><title>{html.escape(v.titulo)}</title>
<link rel="stylesheet" href="../../assets/impressao.css"></head>
<body class="{v.nome}">
{v.html_inicio(colofao(arquivos))}
{v.html_sumario()}
{corpo}
</body></html>
"""
    destino_html = os.path.join(SAIDA, v.nome + ".html")
    with open(destino_html, "w", encoding="utf-8") as f:
        f.write(documento)
    if so_html:
        print(f"{os.path.relpath(destino_html, RAIZ)} gerado.")
        return
    from weasyprint import HTML
    destino = os.path.join(SAIDA, v.nome + ".pdf")
    HTML(destino_html, base_url=SAIDA + "/").write_pdf(destino)
    print(f"{os.path.relpath(destino, RAIZ)} gerado.")


VOLUMES = {"rumo": volume_livro, "consulta": volume_consulta, "exercicios": volume_exercicios}


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--volume", choices=VOLUMES, action="append", help="gera só este volume (pode repetir)")
    parser.add_argument("--so-html", action="store_true", help="gera o HTML sem converter para PDF")
    args = parser.parse_args()
    os.makedirs(FIGURAS, exist_ok=True)
    rotulos = rotulos_aulas()
    for nome in args.volume or VOLUMES:
        volume, arquivos = VOLUMES[nome](rotulos)
        escrever_volume(volume, arquivos, args.so_html)


if __name__ == "__main__":
    main()
