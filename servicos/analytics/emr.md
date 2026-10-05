# Amazon EMR

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A equipe precisa processar grandes conjuntos de dados usando ferramentas como Apache Spark, sem montar sozinha toda a infraestrutura necessária.

**Como este serviço ajuda?** EMR oferece ambientes gerenciados para frameworks de processamento de dados, com modalidades diferentes de execução.

**Exemplo do dia a dia:** Uma equipe executa um processo Spark para preparar um grande histórico antes de gerar relatórios.

**O que ele não resolve sozinho?** EMR não escreve o processo de análise nem elimina decisões sobre dados, capacidade e execução. As responsabilidades variam pela modalidade escolhida.

**Primeiras palavras para entender:**

- **Framework:** conjunto de ferramentas para desenvolver tarefas.
- **Spark:** ferramenta de processamento de dados.
- **Cluster:** recursos que executam o processamento em conjunto.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Frameworks como Spark/Hadoop e modalidades de execução |
| **O que você decide/configura?** | Framework, jobs, capacidade e dados |
| **Em que ordem as coisas acontecem?** | Submeta processamento distribuído em infraestrutura/modalidade apropriada |
| **O que pode fazer, e em que condição?** | Executa frameworks de big data gerenciados |
| **O que não pode presumir?** | Não é ferramenta de dashboard e ainda exige configuração do job |

**Caso comentado:** Equipe já usa Spark para transformar grandes dados: EMR; SQL eventual no S3: Athena.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html)
