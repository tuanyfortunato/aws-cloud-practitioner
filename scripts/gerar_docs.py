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
               "planos-de-suporte", "recursos-de-ajuda-e-parceiros"],
    "fora-do-escopo": ["midia-e-jogos", "iot-robotica-e-satelite", "desenvolvimento-e-aplicacoes",
                       "rede-e-diretorio", "gerenciamento-e-custos"],
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
    "2.10": ["guardduty", "security-hub", "recursos-de-ajuda-e-parceiros"],
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
             "keyspaces-timestream-e-outros", "servicos-de-ia-prontos", "midia-e-jogos",
             "iot-robotica-e-satelite", "desenvolvimento-e-aplicacoes", "rede-e-diretorio",
             "gerenciamento-e-custos"],
    "4.2": ["ec2"],
    "4.3": ["s3", "ebs", "lambda"],
    "4.4": ["cost-explorer", "budgets", "pricing-calculator-cur-e-outras-ferramentas"],
    "4.5": ["planos-de-suporte", "trusted-advisor"],
    "4.6": ["recursos-de-ajuda-e-parceiros", "planos-de-suporte"],
}

# Avisos exibidos no topo de tópicos cujo conteúdo-base (fontes/guia) ficou desatualizado em relação
# ao exam guide oficial (verificação de 04/10/2026).
ESCOPO_LINK = "docs/00-guia-do-exame/escopo-oficial.md"
AVISOS = {
    "3.2": "Na lista oficial atual, **Outposts** está no escopo, **Local Zones** não aparece e **Wavelength** está **fora do escopo**.",
    "3.9": "A **família Snow** e o **DataSync** não aparecem na lista oficial atual (o Snowball Edge está fechado a novos clientes); **FSx for Lustre** e **Transfer Family** estão **fora do escopo**.",
    "3.12": "No escopo: SageMaker AI, Amazon Q, Comprehend, Lex, Polly, Rekognition, Textract, Transcribe e Translate. **Bedrock** e **Kendra** não aparecem na lista atual; **Personalize** e **Fraud Detector** estão **fora do escopo**.",
    "3.14": "No escopo: Connect, SES, AppStream 2.0, WorkSpaces, WorkSpaces Secure Browser, **Amplify** e **IoT Core**. AppSync não aparece na lista atual.",
    "3.15": "No escopo só ficaram **AWS CLI, CodeBuild, CodePipeline e X-Ray**. CodeDeploy, CodeArtifact e CloudShell estão **fora do escopo**; Cloud9, CodeCommit e CodeStar não aparecem.",
    "3.17": "**Migration Hub** e **Application Discovery Service** continuam no escopo, mas estão fechados a novos clientes desde 07/11/2025. **Transfer Family** está **fora do escopo**; Snow e DataSync não aparecem.",
    "3.18": "Vários serviços desta seção estão **fora do escopo** oficial (MSK, AppFlow, Data Exchange, Keyspaces, MemoryDB, Personalize, Device Farm, Network Firewall, AWS IQ). Use-os para reconhecer distratores.",
    "4.5": "O exam guide atual (task 4.3) cobra os **planos novos: Basic, Business Support+, Enterprise e Unified Operations**. O conteúdo abaixo descreve o modelo clássico (válido até 01/01/2027). Estude primeiro a tabela de planos novos na seção de atualizações e na [ficha de planos de suporte](../../servicos/custos/planos-de-suporte.md).",
    "4.6": "**AWS IQ**, **AWS Activate** e **AWS Managed Services** estão **fora do escopo** oficial. A task 4.3 cita: Trust and Safety, APN, Marketplace, Professional Services, Prescriptive Guidance, Knowledge Center e re:Post.",
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

        rotulo = sec
        aviso = ""
        if sec in AVISOS:
            aviso = (f"\n> ⚠️ **Atualização do exam guide (verificado em 04/10/2026):** {AVISOS[sec]} "
                     f"[Ver escopo oficial]({rel(caminho, ESCOPO_LINK)}).\n")
        extra = ler_bloco(os.path.join(RAIZ, caminho), EXTRA_INI, EXTRA_FIM)
        notas = ler_bloco(os.path.join(RAIZ, caminho), NOTAS_INI, NOTAS_FIM, NOTAS_VAZIO)
        conteudo = f"""# {rotulo} {titulo}

> **{nome_dom} ({peso})** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->
{bloco_fichas}{aviso}
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



# Status de cada ficha na lista oficial de serviços da CLF-C02 (verificada em 04/10/2026,
# ver docs/00-guia-do-exame/escopo-oficial.md). ✅ no escopo · 🔀 parcial · ⚪ não listado · ❌ fora do escopo.
ESCOPO = {
    "ec2": "✅ No escopo",
    "ec2-auto-scaling": "✅ No escopo (AWS Auto Scaling)",
    "elastic-load-balancing": "✅ Cobrado junto com o EC2 (não aparece como item separado na lista)",
    "lambda": "✅ No escopo", "ecs": "✅ No escopo", "eks": "✅ No escopo", "fargate": "✅ No escopo",
    "ecr": "✅ No escopo", "elastic-beanstalk": "✅ No escopo", "lightsail": "✅ No escopo", "batch": "✅ No escopo",
    "outposts-local-zones-wavelength": "🔀 Outposts ✅ · Local Zones ⚪ não listado · Wavelength ❌ fora do escopo",
    "s3": "✅ No escopo", "s3-classes-de-armazenamento": "✅ No escopo (S3 e S3 Glacier)",
    "ebs": "✅ No escopo", "efs": "✅ No escopo",
    "fsx": "🔀 FSx ✅ · FSx for Lustre ❌ fora do escopo",
    "storage-gateway": "✅ No escopo", "aws-backup": "✅ No escopo", "elastic-disaster-recovery": "✅ No escopo",
    "rds": "✅ No escopo", "aurora": "✅ No escopo", "dynamodb": "✅ No escopo", "elasticache": "✅ No escopo",
    "memorydb": "❌ Fora do escopo", "redshift": "✅ No escopo", "documentdb": "✅ No escopo", "neptune": "✅ No escopo",
    "keyspaces-timestream-e-outros": "🔀 Keyspaces e MemoryDB ❌ fora do escopo · Timestream ⚪ não listado",
    "vpc": "✅ No escopo",
    "vpc-peering-transit-gateway-e-endpoints": "✅ No escopo (Transit Gateway e PrivateLink listados)",
    "site-to-site-vpn-e-client-vpn": "✅ No escopo", "direct-connect": "✅ No escopo", "route-53": "✅ No escopo",
    "cloudfront": "✅ No escopo", "global-accelerator": "✅ No escopo", "api-gateway": "✅ No escopo",
    "iam": "✅ No escopo (STS ⚪ não listado)", "iam-identity-center": "✅ No escopo", "cognito": "✅ No escopo",
    "directory-service": "✅ No escopo", "kms": "✅ No escopo", "cloudhsm": "✅ No escopo",
    "certificate-manager": "✅ No escopo (Private CA ⚪ não listado)",
    "secrets-manager-e-parameter-store": "✅ No escopo (Parameter Store como parte do Systems Manager)",
    "shield": "✅ No escopo", "waf": "✅ No escopo",
    "firewall-manager-e-network-firewall": "🔀 Firewall Manager ✅ · Network Firewall ❌ fora do escopo",
    "guardduty": "✅ No escopo", "inspector": "✅ No escopo", "macie": "✅ No escopo", "detective": "✅ No escopo",
    "security-hub": "✅ No escopo", "artifact": "✅ No escopo",
    "audit-manager": "⚪ Não listado (saiu da lista atual)",
    "cloudwatch": "✅ No escopo", "cloudtrail": "✅ No escopo", "config": "✅ No escopo",
    "systems-manager": "✅ No escopo", "cloudformation": "✅ No escopo", "organizations": "✅ No escopo",
    "control-tower": "✅ No escopo", "service-catalog-e-ram": "✅ No escopo", "trusted-advisor": "✅ No escopo",
    "health-dashboard": "✅ No escopo",
    "compute-optimizer-service-quotas-e-license-manager": "✅ No escopo (Launch Wizard ❌ fora do escopo)",
    "athena": "✅ No escopo", "glue": "✅ No escopo", "kinesis": "✅ No escopo", "emr": "✅ No escopo",
    "quicksight": "✅ No escopo (como Amazon Quick Sight)", "opensearch": "✅ No escopo",
    "lake-formation-msk-e-outros": "🔀 MSK, AppFlow, Data Exchange, Clean Rooms e DataZone ❌ fora do escopo · Lake Formation ⚪ não listado",
    "sagemaker-ai": "✅ No escopo", "bedrock": "⚪ Não listado", "amazon-q": "✅ No escopo",
    "servicos-de-ia-prontos": "🔀 Comprehend, Lex, Polly, Rekognition, Textract, Transcribe e Translate ✅ · Kendra ⚪ não listado · Personalize e Fraud Detector ❌ fora do escopo",
    "sqs": "✅ No escopo", "sns": "✅ No escopo", "eventbridge": "✅ No escopo", "step-functions": "✅ No escopo",
    "amazon-mq": "⚪ Não listado",
    "cli-sdk-e-cloudshell": "🔀 CLI e Management Console ✅ · CloudShell ❌ fora do escopo · Cloud9 ⚪ não listado",
    "code-services": "🔀 CodeBuild e CodePipeline ✅ · CodeDeploy e CodeArtifact ❌ fora do escopo · CodeCommit e CodeStar ⚪ não listados",
    "x-ray": "✅ No escopo",
    "amazon-connect": "✅ No escopo", "ses": "✅ No escopo",
    "workspaces-e-appstream": "✅ No escopo (WorkSpaces, AppStream 2.0 e WorkSpaces Secure Browser)",
    "amplify-e-appsync": "🔀 Amplify ✅ · AppSync ⚪ não listado · Device Farm ❌ fora do escopo",
    "iot-core-e-greengrass": "🔀 IoT Core ✅ · IoT Greengrass ❌ fora do escopo",
    "discovery-migration-hub-e-evaluator": "✅ No escopo (Migration Hub e Application Discovery Service fechados a novos clientes)",
    "application-migration-service": "✅ No escopo", "dms-e-sct": "✅ No escopo",
    "snow-family": "⚪ Não listado (saiu da lista atual)",
    "datasync-e-transfer-family": "🔀 DataSync ⚪ não listado · Transfer Family ❌ fora do escopo",
    "cost-explorer": "✅ No escopo", "budgets": "✅ No escopo",
    "pricing-calculator-cur-e-outras-ferramentas": "✅ No escopo (Billing Conductor ❌ fora do escopo)",
    "planos-de-suporte": "✅ No escopo (AWS Support — task 4.3 cobra os planos novos)",
    "midia-e-jogos": "❌ Fora do escopo — documentado só para referência",
    "iot-robotica-e-satelite": "❌ Fora do escopo — documentado só para referência",
    "desenvolvimento-e-aplicacoes": "❌ Fora do escopo — documentado só para referência",
    "rede-e-diretorio": "❌ Fora do escopo — documentado só para referência",
    "gerenciamento-e-custos": "❌ Fora do escopo — documentado só para referência",
    "recursos-de-ajuda-e-parceiros": "🔀 Marketplace, APN, Professional Services, Prescriptive Guidance, Knowledge Center, re:Post e Trust and Safety ✅ (task 4.3) · AWS IQ, Activate e AMS ❌ fora do escopo",
}
LINHA_ESCOPO = re.compile(r"\n>\n> \*\*Escopo oficial:\*\*[^\n]*")


def aplicar_escopo_fichas():
    """Escreve (ou atualiza) a linha de escopo oficial logo após o 'Em uma frase' de cada ficha."""
    faltando = [n for n in CATEGORIA if n not in ESCOPO]
    assert not faltando, f"Fichas sem status de escopo: {faltando}"
    for nome, cat in CATEGORIA.items():
        caminho = os.path.join(RAIZ, "servicos", cat, nome + ".md")
        with open(caminho) as f:
            texto = LINHA_ESCOPO.sub("", f.read())
        linha = (f"\n>\n> **Escopo oficial:** {ESCOPO[nome]} · "
                 f"[ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)")
        texto = re.sub(r"(> \*\*Em uma frase:\*\*[^\n]*)", lambda m: m.group(1) + linha, texto, count=1)
        with open(caminho, "w") as f:
            f.write(texto)

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


def gerar_indice_servicos():
    partes = ["# 🔎 Fichas de serviços AWS\n",
              "Uma ficha por serviço (ou família de serviços), com o que cai na prova e o que vai além: "
              "componentes, configurações, limites, cobrança, responsabilidade compartilhada, "
              "atualizações 2025-2026, pegadinhas e perguntas típicas.\n",
              "> Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.\n>\n"
              "> Coluna *Escopo* ([lista oficial](../docs/00-guia-do-exame/escopo-oficial.md)): ✅ no escopo · "
              "🔀 parcial · ⚪ não listado · ❌ fora do escopo.\n>\n> "
              "Modelo para novas fichas: [`templates/servico.md`](../templates/servico.md).\n"]
    total = 0
    for cat, nomes in FICHAS.items():
        partes.append(f"\n## {NOMES_CATEGORIA[cat]}\n\n| Ficha | Escopo | Em uma frase |\n|---|---|---|")
        for nome in nomes:
            caminho = os.path.join(RAIZ, "servicos", cat, nome + ".md")
            with open(caminho) as f:
                texto = f.read()
            frase = re.search(r"\*\*Em uma frase:\*\* (.+)", texto)
            frase = frase.group(1).strip() if frase else ""
            partes.append(f"| [{titulo_ficha(nome)}]({cat}/{nome}.md) | {ESCOPO[nome].split()[0]} | {frase[:1].upper() + frase[1:]} |")
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
               "- [Guia do exame](docs/00-guia-do-exame/README.md) · [Escopo oficial](docs/00-guia-do-exame/escopo-oficial.md) · [Plano de estudos](docs/00-guia-do-exame/plano-de-estudos.md) · [O que mudou em 2025-2026](docs/00-guia-do-exame/atualizacoes-2025-2026.md)",
               "- Flashcards: " + " · ".join(f"[Domínio {d}](flashcards/dominio-{d}.md)" for d in DOMINIOS) + " · [Anki (TSV)](flashcards/anki-clf-c02.tsv)",
               "- Resumos: [Pares que confundem](resumos/comparativos.md) · [Palavras-chave](resumos/palavras-chave.md) · [Números-âncora](resumos/numeros-ancora.md)",
               "- Questões no formato da prova: [Simulado 01 (65 questões)](simulados/simulado-01.md) · " + " · ".join(f"[Domínio {d}](simulados/questoes/dominio-{d}.md)" for d in DOMINIOS),
               "- [Glossário](glossario.md) · [Progresso](progresso.md) · [Simulados](simulados/README.md) · [Erros recorrentes](simulados/erros-recorrentes.md) · [Labs](labs/README.md) · [Links úteis](recursos/links-uteis.md)",
               "- Fontes: [Guia completo](fontes/guia-completo-clf-c02.md) · [Pesquisa 2025-2026](fontes/pesquisa-atualizacoes-2025-2026.md) · [Verificação oficial (10/2026)](fontes/verificacao-fontes-oficiais-2026-10.md)",
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
    aplicar_escopo_fichas()
    fichas = gerar_indice_servicos()
    gerar_indice_readme(secoes, ordem)
    print(f"{len(ordem)} tópicos, {total} flashcards e índice de {fichas} fichas gerados.")


if __name__ == "__main__":
    main()
