# AWS IoT Core, IoT Greengrass e outros serviços de IoT

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Dispositivos físicos precisam enviar dados e receber comandos. Alguns também precisam executar tarefas perto do equipamento, mesmo com conectividade limitada.

**Como este serviço ajuda?** IoT Core conecta dispositivos à nuvem por mecanismos compatíveis. Greengrass leva funções de software para dispositivos de borda preparados para isso.

**Exemplo do dia a dia:** Sensores de uma escola enviam leituras ao IoT Core. Uma necessidade de processamento local pode levar a uma avaliação separada do Greengrass.

**O que ele não resolve sozinho?** Conectar um dispositivo não cria toda a análise dos dados nem autoriza qualquer equipamento. Identidade, políticas e software são necessários; os produtos têm escopos distintos.

**Primeiras palavras para entender:**

- **IoT:** dispositivos conectados.
- **Telemetria:** dados enviados por equipamentos.
- **Borda:** processamento próximo dos dispositivos.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Internet das Coisas · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.14 Aplicações de negócio, usuário final, front-end e IoT](../../docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md)
>
> **Em uma frase:** conectar, gerenciar e processar dados de bilhões de dispositivos com segurança — na nuvem e na borda.
>
> **Escopo oficial:** 🔀 IoT Core ✅ · IoT Greengrass ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Prepare identidade e software dos dispositivos que vão comunicar-se.

**Passo 2.** Configure os canais e as permissões para dados e comandos. Avalie processamento local separadamente quando necessário.

**Passo 3.** Acompanhe conexão e resultado. Equipamento conectado não implica que qualquer análise ou atualização já esteja implementada.

## 2. Recursos e opções, com significado

### AWS IoT Core

**Message broker**

**Detalhe:** **MQTT** (também MQTT sobre WebSocket, HTTPS, LoRaWAN) — publish/subscribe entre dispositivos e nuvem.

**Autenticação**

**Detalhe:** Certificados **X.509** por dispositivo, políticas do IoT; TLS mútuo.

**Device registry**

**Detalhe:** Inventário de "things".

**Device Shadow**

**Detalhe:** Estado desejado/reportado do dispositivo, mesmo quando offline.

**Rules engine**

**Detalhe:** Regras SQL que roteiam mensagens para Lambda, DynamoDB, S3, Kinesis, SNS, Timestream…

**Cobrança**

**Detalhe:** Por milhão de mensagens, minutos de conexão, operações do shadow e regras.

### AWS IoT Greengrass ❌

> ❌ **Fora do escopo da CLF-C02** — documentado só para referência ([lista oficial](../../docs/00-guia-do-exame/escopo-oficial.md)).

Runtime de **borda**: executa **Lambda, contêineres e inferência de ML localmente** no dispositivo/gateway, com operação **offline** e sincronização com a nuvem.

### Outros (reconhecer o nome)

| Serviço | Função |
|---|---|
| **IoT Device Management** | Organizar, monitorar e atualizar (OTA) frotas |
| **IoT Device Defender** | Auditar e detectar comportamento anômalo de dispositivos |
| **IoT SiteWise** | Dados de equipamentos industriais |
| **FreeRTOS** | Sistema operacional para microcontroladores |

🔄 **IoT Analytics** encerrado em 15/12/2025; **IoT Events** encerrado em 20/05/2026; **IoT FleetWise** fechado a novos clientes desde 30/04/2026 — não estudar.

🎯 Na prova, IoT = **só IoT Core**. **IoT Greengrass** e **IoT Device Defender** estão **fora do escopo**.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Conectar um dispositivo não cria toda a análise dos dados nem autoriza qualquer equipamento. Identidade, políticas e software são necessários; os produtos têm escopos distintos.

## 4. Caso resolvido: ligando as peças

Sensores de uma escola enviam leituras ao IoT Core. Uma necessidade de processamento local pode levar a uma avaliação separada do Greengrass.

**Aplicando a sequência à situação:**

**Etapa 1:** Prepare identidade e software dos dispositivos que vão comunicar-se.
**Etapa 2:** Configure os canais e as permissões para dados e comandos. Avalie processamento local separadamente quando necessário.
**Etapa 3:** Acompanhe conexão e resultado. Equipamento conectado não implica que qualquer análise ou atualização já esteja implementada.

**Resultado e responsabilidade:** IoT Core conecta dispositivos à nuvem por mecanismos compatíveis. Greengrass leva funções de software para dispositivos de borda preparados para isso.

**Recursos envolvidos:** Dispositivos, certificados, policies, topics e regras; runtime local Greengrass.

**Decisões que precisam ser tomadas:** Identidade do dispositivo, protocolo, topics e destinos.

**Outra situação comentada:** Sensor envia telemetria com identidade própria: IoT Core; processamento local tem necessidade distinta.

**Por que não concluir mais do que isso:** Não fornece conectividade física; Greengrass está fora do escopo consultado

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Conectar milhões de sensores à nuvem com segurança."

**Resposta curta:** IoT Core.

**Pergunta:** "Rodar inferência de ML no dispositivo sem conexão."

**Resposta curta:** IoT Greengrass.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html) · [Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
