#!/usr/bin/env python3
"""Gera docs/, resumos/ e flashcards/ a partir de fontes/guia-completo-clf-c02.md.

Uso: python3 scripts/gerar_docs.py

ATENÇÃO: sobrescreve os arquivos gerados. Em cada tópico, dois blocos são preservados
entre execuções: <!-- extra:inicio -->…<!-- extra:fim --> (complementos) e
<!-- notas:inicio -->…<!-- notas:fim --> (anotações pessoais).
A seção didática "Antes de começar" de cada tópico vem de scripts/didatica_docs.py.
"""
import csv
import os
import re

from didatica_docs import DOMINIOS as DIDATICA_DOMINIOS, TOPICOS as DIDATICA_TOPICOS, APOIO, bloco_apoio
from aprofundamento import TOPICOS as APROFUNDAMENTOS, FICHAS as FICHAS_PRATICAS, bloco_topico, bloco_ficha
from introducoes_servicos import FICHAS as INTRODUCOES_FICHAS, bloco_ficha as bloco_inicio_ficha
from apostila import BASE as BASE_FICHAS, capitulo_servico, capitulo_topico, capitulos_apoio

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
    "2.2": "A lista oficial de tarefas do root mudou: **alterar o nome da conta** e **mudar o plano de suporte não exigem mais o root**. Continuam exclusivos, entre outros: alterar e-mail/senha do root, fechar conta standalone, restaurar administrador IAM, MFA Delete e desbloquear políticas de S3/SQS.",
    "3.2": "Na lista oficial atual, **Outposts** está no escopo, **Local Zones** não aparece e **Wavelength** está **fora do escopo**.",
    "3.9": "A **família Snow** e o **DataSync** não aparecem na lista oficial atual (o Snowball Edge está fechado a novos clientes); **FSx for Lustre** e **Transfer Family** estão **fora do escopo**.",
    "3.12": "No escopo: SageMaker AI, Amazon Q, Comprehend, Lex, Polly, Rekognition, Textract, Transcribe e Translate. **Bedrock** e **Kendra** não aparecem na lista atual; **Personalize** e **Fraud Detector** estão **fora do escopo**.",
    "3.14": "No escopo: Connect, SES, AppStream 2.0, WorkSpaces, WorkSpaces Secure Browser, **Amplify** e **IoT Core**. AppSync não aparece na lista atual.",
    "3.15": "No escopo só ficaram **AWS CLI, CodeBuild, CodePipeline e X-Ray**. CodeDeploy, CodeArtifact e CloudShell estão **fora do escopo**; Cloud9, CodeCommit e CodeStar não aparecem.",
    "3.17": "**Migration Hub** e **Application Discovery Service** continuam no escopo, mas estão fechados a novos clientes desde 07/11/2025. **Transfer Family** está **fora do escopo**; Snow e DataSync não aparecem.",
    "3.18": "Vários serviços desta seção estão **fora do escopo** oficial (MSK, AppFlow, Data Exchange, Keyspaces, MemoryDB, Personalize, Device Farm, Network Firewall, AWS IQ). Use-os para reconhecer distratores.",
    "4.5": "A task 4.3 consultada cita **Developer, Business, Enterprise On-Ramp e Enterprise**; a página comercial apresenta **Business Support+, Enterprise e Unified Operations**. Estude os dois modelos, distinguindo contexto do guia e oferta comercial. Veja a [auditoria](../00-guia-do-exame/auditoria-conteudo-2026-10.md) e a [ficha de suporte](../../servicos/custos/planos-de-suporte.md).",
    "4.6": "**AWS IQ**, **AWS Activate** e **AWS Managed Services** estão **fora do escopo** oficial. A task 4.3 cita: Trust and Safety, APN, Marketplace, Professional Services, Prescriptive Guidance, Knowledge Center e re:Post.",
}
# Correções aplicadas ao texto de fontes/guia-completo-clf-c02.md na geração (o arquivo-fonte não é
# editado). Baseadas nas verificações oficiais de 04/10/2026. Cada trecho precisa existir na fonte.
CORRECOES = [
    ("**FIFO:** ordem garantida e entrega exatamente uma vez.",
     "**FIFO:** ordenação por grupo e deduplicação no envio dentro das condições do serviço; o consumidor ainda precisa tratar recebimentos repetidos e efeitos de negócio."),
    ('- "Garantir ordem e processamento exatamente uma vez." → Fila SQS FIFO.',
     '- "Ordenar mensagens por grupo e tratar duplicações no envio." → Fila SQS FIFO; o programa ainda precisa evitar efeitos repetidos.'),
    ("Por requisição e por duração; nada quando não executa.",
     "No modelo base, requisições e duração; extras como concorrência provisionada podem cobrar sem invocação."),
    ("| Plano | Preço de referência | Canais | Tempos de resposta | Destaques |",
     "| Plano (modelo clássico; preços históricos, não cotação atual) | Preço mínimo histórico | Canais de suporte técnico | Tempo de primeira resposta | Recursos principais |"),
    ("Objeto de até **5 TB** (upload multipart para arquivos grandes).",
     "Objeto de até **50 TB** (🔄 desde 02/12/2025; antes 5 TB) — upload multipart para arquivos grandes."),
    ("- **Trusted Advisor por plano de suporte:** Basic e Developer só têm as verificações principais de segurança e de cotas; **Business, Enterprise On-Ramp e Enterprise têm todas as verificações** e acesso via API.",
     "- **Trusted Advisor por plano de suporte:** o Basic tem as verificações principais (service limits + 5 de segurança); 🔄 **Business Support+, Enterprise e Unified Operations têm todas as verificações** e acesso via API (no modelo clássico: Business, Enterprise On-Ramp e Enterprise). O **Trusted Advisor Priority** vem no Enterprise e no Unified Operations."),
    ('- "Qual plano de suporte libera todas as verificações do Trusted Advisor?" → Business ou superior.',
     '- "Qual plano de suporte libera todas as verificações do Trusted Advisor?" → Business Support+ ou superior (no modelo clássico, Business).'),
    ("  - A **AWS Health API** está disponível a partir do plano Business.",
     "  - A **AWS Health API** está disponível a partir do plano Business Support+ (no modelo clássico, Business)."),
    ("- **Disponibilidade do Health Dashboard:** gratuito para todos os clientes; a API exige plano Business ou superior.",
     "- **Disponibilidade do Health Dashboard:** gratuito para todos os clientes; a API exige plano Business Support+ ou superior (no modelo clássico, Business)."),
    ("| AWS Billing Conductor | Faturamento personalizado |",
     "| AWS Billing Conductor (❌ fora do escopo) | Faturamento personalizado |"),
    ('- **Cai na prova:** "menor plano com suporte 24/7 por telefone" = Business; "menor plano com todas as verificações do Trusted Advisor" = Business;',
     '- **Cai na prova:** 🔄 *oferta comercial atual (sem confirmação de substituição no banco da prova):* "plano pago de entrada, US$ 29 por conta, 30 min" = Business Support+; "TAM designado e 15 min" = Enterprise; "5 min" = Unified Operations. *Modelo clássico (até 01/01/2027):* "menor plano com suporte 24/7 por telefone" = Business; "menor plano com todas as verificações do Trusted Advisor" = Business;'),
    ('- "Qual o plano mais barato com suporte técnico 24/7 por telefone?" → Business.',
     '- "Qual o plano mais barato com suporte técnico 24/7 por telefone?" → Business Support+ (no modelo clássico, Business).'),
    ('- "Qual o plano mais barato com todas as verificações do Trusted Advisor?" → Business.',
     '- "Qual o plano mais barato com todas as verificações do Trusted Advisor?" → Business Support+ (no modelo clássico, Business).'),
    ('- "Qual plano dá acesso a um pool de TAMs?" → Enterprise On-Ramp.',
     '- "Qual plano dá acesso a um pool de TAMs?" → Enterprise On-Ramp (plano clássico, encerra em 01/01/2027).'),
    ('- "Qual plano responde em menos de 1 hora a produção fora do ar?" → Business.',
     '- "Qual plano responde em menos de 1 hora a produção fora do ar?" → Business Support+ ou superior (no modelo clássico, Business).'),
    ('- "Ambiente de testes que só precisa de ajuda técnica ocasional por e-mail." → Developer.',
     '- "Ambiente de testes que só precisa de ajuda técnica ocasional por e-mail." → Developer (plano clássico, encerra em 01/01/2027; no modelo atual, o plano pago de entrada é o Business Support+).'),
    ("- **AWS IQ:** está na lista oficial da prova.",
     "- **AWS IQ:** 🔄 hoje está declarado **fora do escopo** da prova (verificação de 10/2026)."),
    ("| Business vs Enterprise On-Ramp vs Enterprise | Business = 24/7 e Trusted Advisor completo; On-Ramp = pool de TAMs, 30 min; Enterprise = TAM dedicado, 15 min |",
     "| Business Support+ vs Enterprise vs Unified Operations (atuais) | Business Support+ = US$ 29/conta, 30 min, Trusted Advisor completo; Enterprise = TAM designado, TA Priority, 15 min; Unified Operations = 5 min, monitoramento 24/7 |\n"
     "| Business vs Enterprise On-Ramp vs Enterprise (clássicos, até 01/01/2027) | Business = 24/7 e Trusted Advisor completo; On-Ramp = pool de TAMs, 30 min; Enterprise = TAM dedicado, 15 min |"),
    ("  - Alterar configurações da conta (nome da conta, e-mail, senha do root e access keys do root).\n  - Fechar a conta AWS.\n  - Mudar ou cancelar o plano de AWS Support.\n",
     "  - 🔄 Alterar o **e-mail**, a **senha** e as **access keys** do root (conta standalone). *O nome da conta, contatos e regiões **não** exigem root.*\n"
     "  - Fechar a conta AWS (standalone).\n"
     "  - 🔄 *Mudar o plano de AWS Support **saiu** da lista oficial atual (verificação de 10/2026).*\n"),
    ("  - Editar ou apagar uma política de bucket S3 que bloqueou todo mundo.",
     "  - Editar ou apagar uma política de bucket S3 (ou de fila SQS) que bloqueou todo mundo.\n"
     "  - 🔄 Também na lista oficial: certas operações de Billing e faturas fiscais, inscrição no GovCloud, "
     "autorizar a recuperação de uma chave KMS que ficou sem gerenciamento.\n"
     "  - 🔄 Em AWS Organizations, a conta de gerenciamento pode executar centralmente tarefas privilegiadas das contas-membro "
     "(gerenciamento centralizado de acesso root)."),
    ('- "Qual destas tarefas exige o root?" → Fechar a conta, mudar o plano de suporte, alterar dados da conta ou restaurar permissões de administrador.',
     '- "Qual destas tarefas exige o root?" → Fechar a conta, alterar o e-mail ou a senha do root, restaurar permissões de administrador ou configurar MFA Delete. (🔄 Mudar o plano de suporte e alterar o nome da conta **não** estão mais na lista oficial.)'),
    ('- "Quem pode mudar o plano de suporte?" → O usuário root.',
     '- "Quem pode mudar o plano de suporte?" → 🔄 Não é mais tarefa exclusiva do root (saiu da lista oficial em 10/2026): uma identidade IAM com as permissões necessárias.'),
    ("| S3 Intelligent-Tiering | Padrão de acesso desconhecido ou que muda | Move objetos entre camadas sozinho; pequena taxa de monitoramento; sem taxa de recuperação |",
     "| S3 Intelligent-Tiering | Padrão de acesso desconhecido ou que muda | Move objetos entre camadas sozinho; pequena taxa de monitoramento por objeto; sem taxa de recuperação nas camadas automáticas (🔄 a recuperação Expedited da camada opcional Archive Access é cobrada) |"),
    ('| "petabytes, slow internet" | Família Snow |',
     '| "petabytes, slow internet" | Família Snow (🔄 fora da lista atual; Snowball Edge só para clientes existentes) |'),
]


