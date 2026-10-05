# AWS Glue

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Os dados vêm de lugares diferentes, com formatos que não combinam. A equipe precisa conhecê-los e prepará-los antes de analisar.

**Como este serviço ajuda?** Glue oferece catálogo e ferramentas de integração e transformação de dados. Ele ajuda a descobrir estruturas e a executar processos de preparação.

**Exemplo do dia a dia:** A escola reúne arquivos de matrículas, padroniza campos e organiza informações sobre sua estrutura para análises posteriores.

**O que ele não resolve sozinho?** Catalogar um dado não o torna correto nem concede acesso irrestrito. As transformações e permissões precisam ser definidas para cada processo.

**Primeiras palavras para entender:**

- **Catálogo:** descrição organizada de dados.
- **ETL:** extrair, transformar e carregar dados.
- **Crawler:** recurso que examina fontes para identificar estruturas.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Analytics / integração de dados (ETL) · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)
>
> **Em uma frase:** serviço **serverless de ETL** e **catálogo de dados** para descobrir, preparar e combinar dados para análise.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Componentes

| Componente | Detalhe |
|---|---|
| **Data Catalog** | Repositório central de metadados (bancos, tabelas, schemas) usado por **Athena, Redshift Spectrum, EMR e Lake Formation**. |
| **Crawlers** | Percorrem S3, JDBC, DynamoDB e **inferem o schema** automaticamente, criando/atualizando tabelas. |
| **ETL jobs** | Spark (PySpark/Scala), Python shell ou Ray; serverless; *job bookmarks* processam só dados novos. |
| **Glue Studio** | Interface visual para criar jobs. |
| **Glue DataBrew** | Preparação visual de dados **sem código** (250+ transformações). |
| **Data Quality** | Regras de qualidade de dados. |
| **Triggers / Workflows** | Agendam e encadeiam crawlers e jobs. |
| **Zero-ETL / conectores** | Integrações com fontes SaaS e bancos. |

## Cobrança

- Jobs e crawlers por **DPU-hora** (por segundo); Data Catalog por objetos armazenados e requisições (camada gratuita).

## ⚠️ Não confundir

- Glue (ETL **serverless** + catálogo) × **EMR** (clusters Spark/Hadoop sob seu controle) × **Data Firehose** (entrega de streaming com transformações simples).

## ❓ Perguntas típicas

- "Serviço de ETL serverless e catálogo de dados." → Glue.
- "Descobrir automaticamente o schema de arquivos no S3." → Glue crawler.
- "Preparar dados visualmente sem código." → Glue DataBrew.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Data Catalog, crawlers, jobs e workflows |
| **O que você decide/configura?** | Fonte, schema, script, role e capacidade |
| **Em que ordem as coisas acontecem?** | Crawler descreve dados; job transforma; catálogo atende motores de consulta |
| **O que pode fazer, e em que condição?** | Oferece integração e ETL gerenciado |
| **O que não pode presumir?** | Catálogo não contém necessariamente os arquivos; crawler não faz sozinho a transformação de negócio |

**Caso comentado:** Padronizar arquivos antes da análise: Glue job; consultar dados: Athena.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
