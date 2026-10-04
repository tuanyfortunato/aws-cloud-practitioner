# ☁️ Estudos para a AWS Certified Cloud Practitioner (CLF-C02)

Material **gratuito e em português** para quem quer tirar a certificação **AWS Certified Cloud Practitioner**.
Aqui você encontra todo o conteúdo da prova organizado por tópico, uma ficha para cada serviço AWS, flashcards,
questões no formato da prova com gabarito comentado e resumos para a revisão final.

> ✔️ Conteúdo conferido em **fontes oficiais da AWS em outubro de 2026**, incluindo as mudanças recentes que já
> caem na prova. Não precisa abrir nenhuma pasta: **todos os links estão nesta página**.

**Nesta página:**
[1. A prova em 1 minuto](#1-a-prova-em-1-minuto) ·
[2. O que tem neste repositório](#2-o-que-tem-neste-repositório) ·
[3. Como estudar](#3-como-estudar-roteiro-em-5-passos) ·
[4. Tópicos da prova](#4-o-que-estudar-todos-os-tópicos-da-prova) ·
[5. Fichas de serviços](#5-serviços-aws-todas-as-fichas) ·
[6. Revisão final](#6-revisão-final) ·
[7. Acompanhe seu estudo](#7-acompanhe-seu-estudo) ·
[8. Fontes](#8-fontes-e-confiabilidade) ·
[9. Manutenção](#9-para-quem-mantém-o-repositório)

---

## 1. A prova em 1 minuto

| | |
|---|---|
| **Para quem é** | Quem quer comprovar conhecimento geral de nuvem AWS (não exige experiência técnica nem programação) |
| **Formato** | 65 questões (50 valem nota e 15 são de teste, sem identificação) |
| **Tipos de questão** | Múltipla escolha (1 resposta) e múltipla resposta (2 ou mais; o enunciado diz quantas) |
| **Tempo** | 90 minutos |
| **Nota para passar** | 700 de 1.000 (vale a nota total, não por domínio). Questão em branco conta como erro: **sempre responda** |
| **Preço e validade** | US$ 100 · válida por 3 anos · disponível em português |

**O que cai, e quanto pesa cada parte:**

| Domínio | Peso | Em poucas palavras |
|---|---|---|
| [1. Conceitos de Nuvem](docs/01-conceitos-de-nuvem/README.md) | **24%** | Por que usar a nuvem, princípios de arquitetura (Well-Architected), migração e economia |
| [2. Segurança e Conformidade](docs/02-seguranca-e-conformidade/README.md) | **30%** | Quem é responsável pelo quê, usuário root, IAM, criptografia, logs e detecção de ameaças |
| [3. Tecnologia e Serviços](docs/03-tecnologia-e-servicos/README.md) | **34%** | Infraestrutura global e os serviços: computação, bancos, armazenamento, rede, IA e outros |
| [4. Cobrança, Preços e Suporte](docs/04-cobranca-precos-e-suporte/README.md) | **12%** | Modelos de compra, ferramentas de custo e planos de suporte |

> ⚠️ **Antes de estudar, leia isto.** A AWS atualiza o conteúdo da prova **sem mudar o código CLF-C02**, e várias
> respostas que aparecem em materiais antigos estão desatualizadas. As principais:
> - Os **planos de suporte** cobrados agora são **Basic, Business Support+, Enterprise e Unified Operations**.
> - **Alterar o nome da conta** e **mudar o plano de suporte** **não** exigem mais o usuário root.
> - Vários serviços **saíram** da lista da prova (ex.: AWS IQ, CloudShell, CodeDeploy, família Snow).
>
> Detalhes: 🎯 [Escopo oficial](docs/00-guia-do-exame/escopo-oficial.md) (o que cai e o que não cai) ·
> 🔄 [O que mudou em 2025-2026](docs/00-guia-do-exame/atualizacoes-2025-2026.md) ·
> 📘 [Guia completo do exame](docs/00-guia-do-exame/README.md)

---

## 2. O que tem neste repositório

<!-- conteudo:inicio -->
| Material | O que é | Quando usar |
|---|---|---|
| 📖 [Tópicos da prova](#4-o-que-estudar-todos-os-tópicos-da-prova) | **41 tópicos** que cobrem os 4 domínios, cada um com o conteúdo cobrado, *Cai na prova*, perguntas típicas e atualizações | Estudo principal, na ordem do roteiro |
| 🔎 [Fichas de serviços](#5-serviços-aws-todas-as-fichas) | **105 fichas** (uma por serviço ou família), com configurações, limites, preço, pegadinhas e perguntas; 5 reúnem serviços **fora da prova** | Quando um tópico citar o serviço, ou para tirar dúvidas |
| 🃏 [Flashcards](flashcards/README.md) | **302 perguntas e respostas** por domínio, também em arquivo para o Anki | Todos os dias, para memorizar |
| 📝 [Simulado 01](simulados/simulado-01.md) | **65 questões** no formato da prova, com gabarito comentado | Depois de estudar os 4 domínios (90 min, sem consulta) |
| ❓ [Questões por domínio](simulados/questoes/README.md) | As mesmas questões, agrupadas por tópico | Ao terminar cada domínio |
| ⚖️ [Pares que confundem](resumos/comparativos.md) | **55 pares** de serviços parecidos e a diferença em uma linha | Revisão final |
| 🔑 [Palavras-chave → serviço](resumos/palavras-chave.md) | **28 gatilhos** do enunciado que apontam a resposta | Revisão final |
| 📌 [Números-âncora](resumos/numeros-ancora.md) | Os números que decidem a resposta (e o que **não** precisa decorar) | Revisão final |
| 📖 [Glossário](glossario.md) | **93 termos** e siglas | Sempre que travar num termo |
| ✅ [Progresso](progresso.md) | Checklist de todos os tópicos e marcos | Para acompanhar o seu avanço |
| 🧪 [Labs](labs/README.md) | Exercícios práticos no console AWS, com cuidado de custos | Opcional, para fixar |
<!-- conteudo:fim -->

---

## 3. Como estudar: roteiro em 5 passos

| Passo | O que fazer | Onde |
|---|---|---|
| **1. Entenda a prova** (1 dia) | Leia o guia do exame e veja o que cai e o que não cai | [Guia do exame](docs/00-guia-do-exame/README.md) · [Escopo oficial](docs/00-guia-do-exame/escopo-oficial.md) · [O que mudou](docs/00-guia-do-exame/atualizacoes-2025-2026.md) |
| **2. Estude os tópicos** (4–5 semanas) | Siga o plano semanal. Em cada tópico: leia o conteúdo, tente responder as *perguntas típicas* e abra as fichas indicadas | [Plano de estudos](docs/00-guia-do-exame/plano-de-estudos.md) · [Tópicos](#4-o-que-estudar-todos-os-tópicos-da-prova) |
| **3. Memorize** (todos os dias, 10 min) | Revise os flashcards dos tópicos já estudados | [Flashcards](flashcards/README.md) ([importar no Anki](flashcards/anki-clf-c02.tsv)) |
| **4. Treine com questões** | Ao fim de cada domínio, faça as questões dele. No fim, faça o simulado completo em 90 minutos | [Questões por domínio](simulados/questoes/README.md) · [Simulado 01](simulados/simulado-01.md) |
| **5. Revise os erros** (última semana) | Anote o que errou, releia os tópicos fracos e os resumos de revisão | [Erros recorrentes](simulados/erros-recorrentes.md) · [Revisão final](#6-revisão-final) |

> 🎯 **Meta:** acertar **80% ou mais** no simulado antes de agendar a prova (a nota mínima é cerca de 70%).

<details>
<summary><b>Como ler um tópico e uma ficha</b> (clique para ver)</summary>

**Cada tópico** (ex.: [2.3 IAM](docs/02-seguranca-e-conformidade/03-iam.md)) tem:
- **📖 Conteúdo:** o que a prova cobra, com a linha **Cai na prova** mostrando os cenários mais comuns.
- **❓ Perguntas típicas:** pergunta → resposta, no formato das questões.
- **🔄 Atualizações 2025-2026:** o que mudou e foi conferido em fonte oficial.
- **🔎 Fichas detalhadas:** links para os serviços citados.
- **⚠️ Aviso no topo**, quando o conteúdo mudou na prova atual.
- **📝 Minhas anotações:** espaço para você escrever.

**Cada ficha** (ex.: [Amazon S3](servicos/armazenamento/s3.md)) tem: o que é em uma frase, se está **no escopo da
prova**, a seção **🧠 Entenda em 30 segundos** (analogia, quando escolher, quando **não** escolher e as palavras
do enunciado que apontam para o serviço), para que serve, componentes, configurações, limites, cobrança, responsabilidade compartilhada,
pegadinhas e perguntas típicas.

**Legenda usada em todo o repositório:** 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar ·
✔️ confirmado em fonte oficial · ✅ no escopo da prova · ❌ fora do escopo.

</details>

---

<!-- indice:inicio -->
## 4. O que estudar: todos os tópicos da prova

Estude na ordem. Em cada tópico, abra também as **fichas** listadas ao lado: elas aprofundam os serviços citados.

### Domínio 1 — Conceitos de Nuvem — 24% da prova

➡️ [Visão geral do domínio](docs/01-conceitos-de-nuvem/README.md) · 🃏 [Flashcards](flashcards/dominio-1.md) · ❓ [Questões do domínio](simulados/questoes/dominio-1.md) · 7 tópicos

| # | Tópico | Fichas para abrir junto |
|---|---|---|
| 1.1 | [O que é computação em nuvem](docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md) | — |
| 1.2 | [As 6 vantagens da computação em nuvem](docs/01-conceitos-de-nuvem/02-vantagens-da-nuvem.md) | — |
| 1.3 | [Conceitos de arquitetura que a prova cobra](docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md) | — |
| 1.4 | [AWS Well-Architected Framework](docs/01-conceitos-de-nuvem/04-well-architected-framework.md) | [AWS Trusted Advisor](servicos/gerenciamento/trusted-advisor.md) |
| 1.5 | [AWS Cloud Adoption Framework (CAF)](docs/01-conceitos-de-nuvem/05-cloud-adoption-framework.md) | — |
| 1.6 | [Estratégias de migração (os 7 Rs)](docs/01-conceitos-de-nuvem/06-estrategias-de-migracao.md) | [AWS Application Migration Service](servicos/migracao/application-migration-service.md) · [AWS Database Migration Service](servicos/migracao/dms-e-sct.md) |
| 1.7 | [Economia da nuvem](docs/01-conceitos-de-nuvem/07-economia-da-nuvem.md) | [AWS Compute Optimizer, Service Quotas, License Manager e outros](servicos/gerenciamento/compute-optimizer-service-quotas-e-license-manager.md) · [Pricing Calculator, Cost and Usage Report e outras ferramentas de faturamento](servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md) |

### Domínio 2 — Segurança e Conformidade — 30% da prova

➡️ [Visão geral do domínio](docs/02-seguranca-e-conformidade/README.md) · 🃏 [Flashcards](flashcards/dominio-2.md) · ❓ [Questões do domínio](simulados/questoes/dominio-2.md) · 10 tópicos

| # | Tópico | Fichas para abrir junto |
|---|---|---|
| 2.1 | [Modelo de responsabilidade compartilhada](docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md) | [Amazon EC2](servicos/computacao/ec2.md) · [Amazon RDS](servicos/banco-de-dados/rds.md) · [AWS Lambda](servicos/computacao/lambda.md) · [Amazon S3](servicos/armazenamento/s3.md) · [Amazon DynamoDB](servicos/banco-de-dados/dynamodb.md) |
| 2.2 | [Usuário root](docs/02-seguranca-e-conformidade/02-usuario-root.md) | [AWS IAM](servicos/seguranca/iam.md) |
| 2.3 | [AWS IAM (Identity and Access Management)](docs/02-seguranca-e-conformidade/03-iam.md) | [AWS IAM](servicos/seguranca/iam.md) · [AWS IAM Identity Center](servicos/seguranca/iam-identity-center.md) · [Amazon Cognito](servicos/seguranca/cognito.md) · [AWS Directory Service](servicos/seguranca/directory-service.md) · [AWS Secrets Manager e Systems Manager Parameter Store](servicos/seguranca/secrets-manager-e-parameter-store.md) |
| 2.4 | [Governança multi-conta](docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md) | [AWS Organizations](servicos/gerenciamento/organizations.md) · [AWS Control Tower](servicos/gerenciamento/control-tower.md) · [AWS Service Catalog e AWS Resource Access Manager](servicos/gerenciamento/service-catalog-e-ram.md) |
| 2.5 | [Criptografia](docs/02-seguranca-e-conformidade/05-criptografia.md) | [AWS KMS](servicos/seguranca/kms.md) · [AWS CloudHSM](servicos/seguranca/cloudhsm.md) · [AWS Certificate Manager](servicos/seguranca/certificate-manager.md) · [Amazon S3](servicos/armazenamento/s3.md) |
| 2.6 | [Compliance e governança](docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md) | [AWS Artifact](servicos/seguranca/artifact.md) · [AWS Audit Manager](servicos/seguranca/audit-manager.md) · [AWS Config](servicos/gerenciamento/config.md) |
| 2.7 | [Logs, monitoramento e auditoria](docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md) | [AWS CloudTrail](servicos/gerenciamento/cloudtrail.md) · [AWS Config](servicos/gerenciamento/config.md) · [Amazon CloudWatch](servicos/gerenciamento/cloudwatch.md) · [Amazon VPC](servicos/redes/vpc.md) · [AWS Health Dashboard](servicos/gerenciamento/health-dashboard.md) |
| 2.8 | [Proteção de rede e aplicações](docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md) | [Amazon VPC](servicos/redes/vpc.md) · [AWS Shield](servicos/seguranca/shield.md) · [AWS WAF](servicos/seguranca/waf.md) · [AWS Firewall Manager e AWS Network Firewall](servicos/seguranca/firewall-manager-e-network-firewall.md) |
| 2.9 | [Detecção de ameaças e postura de segurança](docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) | [Amazon GuardDuty](servicos/seguranca/guardduty.md) · [Amazon Inspector](servicos/seguranca/inspector.md) · [Amazon Macie](servicos/seguranca/macie.md) · [Amazon Detective](servicos/seguranca/detective.md) · [AWS Security Hub](servicos/seguranca/security-hub.md) · [AWS Trusted Advisor](servicos/gerenciamento/trusted-advisor.md) |
| 2.10 | [Outros pontos de segurança](docs/02-seguranca-e-conformidade/10-outros-pontos-de-seguranca.md) | [Amazon GuardDuty](servicos/seguranca/guardduty.md) · [AWS Security Hub](servicos/seguranca/security-hub.md) · [Recursos de ajuda, parceiros e serviços ao cliente](servicos/custos/recursos-de-ajuda-e-parceiros.md) |

### Domínio 3 — Tecnologia e Serviços de Nuvem — 34% da prova

➡️ [Visão geral do domínio](docs/03-tecnologia-e-servicos/README.md) · 🃏 [Flashcards](flashcards/dominio-3.md) · ❓ [Questões do domínio](simulados/questoes/dominio-3.md) · 18 tópicos

| # | Tópico | Fichas para abrir junto |
|---|---|---|
| 3.1 | [Formas de acessar e implantar na AWS](docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md) | [Formas de acesso: Console, CLI, SDKs, CloudShell](servicos/desenvolvimento/cli-sdk-e-cloudshell.md) · [AWS CloudFormation](servicos/gerenciamento/cloudformation.md) · [AWS VPN](servicos/redes/site-to-site-vpn-e-client-vpn.md) · [AWS Direct Connect](servicos/redes/direct-connect.md) |
| 3.2 | [Infraestrutura global](docs/03-tecnologia-e-servicos/02-infraestrutura-global.md) | [AWS Outposts, Local Zones e Wavelength](servicos/computacao/outposts-local-zones-wavelength.md) · [Amazon CloudFront](servicos/redes/cloudfront.md) · [AWS Global Accelerator](servicos/redes/global-accelerator.md) |
| 3.3 | [Amazon EC2](docs/03-tecnologia-e-servicos/03-ec2.md) | [Amazon EC2](servicos/computacao/ec2.md) · [Amazon EBS](servicos/armazenamento/ebs.md) |
| 3.4 | [Escalabilidade e balanceamento de carga](docs/03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md) | [Amazon EC2 Auto Scaling](servicos/computacao/ec2-auto-scaling.md) · [Elastic Load Balancing](servicos/computacao/elastic-load-balancing.md) |
| 3.5 | [Containers e serverless](docs/03-tecnologia-e-servicos/05-containers-e-serverless.md) | [Amazon ECS](servicos/computacao/ecs.md) · [Amazon EKS](servicos/computacao/eks.md) · [AWS Fargate](servicos/computacao/fargate.md) · [Amazon ECR](servicos/computacao/ecr.md) · [AWS Lambda](servicos/computacao/lambda.md) |
| 3.6 | [Outros serviços de computação](docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md) | [AWS Elastic Beanstalk](servicos/computacao/elastic-beanstalk.md) · [Amazon Lightsail](servicos/computacao/lightsail.md) · [AWS Batch](servicos/computacao/batch.md) · [AWS Outposts, Local Zones e Wavelength](servicos/computacao/outposts-local-zones-wavelength.md) |
| 3.7 | [Bancos de dados](docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) | [Amazon RDS](servicos/banco-de-dados/rds.md) · [Amazon Aurora](servicos/banco-de-dados/aurora.md) · [Amazon DynamoDB](servicos/banco-de-dados/dynamodb.md) · [Amazon ElastiCache](servicos/banco-de-dados/elasticache.md) · [Amazon MemoryDB](servicos/banco-de-dados/memorydb.md) · [Amazon Redshift](servicos/banco-de-dados/redshift.md) · [Amazon DocumentDB](servicos/banco-de-dados/documentdb.md) · [Amazon Neptune](servicos/banco-de-dados/neptune.md) · [Amazon Keyspaces, Timestream e outros bancos especializados](servicos/banco-de-dados/keyspaces-timestream-e-outros.md) |
| 3.8 | [Amazon S3 — armazenamento de objetos](docs/03-tecnologia-e-servicos/08-s3.md) | [Amazon S3](servicos/armazenamento/s3.md) · [Classes de armazenamento do S3](servicos/armazenamento/s3-classes-de-armazenamento.md) |
| 3.9 | [Outros serviços de armazenamento](docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md) | [Amazon EBS](servicos/armazenamento/ebs.md) · [Amazon EFS](servicos/armazenamento/efs.md) · [Amazon FSx](servicos/armazenamento/fsx.md) · [AWS Storage Gateway](servicos/armazenamento/storage-gateway.md) · [AWS Backup](servicos/armazenamento/aws-backup.md) · [AWS Elastic Disaster Recovery](servicos/armazenamento/elastic-disaster-recovery.md) · [Família AWS Snow](servicos/migracao/snow-family.md) · [AWS DataSync e AWS Transfer Family](servicos/migracao/datasync-e-transfer-family.md) |
| 3.10 | [Rede e entrega de conteúdo](docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) | [Amazon VPC](servicos/redes/vpc.md) · [VPC Peering, Transit Gateway, VPC Endpoints e PrivateLink](servicos/redes/vpc-peering-transit-gateway-e-endpoints.md) · [AWS VPN](servicos/redes/site-to-site-vpn-e-client-vpn.md) · [AWS Direct Connect](servicos/redes/direct-connect.md) · [Amazon Route 53](servicos/redes/route-53.md) · [Amazon CloudFront](servicos/redes/cloudfront.md) · [AWS Global Accelerator](servicos/redes/global-accelerator.md) · [Amazon API Gateway](servicos/redes/api-gateway.md) |
| 3.11 | [Analytics](docs/03-tecnologia-e-servicos/11-analytics.md) | [Amazon Athena](servicos/analytics/athena.md) · [AWS Glue](servicos/analytics/glue.md) · [Amazon Kinesis e Amazon Data Firehose](servicos/analytics/kinesis.md) · [Amazon EMR](servicos/analytics/emr.md) · [Amazon QuickSight](servicos/analytics/quicksight.md) · [Amazon OpenSearch Service](servicos/analytics/opensearch.md) · [Amazon Redshift](servicos/banco-de-dados/redshift.md) · [Lake Formation, MSK, Data Exchange, AppFlow e outros serviços de dados](servicos/analytics/lake-formation-msk-e-outros.md) |
| 3.12 | [IA e machine learning](docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md) | [Amazon SageMaker AI](servicos/ia-ml/sagemaker-ai.md) · [Amazon Bedrock](servicos/ia-ml/bedrock.md) · [Amazon Q](servicos/ia-ml/amazon-q.md) · [Serviços de IA prontos](servicos/ia-ml/servicos-de-ia-prontos.md) |
| 3.13 | [Integração de aplicações](docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md) | [Amazon SQS](servicos/integracao/sqs.md) · [Amazon SNS](servicos/integracao/sns.md) · [Amazon EventBridge](servicos/integracao/eventbridge.md) · [AWS Step Functions](servicos/integracao/step-functions.md) · [Amazon MQ](servicos/integracao/amazon-mq.md) |
| 3.14 | [Aplicações de negócio, usuário final, front-end e IoT](docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md) | [Amazon Connect](servicos/aplicacoes/amazon-connect.md) · [Amazon SES](servicos/aplicacoes/ses.md) · [Amazon WorkSpaces, AppStream 2.0 e WorkSpaces Secure Browser](servicos/aplicacoes/workspaces-e-appstream.md) · [AWS Amplify, AWS AppSync e AWS Device Farm](servicos/aplicacoes/amplify-e-appsync.md) · [AWS IoT Core, IoT Greengrass e outros serviços de IoT](servicos/aplicacoes/iot-core-e-greengrass.md) |
| 3.15 | [Ferramentas de desenvolvimento](docs/03-tecnologia-e-servicos/15-ferramentas-de-desenvolvimento.md) | [Ferramentas de CI/CD: CodeCommit, CodeBuild, CodeDeploy, CodePipeline, CodeArtifact](servicos/desenvolvimento/code-services.md) · [AWS X-Ray](servicos/desenvolvimento/x-ray.md) · [Formas de acesso: Console, CLI, SDKs, CloudShell](servicos/desenvolvimento/cli-sdk-e-cloudshell.md) |
| 3.16 | [Gestão e governança](docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md) | [AWS CloudFormation](servicos/gerenciamento/cloudformation.md) · [AWS Systems Manager](servicos/gerenciamento/systems-manager.md) · [AWS Health Dashboard](servicos/gerenciamento/health-dashboard.md) · [AWS Trusted Advisor](servicos/gerenciamento/trusted-advisor.md) · [AWS Compute Optimizer, Service Quotas, License Manager e outros](servicos/gerenciamento/compute-optimizer-service-quotas-e-license-manager.md) · [AWS Organizations](servicos/gerenciamento/organizations.md) |
| 3.17 | [Migração e transferência](docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md) | [Migration Evaluator, Application Discovery Service e Migration Hub](servicos/migracao/discovery-migration-hub-e-evaluator.md) · [AWS Application Migration Service](servicos/migracao/application-migration-service.md) · [AWS Database Migration Service](servicos/migracao/dms-e-sct.md) · [Família AWS Snow](servicos/migracao/snow-family.md) · [AWS DataSync e AWS Transfer Family](servicos/migracao/datasync-e-transfer-family.md) |
| 3.18 | [Serviços menos conhecidos que podem aparecer](docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md) | [Lake Formation, MSK, Data Exchange, AppFlow e outros serviços de dados](servicos/analytics/lake-formation-msk-e-outros.md) · [Amazon MQ](servicos/integracao/amazon-mq.md) · [AWS Firewall Manager e AWS Network Firewall](servicos/seguranca/firewall-manager-e-network-firewall.md) · [Amazon Keyspaces, Timestream e outros bancos especializados](servicos/banco-de-dados/keyspaces-timestream-e-outros.md) · [Serviços de IA prontos](servicos/ia-ml/servicos-de-ia-prontos.md) · [Serviços de mídia e jogos](servicos/fora-do-escopo/midia-e-jogos.md) · [IoT, robótica, satélite e visão computacional na borda](servicos/fora-do-escopo/iot-robotica-e-satelite.md) · [Desenvolvimento e aplicações](servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md) · [Rede e diretório](servicos/fora-do-escopo/rede-e-diretorio.md) · [Gerenciamento e custos](servicos/fora-do-escopo/gerenciamento-e-custos.md) |

### Domínio 4 — Cobrança, Preços e Suporte — 12% da prova

➡️ [Visão geral do domínio](docs/04-cobranca-precos-e-suporte/README.md) · 🃏 [Flashcards](flashcards/dominio-4.md) · ❓ [Questões do domínio](simulados/questoes/dominio-4.md) · 6 tópicos

| # | Tópico | Fichas para abrir junto |
|---|---|---|
| 4.1 | [Princípios de preço da AWS](docs/04-cobranca-precos-e-suporte/01-principios-de-preco.md) | — |
| 4.2 | [Modelos de compra do EC2](docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) | [Amazon EC2](servicos/computacao/ec2.md) |
| 4.3 | [Como outros recursos são cobrados](docs/04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) | [Amazon S3](servicos/armazenamento/s3.md) · [Amazon EBS](servicos/armazenamento/ebs.md) · [AWS Lambda](servicos/computacao/lambda.md) |
| 4.4 | [Ferramentas de custo e faturamento](docs/04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md) | [AWS Cost Explorer](servicos/custos/cost-explorer.md) · [AWS Budgets](servicos/custos/budgets.md) · [Pricing Calculator, Cost and Usage Report e outras ferramentas de faturamento](servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md) |
| 4.5 | [Planos de AWS Support](docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md) | [Planos de AWS Support](servicos/custos/planos-de-suporte.md) · [AWS Trusted Advisor](servicos/gerenciamento/trusted-advisor.md) |
| 4.6 | [Outros recursos de ajuda](docs/04-cobranca-precos-e-suporte/06-outros-recursos-de-ajuda.md) | [Recursos de ajuda, parceiros e serviços ao cliente](servicos/custos/recursos-de-ajuda-e-parceiros.md) · [Planos de AWS Support](servicos/custos/planos-de-suporte.md) |

## 5. Serviços AWS: todas as fichas

Cada ficha explica um serviço do jeito que a prova cobra: o que é, para que serve, configurações, limites, preço, responsabilidade compartilhada, pegadinhas e perguntas típicas. A coluna **Prova** mostra se o serviço está na [lista oficial](docs/00-guia-do-exame/escopo-oficial.md): ✅ no escopo · 🔀 parte dos serviços da ficha está no escopo · ⚪ não aparece na lista · ❌ fora do escopo.

> Índice só das fichas: [servicos/README.md](servicos/README.md).

### 🖥️ Computação

| Ficha | O que é | Prova |
|---|---|---|
| [Amazon EC2](servicos/computacao/ec2.md) | Servidores virtuais sob demanda, com controle total do sistema operacional (IaaS). | ✅ |
| [Amazon EC2 Auto Scaling](servicos/computacao/ec2-auto-scaling.md) | Aumenta e reduz automaticamente o número de instâncias EC2 conforme a demanda e substitui as que falham. | ✅ |
| [Elastic Load Balancing](servicos/computacao/elastic-load-balancing.md) | Distribui automaticamente o tráfego entre destinos saudáveis (EC2, contêineres, IPs, Lambda) em várias AZs. | ✅ |
| [AWS Lambda](servicos/computacao/lambda.md) | Executa seu código em resposta a eventos, sem servidores, cobrando só pelo tempo de execução. | ✅ |
| [Amazon ECS](servicos/computacao/ecs.md) | Orquestrador de contêineres próprio da AWS, totalmente gerenciado e integrado aos demais serviços. | ✅ |
| [Amazon EKS](servicos/computacao/eks.md) | Kubernetes gerenciado — a AWS opera o plano de controle e você roda seus pods. | ✅ |
| [AWS Fargate](servicos/computacao/fargate.md) | Motor serverless que executa contêineres do ECS ou EKS sem você provisionar ou gerenciar servidores. | ✅ |
| [Amazon ECR](servicos/computacao/ecr.md) | Registro gerenciado para guardar, versionar e distribuir imagens de contêiner (Docker/OCI). | ✅ |
| [AWS Elastic Beanstalk](servicos/computacao/elastic-beanstalk.md) | Você envia o código e o Beanstalk provisiona e gerencia capacidade, balanceamento, escalonamento e monitoramento. | ✅ |
| [Amazon Lightsail](servicos/computacao/lightsail.md) | Servidores virtuais e serviços prontos com **preço mensal fixo e previsível**, para quem está começando. | ✅ |
| [AWS Batch](servicos/computacao/batch.md) | Executa grandes volumes de jobs em lote, escolhendo e provisionando automaticamente a computação ideal. | ✅ |
| [AWS Outposts, Local Zones e Wavelength](servicos/computacao/outposts-local-zones-wavelength.md) | Três formas de levar a infraestrutura AWS para mais perto de onde a latência ou a localização dos dados importam. | 🔀 Outposts ✅ · Local Zones ⚪ não listado · Wavelength ❌ fora do escopo |

### 🗄️ Armazenamento

| Ficha | O que é | Prova |
|---|---|---|
| [Amazon S3](servicos/armazenamento/s3.md) | Armazenamento de objetos ilimitado, com 11 noves de durabilidade, acessado via API/HTTP. | ✅ |
| [Classes de armazenamento do S3](servicos/armazenamento/s3-classes-de-armazenamento.md) | Cada classe troca custo de armazenamento por custo/tempo de acesso — escolha pelo padrão de acesso. | ✅ |
| [Amazon EBS](servicos/armazenamento/ebs.md) | Discos virtuais persistentes, em rede, para instâncias EC2 — como um HD/SSD que sobrevive ao desligamento. | ✅ |
| [Amazon EFS](servicos/armazenamento/efs.md) | Sistema de arquivos NFS gerenciado e elástico, compartilhado por milhares de instâncias Linux em várias AZs. | ✅ |
| [Amazon FSx](servicos/armazenamento/fsx.md) | Sistemas de arquivos populares de terceiros (Windows, Lustre, NetApp ONTAP, OpenZFS) totalmente gerenciados. | 🔀 FSx ✅ · FSx for Lustre ❌ fora do escopo |
| [AWS Storage Gateway](servicos/armazenamento/storage-gateway.md) | Liga aplicações on-premises ao armazenamento da AWS usando protocolos padrão (NFS, SMB, iSCSI), com cache local. | ✅ |
| [AWS Backup](servicos/armazenamento/aws-backup.md) | Centraliza e automatiza backups de vários serviços AWS com políticas, num só lugar. | ✅ |
| [AWS Elastic Disaster Recovery](servicos/armazenamento/elastic-disaster-recovery.md) | Replica servidores continuamente (on-premises, outra nuvem ou outra região AWS) para a AWS e permite recuperá-los em minutos. | ✅ |

### 🛢️ Banco de dados

| Ficha | O que é | Prova |
|---|---|---|
| [Amazon RDS](servicos/banco-de-dados/rds.md) | Banco relacional gerenciado — a AWS cuida de hardware, SO, patches do motor, backups e failover. | ✅ |
| [Amazon Aurora](servicos/banco-de-dados/aurora.md) | Banco relacional compatível com MySQL e PostgreSQL, com desempenho e disponibilidade de nível comercial a custo de open source. | ✅ |
| [Amazon DynamoDB](servicos/banco-de-dados/dynamodb.md) | Banco chave-valor e de documentos, serverless, com latência de milissegundos de um dígito em qualquer escala. | ✅ |
| [Amazon ElastiCache](servicos/banco-de-dados/elasticache.md) | Cache em memória gerenciado (Valkey, Redis OSS, Memcached) com latência de microssegundos. | ✅ |
| [Amazon MemoryDB](servicos/banco-de-dados/memorydb.md) | Banco de dados **primário** em memória, compatível com Valkey/Redis, com durabilidade multi-AZ. | ❌ Fora do escopo |
| [Amazon Redshift](servicos/banco-de-dados/redshift.md) | Data warehouse colunar e massivamente paralelo (MPP) para análises SQL (OLAP) sobre terabytes a petabytes. | ✅ |
| [Amazon DocumentDB](servicos/banco-de-dados/documentdb.md) | Banco de documentos JSON gerenciado, compatível com as APIs e drivers do MongoDB. | ✅ |
| [Amazon Neptune](servicos/banco-de-dados/neptune.md) | Banco de grafos gerenciado para dados altamente conectados (relacionamentos). | ✅ |
| [Amazon Keyspaces, Timestream e outros bancos especializados](servicos/banco-de-dados/keyspaces-timestream-e-outros.md) | A AWS tem um banco "sob medida" para cada modelo de dados — saiba associar o modelo ao serviço. | 🔀 Keyspaces e MemoryDB ❌ fora do escopo · Timestream ⚪ não listado |

### 🌐 Redes e entrega de conteúdo

| Ficha | O que é | Prova |
|---|---|---|
| [Amazon VPC](servicos/redes/vpc.md) | Sua rede privada, isolada logicamente, dentro de uma região da AWS. | ✅ |
| [VPC Peering, Transit Gateway, VPC Endpoints e PrivateLink](servicos/redes/vpc-peering-transit-gateway-e-endpoints.md) | Formas de conectar VPCs entre si e de acessar serviços sem passar pela internet. | ✅ |
| [AWS VPN](servicos/redes/site-to-site-vpn-e-client-vpn.md) | Túneis criptografados (IPsec/TLS) pela internet para ligar redes ou usuários à sua VPC. | ✅ |
| [AWS Direct Connect](servicos/redes/direct-connect.md) | Conexão de rede **física, dedicada e privada** entre seu datacenter e a AWS, sem passar pela internet. | ✅ |
| [Amazon Route 53](servicos/redes/route-53.md) | DNS gerenciado e altamente disponível (o "53" é a porta do DNS), com registro de domínios, roteamento inteligente e health checks. | ✅ |
| [Amazon CloudFront](servicos/redes/cloudfront.md) | Rede de distribuição de conteúdo (CDN) que faz **cache** perto dos usuários, reduzindo latência e carga na origem. | ✅ |
| [AWS Global Accelerator](servicos/redes/global-accelerator.md) | Fornece **2 IPs anycast estáticos** e leva o tráfego TCP/UDP pela rede global da AWS até o endpoint saudável mais próximo. | ✅ |
| [Amazon API Gateway](servicos/redes/api-gateway.md) | Cria, publica, protege e monitora APIs em qualquer escala — a "porta da frente" de back-ends serverless. | ✅ |

### 🔐 Segurança, identidade e compliance

| Ficha | O que é | Prova |
|---|---|---|
| [AWS IAM](servicos/seguranca/iam.md) | Controla **quem** pode se autenticar e **o que** cada identidade pode fazer em quais recursos da conta. | ✅ |
| [AWS IAM Identity Center](servicos/seguranca/iam-identity-center.md) | Login único (SSO) para que **funcionários** acessem várias contas AWS e aplicações SaaS com um só usuário. | ✅ |
| [Amazon Cognito](servicos/seguranca/cognito.md) | Cadastro, login e controle de acesso para **usuários finais** de aplicações web e mobile. | ✅ |
| [AWS Directory Service](servicos/seguranca/directory-service.md) | Microsoft Active Directory gerenciado na AWS, ou ponte para o AD on-premises. | ✅ |
| [AWS KMS](servicos/seguranca/kms.md) | Cria e controla chaves de criptografia integradas a mais de 100 serviços AWS, com auditoria de cada uso. | ✅ |
| [AWS CloudHSM](servicos/seguranca/cloudhsm.md) | HSM (hardware security module) **dedicado e exclusivo** na nuvem, em que só você controla as chaves. | ✅ |
| [AWS Certificate Manager](servicos/seguranca/certificate-manager.md) | Emite, gerencia e **renova automaticamente** certificados SSL/TLS — os públicos são gratuitos. | ✅ |
| [AWS Secrets Manager e Systems Manager Parameter Store](servicos/seguranca/secrets-manager-e-parameter-store.md) | Guardam segredos e configurações fora do código, criptografados com KMS — o Secrets Manager também os **rotaciona automaticamente**. | ✅ |
| [AWS Shield](servicos/seguranca/shield.md) | Proteção gerenciada contra ataques de negação de serviço distribuída (DDoS). | ✅ |
| [AWS WAF](servicos/seguranca/waf.md) | Firewall de **camada 7** que filtra requisições HTTP(S) maliciosas antes que cheguem à aplicação. | ✅ |
| [AWS Firewall Manager e AWS Network Firewall](servicos/seguranca/firewall-manager-e-network-firewall.md) | O Firewall Manager **governa** regras de firewall em todas as contas; o Network Firewall **é** um firewall gerenciado para a VPC. | 🔀 Firewall Manager ✅ · Network Firewall ❌ fora do escopo |
| [Amazon GuardDuty](servicos/seguranca/guardduty.md) | Detecção inteligente e contínua de **ameaças ativas** usando machine learning, detecção de anomalias e inteligência de ameaças. | ✅ |
| [Amazon Inspector](servicos/seguranca/inspector.md) | Varre continuamente cargas de trabalho em busca de **vulnerabilidades de software (CVEs)** e exposição de rede não intencional. | ✅ |
| [Amazon Macie](servicos/seguranca/macie.md) | Usa machine learning e padrões para **descobrir e proteger dados sensíveis (PII) no Amazon S3**. | ✅ |
| [Amazon Detective](servicos/seguranca/detective.md) | Facilita **investigar a causa raiz** de achados de segurança, montando um grafo de comportamento a partir dos logs. | ✅ |
| [AWS Security Hub](servicos/seguranca/security-hub.md) | **painel central** de segurança que agrega achados de vários serviços e verifica a conta contra padrões de boas práticas. | ✅ |
| [AWS Artifact](servicos/seguranca/artifact.md) | Portal de autoatendimento para baixar **relatórios de conformidade da AWS** e aceitar **acordos** legais. | ✅ |
| [AWS Audit Manager](servicos/seguranca/audit-manager.md) | Coleta **evidências da sua conta** continuamente e as mapeia para frameworks, para preparar as suas auditorias. | ⚪ Não listado (saiu da lista atual) |

### ⚙️ Gerenciamento e governança

| Ficha | O que é | Prova |
|---|---|---|
| [Amazon CloudWatch](servicos/gerenciamento/cloudwatch.md) | Monitoramento de **métricas, logs e alarmes** de recursos e aplicações AWS e on-premises. | ✅ |
| [AWS CloudTrail](servicos/gerenciamento/cloudtrail.md) | Registra as **chamadas de API** da conta — quem fez, o quê, quando, de onde e em qual recurso. | ✅ |
| [AWS Config](servicos/gerenciamento/config.md) | Registra a **configuração** dos recursos e seu histórico de mudanças, e avalia continuamente se estão **conformes** com regras. | ✅ |
| [AWS Systems Manager](servicos/gerenciamento/systems-manager.md) | Central de operações para gerenciar **frotas** de servidores (EC2, on-premises, VMs) em escala, sem acesso manual. | ✅ |
| [AWS CloudFormation](servicos/gerenciamento/cloudformation.md) | Descreve a infraestrutura em templates JSON/YAML e cria tudo de forma **repetível, versionada e automatizada**. | ✅ |
| [AWS Organizations](servicos/gerenciamento/organizations.md) | Gerencia várias contas AWS de forma centralizada, com políticas e **uma fatura única**. | ✅ |
| [AWS Control Tower](servicos/gerenciamento/control-tower.md) | Monta e governa automaticamente um ambiente multi-conta seguro e padronizado (**landing zone**) sobre o Organizations. | ✅ |
| [AWS Service Catalog e AWS Resource Access Manager](servicos/gerenciamento/service-catalog-e-ram.md) | Service Catalog oferece um **catálogo de produtos aprovados** para autoatendimento; RAM **compartilha recursos** entre contas. | ✅ |
| [AWS Trusted Advisor](servicos/gerenciamento/trusted-advisor.md) | Inspeciona sua conta e recomenda melhorias com base nas boas práticas da AWS. | ✅ |
| [AWS Health Dashboard](servicos/gerenciamento/health-dashboard.md) | Mostra o status dos serviços AWS e, principalmente, os eventos que afetam **os seus** recursos. | ✅ |
| [AWS Compute Optimizer, Service Quotas, License Manager e outros](servicos/gerenciamento/compute-optimizer-service-quotas-e-license-manager.md) | Ferramentas para dimensionar recursos, controlar limites e licenças, e organizar o ambiente. | ✅ |

### 📊 Analytics

| Ficha | O que é | Prova |
|---|---|---|
| [Amazon Athena](servicos/analytics/athena.md) | Consultas **SQL serverless** direto em arquivos no S3, pagando só pelos dados escaneados. | ✅ |
| [AWS Glue](servicos/analytics/glue.md) | Serviço **serverless de ETL** e **catálogo de dados** para descobrir, preparar e combinar dados para análise. | ✅ |
| [Amazon Kinesis e Amazon Data Firehose](servicos/analytics/kinesis.md) | Coleta, processa e entrega **dados em streaming e tempo real** (cliques, logs, telemetria, vídeo). | ✅ |
| [Amazon EMR](servicos/analytics/emr.md) | Plataforma gerenciada de **big data** para rodar Apache Spark, Hadoop, Hive, Presto/Trino, HBase e Flink. | ✅ |
| [Amazon QuickSight](servicos/analytics/quicksight.md) | BI **serverless** para criar dashboards e relatórios interativos, inclusive com perguntas em linguagem natural. | ✅ |
| [Amazon OpenSearch Service](servicos/analytics/opensearch.md) | Busca de texto, análise de logs e observabilidade com OpenSearch (sucessor do Elasticsearch gerenciado). | ✅ |
| [Lake Formation, MSK, Data Exchange, AppFlow e outros serviços de dados](servicos/analytics/lake-formation-msk-e-outros.md) | Serviços de dados que aparecem como "qual serviço faz X" — saiba a função de cada um. | 🔀 MSK, AppFlow, Data Exchange, Clean Rooms e DataZone ❌ fora do escopo · Lake Formation ⚪ não listado |

### 🤖 IA e machine learning

| Ficha | O que é | Prova |
|---|---|---|
| [Amazon SageMaker AI](servicos/ia-ml/sagemaker-ai.md) | Plataforma completa para **construir, treinar e implantar modelos de ML próprios**. | ✅ |
| [Amazon Bedrock](servicos/ia-ml/bedrock.md) | Acesso **serverless via API** a modelos de fundação (foundation models) de vários provedores para criar aplicações de IA generativa. | ⚪ Não listado |
| [Amazon Q](servicos/ia-ml/amazon-q.md) | Família de **assistentes de IA generativa** prontos para desenvolvedores e para dados corporativos. | ✅ |
| [Serviços de IA prontos](servicos/ia-ml/servicos-de-ia-prontos.md) | APIs de IA já treinadas pela AWS — você não precisa de experiência em ML, só chama a API. | 🔀 Comprehend, Lex, Polly, Rekognition, Textract, Transcribe e Translate ✅ · Kendra ⚪ não listado · Personalize e Fraud Detector ❌ fora do escopo |

### 🔗 Integração de aplicações

| Ficha | O que é | Prova |
|---|---|---|
| [Amazon SQS](servicos/integracao/sqs.md) | Fila de mensagens totalmente gerenciada que **desacopla** produtores e consumidores e absorve picos. | ✅ |
| [Amazon SNS](servicos/integracao/sns.md) | Serviço **pub/sub**: um produtor publica num **tópico** e a mensagem é **empurrada** para todos os assinantes. | ✅ |
| [Amazon EventBridge](servicos/integracao/eventbridge.md) | **barramento de eventos** serverless que recebe eventos de serviços AWS, das suas aplicações e de parceiros SaaS e os roteia por **regras**. | ✅ |
| [AWS Step Functions](servicos/integracao/step-functions.md) | Orquestra **fluxos de trabalho de várias etapas** como máquinas de estado visuais, com tratamento de erros e retentativas. | ✅ |
| [Amazon MQ](servicos/integracao/amazon-mq.md) | Brokers de mensagens gerenciados **Apache ActiveMQ** e **RabbitMQ**, compatíveis com protocolos padrão. | ⚪ Não listado |

### 🛠️ Ferramentas de desenvolvedor

| Ficha | O que é | Prova |
|---|---|---|
| [Formas de acesso: Console, CLI, SDKs, CloudShell](servicos/desenvolvimento/cli-sdk-e-cloudshell.md) | Toda ação na AWS é uma **chamada de API** — Console, CLI e SDKs são apenas formas diferentes de fazê-la. | 🔀 CLI e Management Console ✅ · CloudShell ❌ fora do escopo · Cloud9 ⚪ não listado |
| [Ferramentas de CI/CD: CodeCommit, CodeBuild, CodeDeploy, CodePipeline, CodeArtifact](servicos/desenvolvimento/code-services.md) | Serviços gerenciados que cobrem a esteira **código → build → teste → deploy**. | 🔀 CodeBuild e CodePipeline ✅ · CodeDeploy e CodeArtifact ❌ fora do escopo · CodeCommit e CodeStar ⚪ não listados |
| [AWS X-Ray](servicos/desenvolvimento/x-ray.md) | **rastreamento distribuído** — acompanha cada requisição através dos microsserviços para achar gargalos e erros. | ✅ |

### 💼 Aplicações de negócio, usuário final e IoT

| Ficha | O que é | Prova |
|---|---|---|
| [Amazon Connect](servicos/aplicacoes/amazon-connect.md) | **central de atendimento (contact center) omnicanal na nuvem**, pronta em minutos e paga por uso. | ✅ |
| [Amazon SES](servicos/aplicacoes/ses.md) | Envio (e recebimento) de **e-mails** transacionais e de marketing em grande volume. | ✅ |
| [Amazon WorkSpaces, AppStream 2.0 e WorkSpaces Secure Browser](servicos/aplicacoes/workspaces-e-appstream.md) | Entregam desktops, aplicações ou um navegador seguro hospedados na AWS para qualquer dispositivo. | ✅ |
| [AWS Amplify, AWS AppSync e AWS Device Farm](servicos/aplicacoes/amplify-e-appsync.md) | Ferramentas para criar, hospedar, conectar e testar aplicações web e mobile rapidamente. | 🔀 Amplify ✅ · AppSync ⚪ não listado · Device Farm ❌ fora do escopo |
| [AWS IoT Core, IoT Greengrass e outros serviços de IoT](servicos/aplicacoes/iot-core-e-greengrass.md) | Conectar, gerenciar e processar dados de bilhões de dispositivos com segurança — na nuvem e na borda. | 🔀 IoT Core ✅ · IoT Greengrass ❌ fora do escopo |

### 🚚 Migração e transferência

| Ficha | O que é | Prova |
|---|---|---|
| [Migration Evaluator, Application Discovery Service e Migration Hub](servicos/migracao/discovery-migration-hub-e-evaluator.md) | As ferramentas das fases **avaliar → planejar → acompanhar** de uma migração. | ✅ |
| [AWS Application Migration Service](servicos/migracao/application-migration-service.md) | Migração **lift-and-shift (Rehost)** de servidores físicos, virtuais ou de outras nuvens para EC2, com mínima indisponibilidade. | ✅ |
| [AWS Database Migration Service](servicos/migracao/dms-e-sct.md) | O DMS **move os dados** (com o banco de origem funcionando); o SCT **converte o schema** entre motores diferentes. | ✅ |
| [Família AWS Snow](servicos/migracao/snow-family.md) | Dispositivos físicos robustos para **mover grandes volumes de dados** quando a rede é lenta, cara ou inexistente, e para **computação na borda** desconectada. | ⚪ Não listado (saiu da lista atual) |
| [AWS DataSync e AWS Transfer Family](servicos/migracao/datasync-e-transfer-family.md) | DataSync **move dados online** de forma automatizada e rápida; Transfer Family oferece **SFTP/FTPS/FTP** gerenciado com armazenamento em S3/EFS. | 🔀 DataSync ⚪ não listado · Transfer Family ❌ fora do escopo |

### 💰 Custos e suporte

| Ficha | O que é | Prova |
|---|---|---|
| [AWS Cost Explorer](servicos/custos/cost-explorer.md) | Visualiza, analisa e **prevê** seus custos e uso da AWS ao longo do tempo. | ✅ |
| [AWS Budgets](servicos/custos/budgets.md) | Define orçamentos de custo e uso e **alerta** (ou **age**) quando o valor real ou **previsto** ultrapassa o limite. | ✅ |
| [Pricing Calculator, Cost and Usage Report e outras ferramentas de faturamento](servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md) | Ferramentas para estimar, detalhar, ratear, otimizar e acompanhar os custos da AWS. | ✅ |
| [Planos de AWS Support](servicos/custos/planos-de-suporte.md) | Níveis de suporte técnico da AWS — quanto mais alto, mais rápido o atendimento e mais acompanhamento proativo. | ✅ |
| [Recursos de ajuda, parceiros e serviços ao cliente](servicos/custos/recursos-de-ajuda-e-parceiros.md) | Além dos planos de suporte, a AWS oferece comunidade, documentação, consultoria, parceiros e operação terceirizada — a prova pede quem procurar em cada situação. | 🔀 Marketplace, APN, Professional Services, Prescriptive Guidance, Knowledge Center, re:Post e Trust and Safety ✅ (task 4.3) · AWS IQ, Activate e AMS ❌ fora do escopo |

### ❌ Fora do escopo da prova (só para referência)

<details>
<summary>Serviços que <b>não caem</b> na prova — abra para ver (5 fichas)</summary>

| Ficha | O que é | Prova |
|---|---|---|
| [Serviços de mídia e jogos](servicos/fora-do-escopo/midia-e-jogos.md) | Serviços para processar e transmitir vídeo e para hospedar jogos — úteis para conhecer, mas a prova os usa só como distratores. | ❌ Fora do escopo — documentado só para referência |
| [IoT, robótica, satélite e visão computacional na borda](servicos/fora-do-escopo/iot-robotica-e-satelite.md) | Serviços especializados para dispositivos, robôs, satélites e câmeras inteligentes — fora da prova, que só cobra o IoT Core. | ❌ Fora do escopo — documentado só para referência |
| [Desenvolvimento e aplicações](servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md) | Ferramentas de desenvolvimento, modernização e colaboração que existem na AWS, mas não caem na prova. | ❌ Fora do escopo — documentado só para referência |
| [Rede e diretório](servicos/fora-do-escopo/rede-e-diretorio.md) | Serviços de rede de aplicação e de diretório que complementam a VPC, mas não caem na prova. | ❌ Fora do escopo — documentado só para referência |
| [Gerenciamento e custos](servicos/fora-do-escopo/gerenciamento-e-custos.md) | Ferramentas auxiliares de operação e de cobrança que existem na AWS, mas não caem na prova. | ❌ Fora do escopo — documentado só para referência |

</details>

<!-- indice:fim -->

---

## 6. Revisão final

Use na última semana e na véspera da prova:

| Material | Para quê |
|---|---|
| ⚖️ [Pares que confundem](resumos/comparativos.md) | Diferença entre serviços parecidos (CloudTrail × CloudWatch, SQS × SNS, Shield × WAF…) |
| 🔑 [Palavras-chave → serviço](resumos/palavras-chave.md) | Termos do enunciado que já indicam a resposta ("DDoS" → Shield, "PII no S3" → Macie…) |
| 📌 [Números-âncora](resumos/numeros-ancora.md) | Números que decidem a questão (15 min do Lambda, 2 min do Spot, 11 noves do S3…) e o que não decorar |
| 🔄 [O que mudou em 2025-2026](docs/00-guia-do-exame/atualizacoes-2025-2026.md) | As mudanças recentes, com datas |
| 🎯 [Escopo oficial](docs/00-guia-do-exame/escopo-oficial.md) | O que cai e o que não cai (serviços fora do escopo costumam ser distratores) |
| 📖 [Glossário](glossario.md) | Termos e siglas |
| 📋 [Resumos (índice)](resumos/README.md) | Todos os resumos num só lugar |

---

## 7. Acompanhe seu estudo

| | |
|---|---|
| ✅ [Progresso](progresso.md) | Marque cada tópico estudado e os marcos até a aprovação |
| 🗓️ [Plano de estudos](docs/00-guia-do-exame/plano-de-estudos.md) | Cronograma de 6 semanas, ~1 hora por dia |
| 📝 [Registro de simulados](simulados/README.md) | Anote a nota de cada simulado (use o [modelo](templates/simulado.md)) |
| 🔁 [Erros recorrentes](simulados/erros-recorrentes.md) | Liste os conceitos que você errou mais de uma vez |
| 🧪 [Labs](labs/README.md) | 13 práticas no console AWS (opcionais), começando por um alerta de custo |
| 🔗 [Links úteis](recursos/links-uteis.md) | Páginas oficiais: exam guide, Skill Builder, preços, planos de suporte |

---

## 8. Fontes e confiabilidade

O conteúdo vem de um guia de estudo e de uma pesquisa próprios, conferidos depois em várias rodadas nas páginas
oficiais da AWS. Quando a verificação encontrou algo diferente, o repositório foi corrigido e a mudança aparece
marcada com 🔄 ou ✔️.

| Documento | O que é |
|---|---|
| [Índice das fontes](fontes/README.md) | Como cada fonte foi usada |
| [Guia completo CLF-C02](fontes/guia-completo-clf-c02.md) | Guia de estudo original, base dos tópicos e flashcards |
| [Pesquisa 2025-2026](fontes/pesquisa-atualizacoes-2025-2026.md) | Pesquisa sobre números que caem e mudanças recentes |
| [Verificação oficial (10/2026)](fontes/verificacao-fontes-oficiais-2026-10.md) | Exam guide, escopo, mudanças e números |
| [Verificação — rodadas 3 e 4](fontes/verificacao-fontes-oficiais-2026-10-rodadas-3-4.md) | Termos de cada task, planos de suporte, status de serviços |
| [Verificação das pendências (PDF)](fontes/verificacao-pendencias-2026-10.pdf) | Primeira rodada das pendências |
| [Verificação das pendências — rodada 2](fontes/verificacao-pendencias-2026-10-rodada-2.md) | Rodada final, com trecho literal de cada página oficial |
| [Pendências de verificação](docs/00-guia-do-exame/pendencias-de-verificacao.md) | O que ainda falta conferir (hoje: nada) |

> Preços, limites e nomes de planos mudam. Na semana da prova, confira o
> [exam guide oficial](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)
> e a [lista de serviços no escopo](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html).

---

## 9. Para quem mantém o repositório

<details>
<summary>Scripts, convenções e estrutura de pastas (clique para ver)</summary>

**Regras do repositório:** [CLAUDE.md](CLAUDE.md) (fluxo por Pull Request, passos antes de abrir PR e convenções).

**Scripts** (rodar a partir da raiz):

```bash
python3 scripts/gerar_docs.py      # regenera tópicos, flashcards, resumos, índice de fichas e os blocos gerados deste README
python3 scripts/gerar_simulado.py  # regenera o simulado e as questões por domínio
python3 scripts/verificar_links.py # confere se todos os links internos funcionam
```

| Script / modelo | Função |
|---|---|
| [scripts/gerar_docs.py](scripts/gerar_docs.py) | Gera os tópicos a partir de `fontes/`, aplica `CORRECOES` e `AVISOS`, mantém `FICHAS` e `ESCOPO` |
| [scripts/extras_pesquisa.py](scripts/extras_pesquisa.py) | Inseriu os complementos da pesquisa nos tópicos (uso único) |
| [scripts/banco_questoes.py](scripts/banco_questoes.py) | Banco das 65 questões (enunciado, alternativas e explicação) |
| [scripts/gerar_simulado.py](scripts/gerar_simulado.py) | Gera o simulado e as questões por domínio |
| [scripts/verificar_links.py](scripts/verificar_links.py) | Verificador de links internos |
| [templates/topico.md](templates/topico.md) · [templates/servico.md](templates/servico.md) · [templates/simulado.md](templates/simulado.md) | Modelos de tópico, ficha e registro de simulado |

**Dicas de uso:**
- Anotações pessoais vão na seção *📝 Minhas anotações* de cada tópico; ela é preservada ao regenerar.
- Novo serviço: copie o modelo de ficha para `servicos/<categoria>/` e registre-o em `FICHAS` e `ESCOPO`.
- Nunca faça commit de credenciais AWS (chaves de acesso, `.pem`, IDs de conta).

**Estrutura de pastas:**

```
.
├── docs/                    # Tópicos da prova (gerados a partir de fontes/)
│   ├── 00-guia-do-exame/    # Formato, escopo oficial, plano, atualizações, pendências
│   ├── 01-conceitos-de-nuvem/          # 1.1 a 1.7
│   ├── 02-seguranca-e-conformidade/    # 2.1 a 2.10
│   ├── 03-tecnologia-e-servicos/       # 3.1 a 3.18
│   └── 04-cobranca-precos-e-suporte/   # 4.1 a 4.6
├── servicos/                # Fichas de serviços por categoria (inclui fora do escopo)
├── flashcards/              # Gerados das perguntas típicas (Markdown + TSV para Anki)
├── simulados/               # Simulado, questões por domínio e registro de erros
├── resumos/                 # Comparativos, palavras-chave, números-âncora
├── labs/                    # Práticas no console
├── fontes/                  # Documentos originais e verificações oficiais
├── templates/               # Modelos
├── scripts/                 # Geração e verificação
├── recursos/                # Links úteis
├── assets/imagens/          # Diagramas e prints
├── glossario.md
└── progresso.md
```

</details>
