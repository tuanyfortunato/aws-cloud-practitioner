# Amazon EMR

> **Categoria:** Analytics / big data · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)
>
> **Em uma frase:** plataforma gerenciada de **big data** para rodar Apache Spark, Hadoop, Hive, Presto/Trino, HBase e Flink.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Opções de implantação

| Opção | Detalhe |
|---|---|
| **EMR on EC2** | Clusters com nó **primário** (master), nós **core** (processam e guardam HDFS) e nós **task** (só processam — ideais para **Spot**). |
| **EMR on EKS** | Jobs Spark no seu cluster Kubernetes. |
| **EMR Serverless** | Sem gerenciar clusters; paga por vCPU/memória usados. |

## Destaques

- Dados normalmente no **S3** (EMRFS) — cluster pode ser desligado sem perder dados.
- Escalonamento gerenciado, **instâncias Spot** para reduzir custo, EMR Studio (notebooks).

## Cobrança

- Taxa do EMR por instância/segundo + EC2/EBS (ou vCPU/memória no Serverless).

## ⚠️ Não confundir

- EMR (Spark/Hadoop sob seu controle) × **Glue** (ETL serverless) × **Athena** (SQL serverless) × **Batch** (jobs genéricos em contêiner).

## ❓ Perguntas típicas

- "Rodar Spark e Hadoop gerenciados." → EMR.
- "Reduzir custo de clusters de big data." → Nós task em Spot.

## 🔗 Documentação oficial

- [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html)
