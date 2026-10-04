#!/usr/bin/env python3
"""Gera docs/, resumos/ e flashcards/ a partir de fontes/guia-completo-clf-c02.md.

Uso: python3 scripts/gerar_docs.py

ATENÇÃO: sobrescreve os arquivos gerados. Em cada tópico, dois blocos são preservados
entre execuções: <!-- extra:inicio -->…<!-- extra:fim --> (complementos) e
<!-- notas:inicio -->…<!-- notas:fim --> (anotações pessoais).
"""
import csv
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUIA = os.path.join(RAIZ, "fontes", "guia-completo-clf-c02.md")

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
               "planos-de-suporte"],
}
CATEGORIA = {nome: cat for cat, nomes in FICHAS.items() for nome in nomes}

FICHAS_POR_TOPICO = {
    "1.4": ["trusted-advisor"],
    "1.6": ["application-migration-service", "dms-e-sct"],
    "1.7": ["compute-optimizer-service-quotas-e-license-manager", "pricing-calculator-cur-e-outras-ferramentas"],
    "2.1": ["ec2", "rds", "lambda", "s3", "dynamodb"],
    "2.2": ["iam"],
    "2.3": ["iam", "iam-identity-center", "cognito", "directory-service", "secrets-manager-e-parameter-store"],
    "2.4": ["organizations", "control-tower", "service-catalog-e-ram"],
    "2.5": ["kms", "cloudhsm", "certificate-manager", "s3"],
    "2.6": ["artifact", "audit-manager", "config"],
    "2.7": ["cloudtrail", "config", "cloudwatch", "vpc", "health-dashboard"],
    "2.8": ["vpc", "shield", "waf", "firewall-manager-e-network-firewall"],
    "2.9": ["guardduty", "inspector", "macie", "detective", "security-hub", "trusted-advisor"],
    "2.10": ["guardduty", "security-hub"],
    "3.1": ["cli-sdk-e-cloudshell", "cloudformation", "site-to-site-vpn-e-client-vpn", "direct-connect"],
    "3.2": ["outposts-local-zones-wavelength", "cloudfront", "global-accelerator"],
    "3.3": ["ec2", "ebs"],
    "3.4": ["ec2-auto-scaling", "elastic-load-balancing"],
    "3.5": ["ecs", "eks", "fargate", "ecr", "lambda"],
    "3.6": ["elastic-beanstalk", "lightsail", "batch", "outposts-local-zones-wavelength"],
    "3.7": ["rds", "aurora", "dynamodb", "elasticache", "memorydb", "redshift", "documentdb",
            "neptune", "keyspaces-timestream-e-outros"],
    "3.8": ["s3", "s3-classes-de-armazenamento"],
    "3.9": ["ebs", "efs", "fsx", "storage-gateway", "aws-backup", "elastic-disaster-recovery",
            "snow-family", "datasync-e-transfer-family"],
    "3.10": ["vpc", "vpc-peering-transit-gateway-e-endpoints", "site-to-site-vpn-e-client-vpn",
             "direct-connect", "route-53", "cloudfront", "global-accelerator", "api-gateway"],
    "3.11": ["athena", "glue", "kinesis", "emr", "quicksight", "opensearch", "redshift",
             "lake-formation-msk-e-outros"],
    "3.12": ["sagemaker-ai", "bedrock", "amazon-q", "servicos-de-ia-prontos"],
    "3.13": ["sqs", "sns", "eventbridge", "step-functions", "amazon-mq"],
    "3.14": ["amazon-connect", "ses", "workspaces-e-appstream", "amplify-e-appsync",
             "iot-core-e-greengrass"],
    "3.15": ["code-services", "x-ray", "cli-sdk-e-cloudshell"],
    "3.16": ["cloudformation", "systems-manager", "health-dashboard", "trusted-advisor",
             "compute-optimizer-service-quotas-e-license-manager", "organizations"],
    "3.17": ["discovery-migration-hub-e-evaluator", "application-migration-service", "dms-e-sct",
             "snow-family", "datasync-e-transfer-family"],
    "3.18": ["lake-formation-msk-e-outros", "amazon-mq", "firewall-manager-e-network-firewall",
             "keyspaces-timestream-e-outros", "servicos-de-ia-prontos"],
    "4.2": ["ec2"],
    "4.3": ["s3", "ebs", "lambda"],
    "4.4": ["cost-explorer", "budgets", "pricing-calculator-cur-e-outras-ferramentas"],
    "4.5": ["planos-de-suporte", "trusted-advisor"],
    "4.6": ["planos-de-suporte"],
}

