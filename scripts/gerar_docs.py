#!/usr/bin/env python3
"""Gera os índices, os flashcards e a navegação da apostila a partir das aulas e fichas escritas à mão.

Uso: python3 scripts/gerar_docs.py

Todas as aulas (docs/), fichas (servicos/), páginas do guia do exame e resumos começam com
<!-- autoral --> e são a fonte da verdade: o gerador não reescreve nenhuma delas. Ele cuida de:

- índices de domínio (docs/<domínio>/README.md) e índice das fichas (servicos/README.md);
- flashcards (flashcards/*.md e o arquivo do Anki), tirados da seção Revisão de cada aula;
- blocos gerados do README.md (tabela de materiais e sumário).
"""
import csv
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOMINIOS = {
    "1": ("01-conceitos-de-nuvem", "Domínio 1 — Conceitos de Nuvem", "24%"),
    "2": ("02-seguranca-e-conformidade", "Domínio 2 — Segurança e Conformidade", "30%"),
    "3": ("03-tecnologia-e-servicos", "Domínio 3 — Tecnologia e Serviços de Nuvem", "34%"),
    "4": ("04-cobranca-precos-e-suporte", "Domínio 4 — Cobrança, Preços e Suporte", "12%"),
}

ARQUIVOS = {
    "1.1": "01-o-que-e-computacao-em-nuvem",
    "1.2": "02-vantagens-da-nuvem",
    "1.3": "03-conceitos-de-arquitetura",
    "1.4": "04-well-architected-framework",
    "1.5": "05-cloud-adoption-framework",
    "1.6": "06-estrategias-de-migracao",
    "1.7": "07-economia-da-nuvem",
    "2.1": "01-responsabilidade-compartilhada",
    "2.2": "02-usuario-root",
    "2.3": "03-iam",
    "2.4": "04-governanca-multi-conta",
    "2.5": "05-criptografia",
    "2.6": "06-compliance-e-governanca",
    "2.7": "07-logs-monitoramento-e-auditoria",
    "2.8": "08-protecao-de-rede-e-aplicacoes",
    "2.9": "09-deteccao-de-ameacas",
    "2.10": "10-outros-pontos-de-seguranca",
    "3.1": "01-formas-de-acesso-e-implantacao",
    "3.2": "02-infraestrutura-global",
    "3.3": "03-ec2",
    "3.4": "04-escalabilidade-e-balanceamento",
    "3.5": "05-containers-e-serverless",
    "3.6": "06-outros-servicos-de-computacao",
    "3.7": "07-bancos-de-dados",
    "3.8": "08-s3",
    "3.9": "09-outros-armazenamentos",
    "3.10": "10-rede-e-entrega-de-conteudo",
    "3.11": "11-analytics",
    "3.12": "12-ia-e-machine-learning",
    "3.13": "13-integracao-de-aplicacoes",
    "3.14": "14-aplicacoes-de-negocio-e-iot",
    "3.15": "15-ferramentas-de-desenvolvimento",
    "3.16": "16-gestao-e-governanca",
    "3.17": "17-migracao-e-transferencia",
    "3.18": "18-servicos-menos-conhecidos",
    "4.1": "01-principios-de-preco",
    "4.2": "02-modelos-de-compra-ec2",
    "4.3": "03-cobranca-de-outros-recursos",
    "4.4": "04-ferramentas-de-custo",
    "4.5": "05-planos-de-suporte",
    "4.6": "06-outros-recursos-de-ajuda",
}

