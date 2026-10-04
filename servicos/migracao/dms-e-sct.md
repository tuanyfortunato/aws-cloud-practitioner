# AWS Database Migration Service (DMS) e Schema Conversion Tool (SCT)

> **Categoria:** Migração de bancos de dados · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.17 Migração e transferência](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md)
>
> **Em uma frase:** o DMS **move os dados** (com o banco de origem funcionando); o SCT **converte o schema** entre motores diferentes.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## AWS DMS

| Item | Detalhe |
|---|---|
| **Componentes** | **Endpoints** de origem e destino + **replication instance** (ou **DMS Serverless**) + **tasks**. |
| **Tipos de migração** | **Full load**, **full load + CDC** (*change data capture*: replica mudanças contínuas → mínima indisponibilidade) ou só CDC. |
| **Origens/destinos** | Oracle, SQL Server, MySQL, PostgreSQL, MongoDB, Db2, SAP… → RDS, Aurora, Redshift, DynamoDB, S3, OpenSearch, Kinesis, DocumentDB. |
| **Homogêneas** | Mesmo motor (MySQL → RDS MySQL): só DMS (inclusive *homogeneous data migrations* com ferramentas nativas). |
| **Heterogêneas** | Motores diferentes (Oracle → Aurora PostgreSQL): **SCT/DMS Schema Conversion** + DMS. |
| **Outros usos** | Replicação contínua para análise, consolidação de bancos, DR. |

## AWS SCT e DMS Schema Conversion

- Converte **schema, views, stored procedures e funções** entre motores; gera relatório de avaliação (o que converte automaticamente e o que exige trabalho manual).
- **SCT:** aplicativo de desktop. **DMS Schema Conversion:** versão gerenciada no console, com assistência de IA generativa.
- Também converte schemas de data warehouses (Teradata, Oracle, Netezza → Redshift).

## Cobrança

- DMS: por hora da replication instance (ou DCU no Serverless) + armazenamento + transferência. SCT: gratuito.

## ❓ Perguntas típicas

- "Migrar um banco sem desligar a aplicação." → DMS (full load + CDC).
- "Converter um banco Oracle para Aurora PostgreSQL." → SCT + DMS.
- "Migrar MySQL on-premises para RDS MySQL." → DMS (homogênea, sem SCT).

## 🔗 Documentação oficial

- [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) · [AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)
