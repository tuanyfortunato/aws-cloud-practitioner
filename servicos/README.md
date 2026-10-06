# 🔎 Fichas de serviços AWS

## 🧭 Por onde começar

Se você ainda não conhece um serviço, abra sua ficha e leia a abertura: **Comece pelo problema** ou, nas fichas já no modelo novo, **Que problema resolve**. A abertura explica a dificuldade, a solução, um exemplo, os limites e as primeiras palavras técnicas. Só depois avance para componentes, configurações e questões da prova.

Uma ficha por serviço (ou família de serviços), com o que cai na prova e o que vai além: componentes, configurações, limites, cobrança, responsabilidade compartilhada, atualizações 2025-2026, pegadinhas e perguntas típicas.

> Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.
>
> Coluna *Escopo* ([lista oficial](../docs/00-guia-do-exame/escopo-oficial.md)): ✅ no escopo · 🔀 parcial · ⚪ não listado · ❌ fora do escopo.
>
> Coluna *Grupo*: **núcleo** é ficha completa de serviço central de alguma aula e entra no caderno de consulta impresso; **complementar** é versão curta de serviço periférico no escopo; **referência** é serviço fora da lista oficial, mantido só no digital para reconhecer distratores.
>
> Modelo para novas fichas: [`templates/servico.md`](../templates/servico.md).


## 🖥️ Computação

| Ficha | Escopo | Grupo | Em uma frase |
|---|---|---|---|
| [Amazon EC2 (Elastic Compute Cloud)](computacao/ec2.md) | ✅ | núcleo | Servidores virtuais sob demanda, com controle total do sistema operacional (IaaS). |
| [Amazon EC2 Auto Scaling](computacao/ec2-auto-scaling.md) | ✅ | núcleo | Aumenta e reduz automaticamente o número de instâncias EC2 para acompanhar a demanda e substitui as que falham. |
| [Elastic Load Balancing (ELB)](computacao/elastic-load-balancing.md) | ✅ | núcleo | Distribui automaticamente o tráfego que chega entre destinos saudáveis, como instâncias EC2, containers e endereços IP, em uma ou mais zonas de disponibilidade. |
| [AWS Lambda](computacao/lambda.md) | ✅ | núcleo | Roda código em resposta a eventos sem que você provisione ou gerencie servidores, cobrando pelos pedidos e pela duração. |
| [Amazon ECS (Elastic Container Service)](computacao/ecs.md) | ✅ | núcleo | Orquestrador de containers totalmente gerenciado da própria AWS, que decide onde e quantos containers rodam. |
| [Amazon EKS (Elastic Kubernetes Service)](computacao/eks.md) | ✅ | núcleo | Kubernetes gerenciado: a AWS opera o plano de controle do cluster, e você roda suas aplicações em containers. |
| [AWS Fargate](computacao/fargate.md) | ✅ | núcleo | Mecanismo de computação serverless que roda containers do ECS ou do EKS sem que você provisione ou gerencie servidores. |
| [Amazon ECR (Elastic Container Registry)](computacao/ecr.md) | ✅ | complementar | Registro gerenciado da AWS para guardar e distribuir imagens de container, com repositórios privados controlados pelo IAM e também repositórios públicos. |
| [AWS Elastic Beanstalk](computacao/elastic-beanstalk.md) | ✅ | núcleo | Você envia o código, e o Elastic Beanstalk cria e gerencia instâncias, balanceamento, escalonamento e monitoramento para rodá-lo. |
| [Amazon Lightsail](computacao/lightsail.md) | ✅ | complementar | O jeito mais simples de começar na AWS para criar sites e aplicações web, com servidores, bancos e rede reunidos em planos de preço mensal previsível. |
| [AWS Batch](computacao/batch.md) | ✅ | complementar | Serviço totalmente gerenciado para cargas em lote de qualquer escala: recebe as tarefas, provisiona a capacidade e a libera quando o trabalho acaba. |
| [AWS Outposts, Local Zones e Wavelength](computacao/outposts-local-zones-wavelength.md) | 🔀 | complementar | Formas de levar a infraestrutura da AWS para mais perto: o Outposts no local do cliente, as Local Zones perto de grandes cidades e o Wavelength na rede das operadoras. |

## 🗄️ Armazenamento