# Ficha (servicos/<categoria>/<nome>.md) de cada serviço.
FICHAS = {
    "computacao": ["ec2", "ec2-auto-scaling", "elastic-load-balancing", "lambda", "ecs", "eks",
                   "fargate", "ecr", "elastic-beanstalk", "lightsail", "batch",
                   "outposts-local-zones-wavelength"],
    "armazenamento": ["s3", "s3-classes-de-armazenamento", "ebs", "efs", "fsx", "storage-gateway",
                      "aws-backup", "elastic-disaster-recovery"],
    "banco-de-dados": ["rds", "aurora", "dynamodb", "elasticache", "memorydb", "redshift",
                       "documentdb", "neptune", "keyspaces-timestream-e-outros"],
    "redes": ["vpc", "vpc-peering-transit-gateway-e-endpoints", "site-to-site-vpn-e-client-vpn",
              "direct-connect", "route-53", "cloudfront", "global-accelerator", "api-gateway"],
    "seguranca": ["iam", "iam-identity-center", "cognito", "directory-service", "kms", "cloudhsm",
                  "certificate-manager", "secrets-manager-e-parameter-store", "shield", "waf",
                  "firewall-manager-e-network-firewall", "guardduty", "inspector", "macie",
                  "detective", "security-hub", "artifact", "audit-manager"],
    "gerenciamento": ["cloudwatch", "cloudtrail", "config", "systems-manager", "cloudformation",
                      "organizations", "control-tower", "service-catalog-e-ram", "trusted-advisor",
                      "health-dashboard", "compute-optimizer-service-quotas-e-license-manager"],
    "analytics": ["athena", "glue", "kinesis", "emr", "quicksight", "opensearch",
                  "lake-formation-msk-e-outros"],
    "ia-ml": ["sagemaker-ai", "bedrock", "amazon-q", "servicos-de-ia-prontos"],
    "integracao": ["sqs", "sns", "eventbridge", "step-functions", "amazon-mq"],
    "desenvolvimento": ["cli-sdk-e-cloudshell", "code-services", "x-ray"],
    "aplicacoes": ["amazon-connect", "ses", "workspaces-e-appstream", "amplify-e-appsync",
                   "iot-core-e-greengrass"],
    "migracao": ["discovery-migration-hub-e-evaluator", "application-migration-service",
                 "dms-e-sct", "snow-family", "datasync-e-transfer-family"],
    "custos": ["cost-explorer", "budgets", "pricing-calculator-cur-e-outras-ferramentas",
               "planos-de-suporte", "recursos-de-ajuda-e-parceiros"],
    "fora-do-escopo": ["midia-e-jogos", "iot-robotica-e-satelite", "desenvolvimento-e-aplicacoes",
                       "rede-e-diretorio", "gerenciamento-e-custos"],
}
CATEGORIA = {nome: cat for cat, nomes in FICHAS.items() for nome in nomes}

# Arquivos escritos à mão começam com este marcador nas primeiras linhas. O gerador não os reescreve
# e falha se uma aula, ficha, página do guia ou resumo estiver sem ele.
AUTORAL = "<!-- autoral -->"

# Abertura de cada capítulo no sumário do README e no índice do domínio:
# (título curto, pergunta do capítulo, percurso, objetivo).
CAPITULOS = {
    "1": ("Conceitos de nuvem", "Por que usar recursos pela internet e como pensar em crescimento, falhas e migração?", "Comece pela ideia de nuvem. Depois estude as vantagens, a arquitetura, as boas práticas e a economia.", "Explique a diferença entre comprar infraestrutura e contratar recursos, e reconheça as vantagens e os limites de cada escolha."),
    "2": ("Segurança e conformidade", "Quem pode acessar os recursos e quem precisa cuidar da segurança?", "Com a base do capítulo 1, separe as responsabilidades. Em seguida, estude identidades, permissões, proteção de dados e acompanhamento do ambiente.", "Diferencie as responsabilidades da AWS e do cliente, explique permissões e escolha ferramentas de proteção e auditoria."),
    "3": ("Tecnologia e serviços", "Como montar uma solução usando computação, dados, armazenamento e redes?", "Use a base de nuvem e segurança para entender as peças de uma aplicação. Leia as aulas em ordem e abra as fichas indicadas dentro de cada uma.", "Relacione uma necessidade ao serviço apropriado e explique o que ele entrega, suas limitações e as decisões que ficam com o cliente."),
    "4": ("Cobrança, preços e suporte", "Como entender a conta, controlar gastos e obter ajuda?", "Agora que você conhece os recursos, estude como o uso vira cobrança, quando compromissos de compra fazem sentido e quais ferramentas ajudam a acompanhar custos.", "Diferencie os modelos de compra e as ferramentas de estimativa, acompanhamento e orçamento, além das opções de suporte."),
}