EXTRA_INI = "<!-- extra:inicio -->"
EXTRA_FIM = "<!-- extra:fim -->"
NOTAS_INI = "<!-- notas:inicio -->"
NOTAS_FIM = "<!-- notas:fim -->"
NOTAS_VAZIO = ("## 📝 Minhas anotações\n\n"
               "<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->")


def caminho_topico(secao):
    return os.path.join("docs", DOMINIOS[secao.split(".")[0]][0], ARQUIVOS[secao] + ".md")


def rel(origem, destino):
    return os.path.relpath(destino, os.path.dirname(origem)).replace(os.sep, "/")


def titulo_ficha(nome):
    caminho = os.path.join(RAIZ, "servicos", CATEGORIA[nome], nome + ".md")
    if os.path.exists(caminho):
        with open(caminho) as f:
            primeira = f.readline().strip()
        if primeira.startswith("# "):
            return primeira[2:]
    return nome


def limpar(texto):
    # Corrige negrito duplicado vindo da exportação ("**Nome****:**" -> "**Nome:**").
    return texto.replace("****:**", ":**")


def linkar_referencias(texto, origem):
    def troca(m):
        sec = m.group(2)
        if sec not in ARQUIVOS:
            return m.group(0)
        return f"{m.group(1)}[{sec}]({rel(origem, caminho_topico(sec))})"

    texto = re.sub(r"(\b[Vv]er\b[^;)\n]{0,40}?)(\b[1-4]\.\d{1,2}\b)", troca, texto)
    texto = re.sub(r"(cost allocation tags em )(4\.4)", troca, texto)
    dom4 = os.path.join("docs", DOMINIOS["4"][0], "README.md")
    texto = texto.replace("(ver Domínio 4)", f"(ver [Domínio 4]({rel(origem, dom4)}))")
    return texto


def converter_marcadores(texto):
    linhas = []
    for linha in texto.split("\n"):
        m = re.match(r"^\*\*(Perguntas típicas|Complemento)(.*?):\*\*\s*$", linha)
        if m:
            icone = "❓" if m.group(1) == "Perguntas típicas" else "➕"
            linhas.append(f"## {icone} {m.group(1)}{m.group(2)}")
        else:
            linhas.append(linha)
    return "\n".join(linhas)


def ler_bloco(caminho_abs, ini, fim, padrao=""):
    """Devolve o bloco preservado entre os marcadores (ou um bloco novo com o conteúdo padrão)."""
    novo = f"{ini}\n{padrao}\n{fim}" if padrao else f"{ini}\n{fim}"
    if not os.path.exists(caminho_abs):
        return novo
    with open(caminho_abs) as f:
        atual = f.read()
    m = re.search(re.escape(ini) + r".*?" + re.escape(fim), atual, re.S)
    return m.group(0) if m else novo


def escrever(caminho, conteudo):
    abs_ = os.path.join(RAIZ, caminho)
    os.makedirs(os.path.dirname(abs_), exist_ok=True)
    with open(abs_, "w") as f:
        f.write(conteudo.rstrip() + "\n")