| Ficha | Escopo | Grupo | Em uma frase |
|---|---|---|---|
| [Amazon S3 (Simple Storage Service)](armazenamento/s3.md) | ✅ | núcleo | Guarda arquivos como objetos em buckets, sem limite de quantidade, com durabilidade de 11 noves, acessados pela rede. |
| [Classes de armazenamento do S3 (incluindo S3 Glacier)](armazenamento/s3-classes-de-armazenamento.md) | ✅ | núcleo | Cada classe troca preço de armazenamento por custo e tempo de recuperação; escolha pelo quanto o dado é acessado. |
| [Amazon EBS (Elastic Block Store) e instance store](armazenamento/ebs.md) | ✅ | núcleo | Volumes de disco persistentes, ligados pela rede a instâncias do EC2, que continuam existindo quando a instância para. |
| [Amazon EFS (Elastic File System)](armazenamento/efs.md) | ✅ | núcleo | Sistema de arquivos NFS serverless e elástico, montado ao mesmo tempo por várias instâncias, containers e funções Linux. |
| [Amazon FSx](armazenamento/fsx.md) | 🔀 | complementar | Sistemas de arquivos conhecidos, totalmente gerenciados: Windows File Server, Lustre, NetApp ONTAP e OpenZFS. |
| [AWS Storage Gateway](armazenamento/storage-gateway.md) | ✅ | núcleo | Liga servidores e pessoas no datacenter local ao armazenamento da AWS por NFS, SMB, iSCSI ou fitas virtuais, com cache local. |
| [AWS Backup](armazenamento/aws-backup.md) | ✅ | núcleo | Centraliza e automatiza os backups de vários serviços da AWS com planos aplicados aos recursos, num só lugar. |
| [AWS Elastic Disaster Recovery (AWS DRS)](armazenamento/elastic-disaster-recovery.md) | ✅ | complementar | Replica continuamente servidores locais ou na nuvem para uma área de preparação barata na AWS e, num desastre, lança instâncias de recuperação em minutos. |

## 🛢️ Banco de dados

| Ficha | Escopo | Grupo | Em uma frase |
|---|---|---|---|
| [Amazon RDS (Relational Database Service)](banco-de-dados/rds.md) | ✅ | núcleo | Banco relacional gerenciado: a AWS cuida de hardware, sistema operacional, patches do banco, backups e failover. |
| [Amazon Aurora](banco-de-dados/aurora.md) | ✅ | núcleo | Motor relacional da AWS que funciona com MySQL e PostgreSQL, com armazenamento que cresce sozinho e cópias em três zonas. |
| [Amazon DynamoDB](banco-de-dados/dynamodb.md) | ✅ | núcleo | Banco NoSQL serverless, de chave-valor e documento, com respostas em milissegundos de um dígito em qualquer escala. |
| [Amazon ElastiCache](banco-de-dados/elasticache.md) | ✅ | núcleo | Cache em memória gerenciado, com Valkey, Memcached ou Redis OSS, que responde em microssegundos e alivia o banco. |
| [Amazon MemoryDB](banco-de-dados/memorydb.md) | ❌ | referência | Banco de dados em memória e durável, que trabalha com Valkey e Redis OSS e pode ser o banco principal de uma aplicação, não só um cache. |
| [Amazon Redshift](banco-de-dados/redshift.md) | ✅ | núcleo | Data warehouse gerenciado na escala de petabytes, consultado com SQL e ferramentas de relatório (BI). |
| [Amazon DocumentDB](banco-de-dados/documentdb.md) | ✅ | complementar | Banco de documentos totalmente gerenciado para aplicações feitas para o MongoDB, que roda o mesmo código, drivers e ferramentas. |
| [Amazon Neptune](banco-de-dados/neptune.md) | ✅ | complementar | Banco de grafos totalmente gerenciado, que guarda itens e as ligações entre eles, para recomendações, detecção de fraude e grafos de conhecimento. |
| [Amazon Keyspaces e Amazon Timestream](banco-de-dados/keyspaces-timestream-e-outros.md) | 🔀 | referência | Dois bancos especializados fora da prova: o Keyspaces para aplicações Apache Cassandra e o Timestream para séries temporais. |

## 🌐 Redes e entrega de conteúdo