def caminho_topico(secao):
    return os.path.join("docs", DOMINIOS[secao.split(".")[0]][0], ARQUIVOS[secao] + ".md")


def caminho_ficha(nome):
    return os.path.join("servicos", CATEGORIA[nome], nome + ".md")


def eh_autoral(caminho):
    """Diz se o arquivo traz o marcador de conteúdo autoral nas primeiras linhas."""
    abs_ = caminho if os.path.isabs(caminho) else os.path.join(RAIZ, caminho)
    if not os.path.exists(abs_):
        return False
    with open(abs_) as f:
        return AUTORAL in "".join(f.readlines()[:10])


def rel(origem, destino):
    return os.path.relpath(destino, os.path.dirname(origem)).replace(os.sep, "/")


def titulo_ficha(nome):
    caminho = os.path.join(RAIZ, "servicos", CATEGORIA[nome], nome + ".md")
    if os.path.exists(caminho):
        with open(caminho) as f:
            for linha in f:
                # Fichas autorais começam pelo marcador; o título é a primeira linha "# ".
                if linha.startswith("# "):
                    return linha[2:].strip()
    return nome


def escrever(caminho, conteudo):
    abs_ = os.path.join(RAIZ, caminho)
    os.makedirs(os.path.dirname(abs_), exist_ok=True)
    with open(abs_, "w") as f:
        f.write(conteudo.rstrip() + "\n")


def aulas():
    """Aulas dos domínios 1 a 4, em ordem: [(seção, título, caminho)]. O título vem do próprio arquivo."""
    lista = []
    for sec in sorted(ARQUIVOS, key=lambda s: tuple(int(x) for x in s.split("."))):
        caminho = caminho_topico(sec)
        with open(os.path.join(RAIZ, caminho)) as f:
            m = re.search(r"^# (\d+\.\d+) (.+)$", f.read(), re.M)
        assert m and m.group(1) == sec, f"Aula sem título '# {sec} Título': {caminho}"
        lista.append((sec, m.group(2).strip(), caminho))
    return lista


def conferir_autorais():
    """Falha se algum arquivo de conteúdo perdeu o marcador: nenhum deles tem mais gerador."""
    caminhos = [c for _, _, c in aulas()] + [c for _, _, c in aulas_fundamentos()]
    caminhos += [caminho_ficha(n) for n in CATEGORIA]
    pasta = os.path.join("docs", "00-guia-do-exame")
    caminhos += [os.path.join(pasta, n) for n in sorted(os.listdir(os.path.join(RAIZ, pasta))) if n.endswith(".md")]
    caminhos += [os.path.join("resumos", n) for n in sorted(os.listdir(os.path.join(RAIZ, "resumos"))) if n.endswith(".md")]
    caminhos.append("glossario.md")
    faltando = [c for c in caminhos if not eh_autoral(c)]
    assert not faltando, f"Arquivos sem o marcador {AUTORAL} (o conteúdo é escrito à mão): {faltando}"


def gerar_readmes_dominio(lista):
    for dom, (pasta, nome, peso) in DOMINIOS.items():
        _, pergunta, percurso, objetivo = CAPITULOS[dom]
        linhas = []
        for sec, titulo, caminho in lista:
            if sec.split(".")[0] == dom:
                with open(os.path.join(RAIZ, caminho)) as f:
                    n = len(extrair_cards_revisao(f.read()))
                linhas.append(f"| {sec} | [{titulo}]({os.path.basename(caminho)}) | {n} |")
        escrever(os.path.join("docs", pasta, "README.md"), f"""# {nome}

**Peso na prova:** {peso} das questões pontuadas.

**A pergunta deste capítulo:** {pergunta}

{percurso}

## Aulas

| Aula | Assunto | Perguntas de revisão |
|---|---|---|
{chr(10).join(linhas)}

**Antes de avançar:** {objetivo}

## Para revisar

- [Questões do domínio](../../simulados/questoes/dominio-{dom}.md)
- [Flashcards do domínio](../../flashcards/dominio-{dom}.md)
- [Pares que confundem](../../resumos/comparativos.md), [palavras-chave](../../resumos/palavras-chave.md) e [números que decidem questões](../../resumos/numeros-ancora.md)
- [Controle de progresso](../../progresso.md)
""")

