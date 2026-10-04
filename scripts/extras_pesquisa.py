#!/usr/bin/env python3
"""Insere, uma única vez, os complementos da pesquisa 2025-2026 no bloco "extra" de cada tópico.

Uso: python3 scripts/extras_pesquisa.py
Só preenche blocos vazios; não sobrescreve o que já foi editado.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gerar_docs import EXTRA_FIM, EXTRA_INI, RAIZ, caminho_topico  # noqa: E402

CAB = ("## 🔄 Atualizações 2025-2026 e detalhes extras\n\n"
       "> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). "
       "Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.\n\n")

EXTRAS = {
"3.2": """- **Números atuais (🧊 aproximados):** 39 regiões geográficas e 124 AZs, com mais regiões anunciadas (Arábia Saudita, Chile). A prova cobra o conceito: **região = várias AZs (mínimo 3); AZ = um ou mais datacenters**.
- **Edge (🧊):** CloudFront com 750+ PoPs em 100+ cidades, 1.140+ PoPs embarcados em ISPs e 15 Regional Edge Caches. Simulados antigos falam em "400+" ou "450+". Basta saber que **edge locations são muito mais numerosas que regiões**.
- **AWS European Sovereign Cloud** (Brandenburg, `eusc-de-east-1`): região soberana europeia, operada separadamente. Bom saber que existe.
- ⚠️ "Várias AZs" = alta disponibilidade/tolerância a falhas. "Várias regiões" = DR geográfico, latência global ou exigência legal. **Nunca** "várias edge locations" para alta disponibilidade de computação.
- ⚠️ Local Zones (perto de cidades) × Wavelength (dentro da rede 5G) × Outposts (hardware AWS no seu datacenter).
- 🧊 Não decorar: contagem de AZs por região, códigos de região, lista de cidades de PoPs.
""",
"2.8": """- **Shield Advanced (📌):** **US$ 3.000/mês por organização**, compromisso mínimo de **1 ano**, mais data transfer out dos recursos protegidos. Inclui camada 7 (com WAF), **Shield Response Team 24/7**, **proteção de custo** (créditos por escalonamento causado por DDoS) e **WAF sem custo adicional** nos recursos protegidos. A taxa cobre todas as contas da Organization.
  - *Questão-modelo:* "reembolso de custos de escalonamento causados por DDoS + especialistas 24/7" → **Shield Advanced**.
- **WAF:** cobra por Web ACL, por regra e por milhão de requisições (🧊 valores). Camada 7: SQL injection, XSS, rate-based rules, geo-blocking. ⚠️ Atua em CloudFront, ALB, API Gateway, AppSync e Cognito — **não** atua em NLB.
""",
"2.9": """- **Trusted Advisor — 🔄 6 categorias:** cost optimization, performance, security, fault tolerance, service limits e **operational excellence** (a mais nova). Materiais antigos listam 5; ⚠️ se a questão listar 5, escolha as 5 clássicas.
- **Basic/Developer:** todos os checks de **Service Limits** + checks selecionados de **Security** e **Fault Tolerance**, com refresh manual. 📌 Os "7 core checks" clássicos: S3 Bucket Permissions, Security Groups – Specific Ports Unrestricted, IAM Use, MFA on Root Account, EBS Public Snapshots, RDS Public Snapshots e Service Limits.
- **Business (Support+)/Enterprise/Unified Operations:** todos os checks, acesso via **AWS Support API** e integração com **EventBridge**. **Trusted Advisor Priority** exige Enterprise ou superior.
- 🧊 Contagem de checks: fontes divergem ("56 grátis / 482 no total", "500+"). Não decorar.
- **Ferramenta certa por pergunta (📌):**

