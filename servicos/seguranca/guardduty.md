# Amazon GuardDuty

> **Categoria:** Segurança / detecção de ameaças · **Domínio:** 2 · **Escopo:** Regional (multi-conta via Organizations) · **Tópico do guia:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)
>
> **Em uma frase:** detecção inteligente e contínua de **ameaças ativas** usando machine learning, detecção de anomalias e inteligência de ameaças.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Fontes de dados

| Fundamentais (ativadas ao ligar) | Planos de proteção opcionais |
|---|---|
| **CloudTrail management events** | **S3 Protection** (data events do S3) |
| **VPC Flow Logs** | **EKS Protection** (audit logs do Kubernetes) |
| **Logs de DNS** (Route 53 Resolver) | **Runtime Monitoring** (EC2, ECS, EKS — com agente) |
| | **Malware Protection** (EBS do EC2 e objetos novos no S3) |
| | **RDS Protection** (logins suspeitos no Aurora/RDS) |
| | **Lambda Protection** (tráfego de rede das funções) |

- **Sem agentes** para as fontes fundamentais: o GuardDuty lê os logs de forma independente (não precisa ativar Flow Logs/CloudTrail você mesmo).
- **Extended Threat Detection:** correlaciona eventos em **sequências de ataque** de vários estágios.

## Exemplos de achados (findings)

- Mineração de criptomoeda numa instância; comunicação com IPs/domínios maliciosos (C&C); chamadas de API de locais incomuns; credenciais de instância usadas fora da AWS; *port scanning*; buckets S3 tornados públicos; malware.

## Configurações

- Ativação com **um clique**; **teste gratuito de 30 dias** (no Free Tier novo, aparece vinculado ao **Paid plan**).
- Severidade (baixa, média, alta, crítica); listas de IPs confiáveis/ameaças; filtros de supressão.
- **Resposta automatizada:** achados vão ao **EventBridge** → Lambda/SSM para isolar a instância, notificar via SNS.
- Envia achados ao **Security Hub** e permite investigar no **Detective**.
- Multi-conta com **administrador delegado** no Organizations.

## Cobrança

- Por volume de eventos/logs analisados e por plano de proteção.

## ⚠️ Não confundir

- GuardDuty (**ameaça em andamento**, a partir de logs) × Inspector (**vulnerabilidade** de software) × Macie (**dados sensíveis**) × Detective (**investigação**).

## ❓ Perguntas típicas

- "Detectar atividade maliciosa analisando CloudTrail, VPC Flow Logs e DNS." → GuardDuty.
- "Instância está minerando criptomoeda." → GuardDuty.
- "Responder automaticamente a um achado." → GuardDuty → EventBridge → Lambda.

## 🔗 Documentação oficial

- [GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