def extrair_cards_revisao(texto):
    """Perguntas de revisão de uma aula autoral.

    Formato: uma seção `## Revisão` (o título pode trazer emoji), com uma pergunta por
    subtítulo `### ` e a resposta comentada em seguida, de preferência recolhida num
    `<details>`. O primeiro parágrafo da resposta vira a resposta do flashcard; o resto
    fica só na aula.
    """
    m = re.search(r"^## [^\n]*\bRevisão\b[^\n]*\n(.*?)(?=\n## |\Z)", texto, re.S | re.M)
    if not m:
        return []
    cards = []
    for bloco in re.split(r"^### ", m.group(1), flags=re.M)[1:]:
        pergunta, _, resposta = bloco.partition("\n")
        resposta = re.sub(r"(?m)^\s*(</?details>|<summary>.*</summary>)\s*$", "", resposta)
        paragrafos = [p.strip() for p in re.split(r"\n\s*\n", resposta.strip()) if p.strip()]
        if pergunta.strip() and paragrafos:
            cards.append((pergunta.strip(), paragrafos[0]))
    return cards


def escrever_flashcards(caminho, titulo, grupos, todas, rotulo):
    """grupos: [(número, título, caminho da aula)]; rotulo(número) devolve as tags do Anki."""
    partes = [f"# 🃏 Flashcards — {titulo}\n",
              "Clique na pergunta para ver a resposta. Gerado a partir da seção *Revisão* "
              "de cada aula (`python3 scripts/gerar_docs.py`).\n"]
    total = 0
    for numero, titulo_aula, aula in grupos:
        with open(os.path.join(RAIZ, aula)) as f:
            cards = extrair_cards_revisao(f.read())
        assert cards, f"Aula sem perguntas na seção Revisão: {aula}"
        partes.append(f"\n## [{numero} {titulo_aula}]({rel(caminho, aula)})\n")
        for q, a in cards:
            total += 1
            todas.append((q, a, rotulo(numero)))
            partes.append(f"<details>\n<summary>{q}</summary>\n\n{a}\n</details>\n")
    partes.insert(2, f"**Total:** {total} cards\n")
    escrever(caminho, "\n".join(partes))


