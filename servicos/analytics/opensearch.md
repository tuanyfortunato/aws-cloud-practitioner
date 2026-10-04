# Amazon OpenSearch Service

> **Categoria:** Analytics / busca e logs · **Domínio:** 3 · **Escopo:** Regional (VPC) · **Tópico do guia:** [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)
>
> **Em uma frase:** busca de texto, análise de logs e observabilidade com OpenSearch (sucessor do Elasticsearch gerenciado).
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é o **buscador interno do seu sistema**, que também lê e organiza montanhas de logs.

- ✅ **Escolha quando:** precisa de **busca de texto** ou de **análise de logs**.
- 🚫 **Não é a resposta quando:** quer **SQL sobre arquivos** → [Athena](athena.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "busca de texto", "análise de logs", "Elasticsearch".
<!-- didatico:fim -->

## Destaques

| Item | Detalhe |
|---|---|
| **Domínios gerenciados** | Clusters com nós de dados, nós master dedicados, Multi-AZ, camadas UltraWarm/cold. |
| **OpenSearch Serverless** | Coleções sem gerenciar clusters (busca, séries temporais, **vetores**). |
| **OpenSearch Dashboards** | Visualização (equivalente ao Kibana). |
| **Ingestão** | Data Firehose, OpenSearch Ingestion, CloudWatch Logs, zero-ETL com S3/DynamoDB. |
| **Usos** | Busca de produtos em e-commerce, análise de logs (SIEM), monitoramento de aplicações, **busca vetorial** para IA generativa (RAG). |

## ❓ Perguntas típicas

- "Busca de texto completo no catálogo de produtos." → OpenSearch Service.
- "Analisar e visualizar logs em tempo quase real." → OpenSearch (+ Dashboards).

## 🔗 Documentação oficial

- [OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)
