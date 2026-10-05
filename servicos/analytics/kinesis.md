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

## Família

| Serviço | O que faz | Detalhes |
|---|---|---|
| **Kinesis Data Streams** | Ingestão e armazenamento de streams para **processamento em tempo real** por vários consumidores | **Shards** (capacidade); modos **provisioned** ou **on-demand**; retenção padrão **24 h**, até **365 dias** (8.760 h; acima de 24 h é pago); dados podem ser **relidos**; consumidores: Lambda, KCL, Managed Flink, Firehose |
| **Amazon Data Firehose** (antes Kinesis Data Firehose) | **Entrega** streams automaticamente em destinos, **sem administração** | Destinos: **S3**, **Redshift**, **OpenSearch**, Splunk, HTTP, parceiros, tabelas Iceberg; buffer por tamanho/tempo (**quase tempo real**); transformação com Lambda, conversão para Parquet, compressão |
| **Kinesis Video Streams** | Ingestão e armazenamento de **vídeo** de dispositivos (câmeras) | Integra com Rekognition Video, ML |
| **Amazon Managed Service for Apache Flink** (antes Kinesis Data Analytics) | Processamento de streams com Flink (SQL, Java, Python) | Agregações, janelas, detecção de anomalias |

## Cobrança

- Data Streams: por shard-hora (provisioned) ou por GB e stream-hora (on-demand). Firehose: por GB ingerido e conversões. Video: por GB ingerido/armazenado.

## ⚠️ Não confundir

- **Kinesis × SQS:** streaming em tempo real com **vários consumidores relendo** dados ordenados × fila de mensagens para desacoplar (mensagem consumida e apagada).
- **Data Streams × Firehose:** processamento customizado em tempo real × entrega gerenciada em destinos.
- **Kinesis × MSK:** serviço nativo AWS × Apache Kafka gerenciado.

## ❓ Perguntas típicas

- "Ingerir e processar dados de cliques em tempo real." → Kinesis Data Streams.
- "Entregar dados de streaming no S3 sem administração." → Amazon Data Firehose.
- "Transmitir vídeo de câmeras para análise." → Kinesis Video Streams.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Streams, producers, consumers e oferta Firehose associada |
| **O que você decide/configura?** | Capacidade, retenção e destinos conforme produto |
| **Em que ordem as coisas acontecem?** | Produtores publicam; consumidores processam fluxo ou entrega agrupa dados para destino |
| **O que pode fazer, e em que condição?** | Atende ingestão contínua e processamento de streaming |
| **O que não pode presumir?** | Kinesis não é apenas notificação por e-mail; produtos da família têm funções distintas |

**Caso comentado:** Telemetria contínua: Data Streams para consumidores; Firehose para entrega suportada com buffering.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) · [Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)