def gerar_flashcards(lista):
    todas = []
    escrever_flashcards("flashcards/capitulo-0.md", "Capítulo 0 — Fundamentos de TI", aulas_fundamentos(), todas,
                        lambda n: f"CLF-C02 capitulo-0 aula-{n.replace('.', '_')}")
    for dom, (_, nome, _) in DOMINIOS.items():
        grupos = [a for a in lista if a[0].split(".")[0] == dom]
        escrever_flashcards(f"flashcards/dominio-{dom}.md", nome, grupos, todas,
                            lambda n, d=dom: f"CLF-C02 dominio-{d} secao-{n.replace('.', '_')}")
    with open(os.path.join(RAIZ, "flashcards", "anki-clf-c02.tsv"), "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        for q, a, tags in todas:
            w.writerow([q, a.replace("**", ""), tags])
    return len(todas)


NOMES_CATEGORIA = {
    "computacao": "🖥️ Computação",
    "armazenamento": "🗄️ Armazenamento",
    "banco-de-dados": "🛢️ Banco de dados",
    "redes": "🌐 Redes e entrega de conteúdo",
    "seguranca": "🔐 Segurança, identidade e compliance",
    "gerenciamento": "⚙️ Gerenciamento e governança",
    "analytics": "📊 Analytics",
    "ia-ml": "🤖 IA e machine learning",
    "integracao": "🔗 Integração de aplicações",
    "desenvolvimento": "🛠️ Ferramentas de desenvolvedor",
    "aplicacoes": "💼 Aplicações de negócio, usuário final e IoT",
    "migracao": "🚚 Migração e transferência",
    "custos": "💰 Custos e suporte",
    "fora-do-escopo": "❌ Fora do escopo da prova (só para referência)",
}


def dado_da_ficha(texto, rotulo, caminho):
    m = re.search(rf"\*\*{rotulo}:\*\* ([^·\n]+)", texto)
    assert m, f"Ficha sem o campo '{rotulo}' no cabeçalho: {caminho}"
    return m.group(1).strip()


def gerar_indice_servicos():
    partes = ["# 🔎 Fichas de serviços AWS\n",
              "Cada ficha aprofunda um serviço que aparece nas aulas. Leia a aula primeiro: ela explica o problema e "
              "o mecanismo, e a ficha acrescenta as opções, os limites, o custo e com o que o serviço costuma ser "
              "confundido. As aulas indicam no topo as fichas de cada assunto.\n",
              "> Coluna *Escopo* ([lista oficial](../docs/00-guia-do-exame/escopo-oficial.md)): ✅ no escopo · "
              "🔀 parte no escopo, parte fora · ⚪ não aparece na lista · ❌ fora do escopo.\n>\n"
              "> Coluna *Grupo*: **núcleo** é a ficha completa de um serviço central de alguma aula, que também "
              "entra no caderno de consulta impresso; **complementar** é a versão curta de um serviço periférico "
              "no escopo; **referência** é a versão curta de um serviço fora da lista oficial, para reconhecer "
              "alternativas erradas.\n>\n> "
              "Modelo para novas fichas: [`templates/servico.md`](../templates/servico.md).\n"]
    total = 0
    for cat, nomes in FICHAS.items():
        partes.append(f"\n## {NOMES_CATEGORIA[cat]}\n\n| Ficha | Escopo | Grupo | Em uma frase |\n|---|---|---|---|")
        for nome in nomes:
            caminho = os.path.join(RAIZ, "servicos", cat, nome + ".md")
            with open(caminho) as f:
                texto = f.read()
            frase = re.search(r"\*\*Em uma frase:\*\* (.+)", texto)
            frase = frase.group(1).strip() if frase else ""
            escopo = dado_da_ficha(texto, "Escopo oficial", caminho).split()[0]
            grupo = dado_da_ficha(texto, "Ficha", caminho)
            partes.append(f"| [{titulo_ficha(nome)}]({cat}/{nome}.md) | {escopo} | {grupo} | {frase[:1].upper() + frase[1:]} |")
            total += 1
    escrever("servicos/README.md", "\n".join(partes))
    return total


INDICE_INI = "<!-- indice:inicio -->"
INDICE_FIM = "<!-- indice:fim -->"
CONTEUDO_INI = "<!-- conteudo:inicio -->"
CONTEUDO_FIM = "<!-- conteudo:fim -->"


def nome_curto(titulo):
    """'Amazon EC2 (Elastic Compute Cloud)' -> 'Amazon EC2'."""
    return titulo.split(" (")[0]


def contar_linhas_tabela(caminho):
    with open(os.path.join(RAIZ, caminho)) as f:
        linhas = [l for l in f if l.startswith("|")]
    separador = re.compile(r"^\|\s*:?-{3}")
    # Conta as linhas de dados: descarta separadores e o cabeçalho de cada tabela.
    cabecalhos = sum(1 for i, l in enumerate(linhas[1:], 1) if separador.match(l) and not separador.match(linhas[i - 1]))
    return len([l for l in linhas if not separador.match(l)]) - cabecalhos


def substituir_bloco(texto, ini, fim, bloco):
    padrao = re.escape(ini) + r".*?" + re.escape(fim)
    assert re.search(padrao, texto, re.S), f"Marcadores {ini} … {fim} não encontrados no README.md"
    return re.sub(padrao, lambda _: bloco, texto, flags=re.S)


def bloco_conteudo(total_cards, total_aulas):
    from banco_questoes import QUESTOES
    total_fichas = sum(len(n) for n in FICHAS.values())
    fora = len(FICHAS["fora-do-escopo"])
    linhas = [
        CONTEUDO_INI,
        "| Material | O que é | Quando usar |",
        "|---|---|---|",
        f"| 📖 [Tópicos da prova](#sumário-da-apostila) | **{total_aulas} tópicos** que cobrem os 4 domínios, "
        "com conceitos explicados, casos resolvidos e perguntas de revisão | Estudo principal, na ordem do roteiro |",
        f"| 🔎 [Fichas de serviços](#caderno-de-serviços) | **{total_fichas} fichas** (uma por serviço ou família), "
        f"com funcionamento, opções, limites, segurança, custo e casos resolvidos; {fora} reúnem serviços **fora da prova** | Quando um tópico citar o serviço, ou para tirar dúvidas |",
        f"| 🃏 [Flashcards](flashcards/README.md) | **{total_cards} perguntas e respostas** por capítulo, também em arquivo para o Anki | Todos os dias, para memorizar |",
        f"| ❓ [Questões por domínio](simulados/questoes/README.md) | **{len(QUESTOES)} questões** no formato da prova, agrupadas por tópico, com explicação | Ao terminar cada domínio |",
        f"| ⚖️ [Pares que confundem](resumos/comparativos.md) | **{contar_linhas_tabela('resumos/comparativos.md')} pares** de serviços parecidos e a diferença em uma linha | Revisão final |",
        f"| 🔑 [Palavras-chave → serviço](resumos/palavras-chave.md) | **{contar_linhas_tabela('resumos/palavras-chave.md')} gatilhos** do enunciado que apontam a resposta | Revisão final |",
        f"| 📌 [Números-âncora](resumos/numeros-ancora.md) | Os números que decidem a resposta (e o que **não** precisa decorar) | Revisão final |",
        f"| 📖 [Glossário](glossario.md) | **{contar_linhas_tabela('glossario.md')} termos** e siglas | Sempre que travar num termo |",
        "| ✅ [Progresso](progresso.md) | Checklist de todos os tópicos e marcos | Para acompanhar o seu avanço |",
        "| 🧪 [Labs](labs/README.md) | Exercícios práticos no console AWS, com cuidado de custos | Opcional, para fixar |",
        CONTEUDO_FIM,
    ]
    return "\n".join(linhas)


PASTA_FUNDAMENTOS = os.path.join("docs", "fundamentos")


def aulas_fundamentos():
    """Aulas autorais do capítulo 0, na ordem dos arquivos: [(número, título, caminho)]."""
    pasta = os.path.join(RAIZ, PASTA_FUNDAMENTOS)
    if not os.path.isdir(pasta):
        return []
    aulas = []
    for nome in sorted(os.listdir(pasta)):
        if not nome.endswith(".md") or nome == "README.md":
            continue
        caminho = os.path.join(PASTA_FUNDAMENTOS, nome)
        with open(os.path.join(RAIZ, caminho)) as f:
            m = re.search(r"^# (0\.\d+) (.+)$", f.read(), re.M)
        assert m, f"Aula do capítulo 0 sem título '# 0.x Título': {caminho}"
        aulas.append((m.group(1), m.group(2).strip(), caminho.replace(os.sep, "/")))
    return aulas


def bloco_capitulo_zero():
    aulas = aulas_fundamentos()
    if not aulas:
        return []
    linhas = ["### Capítulo 0: Fundamentos de TI", "",
              "**A pergunta deste capítulo:** O que são servidor, rede, dados, API e criptografia, as peças sobre as quais a AWS oferece serviços?", "",
              "Para quem nunca trabalhou com TI. Se você já conhece esses termos, leia só os resumos no fim de cada aula e siga para o capítulo 1.", "",
              f"Não corresponde a um domínio da prova. [Apresentação do capítulo]({PASTA_FUNDAMENTOS}/README.md).", "",
              "| Aula | Assunto |", "|---|---|"]
    linhas += [f"| {numero} | [{titulo}]({caminho}) |" for numero, titulo, caminho in aulas]
    linhas += ["", f"**Comece pela [aula {aulas[0][0]}]({aulas[0][2]}).**", "",
               "**Confira seu entendimento:** [flashcards do capítulo 0](flashcards/capitulo-0.md).", "",
               "**Próxima etapa:** [capítulo 1](#capítulo-1-conceitos-de-nuvem).", ""]
    return linhas


def bloco_indice(lista):
    linhas = [INDICE_INI, "## Sumário da apostila", "",
              "Leia do capítulo 0 ao 4. Os números das aulas indicam sua posição: **3.3**, por exemplo, é a terceira aula do capítulo 3. Clique no título para abrir o texto.", ""]
    linhas += bloco_capitulo_zero()
    for dom, (pasta, nome, peso) in DOMINIOS.items():
        titulo, pergunta, percurso, objetivo = CAPITULOS[dom]
        linhas += [f"### Capítulo {dom}: {titulo}", "", f"**A pergunta deste capítulo:** {pergunta}", "", percurso, "",
                   f"Corresponde ao {nome.lower()} — **{peso} da prova**. [Apresentação do capítulo](docs/{pasta}/README.md).", "",
                   "| Aula | Assunto |", "|---|---|"]
        do_dominio = [(sec, titulo_aula) for sec, titulo_aula, _ in lista if sec.split(".")[0] == dom]
        linhas += [f"| {sec} | [{titulo_aula}]({caminho_topico(sec)}) |" for sec, titulo_aula in do_dominio]
        primeira = do_dominio[0][0]
        linhas += ["", f"**Comece pela [aula {primeira}]({caminho_topico(primeira)}).**", "", f"**Antes de avançar:** {objetivo}", "",
                   f"**Confira seu entendimento:** [questões do capítulo {dom}](simulados/questoes/dominio-{dom}.md) · [flashcards do capítulo {dom}](flashcards/dominio-{dom}.md).", ""]
        if int(dom) < 4:
            linhas += [f"**Próxima etapa:** [capítulo {int(dom) + 1}](#capítulo-{int(dom) + 1}-" + {"1": "segurança-e-conformidade", "2": "tecnologia-e-serviços", "3": "cobrança-preços-e-suporte"}[dom] + ").", ""]
        else:
            linhas += ["**Próxima etapa:** [pratique e revise](#pratique-e-revise).", ""]
    linhas += ["## Caderno de serviços", "",
               "As fichas são leituras de aprofundamento. Quando uma aula citar um serviço, abra a ficha indicada nela; depois retorne à aula. Se você já conhece o nome do serviço e quer consultá-lo, abra uma categoria abaixo.", "",
               "Cada ficha explica o problema resolvido, o funcionamento, as opções, os limites, a segurança, o custo e um caso resolvido. O status da prova aparece na própria ficha: consulte-o antes de dedicar tempo a um serviço.", "",
               "Exemplos: [EC2 — computadores virtuais](servicos/computacao/ec2.md) · [S3 — armazenamento de objetos](servicos/armazenamento/s3.md) · [IAM — identidades e permissões](servicos/seguranca/iam.md).", "",
               "Você também pode abrir o [índice completo das fichas, com descrições e escopo](servicos/README.md).", ""]
    for cat, nomes in FICHAS.items():
        nome = NOMES_CATEGORIA[cat]
        linhas += ["<details>", f"<summary>{nome} — {len(nomes)} fichas (clique para abrir)</summary>", ""]
        if cat == "fora-do-escopo":
            linhas += ["Leitura complementar; estas fichas reúnem serviços fora do escopo da prova.", ""]
        for n in nomes:
            linhas.append(f"- [{nome_curto(titulo_ficha(n))}](servicos/{cat}/{n}.md)")
        linhas += ["", "</details>", ""]
    linhas.append(INDICE_FIM)
    return "\n".join(linhas)


def gerar_indice_readme(lista, total_cards):
    """Atualiza no README.md os blocos gerados: tabela de materiais e sumário de aulas e fichas."""
    caminho = os.path.join(RAIZ, "README.md")
    with open(caminho) as f:
        texto = f.read()
    texto = substituir_bloco(texto, CONTEUDO_INI, CONTEUDO_FIM, bloco_conteudo(total_cards, len(lista)))
    texto = substituir_bloco(texto, INDICE_INI, INDICE_FIM, bloco_indice(lista))
    with open(caminho, "w") as f:
        f.write(texto)


def main():
    conferir_autorais()
    lista = aulas()
    gerar_readmes_dominio(lista)
    total = gerar_flashcards(lista)
    fichas = gerar_indice_servicos()
    gerar_indice_readme(lista, total)
    print(f"{len(lista)} aulas, {total} flashcards e índice de {fichas} fichas gerados.")


if __name__ == "__main__":
    main()
