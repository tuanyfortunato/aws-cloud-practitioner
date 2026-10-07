<!-- autoral -->

# Amazon Kinesis e Amazon Data Firehose

> **Categoria:** Analytics e dados em tempo real · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** o Kinesis Data Streams coleta e guarda por um tempo fluxos de dados para aplicações processarem em tempo real; o Data Firehose entrega fluxos a destinos como S3 e Redshift sem aplicação para escrever.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

No primeiro dia de inscrições, a coordenação quer ver ao vivo quantas pessoas estão preenchendo o formulário de matrícula e em que etapa desistem. Cada clique é um registro pequeno, e chegam milhares por minuto. Esperar o relatório do fim do dia não serve.

Um **fluxo de dados** (*streaming*) é essa sequência contínua de registros. O **Kinesis Data Streams** recebe o fluxo e guarda os registros em ordem por um período (24 horas por padrão, até 365 dias), para que uma ou mais aplicações os leiam e reajam enquanto chegam, como o painel ao vivo da coordenação. O **Data Firehose** (antes Kinesis Data Firehose) cuida de outra parte: entregar o fluxo a um destino, como S3, Redshift, OpenSearch Service ou Splunk, sem que você escreva a aplicação que lê. O **Kinesis Video Streams** faz o mesmo papel para vídeo ao vivo de dispositivos.

O limite: o Data Streams guarda e distribui os registros, mas o processamento é da aplicação que lê. E o Firehose entrega, mas não é lugar de análise; a consulta acontece depois, no destino, com ferramentas como o [Athena](athena.md).

## Como funciona

1. O site envia cada clique como um registro para um fluxo do Kinesis Data Streams.
2. O fluxo guarda os registros em ordem pelo período de retenção e escala sozinho no modo sob demanda, ou pela capacidade escolhida no modo provisionado.
3. Uma aplicação lê o fluxo e atualiza o painel ao vivo; outra pode ler os mesmos registros para outro fim.
4. Um fluxo do Data Firehose recebe os mesmos eventos e os entrega no S3 para análise posterior.

## Opções principais

| Serviço | O que faz | Exemplo na escola |
|---|---|---|
| Kinesis Data Streams | Recebe e guarda fluxos para processamento em tempo real | Painel ao vivo das inscrições |
| Amazon Data Firehose | Entrega fluxos a S3, Redshift, OpenSearch, Splunk e outros | Guardar os cliques no S3 |
| Kinesis Video Streams | Leva vídeo ao vivo de dispositivos para a AWS | Câmeras da portaria |
| Modo sob demanda (Data Streams) | Escala sozinho, sem planejar capacidade | Pico imprevisível do primeiro dia |
| Modo provisionado (Data Streams) | Capacidade definida por você | Volume estável e conhecido |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Retenção padrão do Data Streams | 24 horas | 06/10/2026 |
| Retenção máxima do Data Streams | 365 dias | 06/10/2026 |
| Cobrança do Data Firehose | Pelo volume de dados recebidos, sem taxa inicial | 06/10/2026 |

## Como é cobrado

No Data Streams sob demanda, paga-se pelo volume de dados gravados e lidos e por hora de cada fluxo; retenção estendida (além de 24 horas) e longa (além de sete dias) são cobradas à parte. No Data Firehose, paga-se pelo volume recebido, mais recursos opcionais como conversão de formato e partição dinâmica.

## Não confundir com

| Serviço | Diferença para o Kinesis | Pista no enunciado |
|---|---|---|
| [Amazon SQS](../integracao/sqs.md) | Fila de mensagens entre partes de uma aplicação | "Desacoplar", "fila" |
| [Amazon EventBridge](../integracao/eventbridge.md) | Roteia eventos entre serviços por regras | "Reagir a um evento" |
| [AWS Glue](glue.md) | ETL de dados já guardados | "Preparar dados", "catálogo" |
| [Amazon Athena](athena.md) | Consulta os dados depois de guardados | "SQL no S3" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)
- [Conceitos do Data Streams](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html)
- [Modos de capacidade](https://docs.aws.amazon.com/streams/latest/dev/how-do-i-size-a-stream.html)
- [O que é o Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)
- [O que é o Kinesis Video Streams](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html)
- [Preços do Data Streams](https://aws.amazon.com/kinesis/data-streams/pricing/) e [do Data Firehose](https://aws.amazon.com/firehose/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
