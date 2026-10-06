#!/usr/bin/env python3
"""Mede, no Markdown já gerado, os problemas apontados na avaliação pedagógica.

Uso:
    python3 scripts/metricas_apostila.py              # resumo por grupo de arquivos
    python3 scripts/metricas_apostila.py --por-arquivo # uma linha por arquivo
    python3 scripts/metricas_apostila.py --markdown    # tabela para colar na descrição do PR

O que é contado em cada arquivo:

- **vocabulário automático:** blocos "Antes de ler este trecho" (AP-01 / seção 3.1 da avaliação);
- **definições defensivas:** ocorrências de "compatíve" e "conforme" (seção 3.2);
- **revisão circular:** respostas da revisão que repetem, palavra por palavra, um parágrafo da
  abertura "Antes de começar" da própria aula (seção 3.4);
- **seções só com texto padrão:** títulos cujo corpo, fora as frases genéricas do gerador e os
  blocos de vocabulário, não tem conteúdo (seção 3.5);
- **autoral × gerado:** arquivos que começam com `<!-- autoral -->`, escritos à mão.

As métricas apontam problemas; não são metas de quantidade. Nenhuma delas julga conteúdo técnico:
afirmações sobre a AWS continuam sendo conferidas em fonte oficial, uma a uma.

Saída com código 0 sempre: é um relatório, não um teste.
"""
import argparse
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

AUTORAL = "<!-- autoral -->"
VOCABULARIO = "**Antes de ler este trecho:**"
DEFENSIVAS = ("compatíve", "conforme")

# Frases genéricas que o gerador repete em todo arquivo (scripts/apostila.py). Uma seção que só
# tem estas frases promete conteúdo e não entrega.
FRASES_PADRAO = (
    "Leia cada linha como uma alternativa e cada coluna como um critério de comparação",
    "A resposta muda se mudar o requisito destacado",
    "Tente responder antes de ler o comentário",
    "Leia primeiro os fundamentos e a sequência",
    "Uma opção deve atender ao requisito da aplicação",
    "Ter o recurso disponível é diferente de operá-lo corretamente",
    "Este capítulo explica os fundamentos e as opções do material",
    "Comece pelas aberturas dos tópicos para entender a situação e a solução",
)

ABERTURA = "## 🧠 Antes de começar"
REVISAO = "### Confira se você compreendeu"

GRUPOS = (
    ("aulas", lambda rel: re.match(r"docs/(0[1-4]-[^/]+|fundamentos)/", rel)
     and not rel.endswith("README.md")),
    ("índices de domínio", lambda rel: re.match(r"docs/(0[1-4]-[^/]+|fundamentos)/README\.md$", rel)),
    ("páginas de apoio", lambda rel: rel.startswith("docs/00-guia-do-exame/")),
    ("fichas", lambda rel: rel.startswith("servicos/") and not rel.endswith("README.md")),
    ("resumos e flashcards", lambda rel: rel.startswith(("resumos/", "flashcards/"))),
    ("simulados e questões", lambda rel: rel.startswith("simulados/")),
)


def paragrafos(texto):
    return [p.strip() for p in texto.split("\n\n") if p.strip()]


def secoes(texto):
    """(título, corpo) de cada título de nível 2 a 6 que não tenha subtítulos.

    Um título com subtítulos entrega o conteúdo neles; só o título folha promete e cumpre
    (ou não) por conta própria.
    """
    partes = re.split(r"^(#{2,6} .+)$", texto, flags=re.M)
    titulos = [(partes[i].strip(), partes[i + 1]) for i in range(1, len(partes), 2)]
    folhas = []
    for i, (titulo, corpo) in enumerate(titulos):
        nivel = len(titulo) - len(titulo.lstrip("#"))
        proximo = titulos[i + 1][0] if i + 1 < len(titulos) else ""
        if proximo and len(proximo) - len(proximo.lstrip("#")) > nivel:
            continue
        folhas.append((titulo, corpo))
    return folhas


def sem_texto_padrao(corpo):
    """Corpo da seção sem os blocos de vocabulário e sem as frases genéricas do gerador."""
    # O bloco de vocabulário é o marcador seguido da lista de definições.
    corpo = re.sub(re.escape(VOCABULARIO) + r"\s*\n(?:- [^\n]*\n?)*", "", corpo)
    return [p for p in paragrafos(corpo) if not any(frase in p for frase in FRASES_PADRAO)]


def respostas_da_abertura(texto):
    """Parágrafos da abertura 'Antes de começar', sem os rótulos em negrito."""
    if ABERTURA not in texto:
        return set()
    corpo = texto.split(ABERTURA, 1)[1].split("\n## ", 1)[0]
    fora = set()
    for p in paragrafos(corpo):
        m = re.match(r"\*\*[^*]+:?\*\*\s*(.+)", p, re.S)
        if m and not p.startswith("| "):
            fora.add(m.group(1).strip())
    return fora


