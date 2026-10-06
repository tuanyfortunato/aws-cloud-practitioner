<!-- autoral -->

# Amazon OpenSearch Service

> **Categoria:** Analytics / busca e logs · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** complementar
>
> **Em uma frase:** serviço gerenciado para implantar, operar e escalar clusters do OpenSearch, para busca, análise de registros e monitoramento de aplicações em tempo real.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

O portal da escola precisa de uma busca de materiais que encontre "fotossíntese" mesmo com erro de digitação, e a TI quer pesquisar milhões de linhas de log em segundos. O **OpenSearch Service** gerencia clusters do **OpenSearch**, um mecanismo de busca e análise de código aberto, e também aceita versões antigas do Elasticsearch.

1. Cria-se um domínio (cluster) do OpenSearch Service.
2. Os dados chegam por aplicações ou por serviços como o Amazon Data Firehose.
3. A aplicação faz buscas, e a equipe analisa os registros.
4. O OpenSearch Dashboards mostra gráficos e painéis sobre os dados.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [Amazon Athena](athena.md) | Consultas SQL sobre arquivos no S3 | "SQL ad hoc" |
| [Amazon CloudWatch](../gerenciamento/cloudwatch.md) | Métricas, logs e alarmes dos recursos | "Alarme", "métrica" |
| [Amazon Kinesis e Data Firehose](kinesis.md) | Coleta e entrega fluxos de dados | "Streaming", "tempo real" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
