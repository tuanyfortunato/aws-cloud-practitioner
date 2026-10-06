# 🃏 Flashcards — Domínio 3 — Tecnologia e Serviços de Nuvem

Clique na pergunta para ver a resposta. Gerado a partir das *Perguntas típicas* de cada tópico (`python3 scripts/gerar_docs.py`).

**Total:** 136 cards


## [3.1 Formas de acessar e implantar na AWS](../docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md)

<details>
<summary>Quais são as formas de acessar e operar os serviços da AWS?</summary>

O AWS Management Console (navegador), a AWS CLI (comandos), os AWS SDKs (código da aplicação) e a infraestrutura como código, com o AWS CloudFormation.
</details>

<details>
<summary>Quando usar o console e quando automatizar?</summary>

O console serve para explorar e para tarefas pontuais; tarefas que se repetem devem ser automatizadas com CLI, SDK ou infraestrutura como código.
</details>

<details>
<summary>O que é infraestrutura como código?</summary>

É descrever em um arquivo os recursos de um ambiente e deixar que uma ferramenta os crie; na AWS, o CloudFormation cria os recursos de um modelo como uma pilha.
</details>

<details>
<summary>Qual é a diferença entre a AWS CLI e um AWS SDK?</summary>

A CLI executa comandos no terminal e em scripts; o SDK é uma biblioteca para chamar as APIs da AWS de dentro do código de uma aplicação.
</details>

<details>
<summary>Como a rede de uma empresa pode se conectar à AWS num modelo híbrido?</summary>

Pela internet pública, por uma Site-to-Site VPN (conexão criptografada que passa pela internet) ou pelo Direct Connect (conexão dedicada, sem passar pelos provedores de internet).
</details>


## [3.2 Infraestrutura global](../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md)

<details>
<summary>Qual é a relação entre Região, Zona de Disponibilidade e local de borda?</summary>

Uma Região é uma área geográfica com três ou mais AZs; cada AZ é um ou mais datacenters independentes; os locais de borda são pontos de presença espalhados pelo mundo, perto dos usuários, ligados às Regiões pela rede da AWS.
</details>

<details>
<summary>Por que distribuir uma aplicação em várias AZs aumenta a disponibilidade?</summary>

Porque as AZs não compartilham pontos únicos de falha: têm energia e rede independentes e ficam distantes o bastante para um mesmo evento não atingir duas.
</details>

<details>
<summary>Quando usar várias Regiões?</summary>

Para recuperação de desastres, continuidade de negócios, baixa latência para usuários em outros lugares do mundo e soberania de dados.
</details>

<details>
<summary>Quais fatores pesam na escolha de uma Região?</summary>

Conformidade com leis e regras sobre os dados, latência para os usuários, custo e disponibilidade dos serviços e recursos necessários.
</details>

<details>
<summary>Para que servem os locais de borda?</summary>

Para rodar serviços perto dos usuários, como o CloudFront (entrega de conteúdo), o Route 53 (DNS) e o Global Accelerator, reduzindo a latência.
</details>


## [3.3 Amazon EC2](../docs/03-tecnologia-e-servicos/03-ec2.md)

<details>
<summary>Qual tipo de instância usar para uma aplicação limitada pelo processador?</summary>

Uma instância otimizada para computação, indicada para processamento em lote, transcodificação de mídia e servidores de jogos.
</details>

<details>
<summary>O que é uma AMI?</summary>

É a imagem com o software necessário para iniciar uma instância, como o sistema operacional; pode vir da AWS, do Marketplace, de outra conta ou ser criada por você.
</details>

<details>
<summary>Qual é a diferença entre EBS e instance store?</summary>

O EBS é um disco durável que existe independentemente da instância; o instance store é um disco temporário do computador hospedeiro, cujos dados se perdem quando a instância é parada ou encerrada.
</details>

<details>
<summary>O que é cobrado quando uma instância está parada?</summary>

O uso da instância não é cobrado, mas os volumes EBS e os endereços IPv4 públicos, como Elastic IPs, continuam sendo cobrados.
</details>

<details>
<summary>Quem atualiza o sistema operacional de uma instância do EC2?</summary>

