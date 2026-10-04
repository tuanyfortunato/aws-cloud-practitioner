# Amazon API Gateway

> **Categoria:** Rede / front-end de APIs · **Domínio:** 3 · **Escopo:** Regional (endpoints edge-optimized usam CloudFront) · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)
>
> **Em uma frase:** cria, publica, protege e monitora APIs em qualquer escala — a "porta da frente" de back-ends serverless.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Tipos de API

| Tipo | Destaques | Uso |
|---|---|---|
| **REST API** | Mais recursos: **cache**, **usage plans e API keys**, validação de requisições, transformação, WAF, endpoints privados | APIs completas e gerenciadas |
| **HTTP API** | Mais simples, **mais barata** e de menor latência; JWT/OIDC nativo | Proxies para Lambda/HTTP |
| **WebSocket API** | Conexões bidirecionais persistentes | Chats, painéis em tempo real |

## Configurações importantes

| Item | Detalhe |
|---|---|
| **Integrações** | **Lambda** (clássico serverless), HTTP, serviços AWS (ex.: gravar direto no SQS/DynamoDB), VPC link (recursos privados via NLB/ALB). |
| **Tipos de endpoint** | **Edge-optimized** (via CloudFront), **Regional**, **Private** (só da VPC via interface endpoint). |
| **Autorização** | **IAM**, **Cognito user pools**, **Lambda authorizer**, JWT (HTTP API). |
| **Throttling** | Limites de requisições por segundo (conta, stage, método, usage plan) → protege o back-end. Padrão: **10.000 req/s por conta e região**, burst de 5.000 (algumas regiões novas: 2.500 / 1.250) 🧊. |
| **Stages** | `dev`, `prod`… com variáveis e deploys separados; *canary release*. |
| **Cache** | Respostas em cache por TTL (REST). |
| **Domínio customizado** | Com certificado do ACM. |
| **Monitoramento** | CloudWatch (métricas, logs de acesso), X-Ray. |

## Cobrança

- Por **milhão de chamadas** (HTTP API é mais barata) + dados transferidos + cache-hora; WebSocket por mensagens e minutos de conexão.

## ⚠️ Pegadinhas e não confundir

- API Gateway (APIs REST/HTTP/WebSocket) × **AppSync** (APIs **GraphQL**).
- API Gateway × ALB: ambos podem chamar Lambda; API Gateway tem throttling, chaves de API, autenticação e cache.

## ❓ Perguntas típicas

- "Criar e proteger uma API REST para funções Lambda." → API Gateway.
- "Limitar requisições por cliente com chaves de API." → Usage plans + API keys.
- "API GraphQL gerenciada." → AppSync (não API Gateway).

## 🔗 Documentação oficial

- [Guia do API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
