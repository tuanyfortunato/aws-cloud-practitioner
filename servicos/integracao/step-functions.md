# AWS Step Functions

> **Categoria:** Integração de aplicações / orquestração · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.13 Integração de aplicações](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)
>
> **Em uma frase:** orquestra **fluxos de trabalho de várias etapas** como máquinas de estado visuais, com tratamento de erros e retentativas.

## Conceitos

| Item | Detalhe |
|---|---|
| **State machine** | Definida em JSON (Amazon States Language) ou desenhada no **Workflow Studio**. |
| **Estados** | **Task** (chama serviço), **Choice** (decisão), **Parallel**, **Map** (para cada item — inclusive *distributed map* sobre milhões de objetos do S3), **Wait**, **Pass**, **Succeed**, **Fail**. |
| **Erros** | `Retry` (com backoff) e `Catch` declarativos. |
| **Integrações** | Lambda, ECS/Fargate, Batch, DynamoDB, SNS, SQS, Glue, SageMaker, Bedrock e **200+ serviços via SDK**. |
| **Callback / aprovação humana** | Pausa o fluxo até receber um token (ex.: aprovação por e-mail). |

## Tipos de workflow

| | **Standard** | **Express** |
|---|---|---|
| Duração máxima | Até **1 ano** | Até **5 minutos** |
| Execução | Exatamente uma vez | Pelo menos uma vez |
| Uso | Processos longos, auditáveis, com humanos | Alto volume de eventos (IoT, streaming) |
| Cobrança | Por transição de estado | Por execução, duração e memória |

## ⚠️ Não confundir

- Step Functions (**orquestra** etapas com estado) × EventBridge (**roteia** eventos) × SQS (fila).
- **SWF** (Simple Workflow Service) é o antecessor legado.
- Solução para "processo maior que 15 min com várias Lambdas" → Step Functions encadeando etapas.

## ❓ Perguntas típicas

- "Orquestrar um processo com várias etapas e tratamento de erro." → Step Functions.
- "Fluxo de pedido com aprovação humana no meio." → Step Functions (callback).

## 🔗 Documentação oficial

- [Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
