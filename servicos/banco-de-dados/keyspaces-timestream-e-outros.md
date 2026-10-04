# Amazon Keyspaces, Timestream e outros bancos especializados

> **Categoria:** Bancos de propósito específico · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) · [3.18 Serviços menos conhecidos](../../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md)
>
> **Em uma frase:** a AWS tem um banco "sob medida" para cada modelo de dados — saiba associar o modelo ao serviço.
>
> **Escopo oficial:** 🔀 Keyspaces e MemoryDB ❌ fora do escopo · Timestream ⚪ não listado · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Tabela de decisão

| Serviço | Modelo | Uso | Observação |
|---|---|---|---|
| **Amazon Keyspaces** ❌ *fora do escopo* | Colunar largo (**Apache Cassandra**, CQL) | Migrar Cassandra para serverless | Fora da lista oficial; raramente cai |
| **Amazon Timestream** | **Séries temporais** | Leituras de sensores IoT, métricas, telemetria | 🔄 *Timestream for LiveAnalytics* fechado a novos clientes (20/06/2025); segue o *Timestream for InfluxDB*. Na prova: "séries temporais" → Timestream |
| **Amazon MemoryDB** ❌ *fora do escopo* | Chave-valor em memória **durável** | Banco primário estilo Redis | [Ficha](memorydb.md) |
| **Amazon DocumentDB** | Documentos (MongoDB) | Catálogos, conteúdo | [Ficha](documentdb.md) |
| **Amazon Neptune** | Grafos | Redes sociais, fraude | [Ficha](neptune.md) |
| **Amazon QLDB** | Ledger imutável | — | 🔄 Encerrado em 31/07/2025 (confirmado) — se aparecer em questão antiga: "registro imutável e verificável criptograficamente" |

## Visão geral: qual banco para qual dado

| Necessidade | Serviço |
|---|---|
| Relacional OLTP | [RDS](rds.md) / [Aurora](aurora.md) |
| Chave-valor em escala, serverless | [DynamoDB](dynamodb.md) |
| Cache em memória | [ElastiCache](elasticache.md) / DAX |
| Data warehouse OLAP | [Redshift](redshift.md) |
| Grafos | [Neptune](neptune.md) |
| Documentos | [DocumentDB](documentdb.md) |
| Séries temporais | Timestream |
| Cassandra | Keyspaces |

## ❓ Perguntas típicas

- "Guardar leituras de sensores IoT ao longo do tempo." → Timestream.
- "Migrar Cassandra sem gerenciar servidores." → Keyspaces.

## 🔗 Documentação oficial

- [Bancos de dados na AWS](https://aws.amazon.com/products/databases/)
