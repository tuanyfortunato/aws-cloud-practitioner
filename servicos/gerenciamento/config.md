# AWS Config

> **Categoria:** Gerenciamento / governança e compliance · **Domínio:** 2 · **Escopo:** Regional (agregadores multi-conta/região) · **Tópico do guia:** [2.7 Logs, monitoramento e auditoria](../../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md) · [2.6 Compliance](../../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md)
>
> **Em uma frase:** registra a **configuração** dos recursos e seu histórico de mudanças, e avalia continuamente se estão **conformes** com regras.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Componentes

| Componente | Detalhe |
|---|---|
| **Configuration recorder** | Registra *configuration items* (estado de cada recurso e relações) — todos os tipos ou selecionados; contínuo ou diário. |
| **Delivery channel** | Envia histórico e snapshots para **S3** e notificações para **SNS**. |
| **Resource timeline** | "Como estava este security group na terça passada e quem mudou?" (com link para o evento no CloudTrail). |
| **Config rules** | **Managed rules** (centenas prontas: `s3-bucket-public-read-prohibited`, `encrypted-volumes`, `restricted-ssh`, `root-account-mfa-enabled`…) ou **custom** (Lambda ou Guard). Avaliação por mudança ou periódica. |
| **Remediation** | Ações corretivas manuais ou **automáticas** via **Systems Manager Automation**. |
| **Conformance packs** | Pacotes de regras + remediações (ex.: boas práticas de PCI DSS, CIS) implantáveis na organização. |
| **Aggregators** | Visão consolidada de várias contas e regiões. |
| **Advanced query** | Consultas SQL sobre o inventário de configuração. |

## Cobrança

- Por **configuration item registrado** + por **avaliação de regra** + conformance packs.

## Quem depende do Config

- **Security Hub** (verificações de padrões), **Firewall Manager**, **Control Tower** (controles detectivos), **Audit Manager**.

## ⚠️ Não confundir

- Config (**estado/conformidade**) × CloudTrail (**quem fez**) × CloudWatch (**métricas**).
- Config **detecta e pode remediar**; **SCP** previne.

## ❓ Perguntas típicas

- "Histórico de configuração de um recurso e se segue as regras." → AWS Config.
- "Como estava o security group semana passada?" → Config.
- "Verificar continuamente se todos os buckets estão criptografados e corrigir automaticamente." → Config rule + remediação (SSM Automation).

## 🔗 Documentação oficial

- [Guia do AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