| Ficha | Escopo | Grupo | Em uma frase |
|---|---|---|---|
| [Amazon VPC (Virtual Private Cloud)](redes/vpc.md) | ✅ | núcleo | Rede virtual isolada logicamente, definida por você, onde ficam os recursos da AWS numa Região. |
| [VPC Peering, Transit Gateway, VPC Endpoints e PrivateLink](redes/vpc-peering-transit-gateway-e-endpoints.md) | ✅ | núcleo | Formas de ligar VPCs entre si e de acessar serviços de forma privada, sem passar pela internet. |
| [AWS VPN (Site-to-Site VPN e Client VPN)](redes/site-to-site-vpn-e-client-vpn.md) | ✅ | núcleo | Túneis criptografados pela internet que ligam uma rede local (Site-to-Site) ou cada usuário (Client VPN) à AWS. |
| [AWS Direct Connect](redes/direct-connect.md) | ✅ | núcleo | Conexão de rede dedicada e privada entre o datacenter e a AWS, por fibra, sem passar pelos provedores de internet. |
| [Amazon Route 53](redes/route-53.md) | ✅ | núcleo | DNS gerenciado da AWS, que registra domínios, liga nomes aos recursos e desvia o tráfego de recursos com falha. |
| [Amazon CloudFront](redes/cloudfront.md) | ✅ | núcleo | Rede de entrega de conteúdo (CDN) que guarda cópias nos locais de borda, perto dos usuários, e reduz a latência e a carga na origem. |
| [AWS Global Accelerator](redes/global-accelerator.md) | ✅ | núcleo | Dá à aplicação dois IPs estáticos anycast e leva o tráfego TCP ou UDP pela rede global da AWS até o endpoint saudável mais adequado. |
| [Amazon API Gateway](redes/api-gateway.md) | ✅ | núcleo | Cria, publica, mantém, monitora e protege APIs REST, HTTP e WebSocket em qualquer escala; a porta de entrada de back-ends serverless. |

## 🔐 Segurança, identidade e compliance

| Ficha | Escopo | Grupo | Em uma frase |
|---|---|---|---|
| [AWS IAM (Identity and Access Management) e AWS STS](seguranca/iam.md) | ✅ | núcleo | Controla quem pode se autenticar na conta e o que cada identidade pode fazer em cada recurso. |
| [AWS IAM Identity Center (antigo AWS SSO)](seguranca/iam-identity-center.md) | ✅ | núcleo | Login único para funcionários acessarem várias contas da AWS e aplicações com uma só identidade. |
| [Amazon Cognito](seguranca/cognito.md) | ✅ | núcleo | Cadastro, login e controle de acesso para os usuários de aplicativos web e móveis. |
| [AWS Directory Service](seguranca/directory-service.md) | ✅ | complementar | Formas de usar o Microsoft Active Directory com os serviços da AWS: um diretório gerenciado pela AWS ou a ligação com o diretório que a empresa já tem. |
| [AWS KMS (Key Management Service)](seguranca/kms.md) | ✅ | núcleo | Cria e controla as chaves usadas para cifrar dados, integradas aos serviços da AWS e com cada uso registrado no CloudTrail. |
| [AWS CloudHSM](seguranca/cloudhsm.md) | ✅ | complementar | Módulos de segurança de hardware (HSMs) dedicados a um único cliente, na nuvem, para guardar chaves e fazer operações criptográficas sob controle exclusivo. |
| [AWS Certificate Manager (ACM) e AWS Private CA](seguranca/certificate-manager.md) | ✅ | complementar | Cria, guarda e renova certificados SSL/TLS públicos e privados e os instala nos serviços integrados, como Elastic Load Balancing, CloudFront e API Gateway. |
| [AWS Secrets Manager e Systems Manager Parameter Store](seguranca/secrets-manager-e-parameter-store.md) | ✅ | núcleo | Guardam segredos e configurações fora do código; o Secrets Manager também faz a rotação automática dos segredos. |
| [AWS Shield](seguranca/shield.md) | ✅ | núcleo | Protege as aplicações contra ataques de negação de serviço distribuído (DDoS), de graça no nível Standard e com equipe de resposta e proteção de custo no Advanced. |
| [AWS WAF (Web Application Firewall)](seguranca/waf.md) | ✅ | núcleo | Firewall de aplicações web que examina cada pedido HTTP ou HTTPS e, pelas regras do cliente, deixa passar, bloqueia ou devolve uma resposta personalizada. |
| [AWS Firewall Manager e AWS Network Firewall](seguranca/firewall-manager-e-network-firewall.md) | 🔀 | complementar | O Firewall Manager aplica as mesmas proteções em todas as contas de uma organização; o Network Firewall filtra e inspeciona o tráfego na borda de uma VPC. |
| [Amazon GuardDuty](seguranca/guardduty.md) | ✅ | núcleo | Analisa continuamente os registros da conta com inteligência de ameaças e aprendizado de máquina e gera achados quando vê atividade suspeita. |
| [Amazon Inspector](seguranca/inspector.md) | ✅ | núcleo | Descobre instâncias EC2, imagens de contêiner e funções Lambda e as examina continuamente em busca de vulnerabilidades conhecidas de software e de exposição de rede não intencional. |
| [Amazon Macie](seguranca/macie.md) | ✅ | núcleo | Descobre dados sensíveis no Amazon S3 com aprendizado de máquina e reconhecimento de padrões e avalia a segurança e o controle de acesso dos buckets. |
| [Amazon Detective](seguranca/detective.md) | ✅ | complementar | Ajuda a investigar a causa raiz de achados de segurança e atividades suspeitas, com visualizações de como identidades, recursos e endereços se relacionaram ao longo do tempo. |
| [AWS Security Hub](seguranca/security-hub.md) | ✅ | núcleo | Reúne, correlaciona e prioriza os sinais de segurança do GuardDuty, do Inspector, do Macie e das verificações de postura, e confere as contas contra padrões de boas práticas. |
| [AWS Artifact](seguranca/artifact.md) | ✅ | núcleo | Portal de autoatendimento, gratuito, para baixar os relatórios de segurança e compliance da AWS e aceitar acordos com ela. |
| [AWS Audit Manager](seguranca/audit-manager.md) | ⚪ | referência | Automatiza a coleta de evidências para auditorias, com frameworks prontos de controles; está em modo de manutenção e fora da lista atual do exame. |