EXTRA_INI = "<!-- extra:inicio -->"
EXTRA_FIM = "<!-- extra:fim -->"
NOTAS_INI = "<!-- notas:inicio -->"
NOTAS_FIM = "<!-- notas:fim -->"
NOTAS_VAZIO = ("## 📝 Minhas anotações\n\n"
               "<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->")

# Marcador de conteúdo autoral: aula ou ficha escrita à mão, cujo Markdown é a fonte
# da verdade. O gerador não reescreve esses arquivos (ver pendencias/plano-de-implementacao.md).
AUTORAL = "<!-- autoral -->"


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
            primeira = f.readline().strip()
        if primeira.startswith("# "):
            return primeira[2:]
    return nome


def limpar(texto):
    # Corrige negrito duplicado vindo da exportação ("**Nome****:**" -> "**Nome:**").
    texto = texto.replace("****:**", ":**")
    for antigo, novo in CORRECOES:
        assert antigo in texto, f"Correção não encontrada na fonte: {antigo[:60]}"
        texto = texto.replace(antigo, novo)
    return texto


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


def bloco_didatico(sec):
    """Seção "Antes de começar" do tópico (conteúdo em scripts/didatica_docs.py)."""
    d = DIDATICA_TOPICOS[sec]
    linhas = ["## 🧠 Antes de começar", "",
              f"**Qual é a dificuldade?** {d['problema']}", "",
              f"**A ideia em palavras simples:** {d['simples']}", "",
              f"**Exemplo do dia a dia:** {d['exemplo']}", "",
              f"**O que não concluir?** {d['limite']}"]
    if d.get("termos"):
        linhas += ["", "**📚 Palavras que aparecem aqui:**", "", "| Termo | Em palavras simples |", "|---|---|"]
        linhas += [f"| **{termo}** | {explicacao} |" for termo, explicacao in d["termos"]]
    return "\n".join(linhas)


