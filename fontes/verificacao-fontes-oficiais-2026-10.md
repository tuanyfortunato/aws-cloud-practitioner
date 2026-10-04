# AWS Certified Cloud Practitioner (CLF-C02): verificação em fontes oficiais

> Consultado em **04/10/2026**. Prova: **CLF-C02**.
> Fontes aceitas: docs.aws.amazon.com, aws.amazon.com (produto, preços, certificação), AWS What's New, AWS News Blog e repost.aws/knowledge-center.
> Também aparecem algumas páginas oficiais da AWS China (amazonaws.cn), sempre sinalizadas.

## Legenda de status

| Status | Significado |
|---|---|
| **CONFIRMA** | A fonte oficial confirma o valor informado |
| **DIVERGE** | A fonte oficial traz outro valor; o valor correto está na tabela |
| **NÃO ENCONTRADO** | Procurei e não achei confirmação em fonte oficial |

> ⚠️ O código da prova continua CLF-C02, mas o conteúdo do exam guide é atualizado sem troca de código. Reabra o guia e a página da certificação alguns dias antes da prova.

---

## Parte 1: exam guide e escopo

Exam guide (HTML): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html
PDF: https://docs.aws.amazon.com/pdfs/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.pdf (© 2026)
Página da certificação: https://aws.amazon.com/certification/certified-cloud-practitioner/ (atualizada em 25/09/2026)

### 1. Formato da prova

| Item | Valor informado | Valor oficial | Status |
|---|---|---|---|
| Versão do guia | — | O guia atual não mostra número de versão. O PDF antigo (d1.awsstatic.com) trazia "Version 1.0" | Sem número de versão no guia atual |
| Questões | 65 (50 + 15) | 65 questões: 50 pontuadas e 15 não pontuadas, sem identificação na prova | CONFIRMA |
| Duração | 90 min | 90 minutos | CONFIRMA |
| Custo | — | 100 USD | — |
| Nota | 700/1000 | Escala de 100 a 1.000, mínimo de 700. Modelo compensatório: não há nota mínima por seção | CONFIRMA |
| Tipos de questão | — | Múltipla escolha: 1 correta e 3 distratores. Múltipla resposta: 2 ou mais corretas entre 5 ou mais opções. Questão em branco conta como erro, sem penalidade por chute | CONFIRMA |
| Pesos | D1 24%, D2 30%, D3 34%, D4 12% | D1 24%, D2 30%, D3 34%, D4 12% | CONFIRMA |
| Idiomas | — | Inclui Português (Brasil). Italiano e alemão serão retirados após 31/12/2026 | — |
| Validade | — | 3 anos | — |

### 2. Task statements (títulos oficiais)

O detalhamento de "Knowledge of / Skills in" de cada task está no exam guide.

**Domínio 1: Cloud Concepts (24%)**
- 1.1 Define the benefits of the AWS Cloud.
- 1.2 Identify design principles of the AWS Cloud.
- 1.3 Understand the benefits of and strategies for migration to the AWS Cloud.
- 1.4 Understand concepts of cloud economics.

**Domínio 2: Security and Compliance (30%)**
- 2.1 Understand the AWS shared responsibility model.
- 2.2 Understand AWS Cloud security, governance, and compliance concepts.
- 2.3 Identify AWS access management capabilities.
- 2.4 Identify components and resources for security.

**Domínio 3: Cloud Technology and Services (34%)**
- 3.1 Define methods of deploying and operating in the AWS Cloud.
- 3.2 Define the AWS global infrastructure.
- 3.3 Identify AWS compute services.
- 3.4 Identify AWS database services.
- 3.5 Identify AWS network services.
- 3.6 Identify AWS storage services.
- 3.7 Identify AWS artificial intelligence and machine learning (AI/ML) services and analytics services.
- 3.8 Identify services from other in-scope AWS service categories.