def parse_guia():
    with open(GUIA) as f:
        linhas = limpar(f.read()).split("\n")

    secoes = {}      # "1.1" -> (titulo, corpo)
    intros = {}      # "1" -> [parágrafos de introdução]
    extras = {}      # "menos", "pares", "palavras", "visao"
    atual = None
    buf = []

    def fechar():
        if atual is None:
            return
        tipo, chave, titulo = atual
        corpo = "\n".join(buf).strip()
        if tipo == "secao":
            secoes[chave] = (titulo, corpo)
        elif tipo == "intro":
            if corpo:
                intros.setdefault(chave, []).append(corpo)
        else:
            extras[chave] = corpo

    for linha in linhas:
        m3 = re.match(r"^### (\d)\.(\d+) (.*)$", linha)
        m2 = re.match(r"^## (.*)$", linha)
        if m3:
            fechar()
            atual = ("secao", f"{m3.group(1)}.{m3.group(2)}", m3.group(3).strip())
            buf = []
        elif m2:
            fechar()
            nome = m2.group(1)
            md = re.match(r"Domínio (\d)", nome)
            if md:
                atual = ("intro", md.group(1), nome)
            elif nome.startswith("Visão geral"):
                atual = ("extra", "visao", nome)
            elif nome.startswith("Serviços menos conhecidos"):
                atual = ("secao", "3.18", "Serviços menos conhecidos que podem aparecer")
            elif nome.startswith("Pares que confundem"):
                atual = ("extra", "pares_intro", nome)
            elif nome.startswith("Fontes"):
                atual = ("extra", "fontes", nome)
            else:
                atual = None
            buf = []
        elif re.match(r"^### (Pares que mais confundem|Palavras-chave)", linha):
            fechar()
            chave = "pares" if "Pares" in linha else "palavras"
            atual = ("extra", chave, linha[4:])
            buf = []
        else:
            buf.append(linha)
    fechar()
    return secoes, intros, extras


def gerar_topicos(secoes):
    ordem = sorted(secoes, key=lambda s: tuple(int(x) for x in s.split(".")))
    for i, sec in enumerate(ordem):
        titulo, corpo = secoes[sec]
        dom = sec.split(".")[0]
        pasta, nome_dom, peso = DOMINIOS[dom]
        caminho = caminho_topico(sec)
        if sec == "3.18":
            # Subtítulos ### viram ## no arquivo próprio.
            corpo = re.sub(r"^### ", "## ", corpo, flags=re.M)
        corpo = linkar_referencias(converter_marcadores(corpo), caminho)
        corpo = re.sub(r"^## ❓ Perguntas típicas", "## ❓ Perguntas típicas\n\n> Também estão nos [flashcards]("
                       + rel(caminho, f"flashcards/dominio-{dom}.md") + ").", corpo, count=1, flags=re.M)

        nav = []
        irmaos = [s for s in ordem if s.split(".")[0] == dom]
        j = irmaos.index(sec)
        if j > 0:
            nav.append(f"⬅️ [{irmaos[j-1]} {secoes[irmaos[j-1]][0]}]({ARQUIVOS[irmaos[j-1]]}.md)")
        nav.append("🏠 [Índice do domínio](README.md)")
        if j < len(irmaos) - 1:
            nav.append(f"[{irmaos[j+1]} {secoes[irmaos[j+1]][0]}]({ARQUIVOS[irmaos[j+1]]}.md) ➡️")

        fichas = FICHAS_POR_TOPICO.get(sec, [])
        bloco_fichas = ""
        if fichas:
            links = " · ".join(
                f"[{titulo_ficha(n)}]({rel(caminho, os.path.join('servicos', CATEGORIA[n], n + '.md'))})"
                for n in fichas)
            bloco_fichas = f"\n> 🔎 **Fichas detalhadas:** {links}\n"

        rotulo = sec if sec != "3.18" else "3.18"
        extra = ler_bloco(os.path.join(RAIZ, caminho), EXTRA_INI, EXTRA_FIM)
        notas = ler_bloco(os.path.join(RAIZ, caminho), NOTAS_INI, NOTAS_FIM, NOTAS_VAZIO)
        conteudo = f"""# {rotulo} {titulo}

> **{nome_dom} ({peso})** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->
{bloco_fichas}
{" · ".join(nav)}

---

## 📖 Conteúdo

{corpo}

{extra}

{notas}

---

{" · ".join(nav)}
"""
        escrever(caminho, conteudo)
    return ordem