| Pergunta | Serviço |
|---|---|
| Quem fez a chamada de API? | CloudTrail |
| Como estava a configuração em tal data / está conforme? | Config |
| Métrica ou alarme de desempenho | CloudWatch |
| Ameaça ativa (mineração de cripto, IP malicioso) | GuardDuty |
| Vulnerabilidade/CVE em EC2, ECR, Lambda | Inspector |
| PII no S3 | Macie |
| Investigar a causa raiz de um achado | Detective |
| Painel central de achados e padrões (CIS, AWS FSBP) | Security Hub |
""",
"2.3": """- **Secrets Manager × Parameter Store (📌):** a **rotação automática nativa** de credenciais (ex.: RDS) é do **Secrets Manager**. O Parameter Store guarda configurações e segredos simples, **sem rotação nativa**.
- 🔄 **MFA obrigatório para o root:** a AWS passou a exigir MFA para usuários root (primeiro nas contas de gerenciamento do Organizations, depois nas contas independentes). Em Organizations também existe o **gerenciamento centralizado de acesso root**, que permite remover as credenciais root das contas-membro.
""",
"2.5": """- **KMS × CloudHSM (📌):** "hardware **single-tenant**, controle **exclusivo** das chaves, FIPS 140 nível 3" → **CloudHSM**. "Chaves gerenciadas e integradas a vários serviços" → **KMS**.
- 🔄 O ACM passou a oferecer **certificados públicos exportáveis** (pagos) para uso fora dos serviços integrados. Na prova continua valendo: "certificado público gratuito com renovação automática para ELB/CloudFront" → ACM.
""",
"3.3": """- **Cobrança por segundo** com **mínimo de 60 segundos** (📌), na maioria das AMIs Linux e Windows, em todas as opções de compra (On-Demand, Spot, Savings Plans…).
- **Dedicated Host** = servidor físico inteiro para você, útil para **licenças vinculadas ao servidor** (BYOL por socket/núcleo). Pode ser comprado On-Demand ou via Savings Plans/reserva. **Dedicated Instance** = hardware dedicado sem visibilidade/controle de sockets.
- **Capacity Reservations:** garantem capacidade numa AZ **sem desconto por si só**, mas combinam com Savings Plans ou RIs regionais.
- 🧊 Não decorar: preço por hora, rede por tamanho de instância, número de ENIs.
""",
"3.5": """- **Lambda — números confirmados (📌):**

| Item | Valor |
|---|---|
| Memória | 128 MB (mínimo e padrão) a **10.240 MB**, em incrementos de 1 MB |
| CPU | **Proporcional à memória** — ⚠️ não existe configuração separada de vCPU |
| Timeout | até **900 s (15 min)** |
| `/tmp` (efêmero) | **512 MB a 10.240 MB** (512 MB sem custo extra) |
| Imagem de contêiner | até 10 GB (🧊) |
| Layers | até 5 por função (🧊) |
| Cobrança | nº de requisições + duração em ms × memória (GB-s) |

- Contas novas têm quotas reduzidas de concorrência/memória que a AWS aumenta automaticamente com o uso (explica relatos de "limite de 3.008 MB").
- *Questão-modelo:* "processar um arquivo por até **2 horas** sem gerenciar servidores" → **não** é Lambda; resposta: **Fargate/ECS ou AWS Batch**.
- 🧊 Não decorar: escalonamento de concorrência (1.000 ambientes a cada 10 s), detalhes de rede da Lambda.
""",
"3.7": """- **DynamoDB:** item de no máximo **400 KB** (📌, incluindo nomes e valores de atributos). ⚠️ "Guardar vídeos/imagens no DynamoDB" → guarde no **S3** e mantenha só a referência na tabela.
- **Aurora:** até **15 Aurora Replicas** por cluster (📌), além da primária. Um cluster secundário de Global Database pode ter até 16.
- **RDS Read Replicas:** até **15** por origem para MySQL, MariaDB e PostgreSQL (até 5 cross-region). Para Oracle/SQL Server as páginas da AWS se contradizem (5 × 15) — 🧊 não decorar.
- ⚠️ **Read Replica × Multi-AZ:** read replica = **escalar leitura** (assíncrona, pode ser cross-region). Multi-AZ = **alta disponibilidade/failover** (standby síncrono que, no modelo clássico, não atende leitura).
- **Diferenças sutis:**
  - Redshift (OLAP, SQL analítico em petabytes) × RDS/Aurora (OLTP) × Athena (SQL serverless direto no S3, paga por dado escaneado).
  - ElastiCache (cache em memória: Valkey/Redis OSS/Memcached) × MemoryDB (banco em memória **durável**) × DAX (cache **exclusivo** do DynamoDB, microssegundos).
  - Neptune = grafos · DocumentDB = MongoDB · Keyspaces = Cassandra · Timestream = séries temporais.