**Domínio 4: Billing, Pricing, and Support (12%)**
- 4.1 Compare AWS pricing models.
- 4.2 Understand resources for billing, budget, and cost management.
- 4.3 Identify AWS technical resources and AWS Support options.

**Pontos atualizados que valem estudo:**
- **1.2:** os seis pilares do Well-Architected (operational excellence, security, reliability, performance efficiency, cost optimization, sustainability).
- **2.3:** inclui AWS IAM Identity Center, proteção do root user e tarefas que só o root pode fazer.
- **3.7:** exemplos atuais são Amazon SageMaker AI, Amazon Lex, Athena, Kinesis, Glue e Amazon Quick Sight.
- **3.8:**
  - end-user computing: AppStream 2.0, WorkSpaces e WorkSpaces Secure Browser;
  - frontend: só o AWS Amplify;
  - IoT: AWS IoT Core;
  - developer tools: CodeBuild, CodePipeline e X-Ray.
- **4.1:** On-Demand, Reserved Instances, Spot, Savings Plans, Dedicated Hosts, Dedicated Instances e Capacity Reservations. Inclui também a flexibilidade de RIs e o comportamento de RIs no AWS Organizations.
- **4.3:**
  - planos de suporte: Basic, AWS Business Support+, AWS Enterprise Support e AWS Unified Operations;
  - Trusted Advisor, Health Dashboard e Health API;
  - AWS Trust and Safety, APN, Marketplace, Professional Services, Prescriptive Guidance, Knowledge Center e re:Post.

### 3. Serviços no escopo, por categoria, como na página

Fonte: https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html. A página avisa que a lista não é exaustiva e pode mudar.

- **Analytics:** Amazon Athena, Amazon EMR, AWS Glue, Amazon Kinesis, Amazon OpenSearch Service, Amazon Quick Sight, Amazon Redshift
- **Application Integration:** Amazon EventBridge, Amazon Simple Notification Service (Amazon SNS), Amazon Simple Queue Service (Amazon SQS), AWS Step Functions
- **Business Applications:** Amazon Connect, Amazon Simple Email Service (Amazon SES)
- **Cloud Financial Management:** AWS Budgets, AWS Cost and Usage Reports, AWS Cost Explorer, AWS Marketplace
- **Compute:** AWS Batch, Amazon EC2, AWS Elastic Beanstalk, Amazon Lightsail, AWS Outposts
- **Containers:** Amazon Elastic Container Registry (Amazon ECR), Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS)
- **Customer Enablement:** AWS Support
- **Database:** Amazon Aurora, Amazon DocumentDB, Amazon DynamoDB, Amazon ElastiCache, Amazon Neptune, Amazon RDS
- **Developer Tools:** AWS CLI, AWS CodeBuild, AWS CodePipeline, AWS X-Ray
- **End User Computing:** Amazon AppStream 2.0, Amazon WorkSpaces, Amazon WorkSpaces Secure Browser
- **Frontend Web and Mobile:** AWS Amplify
- **Internet of Things (IoT):** AWS IoT Core
- **Machine Learning:** Amazon Comprehend, Amazon Lex, Amazon Polly, Amazon Q, Amazon Rekognition, Amazon SageMaker AI, Amazon Textract, Amazon Transcribe, Amazon Translate
- **Management and Governance:** AWS Auto Scaling, AWS CloudFormation, AWS CloudTrail, Amazon CloudWatch, AWS Compute Optimizer, AWS Config, AWS Control Tower, AWS Health Dashboard, AWS License Manager, AWS Management Console, AWS Organizations, AWS Service Catalog, Service Quotas, AWS Systems Manager, AWS Trusted Advisor, AWS Well-Architected Tool
- **Migration and Transfer:** AWS Application Discovery Service, AWS Application Migration Service, AWS Database Migration Service (AWS DMS), Migration Evaluator, AWS Migration Hub, AWS Schema Conversion Tool (AWS SCT)
- **Networking and Content Delivery:** Amazon API Gateway, Amazon CloudFront, AWS Direct Connect, AWS Global Accelerator, AWS PrivateLink, Amazon Route 53, AWS Transit Gateway, Amazon VPC, AWS VPN, AWS Site-to-Site VPN, AWS Client VPN
- **Security, Identity, and Compliance:** AWS Artifact, AWS Certificate Manager (ACM), AWS CloudHSM, Amazon Cognito, Amazon Detective, AWS Directory Service, AWS Firewall Manager, Amazon GuardDuty, AWS Identity and Access Management (IAM), AWS IAM Identity Center, Amazon Inspector, AWS Key Management Service (AWS KMS), Amazon Macie, AWS Resource Access Manager (AWS RAM), AWS Secrets Manager, AWS Security Hub, AWS Shield, AWS WAF
- **Serverless:** AWS Fargate, AWS Lambda
- **Storage:** AWS Backup, Amazon Elastic Block Store (Amazon EBS), Amazon Elastic File System (Amazon EFS), AWS Elastic Disaster Recovery, Amazon FSx, Amazon S3, Amazon S3 Glacier, AWS Storage Gateway