def gerar_readmes_dominio(secoes, intros, ordem):
    for dom, (pasta, nome, peso) in DOMINIOS.items():
        caminho = os.path.join("docs", pasta, "README.md")
        linhas = []
        for sec in ordem:
            if sec.split(".")[0] != dom:
                continue
            titulo, corpo = secoes[sec]
            n = len(extrair_cards(corpo))
            linhas.append(f"| {sec} | [{titulo}]({ARQUIVOS[sec]}.md) | {n} | 🔴 |")
        blocos = intros.get(dom, [])
        if len(blocos) > 1:
            intro = "**Como o conteúdo está dividido:**\n\n" + "\n".join(
                f"- **Parte {i}:** {b}" for i, b in enumerate(blocos, 1))
        else:
            intro = "".join(blocos)
        escrever(caminho, f"""# {nome}

**Peso na prova:** {peso} das questões pontuadas

{intro}

## Tópicos

| # | Tópico | Perguntas típicas | Status |
|---|---|---|---|
{chr(10).join(linhas)}

> Legenda: 🔴 Não iniciado · 🟡 Em andamento · 🟢 Revisado

## Revisão rápida do domínio

- 🃏 [Flashcards do domínio](../../flashcards/dominio-{dom}.md)
- ⚖️ [Pares que confundem](../../resumos/comparativos.md)
- 🔑 [Palavras-chave → serviço](../../resumos/palavras-chave.md)
- 📌 [Números-âncora](../../resumos/numeros-ancora.md)
""")


def extrair_cards(corpo):
    m = re.search(r"\*\*Perguntas típicas:\*\*(.*?)(?=\n\*\*[^*]+:\*\*|\n## |\Z)", corpo, re.S)
    if not m:
        m = re.search(r"## ❓ Perguntas típicas(.*?)(?=\n## |\Z)", corpo, re.S)
    if not m:
        return []
    cards = []
    for linha in m.group(1).split("\n"):
        if not linha.startswith("- "):
            continue
        pares = re.findall(r"\"([^\"]+)\"\s*→\s*([^\"]+?)(?=\s*\"|$)", linha)
        cards.extend((q.strip(), a.strip()) for q, a in pares)
    return cards


def gerar_flashcards(secoes, ordem):
    todas = []
    for dom, (pasta, nome, peso) in DOMINIOS.items():
        partes = [f"# 🃏 Flashcards — {nome}\n",
                  "Clique na pergunta para ver a resposta. Gerado a partir das *Perguntas típicas* "
                  "de cada tópico (`python3 scripts/gerar_docs.py`).\n"]
        total = 0
        for sec in ordem:
            if sec.split(".")[0] != dom:
                continue
            titulo, corpo = secoes[sec]
            cards = extrair_cards(corpo)
            if not cards:
                continue
            link = rel(f"flashcards/dominio-{dom}.md", caminho_topico(sec))
            partes.append(f"\n## [{sec} {titulo}]({link})\n")
            for q, a in cards:
                total += 1
                todas.append((q, a, f"CLF-C02 dominio-{dom} secao-{sec.replace('.', '_')}"))
                partes.append(f"<details>\n<summary>{q}</summary>\n\n{a}\n</details>\n")
        partes.insert(2, f"**Total:** {total} cards\n")
        escrever(f"flashcards/dominio-{dom}.md", "\n".join(partes))

    with open(os.path.join(RAIZ, "flashcards", "anki-clf-c02.tsv"), "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        for q, a, tags in todas:
            w.writerow([q, a.replace("**", ""), tags])
    return len(todas)


def gerar_resumos(extras):
    escrever("resumos/comparativos.md", f"""# ⚖️ Pares que confundem

{extras.get('pares_intro', '').strip()}

{extras['pares'].strip()}

> Veja também: [palavras-chave → serviço](palavras-chave.md) · [números-âncora](numeros-ancora.md)
""")
    escrever("resumos/palavras-chave.md", f"""# 🔑 Palavras-chave que apontam para a resposta

As questões oficiais podem vir em português ou inglês; os termos abaixo aparecem nas duas versões.

{extras['palavras'].strip()}

> Veja também: [pares que confundem](comparativos.md) · [números-âncora](numeros-ancora.md)
""")


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
}


def gerar_indice_servicos():
    partes = ["# 🔎 Fichas de serviços AWS\n",
              "Uma ficha por serviço (ou família de serviços), com o que cai na prova e o que vai além: "
              "componentes, configurações, limites, cobrança, responsabilidade compartilhada, "
              "atualizações 2025-2026, pegadinhas e perguntas típicas.\n",
              "> Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar. "
              "Modelo para novas fichas: [`templates/servico.md`](../templates/servico.md).\n"]
    total = 0
    for cat, nomes in FICHAS.items():
        partes.append(f"\n## {NOMES_CATEGORIA[cat]}\n\n| Ficha | Em uma frase |\n|---|---|")
        for nome in nomes:
            caminho = os.path.join(RAIZ, "servicos", cat, nome + ".md")
            with open(caminho) as f:
                texto = f.read()
            frase = re.search(r"\*\*Em uma frase:\*\* (.+)", texto)
            frase = frase.group(1).strip() if frase else ""
            partes.append(f"| [{titulo_ficha(nome)}]({cat}/{nome}.md) | {frase[:1].upper() + frase[1:]} |")
            total += 1
    escrever("servicos/README.md", "\n".join(partes))
    return total


