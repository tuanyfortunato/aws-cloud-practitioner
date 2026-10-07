<!-- autoral -->

# AWS IoT Core e IoT Greengrass

> **Categoria:** Internet das coisas · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** complementar
>
> **Em uma frase:** o IoT Core permite a comunicação segura, nos dois sentidos, entre dispositivos conectados e os serviços da AWS.
>
> **Escopo oficial:** 🔀 IoT Core ✅ · IoT Greengrass ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.14 Aplicações de negócio, usuário final, front-end e IoT](../../docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Como funciona

**Internet das coisas** (IoT) é o nome para dispositivos conectados que não são computadores, como sensores e medidores. As salas novas da escola têm sensores de temperatura que precisam mandar leituras para algum lugar. O **AWS IoT Core** conecta, gerencia e escala frotas de dispositivos sem que a escola provisione servidores, com autenticação mútua e criptografia.

1. Cada sensor é registrado e recebe credenciais.
2. O sensor publica as leituras com protocolos como **MQTT** (leve, de publicar e assinar), MQTT sobre WebSockets ou HTTPS.
3. O IoT Core recebe as mensagens e, com regras, as encaminha a outros serviços da AWS para guardar e analisar.
4. No sentido contrário, o IoT Core envia comandos aos dispositivos.

O AWS IoT Greengrass está fora do escopo da prova.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [Amazon Kinesis](../analytics/kinesis.md) | Fluxos de dados em tempo real de qualquer origem | "Streaming" |
| [Amazon SNS](../integracao/sns.md) | Notificações para assinantes | "Avisar por SMS ou e-mail" |
| [Amazon SQS](../integracao/sqs.md) | Fila entre partes de uma aplicação | "Desacoplar" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html)
- [Serviços fora do escopo da prova](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-out-of-scope-services.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