### 4. Fora do escopo

**Tarefas fora do escopo (lista não exaustiva):** programação, design de arquitetura de nuvem, troubleshooting, implementação, e testes de carga e desempenho.

**Serviços fora do escopo (lista não exaustiva):**
- **Analytics:** Amazon AppFlow, AWS Clean Rooms, AWS Data Exchange, Amazon DataZone, Amazon Managed Streaming for Apache Kafka (Amazon MSK)
- **Application Integration:** AWS AppFabric, Amazon Simple Workflow Service
- **Business Applications:** Amazon WorkDocs
- **Compute:** AWS Copilot, AWS Wavelength
- **Cost Management:** AWS Application Cost Profiler, Amazon DevPay
- **Customer Enablement:** AWS Activate, AWS IQ, AWS Managed Services (AMS)
- **Cloud Financial Management:** AWS Billing Conductor
- **Database:** Amazon Keyspaces (for Apache Cassandra), Amazon MemoryDB for Redis OSS, AWS AppConfig (sic: a página lista o AppConfig em Database)
- **Developer Tools:** AWS Application Composer, AWS CodeArtifact, AWS CodeDeploy, Amazon CodeGuru, AWS CloudShell, AWS Device Farm
- **Game Tech:** Amazon GameLift, Amazon Lumberyard
- **Internet of Things (IoT):** AWS IoT Device Defender, AWS IoT Greengrass, Amazon Monitron
- **Machine Learning:** Amazon Fraud Detector, Amazon Lookout for Metrics, AWS Panorama, Amazon Personalize
- **Management and Governance:** AWS Chatbot, Amazon Data Lifecycle Manager, Amazon Elastic Transcoder, AWS Launch Wizard
- **Media Services:** AWS Elemental Appliances and Software, AWS Elemental MediaConnect, AWS Elemental MediaConvert, AWS Elemental MediaLive, AWS Elemental MediaPackage, AWS Elemental MediaStore, AWS Elemental MediaTailor, Amazon Interactive Video Service (Amazon IVS)
- **Migration and Transfer:** AWS Migration Hub Refactor Spaces, AWS Transfer Family
- **Networking and Content Delivery:** AWS Cloud Map, AWS Network Access Analyzer, AWS Ground Station, Amazon VPC Lattice
- **Security, Identity, and Compliance:** Amazon Cloud Directory, AWS Network Firewall
- **Robotics:** AWS RoboMaker
- **Storage:** Amazon FSx for Lustre

### 5. Nova versão da prova (CLF-C03)?

**NÃO ENCONTRADO.** A página da certificação, atualizada em 25/09/2026, só fala da CLF-C02. O conteúdo do guia, porém, foi atualizado (detalhes na seção "Novidades").

---

## Parte 2: mudanças de 2025-2026