def gerar_topicos(secoes):
    ordem = sorted(secoes, key=lambda s: tuple(int(x) for x in s.split(".")))
    sem_didatica = set(ordem) ^ set(DIDATICA_TOPICOS)
    assert not sem_didatica, f"Tópicos sem (ou sobrando) em didatica_docs.TOPICOS: {sorted(sem_didatica)}"
    assert set(ordem) == set(APROFUNDAMENTOS), "Cobertura do aprofundamento de tópicos incompleta"
    for i, sec in enumerate(ordem):
        titulo, corpo = secoes[sec]
        dom = sec.split(".")[0]
        pasta, nome_dom, peso = DOMINIOS[dom]
        caminho = caminho_topico(sec)
        if eh_autoral(caminho):
            # Aula escrita à mão: o Markdown é a fonte da verdade.
            continue
        if sec == "3.18":
            # Subtítulos ### viram ## no arquivo próprio.
            corpo = re.sub(r"^### ", "## ", corpo, flags=re.M)
        corpo = linkar_referencias(converter_marcadores(corpo), caminho)
        corpo = re.sub(r"^## ❓ Perguntas típicas", "## ❓ Perguntas típicas\n\n> Também estão nos [flashcards]("
                       + rel(caminho, f"flashcards/dominio-{dom}.md") + ").", corpo, count=1, flags=re.M)
        corpo = capitulo_topico(sec, corpo)

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

