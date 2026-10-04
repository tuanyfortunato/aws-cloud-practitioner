# AWS Glue

> **Categoria:** Analytics / integração de dados (ETL) · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)
>
> **Em uma frase:** serviço **serverless de ETL** e **catálogo de dados** para descobrir, preparar e combinar dados para análise.

## Componentes

| Componente | Detalhe |
|---|---|
| **Data Catalog** | Repositório central de metadados (bancos, tabelas, schemas) usado por **Athena, Redshift Spectrum, EMR e Lake Formation**. |
| **Crawlers** | Percorrem S3, JDBC, DynamoDB e **inferem o schema** automaticamente, criando/atualizando tabelas. |
| **ETL jobs** | Spark (PySpark/Scala), Python shell ou Ray; serverless; *job bookmarks* processam só dados novos. |
| **Glue Studio** | Interface visual para criar jobs. |
| **Glue DataBrew** | Preparação visual de dados **sem código** (250+ transformações). |
| **Data Quality** | Regras de qualidade de dados. |
| **Triggers / Workflows** | Agendam e encadeiam crawlers e jobs. |
| **Zero-ETL / conectores** | Integrações com fontes SaaS e bancos. |

## Cobrança

- Jobs e crawlers por **DPU-hora** (por segundo); Data Catalog por objetos armazenados e requisições (camada gratuita).

## ⚠️ Não confundir

- Glue (ETL **serverless** + catálogo) × **EMR** (clusters Spark/Hadoop sob seu controle) × **Data Firehose** (entrega de streaming com transformações simples).

## ❓ Perguntas típicas

- "Serviço de ETL serverless e catálogo de dados." → Glue.
- "Descobrir automaticamente o schema de arquivos no S3." → Glue crawler.
- "Preparar dados visualmente sem código." → Glue DataBrew.

## 🔗 Documentação oficial

- [Guia do Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