| # | Item | Status | Valor oficial encontrado | Fonte | Data |
|---|---|---|---|---|---|
| 1 | S3: objeto de até 50 TB | CONFIRMA | De 5 TB para 50 TB (10x), em todas as classes de armazenamento; não vale para GovCloud | https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-s3-maximum-object-size-50-tb/ | 02/12/2025 |
| 2 | SQS: mensagem de até 1 MiB | CONFIRMA | De 256 KiB para 1 MiB, em filas Standard e FIFO; o event source mapping do Lambda também aceita 1 MiB | https://aws.amazon.com/about-aws/whats-new/2025/08/amazon-sqs-max-payload-size-1mib | 04/08/2025 |
| 3 | SNS: mensagem de até 1 MiB | CONFIRMA, com ressalva | Até 1 MiB só configurando o atributo `MaximumMessageSize` no tópico, em Standard e FIFO. O padrão continua 256 KiB | https://www.amazonaws.cn/en/new/2026/amazon-sns-supports-message-payloads-up-to-1-mib/ e https://docs.aws.amazon.com/sns/latest/api/API_Publish.html | 18/09/2026 |
| 4 | Free Tier | CONFIRMA | US$ 100 no cadastro + até US$ 100 por atividades (EC2, RDS, Lambda, Bedrock, Budgets). O free plan expira em 6 meses ou quando os créditos acabam, o que vier primeiro. Contas criadas antes de 15/07/2025 continuam no Free Tier legado | https://aws.amazon.com/about-aws/whats-new/2025/07/aws-free-tier-credits-month-free-plan/ e AWS News Blog | Anúncio de 16/07/2025, vigente desde 15/07/2025 |
| 5 | Novos planos de suporte | CONFIRMA | Business Support+: mínimo de US$ 29/mês **por conta**. Enterprise: US$ 5.000/mês. Unified Operations: US$ 50.000/mês, com compromisso mínimo de 90 dias. Casos críticos: 30 / 15 / 5 min | https://aws.amazon.com/premiumsupport/pricing/ e https://aws.amazon.com/about-aws/whats-new/2025/12/aws-support-transformation-ai-powered-operations | 02/12/2025 (preços atualizados em 25/09/2026) |
| 6 | Fim de Developer, Business e On-Ramp | CONFIRMA | Encerram em 01/01/2027. Clientes On-Ramp são migrados automaticamente para Enterprise ao longo de 2026. Os três continuam no GovCloud | https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor.md | — |
| 7 | Trusted Advisor com 6 categorias | CONFIRMA | Cost optimization, Performance, Security, Fault tolerance, Service limits e Operational Excellence | mesma URL acima | — |
| 8 | Família Snow | Snowball Edge: CONFIRMA. Snowcone: CONFIRMA. Snowmobile: NÃO ENCONTRADO em fonte oficial. Data Transfer Terminal: CONFIRMA | Snowball Edge só para clientes existentes desde 07/11/2025; novos clientes são orientados a usar DataSync, AWS Data Transfer Terminal ou parceiros. Snowcone sem novos pedidos desde 12/11/2024. Snowmobile: só há imprensa citando a AWS (site deixou de exibir o serviço por volta de março/2024) | https://aws.amazon.com/blogs/storage/aws-snow-device-updates | 07/11/2025; 12/11/2024 |
| 9 | AWS IQ | CONFIRMA | Fim em 28/05/2026. Alternativa: AWS Marketplace Professional Services. Novos cadastros de experts bloqueados desde 20/05/2025 | https://docs.aws.amazon.com/aws-iq/latest/experts-user-guide/aws-iq-end-of-support.html | 28/05/2026 |
| 10 | Cloud9, CodeStar, CodeCommit | CONFIRMA | Cloud9 fechado a novos clientes em 25/07/2024. CodeStar descontinuado em 31/07/2024. CodeCommit voltou a GA e está aberto a novos clientes | AWS DevOps Blog (Cloud9 e "The Future of AWS CodeCommit"); docs CodeStar; histórico de docs do CodeCommit | Anúncios em 24/11/2025; histórico de docs em 25/11/2025 |
| 11 | Nomes oficiais | Quick Sight: CONFIRMA. Quick Suite: DIVERGE. SageMaker AI: CONFIRMA | O exam guide usa "Amazon Quick Sight" e "Amazon SageMaker AI". O QuickSight foi renomeado Amazon Quick Suite e continua dentro dele como Amazon Quick Sight. Páginas oficiais mais recentes e o site da AWS já usam **"Amazon Quick"** | Exam guide; https://docs.aws.amazon.com/es_es/quicksight/latest/user/table-sort.html | — |
| 12 | Timestream for LiveAnalytics | CONFIRMA | Fechado a novos clientes em 20/06/2025 | https://aws.amazon.com/about-aws/whats-new/2025/05/aws-service-changes | Anúncio de 20/05/2025 |
| 13 | Database Savings Plans | CONFIRMA | Até 35%, com compromisso de 1 ano e sem pagamento adiantado. 35% vale para serverless; instâncias provisionadas chegam a até 20% | https://aws.amazon.com/about-aws/whats-new/2025/12/database-savings-plans-savings | 02/12/2025 |
| 14 | Preços clássicos: Enterprise US$ 15.000, On-Ramp US$ 5.500 | Enterprise: CONFIRMA (valor histórico). On-Ramp: NÃO ENCONTRADO | O Enterprise passou para US$ 5.000 (antes US$ 15.000). A página atual do On-Ramp não mostra preço | Docs Trusted Advisor; https://aws.amazon.com/premiumsupport/plans/enterprise-onramp/ | — |

