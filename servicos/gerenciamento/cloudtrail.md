# AWS CloudTrail

> **Categoria:** Gerenciamento / auditoria · **Domínio:** 2 · **Escopo:** Regional (trails multi-região e de organização) · **Tópico do guia:** [2.7 Logs, monitoramento e auditoria](../../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)
>
> **Em uma frase:** registra as **chamadas de API** da conta — quem fez, o quê, quando, de onde e em qual recurso.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é a **câmera de segurança da conta**: registra quem fez cada ação, quando e de onde.

- ✅ **Escolha quando:** precisa **auditar chamadas de API** e descobrir **quem fez o quê**.
- 🚫 **Não é a resposta quando:** quer **desempenho** → [CloudWatch](cloudwatch.md); quer saber **como estava a configuração** → [Config](config.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "quem fez", "chamadas de API", "auditoria", "90 dias de histórico".
<!-- didatico:fim -->

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Eventos de gerenciamento/dados, event history e trails |
| **O que você decide/configura?** | Cobertura, regiões, destino e retenção |
| **Em que ordem as coisas acontecem?** | Operações elegíveis geram eventos; histórico/trail permite consulta e armazenamento |
| **O que pode fazer, e em que condição?** | Ajuda a investigar identidade e ação executada |
| **O que não pode presumir?** | Eventos de dados têm configuração própria; não é histórico infinito gratuito de todo acesso |

**Caso comentado:** Descobrir quem alterou IAM: CloudTrail; gravar trilha e retenção conforme auditoria.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
