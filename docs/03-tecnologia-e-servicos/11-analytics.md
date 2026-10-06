# 3.11 Analytics

## 🧠 Antes de começar

**Qual é a dificuldade?** A empresa acumulou dados e quer transformar registros em respostas, como quais cursos tiveram mais procura e como a demanda mudou.

**A ideia em palavras simples:** Analytics reúne preparação, consulta, processamento e visualização de dados. Cada etapa pode exigir uma ferramenta diferente.

**Exemplo do dia a dia:** A escola prepara arquivos com Glue, consulta dados com uma ferramenta adequada e mostra resultados num painel. Dados contínuos de sensores pedem um processo diferente de um relatório mensal.

**O que não concluir?** Criar um painel não corrige os dados nem coleta qualquer fonte automaticamente. Identifique se o problema é preparar, consultar, processar um fluxo ou visualizar.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **ETL** | extrair, transformar e carregar dados. |
| **Streaming** | dados chegando continuamente, em tempo real. |
| **BI** | inteligência de negócio: relatórios e painéis para decisão. |

---

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)**

> 🔎 **Fichas detalhadas:** [Amazon Athena](../../servicos/analytics/athena.md) · [AWS Glue](../../servicos/analytics/glue.md) · [Amazon Kinesis e Amazon Data Firehose](../../servicos/analytics/kinesis.md) · [Amazon EMR](../../servicos/analytics/emr.md) · [Amazon QuickSight (Amazon Quick Sight)](../../servicos/analytics/quicksight.md) · [Amazon OpenSearch Service](../../servicos/analytics/opensearch.md) · [Amazon Redshift](../../servicos/banco-de-dados/redshift.md) · [Lake Formation, MSK, Data Exchange, AppFlow e outros serviços de dados](../../servicos/analytics/lake-formation-msk-e-outros.md)

⬅️ [3.10 Rede e entrega de conteúdo](10-rede-e-entrega-de-conteudo.md) · 🏠 [Índice do domínio](README.md) · [3.12 IA e machine learning](12-ia-e-machine-learning.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

Um dado bruto precisa de estrutura e significado antes de responder bem a uma pergunta. Preparação padroniza; catálogo descreve; consulta seleciona e agrega; processamento executa transformações; visualização apresenta resultados.

Uma fonte contínua pode exigir processamento enquanto os registros chegam. Uma análise mensal pode trabalhar sobre arquivos acumulados. Escolha a ferramenta pela etapa e pela forma de chegada dos dados, e não apenas pela categoria ‘analytics’.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é uma **cozinha de dados**: o **Kinesis** é a esteira que traz os ingredientes em tempo real; o **Glue** lava e corta (ETL) e etiqueta tudo (catálogo); o **Athena** prova direto da despensa (S3) com SQL; o **EMR** é a cozinha industrial (Spark/Hadoop); o **QuickSight** monta o prato bonito (dashboards).

</details>

## 2. Conceitos e opções explicados

**Amazon Athena:** Pontos de prova: SQL **serverless** direto em arquivos no S3 (CSV, JSON, Parquet); cobrado por **dados escaneados**; formatos colunares e particionamento reduzem custo; usa o catálogo do Glue.

**AWS Glue:** **ETL serverless** (extrair, transformar e carregar dados) e **Data Catalog** (catálogo de metadados usado por Athena, Redshift e EMR). Crawlers descobrem o schema automaticamente.

**Amazon Kinesis:** dados em **streaming e tempo real**.

  - **Kinesis Data Streams:** ingestão e processamento de streams (cliques, logs, telemetria).

  - **Amazon Data Firehose** (antes Kinesis Data Firehose): entrega streams automaticamente em S3, Redshift, OpenSearch e outros, sem administração.

  - **Kinesis Video Streams:** streaming de vídeo de dispositivos.

**Amazon EMR:** plataforma de **big data** gerenciada com Apache Spark, Hadoop, Hive e Presto.

**Amazon QuickSight:** **BI** serverless; dashboards e relatórios interativos, inclusive com perguntas em linguagem natural.

**Amazon OpenSearch Service:** **busca** e **análise de logs** (sucessor do Elasticsearch gerenciado), com OpenSearch Dashboards.

**Amazon Redshift:** data warehouse (ver [3.7](07-bancos-de-dados.md)).

**Cai na prova:** "consultar logs no S3 com SQL sem servidor" = Athena; "processar cliques em tempo real" = Kinesis; "painéis para executivos" = QuickSight; "preparar e catalogar dados" = Glue; "Spark/Hadoop gerenciado" = EMR; "busca de texto em produtos" = OpenSearch.

## 3. Como analisar uma situação

**Primeiro, identifique o funcionamento:** Dados entram por fontes/streams; Glue cataloga e transforma; Athena consulta; Redshift organiza análise em warehouse; Quick Sight apresenta resultados; OpenSearch pesquisa documentos/logs.

**Depois, compare as escolhas:** Observe o verbo: consultar SQL no S3, transformar, processar fluxo, executar Spark, pesquisar ou visualizar. Cada verbo aponta para uma etapa distinta.

**Por fim, verifique o limite:** Dashboard não coleta automaticamente todo dado. Catálogo guarda metadados, não copia necessariamente o conteúdo. Streaming e ETL não são sinônimos.

## 4. Caso resolvido

Arquivos de vendas já estão no S3 e você quer uma consulta SQL eventual, sem manter cluster. Qual serviço?

**Raciocínio e resposta:** Athena. Glue Data Catalog pode descrever tabelas; Quick Sight visualiza resultados. EMR faz sentido quando o requisito é processamento com frameworks como Spark.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Ligar cada serviço à função: SQL no S3 → Athena; ETL e catálogo → Glue; tempo real → Kinesis.
- [ ] Saber que o **Athena** cobra por **dados escaneados**.
- [ ] Diferenciar **EMR** (big data com Spark/Hadoop), **QuickSight** (BI) e **OpenSearch** (busca e logs).

**Dica de revisão para a prova:** "SQL em arquivos no S3, sem servidor" → **Athena**. "Tempo real/cliques" → **Kinesis**. "Painéis" → **QuickSight**. "Spark/Hadoop" → **EMR**. "Busca de texto" → **OpenSearch**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).
**Pergunta:** "Consultar arquivos no S3 com SQL padrão, sem infraestrutura."

**Resposta curta:** Athena.

**Pergunta:** "Como o Athena é cobrado?"

**Resposta curta:** Por volume de dados escaneados.

**Pergunta:** "Serviço de ETL serverless e catálogo de dados."

**Resposta curta:** Glue.

**Fundamento explicado no capítulo:** **Amazon Athena:** Pontos de prova: SQL **serverless** direto em arquivos no S3 (CSV, JSON, Parquet); cobrado por **dados escaneados**; formatos colunares e particionamento reduzem custo; usa o catálogo do Glue.

**Pergunta:** "Ingerir e processar dados de cliques em tempo real."

**Resposta curta:** Kinesis Data Streams.

**Pergunta:** "Entregar dados de streaming no S3 sem administração."

**Resposta curta:** Amazon Data Firehose.

**Pergunta:** "Rodar Spark e Hadoop gerenciados."

**Resposta curta:** EMR.

**Pergunta:** "Criar dashboards interativos de BI."

**Resposta curta:** QuickSight.

**Pergunta:** "Busca de texto e análise de logs."

**Resposta curta:** OpenSearch Service.

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