## ⚙️ Gerenciamento e governança

| Ficha | Escopo | Grupo | Em uma frase |
|---|---|---|---|
| [Amazon CloudWatch](gerenciamento/cloudwatch.md) | ✅ | núcleo | Monitora recursos e aplicações com métricas, alarmes, painéis e logs, para ver como estão funcionando e agir quando algo passa do limite. |
| [AWS CloudTrail](gerenciamento/cloudtrail.md) | ✅ | núcleo | Registra as ações feitas na conta como eventos, dizendo quem fez o quê, quando, de onde e em qual recurso. |
| [AWS Config](gerenciamento/config.md) | ✅ | núcleo | Registra a configuração dos recursos, as relações entre eles e o histórico de mudanças, e avalia cada recurso contra regras de configuração desejada. |
| [AWS Systems Manager](gerenciamento/systems-manager.md) | ✅ | núcleo | Permite ver e operar de forma central muitas máquinas, em várias contas e Regiões: aplicar patches, rodar comandos, conectar-se sem abrir portas e guardar configurações. |
| [AWS CloudFormation (e CDK, SAM)](gerenciamento/cloudformation.md) | ✅ | núcleo | Cria e atualiza a infraestrutura a partir de um modelo escrito em YAML ou JSON, sempre do mesmo jeito, como uma pilha de recursos que se gerencia em conjunto. |
| [AWS Organizations](gerenciamento/organizations.md) | ✅ | núcleo | Reúne várias contas da AWS numa organização, com políticas aplicadas por grupo de contas e uma fatura única. |
| [AWS Control Tower](gerenciamento/control-tower.md) | ✅ | núcleo | Monta e governa um ambiente com várias contas segundo boas práticas, orquestrando Organizations, IAM Identity Center e outros serviços, e aplicando controles às contas. |
| [AWS Service Catalog e AWS Resource Access Manager (RAM)](gerenciamento/service-catalog-e-ram.md) | ✅ | complementar | O Service Catalog oferece um catálogo de produtos de TI aprovados para autoatendimento; o RAM compartilha recursos entre contas. |
| [AWS Trusted Advisor](gerenciamento/trusted-advisor.md) | ✅ | núcleo | Examina o ambiente da AWS e recomenda onde economizar, melhorar desempenho e disponibilidade, fechar brechas de segurança e respeitar os limites de serviço. |
| [AWS Health Dashboard](gerenciamento/health-dashboard.md) | ✅ | núcleo | Mostra os eventos da AWS que afetam os serviços e as suas contas, como falhas em andamento e manutenções planejadas. |
| [AWS Compute Optimizer, Service Quotas e License Manager](gerenciamento/compute-optimizer-service-quotas-e-license-manager.md) | ✅ | complementar | O Compute Optimizer recomenda o tamanho certo dos recursos, o Service Quotas mostra os limites da conta e pede aumentos, e o License Manager controla licenças de software. |

