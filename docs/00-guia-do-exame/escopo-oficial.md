<!-- autoral -->

# Escopo oficial da CLF-C02

🏠 [Guia do exame](README.md)

---

A AWS publica três listas que dizem o que pode cair na prova: as tarefas (*task statements*) de cada domínio, os serviços no escopo e os serviços fora do escopo. A própria AWS avisa que as listas de serviços não são completas e podem mudar. Esta página traduz as três, liga cada item à aula ou à ficha que o ensina e indica o que ficou de fora das duas listas de serviços.

Use a página para decidir onde investir tempo. Um serviço fora do escopo pode aparecer como alternativa errada numa questão; por isso todos estão documentados nas fichas, com o aviso de que não são cobrados. Ainda assim, leia a alternativa antes de descartá-la: o nome do serviço sozinho não decide a questão.

## Como ler os símbolos

As fichas usam os mesmos símbolos desta página na linha **Escopo oficial**.

| Símbolo | Significado | O que fazer |
|---|---|---|
| ✅ | Está na lista de serviços no escopo | Estude |
| ❌ | Está na lista de serviços fora do escopo | Saiba reconhecer o nome, mas não aprofunde |
| ⚪ | Não aparece em nenhuma das duas listas | Saiba para que serve |
| 🔀 | A ficha reúne serviços com situações diferentes | Veja a situação de cada serviço na ficha |

## As tarefas de cada domínio

A numeração das aulas (1.1 a 4.6) não é a mesma das tarefas oficiais. A tabela abaixo liga uma à outra; a [rastreabilidade](../../simulados/questoes/rastreabilidade.md) acrescenta as questões de cada tarefa.

