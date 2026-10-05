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

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.


**Passo 1.** Organize fontes e o modelo de dados para as perguntas analíticas desejadas.

**Passo 2.** Prepare o ambiente e carregue ou disponibilize dados por mecanismos compatíveis. Execute consultas para obter agregações e comparações.

**Passo 3.** Acompanhe qualidade, capacidade e atualização dos dados. A análise histórica não substitui automaticamente o banco de operações da aplicação.

## 2. Recursos e opções, com significado

### Para que serve

**Antes de ler este trecho:**

- **QuickSight:** QuickSight oferece análise visual e painéis a partir de fontes de dados compatíveis.
- **BI:** Análise e apresentação de dados para apoiar decisões. Um painel depende de dados adequados e de uma interpretação correta dos indicadores.


Relatórios de BI, dashboards (QuickSight), análises históricas, consolidação de dados de várias fontes.

### Conceitos e configurações

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **Aurora:** Aurora é um banco relacional da AWS dentro da família RDS.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **Redshift:** Redshift é um ambiente de banco voltado à análise de dados, conhecido como data warehouse.
- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **KMS:** Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **SaaS:** Software como serviço: aplicação pronta disponibilizada para uso. O cliente administra seu uso e seus dados conforme a oferta, em vez de construir o software do zero.
- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.
- **data lake:** Conjunto de dados mantido para usos diversos, frequentemente em armazenamento de objetos. Organização, catálogo e permissões continuam necessários.
- **ML:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.
- **cluster:** Conjunto de recursos que trabalham de forma coordenada. O termo aparece em computação, banco e outras áreas, com papéis diferentes.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.
- **provisionado:** Recurso ou capacidade já disponibilizado para uso. Em algumas cobranças, a disponibilidade mantida importa mesmo sem execução de trabalho de negócio.
- **RA3:** Família de nós Redshift com modelo próprio de computação e armazenamento. Avalie capacidade e modalidade, sem tratar o nome como número de visitantes suportados.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

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

**Antes de ler este trecho:**

- **OLTP:** Processamento de operações individuais do negócio, como registrar uma compra. É diferente de analisar grandes conjuntos históricos de registros.
- **OLAP:** Análise de conjuntos de dados, como comparar vendas de vários meses. Prioriza perguntas e agregações, não apenas registrar uma operação individual.


**Redshift (OLAP)** × **RDS/Aurora (OLTP)**.

**Antes de ler este trecho:**

- **Athena:** Athena permite consultar dados em formatos e fontes compatíveis usando SQL.
- **data warehouse:** Ambiente de dados organizado para análise de grandes conjuntos. O modelo e as consultas são orientados a perguntas analíticas.


**Redshift** (data warehouse sempre disponível) × **Athena** (SQL sob demanda direto no S3, paga por dado escaneado).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **TB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.


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

**Antes de ler este trecho:**

- **transação:** Conjunto de operações tratado com garantias definidas pelo banco. As garantias e limites variam conforme o serviço e a modalidade.


**Outra situação comentada:** Agregar anos de vendas: Redshift; processar cada venda do caixa: banco transacional apropriado.

**Por que não concluir mais do que isso:** Não é a escolha típica de transação individual de aplicação OLTP

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

A empresa quer analisar muitos registros históricos de vendas e comparar períodos, regiões e produtos, sem sobrecarregar o banco que atende as compras.

**2. O que a solução fornece?**

Redshift é um ambiente de banco voltado à análise de dados, conhecido como data warehouse. Você prepara os dados e executa consultas para obter resultados analíticos.

**3. Que conclusão seria incorreta?**

Seu papel principal é análise; ele não deve ser escolhido apenas porque a aplicação precisa salvar um pedido individual. Carregar e organizar dados continua exigindo planejamento.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Data warehouse para relatórios de BI sobre petabytes."

**Resposta curta:** Redshift.


**Fundamento explicado no capítulo:** "Data warehouse para relatórios de BI sobre petabytes." → Redshift.

**Pergunta:** "Consultar dados do S3 junto com o data warehouse."

**Resposta curta:** Redshift Spectrum.


**Fundamento explicado no capítulo:** "Consultar dados do S3 junto com o data warehouse." → Redshift Spectrum.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
