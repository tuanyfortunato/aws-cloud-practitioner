# 3.11 Analytics

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon Athena](../../servicos/analytics/athena.md) · [AWS Glue](../../servicos/analytics/glue.md) · [Amazon Kinesis e Amazon Data Firehose](../../servicos/analytics/kinesis.md) · [Amazon EMR](../../servicos/analytics/emr.md) · [Amazon QuickSight (Amazon Quick Sight)](../../servicos/analytics/quicksight.md) · [Amazon OpenSearch Service](../../servicos/analytics/opensearch.md) · [Amazon Redshift](../../servicos/banco-de-dados/redshift.md) · [Lake Formation, MSK, Data Exchange, AppFlow e outros serviços de dados](../../servicos/analytics/lake-formation-msk-e-outros.md)

⬅️ [3.10 Rede e entrega de conteúdo](10-rede-e-entrega-de-conteudo.md) · 🏠 [Índice do domínio](README.md) · [3.12 IA e machine learning](12-ia-e-machine-learning.md) ➡️

---

## 📖 Conteúdo

- **Amazon Athena:** Pontos de prova: SQL **serverless** direto em arquivos no S3 (CSV, JSON, Parquet); cobrado por **dados escaneados**; formatos colunares e particionamento reduzem custo; usa o catálogo do Glue.
- **AWS Glue:** **ETL serverless** (extrair, transformar e carregar dados) e **Data Catalog** (catálogo de metadados usado por Athena, Redshift e EMR). Crawlers descobrem o schema automaticamente.
- **Amazon Kinesis:** dados em **streaming e tempo real**.
  - **Kinesis Data Streams:** ingestão e processamento de streams (cliques, logs, telemetria).
  - **Amazon Data Firehose** (antes Kinesis Data Firehose): entrega streams automaticamente em S3, Redshift, OpenSearch e outros, sem administração.
  - **Kinesis Video Streams:** streaming de vídeo de dispositivos.
- **Amazon EMR:** plataforma de **big data** gerenciada com Apache Spark, Hadoop, Hive e Presto.
- **Amazon QuickSight:** **BI** serverless; dashboards e relatórios interativos, inclusive com perguntas em linguagem natural.
- **Amazon OpenSearch Service:** **busca** e **análise de logs** (sucessor do Elasticsearch gerenciado), com OpenSearch Dashboards.
- **Amazon Redshift:** data warehouse (ver [3.7](07-bancos-de-dados.md)).
- **Cai na prova:** "consultar logs no S3 com SQL sem servidor" = Athena; "processar cliques em tempo real" = Kinesis; "painéis para executivos" = QuickSight; "preparar e catalogar dados" = Glue; "Spark/Hadoop gerenciado" = EMR; "busca de texto em produtos" = OpenSearch.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).

- "Consultar arquivos no S3 com SQL padrão, sem infraestrutura." → Athena.
- "Como o Athena é cobrado?" → Por volume de dados escaneados.
- "Serviço de ETL serverless e catálogo de dados." → Glue.
- "Ingerir e processar dados de cliques em tempo real." → Kinesis Data Streams.
- "Entregar dados de streaming no S3 sem administração." → Amazon Data Firehose.
- "Rodar Spark e Hadoop gerenciados." → EMR.
- "Criar dashboards interativos de BI." → QuickSight.
- "Busca de texto e análise de logs." → OpenSearch Service.

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- 🔄 **Nomes atualizados:** a lista oficial in-scope usa **"Amazon Quick Sight"** (BI) — na prova pode aparecer o nome antigo **QuickSight**.
- ⚠️ Athena × Redshift × RDS: Athena = SQL serverless no S3 (paga por dado escaneado); Redshift = data warehouse (OLAP); RDS = transacional (OLTP).
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.10 Rede e entrega de conteúdo](10-rede-e-entrega-de-conteudo.md) · 🏠 [Índice do domínio](README.md) · [3.12 IA e machine learning](12-ia-e-machine-learning.md) ➡️