O cliente, porque o EC2 é IaaS: a AWS cuida do hardware e da virtualização, e o cliente controla o sistema operacional e o que roda nele.
</details>


## [3.4 Escalabilidade e balanceamento de carga](../docs/03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md)

<details>
<summary>O que o Amazon EC2 Auto Scaling faz?</summary>

Ajusta o número de instâncias de um grupo à demanda, entre a capacidade mínima e a máxima, e substitui instâncias com defeito para manter a capacidade desejada.
</details>

<details>
<summary>Qual é a diferença entre escala programada, dinâmica e preditiva?</summary>

A programada muda a capacidade em horários definidos; a dinâmica reage à carga atual, como manter 50% de CPU; a preditiva usa o histórico para aumentar a capacidade antes da carga prevista.
</details>

<details>
<summary>Para que serve um balanceador de carga?</summary>

Para distribuir o tráfego entre vários destinos, em uma ou mais AZs, enviando-o só para os que estão saudáveis, com um único ponto de contato para os clientes.
</details>

<details>
<summary>Quando usar um Application Load Balancer e quando usar um Network Load Balancer?</summary>

O ALB, que trabalha na camada 7, serve para rotear pedidos HTTP pelo caminho da URL ou pelo nome do site; o NLB, na camada 4, serve para milhões de pedidos por segundo e IP fixo por AZ.
</details>

<details>
<summary>Por que Auto Scaling e balanceador de carga costumam ser usados juntos?</summary>

Porque o Auto Scaling cria e remove instâncias, e o balanceador distribui o tráfego entre elas; as instâncias criadas são registradas no balanceador automaticamente.
</details>


## [3.5 Containers e serverless](../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)

<details>
<summary>Qual serviço executa código sem servidores, em resposta a eventos?</summary>

Lambda.
</details>

<details>
<summary>Qual é o tempo máximo de execução do Lambda?</summary>

15 minutos.
</details>

<details>
<summary>Como o Lambda é cobrado?</summary>

No modelo base, requisições e duração; extras como concorrência provisionada podem cobrar sem invocação.
</details>

<details>
<summary>Rodar containers sem gerenciar instâncias.</summary>

Fargate (com ECS ou EKS).
</details>

<details>
<summary>Empresa já usa Kubernetes on-premises e quer migrar.</summary>

EKS.
</details>

<details>
<summary>Onde guardar imagens Docker privadas?</summary>

ECR.
</details>

<details>
<summary>Qual serviço orquestra containers e é nativo da AWS?</summary>

ECS.
</details>


## [3.6 Outros serviços de computação](../docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md)

<details>
<summary>Desenvolvedor quer só subir o código Java e deixar a AWS cuidar de capacidade e balanceamento.</summary>

Elastic Beanstalk.
</details>

<details>
<summary>Elastic Beanstalk tem custo próprio?</summary>

Não; paga-se só os recursos que ele cria.
</details>

<details>
<summary>Site WordPress simples com preço mensal fixo.</summary>

Lightsail.
</details>

<details>
<summary>Processar milhares de jobs em lote com a capacidade ideal.</summary>

AWS Batch.
</details>


## [3.7 Bancos de dados](../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)

<details>
<summary>Qual a vantagem do RDS sobre instalar o banco no EC2?</summary>

A AWS cuida de patch, backups, hardware e failover.
</details>

<details>
<summary>Como garantir failover automático do banco para outra AZ?</summary>

RDS Multi-AZ.
</details>

<details>
<summary>Como aliviar consultas de leitura pesadas?</summary>

Read Replicas (ou cache com ElastiCache).
</details>

<details>
<summary>Qual banco relacional compatível com MySQL e PostgreSQL oferece mais performance?</summary>

Aurora.
</details>

<details>
<summary>Qual banco NoSQL serverless com latência de milissegundos?</summary>

DynamoDB.
</details>

<details>
<summary>Replicação multi-região ativa-ativa no DynamoDB.</summary>

Global Tables.
</details>

<details>
<summary>Cache de microssegundos para DynamoDB.</summary>

DAX.
</details>

<details>
<summary>Banco para relacionamentos complexos (redes sociais, fraude).</summary>

