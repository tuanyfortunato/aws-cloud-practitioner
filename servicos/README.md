# 🔎 Fichas de serviços AWS

## 🧭 Por onde começar

Se você ainda não conhece um serviço, abra sua ficha e leia **Comece pelo problema**. A abertura explica a dificuldade, a solução, um exemplo, os limites e as primeiras palavras técnicas. Só depois avance para componentes, configurações e questões da prova.

Uma ficha por serviço (ou família de serviços), com o que cai na prova e o que vai além: componentes, configurações, limites, cobrança, responsabilidade compartilhada, atualizações 2025-2026, pegadinhas e perguntas típicas.

> Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.
>
> Coluna *Escopo* ([lista oficial](../docs/00-guia-do-exame/escopo-oficial.md)): ✅ no escopo · 🔀 parcial · ⚪ não listado · ❌ fora do escopo.
>
> Modelo para novas fichas: [`templates/servico.md`](../templates/servico.md).


## 🖥️ Computação

| Ficha | Escopo | Em uma frase |
|---|---|---|
| [Amazon EC2 (Elastic Compute Cloud)](computacao/ec2.md) | ✅ | Servidores virtuais sob demanda, com controle total do sistema operacional (IaaS). |
| [Amazon EC2 Auto Scaling](computacao/ec2-auto-scaling.md) | ✅ | Aumenta e reduz automaticamente o número de instâncias EC2 conforme a demanda e substitui as que falham. |
| [Elastic Load Balancing (ELB)](computacao/elastic-load-balancing.md) | ✅ | Distribui automaticamente o tráfego entre destinos saudáveis (EC2, contêineres, IPs, Lambda) em várias AZs. |
| [AWS Lambda](computacao/lambda.md) | ✅ | Executa código em resposta a eventos sem você administrar servidores; o modelo base cobra requisições e duração. |
| [Amazon ECS (Elastic Container Service)](computacao/ecs.md) | ✅ | Orquestrador de contêineres próprio da AWS, totalmente gerenciado e integrado aos demais serviços. |
| [Amazon EKS (Elastic Kubernetes Service)](computacao/eks.md) | ✅ | Kubernetes gerenciado — a AWS opera o plano de controle e você roda seus pods. |
| [AWS Fargate](computacao/fargate.md) | ✅ | Motor serverless que executa contêineres do ECS ou EKS sem você provisionar ou gerenciar servidores. |
| [Amazon ECR (Elastic Container Registry)](computacao/ecr.md) | ✅ | Registro gerenciado para guardar, versionar e distribuir imagens de contêiner (Docker/OCI). |
| [AWS Elastic Beanstalk](computacao/elastic-beanstalk.md) | ✅ | Você envia o código e o Beanstalk provisiona e gerencia capacidade, balanceamento, escalonamento e monitoramento. |
| [Amazon Lightsail](computacao/lightsail.md) | ✅ | Servidores virtuais e serviços prontos com **preço mensal fixo e previsível**, para quem está começando. |
| [AWS Batch](computacao/batch.md) | ✅ | Executa grandes volumes de jobs em lote, escolhendo e provisionando automaticamente a computação ideal. |
| [AWS Outposts, Local Zones e Wavelength](computacao/outposts-local-zones-wavelength.md) | 🔀 | Três formas de levar a infraestrutura AWS para mais perto de onde a latência ou a localização dos dados importam. |

## 🗄️ Armazenamento

