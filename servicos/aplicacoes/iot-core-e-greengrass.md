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

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.


**Passo 1.** Prepare identidade e software dos dispositivos que vão comunicar-se.

**Passo 2.** Configure os canais e as permissões para dados e comandos. Avalie processamento local separadamente quando necessário.

**Passo 3.** Acompanhe conexão e resultado. Equipamento conectado não implica que qualquer análise ou atualização já esteja implementada.

## 2. Recursos e opções, com significado

### AWS IoT Core

**Message broker**

**Antes de ler este trecho:**

- **HTTPS:** HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.
- **WebSocket:** Comunicação que mantém uma conexão para troca de mensagens entre cliente e servidor. É diferente de uma sequência de pedidos web independentes.
- **broker:** Intermediário de mensagens entre componentes. Sua interface e seus protocolos precisam ser compatíveis com as aplicações conectadas.
- **MQTT:** Protocolo de mensagens comum em dispositivos conectados. Aplicação, tópicos e permissões precisam ser definidos para a comunicação desejada.


**Detalhe:** **MQTT** (também MQTT sobre WebSocket, HTTPS, LoRaWAN) — publish/subscribe entre dispositivos e nuvem.

**Autenticação**

**Antes de ler este trecho:**

- **autenticação:** Verificação de quem está acessando. Confirmar a identidade não autoriza qualquer ação no sistema.
- **IoT:** Dispositivos físicos conectados que enviam informações ou recebem comandos. Conexão não substitui autenticação, software e análise dos dados.


**Detalhe:** Certificados **X.509** por dispositivo, políticas do IoT; TLS mútuo.

**Device registry**


**Detalhe:** Inventário de "things".

**Device Shadow**


**Detalhe:** Estado desejado/reportado do dispositivo, mesmo quando offline.

**Rules engine**

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **SNS:** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis.
- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.


**Detalhe:** Regras SQL que roteiam mensagens para Lambda, DynamoDB, S3, Kinesis, SNS, Timestream…

**Cobrança**


**Detalhe:** Por milhão de mensagens, minutos de conexão, operações do shadow e regras.

### AWS IoT Greengrass ❌

> ❌ **Fora do escopo da CLF-C02** — documentado só para referência ([lista oficial](../../docs/00-guia-do-exame/escopo-oficial.md)).

**Antes de ler este trecho:**

- **ML:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.
- **inferência:** Uso de um modelo para produzir um resultado com uma nova entrada. Pode acontecer sem um novo treinamento em cada solicitação.
- **runtime:** Ambiente que executa código de uma linguagem ou plataforma. Compatibilidade de bibliotecas e versões deve ser avaliada.


Runtime de **borda**: executa **Lambda, contêineres e inferência de ML localmente** no dispositivo/gateway, com operação **offline** e sincronização com a nuvem.

### Outros (reconhecer o nome)

**Antes de ler este trecho:**

- **sistema operacional:** Software básico da máquina, como Linux ou Windows. Ele administra arquivos, memória e execução de programas; atualizar esse software é diferente de atualizar a aplicação.
- **OTA:** Atualização enviada remotamente a dispositivos. É necessário preparar compatibilidade, autorização e tratamento de falhas.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

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

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

## 5. Caso resolvido: ligando as peças

Sensores de uma escola enviam leituras ao IoT Core. Uma necessidade de processamento local pode levar a uma avaliação separada do Greengrass.

**Aplicando a sequência à situação:**

**Etapa 1:** Prepare identidade e software dos dispositivos que vão comunicar-se.
**Etapa 2:** Configure os canais e as permissões para dados e comandos. Avalie processamento local separadamente quando necessário.
**Etapa 3:** Acompanhe conexão e resultado. Equipamento conectado não implica que qualquer análise ou atualização já esteja implementada.

**Resultado e responsabilidade:** IoT Core conecta dispositivos à nuvem por mecanismos compatíveis. Greengrass leva funções de software para dispositivos de borda preparados para isso.

**Recursos envolvidos:** Dispositivos, certificados, policies, topics e regras; runtime local Greengrass.

**Decisões que precisam ser tomadas:** Identidade do dispositivo, protocolo, topics e destinos.

**Antes de ler este trecho:**

- **telemetria:** Medidas e informações enviadas por um equipamento ou sistema. Coletar dados é uma etapa diferente de analisá-los ou agir sobre eles.


**Outra situação comentada:** Sensor envia telemetria com identidade própria: IoT Core; processamento local tem necessidade distinta.

**Por que não concluir mais do que isso:** Não fornece conectividade física; Greengrass está fora do escopo consultado

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Dispositivos físicos precisam enviar dados e receber comandos. Alguns também precisam executar tarefas perto do equipamento, mesmo com conectividade limitada.

**2. O que a solução fornece?**

IoT Core conecta dispositivos à nuvem por mecanismos compatíveis. Greengrass leva funções de software para dispositivos de borda preparados para isso.

**3. Que conclusão seria incorreta?**

Conectar um dispositivo não cria toda a análise dos dados nem autoriza qualquer equipamento. Identidade, políticas e software são necessários; os produtos têm escopos distintos.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Conectar milhões de sensores à nuvem com segurança."

**Resposta curta:** IoT Core.


**Fundamento explicado no capítulo:** "Conectar milhões de sensores à nuvem com segurança." → IoT Core.

**Pergunta:** "Rodar inferência de ML no dispositivo sem conexão."

**Resposta curta:** IoT Greengrass.


**Fundamento explicado no capítulo:** "Rodar inferência de ML no dispositivo sem conexão." → IoT Greengrass.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html) · [Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
