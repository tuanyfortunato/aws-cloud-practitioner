# ❓ Questões — Domínio 3 — Tecnologia e Serviços de Nuvem (34%)

26 questões no formato da prova, em ordem de tópico. Responda antes de abrir "Ver resposta".

⬅️ [Todas as questões por domínio](README.md)

---

### Questão 1

<sub>Domínio 3 · tópico [3.1](../../docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md)</sub>

O sistema de matrícula de uma escola, escrito em Python, precisa gravar automaticamente o comprovante de cada aluno num bucket do Amazon S3, sem ninguém clicar em nada. Qual forma de acesso à AWS deve ser usada?

- **A)** O AWS Management Console
- **B)** Um AWS SDK, chamado de dentro do código da aplicação
- **C)** A AWS CLI, executada manualmente pela equipe
- **D)** Um modelo do AWS CloudFormation

<details>
<summary>Ver resposta</summary>

**Resposta: B**

Os **AWS SDKs** são bibliotecas para chamar as APIs da AWS de dentro de um programa, em linguagens como Python e Java. O console serve para tarefas pontuais; a CLI serve para comandos e scripts no terminal; o CloudFormation cria e atualiza a infraestrutura, não grava os dados que a aplicação produz. Todas as formas usam as mesmas APIs e as mesmas permissões do IAM.

</details>

### Questão 2

<sub>Domínio 3 · tópico [3.1](../../docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md)</sub>

Todo semestre, uma equipe monta à mão o mesmo ambiente de testes (servidores, balanceador e banco de dados), e às vezes esquece uma configuração. Ela quer criar o ambiente sempre igual e, no futuro, repeti-lo em outra Região. Qual abordagem atende a esse objetivo?

- **A)** Usar o AWS SDK dentro da aplicação de matrícula
- **B)** Consultar as recomendações do AWS Trusted Advisor
- **C)** Seguir um roteiro escrito no AWS Management Console
- **D)** Descrever o ambiente num modelo do AWS CloudFormation (infraestrutura como código)

<details>
<summary>Ver resposta</summary>

**Resposta: D**

Com **infraestrutura como código**, o modelo do **CloudFormation** descreve o ambiente, e cada pilha criada a partir dele sai igual, em qualquer Região; apagar a pilha remove os recursos. Um roteiro no console continua dependendo de alguém seguir cada passo; o SDK serve para a aplicação usar a AWS; o Trusted Advisor dá recomendações, não cria ambientes.

</details>

### Questão 3

<sub>Domínio 3 · tópico [3.2](../../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md) · **múltipla resposta**</sub>

Quais DOIS fatores uma empresa deve considerar ao escolher a região AWS para uma nova aplicação? (Escolha DUAS.)

- **A)** A data de criação da conta AWS
- **B)** Proximidade dos clientes para reduzir a latência
- **C)** A quantidade de usuários IAM da conta
- **D)** O número de buckets S3 já existentes
- **E)** Requisitos de conformidade e residência de dados

<details>
<summary>Ver resposta</summary>

**Resposta: B, E**

Os quatro fatores clássicos são **conformidade/residência de dados**, **latência para os clientes**, **serviços disponíveis na região** e **preço**. Usuários IAM, idade da conta e buckets existentes não influenciam a escolha.

</details>

### Questão 4

<sub>Domínio 3 · tópico [3.2](../../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md)</sub>

Um hospital precisa processar dados localmente, no próprio datacenter, por exigência de residência de dados, mas quer usar as mesmas APIs, ferramentas e serviços da AWS. Qual solução atende a esse requisito?

- **A)** AWS Local Zones
- **B)** AWS Outposts
- **C)** AWS Wavelength
- **D)** Amazon CloudFront

<details>
<summary>Ver resposta</summary>

**Resposta: B**

O **Outposts** instala racks ou servidores da AWS **no datacenter do cliente**. Local Zones ficam em cidades e são operadas pela AWS; Wavelength fica dentro de redes 5G de operadoras; CloudFront é uma CDN.

</details>

### Questão 5

<sub>Domínio 3 · tópico [3.3](../../docs/03-tecnologia-e-servicos/03-ec2.md)</sub>

