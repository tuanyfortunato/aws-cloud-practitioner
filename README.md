# ☁️ AWS Certified Cloud Practitioner (CLF-C02) — Estudos

Repositório de documentação para a prova **AWS Certified Cloud Practitioner (CLF-C02)**: guia por tópico do exame,
**100 fichas detalhadas de serviços**, **302 flashcards**, **65 questões no formato da prova**, resumos de revisão e acompanhamento do estudo.

## 🚀 Comece por aqui

1. [Guia do exame](docs/00-guia-do-exame/README.md) — formato, domínios, o que cai e o que não cai
2. [Plano de estudos](docs/00-guia-do-exame/plano-de-estudos.md) — cronograma de 6 semanas
3. [Escopo oficial](docs/00-guia-do-exame/escopo-oficial.md) — task statements e serviços dentro/fora da prova (verificado em 04/10/2026)
4. [O que mudou em 2025-2026](docs/00-guia-do-exame/atualizacoes-2025-2026.md) — inclui os **novos planos de suporte**, que o exam guide atual já cobra
5. [Progresso](progresso.md) — checklist do que já foi estudado

## 📚 Conteúdo por domínio da prova

| # | Domínio | Peso | Tópicos |
|---|---|---|---|
| 1 | [Conceitos de Nuvem](docs/01-conceitos-de-nuvem/README.md) | 24% | Vantagens da nuvem, Well-Architected, CAF, 7 Rs, economia |
| 2 | [Segurança e Conformidade](docs/02-seguranca-e-conformidade/README.md) | 30% | Responsabilidade compartilhada, IAM, criptografia, logs, detecção de ameaças |
| 3 | [Tecnologia e Serviços de Nuvem](docs/03-tecnologia-e-servicos/README.md) | 34% | Infraestrutura global, computação, bancos, armazenamento, rede, IA, migração |
| 4 | [Cobrança, Preços e Suporte](docs/04-cobranca-precos-e-suporte/README.md) | 12% | Modelos de compra, ferramentas de custo, planos de suporte |

Cada tópico traz o conteúdo cobrado, **Cai na prova**, **Perguntas típicas**, as **atualizações 2025-2026**,
links para as fichas dos serviços e um espaço para suas anotações.

## 🔎 Fichas de serviços

[`servicos/`](servicos/README.md) tem uma ficha por serviço (ou família) com: componentes, **configurações e opções**,
limites e números, cobrança, responsabilidade compartilhada, atualizações recentes, pegadinhas e perguntas típicas.

| Categoria | Exemplos |
|---|---|
| [Computação](servicos/README.md) | EC2, Auto Scaling, ELB, Lambda, ECS, EKS, Fargate, Beanstalk |
| [Armazenamento](servicos/README.md) | S3 e classes, EBS, EFS, FSx, Storage Gateway, Backup |
| [Banco de dados](servicos/README.md) | RDS, Aurora, DynamoDB, ElastiCache, Redshift, Neptune |
| [Redes](servicos/README.md) | VPC, Route 53, CloudFront, Direct Connect, VPN, API Gateway |
| [Segurança](servicos/README.md) | IAM, KMS, Shield, WAF, GuardDuty, Inspector, Macie, Artifact |
| [Gerenciamento](servicos/README.md) | CloudWatch, CloudTrail, Config, Organizations, Trusted Advisor |
| [Analytics, IA e integração](servicos/README.md) | Athena, Kinesis, Glue, SageMaker AI, Bedrock, SQS, SNS, EventBridge |
| [Migração e custos](servicos/README.md) | MGN, DMS, Snow, Cost Explorer, Budgets, planos de suporte |

<!-- indice:inicio -->
## 🧭 Índice completo

Links diretos para todos os tópicos e fichas (clique para expandir). Gerado por `scripts/gerar_docs.py`.

### Tópicos do exame

<details>
<summary><b>Domínio 1 — Conceitos de Nuvem (24%)</b></summary>