| Tarefa oficial | O que pede | Aulas |
|---|---|---|
| **1.1** | Definir os benefícios da nuvem AWS (*Define the benefits of the AWS Cloud*) | [1.1](../01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md) · [1.2](../01-conceitos-de-nuvem/02-vantagens-da-nuvem.md) · [3.2](../03-tecnologia-e-servicos/02-infraestrutura-global.md) |
| **1.2** | Identificar os princípios de design da nuvem AWS (*Identify design principles of the AWS Cloud*) | [1.3](../01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md) · [1.4](../01-conceitos-de-nuvem/04-well-architected-framework.md) |
| **1.3** | Entender os benefícios e as estratégias de migração (*Understand the benefits of and strategies for migration to the AWS Cloud*) | [1.5](../01-conceitos-de-nuvem/05-cloud-adoption-framework.md) · [1.6](../01-conceitos-de-nuvem/06-estrategias-de-migracao.md) · [3.17](../03-tecnologia-e-servicos/17-migracao-e-transferencia.md) |
| **1.4** | Entender a economia da nuvem (*Understand concepts of cloud economics*) | [1.7](../01-conceitos-de-nuvem/07-economia-da-nuvem.md) |
| **2.1** | Entender o modelo de responsabilidade compartilhada (*Understand the AWS shared responsibility model*) | [2.1](../02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md) |
| **2.2** | Entender segurança, governança e conformidade (*Understand AWS Cloud security, governance, and compliance concepts*) | [2.5](../02-seguranca-e-conformidade/05-criptografia.md) · [2.6](../02-seguranca-e-conformidade/06-compliance-e-governanca.md) · [2.7](../02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md) |
| **2.3** | Identificar os recursos de gestão de acesso (*Identify AWS access management capabilities*) | [2.2](../02-seguranca-e-conformidade/02-usuario-root.md) · [2.3](../02-seguranca-e-conformidade/03-iam.md) · [2.4](../02-seguranca-e-conformidade/04-governanca-multi-conta.md) |
| **2.4** | Identificar componentes e recursos de segurança (*Identify components and resources for security*) | [2.8](../02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md) · [2.9](../02-seguranca-e-conformidade/09-deteccao-de-ameacas.md) · [2.10](../02-seguranca-e-conformidade/10-outros-pontos-de-seguranca.md) |
| **3.1** | Definir formas de implantar e operar na nuvem (*Define methods of deploying and operating in the AWS Cloud*) | [3.1](../03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md) · [3.16](../03-tecnologia-e-servicos/16-gestao-e-governanca.md) |
| **3.2** | Definir a infraestrutura global (*Define the AWS global infrastructure*) | [3.2](../03-tecnologia-e-servicos/02-infraestrutura-global.md) |
| **3.3** | Identificar os serviços de computação (*Identify AWS compute services*) | [3.3](../03-tecnologia-e-servicos/03-ec2.md) · [3.4](../03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md) · [3.5](../03-tecnologia-e-servicos/05-containers-e-serverless.md) · [3.6](../03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md) |
| **3.4** | Identificar os serviços de banco de dados (*Identify AWS database services*) | [3.7](../03-tecnologia-e-servicos/07-bancos-de-dados.md) · [3.17](../03-tecnologia-e-servicos/17-migracao-e-transferencia.md) |
| **3.5** | Identificar os serviços de rede (*Identify AWS network services*) | [3.10](../03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) |
| **3.6** | Identificar os serviços de armazenamento (*Identify AWS storage services*) | [3.8](../03-tecnologia-e-servicos/08-s3.md) · [3.9](../03-tecnologia-e-servicos/09-outros-armazenamentos.md) |
| **3.7** | Identificar os serviços de IA, machine learning e analytics (*Identify AWS AI/ML services and analytics services*) | [3.11](../03-tecnologia-e-servicos/11-analytics.md) · [3.12](../03-tecnologia-e-servicos/12-ia-e-machine-learning.md) |
| **3.8** | Identificar serviços das demais categorias (*Identify services from other in-scope AWS service categories*) | [3.13](../03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md) · [3.14](../03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md) · [3.15](../03-tecnologia-e-servicos/15-ferramentas-de-desenvolvimento.md) · [3.18](../03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md) |
| **4.1** | Comparar os modelos de preço (*Compare AWS pricing models*) | [4.1](../04-cobranca-precos-e-suporte/01-principios-de-preco.md) · [4.2](../04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) · [4.3](../04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) |
| **4.2** | Entender os recursos de cobrança, orçamento e custos (*Understand resources for billing, budget, and cost management*) | [4.4](../04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md) |
| **4.3** | Identificar os recursos técnicos e as opções de suporte (*Identify AWS technical resources and AWS Support options*) | [4.5](../04-cobranca-precos-e-suporte/05-planos-de-suporte.md) · [4.6](../04-cobranca-precos-e-suporte/06-outros-recursos-de-ajuda.md) |

## O que cada tarefa cita

O guia detalha cada tarefa em listas de conhecimentos e habilidades, com exemplos de serviços. A tabela resume todos os termos citados; o texto literal está nas páginas de cada domínio.