## 📊 Analytics

| Ficha | Escopo | Grupo | Em uma frase |
|---|---|---|---|
| [Amazon Athena](analytics/athena.md) | ✅ | núcleo | Consulta com SQL padrão os dados guardados no Amazon S3, sem servidor e sem mover os dados, cobrando pelos dados lidos em cada consulta. |
| [AWS Glue](analytics/glue.md) | ✅ | núcleo | Serviço serverless de integração de dados que descobre fontes, mantém um catálogo central e roda pipelines de ETL para preparar os dados para análise. |
| [Amazon Kinesis e Amazon Data Firehose](analytics/kinesis.md) | ✅ | núcleo | O Kinesis Data Streams coleta e guarda por um tempo fluxos de dados para aplicações processarem em tempo real; o Data Firehose entrega fluxos a destinos como S3 e Redshift sem aplicação para escrever. |
| [Amazon EMR](analytics/emr.md) | ✅ | complementar | Plataforma gerenciada de clusters para rodar ferramentas de big data de código aberto, como Apache Hadoop e Apache Spark, e processar volumes muito grandes de dados. |
| [Amazon QuickSight (Amazon Quick Sight)](analytics/quicksight.md) | ✅ | núcleo | Serviço de visualização de dados e BI que se conecta às fontes, cria painéis interativos e permite incorporar análises em aplicações; hoje faz parte do Amazon Quick. |
| [Amazon OpenSearch Service](analytics/opensearch.md) | ✅ | complementar | Serviço gerenciado para implantar, operar e escalar clusters do OpenSearch, para busca, análise de registros e monitoramento de aplicações em tempo real. |
| [Lake Formation, MSK, Data Exchange, AppFlow e Clean Rooms](analytics/lake-formation-msk-e-outros.md) | 🔀 | referência | Serviços de dados fora da prova: governança de data lake, Kafka gerenciado, troca de dados com outras organizações, integração com aplicações SaaS e análise conjunta sem expor dados. |

## 🤖 IA e machine learning

| Ficha | Escopo | Grupo | Em uma frase |
|---|---|---|---|
| [Amazon SageMaker AI](ia-ml/sagemaker-ai.md) | ✅ | núcleo | Serviço de machine learning totalmente gerenciado para criar, treinar e implantar modelos próprios, sem montar nem gerenciar os servidores. |
| [Amazon Bedrock](ia-ml/bedrock.md) | ⚪ | referência | Serviço totalmente gerenciado que dá acesso a modelos de fundação de várias empresas de IA para criar aplicações de IA generativa; não está na lista do exame. |
| [Amazon Q](ia-ml/amazon-q.md) | ✅ | núcleo | Família de assistentes de IA generativa da AWS; o Amazon Q Developer responde perguntas sobre a AWS e os recursos da conta e ajuda a escrever e melhorar código. |
| [Serviços de IA prontos (Rekognition, Comprehend, Lex, Polly, Transcribe, Translate e Textract)](ia-ml/servicos-de-ia-prontos.md) | 🔀 | núcleo | Serviços que a AWS já treinou para tarefas comuns (conversar, falar, transcrever, traduzir, entender textos, analisar imagens e ler documentos), usados por chamadas de API, sem conhecimento de machine learning. |

## 🔗 Integração de aplicações

