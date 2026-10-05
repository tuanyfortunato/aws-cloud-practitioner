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

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **origem:** Local de onde uma distribuição obtém conteúdo, como um servidor ou bucket. Uma cópia em cache não elimina toda necessidade de acessar a origem.
- **consistência:** Garantia sobre o que leituras observam após gravações. Não é o mesmo que durabilidade, nem garante que o dado inserido pelo programa está correto.


**Passo 1.** Avalie origem, destino e necessidade de conversão da estrutura do banco.

**Passo 2.** Converta o que for suportado e mova dados com o processo compatível, incluindo alterações quando necessário.

**Passo 3.** Teste aplicação e consistência antes da transição. Copiar registros e adaptar consultas são trabalhos diferentes.

## 2. Recursos e opções, com significado

### AWS DMS

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **Aurora:** Aurora é um banco relacional da AWS dentro da família RDS.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **Redshift:** Redshift é um ambiente de banco voltado à análise de dados, conhecido como data warehouse.
- **DocumentDB:** DocumentDB armazena e consulta documentos, como registros estruturados de produtos.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **replicação:** Manutenção de uma cópia dos dados em outro recurso. Se uma alteração incorreta for replicada, a cópia também pode recebê-la; replicação não substitui todo backup.
- **DR:** Recuperação de desastres: plano para recuperar uma operação depois de uma interrupção grave. Inclui recursos, procedimentos e testes.
- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.
- **schema:** Estrutura e tipos dos dados. Em migração, adaptar a estrutura é uma tarefa diferente de copiar os registros.
- **CDC:** Captura de mudanças nos dados para transferi-las ao destino. É diferente de simplesmente copiar uma tabela uma única vez.
- **SCT:** Ferramenta de conversão de estrutura de banco em migrações compatíveis. Nem toda estrutura ou regra da aplicação é convertida automaticamente.
- **DMS:** Database Migration Service: transferência ou replicação de dados entre bancos compatíveis. Conversão de estrutura e ajuste da aplicação são trabalhos relacionados, mas diferentes.
- **SAP:** Tecnologias e aplicações empresariais do ecossistema SAP. Podem exigir requisitos específicos de memória, licenciamento e operação.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

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

**Antes de ler este trecho:**

- **IA:** Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.


**SCT:** aplicativo de desktop. **DMS Schema Conversion:** versão gerenciada no console, com assistência de IA generativa.


Também converte schemas de data warehouses (Teradata, Oracle, Netezza → Redshift).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Mover dados é diferente de converter todas as consultas e regras da aplicação. Conversão automática pode ser incompleta; compatibilidade e testes são essenciais.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **hora:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.
- **DCU:** Unidade de capacidade em modalidade serverless de migração de dados. Deve ser interpretada segundo a oferta; não é duração da migração.


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

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

A empresa precisa mover dados de um banco e pode também precisar adaptar sua estrutura quando o banco de destino usa outra tecnologia.

**2. O que a solução fornece?**

DMS move dados entre fontes e destinos compatíveis, incluindo replicação de mudanças em cenários suportados. SCT ajuda a converter estruturas e identificar adaptações necessárias.

**3. Que conclusão seria incorreta?**

Mover dados é diferente de converter todas as consultas e regras da aplicação. Conversão automática pode ser incompleta; compatibilidade e testes são essenciais.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Migrar um banco sem desligar a aplicação."

**Resposta curta:** DMS (full load + CDC).


**Fundamento explicado no capítulo:** "Migrar um banco sem desligar a aplicação." → DMS (full load + CDC).

**Pergunta:** "Converter um banco Oracle para Aurora PostgreSQL."

**Resposta curta:** SCT + DMS.


**Fundamento explicado no capítulo:** "Converter um banco Oracle para Aurora PostgreSQL." → SCT + DMS.

**Pergunta:** "Migrar MySQL on-premises para RDS MySQL."

**Resposta curta:** DMS (homogênea, sem SCT).

**Antes de ler este trecho:**

- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.


**Fundamento explicado no capítulo:** "Migrar MySQL on-premises para RDS MySQL." → DMS (homogênea, sem SCT).


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) · [AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
