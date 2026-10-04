# Amazon Athena

> **Categoria:** Analytics / consulta interativa · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)
>
> **Em uma frase:** consultas **SQL serverless** direto em arquivos no S3, pagando só pelos dados escaneados.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é **fazer perguntas em SQL direto para arquivos no S3**, sem montar banco de dados nenhum.

- ✅ **Escolha quando:** precisa de **consultas pontuais em logs e arquivos no S3**, pagando só pelo que é lido.
- 🚫 **Não é a resposta quando:** precisa de um **data warehouse sempre disponível** → [Redshift](../banco-de-dados/redshift.md); precisa de **Spark/Hadoop** → [EMR](emr.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "SQL no S3", "serverless", "pago por dados escaneados", "consultar logs".
<!-- didatico:fim -->

## Para que serve

- Analisar logs (CloudTrail, ALB, VPC Flow Logs, CloudFront) e dados do data lake sem carregar em banco.
- Consultas ad hoc, exploração de dados, relatórios com QuickSight, análise do CUR.

## Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Formatos** | CSV, JSON, **Parquet**, **ORC**, Avro, Iceberg, logs. |
| **Catálogo** | Usa o **AWS Glue Data Catalog** (tabelas/schemas); crawlers descobrem o schema. |
| **Resultados** | Gravados num bucket S3. |
| **Workgroups** | Separam times/custos e impõem limites de dados escaneados. |
| **Federated query** | Consulta outras fontes (RDS, DynamoDB, Redshift, on-premises) via conectores Lambda. |
| **Otimização de custo** | **Formatos colunares**, **compressão** e **particionamento** reduzem o volume escaneado (e o custo). |
| **Athena for Apache Spark** | Notebooks Spark serverless. |
| **Capacidade provisionada** | Opcional, preço fixo por DPU. |

## Cobrança

- Por **TB de dados escaneados** (🧊 valor), com mínimo por consulta; DDL e consultas com falha não cobram.

## ⚠️ Não confundir

- Athena (SQL sob demanda no S3) × **Redshift** (data warehouse carregado e sempre disponível) × **Redshift Spectrum** (Redshift lendo o S3) × **EMR** (clusters Spark/Hadoop).

## ❓ Perguntas típicas

- "Consultar arquivos no S3 com SQL padrão, sem infraestrutura." → Athena.
- "Como o Athena é cobrado?" → Por volume de dados escaneados.
- "Reduzir custo de consultas no Athena." → Parquet/ORC, compressão e particionamento.

## 🔗 Documentação oficial

- [Guia do Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)
