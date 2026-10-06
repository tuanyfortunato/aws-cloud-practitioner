# 🃏 Flashcards — Domínio 3 — Tecnologia e Serviços de Nuvem

Clique na pergunta para ver a resposta. Gerado a partir das *Perguntas típicas* de cada tópico (`python3 scripts/gerar_docs.py`).

**Total:** 94 cards


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
<summary>O que é um container e que problema ele resolve?</summary>

É um pacote com o código da aplicação e todos os arquivos e bibliotecas de que ela precisa; resolve o problema de a aplicação funcionar num ambiente e não em outro.
</details>

<details>
<summary>Qual é a diferença entre ECS e EKS?</summary>

Os dois orquestram containers; o ECS é o orquestrador da própria AWS, e o EKS é Kubernetes gerenciado.
</details>

<details>
<summary>O que é o AWS Fargate?</summary>

É um mecanismo de computação serverless para containers, usado com ECS ou EKS: você define CPU e memória, e não gerencia servidores.
</details>

<details>
<summary>Como o AWS Lambda é cobrado?</summary>

Pelo número de pedidos e pela duração das execuções em GB-segundo; quando a função não roda, não há cobrança de computação.
</details>

<details>
<summary>Uma tarefa leva duas horas para terminar. Ela serve para uma função Lambda?</summary>

Não, porque uma função Lambda roda por até 15 minutos em cada execução; a tarefa cabe melhor em containers com Fargate, no AWS Batch ou no EC2.
</details>


## [3.6 Outros serviços de computação](../docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md)

<details>
<summary>O que o AWS Elastic Beanstalk faz com o código que você envia?</summary>

Cria e configura os recursos para rodá-lo: instâncias do EC2 (ou um cluster do EKS), balanceamento de carga, monitoramento de saúde e escalonamento.
</details>

<details>
<summary>Quanto custa o AWS Elastic Beanstalk?</summary>

Não há cobrança adicional pelo serviço; você paga os recursos da AWS que a aplicação consome.
</details>

<details>
<summary>Para quem o Amazon Lightsail foi pensado?</summary>

Para quem quer começar de forma simples, como desenvolvedores individuais, projetos pessoais e iniciantes, com planos de preço baixo e previsível.
</details>

<details>
<summary>Que tipo de trabalho o AWS Batch executa?</summary>

Cargas de processamento em lote de qualquer escala, provisionando automaticamente a capacidade de computação para as tarefas enviadas.
</details>

<details>
<summary>Qual é a diferença entre o Elastic Beanstalk e o Lambda?</summary>

O Elastic Beanstalk cria instâncias e outros recursos que ficam ligados e são cobrados; o Lambda é serverless e cobra só quando a função roda.
</details>


## [3.7 Bancos de dados](../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)

<details>
<summary>Quais tarefas a AWS assume quando o banco sai do EC2 e vai para o RDS?</summary>

Instalação e patches do sistema operacional e do software do banco, backups, alta disponibilidade e escalonamento; o cliente continua cuidando da aplicação e das consultas.
</details>

<details>
<summary>Qual é a diferença entre Multi-AZ e réplica de leitura no RDS?</summary>

Multi-AZ mantém uma cópia síncrona em outra zona de disponibilidade para disponibilidade; a réplica de leitura é uma cópia assíncrona, só de leitura, para melhorar o desempenho de leitura.
</details>

<details>
<summary>Quando escolher o DynamoDB em vez do RDS?</summary>

Quando os dados são chave-valor ou documento e precisam de escala enorme com milissegundos de resposta, sem servidor para gerenciar.
</details>

<details>
<summary>Para que serve o Amazon ElastiCache?</summary>

Para guardar em memória os dados mais pedidos e responder sem consultar o banco, o que acelera a aplicação e alivia o banco principal.
</details>

<details>
<summary>Uma empresa vai migrar um banco Oracle para o Aurora PostgreSQL. Que ferramentas usar?</summary>

