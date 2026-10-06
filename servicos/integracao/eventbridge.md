<!-- autoral -->

# Amazon EventBridge

> **Categoria:** Integração de aplicações · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** serviço serverless que recebe **eventos** de serviços da AWS, de aplicações próprias e de softwares de terceiros e os entrega aos destinos certos por **regras**.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.13 Integração de aplicações](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

Muita coisa acontece na escola sem que alguém peça: o sistema de pagamento de terceiros aprova a taxa de matrícula, uma instância EC2 para, um arquivo chega ao S3. Cada um desses acontecimentos é um **evento**, e vários sistemas precisam reagir a ele. Ligar cada origem a cada destino com código próprio gera uma teia difícil de manter.

O EventBridge resolve isso com um **barramento de eventos** (*event bus*), que recebe os eventos e os entrega aos destinos por **regras**. Uma regra descreve quais eventos interessam (o **padrão de evento**) e para onde mandar (os **destinos**, como uma função Lambda ou um fluxo do Step Functions). Quem emite o evento não precisa saber quem vai reagir: é a **arquitetura orientada a eventos**, uma forma de acoplamento fraco.

O limite: o EventBridge entrega o evento, mas não faz o trabalho; quem confirma a vaga é a função Lambda acionada. A explicação completa, com o exemplo do pagamento aprovado, está na [aula 3.13](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md).

## Como funciona

1. Uma **origem** envia um evento ao barramento: um serviço da AWS, uma aplicação própria ou um software de terceiros (parceiro SaaS).
2. O EventBridge compara o evento com as **regras** daquele barramento.
3. Para cada regra cujo padrão o evento atende, o EventBridge entrega o evento aos **destinos** da regra, que rodam em paralelo. Antes de entregar, a regra pode transformar o evento.
4. O destino faz o trabalho: uma função Lambda roda, uma mensagem entra numa fila do SQS, um fluxo do Step Functions começa.

## Opções principais

| Recurso | O que faz | Quando lembrar |
|---|---|---|
| Barramento padrão (*default*) | Existe em toda conta e recebe automaticamente os eventos de mudança de estado dos serviços da AWS | "Quando uma instância EC2 parar, avisar a equipe" |
| Barramento personalizado (*custom*) | Recebe os eventos das suas aplicações | Integrar sistemas próprios por eventos |
| Barramento de parceiro (*partner*) | Recebe eventos de softwares de terceiros integrados ao EventBridge | "Reagir a um evento de um SaaS" |
| EventBridge Scheduler | Agendador serverless: tarefas recorrentes (expressões cron e rate) ou únicas, com novas tentativas | "Rodar um relatório toda noite"; substitui as antigas regras agendadas |
| EventBridge Pipes | Liga uma origem a um destino, ponto a ponto, com filtro e enriquecimento no caminho | Integração de uma origem com um destino, sem código de ligação |
| Arquivo e replay | Guarda eventos e os reenvia ao barramento depois | Recuperar de um erro ou testar uma funcionalidade nova |

Em setembro de 2026, a AWS lançou um barramento personalizado novo, em que cada consumidor cria seus próprios **assinantes**, e o barramento guarda os eventos por um período definido, com entrega em ordem e replay. O barramento com regras passou a se chamar *Custom Event Bus - Classic* e continua disponível.

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Eventos de gerenciamento da AWS recebidos no barramento (Classic) | Grátis | 06/10/2026 |
| Invocações grátis do Scheduler | 14 milhões por mês | 06/10/2026 |
| Serviços que o Scheduler aciona | Mais de 270 serviços da AWS | 06/10/2026 |

## Como é cobrado

No barramento com regras (Classic), os eventos de gerenciamento que os serviços da AWS enviam são recebidos de graça; eventos próprios, de parceiros e eventos de dados que você ativa (como os do S3) são cobrados por milhão. Entregar a um serviço na mesma conta é grátis; entregar a outro barramento ou a outra conta é cobrado. Cada pedaço de 64 KB do evento conta como um evento.

O barramento personalizado novo cobra pelo volume de dados recebidos e entregues, com 24 horas de armazenamento incluídas. O Scheduler cobra por invocação depois das 14 milhões grátis do mês; o Pipes cobra pelas requisições que passam pelo filtro; o arquivo de eventos também é cobrado. Não há taxa mínima.

## Não confundir com

| Serviço | Diferença para o EventBridge | Pista no enunciado |
|---|---|---|
| [Amazon SNS](sns.md) | Publica num tópico e empurra para todos os assinantes, inclusive pessoas por e-mail e SMS | "Notificar a equipe", "alerta por SMS" |
| [Amazon SQS](sqs.md) | Guarda mensagens numa fila até um consumidor buscar | "Absorver picos", "processar no próprio ritmo" |
| [AWS Step Functions](step-functions.md) | Coordena as etapas de um processo em ordem, com decisões e novas tentativas | "Fluxo de várias etapas", "esperar aprovação" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
- [Barramento padrão e Classic](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html)
- [Barramento personalizado novo](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus.html)
- [Regras](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html)
- [EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html)
- [EventBridge Pipes](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html)
- [Arquivo e replay](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-archive.html)
- [Preços do Amazon EventBridge](https://aws.amazon.com/eventbridge/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
