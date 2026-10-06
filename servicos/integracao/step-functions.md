# AWS Step Functions

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Um processo tem várias etapas, algumas decisões e possibilidade de falha. Controlar toda essa sequência dentro de um único programa pode dificultar o acompanhamento.

**Como este serviço ajuda?** Step Functions coordena fluxos de trabalho entre etapas e serviços compatíveis. Você define a sequência, as decisões e o comportamento diante de falhas.

**Exemplo do dia a dia:** Uma matrícula passa por verificação, cobrança e confirmação. O fluxo coordena essas tarefas e registra o estado de cada execução.

**O que ele não resolve sozinho?** O serviço coordena as etapas; ele não escreve automaticamente o código que cobra ou verifica os dados. As etapas precisam existir e ter acessos configurados.

**Primeiras palavras para entender:**

- **Workflow:** fluxo de trabalho.
- **Estado:** etapa ou condição da execução.
- **Retry:** nova tentativa após determinada falha.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Integração de aplicações / orquestração · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.13 Integração de aplicações](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)
>
> **Em uma frase:** orquestra **fluxos de trabalho de várias etapas** como máquinas de estado visuais, com tratamento de erros e retentativas.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Descreva etapas, decisões e tratamento de falhas do processo.

**Passo 2.** Inicie uma execução com seus dados de entrada. O fluxo coordena as etapas e os componentes que realizam as tarefas.

**Passo 3.** Examine estado e resultado da execução. A coordenação não escreve automaticamente o código de cada tarefa.

## 2. Recursos e opções, com significado

### Conceitos

| Item | Detalhe |
|---|---|
| **State machine** | Definida em JSON (Amazon States Language) ou desenhada no **Workflow Studio**. |
| **Estados** | **Task** (chama serviço), **Choice** (decisão), **Parallel**, **Map** (para cada item — inclusive *distributed map* sobre milhões de objetos do S3), **Wait**, **Pass**, **Succeed**, **Fail**. |
| **Erros** | `Retry` (com backoff) e `Catch` declarativos. |
| **Integrações** | Lambda, ECS/Fargate, Batch, DynamoDB, SNS, SQS, Glue, SageMaker, Bedrock e **200+ serviços via SDK**. |
| **Callback / aprovação humana** | Pausa o fluxo até receber um token (ex.: aprovação por e-mail). |

### Tipos de workflow

| | **Standard** | **Express** |
|---|---|---|
| Duração máxima | Até **1 ano** | Até **5 minutos** |
| Execução | Exatamente uma vez | Pelo menos uma vez |
| Uso | Processos longos, auditáveis, com humanos | Alto volume de eventos (IoT, streaming) |
| Cobrança | Por transição de estado | Por execução, duração e memória |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

O serviço coordena as etapas; ele não escreve automaticamente o código que cobra ou verifica os dados. As etapas precisam existir e ter acessos configurados.

### ⚠️ Não confundir

Step Functions (**orquestra** etapas com estado) × EventBridge (**roteia** eventos) × SQS (fila).

**SWF** (Simple Workflow Service) é o antecessor legado.

Solução para "processo maior que 15 min com várias Lambdas" → Step Functions encadeando etapas.

## 4. Caso resolvido: ligando as peças

Uma matrícula passa por verificação, cobrança e confirmação. O fluxo coordena essas tarefas e registra o estado de cada execução.

**Aplicando a sequência à situação:**

**Etapa 1:** Descreva etapas, decisões e tratamento de falhas do processo.
**Etapa 2:** Inicie uma execução com seus dados de entrada. O fluxo coordena as etapas e os componentes que realizam as tarefas.
**Etapa 3:** Examine estado e resultado da execução. A coordenação não escreve automaticamente o código de cada tarefa.

**Resultado e responsabilidade:** Step Functions coordena fluxos de trabalho entre etapas e serviços compatíveis. Você define a sequência, as decisões e o comportamento diante de falhas.

**Recursos envolvidos:** State machine, states, execution e integrações.

**Decisões que precisam ser tomadas:** Sequência, branches, retries, catches e modalidade.

**Outra situação comentada:** Pedido exige validar, cobrar e confirmar: fluxo coordena etapas; cada tarefa mantém seus próprios limites.

**Por que não concluir mais do que isso:** Não transforma todo código longo numa única função convencional sem limite

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Orquestrar um processo com várias etapas e tratamento de erro."

**Resposta curta:** Step Functions.

**Pergunta:** "Fluxo de pedido com aprovação humana no meio."

**Resposta curta:** Step Functions (callback).

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