| Ficha | Escopo | Em uma frase |
|---|---|---|
| [Amazon S3 (Simple Storage Service)](armazenamento/s3.md) | ✅ | Armazenamento de objetos ilimitado, com 11 noves de durabilidade, acessado via API/HTTP. |
| [Classes de armazenamento do S3 (incluindo S3 Glacier)](armazenamento/s3-classes-de-armazenamento.md) | ✅ | Cada classe troca custo de armazenamento por custo/tempo de acesso — escolha pelo padrão de acesso. |
| [Amazon EBS (Elastic Block Store) e Instance Store](armazenamento/ebs.md) | ✅ | Discos virtuais persistentes, em rede, para instâncias EC2 — como um HD/SSD que sobrevive ao desligamento. |
| [Amazon EFS (Elastic File System)](armazenamento/efs.md) | ✅ | Sistema de arquivos NFS gerenciado e elástico, compartilhado por milhares de instâncias Linux em várias AZs. |
| [Amazon FSx](armazenamento/fsx.md) | 🔀 | Sistemas de arquivos populares de terceiros (Windows, Lustre, NetApp ONTAP, OpenZFS) totalmente gerenciados. |
| [AWS Storage Gateway](armazenamento/storage-gateway.md) | ✅ | Liga aplicações on-premises ao armazenamento da AWS usando protocolos padrão (NFS, SMB, iSCSI), com cache local. |
| [AWS Backup](armazenamento/aws-backup.md) | ✅ | Centraliza e automatiza backups de vários serviços AWS com políticas, num só lugar. |
| [AWS Elastic Disaster Recovery (AWS DRS)](armazenamento/elastic-disaster-recovery.md) | ✅ | Replica servidores continuamente (on-premises, outra nuvem ou outra região AWS) para a AWS e permite recuperá-los em minutos. |

## 🛢️ Banco de dados

| Ficha | Escopo | Em uma frase |
|---|---|---|
| [Amazon RDS (Relational Database Service)](banco-de-dados/rds.md) | ✅ | Banco relacional gerenciado — a AWS cuida de hardware, SO, patches do motor, backups e failover. |
| [Amazon Aurora](banco-de-dados/aurora.md) | ✅ | Banco relacional compatível com MySQL e PostgreSQL, com desempenho e disponibilidade de nível comercial a custo de open source. |
| [Amazon DynamoDB](banco-de-dados/dynamodb.md) | ✅ | Banco chave-valor e de documentos, serverless, com latência de milissegundos de um dígito em qualquer escala. |
| [Amazon ElastiCache](banco-de-dados/elasticache.md) | ✅ | Cache em memória gerenciado (Valkey, Redis OSS, Memcached) com latência de microssegundos. |
| [Amazon MemoryDB](banco-de-dados/memorydb.md) | ❌ | Banco de dados **primário** em memória, compatível com Valkey/Redis, com durabilidade multi-AZ. |
| [Amazon Redshift](banco-de-dados/redshift.md) | ✅ | Data warehouse colunar e massivamente paralelo (MPP) para análises SQL (OLAP) sobre terabytes a petabytes. |
| [Amazon DocumentDB (compatível com MongoDB)](banco-de-dados/documentdb.md) | ✅ | Banco de documentos JSON gerenciado, compatível com as APIs e drivers do MongoDB. |
| [Amazon Neptune](banco-de-dados/neptune.md) | ✅ | Banco de grafos gerenciado para dados altamente conectados (relacionamentos). |
| [Amazon Keyspaces, Timestream e outros bancos especializados](banco-de-dados/keyspaces-timestream-e-outros.md) | 🔀 | A AWS tem um banco "sob medida" para cada modelo de dados — saiba associar o modelo ao serviço. |

## 🌐 Redes e entrega de conteúdo

| Ficha | Escopo | Em uma frase |
|---|---|---|
| [Amazon VPC (Virtual Private Cloud)](redes/vpc.md) | ✅ | Sua rede privada, isolada logicamente, dentro de uma região da AWS. |
| [VPC Peering, Transit Gateway, VPC Endpoints e PrivateLink](redes/vpc-peering-transit-gateway-e-endpoints.md) | ✅ | Formas de conectar VPCs entre si e de acessar serviços sem passar pela internet. |
| [AWS VPN (Site-to-Site VPN e Client VPN)](redes/site-to-site-vpn-e-client-vpn.md) | ✅ | Túneis criptografados (IPsec/TLS) pela internet para ligar redes ou usuários à sua VPC. |
| [AWS Direct Connect](redes/direct-connect.md) | ✅ | Conexão de rede **física, dedicada e privada** entre seu datacenter e a AWS, sem passar pela internet. |
| [Amazon Route 53](redes/route-53.md) | ✅ | DNS gerenciado e altamente disponível (o "53" é a porta do DNS), com registro de domínios, roteamento inteligente e health checks. |
| [Amazon CloudFront](redes/cloudfront.md) | ✅ | Rede de distribuição de conteúdo (CDN) que faz **cache** perto dos usuários, reduzindo latência e carga na origem. |
| [AWS Global Accelerator](redes/global-accelerator.md) | ✅ | Fornece **2 IPs anycast estáticos** e leva o tráfego TCP/UDP pela rede global da AWS até o endpoint saudável mais próximo. |
| [Amazon API Gateway](redes/api-gateway.md) | ✅ | Cria, publica, protege e monitora APIs em qualquer escala — a "porta da frente" de back-ends serverless. |

