# AWS Lambda

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Você precisa executar uma tarefa quando algo acontece, mas não quer manter uma máquina inteira só para esperar por esse acontecimento.

**Como este serviço ajuda?** No Lambda, você entrega uma função, isto é, um trecho de programa. Um evento ou uma chamada dispara sua execução, e a AWS administra a infraestrutura usada para executá-la.

**Exemplo do dia a dia:** Quando uma pessoa envia uma foto, uma função pode gerar uma miniatura. Você escreve o código dessa transformação e configura o que vai acioná-lo.

**O que ele não resolve sozinho?** Lambda não é uma máquina em que você entra para instalar qualquer programa e deixá-lo rodando indefinidamente. Há limites de execução, e dados que precisam durar devem ser guardados em armazenamento apropriado.

**Primeiras palavras para entender:**

- **Evento:** acontecimento que dispara uma ação.
- **Função:** código executado para uma tarefa.
- **Serverless:** a AWS administra os servidores; eles continuam existindo.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Computação serverless · **Domínio:** 1 (serverless) e 3 · **Escopo:** Regional · **Tópico do guia:** [3.5 Containers e serverless](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)
>
> **Em uma frase:** executa código em resposta a eventos sem você administrar servidores; o modelo base cobra requisições e duração.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **memória:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.
- **evento:** Informação sobre algo que aconteceu. Uma regra pode encaminhar o evento; outro componente realiza a ação de negócio.

**Passo 1.** Escreva uma função que realize uma tarefa delimitada e defina como ela será chamada.

**Passo 2.** Configure os recursos, os acessos e a integração que fornece a entrada. A AWS inicia a execução quando recebe a chamada ou o evento.

**Passo 3.** Guarde resultados que precisam durar em um recurso apropriado e trate falhas. Não dependa de execução infinita nem de memória preservada entre chamadas.

## 2. Recursos e opções, com significado

### Para que serve

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **ETL:** Extrair dados de uma fonte, transformá-los e carregá-los num destino. A regra de transformação deve ser definida de acordo com o significado dos dados.

Processar arquivos assim que chegam ao S3 (miniaturas, validação, ETL leve).

**Antes de ler este trecho:**

- **API Gateway:** API Gateway ajuda a publicar e administrar APIs.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.

Back-ends de APIs (com [API Gateway](../redes/api-gateway.md) ou function URLs).

**Antes de ler este trecho:**

- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **SQS:** SQS guarda mensagens numa fila até que consumidores as recebam e processem.

Consumir filas e streams (SQS, Kinesis, DynamoDB Streams).

**Antes de ler este trecho:**

- **EventBridge:** EventBridge recebe eventos e usa regras para encaminhá-los a destinos compatíveis.

Tarefas agendadas (EventBridge Scheduler), automação de operações, chatbots.

### Conceitos e componentes

**Função**

**Antes de ler este trecho:**

- **role:** Papel que fornece permissões a uma sessão que o assume. O termo função IAM não significa um trecho de código como uma função Lambda.
- **timeout:** Limite de espera ou duração. Ao excedê-lo, uma operação pode falhar ou exigir tratamento; não presuma que nada aconteceu antes da interrupção.
- **runtime:** Ambiente que executa código de uma linguagem ou plataforma. Compatibilidade de bibliotecas e versões deve ser avaliada.

**O que é:** Código + configuração (runtime, memória, timeout, role).

**Runtime**

**Antes de ler este trecho:**

- **GB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.
- **imagem:** Pacote ou modelo usado para iniciar um ambiente. Em EC2, a AMI é uma imagem de máquina; em containers, a imagem serve para iniciar containers.

**O que é:** Python, Node.js, Java, .NET, Ruby, **custom runtime** (`provided.al2023`) — Go e Rust usam o custom runtime; também **imagem de contêiner** (até 10 GB).

**Trigger / event source**

**Antes de ler este trecho:**

- **Cognito:** Cognito oferece recursos de identidade para usuários de aplicações.
- **SNS:** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis.
- **ALB:** Modalidades de balanceador com focos diferentes: aplicação, transporte de rede e integração de equipamentos virtuais. Os protocolos e casos de uso determinam a escolha.
- **IoT:** Dispositivos físicos conectados que enviam informações ou recebem comandos. Conexão não substitui autenticação, software e análise dos dados.

**O que é:** O que invoca: S3, API Gateway, ALB, SQS, SNS, EventBridge, DynamoDB/Kinesis Streams, Cognito, IoT…

**Execution role**

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.

**O que é:** IAM role que dá permissões à função (ex.: gravar no DynamoDB).

**Resource-based policy**