Neptune.
</details>

<details>
<summary>Migrar banco MongoDB para serviço gerenciado.</summary>

DocumentDB.
</details>

<details>
<summary>Data warehouse para relatórios de BI sobre petabytes.</summary>

Redshift.
</details>

<details>
<summary>Quais motores o RDS suporta?</summary>

MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Db2 e Aurora.
</details>


## [3.8 Amazon S3 — armazenamento de objetos](../docs/03-tecnologia-e-servicos/08-s3.md)

<details>
<summary>Qual é a durabilidade do S3?</summary>

11 noves (99,999999999%).
</details>

<details>
<summary>Como proteger contra exclusão acidental?</summary>

Versionamento (e MFA Delete).
</details>

<details>
<summary>Como mover dados para classes mais baratas automaticamente após 30 dias?</summary>

Lifecycle policy.
</details>

<details>
<summary>Como dar acesso temporário a um arquivo privado?</summary>

Presigned URL.
</details>

<details>
<summary>Como hospedar um site estático barato?</summary>

S3 (com CloudFront na frente).
</details>

<details>
<summary>Como copiar objetos automaticamente para outra região?</summary>

Cross-Region Replication.
</details>

<details>
<summary>Como acelerar uploads de outros continentes?</summary>

S3 Transfer Acceleration.
</details>

<details>
<summary>Qual classe para dados com acesso imprevisível?</summary>

Intelligent-Tiering.
</details>

<details>
<summary>Qual a classe mais barata para arquivamento de longo prazo?</summary>

Glacier Deep Archive.
</details>

<details>
<summary>Qual classe guarda dados em uma única AZ?</summary>

One Zone-IA (ou Express One Zone).
</details>

<details>
<summary>Como garantir que logs não sejam alterados por 7 anos (WORM)?</summary>

S3 Object Lock.
</details>


## [3.9 Outros serviços de armazenamento](../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)

<details>
<summary>Qual armazenamento em bloco persistente para EC2?</summary>

EBS.
</details>

<details>
<summary>Um volume EBS pode ser usado em outra AZ?</summary>

Não diretamente; cria-se um snapshot e um novo volume na outra AZ.
</details>

<details>
<summary>Onde ficam os snapshots do EBS?</summary>

No S3 (gerenciado pela AWS), de forma incremental.
</details>

<details>
<summary>Sistema de arquivos compartilhado para várias instâncias Linux.</summary>

EFS.
</details>

<details>
<summary>Compartilhamento de arquivos Windows integrado ao Active Directory.</summary>

FSx for Windows File Server.
</details>

<details>
<summary>Sistema de arquivos de alto desempenho para HPC.</summary>

FSx for Lustre.
</details>

<details>
<summary>Aplicações locais precisam usar armazenamento da AWS.</summary>

Storage Gateway.
</details>

<details>
<summary>Substituir fitas físicas de backup.</summary>

Tape Gateway.
</details>

<details>
<summary>Centralizar backups de vários serviços com políticas.</summary>

AWS Backup.
</details>

<details>
<summary>Mover dezenas de terabytes sem depender da internet.</summary>

Snowball Edge.
</details>

<details>
<summary>Processar dados num navio sem conexão.</summary>

Família Snow (computação na borda).
</details>

<details>
<summary>Recuperar servidores em minutos após desastre.</summary>

AWS Elastic Disaster Recovery.
</details>


## [3.10 Rede e entrega de conteúdo](../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)

<details>
<summary>O que torna uma subnet pública?</summary>

Ter rota para um Internet Gateway.
</details>

<details>
<summary>Instâncias em subnet privada precisam baixar atualizações.</summary>

NAT Gateway.
</details>

<details>
<summary>Conectar duas VPCs de contas diferentes.</summary>

VPC Peering.
</details>

<details>
<summary>Conectar dezenas de VPCs e o datacenter num hub.</summary>

Transit Gateway.
</details>

<details>
<summary>Acessar o S3 a partir da VPC sem passar pela internet.</summary>

Gateway VPC endpoint.
</details>

<details>
<summary>Conexão privada e dedicada, sem internet, com desempenho consistente.</summary>

Direct Connect.
</details>