## 🔐 Segurança, identidade e compliance

| Ficha | Escopo | Em uma frase |
|---|---|---|
| [AWS IAM (Identity and Access Management) e AWS STS](seguranca/iam.md) | ✅ | Controla **quem** pode se autenticar e **o que** cada identidade pode fazer em quais recursos da conta. |
| [AWS IAM Identity Center (antigo AWS SSO)](seguranca/iam-identity-center.md) | ✅ | Login único (SSO) para que **funcionários** acessem várias contas AWS e aplicações SaaS com um só usuário. |
| [Amazon Cognito](seguranca/cognito.md) | ✅ | Cadastro, login e controle de acesso para **usuários finais** de aplicações web e mobile. |
| [AWS Directory Service](seguranca/directory-service.md) | ✅ | Microsoft Active Directory gerenciado na AWS, ou ponte para o AD on-premises. |
| [AWS KMS (Key Management Service)](seguranca/kms.md) | ✅ | Cria e controla chaves de criptografia integradas a mais de 100 serviços AWS, com auditoria de cada uso. |
| [AWS CloudHSM](seguranca/cloudhsm.md) | ✅ | HSM (hardware security module) **dedicado e exclusivo** na nuvem, em que só você controla as chaves. |
| [AWS Certificate Manager (ACM) e AWS Private CA](seguranca/certificate-manager.md) | ✅ | Emite e gerencia certificados SSL/TLS, com renovação para certificados elegíveis; públicos não exportáveis em serviços integrados são gratuitos. |
| [AWS Secrets Manager e Systems Manager Parameter Store](seguranca/secrets-manager-e-parameter-store.md) | ✅ | Guardam segredos e configurações fora do código, criptografados com KMS — o Secrets Manager também os **rotaciona automaticamente**. |
| [AWS Shield](seguranca/shield.md) | ✅ | Proteção gerenciada contra ataques de negação de serviço distribuída (DDoS). |
| [AWS WAF (Web Application Firewall)](seguranca/waf.md) | ✅ | Firewall de **camada 7** que filtra requisições HTTP(S) maliciosas antes que cheguem à aplicação. |
| [AWS Firewall Manager e AWS Network Firewall](seguranca/firewall-manager-e-network-firewall.md) | 🔀 | O Firewall Manager **governa** regras de firewall em todas as contas; o Network Firewall **é** um firewall gerenciado para a VPC. |
| [Amazon GuardDuty](seguranca/guardduty.md) | ✅ | Detecção inteligente e contínua de **ameaças ativas** usando machine learning, detecção de anomalias e inteligência de ameaças. |
| [Amazon Inspector](seguranca/inspector.md) | ✅ | Varre continuamente cargas de trabalho em busca de **vulnerabilidades de software (CVEs)** e exposição de rede não intencional. |
| [Amazon Macie](seguranca/macie.md) | ✅ | Usa machine learning e padrões para **descobrir e proteger dados sensíveis (PII) no Amazon S3**. |
| [Amazon Detective](seguranca/detective.md) | ✅ | Facilita **investigar a causa raiz** de achados de segurança, montando um grafo de comportamento a partir dos logs. |
| [AWS Security Hub](seguranca/security-hub.md) | ✅ | **painel central** de segurança que agrega achados de vários serviços e verifica a conta contra padrões de boas práticas. |
| [AWS Artifact](seguranca/artifact.md) | ✅ | Portal de autoatendimento para baixar **relatórios de conformidade da AWS** e aceitar **acordos** legais. |
| [AWS Audit Manager](seguranca/audit-manager.md) | ⚪ | Coleta **evidências da sua conta** continuamente e as mapeia para frameworks, para preparar as suas auditorias. |

