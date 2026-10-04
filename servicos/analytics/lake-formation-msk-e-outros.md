# Lake Formation, MSK, Data Exchange, AppFlow e outros serviços de dados

> **Categoria:** Analytics / dados · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.18 Serviços menos conhecidos](../../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md)
>
> **Em uma frase:** serviços de dados que aparecem como "qual serviço faz X" — saiba a função de cada um.
>
> **Escopo oficial:** 🔀 MSK, AppFlow, Data Exchange, Clean Rooms e DataZone ❌ fora do escopo · Lake Formation ⚪ não listado · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

| Serviço | O que faz | Cenário de prova |
|---|---|---|
| **AWS Lake Formation** | Monta e **governa um data lake no S3** com controle de acesso centralizado e fino (tabela, coluna, linha, tags) sobre o Glue Data Catalog | "Data lake com permissões centralizadas" |
| **Amazon MSK** (Managed Streaming for Apache Kafka) | **Apache Kafka gerenciado** (provisionado ou serverless); MSK Connect para conectores | "Streaming com Kafka sem gerenciar cluster" |
| **AWS Data Exchange** | Encontrar, assinar e usar **conjuntos de dados de terceiros** (mercado financeiro, clima, saúde) | "Comprar dados de mercado para análise" |
| **Amazon AppFlow** | Transfere dados entre **aplicações SaaS** (Salesforce, SAP, Zendesk, Slack) e serviços AWS **sem código** | "Levar dados do Salesforce para o S3" |
| **AWS Clean Rooms** | Colaborar/analisar dados com parceiros **sem compartilhar os dados brutos** | "Análise conjunta preservando privacidade" |
| **Amazon DataZone / SageMaker Unified Studio** | Catálogo e governança de dados para descoberta e compartilhamento entre times | "Portal de dados corporativo" |
| **Amazon Managed Service for Apache Flink** | Processamento de streams com Flink | "Agregações em tempo real" |
| **AWS Data Pipeline** | Orquestração de dados legada | Fechado a novos clientes — não estudar |

## 🔗 Documentação oficial

- [Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) · [MSK](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html) · [Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/what-is.html) · [AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/what-is-appflow.html)
