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

**Antes de ler este trecho:**

- **Redshift:** Redshift é um ambiente de banco voltado à análise de dados, conhecido como data warehouse.
- **Athena:** Athena permite consultar dados em formatos e fontes compatíveis usando SQL.
- **EMR:** EMR oferece ambientes gerenciados para frameworks de processamento de dados, com modalidades diferentes de execução.
- **metadados:** Informações que descrevem outros dados, como características de um objeto. Conhecer a descrição não significa ler todo o conteúdo.

**Detalhe:** Repositório central de metadados (bancos, tabelas, schemas) usado por **Athena, Redshift Spectrum, EMR e Lake Formation**.

**Crawlers**

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **schema:** Estrutura e tipos dos dados. Em migração, adaptar a estrutura é uma tarefa diferente de copiar os registros.
- **JDBC:** Interface Java para acesso a bancos compatíveis. Um driver faz a integração; conexão e autorização ainda precisam estar corretas.

**Detalhe:** Percorrem S3, JDBC, DynamoDB e **inferem o schema** automaticamente, criando/atualizando tabelas.

**ETL jobs**

**Antes de ler este trecho:**

- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **ETL:** Extrair dados de uma fonte, transformá-los e carregá-los num destino. A regra de transformação deve ser definida de acordo com o significado dos dados.
- **Spark:** Ferramenta de processamento de dados. O ambiente pode executar o trabalho distribuído, mas a equipe define o código e valida a transformação.
- **job:** Trabalho submetido a uma execução. Uma fila ou agendador organiza quando ele roda; seu programa realiza a tarefa.

**Detalhe:** Spark (PySpark/Scala), Python shell ou Ray; serverless; *job bookmarks* processam só dados novos.

**Glue Studio**

**Antes de ler este trecho:**

- **Glue:** Glue oferece catálogo e ferramentas de integração e transformação de dados.

**Detalhe:** Interface visual para criar jobs.

**Glue DataBrew**

**Detalhe:** Preparação visual de dados **sem código** (250+ transformações).

**Data Quality**

**Detalhe:** Regras de qualidade de dados.

**Triggers / Workflows**

**Detalhe:** Agendam e encadeiam crawlers e jobs.

**Zero-ETL / conectores**

**Antes de ler este trecho:**

- **SaaS:** Software como serviço: aplicação pronta disponibilizada para uso. O cliente administra seu uso e seus dados conforme a oferta, em vez de construir o software do zero.

**Detalhe:** Integrações com fontes SaaS e bancos.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Catalogar um dado não o torna correto nem concede acesso irrestrito. As transformações e permissões precisam ser definidas para cada processo.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **streaming:** Fluxo contínuo de dados ou mídia. É diferente de esperar um arquivo completo antes de iniciar o trabalho.

Glue (ETL **serverless** + catálogo) × **EMR** (clusters Spark/Hadoop sob seu controle) × **Data Firehose** (entrega de streaming com transformações simples).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **segundo:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.

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