- [1.1 O que é computação em nuvem](docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md)
- [1.2 As 6 vantagens da computação em nuvem](docs/01-conceitos-de-nuvem/02-vantagens-da-nuvem.md)
- [1.3 Conceitos de arquitetura que a prova cobra](docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md)
- [1.4 AWS Well-Architected Framework](docs/01-conceitos-de-nuvem/04-well-architected-framework.md)
- [1.5 AWS Cloud Adoption Framework (CAF)](docs/01-conceitos-de-nuvem/05-cloud-adoption-framework.md)
- [1.6 Estratégias de migração (os 7 Rs)](docs/01-conceitos-de-nuvem/06-estrategias-de-migracao.md)
- [1.7 Economia da nuvem](docs/01-conceitos-de-nuvem/07-economia-da-nuvem.md)

</details>

<details>
<summary><b>Domínio 2 — Segurança e Conformidade (30%)</b></summary>

- [2.1 Modelo de responsabilidade compartilhada](docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md)
- [2.2 Usuário root](docs/02-seguranca-e-conformidade/02-usuario-root.md)
- [2.3 AWS IAM (Identity and Access Management)](docs/02-seguranca-e-conformidade/03-iam.md)
- [2.4 Governança multi-conta](docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md)
- [2.5 Criptografia](docs/02-seguranca-e-conformidade/05-criptografia.md)
- [2.6 Compliance e governança](docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md)
- [2.7 Logs, monitoramento e auditoria](docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)
- [2.8 Proteção de rede e aplicações](docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)
- [2.9 Detecção de ameaças e postura de segurança](docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)
- [2.10 Outros pontos de segurança](docs/02-seguranca-e-conformidade/10-outros-pontos-de-seguranca.md)

</details>

<details>
<summary><b>Domínio 3 — Tecnologia e Serviços de Nuvem (34%)</b></summary>

- [3.1 Formas de acessar e implantar na AWS](docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md)
- [3.2 Infraestrutura global](docs/03-tecnologia-e-servicos/02-infraestrutura-global.md)
- [3.3 Amazon EC2](docs/03-tecnologia-e-servicos/03-ec2.md)
- [3.4 Escalabilidade e balanceamento de carga](docs/03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md)
- [3.5 Containers e serverless](docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)
- [3.6 Outros serviços de computação](docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md)
- [3.7 Bancos de dados](docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)
- [3.8 Amazon S3 — armazenamento de objetos](docs/03-tecnologia-e-servicos/08-s3.md)
- [3.9 Outros serviços de armazenamento](docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)
- [3.10 Rede e entrega de conteúdo](docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)
- [3.11 Analytics](docs/03-tecnologia-e-servicos/11-analytics.md)
- [3.12 IA e machine learning](docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)
- [3.13 Integração de aplicações](docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)
- [3.14 Aplicações de negócio, usuário final, front-end e IoT](docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md)
- [3.15 Ferramentas de desenvolvimento](docs/03-tecnologia-e-servicos/15-ferramentas-de-desenvolvimento.md)
- [3.16 Gestão e governança](docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md)
- [3.17 Migração e transferência](docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md)
- [3.18 Serviços menos conhecidos que podem aparecer](docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md)

</details>

<details>
<summary><b>Domínio 4 — Cobrança, Preços e Suporte (12%)</b></summary>

- [4.1 Princípios de preço da AWS](docs/04-cobranca-precos-e-suporte/01-principios-de-preco.md)
- [4.2 Modelos de compra do EC2](docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md)
- [4.3 Como outros recursos são cobrados](docs/04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md)
- [4.4 Ferramentas de custo e faturamento](docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)
- [4.5 Planos de AWS Support](docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md)
- [4.6 Outros recursos de ajuda](docs/04-cobranca-precos-e-suporte/06-outros-recursos-de-ajuda.md)

</details>

### Fichas de serviços

<details>
<summary><b>🖥️ Computação</b> (12)</summary>

