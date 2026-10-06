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

## 1. A sequência de funcionamento

**Passo 1.** Escolha a ferramenta de processamento e prepare o código e os dados de entrada.

**Passo 2.** Execute o trabalho numa modalidade EMR compatível e com os acessos necessários.

**Passo 3.** Valide os dados de saída e acompanhe uso de capacidade. O ambiente executa o processo; a lógica de análise deve estar correta.

## 2. Recursos e opções, com significado

### Opções de implantação

**EMR on EC2**

**Detalhe:** Clusters com nó **primário** (master), nós **core** (processam e guardam HDFS) e nós **task** (só processam — ideais para **Spot**).

**EMR on EKS**

**Detalhe:** Jobs Spark no seu cluster Kubernetes.

**EMR Serverless**

**Detalhe:** Sem gerenciar clusters; paga por vCPU/memória usados.

### Destaques

Dados normalmente no **S3** (EMRFS) — cluster pode ser desligado sem perder dados.

Escalonamento gerenciado, **instâncias Spot** para reduzir custo, EMR Studio (notebooks).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

EMR não escreve o processo de análise nem elimina decisões sobre dados, capacidade e execução. As responsabilidades variam pela modalidade escolhida.

### ⚠️ Não confundir

EMR (Spark/Hadoop sob seu controle) × **Glue** (ETL serverless) × **Athena** (SQL serverless) × **Batch** (jobs genéricos em contêiner).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Taxa do EMR por instância/segundo + EC2/EBS (ou vCPU/memória no Serverless).

## 5. Caso resolvido: ligando as peças

Uma equipe executa um processo Spark para preparar um grande histórico antes de gerar relatórios.

**Aplicando a sequência à situação:**

**Etapa 1:** Escolha a ferramenta de processamento e prepare o código e os dados de entrada.
**Etapa 2:** Execute o trabalho numa modalidade EMR compatível e com os acessos necessários.
**Etapa 3:** Valide os dados de saída e acompanhe uso de capacidade. O ambiente executa o processo; a lógica de análise deve estar correta.

**Resultado e responsabilidade:** EMR oferece ambientes gerenciados para frameworks de processamento de dados, com modalidades diferentes de execução.

**Recursos envolvidos:** Frameworks como Spark/Hadoop e modalidades de execução.

**Decisões que precisam ser tomadas:** Framework, jobs, capacidade e dados.

**Outra situação comentada:** Equipe já usa Spark para transformar grandes dados: EMR; SQL eventual no S3: Athena.

**Por que não concluir mais do que isso:** Não é ferramenta de dashboard e ainda exige configuração do job

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Rodar Spark e Hadoop gerenciados."

**Resposta curta:** EMR.

**Pergunta:** "Reduzir custo de clusters de big data."

**Resposta curta:** Nós task em Spot.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
