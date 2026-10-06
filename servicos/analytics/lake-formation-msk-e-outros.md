# Lake Formation, MSK, Data Exchange, AppFlow e outros serviços de dados

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Ao trabalhar com muitos dados, a empresa pode precisar controlar acessos, manter fluxos Kafka ou integrar fontes. Esses problemas não são uma só tarefa.

**Como este serviço ajuda?** Esta ficha compara ferramentas: Lake Formation ajuda na governança de um conjunto de dados; MSK fornece Kafka gerenciado; outras opções atendem integração e colaboração em dados.

**Exemplo do dia a dia:** Uma equipe controla acesso a tabelas no seu ambiente de dados. Outra precisa receber eventos de uma aplicação que já usa Kafka; ela avalia MSK.

**O que ele não resolve sozinho?** A família não forma um único serviço intercambiável. Parte dos nomes está fora da prova ou não aparece na lista atual; use o escopo indicado para priorizar.

**Primeiras palavras para entender:**

- **Data lake:** conjunto de dados mantidos para diversos usos.
- **Kafka:** plataforma de fluxo de eventos.
- **Governança:** controle de regras e acessos.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Analytics / dados · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.18 Serviços menos conhecidos](../../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md)
>
> **Em uma frase:** serviços de dados que aparecem como "qual serviço faz X" — saiba a função de cada um.
>
> **Escopo oficial:** 🔀 MSK, AppFlow, Data Exchange, Clean Rooms e DataZone ❌ fora do escopo · Lake Formation ⚪ não listado · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

| Serviço | O que faz | Cenário de prova |
|---|---|---|
| **AWS Lake Formation** | Monta e **governa um data lake no S3** com controle de acesso centralizado e fino (tabela, coluna, linha, tags) sobre o Glue Data Catalog | "Data lake com permissões centralizadas" |
| **Amazon MSK** (Managed Streaming for Apache Kafka) ❌ *fora do escopo* | **Apache Kafka gerenciado** (provisionado ou serverless); MSK Connect para conectores | "Streaming com Kafka sem gerenciar cluster" |
| **AWS Data Exchange** ❌ *fora do escopo* | Encontrar, assinar e usar **conjuntos de dados de terceiros** (mercado financeiro, clima, saúde) | "Comprar dados de mercado para análise" |
| **Amazon AppFlow** ❌ *fora do escopo* | Transfere dados entre **aplicações SaaS** (Salesforce, SAP, Zendesk, Slack) e serviços AWS **sem código** | "Levar dados do Salesforce para o S3" |
| **AWS Clean Rooms** ❌ *fora do escopo* | Colaborar/analisar dados com parceiros **sem compartilhar os dados brutos** | "Análise conjunta preservando privacidade" |
| **Amazon DataZone / SageMaker Unified Studio** ❌ *fora do escopo* | Catálogo e governança de dados para descoberta e compartilhamento entre times | "Portal de dados corporativo" |
| **Amazon Managed Service for Apache Flink** | Processamento de streams com Flink | "Agregações em tempo real" |
| **AWS Data Pipeline** | Orquestração de dados legada | Fechado a novos clientes — não estudar |

## 1. A sequência de funcionamento

**Passo 1.** Separe a necessidade de governar dados da necessidade de fluxos Kafka ou integrações especializadas.

**Passo 2.** Avalie o produto específico e prepare suas fontes, identidades e destinos compatíveis.

**Passo 3.** Confira o resultado e a oferta atual. A categoria reúne ferramentas distintas, não uma solução única.

## 2. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

A família não forma um único serviço intercambiável. Parte dos nomes está fora da prova ou não aparece na lista atual; use o escopo indicado para priorizar.

## 3. Caso resolvido: ligando as peças

Uma equipe controla acesso a tabelas no seu ambiente de dados. Outra precisa receber eventos de uma aplicação que já usa Kafka; ela avalia MSK.

**Aplicando a sequência à situação:**

**Etapa 1:** Separe a necessidade de governar dados da necessidade de fluxos Kafka ou integrações especializadas.
**Etapa 2:** Avalie o produto específico e prepare suas fontes, identidades e destinos compatíveis.
**Etapa 3:** Confira o resultado e a oferta atual. A categoria reúne ferramentas distintas, não uma solução única.

**Resultado e responsabilidade:** Esta ficha compara ferramentas: Lake Formation ajuda na governança de um conjunto de dados; MSK fornece Kafka gerenciado; outras opções atendem integração e colaboração em dados.

**Recursos envolvidos:** Governança de lake, brokers Kafka e serviços de troca/integração de dados.

**Decisões que precisam ser tomadas:** Requisito e status individual no escopo.

**Outra situação comentada:** Kafka gerenciado é MSK; streaming no foco CLF-C02 inclui Kinesis. Compatibilidade Kafka é requisito diferente.

**Por que não concluir mais do que isso:** Vários nomes estão fora do escopo; não generalize capacidades/autorizações entre produtos

## 4. Revisão e perguntas

### ❓ Perguntas típicas

> ⚠️ MSK, AppFlow, Data Exchange, Clean Rooms e DataZone estão **fora do escopo** da prova: se aparecerem como alternativa, desconfie. A resposta no escopo costuma ser outra (ex.: streaming → **Kinesis**; ETL → **Glue**; SQL no S3 → **Athena**).
**Pergunta:** "Criar um data lake no S3 com permissões centralizadas por tabela e coluna."

**Resposta curta:** Lake Formation.

**Pergunta:** "Usar Apache Kafka sem gerenciar o cluster."

**Resposta curta:** Amazon MSK.

**Pergunta:** "Assinar conjuntos de dados de terceiros."

**Resposta curta:** AWS Data Exchange.

**Pergunta:** "Levar dados do Salesforce para o S3 sem código."

**Resposta curta:** Amazon AppFlow.

**Pergunta:** "Analisar dados com um parceiro sem compartilhar os dados brutos."

**Resposta curta:** AWS Clean Rooms.

## 5. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) · [MSK](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html) · [Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/what-is.html) · [AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/what-is-appflow.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