INDICE_INI = "<!-- indice:inicio -->"
INDICE_FIM = "<!-- indice:fim -->"


def gerar_indice_readme(secoes, ordem):
    """Atualiza no README.md o índice com link direto para cada tópico e cada ficha."""
    linhas = [INDICE_INI, "## 🧭 Índice completo", "",
              "Links diretos para todos os tópicos e fichas (clique para expandir). "
              "Gerado por `scripts/gerar_docs.py`.", "", "### Tópicos do exame", ""]
    for dom, (pasta, nome, peso) in DOMINIOS.items():
        linhas += ["<details>", f"<summary><b>{nome} ({peso})</b></summary>", ""]
        for sec in ordem:
            if sec.split(".")[0] == dom:
                linhas.append(f"- [{sec} {secoes[sec][0]}]({caminho_topico(sec)})")
        linhas += ["", "</details>", ""]
    linhas += ["### Fichas de serviços", ""]
    for cat, nomes in FICHAS.items():
        linhas += ["<details>", f"<summary><b>{NOMES_CATEGORIA[cat]}</b> ({len(nomes)})</summary>", ""]
        linhas += [f"- [{titulo_ficha(n)}](servicos/{cat}/{n}.md)" for n in nomes]
        linhas += ["", "</details>", ""]
    linhas += ["### Outros materiais", "",
               "- [Guia do exame](docs/00-guia-do-exame/README.md) · [Plano de estudos](docs/00-guia-do-exame/plano-de-estudos.md) · [O que mudou em 2025-2026](docs/00-guia-do-exame/atualizacoes-2025-2026.md)",
               "- Flashcards: " + " · ".join(f"[Domínio {d}](flashcards/dominio-{d}.md)" for d in DOMINIOS) + " · [Anki (TSV)](flashcards/anki-clf-c02.tsv)",
               "- Resumos: [Pares que confundem](resumos/comparativos.md) · [Palavras-chave](resumos/palavras-chave.md) · [Números-âncora](resumos/numeros-ancora.md)",
               "- [Glossário](glossario.md) · [Progresso](progresso.md) · [Simulados](simulados/README.md) · [Erros recorrentes](simulados/erros-recorrentes.md) · [Labs](labs/README.md) · [Links úteis](recursos/links-uteis.md)",
               "- Fontes: [Guia completo](fontes/guia-completo-clf-c02.md) · [Pesquisa 2025-2026](fontes/pesquisa-atualizacoes-2025-2026.md)",
               "- Modelos: [Tópico](templates/topico.md) · [Ficha de serviço](templates/servico.md) · [Simulado](templates/simulado.md)",
               INDICE_FIM]
    bloco = "\n".join(linhas)
    caminho = os.path.join(RAIZ, "README.md")
    with open(caminho) as f:
        atual = f.read()
    padrao = re.escape(INDICE_INI) + r".*?" + re.escape(INDICE_FIM)
    if re.search(padrao, atual, re.S):
        novo = re.sub(padrao, lambda _: bloco, atual, flags=re.S)
    else:
        # Primeira execução: insere antes da seção de revisão.
        novo = atual.replace("## 🧠 Revisão", bloco + "\n\n## 🧠 Revisão", 1)
    with open(caminho, "w") as f:
        f.write(novo)


def main():
    secoes, intros, extras = parse_guia()
    ordem = gerar_topicos(secoes)
    gerar_readmes_dominio(secoes, intros, ordem)
    total = gerar_flashcards(secoes, ordem)
    gerar_resumos(extras)
    fichas = gerar_indice_servicos()
    gerar_indice_readme(secoes, ordem)
    print(f"{len(ordem)} tópicos, {total} flashcards e índice de {fichas} fichas gerados.")


if __name__ == "__main__":
    main()