<details>
<summary>Conexão criptografada com o datacenter, pronta hoje.</summary>

Site-to-Site VPN.
</details>

<details>
<summary>Funcionários em casa precisam acessar a VPC.</summary>

Client VPN.
</details>

<details>
<summary>Registrar domínio e gerenciar DNS.</summary>

Route 53.
</details>

<details>
<summary>Mandar 10% dos usuários para a nova versão.</summary>

Route 53 weighted routing.
</details>

<details>
<summary>Reduzir latência de conteúdo para usuários globais.</summary>

CloudFront.
</details>

<details>
<summary>IPs estáticos globais e failover rápido entre regiões para TCP/UDP.</summary>

Global Accelerator.
</details>

<details>
<summary>Criar e proteger uma API REST para funções Lambda.</summary>

API Gateway.
</details>


## [3.11 Analytics](../docs/03-tecnologia-e-servicos/11-analytics.md)

<details>
<summary>Consultar arquivos no S3 com SQL padrão, sem infraestrutura.</summary>

Athena.
</details>

<details>
<summary>Como o Athena é cobrado?</summary>

Por volume de dados escaneados.
</details>

<details>
<summary>Serviço de ETL serverless e catálogo de dados.</summary>

Glue.
</details>

<details>
<summary>Ingerir e processar dados de cliques em tempo real.</summary>

Kinesis Data Streams.
</details>

<details>
<summary>Entregar dados de streaming no S3 sem administração.</summary>

Amazon Data Firehose.
</details>

<details>
<summary>Rodar Spark e Hadoop gerenciados.</summary>

EMR.
</details>

<details>
<summary>Criar dashboards interativos de BI.</summary>

QuickSight.
</details>

<details>
<summary>Busca de texto e análise de logs.</summary>

OpenSearch Service.
</details>


## [3.12 IA e machine learning](../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)

<details>
<summary>Construir, treinar e implantar modelos de ML próprios.</summary>

SageMaker AI.
</details>

<details>
<summary>Identificar rostos e objetos em fotos.</summary>

Rekognition.
</details>

<details>
<summary>Analisar o sentimento de avaliações de clientes.</summary>

Comprehend.
</details>

<details>
<summary>Criar um chatbot de atendimento.</summary>

Lex.
</details>

<details>
<summary>Converter texto em voz.</summary>

Polly.
</details>

<details>
<summary>Converter áudio em texto.</summary>

Transcribe.
</details>

<details>
<summary>Traduzir conteúdo do site.</summary>

Translate.
</details>

<details>
<summary>Extrair dados de formulários escaneados.</summary>

Textract.
</details>

<details>
<summary>Busca inteligente nos documentos internos da empresa.</summary>

Kendra.
</details>

<details>
<summary>Assistente de IA generativa para funcionários e desenvolvedores.</summary>

Amazon Q.
</details>


## [3.13 Integração de aplicações](../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)

<details>
<summary>Desacoplar componentes para que um pico não derrube o processamento.</summary>

SQS.
</details>

<details>
<summary>Ordenar mensagens por grupo e tratar duplicações no envio.</summary>

Fila SQS FIFO; o programa ainda precisa evitar efeitos repetidos.
</details>

<details>
<summary>Enviar a mesma mensagem para vários sistemas e para e-mail.</summary>

SNS.
</details>

<details>
<summary>Um evento precisa ser processado por várias filas em paralelo.</summary>

Fan-out com SNS + SQS.
</details>

<details>
<summary>Reagir a eventos de serviços AWS e de aplicações SaaS com regras.</summary>

EventBridge.
</details>

<details>
<summary>Executar uma tarefa todo dia às 2h sem servidor.</summary>

EventBridge Scheduler (disparando Lambda).
</details>

<details>
<summary>Orquestrar um processo com várias etapas e tratamento de erro.</summary>

Step Functions.
</details>


## [3.14 Aplicações de negócio, usuário final, front-end e IoT](../docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md)

<details>
<summary>Criar uma central de atendimento na nuvem.</summary>

Amazon Connect.
</details>

<details>
<summary>Enviar e-mails de confirmação e marketing em massa.</summary>

SES.
</details>

