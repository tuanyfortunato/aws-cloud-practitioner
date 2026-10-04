# AWS IoT Core, IoT Greengrass e outros serviços de IoT

> **Categoria:** Internet das Coisas · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.14 Aplicações de negócio, usuário final, front-end e IoT](../../docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md)
>
> **Em uma frase:** conectar, gerenciar e processar dados de bilhões de dispositivos com segurança — na nuvem e na borda.
>
> **Escopo oficial:** 🔀 IoT Core ✅ · IoT Greengrass ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## AWS IoT Core

| Componente | Detalhe |
|---|---|
| **Message broker** | **MQTT** (também MQTT sobre WebSocket, HTTPS, LoRaWAN) — publish/subscribe entre dispositivos e nuvem. |
| **Autenticação** | Certificados **X.509** por dispositivo, políticas do IoT; TLS mútuo. |
| **Device registry** | Inventário de "things". |
| **Device Shadow** | Estado desejado/reportado do dispositivo, mesmo quando offline. |
| **Rules engine** | Regras SQL que roteiam mensagens para Lambda, DynamoDB, S3, Kinesis, SNS, Timestream… |
| **Cobrança** | Por milhão de mensagens, minutos de conexão, operações do shadow e regras. |

## AWS IoT Greengrass

- Runtime de **borda**: executa **Lambda, contêineres e inferência de ML localmente** no dispositivo/gateway, com operação **offline** e sincronização com a nuvem.

## Outros (reconhecer o nome)

| Serviço | Função |
|---|---|
| **IoT Device Management** | Organizar, monitorar e atualizar (OTA) frotas |
| **IoT Device Defender** | Auditar e detectar comportamento anômalo de dispositivos |
| **IoT SiteWise** | Dados de equipamentos industriais |
| **FreeRTOS** | Sistema operacional para microcontroladores |

- 🔄 **IoT Analytics** encerrado em 15/12/2025; **IoT Events** encerrado em 20/05/2026; **IoT FleetWise** fechado a novos clientes desde 30/04/2026 — não estudar.
- 🎯 Na prova, IoT = **só IoT Core**. **IoT Greengrass** e **IoT Device Defender** estão **fora do escopo**.

## ❓ Perguntas típicas

- "Conectar milhões de sensores à nuvem com segurança." → IoT Core.
- "Rodar inferência de ML no dispositivo sem conexão." → IoT Greengrass.

## 🔗 Documentação oficial

- [IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html) · [Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html)
