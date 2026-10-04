# AWS CloudTrail

> **Categoria:** Gerenciamento / auditoria · **Domínio:** 2 · **Escopo:** Regional (trails multi-região e de organização) · **Tópico do guia:** [2.7 Logs, monitoramento e auditoria](../../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)
>
> **Em uma frase:** registra as **chamadas de API** da conta — quem fez, o quê, quando, de onde e em qual recurso.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Tipos de eventos

| Tipo | Exemplo | Registrado por padrão? |
|---|---|---|
| **Management events** | `RunInstances`, `CreateBucket`, `AttachRolePolicy`, login no console | ✅ (Event history) |
| **Data events** | `GetObject`/`PutObject` no S3, `Invoke` no Lambda, itens do DynamoDB | ❌ — ativar no trail (pago, alto volume) |
| **Network activity events** | Chamadas via VPC endpoints | ❌ — opcional |
| **Insights events** | Picos anormais de chamadas/erros de API | ❌ — ativar CloudTrail Insights (pago) |

## Configurações

| Item | Detalhe |
|---|---|
| **Event history** | 📌 **90 dias** de management events, **grátis**, sem configurar nada (por região). |
| **Trail** | Envia eventos continuamente para um **bucket S3** (e opcionalmente CloudWatch Logs e EventBridge) → retenção longa. Pode ser **multi-região** e de **organização** (todas as contas). |
| **Log file integrity validation** ✔️ | Arquivos *digest* com hash para provar que os logs não foram alterados. |
| **Criptografia** | SSE-S3 por padrão; SSE-KMS opcional. |
| **CloudTrail Lake** | Data store gerenciado com **consultas SQL** e retenção longa. 🔄 Fechado a novos clientes desde **31/05/2026** (anúncio de 31/03/2026; uma verificação anterior citava 30/04/2026). Trails e Event history continuam. |
| **Proteção dos logs** | Bucket com Object Lock/MFA Delete, política restrita, conta de logs separada. |

## Cobrança

- Event history e **primeira cópia** dos management events num trail: grátis. Pagos: cópias adicionais, data events, Insights, Lake.

## ⚠️ Não confundir

- CloudTrail (**ações**: quem fez) × Config (**estado**: como estava) × CloudWatch (**desempenho**).
- CloudTrail registra **chamadas de API**, não o tráfego de rede (isso é VPC Flow Logs).

## ❓ Perguntas típicas

- "Quem encerrou a instância e quando?" → CloudTrail.
- "Por quanto tempo o CloudTrail guarda eventos sem configurar nada?" → 90 dias.
- "Guardar logs de API por anos." → Trail → S3.
- "Provar que os logs não foram adulterados." → Log file integrity validation.
- "Auditar leituras de objetos do S3." → Data events.

## 🔗 Documentação oficial

- [Guia do CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