Uma empresa vai executar um banco de dados em memória de alto desempenho no Amazon EC2. Qual família de instâncias é a mais indicada?

- **A)** Uso geral com desempenho expansível (por exemplo, T)
- **B)** Computação acelerada (por exemplo, P ou G)
- **C)** Otimizada para memória (por exemplo, R ou X)
- **D)** Otimizada para computação (por exemplo, C)

<details>
<summary>Ver resposta</summary>

**Resposta: C**

Bancos em memória e análises em tempo real usam instâncias **otimizadas para memória** (R, X). C é para uso intenso de CPU; T é para cargas leves com picos; P e G são para GPU/ML.

</details>

### Questão 6

<sub>Domínio 3 · tópico [3.3](../../docs/03-tecnologia-e-servicos/03-ec2.md)</sub>

Uma aplicação grava arquivos temporários de cache no instance store de uma instância EC2. O que acontece com esses dados quando a instância é PARADA (stop)?

- **A)** Os dados são preservados e ficam disponíveis quando a instância voltar
- **B)** Os dados são copiados automaticamente para um snapshot do EBS
- **C)** Os dados são movidos automaticamente para o Amazon S3
- **D)** Os dados são perdidos

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **instance store** é armazenamento local **efêmero**: os dados se perdem ao parar, hibernar ou encerrar a instância (sobrevivem só ao reboot). Para persistência, use EBS.

</details>

### Questão 7

<sub>Domínio 3 · tópico [3.4](../../docs/03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md)</sub>

Uma aplicação de microsserviços precisa enviar requisições com caminho /api para um grupo de contêineres e /imagens para outro, usando o mesmo endereço. Qual load balancer deve ser usado?

- **A)** Gateway Load Balancer
- **B)** Classic Load Balancer
- **C)** Network Load Balancer
- **D)** Application Load Balancer

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **ALB** opera na camada 7 e roteia por caminho, host e cabeçalho. O NLB opera na camada 4 (TCP/UDP); o GWLB encaminha tráfego para appliances de segurança; o Classic é legado e não recomendado.

</details>

### Questão 8

<sub>Domínio 3 · tópico [3.5](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)</sub>

Um processamento de vídeo leva cerca de 2 horas por arquivo. A empresa quer executá-lo em contêineres, sem provisionar nem gerenciar servidores. Qual opção é a mais adequada?

- **A)** Amazon ECS com AWS Fargate
- **B)** Amazon Lightsail
- **C)** Amazon EC2 com Auto Scaling
- **D)** AWS Lambda

<details>
<summary>Ver resposta</summary>

**Resposta: A**

O **Fargate** executa contêineres sem servidores e sem limite de duração. O Lambda tem limite de **15 minutos** por execução; EC2 e Lightsail exigem gerenciar servidores.

</details>

### Questão 9

<sub>Domínio 3 · tópico [3.5](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)</sub>

Uma empresa já usa Kubernetes on-premises e quer migrar seus manifestos e ferramentas para um serviço gerenciado na AWS, com o plano de controle operado pela AWS. Qual serviço atende melhor?

- **A)** Amazon ECS
- **B)** Amazon EKS
- **C)** AWS Batch
- **D)** AWS Elastic Beanstalk

<details>
<summary>Ver resposta</summary>

**Resposta: B**

O **EKS** é Kubernetes gerenciado e preserva manifestos e ferramentas do ecossistema. O ECS é o orquestrador próprio da AWS (não Kubernetes); Beanstalk é PaaS para aplicações; Batch é para jobs em lote.

</details>

### Questão 10

<sub>Domínio 3 · tópico [3.6](../../docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md)</sub>

A dona de uma pequena escola de idiomas, com pouca experiência em nuvem, quer publicar um blog em WordPress e saber de antemão quanto vai pagar por mês. Qual serviço atende melhor?

- **A)** AWS Batch
- **B)** Amazon EC2 com Auto Scaling e Elastic Load Balancing
- **C)** AWS Elastic Beanstalk
- **D)** Amazon Lightsail

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **Lightsail** é o jeito mais simples de começar na AWS: oferece imagens prontas, como WordPress, e planos com preço mensal baixo e previsível que reúnem processador, memória, armazenamento e transferência. EC2 com Auto Scaling e balanceador exige montar várias peças cobradas por uso; o Elastic Beanstalk implanta código próprio e cobra os recursos que cria; o Batch roda processamento em lote.