| Ficha | Escopo | Grupo | Em uma frase |
|---|---|---|---|
| [Amazon SQS (Simple Queue Service)](integracao/sqs.md) | ✅ | núcleo | Fila de mensagens gerenciada que **desacopla** quem pede um trabalho de quem o executa e absorve picos. |
| [Amazon SNS (Simple Notification Service)](integracao/sns.md) | ✅ | núcleo | Serviço de **publicar e assinar**: o publicador envia a mensagem a um **tópico**, e o SNS a empurra para todos os assinantes. |
| [Amazon EventBridge](integracao/eventbridge.md) | ✅ | núcleo | Serviço serverless que recebe **eventos** de serviços da AWS, de aplicações próprias e de softwares de terceiros e os entrega aos destinos certos por **regras**. |
| [AWS Step Functions](integracao/step-functions.md) | ✅ | núcleo | Coordena **fluxos de trabalho** de várias etapas, com decisões, novas tentativas e acompanhamento visual de cada execução. |
| [Amazon MQ](integracao/amazon-mq.md) | ⚪ | referência | Serviço gerenciado de message broker para Apache ActiveMQ Classic e RabbitMQ, para migrar sistemas que já usam esses brokers sem reescrever o código de mensagens. |

## 🛠️ Ferramentas de desenvolvedor

| Ficha | Escopo | Grupo | Em uma frase |
|---|---|---|---|
| [Formas de acesso: Console, CLI, SDKs e CloudShell](desenvolvimento/cli-sdk-e-cloudshell.md) | 🔀 | núcleo | As formas de usar a AWS: cliques no console, comandos na CLI, código com os SDKs e um terminal no navegador com o CloudShell, todas chegando às mesmas APIs. |
| [Ferramentas de CI/CD: CodeBuild e CodePipeline](desenvolvimento/code-services.md) | 🔀 | complementar | O CodeBuild compila e testa o código sem servidores de build; o CodePipeline automatiza a esteira que leva cada mudança do repositório à produção. |
| [AWS X-Ray](desenvolvimento/x-ray.md) | ✅ | complementar | Coleta dados sobre as requisições que a aplicação atende e mostra o caminho de cada uma pelos serviços, bancos e APIs, para achar lentidão e erros. |

## 💼 Aplicações de negócio, usuário final e IoT

| Ficha | Escopo | Grupo | Em uma frase |
|---|---|---|---|
| [Amazon Connect](aplicacoes/amazon-connect.md) | ✅ | complementar | Central de atendimento (contact center) na nuvem, com voz, chat e SMS, filas, roteamento e IA, cobrada pelo uso. |
| [Amazon SES (Simple Email Service)](aplicacoes/ses.md) | ✅ | complementar | Plataforma de e-mail para enviar e receber mensagens com os endereços e domínios da própria empresa: transacionais, de marketing e boletins. |
| [Amazon WorkSpaces, WorkSpaces Applications (AppStream 2.0) e WorkSpaces Secure Browser](aplicacoes/workspaces-e-appstream.md) | ✅ | complementar | Serviços em que o programa roda na AWS e o dispositivo só mostra a tela: desktops virtuais, streaming de aplicações e navegador seguro. |
| [AWS Amplify](aplicacoes/amplify-e-appsync.md) | 🔀 | complementar | Acelera o desenvolvimento de aplicações web e mobile full-stack: hospeda o front-end a partir do Git e adiciona login, armazenamento e dados sem exigir conhecimento de nuvem. |
| [AWS IoT Core e IoT Greengrass](aplicacoes/iot-core-e-greengrass.md) | 🔀 | complementar | O IoT Core permite a comunicação segura, nos dois sentidos, entre dispositivos conectados e os serviços da AWS. |

## 🚚 Migração e transferência

