# 🎯 Escopo oficial da CLF-C02 (verificado em 04/10/2026)

> Fonte: [verificação em fontes oficiais](../../fontes/verificacao-fontes-oficiais-2026-10.md), feita no
> [exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)
> e na [lista de serviços no escopo](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html).
>
> ⚠️ O código da prova continua **CLF-C02**, mas a AWS atualiza o conteúdo do guia **sem trocar o código**.
> Reabra as duas páginas alguns dias antes da prova. A própria AWS avisa que as listas não são exaustivas.

## Task statements oficiais → tópicos deste repositório

Os tópicos de `docs/` seguem a numeração do guia de estudo (1.1 a 4.6), que é **diferente** da numeração
oficial das tasks. A tabela abaixo liga uma à outra.

| Task oficial | Texto oficial | Tópicos do repositório |
|---|---|---|
| **1.1** | Define the benefits of the AWS Cloud | [1.1](../01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md) · [1.2](../01-conceitos-de-nuvem/02-vantagens-da-nuvem.md) · [3.2](../03-tecnologia-e-servicos/02-infraestrutura-global.md) |
| **1.2** | Identify design principles of the AWS Cloud | [1.3](../01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md) · [1.4 Well-Architected (6 pilares)](../01-conceitos-de-nuvem/04-well-architected-framework.md) |
| **1.3** | Understand the benefits of and strategies for migration to the AWS Cloud | [1.5 CAF](../01-conceitos-de-nuvem/05-cloud-adoption-framework.md) · [1.6 7 Rs](../01-conceitos-de-nuvem/06-estrategias-de-migracao.md) · [3.17](../03-tecnologia-e-servicos/17-migracao-e-transferencia.md) |
| **1.4** | Understand concepts of cloud economics | [1.7](../01-conceitos-de-nuvem/07-economia-da-nuvem.md) |
| **2.1** | Understand the AWS shared responsibility model | [2.1](../02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md) |
| **2.2** | Understand AWS Cloud security, governance, and compliance concepts | [2.5](../02-seguranca-e-conformidade/05-criptografia.md) · [2.6](../02-seguranca-e-conformidade/06-compliance-e-governanca.md) · [2.7](../02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md) |
| **2.3** | Identify AWS access management capabilities (inclui **IAM Identity Center**, proteção do root e tarefas exclusivas do root) | [2.2](../02-seguranca-e-conformidade/02-usuario-root.md) · [2.3](../02-seguranca-e-conformidade/03-iam.md) · [2.4](../02-seguranca-e-conformidade/04-governanca-multi-conta.md) |
| **2.4** | Identify components and resources for security | [2.8](../02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md) · [2.9](../02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) · [2.10](../02-seguranca-e-conformidade/10-outros-pontos-de-seguranca.md) |
| **3.1** | Define methods of deploying and operating in the AWS Cloud | [3.1](../03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md) · [3.16](../03-tecnologia-e-servicos/16-gestao-e-governanca.md) |
| **3.2** | Define the AWS global infrastructure | [3.2](../03-tecnologia-e-servicos/02-infraestrutura-global.md) |
| **3.3** | Identify AWS compute services | [3.3](../03-tecnologia-e-servicos/03-ec2.md) · [3.4](../03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md) · [3.5](../03-tecnologia-e-servicos/05-containers-e-serverless.md) · [3.6](../03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md) |
| **3.4** | Identify AWS database services | [3.7](../03-tecnologia-e-servicos/07-bancos-de-dados.md) |
| **3.5** | Identify AWS network services | [3.10](../03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) |
| **3.6** | Identify AWS storage services | [3.8](../03-tecnologia-e-servicos/08-s3.md) · [3.9](../03-tecnologia-e-servicos/09-outros-armazenamentos.md) |
| **3.7** | Identify AWS AI/ML services and analytics services (SageMaker AI, Lex, Athena, Kinesis, Glue, Quick Sight…) | [3.11](../03-tecnologia-e-servicos/11-analytics.md) · [3.12](../03-tecnologia-e-servicos/12-ia-e-machine-learning.md) |
| **3.8** | Identify services from other in-scope AWS service categories | [3.13](../03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md) · [3.14](../03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md) · [3.15](../03-tecnologia-e-servicos/15-ferramentas-de-desenvolvimento.md) · [3.18](../03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md) |
| **4.1** | Compare AWS pricing models (On-Demand, RIs, Spot, Savings Plans, Dedicated Hosts/Instances, Capacity Reservations; flexibilidade de RIs e RIs no Organizations) | [4.1](../04-cobranca-precos-e-suporte/01-principios-de-preco.md) · [4.2](../04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) · [4.3](../04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) |
| **4.2** | Understand resources for billing, budget, and cost management | [4.4](../04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md) |
| **4.3** | Identify AWS technical resources and AWS Support options (**Basic, Business Support+, Enterprise, Unified Operations**; Trusted Advisor, Health Dashboard e Health API; Trust and Safety, APN, Marketplace, Professional Services, Prescriptive Guidance, Knowledge Center, re:Post) | [4.5](../04-cobranca-precos-e-suporte/05-planos-de-suporte.md) · [4.6](../04-cobranca-precos-e-suporte/06-outros-recursos-de-ajuda.md) |

