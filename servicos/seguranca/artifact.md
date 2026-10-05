# AWS Artifact

> **Categoria:** Compliance · **Domínio:** 2 · **Escopo:** Global (portal) · **Gratuito** · **Tópico do guia:** [2.6 Compliance e governança](../../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md)
>
> **Em uma frase:** portal de autoatendimento para baixar **relatórios de conformidade da AWS** e aceitar **acordos** legais.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é a **secretaria da AWS** onde você baixa os certificados e relatórios de auditoria **da própria AWS**.

- ✅ **Escolha quando:** um **auditor** pede relatórios de conformidade da AWS (SOC, PCI, ISO) ou é preciso **aceitar um acordo** (como o BAA).
- 🚫 **Não é a resposta quando:** precisa juntar **evidências da sua própria conta** → [Audit Manager](audit-manager.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "relatório SOC 2", "atestado PCI", "ISO", "compliance da AWS", "BAA/HIPAA".
<!-- didatico:fim -->

## O que oferece

| Seção | Exemplos |
|---|---|
| **Artifact Reports** | **SOC 1, SOC 2, SOC 3**, **PCI DSS** (Attestation of Compliance), certificações **ISO 27001/27017/27018/9001**, C5, relatórios de terceiros (ISVs do Marketplace). |
| **Artifact Agreements** | **BAA** (Business Associate Addendum — **HIPAA**), NDA, acordos de GDPR; aceitar por conta ou para toda a organização. |
| **Notificações** | Avisos de novos relatórios. |

- Acesso controlado por IAM; alguns relatórios exigem aceitar termos de confidencialidade.

## ⚠️ Não confundir

- **Artifact** = evidências **da AWS** (o que a AWS certifica). **Audit Manager** = evidências **da sua conta** para a **sua** auditoria.

## ❓ Perguntas típicas

- "Auditor pede o relatório SOC 2 da AWS." → Artifact.
- "Aceitar o BAA para HIPAA." → Artifact Agreements.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Relatórios e agreements |
| **O que você decide/configura?** | Documento solicitado e autorização para consulta |
| **Em que ordem as coisas acontecem?** | Localize e obtenha evidência oficial da AWS |
| **O que pode fazer, e em que condição?** | Ajuda a demonstrar controles da infraestrutura AWS |
| **O que não pode presumir?** | Não registra atividade de usuários da sua conta nem certifica sua aplicação |

**Caso comentado:** Auditor pede relatório AWS: Artifact; quem apagou recurso: CloudTrail.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html)
