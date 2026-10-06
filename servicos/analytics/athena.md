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

## 1. A sequência de funcionamento

**Passo 1.** Identifique a fonte compatível e descreva a estrutura dos dados.

**Passo 2.** Escreva uma consulta para responder a uma pergunta concreta e execute-a sobre os dados necessários.

**Passo 3.** Leia o resultado e examine o volume consultado. Dados mal interpretados não se tornam corretos só porque a consulta executou.

## 2. Recursos e opções, com significado

### Para que serve

Analisar logs (CloudTrail, ALB, VPC Flow Logs, CloudFront) e dados do data lake sem carregar em banco.

Consultas ad hoc, exploração de dados, relatórios com QuickSight, análise do CUR.

### Conceitos e configurações

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

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Athena não corrige sozinho dados desorganizados nem é o banco transacional do aplicativo. Formato, organização e quantidade de dados consultados influenciam o resultado e o custo.

### ⚠️ Não confundir

Athena (SQL sob demanda no S3) × **Redshift** (data warehouse carregado e sempre disponível) × **Redshift Spectrum** (Redshift lendo o S3) × **EMR** (clusters Spark/Hadoop).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por **TB de dados escaneados** (🧊 valor), com mínimo por consulta; DDL e consultas com falha não cobram.

## 5. Caso resolvido: ligando as peças

A escola guarda registros de acesso em arquivos e consulta quantos acessos ocorreram por dia.

**Aplicando a sequência à situação:**

**Etapa 1:** Identifique a fonte compatível e descreva a estrutura dos dados.
**Etapa 2:** Escreva uma consulta para responder a uma pergunta concreta e execute-a sobre os dados necessários.
**Etapa 3:** Leia o resultado e examine o volume consultado. Dados mal interpretados não se tornam corretos só porque a consulta executou.

**Resultado e responsabilidade:** Athena permite consultar dados em formatos e fontes compatíveis usando SQL. Você precisa descrever ou disponibilizar a estrutura dos dados para que a consulta faça sentido.

**Recursos envolvidos:** Workgroups, consultas, catálogo e local de resultados.

**Decisões que precisam ser tomadas:** Dados, schema, formato, permissão e configurações do workgroup.

**Outra situação comentada:** Consultar logs S3 eventualmente: Athena com catálogo/resultado autorizados.

**Por que não concluir mais do que isso:** Não é banco OLTP nem deixa leitura de todo arquivo gratuita; otimizar leitura pode reduzir custo

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Consultar arquivos no S3 com SQL padrão, sem infraestrutura."

**Resposta curta:** Athena.

**Pergunta:** "Como o Athena é cobrado?"

**Resposta curta:** Por volume de dados escaneados.

**Pergunta:** "Reduzir custo de consultas no Athena."

**Resposta curta:** Parquet/ORC, compressão e particionamento.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