## ⚙️ Gerenciamento e governança

| Ficha | Escopo | Em uma frase |
|---|---|---|
| [Amazon CloudWatch](gerenciamento/cloudwatch.md) | ✅ | Monitoramento de **métricas, logs e alarmes** de recursos e aplicações AWS e on-premises. |
| [AWS CloudTrail](gerenciamento/cloudtrail.md) | ✅ | Registra as **chamadas de API** da conta — quem fez, o quê, quando, de onde e em qual recurso. |
| [AWS Config](gerenciamento/config.md) | ✅ | Registra a **configuração** dos recursos e seu histórico de mudanças, e avalia continuamente se estão **conformes** com regras. |
| [AWS Systems Manager (SSM)](gerenciamento/systems-manager.md) | ✅ | Central de operações para gerenciar **frotas** de servidores (EC2, on-premises, VMs) em escala, sem acesso manual. |
| [AWS CloudFormation (e CDK, SAM)](gerenciamento/cloudformation.md) | ✅ | Descreve a infraestrutura em templates JSON/YAML e cria tudo de forma **repetível, versionada e automatizada**. |
| [AWS Organizations](gerenciamento/organizations.md) | ✅ | Gerencia várias contas AWS de forma centralizada, com políticas e **uma fatura única**. |
| [AWS Control Tower](gerenciamento/control-tower.md) | ✅ | Monta e governa automaticamente um ambiente multi-conta seguro e padronizado (**landing zone**) sobre o Organizations. |
| [AWS Service Catalog e AWS Resource Access Manager (RAM)](gerenciamento/service-catalog-e-ram.md) | ✅ | Service Catalog oferece um **catálogo de produtos aprovados** para autoatendimento; RAM **compartilha recursos** entre contas. |
| [AWS Trusted Advisor](gerenciamento/trusted-advisor.md) | ✅ | Inspeciona sua conta e recomenda melhorias com base nas boas práticas da AWS. |
| [AWS Health Dashboard](gerenciamento/health-dashboard.md) | ✅ | Mostra o status dos serviços AWS e, principalmente, os eventos que afetam **os seus** recursos. |
| [AWS Compute Optimizer, Service Quotas, License Manager e outros](gerenciamento/compute-optimizer-service-quotas-e-license-manager.md) | ✅ | Ferramentas para dimensionar recursos, controlar limites e licenças, e organizar o ambiente. |

## 📊 Analytics

| Ficha | Escopo | Em uma frase |
|---|---|---|
| [Amazon Athena](analytics/athena.md) | ✅ | Consultas **SQL serverless** direto em arquivos no S3, pagando só pelos dados escaneados. |
| [AWS Glue](analytics/glue.md) | ✅ | Serviço **serverless de ETL** e **catálogo de dados** para descobrir, preparar e combinar dados para análise. |
| [Amazon Kinesis e Amazon Data Firehose](analytics/kinesis.md) | ✅ | Coleta, processa e entrega **dados em streaming e tempo real** (cliques, logs, telemetria, vídeo). |
| [Amazon EMR](analytics/emr.md) | ✅ | Plataforma gerenciada de **big data** para rodar Apache Spark, Hadoop, Hive, Presto/Trino, HBase e Flink. |
| [Amazon QuickSight (Amazon Quick Sight)](analytics/quicksight.md) | ✅ | BI **serverless** para criar dashboards e relatórios interativos, inclusive com perguntas em linguagem natural. |
| [Amazon OpenSearch Service](analytics/opensearch.md) | ✅ | Busca de texto, análise de logs e observabilidade com OpenSearch (sucessor do Elasticsearch gerenciado). |
| [Lake Formation, MSK, Data Exchange, AppFlow e outros serviços de dados](analytics/lake-formation-msk-e-outros.md) | 🔀 | Serviços de dados que aparecem como "qual serviço faz X" — saiba a função de cada um. |

## 🤖 IA e machine learning