**Antes de ler este trecho:**

- **policy:** Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.

**O que é:** Quem pode invocar a função (ex.: permitir o S3 ou outra conta).

**Invocação**

**Antes de ler este trecho:**

- **URL:** Endereço usado para acessar um recurso. Uma URL pode incluir domínio, caminho e parâmetros; possuir o endereço não significa ter autorização.
- **DLQ:** Fila separada para mensagens que atingiram condições configuradas de falha. Ajuda a isolar e investigar o problema; não corrige a mensagem automaticamente.

**O que é:** **Síncrona** (API Gateway, function URL), **assíncrona** (S3, SNS, EventBridge — com retentativas e *destinations*/DLQ) ou **event source mapping** (polling de SQS/Kinesis/DynamoDB).

**Layers**

**O que é:** Pacotes de bibliotecas compartilhados entre funções (até 5).

**Versões e aliases**

**O que é:** Versões imutáveis + aliases (`prod`, `dev`) que apontam para elas; permitem *canary*/peso.

**Cold start**

**Antes de ler este trecho:**

- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.

**O que é:** Latência extra ao criar um novo ambiente de execução.

### Configurações e opções importantes

**Memória**

**Antes de ler este trecho:**

- **CPU:** CPU é o processador que executa instruções. vCPU é a unidade de processamento virtual apresentada ao ambiente. Mais processamento não resolve automaticamente falta de memória ou de velocidade do disco.

**O que faz:** 128 MB – 10.240 MB; a **CPU é proporcional à memória**

**Timeout**

**O que faz:** até **900 s (15 min)**

**Armazenamento efêmero /tmp**

**O que faz:** 512 MB – 10.240 MB

**Variáveis de ambiente**

**Antes de ler este trecho:**

- **KMS:** Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.

**O que faz:** Configuração (criptografadas com KMS)

**Arquitetura**

**Antes de ler este trecho:**

- **Graviton:** Família de processadores AWS baseada em arquitetura ARM. A aplicação e sua imagem precisam ser compatíveis com essa arquitetura.

**O que faz:** x86_64 ou **arm64 (Graviton)** — mais barato por GB-s

**Concorrência reservada**

**O que faz:** Garante (e limita) concorrência para uma função

**Concorrência provisionada**

**O que faz:** Ambientes pré-aquecidos — elimina cold start (pago)

**SnapStart**

**Antes de ler este trecho:**

- **snapshot:** Cópia de estado de um recurso em determinado momento, conforme o serviço. Restauração pode criar um novo recurso; não presuma uma máquina pronta e instantânea.

**O que faz:** Reduz cold start (Java, Python, .NET) restaurando um snapshot

**Acesso à VPC**

**Antes de ler este trecho:**

- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **ElastiCache:** ElastiCache fornece armazenamento em memória para manter dados próximos da aplicação e acelerar acessos, conforme o mecanismo e a configuração.
- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.

**O que faz:** Função acessa recursos privados (RDS, ElastiCache)

**Function URL**

**Antes de ler este trecho:**

- **HTTPS:** HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.
- **endpoint:** Ponto de acesso a um serviço ou componente. Pode ser um endereço de API ou um recurso de conectividade; identifique qual sentido a seção usa.

**O que faz:** Endpoint HTTPS dedicado, sem API Gateway

**Destinations / DLQ**

**O que faz:** Para onde vão os resultados ou falhas de invocações assíncronas

### Limites e números

📌 Timeout máximo **15 min** · memória **10.240 MB** · CPU proporcional.

**Antes de ler este trecho:**

- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.

🧊 Concorrência padrão de 1.000 por região (ajustável), pacote zip 50 MB (250 MB descompactado), 5 layers, payload síncrono de 6 MB.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.

Lambda não é uma máquina em que você entra para instalar qualquer programa e deixá-lo rodando indefinidamente. Há limites de execução, e dados que precisam durar devem ser guardados em armazenamento apropriado.

### ⚠️ Pegadinhas e não confundir

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Fargate:** Fargate fornece a capacidade para executar containers com ECS ou EKS, sem você administrar diretamente os servidores dessa execução.
- **Batch:** O AWS Batch organiza trabalhos em filas e fornece capacidade de computação para executá-los conforme as configurações.
- **workflow:** Fluxo de trabalho descrito por etapas, decisões e estados. Coordenar etapas é diferente de escrever o programa que realiza cada tarefa.

⚠️ **Uma invocação convencional > 15 minutos** não é suportada. Considere Fargate/Batch/EC2 ou dividir o fluxo. Durable Functions e Lambda MicroVMs têm modelos próprios; não confunda duração total do workflow com uma invocação convencional.

