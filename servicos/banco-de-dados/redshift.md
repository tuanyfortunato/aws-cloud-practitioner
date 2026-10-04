# Amazon Redshift

> **Categoria:** Data warehouse · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) · [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)
>
> **Em uma frase:** data warehouse colunar e massivamente paralelo (MPP) para análises SQL (OLAP) sobre terabytes a petabytes.

## Para que serve

- Relatórios de BI, dashboards (QuickSight), análises históricas, consolidação de dados de várias fontes.

## Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Armazenamento colunar + compressão** | Consultas analíticas rápidas lendo só as colunas necessárias. |
| **Cluster provisionado** | Nó líder + nós de computação; **RA3** separa computação de armazenamento gerenciado (S3). |
| **Redshift Serverless** | Sem gerenciar cluster; paga por RPU-hora usada. |
| **Redshift Spectrum** | Consulta dados **direto no S3** (data lake) junto com tabelas locais. |
| **Concurrency scaling** | Capacidade extra temporária em picos de consultas. |
| **Data sharing** | Compartilha dados entre clusters/contas sem copiar. |
| **Zero-ETL** | Integra Aurora, RDS, DynamoDB e aplicações SaaS quase em tempo real. |
| **Redshift ML** | Cria modelos (SageMaker) com SQL. |
| **Segurança** | VPC, criptografia KMS, auditoria, controle por coluna/linha. |

## Cobrança

- Nó-hora (ou nós reservados) ou RPU-hora (Serverless) + armazenamento gerenciado + Spectrum por TB escaneado.

## ⚠️ Pegadinhas e não confundir

- **Redshift (OLAP)** × **RDS/Aurora (OLTP)**.
- **Redshift** (data warehouse sempre disponível) × **Athena** (SQL sob demanda direto no S3, paga por dado escaneado).

## ❓ Perguntas típicas

- "Data warehouse para relatórios de BI sobre petabytes." → Redshift.
- "Consultar dados do S3 junto com o data warehouse." → Redshift Spectrum.

## 🔗 Documentação oficial

- [Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html)