</details>

### Questão 11

<sub>Domínio 3 · tópico [3.6](../../docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md)</sub>

Uma equipe de desenvolvimento quer enviar o código da sua aplicação web e deixar a AWS provisionar servidores, balanceamento de carga e escalabilidade, pagando apenas pelos recursos usados. Qual serviço atende a esse requisito?

- **A)** AWS Elastic Beanstalk
- **B)** AWS Outposts
- **C)** Amazon Lightsail
- **D)** AWS Batch

<details>
<summary>Ver resposta</summary>

**Resposta: A**

O **Elastic Beanstalk** recebe o código e provisiona o ambiente (instâncias, balanceador, Auto Scaling), e **não tem cobrança adicional**: paga-se só pelos recursos criados. O Lightsail oferece planos simples de preço fixo, sem partir do código da equipe; o Outposts leva a infraestrutura da AWS ao datacenter do cliente; o Batch roda trabalhos em lote.

</details>

### Questão 12

<sub>Domínio 3 · tópico [3.6](../../docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md)</sub>

Um hospital precisa processar dados localmente, com baixa latência, no seu próprio datacenter, mas quer usar os mesmos serviços, APIs e ferramentas que usa nas Regiões da AWS. Qual serviço atende a essa necessidade?

- **A)** AWS Elastic Beanstalk
- **B)** Amazon Lightsail
- **C)** AWS Batch
- **D)** AWS Outposts

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **Outposts** é um serviço totalmente gerenciado que leva a infraestrutura, os serviços, as APIs e as ferramentas da AWS ao local do cliente, para baixa latência e processamento local. Elastic Beanstalk, Lightsail e Batch rodam nas Regiões da AWS, não no datacenter do cliente.

</details>

### Questão 13

<sub>Domínio 3 · tópico [3.7](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)</sub>

Um jogo online precisa armazenar o perfil e o progresso de milhões de jogadores com latência de milissegundos de um dígito, em qualquer escala, sem gerenciar servidores. Qual banco de dados atende melhor?

- **A)** Amazon Neptune
- **B)** Amazon Redshift
- **C)** Amazon DynamoDB
- **D)** Amazon RDS for PostgreSQL

<details>
<summary>Ver resposta</summary>

**Resposta: C**

O **DynamoDB** é NoSQL chave-valor serverless, com latência de milissegundos de um dígito em qualquer escala. RDS é relacional e exige dimensionar instâncias; Redshift é data warehouse (OLAP); Neptune é banco de grafos.

</details>

### Questão 14

<sub>Domínio 3 · tópico [3.7](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)</sub>

Uma empresa quer que seu banco Amazon RDS continue disponível mesmo se uma zona de disponibilidade inteira falhar, com failover automático. Qual recurso deve ser habilitado?

- **A)** RDS Multi-AZ
- **B)** Snapshots manuais diários
- **C)** Amazon ElastiCache na frente do banco
- **D)** Read replicas na mesma região

<details>
<summary>Ver resposta</summary>

**Resposta: A**

O **Multi-AZ** mantém um standby síncrono em outra AZ com **failover automático** — o objetivo é disponibilidade. Read replicas escalam leitura; snapshots exigem restauração manual; ElastiCache é cache, não alta disponibilidade do banco.

</details>

### Questão 15

<sub>Domínio 3 · tópico [3.7](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)</sub>

O time de BI precisa executar consultas SQL analíticas complexas sobre petabytes de dados históricos de vendas, alimentando dashboards. Qual serviço é o mais indicado?

- **A)** Amazon Redshift
- **B)** Amazon RDS for MySQL
- **C)** Amazon ElastiCache
- **D)** Amazon DynamoDB

<details>
<summary>Ver resposta</summary>

**Resposta: A**

O **Redshift** é o data warehouse colunar para análises (OLAP) em grande escala. RDS é otimizado para transações (OLTP); DynamoDB é NoSQL chave-valor; ElastiCache é cache em memória.

</details>

### Questão 16

