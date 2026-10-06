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

## 1. A sequência de funcionamento

**Passo 1.** Defina fontes, estruturas e a transformação necessária para preparar os dados.

**Passo 2.** Catalogue ou descubra estruturas e execute trabalhos de transformação compatíveis.

**Passo 3.** Verifique o conteúdo de saída e suas permissões. Padronizar nomes de campos não garante qualidade de todo registro.

## 2. Recursos e opções, com significado

### Componentes

**Data Catalog**

**Detalhe:** Repositório central de metadados (bancos, tabelas, schemas) usado por **Athena, Redshift Spectrum, EMR e Lake Formation**.

**Crawlers**

**Detalhe:** Percorrem S3, JDBC, DynamoDB e **inferem o schema** automaticamente, criando/atualizando tabelas.

**ETL jobs**

**Detalhe:** Spark (PySpark/Scala), Python shell ou Ray; serverless; *job bookmarks* processam só dados novos.

**Glue Studio**

**Detalhe:** Interface visual para criar jobs.

**Glue DataBrew**

**Detalhe:** Preparação visual de dados **sem código** (250+ transformações).

**Data Quality**

**Detalhe:** Regras de qualidade de dados.

**Triggers / Workflows**

**Detalhe:** Agendam e encadeiam crawlers e jobs.

**Zero-ETL / conectores**

**Detalhe:** Integrações com fontes SaaS e bancos.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Catalogar um dado não o torna correto nem concede acesso irrestrito. As transformações e permissões precisam ser definidas para cada processo.

### ⚠️ Não confundir

Glue (ETL **serverless** + catálogo) × **EMR** (clusters Spark/Hadoop sob seu controle) × **Data Firehose** (entrega de streaming com transformações simples).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Jobs e crawlers por **DPU-hora** (por segundo); Data Catalog por objetos armazenados e requisições (camada gratuita).

## 5. Caso resolvido: ligando as peças

A escola reúne arquivos de matrículas, padroniza campos e organiza informações sobre sua estrutura para análises posteriores.

**Aplicando a sequência à situação:**

**Etapa 1:** Defina fontes, estruturas e a transformação necessária para preparar os dados.
**Etapa 2:** Catalogue ou descubra estruturas e execute trabalhos de transformação compatíveis.
**Etapa 3:** Verifique o conteúdo de saída e suas permissões. Padronizar nomes de campos não garante qualidade de todo registro.

**Resultado e responsabilidade:** Glue oferece catálogo e ferramentas de integração e transformação de dados. Ele ajuda a descobrir estruturas e a executar processos de preparação.

**Recursos envolvidos:** Data Catalog, crawlers, jobs e workflows.

**Decisões que precisam ser tomadas:** Fonte, schema, script, role e capacidade.

**Outra situação comentada:** Padronizar arquivos antes da análise: Glue job; consultar dados: Athena.

**Por que não concluir mais do que isso:** Catálogo não contém necessariamente os arquivos; crawler não faz sozinho a transformação de negócio

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Serviço de ETL serverless e catálogo de dados."

**Resposta curta:** Glue.

**Pergunta:** "Descobrir automaticamente o schema de arquivos no S3."

**Resposta curta:** Glue crawler.

**Pergunta:** "Preparar dados visualmente sem código."

**Resposta curta:** Glue DataBrew.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