- [Amazon EC2 (Elastic Compute Cloud)](servicos/computacao/ec2.md)
- [Amazon EC2 Auto Scaling](servicos/computacao/ec2-auto-scaling.md)
- [Elastic Load Balancing (ELB)](servicos/computacao/elastic-load-balancing.md)
- [AWS Lambda](servicos/computacao/lambda.md)
- [Amazon ECS (Elastic Container Service)](servicos/computacao/ecs.md)
- [Amazon EKS (Elastic Kubernetes Service)](servicos/computacao/eks.md)
- [AWS Fargate](servicos/computacao/fargate.md)
- [Amazon ECR (Elastic Container Registry)](servicos/computacao/ecr.md)
- [AWS Elastic Beanstalk](servicos/computacao/elastic-beanstalk.md)
- [Amazon Lightsail](servicos/computacao/lightsail.md)
- [AWS Batch](servicos/computacao/batch.md)
- [AWS Outposts, Local Zones e Wavelength](servicos/computacao/outposts-local-zones-wavelength.md)

</details>

<details>
<summary><b>🗄️ Armazenamento</b> (8)</summary>

- [Amazon S3 (Simple Storage Service)](servicos/armazenamento/s3.md)
- [Classes de armazenamento do S3 (incluindo S3 Glacier)](servicos/armazenamento/s3-classes-de-armazenamento.md)
- [Amazon EBS (Elastic Block Store) e Instance Store](servicos/armazenamento/ebs.md)
- [Amazon EFS (Elastic File System)](servicos/armazenamento/efs.md)
- [Amazon FSx](servicos/armazenamento/fsx.md)
- [AWS Storage Gateway](servicos/armazenamento/storage-gateway.md)
- [AWS Backup](servicos/armazenamento/aws-backup.md)
- [AWS Elastic Disaster Recovery (AWS DRS)](servicos/armazenamento/elastic-disaster-recovery.md)

</details>

<details>
<summary><b>🛢️ Banco de dados</b> (9)</summary>

- [Amazon RDS (Relational Database Service)](servicos/banco-de-dados/rds.md)
- [Amazon Aurora](servicos/banco-de-dados/aurora.md)
- [Amazon DynamoDB](servicos/banco-de-dados/dynamodb.md)
- [Amazon ElastiCache](servicos/banco-de-dados/elasticache.md)
- [Amazon MemoryDB](servicos/banco-de-dados/memorydb.md)
- [Amazon Redshift](servicos/banco-de-dados/redshift.md)
- [Amazon DocumentDB (compatível com MongoDB)](servicos/banco-de-dados/documentdb.md)
- [Amazon Neptune](servicos/banco-de-dados/neptune.md)
- [Amazon Keyspaces, Timestream e outros bancos especializados](servicos/banco-de-dados/keyspaces-timestream-e-outros.md)

</details>

<details>
<summary><b>🌐 Redes e entrega de conteúdo</b> (8)</summary>

- [Amazon VPC (Virtual Private Cloud)](servicos/redes/vpc.md)
- [VPC Peering, Transit Gateway, VPC Endpoints e PrivateLink](servicos/redes/vpc-peering-transit-gateway-e-endpoints.md)
- [AWS VPN (Site-to-Site VPN e Client VPN)](servicos/redes/site-to-site-vpn-e-client-vpn.md)
- [AWS Direct Connect](servicos/redes/direct-connect.md)
- [Amazon Route 53](servicos/redes/route-53.md)
- [Amazon CloudFront](servicos/redes/cloudfront.md)
- [AWS Global Accelerator](servicos/redes/global-accelerator.md)
- [Amazon API Gateway](servicos/redes/api-gateway.md)

</details>

<details>
<summary><b>🔐 Segurança, identidade e compliance</b> (18)</summary>