---

## Parte 3: afirmações que precisavam de verificação cuidadosa

| # | Item | Status | Valor oficial encontrado | Fonte | Data |
|---|---|---|---|---|---|
| 1 | CloudFront com planos flat-rate | CONFIRMA | Um preço mensal que agrupa CDN, WAF, proteção DDoS, Route 53, CloudWatch Logs, edge compute e créditos de S3, sem cobrança por excedente. Planos: Free (US$ 0), Pro (US$ 15), Business (US$ 200), Premium (US$ 1.000) | https://aws.amazon.com/about-aws/whats-new/2025/11/aws-flat-rate-pricing-plans | 18/11/2025 |
| 2 | Security Hub CSPM | CONFIRMA (só o nome) | A documentação oficial já usa "AWS Security Hub CSPM". Não achei o anúncio da reformulação | Docs Trusted Advisor | — |
| 3 | Q Business incorporado ao Quick Suite | DIVERGE | Aplicações do Q Business podem ser **conectadas** ao Quick Suite. O Q Business entrou em manutenção e não aceita novos clientes a partir de 30/07/2026. A palavra "incorporado" não aparece nas fontes | https://aws.amazon.com/about-aws/whats-new/2026/06/aws-service-availability/ | 2026 |
| 4 | Fraud Detector, Forecast, Lookout | CONFIRMA (Lookout for Equipment: NÃO ENCONTRADO em fonte oficial) | **Fraud Detector:** manutenção, sem novos clientes desde 07/11/2025. **Forecast:** fechado a novos clientes (data não informada nas docs). **Lookout for Vision:** novos clientes bloqueados em 10/10/2024; fim em 31/10/2025. **Lookout for Metrics:** fim em 12/09/2025 | whats-new/2025/10/aws-service-availability; docs Forecast; FAQ Lookout for Vision; docs Lookout for Metrics | ver valores |
| 5 | Amazon ECS Express Mode | CONFIRMA | Lançado sem custo adicional, em todas as regiões | https://aws.amazon.com/about-aws/whats-new/2025/11/announcing-amazon-ecs-express-mode/ | 21/11/2025 |
| 6 | ACM com certificados públicos exportáveis | CONFIRMA | Lançamento: validade de 395 dias, a US$ 15 por FQDN e US$ 149 por wildcard. A página de preços atual mostra **US$ 7 e US$ 79** | https://aws.amazon.com/about-aws/whats-new/2025/06/aws-certificate-manager-public-certificates-use-anywhere e https://aws.amazon.com/certificate-manager/pricing/ | 17/06/2025 |
| 7 | MFA obrigatório no root e gestão centralizada de root | CONFIRMA | Contas de gerenciamento: maio/2024. Contas standalone: junho/2024. Gestão centralizada de root no Organizations: novembro/2024. Contas membro: 2025 | https://aws.amazon.com/about-aws/whats-new/2025/06/aws-iam-mfa-root-users-across-all-account-types | 17/06/2025 |
| 8 | QLDB, Data Pipeline, IoT Analytics, IoT Events | CONFIRMA | **QLDB:** fim em 31/07/2025. **Data Pipeline:** fechado a novos clientes. **IoT Analytics:** fim em 15/12/2025. **IoT Events:** fim em 20/05/2026, fechado a novos clientes desde 20/05/2025 | Docs de cada serviço | ver valores |
| 9 | Aurora DSQL e AWS Transform | CONFIRMA | Aurora DSQL em GA. O site da AWS lista o Transform (modernização de legado com IA agêntica) | https://aws.amazon.com/about-aws/whats-new/2025/05/amazon-aurora-dsql-generally-available; https://aws.amazon.com/transform/ | 27/05/2025 (Transform: sem data) |
| 10 | On-Ramp inclui 1 IEM por ano | DIVERGE (nome) | A página fala em **1 engajamento de AWS Countdown por ano**, sem usar o termo "IEM" | https://aws.amazon.com/premiumsupport/plans/enterprise-onramp/ | página atualizada em 20/08/2026 |
| 11 | Budgets com actions: os 2 primeiros grátis | CONFIRMA | Os dois primeiros budgets com actions são grátis por mês; os demais custam US$ 0,10/dia. Cada relatório do Budgets Reports custa US$ 0,01 | https://aws.amazon.com/aws-cost-management/aws-budgets/pricing | — |
| 12 | Incident Manager e Migration Hub abertos a novos clientes? | DIVERGE: **não** | Os dois entraram em manutenção e fecharam a novos clientes em 07/11/2025 | https://aws.amazon.com/about-aws/whats-new/2025/10/aws-service-availability/ | 07/11/2025 |