| Ficha | Escopo | Em uma frase |
|---|---|---|
| [Amazon SageMaker AI](ia-ml/sagemaker-ai.md) | ✅ | Plataforma completa para **construir, treinar e implantar modelos de ML próprios**. |
| [Amazon Bedrock](ia-ml/bedrock.md) | ⚪ | Acesso **serverless via API** a modelos de fundação (foundation models) de vários provedores para criar aplicações de IA generativa. |
| [Amazon Q](ia-ml/amazon-q.md) | ✅ | Família de **assistentes de IA generativa** prontos para desenvolvedores e para dados corporativos. |
| [Serviços de IA prontos (Rekognition, Comprehend, Lex, Polly, Transcribe, Translate, Textract, Kendra, Personalize…)](ia-ml/servicos-de-ia-prontos.md) | 🔀 | APIs de IA já treinadas pela AWS — você não precisa de experiência em ML, só chama a API. |

## 🔗 Integração de aplicações

| Ficha | Escopo | Em uma frase |
|---|---|---|
| [Amazon SQS (Simple Queue Service)](integracao/sqs.md) | ✅ | Fila de mensagens gerenciada que **desacopla** quem pede um trabalho de quem o executa e absorve picos. |
| [Amazon SNS (Simple Notification Service)](integracao/sns.md) | ✅ | Serviço **pub/sub**: um produtor publica num **tópico** e a mensagem é **empurrada** para todos os assinantes. |
| [Amazon EventBridge](integracao/eventbridge.md) | ✅ | **barramento de eventos** serverless que recebe eventos de serviços AWS, das suas aplicações e de parceiros SaaS e os roteia por **regras**. |
| [AWS Step Functions](integracao/step-functions.md) | ✅ | Orquestra **fluxos de trabalho de várias etapas** como máquinas de estado visuais, com tratamento de erros e retentativas. |
| [Amazon MQ](integracao/amazon-mq.md) | ⚪ | Brokers de mensagens gerenciados **Apache ActiveMQ** e **RabbitMQ**, compatíveis com protocolos padrão. |

## 🛠️ Ferramentas de desenvolvedor

| Ficha | Escopo | Em uma frase |
|---|---|---|
| [Formas de acesso: Console, CLI, SDKs, CloudShell (e Cloud9)](desenvolvimento/cli-sdk-e-cloudshell.md) | 🔀 | Toda ação na AWS é uma **chamada de API** — Console, CLI e SDKs são apenas formas diferentes de fazê-la. |
| [Ferramentas de CI/CD: CodeCommit, CodeBuild, CodeDeploy, CodePipeline, CodeArtifact](desenvolvimento/code-services.md) | 🔀 | Serviços gerenciados que cobrem a esteira **código → build → teste → deploy**. |
| [AWS X-Ray](desenvolvimento/x-ray.md) | ✅ | **rastreamento distribuído** — acompanha cada requisição através dos microsserviços para achar gargalos e erros. |

## 💼 Aplicações de negócio, usuário final e IoT

| Ficha | Escopo | Em uma frase |
|---|---|---|
| [Amazon Connect](aplicacoes/amazon-connect.md) | ✅ | **central de atendimento (contact center) omnicanal na nuvem**, pronta em minutos e paga por uso. |
| [Amazon SES (Simple Email Service)](aplicacoes/ses.md) | ✅ | Envio (e recebimento) de **e-mails** transacionais e de marketing em grande volume. |
| [Amazon WorkSpaces, AppStream 2.0 e WorkSpaces Secure Browser](aplicacoes/workspaces-e-appstream.md) | ✅ | Entregam desktops, aplicações ou um navegador seguro hospedados na AWS para qualquer dispositivo. |
| [AWS Amplify, AWS AppSync e AWS Device Farm](aplicacoes/amplify-e-appsync.md) | 🔀 | Ferramentas para criar, hospedar, conectar e testar aplicações web e mobile rapidamente. |
| [AWS IoT Core, IoT Greengrass e outros serviços de IoT](aplicacoes/iot-core-e-greengrass.md) | 🔀 | Conectar, gerenciar e processar dados de bilhões de dispositivos com segurança — na nuvem e na borda. |

## 🚚 Migração e transferência