<details>
<summary>Oferecer desktops virtuais a funcionários remotos.</summary>

WorkSpaces.
</details>

<details>
<summary>Disponibilizar um aplicativo de desktop pelo navegador.</summary>

AppStream 2.0.
</details>

<details>
<summary>Criar e hospedar rapidamente um app web ou mobile full-stack.</summary>

Amplify.
</details>

<details>
<summary>API GraphQL gerenciada com dados em tempo real.</summary>

AppSync.
</details>

<details>
<summary>Conectar milhões de sensores à nuvem.</summary>

IoT Core.
</details>


## [3.15 Ferramentas de desenvolvimento](../docs/03-tecnologia-e-servicos/15-ferramentas-de-desenvolvimento.md)

<details>
<summary>Orquestrar a esteira de CI/CD na AWS.</summary>

CodePipeline.
</details>

<details>
<summary>Compilar e executar testes sem gerenciar servidores de build.</summary>

CodeBuild.
</details>

<details>
<summary>Automatizar deploy em EC2 e servidores on-premises.</summary>

CodeDeploy.
</details>

<details>
<summary>Encontrar gargalos de latência entre microsserviços.</summary>

X-Ray.
</details>


## [3.16 Gestão e governança](../docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md)

<details>
<summary>Provisionar infraestrutura a partir de templates JSON/YAML.</summary>

CloudFormation.
</details>

<details>
<summary>Implantar a mesma stack em várias contas e regiões.</summary>

CloudFormation StackSets.
</details>

<details>
<summary>Gerenciar e aplicar patches em uma frota de instâncias, inclusive on-premises.</summary>

Systems Manager.
</details>

<details>
<summary>Acessar a instância sem abrir a porta 22.</summary>

Systems Manager Session Manager.
</details>

<details>
<summary>Ver eventos de manutenção da AWS que afetam meus recursos.</summary>

AWS Health Dashboard.
</details>

<details>
<summary>Pedir aumento do limite de instâncias.</summary>

Service Quotas.
</details>

<details>
<summary>Controlar quantas licenças de SQL Server estão em uso.</summary>

License Manager.
</details>

<details>
<summary>Recomendar o tamanho ideal das instâncias com base no uso.</summary>

Compute Optimizer.
</details>


## [3.17 Migração e transferência](../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md)

<details>
<summary>Levantar servidores e dependências antes de migrar.</summary>

Application Discovery Service.
</details>

<details>
<summary>Estimar quanto a empresa vai economizar ao migrar.</summary>

Migration Evaluator.
</details>

<details>
<summary>Acompanhar todas as migrações num painel central.</summary>

Migration Hub.
</details>

<details>
<summary>Migrar servidores físicos e VMs para EC2 com pouca indisponibilidade.</summary>

Application Migration Service.
</details>

<details>
<summary>Migrar um banco sem desligar a aplicação.</summary>

DMS.
</details>

<details>
<summary>Converter um banco Oracle para Aurora PostgreSQL.</summary>

SCT + DMS.
</details>

<details>
<summary>Transferir arquivos online de forma automatizada para o S3.</summary>

DataSync.
</details>

<details>
<summary>Parceiros enviam arquivos via SFTP para o S3.</summary>

Transfer Family.
</details>


## [3.18 Serviços menos conhecidos que podem aparecer](../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md)

<details>
<summary>Como acompanhar a pegada de carbono do uso da AWS?</summary>

AWS Customer Carbon Footprint Tool.
</details>

<details>
<summary>Onde contratar especialistas certificados sob demanda para um projeto pequeno?</summary>

AWS IQ (descontinuado; hoje, AWS Marketplace Professional Services ou um parceiro da APN).
</details>

<details>
<summary>Qual serviço emite as credenciais temporárias usadas pelas roles?</summary>

AWS STS.
</details>

<details>
<summary>A aplicação usa RabbitMQ e deve migrar sem mudar o código.</summary>

Amazon MQ.
</details>

<details>
<summary>Testar a resiliência injetando falhas de propósito.</summary>

AWS Fault Injection Service.
</details>

<details>
<summary>Testar um app mobile em centenas de dispositivos reais.</summary>

AWS Device Farm.
</details>