---

## Parte 4: números que caem na prova

### Lambda
| Item | Status | Valor oficial | Fonte |
|---|---|---|---|
| Memória | CONFIRMA | 128 MB a 10.240 MB, em incrementos de 1 MB | https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html |
| Timeout | CONFIRMA | 900 s (15 min) | mesma |
| /tmp | CONFIRMA | 512 MB a 10.240 MB | mesma |
| Free tier | CONFIRMA | 1 milhão de requisições e 400.000 GB-s por mês | https://aws.amazon.com/lambda/pricing/ |

### SQS
| Item | Status | Valor oficial | Fonte |
|---|---|---|---|
| Retenção | CONFIRMA | Padrão de 4 dias (mínimo 60 s, máximo 14 dias) | https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html |
| Visibility timeout | CONFIRMA | Padrão de 30 s (0 s a 12 h) | mesma |
| Delay | CONFIRMA | 0 a 15 min | mesma |
| Long polling | CONFIRMA | 0 a 20 s (0 = short polling) | docs SQS (configuração de fila no console) |
| Tamanho da mensagem | CONFIRMA | Até 1 MiB | mesma |

### S3: classes de armazenamento
Fonte: https://aws.amazon.com/s3/storage-classes/ (atualizada em 25/09/2026)

| Classe | Disponibilidade projetada | SLA | AZs | Duração mínima cobrada |
|---|---|---|---|---|
| S3 Standard | 99,99% | 99,9% | ≥3 | N/A |
| S3 Intelligent-Tiering | 99,9% | 99% | ≥3 | N/A |
| S3 Express One Zone | 99,95% | 99,9% | 1 | 1 hora |
| S3 Standard-IA | 99,9% | 99% | ≥3 | 30 dias |
| S3 One Zone-IA | 99,5% | 99% | 1 | 30 dias |
| S3 Glacier Instant Retrieval | 99,9% | 99% | ≥3 | 90 dias |
| S3 Glacier Flexible Retrieval | 99,99% | 99,9% | ≥3 | 90 dias |
| S3 Glacier Deep Archive | 99,99% | 99,9% | ≥3 | 180 dias |

