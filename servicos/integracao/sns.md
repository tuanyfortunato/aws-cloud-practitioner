<!-- autoral -->

# Amazon SNS (Simple Notification Service)

> **Categoria:** Integração de aplicações · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** serviço de **publicar e assinar**: o publicador envia a mensagem a um **tópico**, e o SNS a empurra para todos os assinantes.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.13 Integração de aplicações](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md) · base em [0.4 Como programas conversam](../../docs/fundamentos/04-api-e-filas.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

Uma matrícula nova interessa a vários sistemas ao mesmo tempo: o gerador de comprovantes, o financeiro, a secretaria da unidade e a equipe que recebe um e-mail de aviso. Se o site da escola tiver de chamar cada um deles, toda vez que surgir um interessado novo alguém precisa mudar o código do site.

O SNS resolve isso com um **tópico**, um canal de comunicação. O site publica a mensagem uma vez no tópico, e o SNS entrega uma cópia a cada **assinante**. Assinantes podem ser aplicações, como filas do SQS e funções Lambda, ou pessoas, por e-mail, SMS e notificação no celular. Por isso o SNS é a resposta da prova para **alertas e notificações**.

O limite: o SNS empurra a mensagem na hora e não a guarda para um consumidor buscar depois. Se o assinante estiver fora do ar, as tentativas de entrega acabam e a mensagem é descartada, a menos que a assinatura tenha uma fila de mensagens mortas. Para que cada sistema processe no seu ritmo sem perder mensagens, assine filas do SQS no tópico (o padrão fan-out, na [aula 3.13](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md)).

## Como funciona

1. Você cria um **tópico** e inscreve nele os **assinantes**. E-mails, endpoints HTTP(S) e recursos de outras contas precisam confirmar a assinatura antes de receber.
2. O **publicador** envia uma mensagem ao tópico.
3. O SNS compara a mensagem com a **política de filtro** de cada assinatura. Sem filtro, o assinante recebe tudo.
4. O SNS empurra uma cópia para cada assinante que passou no filtro e tenta de novo quando a entrega falha.
5. Mensagens que esgotam as tentativas vão para a **fila de mensagens mortas** da assinatura, uma fila do SQS, se houver uma configurada. Sem ela, são descartadas.

## Opções principais

| | Tópico padrão (Standard) | Tópico FIFO |
|---|---|---|
| Ordem e repetição | Sem garantia de ordem; a mesma mensagem pode chegar mais de uma vez | Ordem e deduplicação, com filas FIFO do SQS como assinantes |
| Assinantes | SQS, Lambda, HTTP(S), e-mail, SMS, push para celular, Amazon Data Firehose e provedores parceiros | Só filas do SQS (FIFO ou padrão); não entrega para e-mail, SMS, celular ou HTTP(S) |
| Nome | Livre | Termina em `.fifo` |
| Quando usar | Notificar pessoas e muitos sistemas | Manter a ordem dos eventos entre sistemas, como mudanças de preço |

| Recurso | O que faz | Quando lembrar |
|---|---|---|
| Fan-out (SNS + SQS) | Cada mensagem do tópico é copiada para várias filas, e cada fila alimenta um sistema | Vários sistemas processam a mesma mensagem em paralelo, cada um no seu ritmo |
| Política de filtro | Cada assinatura recebe só as mensagens que atendem às condições, pelos atributos ou pelo corpo | Assinantes interessados em tipos diferentes de mensagem |
| A2A e A2P | Entrega de aplicação para aplicação (SQS, Lambda, HTTP) ou de aplicação para pessoa (e-mail, SMS, push) | "Avisar a equipe por e-mail ou SMS" |
| Fila de mensagens mortas | Guarda numa fila do SQS as mensagens que não foram entregues | Não perder mensagens de assinantes com falha |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Tamanho da mensagem | 256 KiB por padrão; até 1 MiB configurando o atributo `MaximumMessageSize` do tópico | 06/10/2026 |
| Tópico acima de 256 KiB | Só assinantes SQS, Lambda e Firehose, até 100 assinaturas | 06/10/2026 |
| Requisições grátis | 1 milhão por mês | 06/10/2026 |

## Como é cobrado

No tópico padrão, você paga pelas **requisições** à API (publicações e operações no tópico) e pelas **entregas**, com preço por tipo de destino. O primeiro milhão de requisições por mês é grátis, e cada destino tem sua franquia mensal: 1 milhão de notificações push, 100 mil entregas HTTP(S) e mil e-mails. Entregar para filas do SQS e funções Lambda não tem cobrança do SNS; vale o preço do SQS ou do Lambda e a transferência de dados.

Cada pedaço de 64 KB conta como uma requisição na publicação e como uma entrega no envio, exceto SMS: uma mensagem de 1 MiB conta 16 vezes. No tópico FIFO, a cobrança é pelas mensagens publicadas, pelas mensagens de assinatura (mensagens publicadas vezes assinaturas) e pelo volume de dados. Não há taxa mínima.

## Não confundir com

| Serviço | Diferença para o SNS | Pista no enunciado |
|---|---|---|
| [Amazon SQS](sqs.md) | Guarda a mensagem até um consumidor buscar, e cada mensagem é processada por um consumidor | "Desacoplar", "absorver picos", "processar no próprio ritmo" |
| [Amazon EventBridge](eventbridge.md) | Roteia eventos por regras e recebe eventos de serviços da AWS e de softwares de terceiros | "Reagir quando algo acontece", "evento de um SaaS" |
| [Amazon SES](../aplicacoes/ses.md) | Plataforma de e-mail para mensagens transacionais e de marketing com os domínios da empresa | "Campanha de e-mail", "boletim para clientes" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)
- [Criar uma assinatura e tipos de destino](https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html)
- [Filtragem de mensagens](https://docs.aws.amazon.com/sns/latest/dg/sns-message-filtering.html)
- [Entrega em tópicos FIFO](https://docs.aws.amazon.com/sns/latest/dg/fifo-message-delivery.html)
- [Filas de mensagens mortas do SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-dead-letter-queues.html)
- [Mensagens grandes](https://docs.aws.amazon.com/sns/latest/dg/large-message-payloads.html)
- [Perguntas frequentes do SNS (ordem e mensagens repetidas)](https://aws.amazon.com/sns/faqs/)
- [Preços do Amazon SNS](https://aws.amazon.com/sns/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