⚠️ Não existe "configurar vCPU" no Lambda: aumente a **memória**.

**Antes de ler este trecho:**

- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.

Lambda × Fargate: função convencional por evento (até 15 min por invocação) × contêiner serverless sem limite de duração.

**Antes de ler este trecho:**

- **PaaS:** Plataforma como serviço: parte da infraestrutura e do ambiente de execução é administrada para você entregar a aplicação. O código e suas regras continuam sendo do cliente.

Lambda é "serverless/FaaS"; o guia o classifica também como PaaS.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Requisições** (por milhão) + **duração** em GB-segundo (arredondada ao ms, proporcional à memória).

Free Tier "sempre gratuito": **1 milhão de requisições e 400.000 GB-s por mês**.

Extras: concorrência provisionada, `/tmp` acima de 512 MB, transferência de dados.

**Antes de ler este trecho:**

- **Savings Plans:** Compromisso de gasto por período em troca de condições de preço para uso elegível. Se a necessidade diminuir, o compromisso não desaparece automaticamente.

Coberto pelo **Compute Savings Plans**.

### Segurança e responsabilidade compartilhada

**Antes de ler este trecho:**

- **SO:** Software básico da máquina, como Linux ou Windows. Ele administra arquivos, memória e execução de programas; atualizar esse software é diferente de atualizar a aplicação.
- **Multi-AZ:** Configuração que utiliza mais de uma zona de disponibilidade. Seu comportamento depende do serviço: não presuma que toda cópia atende leituras ou que isso é backup de dados apagados.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
- **alta disponibilidade:** Planejamento para manter o sistema acessível diante de determinadas falhas. Não é promessa de ausência de qualquer interrupção.

**AWS:** infraestrutura, SO, runtime gerenciado (patches), escalonamento e alta disponibilidade (multi-AZ automático).

**Antes de ler este trecho:**

- **menor privilégio:** Conceder apenas o acesso necessário ao trabalho. Evita que uma tarefa simples carregue poder desnecessário sobre outros recursos.

**Cliente:** **código**, dependências, permissões (execution role com menor privilégio), configuração, dados, segredos (use Secrets Manager).

### 🔄 Atualizações 2025-2026

Contas novas começam com quotas reduzidas de concorrência/memória, aumentadas automaticamente com o uso.

## 5. Caso resolvido: ligando as peças

A escola precisa criar uma miniatura quando uma pessoa envia uma foto. O trabalho tem entrada e resultado definidos e não precisa de uma máquina própria aguardando permanentemente o evento.

A equipe escreve a função de transformação, prepara permissões e configura uma integração compatível para acioná-la. Quando chega a entrada, a função executa o código e grava o resultado num armazenamento adequado. O serviço fornece a infraestrutura da execução.

Se o código falhar ou a entrada aparecer novamente, a aplicação precisa de tratamento apropriado. Não confie em memória de uma execução como armazenamento definitivo. A AWS administrar a execução não corrige automaticamente bibliotecas incluídas no pacote nem decide quem pode ler as fotos.

**Recursos envolvidos:** Função convencional, código, runtime, execution role, trigger e logs.

**Decisões que precisam ser tomadas:** Memória, timeout, concorrência, VPC e tratamento de falha.

**Outra situação comentada:** Miniatura após upload: evento S3 invoca função que precisa de leitura/gravação e logs autorizados.

**Por que não concluir mais do que isso:** Limite de quinze minutos é por invocação convencional; recursos como MicroVMs e Durable Functions têm modelos próprios

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Executar código sem servidores, em resposta a eventos."

**Resposta curta:** Lambda.

**Pergunta:** "Tempo máximo de uma invocação convencional?"

**Resposta curta:** 15 minutos.

**Pergunta:** "Como o Lambda é cobrado?"

**Resposta curta:** No modelo base, requisições e duração (GB-s); concorrência provisionada, snapshots e outros extras podem cobrar sem invocação.

**Antes de ler este trecho:**

- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.

**Pergunta:** "Gerar miniatura quando uma imagem chega ao S3."

**Resposta curta:** Notificação de evento do S3 → Lambda.

**Pergunta:** "Eliminar cold start em função crítica."

**Resposta curta:** Concorrência provisionada.

**Pergunta:** "Dar acesso da função ao DynamoDB."

**Resposta curta:** Execution role.

**Pergunta:** "Tarefa todo dia às 2h sem servidor."

**Resposta curta:** EventBridge Scheduler + Lambda.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do desenvolvedor do Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Quotas do Lambda](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)
- [Preços](https://aws.amazon.com/lambda/pricing/)
- [Durable Functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