<sub>Domínio 3 · tópico [3.8](../../docs/03-tecnologia-e-servicos/08-s3.md)</sub>

Uma empresa armazena milhões de objetos no Amazon S3 com padrão de acesso imprevisível: alguns são lidos com frequência e outros ficam meses sem acesso. Qual classe de armazenamento otimiza o custo automaticamente sem afetar o desempenho?

- **A)** S3 Standard
- **B)** S3 One Zone-IA
- **C)** S3 Intelligent-Tiering
- **D)** S3 Glacier Deep Archive

<details>
<summary>Ver resposta</summary>

**Resposta: C**

O **Intelligent-Tiering** move os objetos entre camadas automaticamente conforme o acesso, sem taxa de recuperação nas camadas automáticas (cobra só uma pequena taxa de monitoramento por objeto). Standard não otimiza custo; One Zone-IA cobra recuperação e guarda em uma AZ; Deep Archive tem recuperação de horas.

</details>

### Questão 17

<sub>Domínio 3 · tópico [3.8](../../docs/03-tecnologia-e-servicos/08-s3.md)</sub>

Por exigência regulatória, uma empresa precisa guardar registros por 7 anos. Eles quase nunca são lidos e uma recuperação de até 48 horas é aceitável. Qual é a opção de MENOR custo?

- **A)** S3 Standard-IA
- **B)** S3 Glacier Instant Retrieval
- **C)** S3 Intelligent-Tiering
- **D)** S3 Glacier Deep Archive

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **Glacier Deep Archive** é a classe mais barata, para retenção de longo prazo, com recuperação em até 12 h (padrão) ou 48 h (bulk). Instant Retrieval e Standard-IA custam mais por oferecerem acesso em milissegundos.

</details>

### Questão 18

<sub>Domínio 3 · tópico [3.9](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)</sub>

Dezenas de instâncias Linux distribuídas em várias zonas de disponibilidade precisam ler e gravar os mesmos arquivos ao mesmo tempo. Qual serviço de armazenamento atende a esse requisito?

- **A)** Amazon FSx for Windows File Server
- **B)** Amazon EBS
- **C)** Instance store
- **D)** Amazon EFS

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **EFS** é um sistema de arquivos NFS compartilhado entre muitas instâncias Linux em várias AZs. O EBS fica preso a uma AZ (Multi-Attach só io1/io2, mesma AZ); instance store é local e efêmero; FSx for Windows é SMB para Windows.

</details>

### Questão 19

<sub>Domínio 3 · tópico [3.9](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)</sub>

Uma empresa quer acabar com o backup em fitas físicas, mas sem trocar o software de backup que já usa. Qual solução atende a esse requisito?

- **A)** Amazon EFS
- **B)** AWS Snowball Edge
- **C)** AWS DataSync
- **D)** AWS Storage Gateway com Tape Gateway

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **Tape Gateway** apresenta fitas virtuais (VTL) ao software de backup e arquiva os dados no S3 Glacier. DataSync transfere arquivos; EFS é sistema de arquivos; Snowball Edge é transferência física pontual.

</details>

### Questão 20

<sub>Domínio 3 · tópico [3.10](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)</sub>

Instâncias EC2 em uma subnet privada precisam baixar atualizações de segurança da internet, mas não podem receber conexões iniciadas de fora. O que deve ser configurado?

- **A)** Um VPC peering com a VPC padrão
- **B)** Um gateway VPC endpoint para o Amazon S3
- **C)** Um Internet Gateway com rota direta a partir da subnet privada
- **D)** Um NAT Gateway em uma subnet pública, com rota a partir da subnet privada

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **NAT Gateway** permite apenas a **saída** para a internet a partir de subnets privadas. Uma rota direta para o Internet Gateway tornaria a subnet pública; o gateway endpoint só acessa S3/DynamoDB; peering liga VPCs, não dá acesso à internet.

</details>

### Questão 21

<sub>Domínio 3 · tópico [3.10](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)</sub>

Uma empresa transfere grandes volumes de dados todos os dias entre o datacenter e a AWS e precisa de uma conexão privada, dedicada, que não passe pela internet e tenha desempenho consistente. Qual serviço atende a esse requisito?

