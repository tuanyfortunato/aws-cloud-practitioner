# Amazon QuickSight (Amazon Quick Sight)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Há resultados e tabelas, mas as pessoas do negócio precisam enxergar indicadores em gráficos e painéis, sem ler dados brutos.

**Como este serviço ajuda?** QuickSight oferece análise visual e painéis a partir de fontes de dados compatíveis. Você prepara as conexões, os conjuntos de dados e as visualizações.

**Exemplo do dia a dia:** A escola cria um painel com matrículas por curso e período para a equipe administrativa acompanhar a demanda.

**O que ele não resolve sozinho?** O painel não coleta nem corrige automaticamente qualquer dado. Permissões, qualidade e atualização dos dados precisam ser planejadas.

**Primeiras palavras para entender:**

- **BI:** análise de dados para apoiar decisões.
- **Dashboard:** painel de indicadores.
- **Visualização:** gráfico ou outra representação dos dados.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Analytics / BI · **Domínio:** 3 · **Escopo:** Regional (conta) · **Tópico do guia:** [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)
>
> **Em uma frase:** BI **serverless** para criar dashboards e relatórios interativos, inclusive com perguntas em linguagem natural.
>
> **Escopo oficial:** ✅ No escopo (como Amazon Quick Sight) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Conecte uma fonte compatível e prepare um conjunto de dados com significado definido.

**Passo 2.** Crie visualizações que respondam às perguntas desejadas e controle quem pode vê-las.

**Passo 3.** Confira atualização e interpretação dos indicadores. Uma visualização bonita não garante um resultado correto.

## 2. Recursos e opções, com significado

### Destaques

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **Aurora:** Aurora é um banco relacional da AWS dentro da família RDS.
- **Redshift:** Redshift é um ambiente de banco voltado à análise de dados, conhecido como data warehouse.
- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **IAM Identity Center:** Serviço de acesso central para a força de trabalho. Atribuições de contas e aplicações não são o cadastro de clientes de um aplicativo.
- **Athena:** Athena permite consultar dados em formatos e fontes compatíveis usando SQL.
- **QuickSight:** QuickSight oferece análise visual e painéis a partir de fontes de dados compatíveis.
- **Amazon Q / Q:** A família Amazon Q inclui assistentes com funções diferentes: Q Developer apoia desenvolvimento; Q Business trabalha com conhecimento corporativo conectado e autorizado.
- **IA:** Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.
- **memória:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.
- **SPICE:** Mecanismo de dados do QuickSight para consultas e visualizações. Conservação e atualização do conjunto precisam ser planejadas.

| Item | Detalhe |
|---|---|
| **Fontes** | S3 (via Athena), Redshift, RDS/Aurora, OpenSearch, Snowflake, Salesforce, arquivos, entre outras. |
| **SPICE** | Motor **em memória** que acelera as análises e reduz consultas à fonte. |
| **Dashboards e análises** | Visualizações interativas, filtros, drill-down, relatórios paginados, alertas. |
| **IA generativa (Amazon Q in QuickSight)** | Perguntas em linguagem natural, histórias de dados, criação assistida de visuais. |
| **Embedding** | Dashboards dentro de aplicações. |
| **Segurança** | Integração com IAM Identity Center, segurança em nível de linha/coluna. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

O painel não coleta nem corrige automaticamente qualquer dado. Permissões, qualidade e atualização dos dados precisam ser planejadas.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.

Por usuário (autores, leitores) — leitores podem ser **por sessão**; capacidade SPICE adicional.

### 🔄 Atualizações 2025-2026

**Antes de ler este trecho:**

- **BI:** Análise e apresentação de dados para apoiar decisões. Um painel depende de dados adequados e de uma interpretação correta dos indicadores.

Nomes: Amazon QuickSight → **Amazon Quick Suite** → hoje **"Amazon Quick"**. A parte de BI continua como **Amazon Quick Sight**, nome usado no exam guide e na lista de serviços. Na prova pode aparecer também "QuickSight".

## 5. Caso resolvido: ligando as peças

A escola cria um painel com matrículas por curso e período para a equipe administrativa acompanhar a demanda.

**Aplicando a sequência à situação:**

**Etapa 1:** Conecte uma fonte compatível e prepare um conjunto de dados com significado definido.
**Etapa 2:** Crie visualizações que respondam às perguntas desejadas e controle quem pode vê-las.
**Etapa 3:** Confira atualização e interpretação dos indicadores. Uma visualização bonita não garante um resultado correto.

**Resultado e responsabilidade:** QuickSight oferece análise visual e painéis a partir de fontes de dados compatíveis. Você prepara as conexões, os conjuntos de dados e as visualizações.

**Recursos envolvidos:** Data sources, datasets, analyses e dashboards.

**Decisões que precisam ser tomadas:** Conexão, atualização, permissões e compartilhamento.

**Antes de ler este trecho:**

- **ETL:** Extrair dados de uma fonte, transformá-los e carregá-los num destino. A regra de transformação deve ser definida de acordo com o significado dos dados.

**Outra situação comentada:** Gerentes precisam gráficos de vendas: Quick Sight sobre uma fonte preparada.

**Por que não concluir mais do que isso:** Não é ferramenta principal de ETL nem acesso irrestrito de qualquer usuário

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Criar dashboards interativos de BI para executivos."

**Resposta curta:** QuickSight.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