**Destaques do guia atual:**
- **3.8 (outras categorias):** end-user computing = AppStream 2.0, WorkSpaces e WorkSpaces Secure Browser; frontend = **só Amplify**; IoT = **só IoT Core**; developer tools = **CodeBuild, CodePipeline e X-Ray** (e a CLI).
- **4.3:** os planos de suporte cobrados agora são os **novos**. Veja [planos de suporte](../../servicos/custos/planos-de-suporte.md).

## ✅ Serviços no escopo (lista oficial)

| Categoria | Serviços → ficha |
|---|---|
| Analytics | [Athena](../../servicos/analytics/athena.md) · [EMR](../../servicos/analytics/emr.md) · [Glue](../../servicos/analytics/glue.md) · [Kinesis](../../servicos/analytics/kinesis.md) · [OpenSearch Service](../../servicos/analytics/opensearch.md) · [Quick Sight](../../servicos/analytics/quicksight.md) · [Redshift](../../servicos/banco-de-dados/redshift.md) |
| Application Integration | [EventBridge](../../servicos/integracao/eventbridge.md) · [SNS](../../servicos/integracao/sns.md) · [SQS](../../servicos/integracao/sqs.md) · [Step Functions](../../servicos/integracao/step-functions.md) |
| Business Applications | [Amazon Connect](../../servicos/aplicacoes/amazon-connect.md) · [SES](../../servicos/aplicacoes/ses.md) |
| Cloud Financial Management | [Budgets](../../servicos/custos/budgets.md) · [Cost and Usage Reports](../../servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md) · [Cost Explorer](../../servicos/custos/cost-explorer.md) · [Marketplace](../../servicos/custos/recursos-de-ajuda-e-parceiros.md) |
| Compute | [Batch](../../servicos/computacao/batch.md) · [EC2](../../servicos/computacao/ec2.md) · [Elastic Beanstalk](../../servicos/computacao/elastic-beanstalk.md) · [Lightsail](../../servicos/computacao/lightsail.md) · [Outposts](../../servicos/computacao/outposts-local-zones-wavelength.md) |
| Containers | [ECR](../../servicos/computacao/ecr.md) · [ECS](../../servicos/computacao/ecs.md) · [EKS](../../servicos/computacao/eks.md) |
| Customer Enablement | [AWS Support](../../servicos/custos/planos-de-suporte.md) |
| Database | [Aurora](../../servicos/banco-de-dados/aurora.md) · [DocumentDB](../../servicos/banco-de-dados/documentdb.md) · [DynamoDB](../../servicos/banco-de-dados/dynamodb.md) · [ElastiCache](../../servicos/banco-de-dados/elasticache.md) · [Neptune](../../servicos/banco-de-dados/neptune.md) · [RDS](../../servicos/banco-de-dados/rds.md) |
| Developer Tools | [AWS CLI](../../servicos/desenvolvimento/cli-sdk-e-cloudshell.md) · [CodeBuild, CodePipeline](../../servicos/desenvolvimento/code-services.md) · [X-Ray](../../servicos/desenvolvimento/x-ray.md) |
| End User Computing | [AppStream 2.0, WorkSpaces, WorkSpaces Secure Browser](../../servicos/aplicacoes/workspaces-e-appstream.md) |
| Frontend Web and Mobile | [Amplify](../../servicos/aplicacoes/amplify-e-appsync.md) |
| Internet of Things | [IoT Core](../../servicos/aplicacoes/iot-core-e-greengrass.md) |
| Machine Learning | [Comprehend, Lex, Polly, Rekognition, Textract, Transcribe, Translate](../../servicos/ia-ml/servicos-de-ia-prontos.md) · [Amazon Q](../../servicos/ia-ml/amazon-q.md) · [SageMaker AI](../../servicos/ia-ml/sagemaker-ai.md) |
| Management and Governance | [Auto Scaling](../../servicos/computacao/ec2-auto-scaling.md) · [CloudFormation](../../servicos/gerenciamento/cloudformation.md) · [CloudTrail](../../servicos/gerenciamento/cloudtrail.md) · [CloudWatch](../../servicos/gerenciamento/cloudwatch.md) · [Compute Optimizer, License Manager, Service Quotas](../../servicos/gerenciamento/compute-optimizer-service-quotas-e-license-manager.md) · [Config](../../servicos/gerenciamento/config.md) · [Control Tower](../../servicos/gerenciamento/control-tower.md) · [Health Dashboard](../../servicos/gerenciamento/health-dashboard.md) · [Management Console](../../servicos/desenvolvimento/cli-sdk-e-cloudshell.md) · [Organizations](../../servicos/gerenciamento/organizations.md) · [Service Catalog](../../servicos/gerenciamento/service-catalog-e-ram.md) · [Systems Manager](../../servicos/gerenciamento/systems-manager.md) · [Trusted Advisor](../../servicos/gerenciamento/trusted-advisor.md) · [Well-Architected Tool](../01-conceitos-de-nuvem/04-well-architected-framework.md) |
| Migration and Transfer | [Application Discovery Service, Migration Evaluator, Migration Hub](../../servicos/migracao/discovery-migration-hub-e-evaluator.md) · [Application Migration Service](../../servicos/migracao/application-migration-service.md) · [DMS e SCT](../../servicos/migracao/dms-e-sct.md) |
| Networking and Content Delivery | [API Gateway](../../servicos/redes/api-gateway.md) · [CloudFront](../../servicos/redes/cloudfront.md) · [Direct Connect](../../servicos/redes/direct-connect.md) · [Global Accelerator](../../servicos/redes/global-accelerator.md) · [PrivateLink, Transit Gateway](../../servicos/redes/vpc-peering-transit-gateway-e-endpoints.md) · [Route 53](../../servicos/redes/route-53.md) · [VPC](../../servicos/redes/vpc.md) · [AWS VPN, Site-to-Site VPN, Client VPN](../../servicos/redes/site-to-site-vpn-e-client-vpn.md) |
| Security, Identity, and Compliance | [Artifact](../../servicos/seguranca/artifact.md) · [ACM](../../servicos/seguranca/certificate-manager.md) · [CloudHSM](../../servicos/seguranca/cloudhsm.md) · [Cognito](../../servicos/seguranca/cognito.md) · [Detective](../../servicos/seguranca/detective.md) · [Directory Service](../../servicos/seguranca/directory-service.md) · [Firewall Manager](../../servicos/seguranca/firewall-manager-e-network-firewall.md) · [GuardDuty](../../servicos/seguranca/guardduty.md) · [IAM](../../servicos/seguranca/iam.md) · [IAM Identity Center](../../servicos/seguranca/iam-identity-center.md) · [Inspector](../../servicos/seguranca/inspector.md) · [KMS](../../servicos/seguranca/kms.md) · [Macie](../../servicos/seguranca/macie.md) · [RAM](../../servicos/gerenciamento/service-catalog-e-ram.md) · [Secrets Manager](../../servicos/seguranca/secrets-manager-e-parameter-store.md) · [Security Hub](../../servicos/seguranca/security-hub.md) · [Shield](../../servicos/seguranca/shield.md) · [WAF](../../servicos/seguranca/waf.md) |
| Serverless | [Fargate](../../servicos/computacao/fargate.md) · [Lambda](../../servicos/computacao/lambda.md) |
| Storage | [AWS Backup](../../servicos/armazenamento/aws-backup.md) · [EBS](../../servicos/armazenamento/ebs.md) · [EFS](../../servicos/armazenamento/efs.md) · [Elastic Disaster Recovery](../../servicos/armazenamento/elastic-disaster-recovery.md) · [FSx](../../servicos/armazenamento/fsx.md) · [S3 e S3 Glacier](../../servicos/armazenamento/s3-classes-de-armazenamento.md) · [Storage Gateway](../../servicos/armazenamento/storage-gateway.md) |