| Tarefa | Termos e serviços citados |
|---|---|
| 1.1 | Proposta de valor da nuvem; benefícios da infraestrutura global, como velocidade de implantação e alcance global; vantagens da alta disponibilidade, da elasticidade e da agilidade |
| 1.2 | Well-Architected Framework, seus seis pilares (excelência operacional, segurança, confiabilidade, eficiência de desempenho, otimização de custos e sustentabilidade) e as diferenças entre eles |
| 1.3 | Estratégias de adoção; recursos de apoio à migração; componentes do AWS CAF (menor risco de negócio, melhor desempenho ESG, mais receita, mais eficiência operacional); estratégias de migração, como a replicação de banco de dados |
| 1.4 | Economia ao migrar; custos fixos e variáveis; custos do ambiente local; licença própria (BYOL) e licença incluída; dimensionamento correto (*rightsizing*); benefícios da automação; economias de escala |
| 2.1 | Responsabilidades do cliente, da AWS e compartilhadas, e como elas mudam de um serviço para outro, como no RDS, no Lambda e no EC2 |
| 2.2 | Conformidade e governança; onde ficam os logs de segurança; onde encontrar informações de conformidade (Artifact); exigências por região ou setor; Inspector, Security Hub, GuardDuty e Shield; criptografia em trânsito e em repouso; CloudWatch, CloudTrail, Config e relatórios de acesso |
| 2.3 | IAM; proteção do usuário root e tarefas que só o root faz; menor privilégio; IAM Identity Center; chaves de acesso, políticas de senha e guarda de credenciais (Secrets Manager, Systems Manager); MFA e funções entre contas; grupos, usuários e políticas; identidade federada |
| 2.4 | WAF, Firewall Manager, Shield e GuardDuty; produtos de segurança de terceiros no Marketplace; Knowledge Center, Security Center e Security Blog; Trusted Advisor para achar problemas de segurança |
| 3.1 | APIs, SDKs e CLI, console e infraestrutura como código; operação única ou processo repetível; modelos de implantação em nuvem, híbrido e local |
| 3.2 | Regiões, zonas de disponibilidade e pontos de presença e a relação entre eles; alta disponibilidade com várias zonas, que não compartilham pontos únicos de falha; quando usar várias Regiões (recuperação de desastres, continuidade, latência, soberania de dados) |
| 3.3 | Tipos de instância do EC2; ECS e EKS; Fargate e Lambda; Auto Scaling como elasticidade; função dos load balancers |
| 3.4 | Banco no EC2 ou gerenciado; relacionais (RDS, Aurora); NoSQL (DynamoDB); em memória (ElastiCache); ferramentas de migração (DMS, SCT) |
| 3.5 | Componentes da VPC, como sub-redes e gateways; segurança na VPC (network ACLs, security groups, Inspector); Route 53; conexões com a AWS (VPN, Direct Connect) |
| 3.6 | Armazenamento de objetos e classes do S3; armazenamento em bloco (EBS, instance store); serviços de arquivos (EFS, FSx); arquivos com cache (Storage Gateway); políticas de ciclo de vida; AWS Backup |
| 3.7 | SageMaker AI e Lex; Athena, Kinesis, Glue e Quick Sight |
| 3.8 | EventBridge, SNS e SQS; Connect e SES; AWS Support; CodeBuild, CodePipeline e X-Ray; AppStream 2.0, WorkSpaces e WorkSpaces Secure Browser; Amplify; IoT Core |
| 4.1 | Sob demanda, instâncias reservadas, Spot, Savings Plans, Dedicated Hosts, Dedicated Instances e Capacity Reservations; flexibilidade das instâncias reservadas e comportamento delas no Organizations; custos de transferência de dados; preços das classes de armazenamento |
| 4.2 | Informações de cobrança e preços; Organizations e faturamento consolidado; tags de alocação de custos e relatórios (Cost and Usage Report); Budgets, Cost Explorer e Pricing Calculator |
| 4.3 | Documentação, whitepapers e blogs; Prescriptive Guidance, Knowledge Center e re:Post; Support Center; atendimento e comunidades, Basic Support, Business Support+, Enterprise Support e Unified Operations; Trusted Advisor, Health Dashboard e Health API; equipe Trust and Safety; parceiros (APN, ISVs, integradores) e seus benefícios; Marketplace; Professional Services e solutions architects |

## Serviços no escopo

