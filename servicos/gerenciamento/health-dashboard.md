# AWS Health Dashboard

> **Categoria:** Gerenciamento / operações · **Domínio:** 2 e 3 · **Escopo:** Global · **Gratuito** · **Tópico do guia:** [3.16 Gestão e governança](../../docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md)
>
> **Em uma frase:** mostra o status dos serviços AWS e, principalmente, os eventos que afetam **os seus** recursos.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Duas visões

| Visão | O que mostra | Acesso |
|---|---|---|
| **Service health** | Status **público** de todos os serviços em todas as regiões | Sem login |
| **Your account health** | Eventos **personalizados**: manutenções programadas (ex.: reinício de instância por hardware), problemas que afetam seus recursos, avisos (fim de versões, certificados) — com **orientação de correção** | Console, para todos os clientes |

## Integrações

- **AWS Health API:** acesso programático — exige plano **Business ou superior**.
- **EventBridge:** automatizar respostas a eventos (ex.: notificar no Slack, mover cargas).
- **Organizational view:** eventos de todas as contas da organização.

## ⚠️ Não confundir

- Health Dashboard (eventos **da AWS** que afetam você) × CloudWatch (métricas **dos seus** recursos) × Trusted Advisor (recomendações).

## ❓ Perguntas típicas

- "Ver eventos de manutenção da AWS que afetam minhas instâncias." → AWS Health Dashboard.
- "Automatizar reação a um evento de manutenção programada." → Health + EventBridge.

## 🔗 Documentação oficial

- [AWS Health](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html)
