# Amazon Kinesis e Amazon Data Firehose

> **Categoria:** Analytics / streaming · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)
>
> **Em uma frase:** coleta, processa e entrega **dados em streaming e tempo real** (cliques, logs, telemetria, vídeo).
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Família

| Serviço | O que faz | Detalhes |
|---|---|---|
| **Kinesis Data Streams** | Ingestão e armazenamento de streams para **processamento em tempo real** por vários consumidores | **Shards** (capacidade); modos **provisioned** ou **on-demand**; retenção padrão **24 h**, até **365 dias**; dados podem ser **relidos**; consumidores: Lambda, KCL, Managed Flink, Firehose |
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

## 🔗 Documentação oficial

- [Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) · [Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)