- [AWS IAM (Identity and Access Management) e AWS STS](servicos/seguranca/iam.md)
- [AWS IAM Identity Center (antigo AWS SSO)](servicos/seguranca/iam-identity-center.md)
- [Amazon Cognito](servicos/seguranca/cognito.md)
- [AWS Directory Service](servicos/seguranca/directory-service.md)
- [AWS KMS (Key Management Service)](servicos/seguranca/kms.md)
- [AWS CloudHSM](servicos/seguranca/cloudhsm.md)
- [AWS Certificate Manager (ACM) e AWS Private CA](servicos/seguranca/certificate-manager.md)
- [AWS Secrets Manager e Systems Manager Parameter Store](servicos/seguranca/secrets-manager-e-parameter-store.md)
- [AWS Shield](servicos/seguranca/shield.md)
- [AWS WAF (Web Application Firewall)](servicos/seguranca/waf.md)
- [AWS Firewall Manager e AWS Network Firewall](servicos/seguranca/firewall-manager-e-network-firewall.md)
- [Amazon GuardDuty](servicos/seguranca/guardduty.md)
- [Amazon Inspector](servicos/seguranca/inspector.md)
- [Amazon Macie](servicos/seguranca/macie.md)
- [Amazon Detective](servicos/seguranca/detective.md)
- [AWS Security Hub](servicos/seguranca/security-hub.md)
- [AWS Artifact](servicos/seguranca/artifact.md)
- [AWS Audit Manager](servicos/seguranca/audit-manager.md)

</details>

<details>
<summary><b>⚙️ Gerenciamento e governança</b> (11)</summary>

- [Amazon CloudWatch](servicos/gerenciamento/cloudwatch.md)
- [AWS CloudTrail](servicos/gerenciamento/cloudtrail.md)
- [AWS Config](servicos/gerenciamento/config.md)
- [AWS Systems Manager (SSM)](servicos/gerenciamento/systems-manager.md)
- [AWS CloudFormation (e CDK, SAM)](servicos/gerenciamento/cloudformation.md)
- [AWS Organizations](servicos/gerenciamento/organizations.md)
- [AWS Control Tower](servicos/gerenciamento/control-tower.md)
- [AWS Service Catalog e AWS Resource Access Manager (RAM)](servicos/gerenciamento/service-catalog-e-ram.md)
- [AWS Trusted Advisor](servicos/gerenciamento/trusted-advisor.md)
- [AWS Health Dashboard](servicos/gerenciamento/health-dashboard.md)
- [AWS Compute Optimizer, Service Quotas, License Manager e outros](servicos/gerenciamento/compute-optimizer-service-quotas-e-license-manager.md)

</details>

<details>
<summary><b>📊 Analytics</b> (7)</summary>

- [Amazon Athena](servicos/analytics/athena.md)
- [AWS Glue](servicos/analytics/glue.md)
- [Amazon Kinesis e Amazon Data Firehose](servicos/analytics/kinesis.md)
- [Amazon EMR](servicos/analytics/emr.md)
- [Amazon QuickSight (Amazon Quick Sight)](servicos/analytics/quicksight.md)
- [Amazon OpenSearch Service](servicos/analytics/opensearch.md)
- [Lake Formation, MSK, Data Exchange, AppFlow e outros serviços de dados](servicos/analytics/lake-formation-msk-e-outros.md)

</details>

<details>
<summary><b>🤖 IA e machine learning</b> (4)</summary>

- [Amazon SageMaker AI](servicos/ia-ml/sagemaker-ai.md)
- [Amazon Bedrock](servicos/ia-ml/bedrock.md)
- [Amazon Q](servicos/ia-ml/amazon-q.md)
- [Serviços de IA prontos (Rekognition, Comprehend, Lex, Polly, Transcribe, Translate, Textract, Kendra, Personalize…)](servicos/ia-ml/servicos-de-ia-prontos.md)

</details>

<details>
<summary><b>🔗 Integração de aplicações</b> (5)</summary>

- [Amazon SQS (Simple Queue Service)](servicos/integracao/sqs.md)
- [Amazon SNS (Simple Notification Service)](servicos/integracao/sns.md)
- [Amazon EventBridge](servicos/integracao/eventbridge.md)
- [AWS Step Functions](servicos/integracao/step-functions.md)
- [Amazon MQ](servicos/integracao/amazon-mq.md)

</details>

<details>
<summary><b>🛠️ Ferramentas de desenvolvedor</b> (3)</summary>