- 🔄 **Timestream for LiveAnalytics** fechado para novos clientes (20/06/2025). Na prova, "séries temporais/IoT" ainda → Timestream.
- 🧊 Não decorar: RCU/WCU por tamanho de item, limites de armazenamento por motor, versões.
""",
"3.8": """- 🔄 **Objeto máximo: 50 TB** (anunciado em 02/12/2025, re:Invent 2025; antes **5 TB**). ⚠️ A prova e os simulados quase certamente ainda usam **5 TB**: se "5 TB" for opção e "50 TB" não, marque 5 TB. Para uploads grandes a resposta continua sendo **multipart upload** (e Transfer Acceleration quando a distância é o problema).
- **Durabilidade:** todas as classes têm **11 noves**. A diferença está na **disponibilidade**, nº de AZs, **duração mínima** e **taxa de recuperação**.
- **Classe padrão:** sem especificar, o objeto vai para **S3 Standard**.

| Classe | Disponibilidade (design) | AZs | Duração mínima | Observação de prova |
|---|---|---|---|---|
| Standard | 99,99% | ≥3 | nenhuma | sem taxa de recuperação |
| Intelligent-Tiering | 99,9% | ≥3 | — (cobra monitoramento) | padrão de acesso desconhecido/mutável |
| Standard-IA | 99,9% | ≥3 | 30 dias | objeto mínimo cobrado: 128 KB; taxa por GB recuperado |
| One Zone-IA | 99,5% | **1** | 30 dias | dados **recriáveis** |
| Glacier Instant Retrieval | 99,9% | ≥3 | 90 dias | milissegundos; ~1 acesso por trimestre |
| Glacier Flexible Retrieval | 99,99% | ≥3 | 90 dias | Expedited **1–5 min**, Standard **3–5 h**, Bulk **5–12 h** (grátis) |
| Glacier Deep Archive | 99,99% | ≥3 | **180 dias** | Standard **até 12 h**, Bulk **até 48 h**; **sem Expedited**; o mais barato |

- *Questões-modelo:* "compliance por 7 anos, acesso raro, até 48 h aceitável, menor custo" → **Deep Archive**. "Miniaturas regeneráveis, acesso pouco frequente, menor custo" → **One Zone-IA**.
- 🧊 Fontes divergem sobre a duração mínima do Intelligent-Tiering; suporte a até 1 milhão de buckets por conta — não decorar.
""",
"3.9": """- **EBS Multi-Attach (📌):** só **io1/io2**, até **16 instâncias Nitro na mesma AZ**. ⚠️ "Compartilhar um volume entre muitas instâncias em várias AZs" → **EFS**, não EBS.
- EBS fica preso a uma AZ; para mudar de AZ/região use **snapshot** (armazenado regionalmente no S3 e copiável entre regiões).
- 🔄 **Família Snow:**
  - **Snowmobile** (100 PB): aposentado em 2024.
  - **Snowcone:** sem novos pedidos desde 12/11/2024; suporte encerrado em 12/11/2025.
  - **Snowball Edge:** desde **07/11/2025**, só para **clientes existentes**. Novos clientes: **DataSync** (online), **AWS Data Transfer Terminal** (transferência física em local seguro) ou parceiros; para borda, **Outposts**. Restam o Storage Optimized de 210 TB e o Compute Optimized de 104 vCPUs.
  - ⚠️ **Na prova** o exam guide ainda cita Snowball Edge/Snowmobile: "migrar petabytes com banda limitada" → **Snowball Edge**; "exabytes / 100 PB" → Snowmobile (questões antigas).
- 🧊 Não decorar: IOPS por tipo de EBS, throughput st1/sc1, tamanhos antigos de Snowball (80 TB), preços por GB.
""",
"3.10": """- **Direct Connect (📌):**
  - **Dedicated:** portas de **1, 10, 100 e 400 Gbps**. **Hosted** (via parceiro): **50 Mbps a 25 Gbps**.
  - ⚠️ **Não é criptografado por padrão.** **MACsec** existe em conexões dedicadas de 10/100/400 Gbps em locais selecionados; fora isso, use **VPN IPsec sobre o Direct Connect**.
  - "Privada, banda consistente, sem internet" → Direct Connect · "criptografada e rápida de configurar" → Site-to-Site VPN · "funcionários remotos" → **Client VPN**.
- **Route 53 — SLA de 100% (📌):** crédito para qualquer disponibilidade mensal < 100% do DNS autoritativo (API e console fora do SLA). "Único serviço com SLA de 100%" → Route 53.
  - Failover usa health checks · Geolocation = país/regulação · Latency = menor latência · Weighted = A/B e migração gradual.
