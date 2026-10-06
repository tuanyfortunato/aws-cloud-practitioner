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

## 1. A sequência de funcionamento

**Passo 1.** Defina quem produz registros e quem precisa processá-los ou recebê-los num destino.

**Passo 2.** Escolha o produto apropriado para fluxo, processamento ou entrega e envie os dados pelas interfaces compatíveis.

**Passo 3.** Acompanhe consumo, conservação e destino dos registros. Cada produto tem condições diferentes de processamento e espera.

## 2. Recursos e opções, com significado

### Família

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

**Kinesis × SQS:** streaming em tempo real com **vários consumidores relendo** dados ordenados × fila de mensagens para desacoplar (mensagem consumida e apagada).

**Data Streams × Firehose:** processamento customizado em tempo real × entrega gerenciada em destinos.

**Kinesis × MSK:** serviço nativo AWS × Apache Kafka gerenciado.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

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

**Outra situação comentada:** Telemetria contínua: Data Streams para consumidores; Firehose para entrega suportada com buffering.

**Por que não concluir mais do que isso:** Kinesis não é apenas notificação por e-mail; produtos da família têm funções distintas

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Ingerir e processar dados de cliques em tempo real."

**Resposta curta:** Kinesis Data Streams.

**Pergunta:** "Entregar dados de streaming no S3 sem administração."

**Resposta curta:** Amazon Data Firehose.

**Pergunta:** "Transmitir vídeo de câmeras para análise."

**Resposta curta:** Kinesis Video Streams.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) · [Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
