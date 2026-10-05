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

## Para que serve

- Processar arquivos assim que chegam ao S3 (miniaturas, validação, ETL leve).
- Back-ends de APIs (com [API Gateway](../redes/api-gateway.md) ou function URLs).
- Consumir filas e streams (SQS, Kinesis, DynamoDB Streams).
- Tarefas agendadas (EventBridge Scheduler), automação de operações, chatbots.

## Conceitos e componentes

| Componente | O que é |
|---|---|
| **Função** | Código + configuração (runtime, memória, timeout, role). |
| **Runtime** | Python, Node.js, Java, .NET, Ruby, **custom runtime** (`provided.al2023`) — Go e Rust usam o custom runtime; também **imagem de contêiner** (até 10 GB). |
| **Trigger / event source** | O que invoca: S3, API Gateway, ALB, SQS, SNS, EventBridge, DynamoDB/Kinesis Streams, Cognito, IoT… |
| **Execution role** | IAM role que dá permissões à função (ex.: gravar no DynamoDB). |
| **Resource-based policy** | Quem pode invocar a função (ex.: permitir o S3 ou outra conta). |
| **Invocação** | **Síncrona** (API Gateway, function URL), **assíncrona** (S3, SNS, EventBridge — com retentativas e *destinations*/DLQ) ou **event source mapping** (polling de SQS/Kinesis/DynamoDB). |
| **Layers** | Pacotes de bibliotecas compartilhados entre funções (até 5). |
| **Versões e aliases** | Versões imutáveis + aliases (`prod`, `dev`) que apontam para elas; permitem *canary*/peso. |
| **Cold start** | Latência extra ao criar um novo ambiente de execução. |

## Configurações e opções importantes

| Opção | O que faz |
|---|---|
| **Memória** | 128 MB – 10.240 MB; a **CPU é proporcional à memória** |
| **Timeout** | até **900 s (15 min)** |
| **Armazenamento efêmero `/tmp`** | 512 MB – 10.240 MB |
| **Variáveis de ambiente** | Configuração (criptografadas com KMS) |
| **Arquitetura** | x86_64 ou **arm64 (Graviton)** — mais barato por GB-s |
| **Concorrência reservada** | Garante (e limita) concorrência para uma função |
| **Concorrência provisionada** | Ambientes pré-aquecidos — elimina cold start (pago) |
| **SnapStart** | Reduz cold start (Java, Python, .NET) restaurando um snapshot |
| **Acesso à VPC** | Função acessa recursos privados (RDS, ElastiCache) |
| **Function URL** | Endpoint HTTPS dedicado, sem API Gateway |
| **Destinations / DLQ** | Para onde vão os resultados ou falhas de invocações assíncronas |

## Limites e números

- 📌 Timeout máximo **15 min** · memória **10.240 MB** · CPU proporcional.
- 🧊 Concorrência padrão de 1.000 por região (ajustável), pacote zip 50 MB (250 MB descompactado), 5 layers, payload síncrono de 6 MB.

## Cobrança

- **Requisições** (por milhão) + **duração** em GB-segundo (arredondada ao ms, proporcional à memória).
- Free Tier "sempre gratuito": **1 milhão de requisições e 400.000 GB-s por mês**.
- Extras: concorrência provisionada, `/tmp` acima de 512 MB, transferência de dados.
- Coberto pelo **Compute Savings Plans**.

## Segurança e responsabilidade compartilhada

- **AWS:** infraestrutura, SO, runtime gerenciado (patches), escalonamento e alta disponibilidade (multi-AZ automático).
- **Cliente:** **código**, dependências, permissões (execution role com menor privilégio), configuração, dados, segredos (use Secrets Manager).

## 🔄 Atualizações 2025-2026

- Contas novas começam com quotas reduzidas de concorrência/memória, aumentadas automaticamente com o uso.

## ⚠️ Pegadinhas e não confundir

- ⚠️ **Uma invocação convencional > 15 minutos** não é suportada. Considere Fargate/Batch/EC2 ou dividir o fluxo. Durable Functions e Lambda MicroVMs têm modelos próprios; não confunda duração total do workflow com uma invocação convencional.
- ⚠️ Não existe "configurar vCPU" no Lambda: aumente a **memória**.
- Lambda × Fargate: função convencional por evento (até 15 min por invocação) × contêiner serverless sem limite de duração.
- Lambda é "serverless/FaaS"; o guia o classifica também como PaaS.

## ❓ Perguntas típicas

- "Executar código sem servidores, em resposta a eventos." → Lambda.
- "Tempo máximo de uma invocação convencional?" → 15 minutos.
- "Como o Lambda é cobrado?" → No modelo base, requisições e duração (GB-s); concorrência provisionada, snapshots e outros extras podem cobrar sem invocação.
- "Gerar miniatura quando uma imagem chega ao S3." → Notificação de evento do S3 → Lambda.
- "Eliminar cold start em função crítica." → Concorrência provisionada.
- "Dar acesso da função ao DynamoDB." → Execution role.
- "Tarefa todo dia às 2h sem servidor." → EventBridge Scheduler + Lambda.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Função convencional, código, runtime, execution role, trigger e logs |
| **O que você decide/configura?** | Memória, timeout, concorrência, VPC e tratamento de falha |
| **Em que ordem as coisas acontecem?** | Evento invoca a função; código usa permissões da role e devolve ou grava resultado |
| **O que pode fazer, e em que condição?** | Executa lógica sem administrar hosts; memória/código local não são armazenamento durável garantido |
| **O que não pode presumir?** | Limite de quinze minutos é por invocação convencional; recursos como MicroVMs e Durable Functions têm modelos próprios |

**Caso comentado:** Miniatura após upload: evento S3 invoca função que precisa de leitura/gravação e logs autorizados.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do desenvolvedor do Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Quotas do Lambda](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)
- [Preços](https://aws.amazon.com/lambda/pricing/)
- [Durable Functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)
