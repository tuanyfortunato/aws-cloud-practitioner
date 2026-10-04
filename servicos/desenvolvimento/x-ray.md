# AWS X-Ray

> **Categoria:** Ferramentas de desenvolvedor / observabilidade · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.15 Ferramentas de desenvolvimento](../../docs/03-tecnologia-e-servicos/15-ferramentas-de-desenvolvimento.md)
>
> **Em uma frase:** **rastreamento distribuído** — acompanha cada requisição através dos microsserviços para achar gargalos e erros.

## Conceitos

| Item | Detalhe |
|---|---|
| **Trace** | Caminho completo de uma requisição. |
| **Segments / subsegments** | Tempo gasto em cada serviço e chamada (banco, HTTP, AWS SDK). |
| **Service map** | Mapa visual das dependências com latência e taxa de erro. |
| **Sampling** | Regras para registrar só uma amostra das requisições (controla custo). |
| **Instrumentação** | SDKs do X-Ray ou **OpenTelemetry (ADOT)**; integração nativa com Lambda, API Gateway, ECS, Elastic Beanstalk, App Runner. |
| **Integração** | Visualização no CloudWatch (Application Signals / Transaction Search). |

## ⚠️ Não confundir

- **X-Ray** (rastreia requisições entre serviços) × **CloudWatch** (métricas/logs) × **CloudTrail** (chamadas de API da conta).

## ❓ Perguntas típicas

- "Encontrar qual microsserviço deixa a requisição lenta." → X-Ray.

## 🔗 Documentação oficial

- [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
