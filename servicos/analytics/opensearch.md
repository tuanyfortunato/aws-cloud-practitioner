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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Índices, documentos e domínios/collections conforme modalidade |
| **O que você decide/configura?** | Ingestão, indexação, capacidade e acesso |
| **Em que ordem as coisas acontecem?** | Dados são indexados para busca/agregação e exploração |
| **O que pode fazer, e em que condição?** | Atende pesquisa e analytics de logs/documentos |
| **O que não pode presumir?** | Não substitui automaticamente sistema transacional de registros |

**Caso comentado:** Busca por texto em catálogo: OpenSearch; transações de compra: banco apropriado.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)
