# AWS Step Functions

> **Categoria:** Integração de aplicações / orquestração · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.13 Integração de aplicações](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)
>
> **Em uma frase:** orquestra **fluxos de trabalho de várias etapas** como máquinas de estado visuais, com tratamento de erros e retentativas.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é um **fluxograma que se executa sozinho**: passo 1, depois o 2; se der erro, tenta de novo; se precisar, espera aprovação.

- ✅ **Escolha quando:** precisa **orquestrar processos de várias etapas** com tratamento de erro.
- 🚫 **Não é a resposta quando:** precisa só **reagir a um evento** → [EventBridge](eventbridge.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "orquestrar", "workflow", "várias etapas", "aprovação humana".
<!-- didatico:fim -->

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | State machine, states, execution e integrações |
| **O que você decide/configura?** | Sequência, branches, retries, catches e modalidade |
| **Em que ordem as coisas acontecem?** | Execução percorre etapas e trata resultados/falhas conforme definição |
| **O que pode fazer, e em que condição?** | Coordena processos com estado e chamadas a serviços |
| **O que não pode presumir?** | Não transforma todo código longo numa única função convencional sem limite |

**Caso comentado:** Pedido exige validar, cobrar e confirmar: fluxo coordena etapas; cada tarefa mantém seus próprios limites.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
