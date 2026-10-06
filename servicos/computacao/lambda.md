# AWS Lambda

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Você precisa executar uma tarefa quando algo acontece, mas não quer manter uma máquina inteira só para esperar por esse acontecimento.

**Como este serviço ajuda?** No Lambda, você entrega uma função, isto é, um trecho de programa. Um evento ou uma chamada dispara sua execução, e a AWS administra a infraestrutura usada para executá-la.

**Exemplo do dia a dia:** Quando uma pessoa envia uma foto, uma função pode gerar uma miniatura. Você escreve o código dessa transformação e configura o que vai acioná-lo.

**O que ele não resolve sozinho?** Lambda não é uma máquina em que você entra para instalar qualquer programa e deixá-lo rodando indefinidamente. Há limites de execução, e dados que precisam durar devem ser guardados em armazenamento apropriado.

**Primeiras palavras para entender:**

- **Evento:** acontecimento que dispara uma ação.
- **Função:** código executado para uma tarefa.
- **Serverless:** a AWS administra os servidores; eles continuam existindo.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Computação serverless · **Domínio:** 1 (serverless) e 3 · **Escopo:** Regional · **Tópico do guia:** [3.5 Containers e serverless](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)
>
> **Em uma frase:** executa código em resposta a eventos sem você administrar servidores; o modelo base cobra requisições e duração.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Escreva uma função que realize uma tarefa delimitada e defina como ela será chamada.

**Passo 2.** Configure os recursos, os acessos e a integração que fornece a entrada. A AWS inicia a execução quando recebe a chamada ou o evento.

**Passo 3.** Guarde resultados que precisam durar em um recurso apropriado e trate falhas. Não dependa de execução infinita nem de memória preservada entre chamadas.

## 2. Recursos e opções, com significado

### Para que serve

Processar arquivos assim que chegam ao S3 (miniaturas, validação, ETL leve).

Back-ends de APIs (com [API Gateway](../redes/api-gateway.md) ou function URLs).

Consumir filas e streams (SQS, Kinesis, DynamoDB Streams).

Tarefas agendadas (EventBridge Scheduler), automação de operações, chatbots.

### Conceitos e componentes

**Função**

**O que é:** Código + configuração (runtime, memória, timeout, role).

**Runtime**

**O que é:** Python, Node.js, Java, .NET, Ruby, **custom runtime** (`provided.al2023`) — Go e Rust usam o custom runtime; também **imagem de contêiner** (até 10 GB).

**Trigger / event source**

**O que é:** O que invoca: S3, API Gateway, ALB, SQS, SNS, EventBridge, DynamoDB/Kinesis Streams, Cognito, IoT…

**Execution role**

**O que é:** IAM role que dá permissões à função (ex.: gravar no DynamoDB).

**Resource-based policy**

**O que é:** Quem pode invocar a função (ex.: permitir o S3 ou outra conta).

**Invocação**

**O que é:** **Síncrona** (API Gateway, function URL), **assíncrona** (S3, SNS, EventBridge — com retentativas e *destinations*/DLQ) ou **event source mapping** (polling de SQS/Kinesis/DynamoDB).

**Layers**

**O que é:** Pacotes de bibliotecas compartilhados entre funções (até 5).

**Versões e aliases**

**O que é:** Versões imutáveis + aliases (`prod`, `dev`) que apontam para elas; permitem *canary*/peso.

**Cold start**

**O que é:** Latência extra ao criar um novo ambiente de execução.

### Configurações e opções importantes

**Memória**

**O que faz:** 128 MB – 10.240 MB; a **CPU é proporcional à memória**

**Timeout**

**O que faz:** até **900 s (15 min)**

**Armazenamento efêmero /tmp**

**O que faz:** 512 MB – 10.240 MB

**Variáveis de ambiente**

**O que faz:** Configuração (criptografadas com KMS)

**Arquitetura**

**O que faz:** x86_64 ou **arm64 (Graviton)** — mais barato por GB-s

**Concorrência reservada**

**O que faz:** Garante (e limita) concorrência para uma função

**Concorrência provisionada**

**O que faz:** Ambientes pré-aquecidos — elimina cold start (pago)

**SnapStart**

**O que faz:** Reduz cold start (Java, Python, .NET) restaurando um snapshot

**Acesso à VPC**

**O que faz:** Função acessa recursos privados (RDS, ElastiCache)