- **CloudFront × Global Accelerator (📌):** CloudFront = **cache** HTTP/HTTPS nas edge locations. Global Accelerator = **sem cache**, **2 IPs anycast estáticos**, TCP/UDP pela rede global da AWS até o endpoint mais saudável (jogos, VoIP, failover regional rápido).
- 🧊 Não decorar: número de VIFs (51), regras de LAG, preços por GB, quotas de VPC/subnet.
""",
"3.11": """- 🔄 **Nomes atualizados:** a lista oficial in-scope usa **"Amazon Quick Sight"** (BI) — na prova pode aparecer o nome antigo **QuickSight**.
- ⚠️ Athena × Redshift × RDS: Athena = SQL serverless no S3 (paga por dado escaneado); Redshift = data warehouse (OLAP); RDS = transacional (OLTP).
""",
"3.12": """- 🔄 **Nomes:** "Amazon **SageMaker AI**" (construir/treinar/implantar modelos próprios). Na prova pode aparecer "SageMaker".
- **Bedrock** = modelos de fundação via API (IA generativa sem treinar do zero). **Amazon Q** = assistente de IA generativa (Q Developer para código, Q Business para dados corporativos).
- **Associações frase → serviço (📌):** texto → fala = **Polly** · fala → texto = **Transcribe** · chatbot = **Lex** · sentimento/entidades = **Comprehend** · texto/formulários de documentos digitalizados = **Textract** (⚠️ não Rekognition) · rostos/objetos em imagem e vídeo = **Rekognition** · busca inteligente corporativa = **Kendra** · traduzir = **Translate**.
""",
"3.13": """- **SQS — números (📌):**

| Item | Valor |
|---|---|
| Tamanho máximo de mensagem | 🔄 **1 MiB** desde 04/08/2025 (antes **256 KiB**) — ⚠️ se só houver 256 KB como opção, marque 256 KB |
| Retenção | padrão **4 dias**, mínimo 60 s, máximo **14 dias** |
| Visibility timeout | padrão **30 s**, mínimo 0, máximo **12 h** |
| Delay queue | até **15 min** |

- **Standard × FIFO:** Standard = throughput quase ilimitado, entrega "pelo menos uma vez", ordem por melhor esforço. FIFO = ordem garantida e processamento exatamente uma vez.
- 🔄 Segundo a pesquisa, o **SNS** também passou a aceitar mensagens de 1 MiB.
- **SQS × SNS × EventBridge:** fila (pull, buffer) × pub/sub (push, fan-out) × barramento de eventos com regras, eventos AWS/SaaS e agendamento (Scheduler). **Step Functions** = orquestração; **SWF** é legado.
- 🧊 Não decorar: mensagens in-flight, cobrança por blocos de 64 KB, throughput exato do FIFO.
""",
"3.14": """- **IoT:** IoT Core (conectar dispositivos e trocar mensagens MQTT) × **IoT Greengrass** (rodar Lambda e ML localmente no dispositivo de borda).
- 🔄 IoT Analytics e IoT Events tiveram fim de suporte anunciado — não estudar.
""",
"3.15": """- 🔄 **Status das ferramentas de desenvolvedor:**
  - **CodeCommit:** voltou a **GA e aberto a novos clientes em 24/11/2025** (tinha sido fechado em 2024).
  - **Cloud9:** fechado para novos clientes desde 25/07/2024 → alternativa: **CloudShell** (shell no navegador, autenticado, com CLI).
  - **CodeStar:** descontinuado em 31/07/2024.
  - Como o exam guide ainda lista Cloud9 e CodeStar, saiba o propósito: Cloud9 = IDE no navegador; CodeStar = gerenciar projetos de CI/CD.
- **AppConfig** = feature flags/configuração dinâmica · **X-Ray** = rastreamento distribuído · **CodeArtifact** = repositório de pacotes (npm, Maven, PyPI).
""",
"4.2": """- **Descontos confirmados (📌):**

