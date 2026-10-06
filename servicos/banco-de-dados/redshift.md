# Amazon Redshift

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa quer analisar muitos registros históricos de vendas e comparar períodos, regiões e produtos, sem sobrecarregar o banco que atende as compras.

**Como este serviço ajuda?** Redshift é um ambiente de banco voltado à análise de dados, conhecido como data warehouse. Você prepara os dados e executa consultas para obter resultados analíticos.

**Exemplo do dia a dia:** Uma loja reúne seu histórico de vendas e consulta o total vendido por mês e categoria no Redshift.

**O que ele não resolve sozinho?** Seu papel principal é análise; ele não deve ser escolhido apenas porque a aplicação precisa salvar um pedido individual. Carregar e organizar dados continua exigindo planejamento.

**Primeiras palavras para entender:**

- **Data warehouse:** banco organizado para análise.
- **Analítico:** voltado a padrões e agregações.
- **SQL:** linguagem para consultar dados.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Data warehouse · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) · [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)
>
> **Em uma frase:** data warehouse colunar e massivamente paralelo (MPP) para análises SQL (OLAP) sobre terabytes a petabytes.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Organize fontes e o modelo de dados para as perguntas analíticas desejadas.

**Passo 2.** Prepare o ambiente e carregue ou disponibilize dados por mecanismos compatíveis. Execute consultas para obter agregações e comparações.

**Passo 3.** Acompanhe qualidade, capacidade e atualização dos dados. A análise histórica não substitui automaticamente o banco de operações da aplicação.

## 2. Recursos e opções, com significado

### Para que serve

Relatórios de BI, dashboards (QuickSight), análises históricas, consolidação de dados de várias fontes.

### Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Armazenamento colunar + compressão** | Consultas analíticas rápidas lendo só as colunas necessárias. |
| **Cluster provisionado** | Nó líder + nós de computação; **RA3** separa computação de armazenamento gerenciado (S3). |
| **Redshift Serverless** | Sem gerenciar cluster; paga por RPU-hora usada. |
| **Redshift Spectrum** | Consulta dados **direto no S3** (data lake) junto com tabelas locais. |
| **Concurrency scaling** | Capacidade extra temporária em picos de consultas. |
| **Data sharing** | Compartilha dados entre clusters/contas sem copiar. |
| **Zero-ETL** | Integra Aurora, RDS, DynamoDB e aplicações SaaS quase em tempo real. |
| **Redshift ML** | Cria modelos (SageMaker) com SQL. |
| **Segurança** | VPC, criptografia KMS, auditoria, controle por coluna/linha. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Seu papel principal é análise; ele não deve ser escolhido apenas porque a aplicação precisa salvar um pedido individual. Carregar e organizar dados continua exigindo planejamento.

### ⚠️ Pegadinhas e não confundir

**Redshift (OLAP)** × **RDS/Aurora (OLTP)**.

**Redshift** (data warehouse sempre disponível) × **Athena** (SQL sob demanda direto no S3, paga por dado escaneado).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Nó-hora (ou nós reservados) ou RPU-hora (Serverless) + armazenamento gerenciado + Spectrum por TB escaneado.

## 5. Caso resolvido: ligando as peças

Uma loja reúne seu histórico de vendas e consulta o total vendido por mês e categoria no Redshift.

**Aplicando a sequência à situação:**

**Etapa 1:** Organize fontes e o modelo de dados para as perguntas analíticas desejadas.
**Etapa 2:** Prepare o ambiente e carregue ou disponibilize dados por mecanismos compatíveis. Execute consultas para obter agregações e comparações.
**Etapa 3:** Acompanhe qualidade, capacidade e atualização dos dados. A análise histórica não substitui automaticamente o banco de operações da aplicação.

**Resultado e responsabilidade:** Redshift é um ambiente de banco voltado à análise de dados, conhecido como data warehouse. Você prepara os dados e executa consultas para obter resultados analíticos.

**Recursos envolvidos:** Warehouse, tabelas, endpoints e modalidades provisionada/serverless.

**Decisões que precisam ser tomadas:** Capacidade, dados, acesso e carregamento/consulta.

**Outra situação comentada:** Agregar anos de vendas: Redshift; processar cada venda do caixa: banco transacional apropriado.

**Por que não concluir mais do que isso:** Não é a escolha típica de transação individual de aplicação OLTP

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Data warehouse para relatórios de BI sobre petabytes."

**Resposta curta:** Redshift.

**Pergunta:** "Consultar dados do S3 junto com o data warehouse."

**Resposta curta:** Redshift Spectrum.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
