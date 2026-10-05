# Amazon MQ

> **Categoria:** Integração de aplicações / message broker · **Domínio:** 3 · **Escopo:** Regional (Multi-AZ opcional) · **Tópico do guia:** [3.18 Serviços menos conhecidos](../../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md)
>
> **Em uma frase:** brokers de mensagens gerenciados **Apache ActiveMQ** e **RabbitMQ**, compatíveis com protocolos padrão.
>
> **Escopo oficial:** ⚪ Não listado · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é o **mesmo carteiro** (ActiveMQ ou RabbitMQ) que a aplicação já usa, só que gerenciado pela AWS.

- ✅ **Escolha quando:** precisa **migrar aplicações que já usam brokers padrão** sem reescrever o código.
- 🚫 **Não é a resposta quando:** a aplicação é **nova, feita para a nuvem** → [SQS](sqs.md) e [SNS](sns.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "RabbitMQ", "ActiveMQ", "sem mudar o código".
<!-- didatico:fim -->

## Quando usar

- **Migrar aplicações existentes** que já usam ActiveMQ/RabbitMQ e protocolos padrão (**JMS, AMQP, MQTT, STOMP, OpenWire, WebSocket**) **sem reescrever o código**.
- Para aplicações novas na nuvem, a AWS recomenda SQS/SNS (mais escaláveis e simples).

## Destaques

- Instância única ou ativo/standby Multi-AZ (ActiveMQ) / cluster (RabbitMQ); a AWS cuida de patch e manutenção.

## ❓ Perguntas típicas

- "Aplicação usa RabbitMQ e deve migrar sem mudar o código." → Amazon MQ (SQS exigiria reescrever).

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Broker, filas/tópicos e engines/protocolos compatíveis |
| **O que você decide/configura?** | ActiveMQ/RabbitMQ, capacidade, rede e acesso |
| **Em que ordem as coisas acontecem?** | Clientes usam protocolo compatível e broker gerenciado |
| **O que pode fazer, e em que condição?** | Ajuda migração de sistemas dependentes de brokers tradicionais |
| **O que não pode presumir?** | Não listado não é exclusão formal; escolha por compatibilidade, sem igualar a API SQS |

**Caso comentado:** Aplicação exige protocolo de broker existente: avalie MQ; nova fila AWS simples: SQS.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html)