- [Formas de acesso: Console, CLI, SDKs, CloudShell (e Cloud9)](servicos/desenvolvimento/cli-sdk-e-cloudshell.md)
- [Ferramentas de CI/CD: CodeCommit, CodeBuild, CodeDeploy, CodePipeline, CodeArtifact](servicos/desenvolvimento/code-services.md)
- [AWS X-Ray](servicos/desenvolvimento/x-ray.md)

</details>

<details>
<summary><b>💼 Aplicações de negócio, usuário final e IoT</b> (5)</summary>

- [Amazon Connect](servicos/aplicacoes/amazon-connect.md)
- [Amazon SES (Simple Email Service)](servicos/aplicacoes/ses.md)
- [Amazon WorkSpaces, AppStream 2.0 e WorkSpaces Secure Browser](servicos/aplicacoes/workspaces-e-appstream.md)
- [AWS Amplify, AWS AppSync e AWS Device Farm](servicos/aplicacoes/amplify-e-appsync.md)
- [AWS IoT Core, IoT Greengrass e outros serviços de IoT](servicos/aplicacoes/iot-core-e-greengrass.md)

</details>

<details>
<summary><b>🚚 Migração e transferência</b> (5)</summary>

- [Migration Evaluator, Application Discovery Service e Migration Hub](servicos/migracao/discovery-migration-hub-e-evaluator.md)
- [AWS Application Migration Service (AWS MGN)](servicos/migracao/application-migration-service.md)
- [AWS Database Migration Service (DMS) e Schema Conversion Tool (SCT)](servicos/migracao/dms-e-sct.md)
- [Família AWS Snow (Snowball Edge, Snowcone, Snowmobile)](servicos/migracao/snow-family.md)
- [AWS DataSync e AWS Transfer Family](servicos/migracao/datasync-e-transfer-family.md)

</details>

<details>
<summary><b>💰 Custos e suporte</b> (5)</summary>

- [AWS Cost Explorer](servicos/custos/cost-explorer.md)
- [AWS Budgets](servicos/custos/budgets.md)
- [Pricing Calculator, Cost and Usage Report e outras ferramentas de faturamento](servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md)
- [Planos de AWS Support](servicos/custos/planos-de-suporte.md)
- [Recursos de ajuda, parceiros e serviços ao cliente (AWS IQ, Managed Services, Professional Services, re:Post…)](servicos/custos/recursos-de-ajuda-e-parceiros.md)

</details>

### Outros materiais

- [Guia do exame](docs/00-guia-do-exame/README.md) · [Escopo oficial](docs/00-guia-do-exame/escopo-oficial.md) · [Plano de estudos](docs/00-guia-do-exame/plano-de-estudos.md) · [O que mudou em 2025-2026](docs/00-guia-do-exame/atualizacoes-2025-2026.md)
- Flashcards: [Domínio 1](flashcards/dominio-1.md) · [Domínio 2](flashcards/dominio-2.md) · [Domínio 3](flashcards/dominio-3.md) · [Domínio 4](flashcards/dominio-4.md) · [Anki (TSV)](flashcards/anki-clf-c02.tsv)
- Resumos: [Pares que confundem](resumos/comparativos.md) · [Palavras-chave](resumos/palavras-chave.md) · [Números-âncora](resumos/numeros-ancora.md)
- Questões no formato da prova: [Simulado 01 (65 questões)](simulados/simulado-01.md) · [Domínio 1](simulados/questoes/dominio-1.md) · [Domínio 2](simulados/questoes/dominio-2.md) · [Domínio 3](simulados/questoes/dominio-3.md) · [Domínio 4](simulados/questoes/dominio-4.md)
- [Glossário](glossario.md) · [Progresso](progresso.md) · [Simulados](simulados/README.md) · [Erros recorrentes](simulados/erros-recorrentes.md) · [Labs](labs/README.md) · [Links úteis](recursos/links-uteis.md)
- Fontes: [Guia completo](fontes/guia-completo-clf-c02.md) · [Pesquisa 2025-2026](fontes/pesquisa-atualizacoes-2025-2026.md) · [Verificação oficial (10/2026)](fontes/verificacao-fontes-oficiais-2026-10.md)
- Modelos: [Tópico](templates/topico.md) · [Ficha de serviço](templates/servico.md) · [Simulado](templates/simulado.md)
<!-- indice:fim -->