{bloco_didatico(sec)}

---

> **{nome_dom} ({peso})**
{bloco_fichas}{aviso}
{" · ".join(nav)}

---

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
            n = len(cards_do_topico(sec, corpo))
            linhas.append(f"| {sec} | [{titulo}]({ARQUIVOS[sec]}.md) | {n} |")
        blocos = intros.get(dom, [])
        if len(blocos) > 1:
            intro = "**Como o conteúdo está dividido:**\n\n" + "\n".join(
                f"- **Parte {i}:** {b}" for i, b in enumerate(blocos, 1))
        else:
            intro = "".join(blocos)
        escrever(caminho, f"""# {nome}

## 🧠 Antes de começar

**Qual é a dificuldade?** {DIDATICA_DOMINIOS[dom]['problema']}

**A ideia em palavras simples:** {DIDATICA_DOMINIOS[dom]['simples']}

**Exemplo do dia a dia:** {DIDATICA_DOMINIOS[dom]['exemplo']}

Comece pelas aberturas dos tópicos para entender a situação e a solução. Depois use o vocabulário,
os objetivos de leitura e o conteúdo técnico. As fichas detalham cada serviço; o índice não substitui essa leitura.

**Peso na prova:** {peso} das questões pontuadas

{intro}

## 🧭 Como estudar este domínio

- 🗺️ **Ordem sugerida:** {DIDATICA_DOMINIOS[dom]['ordem']}
- 🎯 **Dica:** {DIDATICA_DOMINIOS[dom]['dica']}
- 🧠 Cada tópico começa com a seção **Antes de começar**: problema, explicação, exemplo e limite.
  Depois vêm palavras novas explicadas, objetivos de leitura e revisão para a prova.

## Tópicos

| # | Tópico | Perguntas típicas |
|---|---|---|
{chr(10).join(linhas)}

> Acompanhe o seu avanço no [progresso](../../progresso.md).

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


def cards_do_topico(sec, corpo):
    """Flashcards da aula: da própria aula quando autoral, do guia original quando gerada."""
    caminho = caminho_topico(sec)
    if eh_autoral(caminho):
        with open(os.path.join(RAIZ, caminho)) as f:
            return extrair_cards_revisao(f.read())
    return extrair_cards(corpo)


def gerar_flashcards_capitulo_zero(todas):
    """Flashcards do capítulo 0, tirados da seção Revisão de cada aula autoral."""
    aulas = aulas_fundamentos()
    if not aulas:
        return
    partes = ["# 🃏 Flashcards — Capítulo 0 — Fundamentos de TI\n",
              "Clique na pergunta para ver a resposta. Gerado a partir da seção *Revisão* "
              "de cada aula (`python3 scripts/gerar_docs.py`).\n"]
    total = 0
    for numero, titulo, caminho in aulas:
        with open(os.path.join(RAIZ, caminho)) as f:
            cards = extrair_cards_revisao(f.read())
        assert cards, f"Aula do capítulo 0 sem perguntas na seção Revisão: {caminho}"
        partes.append(f"\n## [{numero} {titulo}]({rel('flashcards/capitulo-0.md', caminho)})\n")
        for q, a in cards:
            total += 1
            todas.append((q, a, f"CLF-C02 capitulo-0 aula-{numero.replace('.', '_')}"))
            partes.append(f"<details>\n<summary>{q}</summary>\n\n{a}\n</details>\n")
    partes.insert(2, f"**Total:** {total} cards\n")
    escrever("flashcards/capitulo-0.md", "\n".join(partes))


def gerar_flashcards(secoes, ordem):
    todas = []
    gerar_flashcards_capitulo_zero(todas)
    for dom, (pasta, nome, peso) in DOMINIOS.items():
        partes = [f"# 🃏 Flashcards — {nome}\n",
                  "Clique na pergunta para ver a resposta. Gerado a partir das *Perguntas típicas* "
                  "de cada tópico (`python3 scripts/gerar_docs.py`).\n"]
        total = 0
        for sec in ordem:
            if sec.split(".")[0] != dom:
                continue
            titulo, corpo = secoes[sec]
            cards = cards_do_topico(sec, corpo)
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
    "planos-de-suporte": "✅ No escopo (AWS Support — distinguir exemplos do guia e oferta comercial atual)",
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
        if eh_autoral(caminho_ficha(nome)):
            continue
        caminho = os.path.join(RAIZ, "servicos", cat, nome + ".md")
        with open(caminho) as f:
            texto = LINHA_ESCOPO.sub("", f.read())
        linha = (f"\n>\n> **Escopo oficial:** {ESCOPO[nome]} · "
                 f"[ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)")
        texto = re.sub(r"(> \*\*Em uma frase:\*\*[^\n]*)", lambda m: m.group(1) + linha, texto, count=1)
        with open(caminho, "w") as f:
            f.write(texto)


def aplicar_fichas_praticas():
    """Atualiza apenas o bloco próprio, preservando o texto e as anotações existentes."""
    assert set(CATEGORIA) == set(FICHAS_PRATICAS), "Cobertura das fichas práticas incompleta"
    marcador = re.compile(r"<!-- aprofundamento:inicio -->.*?<!-- aprofundamento:fim -->\n*", re.S)
    for nome, cat in CATEGORIA.items():
        if eh_autoral(caminho_ficha(nome)):
            continue
        caminho = os.path.join(RAIZ, "servicos", cat, nome + ".md")
        with open(caminho) as f:
            texto = marcador.sub("", f.read())
        ancora = "## 🔗 Documentação oficial"
        assert texto.count(ancora) == 1, f"Âncora da documentação ausente/duplicada: {caminho}"
        texto = texto.replace(ancora, bloco_ficha(nome) + "\n" + ancora, 1)
        escrever(caminho, texto)


def gerar_capitulos_servicos():
    """Regenera a apresentação das fichas a partir da fonte editorial separada."""
    assert set(CATEGORIA) == set(BASE_FICHAS), "Conteúdo-base de fichas incompleto"
    for nome, cat in CATEGORIA.items():
        caminho = caminho_ficha(nome)
        if eh_autoral(caminho):
            continue
        notas = ler_bloco(os.path.join(RAIZ, caminho), NOTAS_INI, NOTAS_FIM, NOTAS_VAZIO)
        escrever(caminho, capitulo_servico(nome) + "\n" + notas + "\n")


def inserir_abertura(texto, bloco):
    """Substitui só a abertura gerenciada e a posiciona logo após o título."""
    marcador = re.compile(r"<!-- didatico:inicio -->.*?<!-- didatico:fim -->\n*", re.S)
    quantidade = len(marcador.findall(texto))
    assert quantidade <= 1, "Bloco didático duplicado"
    assert (texto.count("<!-- didatico:inicio -->") ==
            texto.count("<!-- didatico:fim -->") == quantidade), "Marcadores didáticos incompletos"
    texto = marcador.sub("", texto)
    titulo, separador, resto = texto.partition("\n")
    assert separador and titulo.startswith("# "), "Título inicial ausente"
    return titulo + "\n\n" + bloco + "\n\n" + resto.lstrip("\n")


def aplicar_introducoes():
    """Aberturas completas; sem alterar notas, conteúdo técnico ou fontes originais."""
    assert set(CATEGORIA) == set(INTRODUCOES_FICHAS), "Cobertura das introduções de fichas incompleta"
    for nome, cat in CATEGORIA.items():
        caminho = caminho_ficha(nome)
        if eh_autoral(caminho):
            continue
        with open(os.path.join(RAIZ, caminho)) as f:
            texto = f.read()
        escrever(caminho, inserir_abertura(texto, bloco_inicio_ficha(nome)))
    pasta = os.path.join("docs", "00-guia-do-exame")
    existentes = {n for n in os.listdir(os.path.join(RAIZ, pasta)) if n.endswith(".md")}
    assert existentes == set(APOIO), "Cobertura das introduções do guia incompleta"
    for nome in APOIO:
        caminho = os.path.join(pasta, nome)
        with open(os.path.join(RAIZ, caminho)) as f:
            texto = f.read()
        escrever(caminho, inserir_abertura(texto, bloco_apoio(nome)))

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
              "## 🧭 Por onde começar\n\n"
              "Se você ainda não conhece um serviço, abra sua ficha e leia **Comece pelo problema**. "
              "A abertura explica a dificuldade, a solução, um exemplo, os limites e as primeiras palavras técnicas. "
              "Só depois avance para componentes, configurações e questões da prova.\n",
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
CONTEUDO_INI = "<!-- conteudo:inicio -->"
CONTEUDO_FIM = "<!-- conteudo:fim -->"


def nome_curto(titulo):
    """'Amazon EC2 (Elastic Compute Cloud)' -> 'Amazon EC2'."""
    return titulo.split(" (")[0]


def contar_linhas_tabela(caminho):
    with open(os.path.join(RAIZ, caminho)) as f:
        linhas = [l for l in f if l.startswith("| ") and not l.startswith("| ---")]
    return max(len(linhas) - 1, 0)  # desconta o cabeçalho


def substituir_bloco(texto, ini, fim, bloco):
    padrao = re.escape(ini) + r".*?" + re.escape(fim)
    assert re.search(padrao, texto, re.S), f"Marcadores {ini} … {fim} não encontrados no README.md"
    return re.sub(padrao, lambda _: bloco, texto, flags=re.S)


def bloco_conteudo(total_cards, total_topicos):
    from banco_questoes import QUESTOES
    total_fichas = sum(len(n) for n in FICHAS.values())
    fora = len(FICHAS["fora-do-escopo"])
    linhas = [
        CONTEUDO_INI,
        "| Material | O que é | Quando usar |",
        "|---|---|---|",
        f"| 📖 [Tópicos da prova](#sumário-da-apostila) | **{total_topicos} tópicos** que cobrem os 4 domínios, "
        "com conceitos explicados, casos resolvidos e perguntas de revisão | Estudo principal, na ordem do roteiro |",
        f"| 🔎 [Fichas de serviços](#caderno-de-serviços) | **{total_fichas} fichas** (uma por serviço ou família), "
        f"com funcionamento, opções, limites, segurança, custo e casos resolvidos; {fora} reúnem serviços **fora da prova** | Quando um tópico citar o serviço, ou para tirar dúvidas |",
        f"| 🃏 [Flashcards](flashcards/README.md) | **{total_cards} perguntas e respostas** por capítulo, também em arquivo para o Anki | Todos os dias, para memorizar |",
        f"| 📝 [Simulado 01](simulados/simulado-01.md) | **{len(QUESTOES)} questões** no formato da prova, com gabarito comentado | Depois de estudar os 4 domínios (90 min, sem consulta) |",
        "| ❓ [Questões por domínio](simulados/questoes/README.md) | As mesmas questões, agrupadas por tópico | Ao terminar cada domínio |",
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


def bloco_indice(secoes, ordem):
    aberturas = {
        "1": ("Conceitos de nuvem", "Por que usar recursos pela internet e como pensar em crescimento, falhas e migração?", "Comece pela ideia de nuvem. Depois estude as vantagens, a arquitetura, as boas práticas e a economia.", "Explique a diferença entre comprar infraestrutura e contratar recursos, e reconheça as vantagens e os limites de cada escolha."),
        "2": ("Segurança e conformidade", "Quem pode acessar os recursos e quem precisa cuidar da segurança?", "Com a base do capítulo 1, separe as responsabilidades. Em seguida, estude identidades, permissões, proteção de dados e acompanhamento do ambiente.", "Diferencie as responsabilidades da AWS e do cliente, explique permissões e escolha ferramentas de proteção e auditoria."),
        "3": ("Tecnologia e serviços", "Como montar uma solução usando computação, dados, armazenamento e redes?", "Use a base de nuvem e segurança para entender as peças de uma aplicação. Leia as aulas em ordem e abra as fichas indicadas dentro de cada uma.", "Relacione uma necessidade ao serviço apropriado e explique o que ele entrega, suas limitações e as decisões que ficam com o cliente."),
        "4": ("Cobrança, preços e suporte", "Como entender a conta, controlar gastos e obter ajuda?", "Agora que você conhece os recursos, estude como o uso vira cobrança, quando compromissos de compra fazem sentido e quais ferramentas ajudam a acompanhar custos.", "Diferencie os modelos de compra e as ferramentas de estimativa, acompanhamento e orçamento, além das opções de suporte."),
    }
    linhas = [INDICE_INI, "## Sumário da apostila", "",
              "Leia do capítulo 0 ao 4. Os números das aulas indicam sua posição: **3.3**, por exemplo, é a terceira aula do capítulo 3. Clique no título para abrir o texto.", ""]
    linhas += bloco_capitulo_zero()
    for dom, (pasta, nome, peso) in DOMINIOS.items():
        titulo, pergunta, percurso, objetivo = aberturas[dom]
        linhas += [f"### Capítulo {dom}: {titulo}", "", f"**A pergunta deste capítulo:** {pergunta}", "", percurso, "",
                   f"Corresponde ao {nome.lower()} — **{peso} da prova**. [Apresentação do capítulo](docs/{pasta}/README.md).", "",
                   "| Aula | Assunto |", "|---|---|"]
        for sec in ordem:
            if sec.split(".")[0] == dom:
                linhas.append(f"| {sec} | [{secoes[sec][0]}]({caminho_topico(sec)}) |")
        primeira = next(sec for sec in ordem if sec.split(".")[0] == dom)
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


def gerar_indice_readme(secoes, ordem, total_cards):
    """Atualiza no README.md os blocos gerados: tabela de materiais e índice de tópicos e fichas."""
    caminho = os.path.join(RAIZ, "README.md")
    with open(caminho) as f:
        texto = f.read()
    texto = substituir_bloco(texto, CONTEUDO_INI, CONTEUDO_FIM, bloco_conteudo(total_cards, len(ordem)))
    texto = substituir_bloco(texto, INDICE_INI, INDICE_FIM, bloco_indice(secoes, ordem))
    with open(caminho, "w") as f:
        f.write(texto)


def main():
    secoes, intros, extras = parse_guia()
    ordem = gerar_topicos(secoes)
    gerar_readmes_dominio(secoes, intros, ordem)
    total = gerar_flashcards(secoes, ordem)
    gerar_resumos(extras)
    gerar_capitulos_servicos()
    aplicar_escopo_fichas()
    for nome, texto in capitulos_apoio().items():
        escrever(os.path.join("docs", "00-guia-do-exame", nome), texto)
    aplicar_introducoes()
    fichas = gerar_indice_servicos()
    gerar_indice_readme(secoes, ordem, total)
    print(f"{len(ordem)} tópicos, {total} flashcards e índice de {fichas} fichas gerados.")


if __name__ == "__main__":
    main()