Todas as classes são projetadas para durabilidade de 99,999999999% (11 noves). O Express One Zone usa directory buckets e não suporta transições de Lifecycle.

| Recuperação | Status | Valor oficial | Fonte |
|---|---|---|---|
| Glacier Flexible: Standard 3–5 h, Bulk 5–12 h (Bulk gratuito) | CONFIRMA | 3–5 h / 5–12 h | https://docs.aws.amazon.com/cli/latest/reference/s3api/restore-object.html |
| Glacier Flexible: Expedited 1–5 min | NÃO ENCONTRADO em fonte oficial | Só em fornecedores terceiros | — |
| Deep Archive: Standard 12 h, Bulk 48 h, sem Expedited | CONFIRMA | até 12 h / até 48 h | mesma |

### Demais números
| Item | Status | Valor oficial | Fonte |
|---|---|---|---|
| EBS Multi-Attach | CONFIRMA | Só io1/io2; até 16 instâncias Nitro na mesma AZ (Windows: só io2) | https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-multi.html |
| Aurora | CONFIRMA | Replicação síncrona em 6 nós de armazenamento distribuídos entre AZs; até 15 réplicas em quaisquer três AZs | docs Aurora (High availability) e auroraextendedcontent |
| RDS: backup | CONFIRMA | Retenção do backup automático de até 35 dias | docs Aurora/RDS |
| RDS: read replicas | CONFIRMA, com detalhe | Até 15 (MySQL, MariaDB, PostgreSQL); Oracle e SQL Server até 5; Db2 até 3 | docs da API do RDS (CreateDBInstanceReadReplica) |
| DynamoDB | CONFIRMA | Item de no máximo 400 KB, contando nomes e valores dos atributos | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Constraints.html |
| Direct Connect | CONFIRMA | Dedicada: 1, 10, 100 e 400 Gbps. Hosted: 50 Mbps a 25 Gbps | https://docs.aws.amazon.com/directconnect/latest/UserGuide/connection_options.html |
| Route 53: SLA | CONFIRMA, com ressalva | A página não escreve "100%": o crédito de 10% começa abaixo de 100% de disponibilidade mensal, o que equivale a um compromisso de 100%. No GovCloud, o crédito começa abaixo de 99,995% | https://aws.amazon.com/route53/sla/ (atualizada em 16/04/2025) |
| CloudTrail | CONFIRMA | Event history com 90 dias de eventos de gerenciamento, por região, sem custo | https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html |
| CloudWatch (EC2) | CONFIRMA, com detalhe | Básico: métricas a cada 5 min (status checks a cada 1 min). Detalhado: tudo a cada 1 min, pago por métrica | https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-detailed-monitoring.html |
| Shield Advanced | CONFIRMA | US$ 3.000/mês, cobrado uma vez por organização, com compromisso de 1 ano | https://aws.amazon.com/shield/pricing/ |
| EC2: cobrança por segundo | CONFIRMA (fonte: AWS China) | Incrementos de 1 s, mínimo de 60 s (Amazon Linux, Windows, Ubuntu) | https://www.amazonaws.cn/en/ec2/pricing/ |
| Spot | CONFIRMA | Até 90% de desconto; aviso de interrupção de 2 min | docs EC2 Spot |
| Descontos de RI e Savings Plans | CONFIRMA | Standard RI até 72%; Convertible RI até 66%; Compute SP até 66%; EC2 Instance SP até 72% | https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-ris.html |