## 🧠 Revisão

| Material | Para quê |
|---|---|
| [Flashcards](flashcards/README.md) | 302 perguntas e respostas por domínio (+ arquivo para importar no Anki) |
| [Pares que confundem](resumos/comparativos.md) | ~55 pares de serviços vizinhos |
| [Palavras-chave → serviço](resumos/palavras-chave.md) | Gatilhos dos enunciados |
| [Números-âncora](resumos/numeros-ancora.md) | Números que decidem a resposta (e o que não decorar) |
| [Glossário](glossario.md) | Termos e siglas |
| [Simulado 01](simulados/simulado-01.md) | 65 questões no formato da prova, com gabarito comentado e folha de correção |
| [Questões por domínio](simulados/questoes/README.md) | As mesmas questões agrupadas por domínio e tópico, para estudo direcionado |
| [Simulados](simulados/README.md) | Registro de simulados e erros recorrentes |
| [Labs](labs/README.md) | Práticas no console com cuidado de custos |

## 🗂️ Estrutura do repositório

```
.
├── docs/                    # Conteúdo por tópico do exame (gerado a partir de fontes/)
│   ├── 00-guia-do-exame/    # Formato da prova, plano de estudos, atualizações 2025-2026
│   ├── 01-conceitos-de-nuvem/          # 1.1 a 1.7
│   ├── 02-seguranca-e-conformidade/    # 2.1 a 2.10
│   ├── 03-tecnologia-e-servicos/       # 3.1 a 3.18
│   └── 04-cobranca-precos-e-suporte/   # 4.1 a 4.6
├── servicos/                # 100 fichas detalhadas, por categoria
├── flashcards/              # Gerados das "Perguntas típicas" (Markdown + TSV para Anki)
├── resumos/                 # Comparativos, palavras-chave, números-âncora
├── simulados/               # Simulado de 65 questões, questões por domínio e registro de erros
├── labs/                    # Exercícios práticos no console
├── fontes/                  # Documentos originais (fonte da verdade)
├── templates/               # Modelos de tópico, ficha de serviço e simulado
├── scripts/                 # Geração dos docs e verificação de links
├── recursos/                # Links úteis
├── assets/imagens/          # Diagramas e prints
├── glossario.md
└── progresso.md
```

## ✍️ Como usar e manter

- **Estudou um tópico?** Atualize o status no topo do arquivo (🔴 → 🟡 → 🟢) e em [progresso.md](progresso.md).
- **Anotações pessoais:** escreva na seção *📝 Minhas anotações* de cada tópico (é preservada ao regenerar).
- **Complementos de um tópico:** use o bloco entre `<!-- extra:inicio -->` e `<!-- extra:fim -->` (também preservado).
- **Mudou algo no guia?** Edite [`fontes/guia-completo-clf-c02.md`](fontes/guia-completo-clf-c02.md) e rode:

  ```bash
  python3 scripts/gerar_docs.py      # regenera tópicos, flashcards, resumos e índice de fichas
  python3 scripts/gerar_simulado.py  # regenera o simulado e as questões por domínio
  python3 scripts/verificar_links.py # confere se todos os links internos funcionam
  ```

- **Novo serviço?** Copie [`templates/servico.md`](templates/servico.md) para a categoria certa em `servicos/` e
  registre o nome em `FICHAS` dentro de `scripts/gerar_docs.py`.
- **Fez um simulado?** Use o [modelo de simulado](templates/simulado.md) e registre os erros em
  [`simulados/erros-recorrentes.md`](simulados/erros-recorrentes.md).

### Convenções

- Nomes de arquivos em minúsculas, sem acento, separados por hífen.
- Legenda nas fichas: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.
- Preços, limites e nomes de planos mudam: confira as páginas oficiais na semana da prova.
- Nunca faça commit de credenciais AWS (chaves de acesso, `.pem`, IDs de conta).