**Function URL**

**O que faz:** Endpoint HTTPS dedicado, sem API Gateway

**Destinations / DLQ**

**O que faz:** Para onde vão os resultados ou falhas de invocações assíncronas

### Limites e números

📌 Timeout máximo **15 min** · memória **10.240 MB** · CPU proporcional.

🧊 Concorrência padrão de 1.000 por região (ajustável), pacote zip 50 MB (250 MB descompactado), 5 layers, payload síncrono de 6 MB.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Lambda não é uma máquina em que você entra para instalar qualquer programa e deixá-lo rodando indefinidamente. Há limites de execução, e dados que precisam durar devem ser guardados em armazenamento apropriado.

### ⚠️ Pegadinhas e não confundir

⚠️ **Uma invocação convencional > 15 minutos** não é suportada. Considere Fargate/Batch/EC2 ou dividir o fluxo. Durable Functions e Lambda MicroVMs têm modelos próprios; não confunda duração total do workflow com uma invocação convencional.

⚠️ Não existe "configurar vCPU" no Lambda: aumente a **memória**.

Lambda × Fargate: função convencional por evento (até 15 min por invocação) × contêiner serverless sem limite de duração.

Lambda é "serverless/FaaS"; o guia o classifica também como PaaS.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Requisições** (por milhão) + **duração** em GB-segundo (arredondada ao ms, proporcional à memória).

Free Tier "sempre gratuito": **1 milhão de requisições e 400.000 GB-s por mês**.

Extras: concorrência provisionada, `/tmp` acima de 512 MB, transferência de dados.

Coberto pelo **Compute Savings Plans**.

### Segurança e responsabilidade compartilhada

**AWS:** infraestrutura, SO, runtime gerenciado (patches), escalonamento e alta disponibilidade (multi-AZ automático).

**Cliente:** **código**, dependências, permissões (execution role com menor privilégio), configuração, dados, segredos (use Secrets Manager).

### 🔄 Atualizações 2025-2026

Contas novas começam com quotas reduzidas de concorrência/memória, aumentadas automaticamente com o uso.

## 5. Caso resolvido: ligando as peças

A escola precisa criar uma miniatura quando uma pessoa envia uma foto. O trabalho tem entrada e resultado definidos e não precisa de uma máquina própria aguardando permanentemente o evento.

A equipe escreve a função de transformação, prepara permissões e configura uma integração compatível para acioná-la. Quando chega a entrada, a função executa o código e grava o resultado num armazenamento adequado. O serviço fornece a infraestrutura da execução.

Se o código falhar ou a entrada aparecer novamente, a aplicação precisa de tratamento apropriado. Não confie em memória de uma execução como armazenamento definitivo. A AWS administrar a execução não corrige automaticamente bibliotecas incluídas no pacote nem decide quem pode ler as fotos.

**Recursos envolvidos:** Função convencional, código, runtime, execution role, trigger e logs.

**Decisões que precisam ser tomadas:** Memória, timeout, concorrência, VPC e tratamento de falha.

**Outra situação comentada:** Miniatura após upload: evento S3 invoca função que precisa de leitura/gravação e logs autorizados.

**Por que não concluir mais do que isso:** Limite de quinze minutos é por invocação convencional; recursos como MicroVMs e Durable Functions têm modelos próprios

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Executar código sem servidores, em resposta a eventos."

**Resposta curta:** Lambda.

**Pergunta:** "Tempo máximo de uma invocação convencional?"

**Resposta curta:** 15 minutos.

**Pergunta:** "Como o Lambda é cobrado?"

**Resposta curta:** No modelo base, requisições e duração (GB-s); concorrência provisionada, snapshots e outros extras podem cobrar sem invocação.

**Pergunta:** "Gerar miniatura quando uma imagem chega ao S3."

**Resposta curta:** Notificação de evento do S3 → Lambda.

**Pergunta:** "Eliminar cold start em função crítica."

**Resposta curta:** Concorrência provisionada.

**Pergunta:** "Dar acesso da função ao DynamoDB."

**Resposta curta:** Execution role.

**Pergunta:** "Tarefa todo dia às 2h sem servidor."

**Resposta curta:** EventBridge Scheduler + Lambda.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do desenvolvedor do Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Quotas do Lambda](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)
- [Preços](https://aws.amazon.com/lambda/pricing/)
- [Durable Functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