def revisao_circular(texto):
    """Respostas da revisão que são cópia literal de um parágrafo da abertura."""
    if REVISAO not in texto:
        return 0
    abertura = respostas_da_abertura(texto)
    if not abertura:
        return 0
    corpo = texto.split(REVISAO, 1)[1]
    corpo = re.split(r"^#{2,3} ", corpo, maxsplit=1, flags=re.M)[0]
    return sum(1 for p in paragrafos(corpo) if p in abertura)


def medir(caminho):
    with open(caminho) as f:
        texto = f.read()
    vazias = [t for t, corpo in secoes(texto) if not sem_texto_padrao(corpo)]
    return {
        "autoral": AUTORAL in "".join(texto.splitlines(keepends=True)[:10]),
        "vocabulario": texto.count(VOCABULARIO),
        "defensivas": sum(texto.lower().count(p) for p in DEFENSIVAS),
        "circular": revisao_circular(texto),
        "secoes_padrao": len(vazias),
        "titulos_padrao": vazias,
        "palavras": len(texto.split()),
    }


CAMPOS = (("Arquivos", "arquivos"), ("Autorais", "autorais"), ("Vocabulário automático", "vocabulario"),
          ("Definições defensivas", "defensivas"), ("Revisões circulares", "circular"),
          ("Seções só com texto padrão", "secoes_padrao"), ("Palavras", "palavras"))


def coletar():
    """Métricas por arquivo, na ordem dos grupos."""
    encontrados = []
    for pasta, _, arquivos in os.walk(RAIZ):
        rel_pasta = os.path.relpath(pasta, RAIZ)
        if "/.git" in pasta or rel_pasta.startswith((".git", "templates", "fontes", "pendencias", "scripts", "build", "node_modules")):
            continue
        for nome in sorted(arquivos):
            if nome.endswith(".md"):
                rel = os.path.relpath(os.path.join(pasta, nome), RAIZ).replace(os.sep, "/")
                encontrados.append(rel)
    resultado = []
    usados = set()
    for grupo, pertence in GRUPOS:
        for rel in sorted(encontrados):
            if rel not in usados and pertence(rel):
                usados.add(rel)
                resultado.append((grupo, rel, medir(os.path.join(RAIZ, rel))))
    for rel in sorted(set(encontrados) - usados):
        resultado.append(("outros", rel, medir(os.path.join(RAIZ, rel))))
    return resultado


def totais(linhas):
    agregado = {chave: 0 for _, chave in CAMPOS}
    for _, _, m in linhas:
        agregado["arquivos"] += 1
        agregado["autorais"] += int(m["autoral"])
        for chave in ("vocabulario", "defensivas", "circular", "secoes_padrao", "palavras"):
            agregado[chave] += m[chave]
    return agregado


def tabela(cabecalho, linhas):
    larguras = [max(len(str(l[i])) for l in [cabecalho] + linhas) for i in range(len(cabecalho))]
    def formata(l):
        return "  ".join(str(v).ljust(larguras[i]) if i == 0 else str(v).rjust(larguras[i])
                         for i, v in enumerate(l))
    return "\n".join([formata(cabecalho), "  ".join("-" * w for w in larguras)]
                     + [formata(l) for l in linhas])


def main(argv=None):
    p = argparse.ArgumentParser(description="Métricas do Markdown da apostila.")
    p.add_argument("--por-arquivo", action="store_true", help="uma linha por arquivo")
    p.add_argument("--markdown", action="store_true", help="tabela em Markdown, para a descrição do PR")
    p.add_argument("--secoes-padrao", action="store_true", help="lista os títulos sem conteúdo próprio")
    args = p.parse_args(argv)

    linhas = coletar()
    rotulos = [r for r, _ in CAMPOS]
    if args.por_arquivo:
        dados = [[rel, int(m["autoral"]), m["vocabulario"], m["defensivas"], m["circular"],
                  m["secoes_padrao"], m["palavras"]] for _, rel, m in linhas]
        cabecalho = ["Arquivo", "Autoral", "Vocabulário", "Defensivas", "Circulares", "Padrão", "Palavras"]
    else:
        grupos = []
        for grupo, _ in GRUPOS + (("outros", None),):
            do_grupo = [l for l in linhas if l[0] == grupo]
            if do_grupo:
                t = totais(do_grupo)
                grupos.append([grupo] + [t[chave] for _, chave in CAMPOS])
        t = totais(linhas)
        grupos.append(["total"] + [t[chave] for _, chave in CAMPOS])
        dados = grupos
        cabecalho = ["Grupo"] + rotulos

    if args.markdown:
        print("| " + " | ".join(cabecalho) + " |")
        print("|" + "---|" * len(cabecalho))
        for linha in dados:
            print("| " + " | ".join(str(v) for v in linha) + " |")
    else:
        print(tabela(cabecalho, dados))

    if args.secoes_padrao:
        print("\nSeções só com texto padrão:")
        for _, rel, m in linhas:
            for titulo in m["titulos_padrao"]:
                print(f"  {rel} → {titulo}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
