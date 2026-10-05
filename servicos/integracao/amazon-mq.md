# Amazon MQ

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma aplicação existente já usa um intermediário de mensagens específico, e trocar seu protocolo ou reescrever sua integração seria trabalhoso.

**Como este serviço ajuda?** Amazon MQ oferece brokers gerenciados compatíveis com tecnologias suportadas, como ActiveMQ e RabbitMQ.

**Exemplo do dia a dia:** Uma empresa avalia mover seu broker compatível para Amazon MQ preservando a interface usada por suas aplicações.

**O que ele não resolve sozinho?** Ele não é intercambiável com SQS ou SNS em todas as interfaces. Migração e compatibilidade precisam ser avaliadas; o nome não consta da lista de escopo indicada nesta ficha.

**Primeiras palavras para entender:**

- **Broker:** intermediário de mensagens.
- **Protocolo:** regras da comunicação.
- **Compatibilidade:** suporte às interfaces usadas pela aplicação.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Integração de aplicações / message broker · **Domínio:** 3 · **Escopo:** Regional (Multi-AZ opcional) · **Tópico do guia:** [3.18 Serviços menos conhecidos](../../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md)
>
> **Em uma frase:** brokers de mensagens gerenciados **Apache ActiveMQ** e **RabbitMQ**, compatíveis com protocolos padrão.
>
> **Escopo oficial:** ⚪ Não listado · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

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
