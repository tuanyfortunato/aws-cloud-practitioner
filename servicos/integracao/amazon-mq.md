<!-- autoral -->

# Amazon MQ

> **Categoria:** Integração de aplicações / message broker · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** referência
>
> **Em uma frase:** serviço gerenciado de message broker para Apache ActiveMQ Classic e RabbitMQ, para migrar sistemas que já usam esses brokers sem reescrever o código de mensagens.
>
> **Escopo oficial:** ⚪ Não listado · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.13 Integração de aplicações](../../docs/03-tecnologia-e-servicos/13-integracao-de-aplicacoes.md) · [3.18 Serviços menos conhecidos](../../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

O sistema financeiro antigo da rede troca mensagens por um **message broker** (o intermediário que recebe e entrega mensagens entre programas) RabbitMQ, com protocolos padrão do mercado. Trocar tudo por SQS exigiria reescrever o código. O **Amazon MQ** gerencia brokers ActiveMQ Classic e RabbitMQ na AWS. Ele não aparece na lista do exame.

1. Cria-se um broker do Amazon MQ, com ActiveMQ Classic ou RabbitMQ.
2. As aplicações se conectam com os protocolos padrão que já usam.
3. O Amazon MQ cuida da configuração, da manutenção e das atualizações de versão na janela de manutenção escolhida.
4. O CloudWatch monitora o broker.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [Amazon SQS](sqs.md) | Fila gerenciada da própria AWS, no escopo | "Desacoplar", "fila" |
| [Amazon SNS](sns.md) | Publicar e assinar notificações, no escopo | "Avisar vários assinantes" |
| [Amazon MSK](../analytics/lake-formation-msk-e-outros.md) | Apache Kafka gerenciado, fora do escopo | "Kafka" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html)
- [Serviços no escopo da prova](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