| Opção | Desconto máx. vs On-Demand | Compromisso | Detalhe que cai |
|---|---|---|---|
| Spot | até **90%** | nenhum | **aviso de 2 min**; ⚠️ Savings Plans **não** se aplicam a Spot |
| EC2 Instance Savings Plans | até **72%** | 1 ou 3 anos, US$/hora | família fixa numa região (tamanho/SO flexíveis) |
| Compute Savings Plans | até **66%** | 1 ou 3 anos | EC2 (qualquer família/região), **Fargate e Lambda** |
| Standard RI | até **72%** | 1 ou 3 anos | revendável no RI Marketplace |
| Convertible RI | até **66%** (página de preços de RI; o SAP Lens cita 54%) | 1 ou 3 anos | troca família/SO |
| Database Savings Plans | até 35% | 1 ou 3 anos | 🔄 novo (RDS, Aurora, DynamoDB, ElastiCache…) |
| SageMaker AI Savings Plans | até 64% | 1 ou 3 anos | — |

- Para a prova basta: "Convertible < Standard em desconto, porém mais flexível".
- ⚠️ "Estável 24/7 por 3 anos, menor custo, sem flexibilidade" → Standard RI ou EC2 Instance SP · "EC2 + Lambda + Fargate com flexibilidade" → **Compute Savings Plans** · "tolera interrupção (batch, CI/CD, render)" → **Spot**.
""",
"4.3": """- 🔄 **Free Tier (mudou em 15/07/2025):**
  - Contas novas escolhem **Free plan** ou **Paid plan**. Ambas recebem **US$ 100 em créditos no cadastro + até US$ 100** por atividades de onboarding (total até **US$ 200**).
  - O **Free plan** expira em **6 meses ou quando os créditos acabam** (o que vier primeiro); não gera cobrança, mas bloqueia alguns serviços caros. Para continuar, upgrade para o Paid plan.
  - **30+ serviços Always Free** continuam valendo. Contas anteriores a 15/07/2025 seguem no modelo legado (12 meses, trials, Always Free).
  - ⚠️ **Na prova:** responda pelo modelo clássico (**Always Free, 12 meses grátis, trials**), a menos que a questão fale em créditos.
- **Per-second billing** (mínimo de 60 s) também explica questões de "parar instâncias ociosas reduz custo".
""",
"4.5": """- 🔄 **Planos reestruturados (dezembro/2025):**

| Novo plano | Preço de referência | Resposta crítica |
|---|---|---|
| Basic | Grátis | — |
| **Business Support+** | a partir de **US$ 29/mês por conta** (ou % do uso começando em 9%) | **30 min** |
| **Enterprise** | mínimo **US$ 5.000/mês** (antes US$ 15.000); TAM designado | **15 min** |
| **Unified Operations** | a partir de **US$ 50.000/mês** | **5 min** |

- Tempos comuns aos pagos: general guidance < 24 h · system impaired < 12 h · production system impaired < 4 h · production system down < 1 h.
- **Developer, Business e Enterprise On-Ramp encerram em 01/01/2027** (Enterprise On-Ramp migrando automaticamente para Enterprise em 2026; os legados seguem no GovCloud).
- ⚠️ **Na prova** continue estudando os **5 planos clássicos** (Basic, Developer, Business, Enterprise On-Ramp, Enterprise). "Menor plano com TAM designado e 15 min" → **Enterprise** (válido nos dois modelos). "Menor custo com < 1 h para produção fora do ar" → **Business** (clássico) / Business Support+ (novo).
- Shield Advanced (US$ 3.000/mês) e Enterprise (US$ 5.000 mínimo) são "custo fixo alto": raramente são a resposta "mais barata".
""",
"4.6": """- 🔄 **AWS IQ encerrado em 28/05/2026** (novos cadastros de especialistas pararam em 20/05/2025). Substituto indicado: **AWS Marketplace Professional Services**. ⚠️ O exam guide ainda cita o AWS IQ como "contratar freelancers/consultorias certificadas sob demanda" — se aparecer, é a resposta.
- **AWS Marketplace** também vende **serviços profissionais**, além de AMIs, SaaS, contêineres e dados.
""",
}


def main():
    for sec, texto in EXTRAS.items():
        caminho = os.path.join(RAIZ, caminho_topico(sec))
        with open(caminho) as f:
            atual = f.read()
        vazio = f"{EXTRA_INI}\n{EXTRA_FIM}"
        if vazio not in atual:
            print(f"{sec}: bloco já preenchido, ignorado")
            continue
        novo = f"{EXTRA_INI}\n{CAB}{texto.strip()}\n{EXTRA_FIM}"
        with open(caminho, "w") as f:
            f.write(atual.replace(vazio, novo))
        print(f"{sec}: ok")


if __name__ == "__main__":
    main()