O AWS SCT (ou o DMS Schema Conversion) para converter o esquema, e o AWS DMS para migrar os dados.
</details>


## [3.8 Amazon S3 — armazenamento de objetos](../docs/03-tecnologia-e-servicos/08-s3.md)

<details>
<summary>O que identifica um objeto no S3?</summary>

O bucket onde ele está e a sua chave, o nome único do objeto dentro do bucket (e a versão, quando o versionamento está ligado).
</details>

<details>
<summary>Qual é a diferença entre durabilidade e disponibilidade no S3?</summary>

Durabilidade é a chance de o dado não se perder (11 noves em todas as classes da tabela desta aula); disponibilidade é a chance de ele estar acessível quando pedido, e varia por classe.
</details>

<details>
<summary>Quando usar o S3 Intelligent-Tiering?</summary>

Quando o padrão de acesso aos dados é desconhecido ou muda, porque ele move cada objeto para a camada mais barata sozinho, sem taxa de recuperação.
</details>

<details>
<summary>O que uma política de ciclo de vida do S3 faz?</summary>

Aplica regras automáticas a grupos de objetos: transição para outra classe depois de um tempo e expiração (exclusão) quando o prazo termina.
</details>

<details>
<summary>Qual classe tem o armazenamento mais barato, e qual é o preço dessa economia?</summary>

O S3 Glacier Deep Archive; em troca, o objeto precisa ser restaurado antes da leitura, o que leva horas, e há mínimo de 180 dias de cobrança.
</details>


## [3.9 Outros serviços de armazenamento](../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)

<details>
<summary>Qual é a diferença entre um volume EBS e o instance store?</summary>

O volume EBS é persistente e existe independentemente da instância, numa zona de disponibilidade; o instance store é um disco físico do servidor, cujos dados se perdem quando a instância é parada ou encerrada.
</details>

<details>
<summary>Quando usar o EFS em vez do EBS?</summary>

Quando várias instâncias Linux precisam acessar os mesmos arquivos ao mesmo tempo; o EFS é um sistema de arquivos compartilhado (NFS) que cresce e encolhe sozinho.
</details>

<details>
<summary>O que o Amazon FSx oferece?</summary>

Sistemas de arquivos conhecidos totalmente gerenciados: Windows File Server, Lustre, NetApp ONTAP e OpenZFS.
</details>

<details>
<summary>Para que serve o AWS Storage Gateway?</summary>

Para ligar o ambiente local do cliente ao armazenamento da AWS, guardando os dados na nuvem e mantendo um cache local para acesso rápido.
</details>

<details>
<summary>Qual é a vantagem do AWS Backup?</summary>

Centralizar e automatizar os backups de vários serviços com planos de backup, em vez de configurar e conferir serviço por serviço.
</details>


## [3.10 Rede e entrega de conteúdo](../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)

<details>
<summary>O que torna uma sub-rede pública?</summary>

Uma rota direta para um internet gateway na tabela de rotas da sub-rede; sem essa rota, a sub-rede é privada.
</details>

<details>
<summary>Para que serve o NAT gateway?</summary>

Para que instâncias em sub-redes privadas iniciem conexões com serviços fora da VPC, como baixar atualizações, sem que serviços de fora possam iniciar conexões com elas.
</details>

<details>
<summary>Quando usar o Transit Gateway em vez de VPC peering?</summary>

Quando há muitas VPCs e redes locais para interligar; o Transit Gateway é um hub central, enquanto o peering liga só duas VPCs e não é transitivo.
</details>

<details>
<summary>Qual é a diferença entre Site-to-Site VPN e Direct Connect?</summary>

A Site-to-Site VPN é uma conexão criptografada (IPsec) que passa pela internet; o Direct Connect é uma conexão dedicada por fibra até um local do Direct Connect, sem passar pelos provedores de internet, com desempenho mais consistente.
</details>

