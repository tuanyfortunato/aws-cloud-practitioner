# AWS Database Migration Service (DMS) e Schema Conversion Tool (SCT)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa precisa mover dados de um banco e pode também precisar adaptar sua estrutura quando o banco de destino usa outra tecnologia.

**Como este serviço ajuda?** DMS move dados entre fontes e destinos compatíveis, incluindo replicação de mudanças em cenários suportados. SCT ajuda a converter estruturas e identificar adaptações necessárias.

**Exemplo do dia a dia:** A equipe avalia a estrutura de um banco e transfere seus dados para um destino compatível, planejando também a continuidade das alterações.

**O que ele não resolve sozinho?** Mover dados é diferente de converter todas as consultas e regras da aplicação. Conversão automática pode ser incompleta; compatibilidade e testes são essenciais.

**Primeiras palavras para entender:**

- **Schema:** estrutura do banco.
- **Replicação:** manter uma cópia de dados.
- **CDC:** captura de alterações para transferi-las ao destino.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Migração de bancos de dados · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.17 Migração e transferência](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md)
>
> **Em uma frase:** o DMS **move os dados** (com o banco de origem funcionando); o SCT **converte o schema** entre motores diferentes.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Avalie origem, destino e necessidade de conversão da estrutura do banco.

**Passo 2.** Converta o que for suportado e mova dados com o processo compatível, incluindo alterações quando necessário.

**Passo 3.** Teste aplicação e consistência antes da transição. Copiar registros e adaptar consultas são trabalhos diferentes.

## 2. Recursos e opções, com significado

### AWS DMS

| Item | Detalhe |
|---|---|
| **Componentes** | **Endpoints** de origem e destino + **replication instance** (ou **DMS Serverless**) + **tasks**. |
| **Tipos de migração** | **Full load**, **full load + CDC** (*change data capture*: replica mudanças contínuas → mínima indisponibilidade) ou só CDC. |
| **Origens/destinos** | Oracle, SQL Server, MySQL, PostgreSQL, MongoDB, Db2, SAP… → RDS, Aurora, Redshift, DynamoDB, S3, OpenSearch, Kinesis, DocumentDB. |
| **Homogêneas** | Mesmo motor (MySQL → RDS MySQL): só DMS (inclusive *homogeneous data migrations* com ferramentas nativas). |
| **Heterogêneas** | Motores diferentes (Oracle → Aurora PostgreSQL): **SCT/DMS Schema Conversion** + DMS. |
| **Outros usos** | Replicação contínua para análise, consolidação de bancos, DR. |

### AWS SCT e DMS Schema Conversion

Converte **schema, views, stored procedures e funções** entre motores; gera relatório de avaliação (o que converte automaticamente e o que exige trabalho manual).

**SCT:** aplicativo de desktop. **DMS Schema Conversion:** versão gerenciada no console, com assistência de IA generativa.

Também converte schemas de data warehouses (Teradata, Oracle, Netezza → Redshift).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Mover dados é diferente de converter todas as consultas e regras da aplicação. Conversão automática pode ser incompleta; compatibilidade e testes são essenciais.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

DMS: por hora da replication instance (ou DCU no Serverless) + armazenamento + transferência. SCT: gratuito.

## 5. Caso resolvido: ligando as peças

A equipe avalia a estrutura de um banco e transfere seus dados para um destino compatível, planejando também a continuidade das alterações.

**Aplicando a sequência à situação:**

**Etapa 1:** Avalie origem, destino e necessidade de conversão da estrutura do banco.
**Etapa 2:** Converta o que for suportado e mova dados com o processo compatível, incluindo alterações quando necessário.
**Etapa 3:** Teste aplicação e consistência antes da transição. Copiar registros e adaptar consultas são trabalhos diferentes.

**Resultado e responsabilidade:** DMS move dados entre fontes e destinos compatíveis, incluindo replicação de mudanças em cenários suportados. SCT ajuda a converter estruturas e identificar adaptações necessárias.

**Recursos envolvidos:** Endpoints, tarefas de migração/replicação e conversão de esquema.

**Decisões que precisam ser tomadas:** Origem/destino suportados, rede, full load/CDC e mapeamentos.

**Outra situação comentada:** Oracle para PostgreSQL: conversão e avaliação mais DMS, não promessa de compatibilidade total.

**Por que não concluir mais do que isso:** Nem toda função/stored procedure é convertida; CDC exige pré-requisitos da origem

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Migrar um banco sem desligar a aplicação."

**Resposta curta:** DMS (full load + CDC).

**Pergunta:** "Converter um banco Oracle para Aurora PostgreSQL."

**Resposta curta:** SCT + DMS.

**Pergunta:** "Migrar MySQL on-premises para RDS MySQL."

**Resposta curta:** DMS (homogênea, sem SCT).

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) · [AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