| Ficha | Escopo | Grupo | Em uma frase |
|---|---|---|---|
| [Migration Evaluator, Application Discovery Service e Migration Hub](migracao/discovery-migration-hub-e-evaluator.md) | ✅ | complementar | Ferramentas para antes e durante a migração: o Migration Evaluator monta o caso de negócio, o Discovery Service levanta servidores e dependências e o Migration Hub acompanha o andamento. |
| [AWS Application Migration Service (AWS MGN)](migracao/application-migration-service.md) | ✅ | núcleo | Automatiza o rehost (*lift and shift*) de servidores físicos, virtuais e de outras nuvens para a AWS, com replicação contínua e virada em minutos; hoje se chama AWS Transform MGN. |
| [AWS Database Migration Service (DMS) e Schema Conversion Tool (SCT)](migracao/dms-e-sct.md) | ✅ | núcleo | O DMS move os dados de um banco para a AWS, uma vez ou com replicação contínua; a SCT converte o esquema quando o banco muda de motor. |
| [Família AWS Snow](migracao/snow-family.md) | ⚪ | referência | Dispositivos físicos que a AWS enviava ao cliente para levar dados fora da rede e processar na borda; não estão mais disponíveis para novos clientes. |
| [AWS DataSync e AWS Transfer Family](migracao/datasync-e-transfer-family.md) | 🔀 | referência | O DataSync copia arquivos e objetos pela rede para S3, EFS e FSx; o Transfer Family recebe e envia arquivos por SFTP, FTPS, FTP e AS2. |

## 💰 Custos e suporte

| Ficha | Escopo | Grupo | Em uma frase |
|---|---|---|---|
| [AWS Cost Explorer](custos/cost-explorer.md) | ✅ | núcleo | Mostra os custos e o uso da conta em gráficos e relatórios, com filtros e agrupamentos, até 13 meses para trás e previsão para os próximos. |
| [AWS Budgets](custos/budgets.md) | ✅ | núcleo | Acompanha custos e uso contra um valor definido, avisa quando o real ou o previsto se aproxima ou passa dele e pode agir automaticamente. |
| [Pricing Calculator, Cost and Usage Report e outras ferramentas de faturamento](custos/pricing-calculator-cur-e-outras-ferramentas.md) | ✅ | núcleo | As demais ferramentas de custo da prova: a Pricing Calculator estima antes, as tags e o faturamento consolidado separam e juntam os custos, o Cost Anomaly Detection pega gastos fora do padrão e o Cost and Usage Report entrega os dados completos. |
| [Planos de AWS Support](custos/planos-de-suporte.md) | ✅ | núcleo | Os quatro planos de suporte da AWS (Basic, Business Support+, Enterprise Support e Unified Operations), que vão do atendimento de conta incluído para todos até especialistas designados com resposta em minutos. |
| [Recursos de ajuda, parceiros e AWS Marketplace](custos/recursos-de-ajuda-e-parceiros.md) | 🔀 | núcleo | Onde buscar ajuda além dos planos de suporte: documentação, Knowledge Center e re:Post para resolver sozinho; Professional Services e parceiros da APN para projetos; o Marketplace para software pronto; e o Trust and Safety para denunciar abuso. |

## ❌ Fora do escopo da prova (só para referência)

| Ficha | Escopo | Grupo | Em uma frase |
|---|---|---|---|
| [Serviços de mídia e jogos (Elemental, IVS, Elastic Transcoder, GameLift, Lumberyard)](fora-do-escopo/midia-e-jogos.md) | ❌ | referência | Serviços para processar e transmitir vídeo e para hospedar jogos — úteis para conhecer, mas a prova os usa só como distratores. |
| [IoT, robótica, satélite e visão computacional na borda (Device Defender, Monitron, Panorama, RoboMaker, Ground Station)](fora-do-escopo/iot-robotica-e-satelite.md) | ❌ | referência | Serviços especializados para dispositivos, robôs, satélites e câmeras inteligentes — fora da prova, que só cobra o IoT Core. |
| [Desenvolvimento e aplicações (AppConfig, Infrastructure Composer, CodeGuru, Copilot, Refactor Spaces, AppFabric, SWF, WorkDocs)](fora-do-escopo/desenvolvimento-e-aplicacoes.md) | ❌ | referência | Ferramentas de desenvolvimento, modernização e colaboração que existem na AWS, mas não caem na prova. |
| [Rede e diretório (Cloud Map, VPC Lattice, Network Access Analyzer, Cloud Directory)](fora-do-escopo/rede-e-diretorio.md) | ❌ | referência | Serviços de rede de aplicação e de diretório que complementam a VPC, mas não caem na prova. |
| [Gerenciamento e custos (Data Lifecycle Manager, Chatbot, Launch Wizard, Application Cost Profiler, DevPay)](fora-do-escopo/gerenciamento-e-custos.md) | ❌ | referência | Ferramentas auxiliares de operação e de cobrança que existem na AWS, mas não caem na prova. |