<details>
<summary>Quais são as três funções do Amazon Route 53?</summary>

Registrar domínios, rotear o tráfego do nome do domínio para os recursos e verificar a saúde desses recursos.
</details>


## [3.11 Analytics](../docs/03-tecnologia-e-servicos/11-analytics.md)

<details>
<summary>Qual é a diferença entre data lake e data warehouse?</summary>

O data lake guarda dados estruturados e não estruturados como chegaram, em qualquer escala; o data warehouse guarda dados relacionais organizados antes, otimizados para consultas analíticas.
</details>

<details>
<summary>Como o Amazon Athena é cobrado, e como reduzir esse custo?</summary>

Pela quantidade de dados lidos em cada consulta; comprimir, particionar e usar formatos colunares reduz o que o Athena lê.
</details>

<details>
<summary>O que o AWS Glue faz?</summary>

Descobre, prepara e integra dados de muitas fontes, roda pipelines de ETL sem servidor e mantém um catálogo central de dados.
</details>

<details>
<summary>Quando usar o Amazon Kinesis?</summary>

Quando os dados chegam em fluxo contínuo e precisam ser coletados e processados em tempo real, como cliques ou leituras de sensores.
</details>

<details>
<summary>Que serviço cria painéis de BI na AWS?</summary>

O Amazon Quick Sight, que se conecta às fontes de dados e cria painéis interativos.
</details>


## [3.12 IA e machine learning](../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)

<details>
<summary>Qual é a relação entre IA, machine learning e IA generativa?</summary>

IA é o termo amplo; machine learning é um tipo de IA que aprende padrões a partir de dados; IA generativa é um tipo de IA que cria conteúdo novo usando modelos de fundação.
</details>

<details>
<summary>Quando usar o SageMaker AI em vez de um serviço de IA pronto?</summary>

Quando o problema exige um modelo próprio, treinado com os dados da empresa, que nenhum serviço pronto resolve.
</details>

<details>
<summary>Qual é a diferença entre Amazon Polly e Amazon Transcribe?</summary>

O Polly converte texto em fala; o Transcribe converte fala em texto.
</details>

<details>
<summary>Qual é a diferença entre Amazon Textract e Amazon Rekognition?</summary>

O Textract extrai texto, formulários e tabelas de documentos; o Rekognition analisa imagens e vídeos para detectar rostos, objetos e conteúdo impróprio.
</details>

<details>
<summary>Para que serve o Amazon Lex?</summary>

Para criar interfaces conversacionais, como chatbots, por voz e texto, com reconhecimento de fala e compreensão de linguagem natural.
</details>


## [3.13 Integração de aplicações](../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)

<details>
<summary>Para que serve o Amazon SQS?</summary>

Para desacoplar componentes com uma fila: o produtor envia mensagens, e o consumidor as busca e processa no seu ritmo, o que absorve picos e falhas.
</details>

<details>
<summary>Qual é a diferença entre uma fila padrão e uma fila FIFO no SQS?</summary>

A fila padrão tem vazão quase ilimitada, mas pode repetir mensagens e entregá-las fora de ordem; a FIFO mantém a ordem dentro de cada grupo e processa cada mensagem uma vez.
</details>

<details>
<summary>Qual é a diferença entre SQS e SNS?</summary>

No SQS, a mensagem espera numa fila até um consumidor buscá-la; no SNS, a mensagem publicada num tópico é empurrada na hora para todos os assinantes.
</details>

<details>
<summary>Quando usar o Amazon EventBridge?</summary>

Para ligar componentes por eventos: receber eventos de aplicações, de serviços da AWS e de softwares de terceiros e entregá-los aos destinos certos, ou para agendar tarefas com o EventBridge Scheduler.
</details>

<details>
<summary>O que o AWS Step Functions faz?</summary>

