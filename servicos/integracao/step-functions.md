<!-- autoral -->

# AWS Step Functions

> **Categoria:** Integração de aplicações · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** coordena **fluxos de trabalho** de várias etapas, com decisões, novas tentativas e acompanhamento visual de cada execução.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.13 Integração de aplicações](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

Alguns processos da escola têm etapas em ordem e decisões no meio: validar os documentos da matrícula, esperar a aprovação da coordenação, reservar a vaga, cobrar a taxa e, se a cobrança falhar, liberar a vaga. Coordenar isso com código espalhado em várias funções Lambda fica frágil: cada função precisa saber qual é a próxima, e uma falha no meio deixa o processo pela metade.

O Step Functions resolve isso com um **fluxo de trabalho** (*workflow*, também chamado de **máquina de estados**). Cada etapa é um **estado**, e uma etapa de trabalho (estado *Task*) chama um serviço da AWS, como uma função Lambda. O fluxo decide o caminho, repete etapas que falharam e desvia para etapas alternativas, e o console mostra cada **execução** passo a passo. Ele também atende processos longos, inclusive os que esperam uma ação humana.

O limite: o Step Functions coordena, mas não faz o trabalho de cada etapa; quem cobra a taxa é a função ou o serviço chamado. Ele também é a resposta para um processo que passa dos 15 minutos de uma função Lambda ([aula 3.5](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)): várias funções curtas encadeadas num fluxo.

## Como funciona

1. Você define o fluxo na Amazon States Language (um formato JSON) ou desenha no console, no Workflow Studio.
2. Uma **execução** começa com dados de entrada, chamada por uma API, por uma regra do EventBridge ou pelo API Gateway.
3. Cada estado recebe a entrada, faz sua parte e passa a saída para o próximo. Estados de trabalho chamam serviços; estados de controle decidem o caminho, rodam ramos em paralelo, esperam ou encerram.
4. Quando uma etapa falha, o fluxo tenta de novo (*Retry*) ou desvia para um tratamento de erro (*Catch*).
5. O console mostra o estado de cada etapa da execução, com entrada, saída e duração.

## Opções principais

| | Fluxo Standard | Fluxo Express |
|---|---|---|
| Duração máxima | Até 1 ano | Até 5 minutos |
| Execução | Exatamente uma vez: cada etapa roda uma vez, salvo novas tentativas configuradas | Pelo menos uma vez (assíncrono) ou no máximo uma vez (síncrono) |
| Para quê | Processos longos e auditáveis, ações que não podem repetir (cobrar um pagamento), espera por pessoas | Alto volume de eventos curtos, como dados de IoT e processamento de streaming |
| Cobrança | Por transição de estado | Por número de execuções, duração e memória |

O tipo é escolhido na criação e não pode ser mudado depois.

| Estado | O que faz |
|---|---|
| Task | Uma unidade de trabalho: chama um serviço da AWS ou uma API |
| Choice | Escolhe o próximo ramo pela entrada |
| Parallel | Roda ramos diferentes ao mesmo tempo |
| Map | Repete as mesmas etapas para cada item de uma lista |
| Wait | Espera um tempo ou até uma data |
| Pass, Succeed e Fail | Repassa dados, encerra com sucesso ou encerra com falha |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Duração máxima do fluxo Standard | 1 ano | 06/10/2026 |
| Duração máxima do fluxo Express | 5 minutos | 06/10/2026 |
| Transições de estado grátis | 4.000 por mês, sem prazo de validade | 06/10/2026 |

## Como é cobrado

No fluxo Standard, você paga por **transição de estado**, contada cada vez que uma etapa da execução termina, inclusive as novas tentativas. As primeiras 4.000 transições do mês são grátis para clientes novos e antigos, sem prazo para acabar. No fluxo Express, paga pelo número de execuções, pela duração e pela memória usada. Os serviços chamados em cada etapa, como o Lambda, são cobrados à parte.

## Não confundir com

| Serviço | Diferença para o Step Functions | Pista no enunciado |
|---|---|---|
| [Amazon EventBridge](eventbridge.md) | Entrega eventos aos destinos por regras, sem acompanhar um processo de várias etapas | "Reagir quando algo acontece", "agendar" |
| [Amazon SQS](sqs.md) | Guarda mensagens numa fila até um consumidor buscar | "Desacoplar", "absorver picos" |
| [AWS Lambda](../computacao/lambda.md) | Roda uma função curta em resposta a um evento; o Step Functions encadeia várias funções | "Processo com várias funções em ordem", "passa de 15 minutos" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- [Escolher o tipo de fluxo](https://docs.aws.amazon.com/step-functions/latest/dg/choosing-workflow-type.html)
- [Estados do fluxo](https://docs.aws.amazon.com/step-functions/latest/dg/workflow-states.html)
- [Tratamento de erros](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html)
- [Preços do AWS Step Functions](https://aws.amazon.com/step-functions/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