A lista oficial organiza os serviços por categoria, com os nomes em inglês. Cada nome abaixo leva à ficha do serviço.

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
| Migration and Transfer | [Application Discovery Service, Migration Evaluator, Migration Hub](../../servicos/migracao/discovery-migration-hub-e-evaluator.md) · [Application Migration Service](../../servicos/migracao/application-migration-service.md) · [DMS e SCT](../../servicos/migracao/dms-e-sct.md) (o Application Migration Service hoje se chama AWS Transform MGN) |
| Networking and Content Delivery | [API Gateway](../../servicos/redes/api-gateway.md) · [CloudFront](../../servicos/redes/cloudfront.md) · [Direct Connect](../../servicos/redes/direct-connect.md) · [Global Accelerator](../../servicos/redes/global-accelerator.md) · [PrivateLink, Transit Gateway](../../servicos/redes/vpc-peering-transit-gateway-e-endpoints.md) · [Route 53](../../servicos/redes/route-53.md) · [VPC](../../servicos/redes/vpc.md) · [AWS VPN, Site-to-Site VPN, Client VPN](../../servicos/redes/site-to-site-vpn-e-client-vpn.md) |
| Security, Identity, and Compliance | [Artifact](../../servicos/seguranca/artifact.md) · [ACM](../../servicos/seguranca/certificate-manager.md) · [CloudHSM](../../servicos/seguranca/cloudhsm.md) · [Cognito](../../servicos/seguranca/cognito.md) · [Detective](../../servicos/seguranca/detective.md) · [Directory Service](../../servicos/seguranca/directory-service.md) · [Firewall Manager](../../servicos/seguranca/firewall-manager-e-network-firewall.md) · [GuardDuty](../../servicos/seguranca/guardduty.md) · [IAM](../../servicos/seguranca/iam.md) · [IAM Identity Center](../../servicos/seguranca/iam-identity-center.md) · [Inspector](../../servicos/seguranca/inspector.md) · [KMS](../../servicos/seguranca/kms.md) · [Macie](../../servicos/seguranca/macie.md) · [RAM](../../servicos/gerenciamento/service-catalog-e-ram.md) · [Secrets Manager](../../servicos/seguranca/secrets-manager-e-parameter-store.md) · [Security Hub](../../servicos/seguranca/security-hub.md) · [Shield](../../servicos/seguranca/shield.md) · [WAF](../../servicos/seguranca/waf.md) |
| Serverless | [Fargate](../../servicos/computacao/fargate.md) · [Lambda](../../servicos/computacao/lambda.md) |
| Storage | [AWS Backup](../../servicos/armazenamento/aws-backup.md) · [EBS](../../servicos/armazenamento/ebs.md) · [EFS](../../servicos/armazenamento/efs.md) · [Elastic Disaster Recovery](../../servicos/armazenamento/elastic-disaster-recovery.md) · [FSx](../../servicos/armazenamento/fsx.md) · [S3 e S3 Glacier](../../servicos/armazenamento/s3-classes-de-armazenamento.md) · [Storage Gateway](../../servicos/armazenamento/storage-gateway.md) |

Alguns serviços da lista mudaram depois que ela foi publicada. O Amazon AppStream 2.0 hoje se chama Amazon WorkSpaces Applications, o Amazon Connect é oferecido como Amazon Connect Customer e o Quick Sight faz parte do Amazon Quick. O AWS Migration Hub e o AWS Application Discovery Service não aceitam clientes novos desde 07/11/2025, e o WorkSpaces Secure Browser deixa de aceitar em 29/10/2026. Todos continuam na lista e podem cair na prova.

## Serviços fora do escopo

Todos estão documentados nas fichas indicadas, com o aviso de que não caem na prova. Os que não pertencem a nenhuma outra ficha estão na categoria [fora do escopo da prova](../../servicos/README.md) do índice das fichas.