Coordena fluxos de trabalho com várias etapas, chamando serviços como o Lambda, com novas tentativas e caminhos alternativos em caso de erro.
</details>


## [3.14 Aplicações de negócio, usuário final, front-end e IoT](../docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md)

<details>
<summary>Para que serve o Amazon Connect?</summary>

É a central de atendimento na nuvem: clientes entram em contato por voz, chat ou SMS, e atendentes resolvem os casos, pagando-se pelo uso.
</details>

<details>
<summary>Qual é a diferença entre Amazon SES e Amazon SNS para enviar e-mails?</summary>

O SES é o serviço de e-mail completo, para mensagens transacionais e de marketing enviadas da aplicação; o SNS manda notificações simples a quem assinou um tópico.
</details>

<details>
<summary>Qual é a diferença entre WorkSpaces e WorkSpaces Applications (AppStream 2.0)?</summary>

O WorkSpaces entrega um desktop virtual inteiro; o WorkSpaces Applications faz streaming de programas de desktop específicos para o navegador ou um cliente.
</details>

<details>
<summary>O que o AWS Amplify oferece?</summary>

Ferramentas para criar, implantar e hospedar aplicações web e mobile full-stack, sem exigir conhecimento de nuvem.
</details>

<details>
<summary>Para que serve o AWS IoT Core?</summary>

Para conectar dispositivos IoT à AWS com segurança, nos dois sentidos, e gerenciar frotas de dispositivos sem provisionar servidores.
</details>


## [3.15 Ferramentas de desenvolvimento](../docs/03-tecnologia-e-servicos/15-ferramentas-de-desenvolvimento.md)

<details>
<summary>O que é integração contínua?</summary>

É a prática de juntar as mudanças de código num repositório central com frequência, e cada junção dispara automaticamente a compilação e os testes.
</details>

<details>
<summary>Para que serve o AWS CodeBuild?</summary>

Para compilar o código-fonte, rodar os testes e produzir pacotes prontos para implantar, sem servidores de build para gerenciar.
</details>

<details>
<summary>Para que serve o AWS CodePipeline?</summary>

Para modelar, visualizar e automatizar as etapas de lançamento de software, da mudança no repositório até a implantação.
</details>

<details>
<summary>O que o AWS X-Ray mostra?</summary>

O caminho de cada requisição pela aplicação, incluindo as chamadas a outros serviços, microsserviços e bancos, para encontrar gargalos e erros.
</details>

<details>
<summary>Qual é a diferença entre o CloudWatch e o X-Ray?</summary>

O CloudWatch coleta métricas e logs de cada recurso; o X-Ray segue uma requisição de ponta a ponta pelas várias peças da aplicação.
</details>


## [3.16 Gestão e governança](../docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md)

<details>
<summary>O que o AWS Systems Manager permite fazer?</summary>

Operar de forma centralizada muitas máquinas na AWS e fora dela: aplicar patches em escala, rodar comandos remotamente, conectar-se sem abrir portas de entrada e guardar configurações.
</details>

<details>
<summary>Quais são as duas visões do AWS Health Dashboard?</summary>

A saúde dos serviços, página pública com os eventos da AWS em todas as Regiões, e a saúde da conta, com os eventos que podem afetar as suas contas e recursos.
</details>

<details>
<summary>O que fazer quando a conta atinge o limite de um recurso?</summary>

Verificar a cota no Service Quotas e, se ela for ajustável, pedir o aumento por lá.
</details>

<details>
<summary>Para que serve o AWS Compute Optimizer?</summary>

Para analisar a configuração e o uso dos recursos e recomendar o tamanho certo, além de apontar recursos ociosos, reduzindo custo e melhorando desempenho.
</details>

<details>
<summary>O que o CloudFormation StackSets acrescenta ao CloudFormation?</summary>

A possibilidade de criar, atualizar ou apagar pilhas em várias contas e Regiões numa única operação, a partir do mesmo modelo.
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
