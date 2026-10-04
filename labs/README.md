# 🧪 Labs Práticos

A CLF-C02 não exige prática, mas usar o console fixa os conceitos. Registre aqui cada lab (um arquivo por lab,
ex.: `01-alerta-de-orcamento.md`).

> ⚠️ **Cuidado com custos:** comece pelo lab 01 (orçamento com alerta), use o Free Tier/créditos e **apague os
> recursos** ao terminar. Nunca faça commit de chaves de acesso, senhas ou IDs de conta.

## Labs sugeridos

| # | Lab | Serviços | Conceitos da prova | Status |
|---|---|---|---|---|
| 01 | Criar orçamento de "gasto zero" com alerta por e-mail | [Budgets](../servicos/custos/budgets.md) | Ferramentas de custo | 🔴 |
| 02 | Proteger o root com MFA e criar usuário administrativo no Identity Center | [IAM](../servicos/seguranca/iam.md), [Identity Center](../servicos/seguranca/iam-identity-center.md) | Root, MFA, menor privilégio | 🔴 |
| 03 | Gerar o credential report e revisar o Access Advisor | [IAM](../servicos/seguranca/iam.md) | Auditoria do IAM | 🔴 |
| 04 | Hospedar site estático no S3 + versionamento + lifecycle | [S3](../servicos/armazenamento/s3.md) | Classes, versionamento, Block Public Access | 🔴 |
| 05 | Colocar o CloudFront com OAC na frente do bucket | [CloudFront](../servicos/redes/cloudfront.md) | CDN, edge locations | 🔴 |
| 06 | Lançar EC2 com user data e acessar via Session Manager | [EC2](../servicos/computacao/ec2.md), [Systems Manager](../servicos/gerenciamento/systems-manager.md) | AMI, SG, IAM role, sem SSH | 🔴 |
| 07 | Alarme do CloudWatch de CPU com notificação SNS | [CloudWatch](../servicos/gerenciamento/cloudwatch.md), [SNS](../servicos/integracao/sns.md) | Monitoramento | 🔴 |
| 08 | Ver o Event history do CloudTrail e criar um trail | [CloudTrail](../servicos/gerenciamento/cloudtrail.md) | Auditoria de API | 🔴 |
| 09 | Função Lambda disparada por upload no S3 | [Lambda](../servicos/computacao/lambda.md) | Serverless, eventos | 🔴 |
| 10 | Fila SQS + tópico SNS (fan-out) | [SQS](../servicos/integracao/sqs.md), [SNS](../servicos/integracao/sns.md) | Desacoplamento | 🔴 |
| 11 | Stack CloudFormation que cria um bucket | [CloudFormation](../servicos/gerenciamento/cloudformation.md) | IaC | 🔴 |
| 12 | Explorar Trusted Advisor, Health Dashboard e Cost Explorer | [Trusted Advisor](../servicos/gerenciamento/trusted-advisor.md), [Cost Explorer](../servicos/custos/cost-explorer.md) | Boas práticas e custos | 🔴 |
| 13 | Montar estimativa no Pricing Calculator | [Pricing Calculator](../servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md) | Estimativa de custo | 🔴 |

## Modelo de lab

```markdown
# Lab XX — Título

**Objetivo:**
**Serviços:**
**Custo esperado:** (Free Tier / centavos / ...)

## Passo a passo
1.

## O que aprendi (ligação com a prova)

## Limpeza (recursos apagados)
- [ ]
```