- **A)** AWS Client VPN
- **B)** AWS Direct Connect
- **C)** Amazon CloudFront
- **D)** AWS Site-to-Site VPN

<details>
<summary>Ver resposta</summary>

**Resposta: B**

O **Direct Connect** é um link físico dedicado e privado, com banda estável. A Site-to-Site VPN passa pela internet (criptografada); a Client VPN é para usuários remotos; CloudFront é CDN.

</details>

### Questão 22

<sub>Domínio 3 · tópico [3.10](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)</sub>

Uma empresa de mídia quer reduzir a latência na entrega de vídeos e imagens para usuários no mundo todo, fazendo cache do conteúdo perto deles. Qual serviço deve ser usado?

- **A)** AWS Global Accelerator
- **B)** AWS Direct Connect
- **C)** Amazon CloudFront
- **D)** Amazon Route 53

<details>
<summary>Ver resposta</summary>

**Resposta: C**

O **CloudFront** é a CDN da AWS e faz **cache** nas edge locations. O Global Accelerator otimiza o caminho de rede TCP/UDP, mas **não faz cache**; o Route 53 é DNS; o Direct Connect liga datacenters à AWS.

</details>

### Questão 23

<sub>Domínio 3 · tópico [3.11](../../docs/03-tecnologia-e-servicos/11-analytics.md)</sub>

Um analista quer consultar com SQL padrão os logs armazenados em um bucket S3, sem provisionar servidores e pagando apenas pelos dados lidos em cada consulta. Qual serviço atende a esse requisito?

- **A)** Amazon RDS
- **B)** Amazon Redshift
- **C)** Amazon Athena
- **D)** Amazon EMR

<details>
<summary>Ver resposta</summary>

**Resposta: C**

O **Athena** executa SQL serverless direto no S3 e cobra por dados escaneados. Redshift exige carregar dados num data warehouse; EMR exige clusters de big data; RDS é banco transacional.

</details>

### Questão 24

<sub>Domínio 3 · tópico [3.12](../../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)</sub>

Uma seguradora recebe milhares de formulários escaneados e quer extrair automaticamente o texto, os campos (chave-valor) e as tabelas. Qual serviço deve ser usado?

- **A)** Amazon Comprehend
- **B)** Amazon Transcribe
- **C)** Amazon Rekognition
- **D)** Amazon Textract

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **Textract** extrai texto, formulários e tabelas de documentos digitalizados. O Rekognition analisa imagens e vídeos (rostos, objetos); o Comprehend analisa texto já extraído (sentimento, entidades); o Transcribe converte fala em texto.

</details>

### Questão 25

<sub>Domínio 3 · tópico [3.13](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)</sub>

Quando um pedido é criado, a mesma mensagem precisa ser entregue a três sistemas diferentes e também enviada por e-mail ao time financeiro. Qual serviço deve receber a publicação do evento?

- **A)** AWS Step Functions
- **B)** Amazon SQS
- **C)** Amazon Kinesis Data Streams
- **D)** Amazon SNS

<details>
<summary>Ver resposta</summary>

**Resposta: D**

O **SNS** é pub/sub: publica num tópico e empurra a mensagem para vários assinantes (filas SQS, Lambda, HTTP, e-mail). Uma fila SQS é consumida por um processador; Step Functions orquestra etapas; Kinesis é para streaming em tempo real.

</details>

### Questão 26

<sub>Domínio 3 · tópico [3.17](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md)</sub>

Uma empresa quer migrar um banco Oracle on-premises para o Amazon Aurora PostgreSQL, mantendo o banco de origem em operação durante a migração. Quais serviços devem ser usados?

- **A)** AWS DataSync e AWS Transfer Family
- **B)** AWS Schema Conversion Tool (SCT) e AWS Database Migration Service (DMS)
- **C)** AWS Snowball Edge e Amazon S3
- **D)** Somente o AWS Application Migration Service

<details>
<summary>Ver resposta</summary>

**Resposta: B**

Migração **heterogênea**: o **SCT** converte o schema e o código do Oracle para PostgreSQL, e o **DMS** move os dados com replicação contínua (CDC). O Application Migration Service migra servidores inteiros; DataSync, Transfer Family e Snowball transferem arquivos.

</details>
