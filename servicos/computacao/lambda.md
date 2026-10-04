# AWS Lambda

> **Categoria:** Computação serverless · **Domínio:** 1 (serverless) e 3 · **Escopo:** Regional · **Tópico do guia:** [3.5 Containers e serverless](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)
>
> **Em uma frase:** executa seu código em resposta a eventos, sem servidores, cobrando só pelo tempo de execução.

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

- ⚠️ **> 15 minutos** → não é Lambda (use Fargate, Batch, EC2 ou Step Functions dividindo em etapas).
- ⚠️ Não existe "configurar vCPU" no Lambda: aumente a **memória**.
- Lambda × Fargate: função por evento (até 15 min) × contêiner serverless sem limite de duração.
- Lambda é "serverless/FaaS"; o guia o classifica também como PaaS.

## ❓ Perguntas típicas

- "Executar código sem servidores, em resposta a eventos." → Lambda.
- "Tempo máximo de execução?" → 15 minutos.
- "Como o Lambda é cobrado?" → Por requisições e duração (GB-s); nada quando não executa.
- "Gerar miniatura quando uma imagem chega ao S3." → Notificação de evento do S3 → Lambda.
- "Eliminar cold start em função crítica." → Concorrência provisionada.
- "Dar acesso da função ao DynamoDB." → Execution role.
- "Tarefa todo dia às 2h sem servidor." → EventBridge Scheduler + Lambda.

## 🔗 Documentação oficial

- [Guia do desenvolvedor do Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Quotas do Lambda](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)
- [Preços](https://aws.amazon.com/lambda/pricing/)
