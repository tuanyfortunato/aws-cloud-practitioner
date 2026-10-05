# Amazon Athena

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Há arquivos com dados no S3 e a equipe quer fazer perguntas sobre esse conteúdo sem administrar um servidor de consultas.

**Como este serviço ajuda?** Athena permite consultar dados em formatos e fontes compatíveis usando SQL. Você precisa descrever ou disponibilizar a estrutura dos dados para que a consulta faça sentido.

**Exemplo do dia a dia:** A escola guarda registros de acesso em arquivos e consulta quantos acessos ocorreram por dia.

**O que ele não resolve sozinho?** Athena não corrige sozinho dados desorganizados nem é o banco transacional do aplicativo. Formato, organização e quantidade de dados consultados influenciam o resultado e o custo.

**Primeiras palavras para entender:**

- **Consulta:** pergunta expressa para obter dados.
- **SQL:** linguagem de consulta.
- **Schema:** descrição dos campos e tipos dos dados.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Analytics / consulta interativa · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)
>
> **Em uma frase:** consultas **SQL serverless** direto em arquivos no S3, pagando só pelos dados escaneados.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Workgroups, consultas, catálogo e local de resultados |
| **O que você decide/configura?** | Dados, schema, formato, permissão e configurações do workgroup |
| **Em que ordem as coisas acontecem?** | Defina tabela sobre dados e execute consulta; resultados têm destino |
| **O que pode fazer, e em que condição?** | Consulta SQL sobre dados suportados sem manter cluster |
| **O que não pode presumir?** | Não é banco OLTP nem deixa leitura de todo arquivo gratuita; otimizar leitura pode reduzir custo |

**Caso comentado:** Consultar logs S3 eventualmente: Athena com catálogo/resultado autorizados.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)