| Ficha | Escopo | Em uma frase |
|---|---|---|
| [Migration Evaluator, Application Discovery Service e Migration Hub](migracao/discovery-migration-hub-e-evaluator.md) | ✅ | As ferramentas das fases **avaliar → planejar → acompanhar** de uma migração. |
| [AWS Application Migration Service (AWS MGN)](migracao/application-migration-service.md) | ✅ | Migração **lift-and-shift (Rehost)** de servidores físicos, virtuais ou de outras nuvens para EC2, com mínima indisponibilidade. |
| [AWS Database Migration Service (DMS) e Schema Conversion Tool (SCT)](migracao/dms-e-sct.md) | ✅ | O DMS **move os dados** (com o banco de origem funcionando); o SCT **converte o schema** entre motores diferentes. |
| [Família AWS Snow (Snowball Edge, Snowcone, Snowmobile)](migracao/snow-family.md) | ⚪ | Dispositivos físicos robustos para **mover grandes volumes de dados** quando a rede é lenta, cara ou inexistente, e para **computação na borda** desconectada. |
| [AWS DataSync e AWS Transfer Family](migracao/datasync-e-transfer-family.md) | 🔀 | DataSync **move dados online** de forma automatizada e rápida; Transfer Family oferece **SFTP/FTPS/FTP** gerenciado com armazenamento em S3/EFS. |

## 💰 Custos e suporte

| Ficha | Escopo | Em uma frase |
|---|---|---|
| [AWS Cost Explorer](custos/cost-explorer.md) | ✅ | Visualiza, analisa e **prevê** seus custos e uso da AWS ao longo do tempo. |
| [AWS Budgets](custos/budgets.md) | ✅ | Define orçamentos de custo e uso e **alerta** (ou **age**) quando o valor real ou **previsto** ultrapassa o limite. |
| [Pricing Calculator, Cost and Usage Report e outras ferramentas de faturamento](custos/pricing-calculator-cur-e-outras-ferramentas.md) | ✅ | Ferramentas para estimar, detalhar, ratear, otimizar e acompanhar os custos da AWS. |
| [Planos de AWS Support](custos/planos-de-suporte.md) | ✅ | Níveis de suporte técnico da AWS — quanto mais alto, mais rápido o atendimento e mais acompanhamento proativo. |
| [Recursos de ajuda, parceiros e serviços ao cliente (AWS IQ, Managed Services, Professional Services, re:Post…)](custos/recursos-de-ajuda-e-parceiros.md) | 🔀 | Além dos planos de suporte, a AWS oferece comunidade, documentação, consultoria, parceiros e operação terceirizada — a prova pede quem procurar em cada situação. |

## ❌ Fora do escopo da prova (só para referência)

| Ficha | Escopo | Em uma frase |
|---|---|---|
| [Serviços de mídia e jogos (Elemental, IVS, Elastic Transcoder, GameLift, Lumberyard)](fora-do-escopo/midia-e-jogos.md) | ❌ | Serviços para processar e transmitir vídeo e para hospedar jogos — úteis para conhecer, mas a prova os usa só como distratores. |
| [IoT, robótica, satélite e visão computacional na borda (Device Defender, Monitron, Panorama, RoboMaker, Ground Station)](fora-do-escopo/iot-robotica-e-satelite.md) | ❌ | Serviços especializados para dispositivos, robôs, satélites e câmeras inteligentes — fora da prova, que só cobra o IoT Core. |
| [Desenvolvimento e aplicações (AppConfig, Infrastructure Composer, CodeGuru, Copilot, Refactor Spaces, AppFabric, SWF, WorkDocs)](fora-do-escopo/desenvolvimento-e-aplicacoes.md) | ❌ | Ferramentas de desenvolvimento, modernização e colaboração que existem na AWS, mas não caem na prova. |
| [Rede e diretório (Cloud Map, VPC Lattice, Network Access Analyzer, Cloud Directory)](fora-do-escopo/rede-e-diretorio.md) | ❌ | Serviços de rede de aplicação e de diretório que complementam a VPC, mas não caem na prova. |
| [Gerenciamento e custos (Data Lifecycle Manager, Chatbot, Launch Wizard, Application Cost Profiler, DevPay)](fora-do-escopo/gerenciamento-e-custos.md) | ❌ | Ferramentas auxiliares de operação e de cobrança que existem na AWS, mas não caem na prova. |