| Categoria | Serviços → onde estão documentados |
|---|---|
| Analytics | [AppFlow, Clean Rooms, Data Exchange, DataZone, MSK](../../servicos/analytics/lake-formation-msk-e-outros.md) |
| Application Integration | [AppFabric, Simple Workflow Service (SWF)](../../servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md) |
| Business Applications | [WorkDocs](../../servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md) |
| Compute | [Copilot](../../servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md) · [Wavelength](../../servicos/computacao/outposts-local-zones-wavelength.md) |
| Cost / Financial Management | [Application Cost Profiler, DevPay](../../servicos/fora-do-escopo/gerenciamento-e-custos.md) · [Billing Conductor](../../servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md) |
| Customer Enablement | [AWS Activate, AWS IQ, AWS Managed Services (AMS)](../../servicos/custos/recursos-de-ajuda-e-parceiros.md) |
| Database | [Keyspaces](../../servicos/banco-de-dados/keyspaces-timestream-e-outros.md) · [MemoryDB](../../servicos/banco-de-dados/memorydb.md) · [AppConfig (listado assim na página)](../../servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md) |
| Developer Tools | [Application Composer, CodeGuru](../../servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md) · [CodeArtifact, CodeDeploy](../../servicos/desenvolvimento/code-services.md) · [CloudShell](../../servicos/desenvolvimento/cli-sdk-e-cloudshell.md) · [Device Farm](../../servicos/aplicacoes/amplify-e-appsync.md) |
| Game Tech | [GameLift, Lumberyard](../../servicos/fora-do-escopo/midia-e-jogos.md) |
| IoT | [IoT Device Defender, Monitron](../../servicos/fora-do-escopo/iot-robotica-e-satelite.md) · [IoT Greengrass](../../servicos/aplicacoes/iot-core-e-greengrass.md) |
| Machine Learning | [Fraud Detector, Personalize](../../servicos/ia-ml/servicos-de-ia-prontos.md) · [Lookout for Metrics, Panorama](../../servicos/fora-do-escopo/iot-robotica-e-satelite.md) |
| Management and Governance | [Chatbot, Data Lifecycle Manager, Launch Wizard](../../servicos/fora-do-escopo/gerenciamento-e-custos.md) · [Elastic Transcoder](../../servicos/fora-do-escopo/midia-e-jogos.md) |
| Media Services | [Elemental (MediaConnect, MediaConvert, MediaLive, MediaPackage, MediaStore, MediaTailor, Appliances and Software), IVS](../../servicos/fora-do-escopo/midia-e-jogos.md) |
| Migration and Transfer | [Migration Hub Refactor Spaces](../../servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md) · [Transfer Family](../../servicos/migracao/datasync-e-transfer-family.md) |
| Networking | [Cloud Map, Network Access Analyzer, VPC Lattice](../../servicos/fora-do-escopo/rede-e-diretorio.md) · [Ground Station](../../servicos/fora-do-escopo/iot-robotica-e-satelite.md) |
| Security | [Cloud Directory](../../servicos/fora-do-escopo/rede-e-diretorio.md) · [Network Firewall](../../servicos/seguranca/firewall-manager-e-network-firewall.md) |
| Robotics | [RoboMaker](../../servicos/fora-do-escopo/iot-robotica-e-satelite.md) |
| Storage | [FSx for Lustre](../../servicos/armazenamento/fsx.md) |

## Serviços que não aparecem em nenhuma lista

Alguns serviços que aparecem em materiais de estudo não estão em nenhuma das duas listas: Local Zones, família Snow, DataSync, Bedrock, Kendra, Audit Manager, AppSync, Amazon MQ, Cloud9, CodeCommit, CodeStar, Timestream, Lake Formation e STS. A chance de serem cobrados é baixa, mas vale saber para que servem; as fichas e as aulas que os citam explicam cada um.

## Fontes oficiais

Verificadas em 06/10/2026.

- [Guia do exame CLF-C02](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html) e as páginas [Content Domain 1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html), [2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html), [3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html) e [4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html): tarefas e termos citados.
- [In-Scope AWS Services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html) e [Out-of-Scope AWS Services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-out-of-scope-services.html): as duas listas e o aviso de que não são completas.
- As mudanças de nome e de situação de cada serviço têm a fonte oficial na ficha correspondente.

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações sobre o escopo. -->
<!-- notas:fim -->
