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

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.


**Passo 1.** Identifique a fonte compatível e descreva a estrutura dos dados.

**Passo 2.** Escreva uma consulta para responder a uma pergunta concreta e execute-a sobre os dados necessários.

**Passo 3.** Leia o resultado e examine o volume consultado. Dados mal interpretados não se tornam corretos só porque a consulta executou.

## 2. Recursos e opções, com significado

### Para que serve

**Antes de ler este trecho:**

- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **CloudFront:** CloudFront distribui conteúdo por uma rede de pontos de presença.
- **CloudTrail:** Registro de atividades e chamadas AWS compatíveis. Ajuda a analisar quem realizou uma operação, em vez de medir sozinho a velocidade da aplicação.
- **ALB:** Modalidades de balanceador com focos diferentes: aplicação, transporte de rede e integração de equipamentos virtuais. Os protocolos e casos de uso determinam a escolha.
- **data lake:** Conjunto de dados mantido para usos diversos, frequentemente em armazenamento de objetos. Organização, catálogo e permissões continuam necessários.


Analisar logs (CloudTrail, ALB, VPC Flow Logs, CloudFront) e dados do data lake sem carregar em banco.

**Antes de ler este trecho:**

- **QuickSight:** QuickSight oferece análise visual e painéis a partir de fontes de dados compatíveis.
- **CUR:** Relatório de custos e uso. Ele ajuda a analisar consumo registrado; é diferente de uma estimativa antes de criar recursos.


Consultas ad hoc, exploração de dados, relatórios com QuickSight, análise do CUR.

### Conceitos e configurações

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **Redshift:** Redshift é um ambiente de banco voltado à análise de dados, conhecido como data warehouse.
- **Athena:** Athena permite consultar dados em formatos e fontes compatíveis usando SQL.
- **AWS Glue / Glue:** Glue oferece catálogo e ferramentas de integração e transformação de dados.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **JSON / CSV / Parquet:** Formatos de dados com estruturas diferentes. O formato influencia como uma ferramenta lê e processa os arquivos; não muda sozinho o significado dos registros.
- **schema:** Estrutura e tipos dos dados. Em migração, adaptar a estrutura é uma tarefa diferente de copiar os registros.
- **bucket:** Recipiente que organiza objetos no S3. A aplicação usa o bucket e a identificação do objeto para pedir operações autorizadas.
- **Apache Spark / Spark:** Ferramenta de processamento de dados. O ambiente pode executar o trabalho distribuído, mas a equipe define o código e valida a transformação.
- **DPU:** Unidade de processamento de determinadas ferramentas de dados, como Glue. Consumo e cobrança dependem do trabalho e da modalidade.
- **ORC:** Formato colunar de dados para ferramentas analíticas compatíveis. A organização física do arquivo é diferente do significado de seus campos.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

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

**Antes de ler este trecho:**

- **EMR:** EMR oferece ambientes gerenciados para frameworks de processamento de dados, com modalidades diferentes de execução.
- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.
- **data warehouse:** Ambiente de dados organizado para análise de grandes conjuntos. O modelo e as consultas são orientados a perguntas analíticas.


Athena (SQL sob demanda no S3) × **Redshift** (data warehouse carregado e sempre disponível) × **Redshift Spectrum** (Redshift lendo o S3) × **EMR** (clusters Spark/Hadoop).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **TB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.


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

**Antes de ler este trecho:**

- **OLTP:** Processamento de operações individuais do negócio, como registrar uma compra. É diferente de analisar grandes conjuntos históricos de registros.


**Outra situação comentada:** Consultar logs S3 eventualmente: Athena com catálogo/resultado autorizados.

**Por que não concluir mais do que isso:** Não é banco OLTP nem deixa leitura de todo arquivo gratuita; otimizar leitura pode reduzir custo

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Há arquivos com dados no S3 e a equipe quer fazer perguntas sobre esse conteúdo sem administrar um servidor de consultas.

**2. O que a solução fornece?**

Athena permite consultar dados em formatos e fontes compatíveis usando SQL. Você precisa descrever ou disponibilizar a estrutura dos dados para que a consulta faça sentido.

**3. Que conclusão seria incorreta?**

Athena não corrige sozinho dados desorganizados nem é o banco transacional do aplicativo. Formato, organização e quantidade de dados consultados influenciam o resultado e o custo.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Consultar arquivos no S3 com SQL padrão, sem infraestrutura."

**Resposta curta:** Athena.


**Fundamento explicado no capítulo:** "Consultar arquivos no S3 com SQL padrão, sem infraestrutura." → Athena.

**Pergunta:** "Como o Athena é cobrado?"

**Resposta curta:** Por volume de dados escaneados.


**Fundamento explicado no capítulo:** "Como o Athena é cobrado?" → Por volume de dados escaneados.

**Pergunta:** "Reduzir custo de consultas no Athena."

**Resposta curta:** Parquet/ORC, compressão e particionamento.


**Fundamento explicado no capítulo:** "Reduzir custo de consultas no Athena." → Parquet/ORC, compressão e particionamento.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
