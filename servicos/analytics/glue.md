<!-- autoral -->

# AWS Glue

> **Categoria:** Analytics e integração de dados (ETL) · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** serviço serverless de integração de dados que descobre fontes, mantém um catálogo central e roda pipelines de ETL para preparar os dados para análise.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

Os dados da rede de escolas estão espalhados: registros de acesso em JSON no S3, exportações do banco de matrículas em CSV e planilhas das secretarias, cada uma com colunas diferentes. Antes de qualquer análise, alguém precisa descobrir o que existe, limpar e juntar tudo num formato comum.

Esse trabalho chama-se **ETL**: extrair (*extract*) da origem, transformar (*transform*) e carregar (*load*) no destino. O **Glue** faz isso sem servidor para gerenciar. Um **crawler** percorre as fontes, reconhece o formato e cria ou atualiza tabelas no **catálogo de dados** (*Data Catalog*), que registra onde está cada conjunto de dados e qual a sua estrutura. **Jobs de ETL**, criados visualmente no Glue Studio ou em código, transformam os dados e os gravam no data lake. O Athena, o EMR e o Redshift consultam os dados catalogados.

O limite: o Glue prepara e cataloga, mas não é a ferramenta de consulta nem de painel; a pergunta da direção é respondida pelo [Athena](athena.md) ou pelo [Redshift](../banco-de-dados/redshift.md), e mostrada no [Quick Sight](quicksight.md). E um job mal dimensionado custa mais, porque a cobrança é pelo tempo de processamento.

## Como funciona

1. Um crawler lê as fontes (S3, bancos e outras) e cria as tabelas no catálogo de dados.
2. Você cria um job de ETL, visualmente ou em código, que lê as tabelas, transforma e grava o resultado, por exemplo no S3 em formato colunar.
3. O job roda sob demanda, agendado ou disparado por eventos, num motor serverless baseado em Apache Spark.
4. Athena, EMR e Redshift usam o catálogo para consultar os dados preparados.

## Opções principais

| Peça | O que faz | Exemplo na escola |
|---|---|---|
| Crawler | Descobre o formato e cria tabelas no catálogo | Catalogar os registros de acesso no S3 |
| Catálogo de dados | Registro central de onde estão os dados e sua estrutura | Athena sabe as colunas dos arquivos |
| Jobs de ETL | Transformam e carregam os dados | Juntar planilhas e banco num só formato |
| Glue Studio | Interface visual para criar e acompanhar os jobs | Equipe sem muita programação |
| Glue DataBrew | Preparação visual de dados | Limpar colunas de uma planilha |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Fontes de dados | Mais de 70 | 06/10/2026 |
| Catálogo de dados gratuito | Primeiro milhão de objetos e primeiro milhão de acessos | 06/10/2026 |
| Unidade de cobrança dos jobs | DPU-hora (1 DPU = 4 vCPU e 16 GB), por segundo | 06/10/2026 |

## Como é cobrado

Jobs de ETL e crawlers são cobrados por hora de DPU (unidade de processamento), medida por segundo, sem custo de início nem de parada. O catálogo tem taxa mensal pelo armazenamento e pelos acessos, com o primeiro milhão de cada grátis.

## Não confundir com

| Serviço | Diferença para o Glue | Pista no enunciado |
|---|---|---|
| [Amazon Athena](athena.md) | Consulta os dados com SQL | "SQL no S3" |
| [Amazon EMR](emr.md) | Clusters de Hadoop e Spark que a equipe opera | "Hadoop", "cluster" |
| [Amazon Data Firehose](kinesis.md) | Entrega fluxos em tempo real ao destino | "Streaming", "tempo real" |
| [AWS DMS](../migracao/dms-e-sct.md) | Migra bancos de dados | "Migrar o banco" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
- [Crawlers e catálogo de dados](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html)
- [Preços do AWS Glue](https://aws.amazon.com/glue/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