### Planos de suporte clássicos (válidos até 01/01/2027)
Fontes: https://aws.amazon.com/premiumsupport/plans/ e https://aws.amazon.com/premiumsupport/plans/developers

| Plano | Tempos de resposta | Preço de referência | Status |
|---|---|---|---|
| Developer | Orientação geral <24 **horas úteis**; sistema prejudicado <12 horas úteis | US$ 29 | Tempos: CONFIRMA. Preço: NÃO ENCONTRADO |
| Business | ... produção prejudicada <4 h; produção fora do ar <1 h | US$ 100 | Tempos: CONFIRMA. Preço: NÃO ENCONTRADO |
| Enterprise On-Ramp | ... produção fora do ar <1 h; sistema crítico de negócio fora do ar <30 min | US$ 5.500 | Tempos: CONFIRMA. Preço: NÃO ENCONTRADO |
| Enterprise | ... sistema crítico de negócio/missão fora do ar <15 min | US$ 15.000, hoje US$ 5.000 | CONFIRMA |

### Planos de suporte novos
| Plano | Crítico | Mínimo |
|---|---|---|
| Basic | — | Grátis |
| Business Support+ | 30 min | US$ 29/mês **por conta** |
| Enterprise Support | 15 min | US$ 5.000/mês |
| Unified Operations | 5 min | US$ 50.000/mês (compromisso de 90 dias) |

> ⚠️ **Pegadinha:** o Business Support+ começa em US$ 29, o mesmo valor que se costuma citar para o antigo Developer. Numa questão de preço, confira o nome do plano.

---

## Novidades relevantes que não estavam na lista original

1. **Escopo da prova mudou em relação às versões traduzidas antigas.** A versão em francês ainda lista AWS Audit Manager e AWS AppSync, e a versão em alemão lista o Amazon Kendra. Nenhum dos três aparece na lista atual em inglês. AWS IQ, AWS Activate e AMS agora estão explicitamente fora do escopo.
2. **Serviços no escopo, mas fechados a novos clientes:** AWS Migration Hub e AWS Application Discovery Service, desde 07/11/2025. Eles ainda podem cair na prova.
3. **Outras entradas em manutenção (sem novos clientes):**
   - **Desde 07/11/2025:** Amazon Glacier (o serviço original baseado em vaults, **diferente** das classes S3 Glacier), S3 Object Lambda, Systems Manager Change Manager, Systems Manager Incident Manager, CodeCatalyst, CodeGuru Reviewer, Cloud Directory e Snowball Edge.
   - **Desde 30/04/2026:** AWS Audit Manager, CloudTrail Lake, AWS App Runner e IoT FleetWise.
   - **Desde 30/07/2026:** Amazon Kendra, Amazon Q Business, Directory Service Simple AD, Service Catalog AppRegistry e Cognito Sync. Bedrock Agents passou a se chamar "Bedrock Agents Classic".
4. **Encerramentos anunciados em maio/2025:** Amazon Inspector Classic, Amazon Pinpoint, AWS Panorama, Connect Voice ID e DMS Fleet Advisor.
5. **WorkSpaces:** PCoIP e Pools entraram em sunset. O serviço continua no escopo.
6. **ACM:** a página de preços já mostra valores menores para certificados exportáveis (US$ 7 e US$ 79), alinhados à validade mais curta dos certificados públicos.
7. **Nomes:** Amazon QuickSight → Amazon Quick Suite → **Amazon Quick**. A parte de BI continua como **Amazon Quick Sight**, que é o nome usado no exam guide.

---

## Checklist rápido para a véspera da prova

- [ ] Reabrir o exam guide e a lista de serviços no escopo (podem mudar sem troca de código).
- [ ] Revisar os nomes novos dos planos de suporte (task 4.3).
- [ ] Revisar a tabela de classes do S3 (disponibilidade e duração mínima).
- [ ] Revisar os percentuais de RI, Savings Plans e Spot.
- [ ] Revisar as 6 categorias do Trusted Advisor e os 6 pilares do Well-Architected.
