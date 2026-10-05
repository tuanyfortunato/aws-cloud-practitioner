# AWS IoT Core, IoT Greengrass e outros serviços de IoT

> **Categoria:** Internet das Coisas · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.14 Aplicações de negócio, usuário final, front-end e IoT](../../docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md)
>
> **Em uma frase:** conectar, gerenciar e processar dados de bilhões de dispositivos com segurança — na nuvem e na borda.
>
> **Escopo oficial:** 🔀 IoT Core ✅ · IoT Greengrass ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é uma **central que conecta milhões de dispositivos** e recebe as mensagens deles com segurança.

- ✅ **Escolha quando:** precisa **conectar sensores e dispositivos** à nuvem (IoT Core, o único serviço de IoT da prova).
- 🚫 **Não é a resposta quando:** precisa guardar **séries temporais** → Timestream, na ficha de [bancos especializados](../banco-de-dados/keyspaces-timestream-e-outros.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "sensores", "dispositivos", "MQTT", "conectar milhões de dispositivos".
<!-- didatico:fim -->

## AWS IoT Core

| Componente | Detalhe |
|---|---|
| **Message broker** | **MQTT** (também MQTT sobre WebSocket, HTTPS, LoRaWAN) — publish/subscribe entre dispositivos e nuvem. |
| **Autenticação** | Certificados **X.509** por dispositivo, políticas do IoT; TLS mútuo. |
| **Device registry** | Inventário de "things". |
| **Device Shadow** | Estado desejado/reportado do dispositivo, mesmo quando offline. |
| **Rules engine** | Regras SQL que roteiam mensagens para Lambda, DynamoDB, S3, Kinesis, SNS, Timestream… |
| **Cobrança** | Por milhão de mensagens, minutos de conexão, operações do shadow e regras. |

## AWS IoT Greengrass ❌

> ❌ **Fora do escopo da CLF-C02** — documentado só para referência ([lista oficial](../../docs/00-guia-do-exame/escopo-oficial.md)).

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Dispositivos, certificados, policies, topics e regras; runtime local Greengrass |
| **O que você decide/configura?** | Identidade do dispositivo, protocolo, topics e destinos |
| **Em que ordem as coisas acontecem?** | Dispositivo autentica, publica/recebe e regra encaminha dados |
| **O que pode fazer, e em que condição?** | IoT Core conecta dispositivos; Greengrass atende execução local compatível |
| **O que não pode presumir?** | Não fornece conectividade física; Greengrass está fora do escopo consultado |

**Caso comentado:** Sensor envia telemetria com identidade própria: IoT Core; processamento local tem necessidade distinta.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html) · [Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html)
