# Amazon Kinesis e Amazon Data Firehose

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Dados chegam continuamente, como cliques ou leituras de sensores. A equipe quer recebê-los e processá-los sem esperar juntar um arquivo no fim do dia.

**Como este serviço ajuda?** Kinesis Data Streams organiza fluxos de registros para consumidores. A ficha também distingue Firehose, que entrega dados a destinos compatíveis, e outras ferramentas de processamento e vídeo.

**Exemplo do dia a dia:** Sensores enviam leituras continuamente. Uma aplicação lê o fluxo e calcula indicadores; uma opção de entrega pode levar os dados ao armazenamento.

**O que ele não resolve sozinho?** Fluxo contínuo não é o mesmo problema que uma fila de tarefas. As ferramentas da família têm funções e tempos de entrega diferentes.

**Primeiras palavras para entender:**

- **Streaming:** fluxo contínuo de dados.
- **Produtor:** quem envia registros.
- **Consumidor:** quem lê e processa esses registros.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Analytics / streaming · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)
>
> **Em uma frase:** coleta, processa e entrega **dados em streaming e tempo real** (cliques, logs, telemetria, vídeo).
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento


**Passo 1.** Defina quem produz registros e quem precisa processá-los ou recebê-los num destino.

**Passo 2.** Escolha o produto apropriado para fluxo, processamento ou entrega e envie os dados pelas interfaces compatíveis.

**Passo 3.** Acompanhe consumo, conservação e destino dos registros. Cada produto tem condições diferentes de processamento e espera.

## 2. Recursos e opções, com significado

### Família

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **Redshift:** Redshift é um ambiente de banco voltado à análise de dados, conhecido como data warehouse.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **retenção:** Tempo durante o qual dados ou registros são conservados. Depois desse prazo, o comportamento depende das regras do serviço e das configurações.
- **HTTP:** Protocolo de pedidos e respostas usado na web. Uma URL e um método indicam a operação; HTTP sozinho não protege o conteúdo por criptografia.
- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.
- **Parquet:** Formatos de dados com estruturas diferentes. O formato influencia como uma ferramenta lê e processa os arquivos; não muda sozinho o significado dos registros.
- **ML:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.
- **On-Demand:** Modalidade de uso sem o compromisso de longo prazo descrito por reservas e planos. Cobrança e unidades dependem do recurso contratado.
- **KCL:** Biblioteca para desenvolver consumidores de Kinesis. Ela ajuda a processar registros; a aplicação continua definindo o trabalho sobre os dados.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Serviço | O que faz | Detalhes |
|---|---|---|
| **Kinesis Data Streams** | Ingestão e armazenamento de streams para **processamento em tempo real** por vários consumidores | **Shards** (capacidade); modos **provisioned** ou **on-demand**; retenção padrão **24 h**, até **365 dias** (8.760 h; acima de 24 h é pago); dados podem ser **relidos**; consumidores: Lambda, KCL, Managed Flink, Firehose |
| **Amazon Data Firehose** (antes Kinesis Data Firehose) | **Entrega** streams automaticamente em destinos, **sem administração** | Destinos: **S3**, **Redshift**, **OpenSearch**, Splunk, HTTP, parceiros, tabelas Iceberg; buffer por tamanho/tempo (**quase tempo real**); transformação com Lambda, conversão para Parquet, compressão |
| **Kinesis Video Streams** | Ingestão e armazenamento de **vídeo** de dispositivos (câmeras) | Integra com Rekognition Video, ML |
| **Amazon Managed Service for Apache Flink** (antes Kinesis Data Analytics) | Processamento de streams com Flink (SQL, Java, Python) | Agregações, janelas, detecção de anomalias |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Fluxo contínuo não é o mesmo problema que uma fila de tarefas. As ferramentas da família têm funções e tempos de entrega diferentes.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **SQS:** SQS guarda mensagens numa fila até que consumidores as recebam e processem.
- **streaming:** Fluxo contínuo de dados ou mídia. É diferente de esperar um arquivo completo antes de iniciar o trabalho.


**Kinesis × SQS:** streaming em tempo real com **vários consumidores relendo** dados ordenados × fila de mensagens para desacoplar (mensagem consumida e apagada).


**Data Streams × Firehose:** processamento customizado em tempo real × entrega gerenciada em destinos.

**Antes de ler este trecho:**

- **MSK / Kafka:** Kafka é uma plataforma de fluxo de eventos; MSK é a oferta gerenciada compatível da AWS. A aplicação ainda precisa produzir e consumir os registros.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.


**Kinesis × MSK:** serviço nativo AWS × Apache Kafka gerenciado.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **GB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.


Data Streams: por shard-hora (provisioned) ou por GB e stream-hora (on-demand). Firehose: por GB ingerido e conversões. Video: por GB ingerido/armazenado.

## 5. Caso resolvido: ligando as peças

Sensores enviam leituras continuamente. Uma aplicação lê o fluxo e calcula indicadores; uma opção de entrega pode levar os dados ao armazenamento.

**Aplicando a sequência à situação:**

**Etapa 1:** Defina quem produz registros e quem precisa processá-los ou recebê-los num destino.
**Etapa 2:** Escolha o produto apropriado para fluxo, processamento ou entrega e envie os dados pelas interfaces compatíveis.
**Etapa 3:** Acompanhe consumo, conservação e destino dos registros. Cada produto tem condições diferentes de processamento e espera.

**Resultado e responsabilidade:** Kinesis Data Streams organiza fluxos de registros para consumidores. A ficha também distingue Firehose, que entrega dados a destinos compatíveis, e outras ferramentas de processamento e vídeo.

**Recursos envolvidos:** Streams, producers, consumers e oferta Firehose associada.

**Decisões que precisam ser tomadas:** Capacidade, retenção e destinos conforme produto.

**Antes de ler este trecho:**

- **telemetria:** Medidas e informações enviadas por um equipamento ou sistema. Coletar dados é uma etapa diferente de analisá-los ou agir sobre eles.


**Outra situação comentada:** Telemetria contínua: Data Streams para consumidores; Firehose para entrega suportada com buffering.

**Por que não concluir mais do que isso:** Kinesis não é apenas notificação por e-mail; produtos da família têm funções distintas

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Dados chegam continuamente, como cliques ou leituras de sensores. A equipe quer recebê-los e processá-los sem esperar juntar um arquivo no fim do dia.

**2. O que a solução fornece?**

Kinesis Data Streams organiza fluxos de registros para consumidores. A ficha também distingue Firehose, que entrega dados a destinos compatíveis, e outras ferramentas de processamento e vídeo.

**3. Que conclusão seria incorreta?**

Fluxo contínuo não é o mesmo problema que uma fila de tarefas. As ferramentas da família têm funções e tempos de entrega diferentes.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Ingerir e processar dados de cliques em tempo real."

**Resposta curta:** Kinesis Data Streams.


**Fundamento explicado no capítulo:** "Ingerir e processar dados de cliques em tempo real." → Kinesis Data Streams.

**Pergunta:** "Entregar dados de streaming no S3 sem administração."

**Resposta curta:** Amazon Data Firehose.


**Fundamento explicado no capítulo:** "Entregar dados de streaming no S3 sem administração." → Amazon Data Firehose.

**Pergunta:** "Transmitir vídeo de câmeras para análise."

**Resposta curta:** Kinesis Video Streams.


**Fundamento explicado no capítulo:** "Transmitir vídeo de câmeras para análise." → Kinesis Video Streams.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) · [Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