## ❌ Fora do escopo (lista oficial, não exaustiva)

Se uma alternativa citar um destes, provavelmente é distrator.

| Categoria | Serviços |
|---|---|
| Analytics | AppFlow, Clean Rooms, Data Exchange, DataZone, **MSK** |
| Application Integration | AppFabric, Simple Workflow Service (SWF) |
| Business Applications | WorkDocs |
| Compute | Copilot, **Wavelength** |
| Cost / Financial Management | Application Cost Profiler, DevPay, **Billing Conductor** |
| Customer Enablement | **AWS Activate**, **AWS IQ**, **AWS Managed Services (AMS)** |
| Database | **Keyspaces**, **MemoryDB**, AppConfig (listado assim na página) |
| Developer Tools | Application Composer, **CodeArtifact**, **CodeDeploy**, CodeGuru, **CloudShell**, **Device Farm** |
| Game Tech | GameLift, Lumberyard |
| IoT | IoT Device Defender, **IoT Greengrass**, Monitron |
| Machine Learning | Fraud Detector, Lookout for Metrics, Panorama, **Personalize** |
| Management and Governance | Chatbot, Data Lifecycle Manager, Elastic Transcoder, Launch Wizard |
| Media Services | Elemental (todos), Interactive Video Service (IVS) |
| Migration and Transfer | Migration Hub Refactor Spaces, **Transfer Family** |
| Networking | Cloud Map, Network Access Analyzer, Ground Station, VPC Lattice |
| Security | Cloud Directory, **Network Firewall** |
| Robotics | RoboMaker |
| Storage | **FSx for Lustre** |

## ⚪ Nem dentro nem fora: não aparecem em nenhuma das listas

Continuam úteis como contexto, mas têm baixa chance de cair: **Local Zones**, **família Snow** (Snowball Edge),
**DataSync**, **Bedrock**, **Kendra**, **Audit Manager**, **AppSync**, **Amazon MQ**, **Cloud9**, **CodeCommit**,
**CodeStar**, **Timestream**, **Lake Formation**, **STS**.

> Versões traduzidas antigas da lista ainda citam Audit Manager, AppSync e Kendra; a lista atual em inglês não.

## ⏸️ No escopo, mas fechados a novos clientes

- **AWS Migration Hub** e **AWS Application Discovery Service** (desde 07/11/2025). Ainda podem cair na prova.
