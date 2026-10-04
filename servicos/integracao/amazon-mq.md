# Amazon MQ

> **Categoria:** Integração de aplicações / message broker · **Domínio:** 3 · **Escopo:** Regional (Multi-AZ opcional) · **Tópico do guia:** [3.18 Serviços menos conhecidos](../../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md)
>
> **Em uma frase:** brokers de mensagens gerenciados **Apache ActiveMQ** e **RabbitMQ**, compatíveis com protocolos padrão.

## Quando usar

- **Migrar aplicações existentes** que já usam ActiveMQ/RabbitMQ e protocolos padrão (**JMS, AMQP, MQTT, STOMP, OpenWire, WebSocket**) **sem reescrever o código**.
- Para aplicações novas na nuvem, a AWS recomenda SQS/SNS (mais escaláveis e simples).

## Destaques

- Instância única ou ativo/standby Multi-AZ (ActiveMQ) / cluster (RabbitMQ); a AWS cuida de patch e manutenção.

## ❓ Perguntas típicas

- "Aplicação usa RabbitMQ e deve migrar sem mudar o código." → Amazon MQ (SQS exigiria reescrever).

## 🔗 Documentação oficial

- [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html)
