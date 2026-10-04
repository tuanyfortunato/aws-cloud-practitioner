# AWS Control Tower

> **Categoria:** Gerenciamento / governança multi-conta · **Domínio:** 2 · **Escopo:** Organização (região *home*) · **Tópico do guia:** [2.4 Governança multi-conta](../../docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md)
>
> **Em uma frase:** monta e governa automaticamente um ambiente multi-conta seguro e padronizado (**landing zone**) sobre o Organizations.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## O que configura

| Item | Detalhe |
|---|---|
| **Landing zone** | Organização com OUs (Security, Sandbox…) e contas compartilhadas: **Log Archive** (logs centralizados de CloudTrail e Config) e **Audit** (acesso de segurança). Integra IAM Identity Center. |
| **Controls (guardrails)** | **Preventivos** (SCPs/RCPs — impedem ações), **detectivos** (regras do **Config** — detectam desvios) e **proativos** (hooks do CloudFormation — barram recursos não conformes antes de criar). Categorias: obrigatórios, fortemente recomendados, eletivos. |
| **Account Factory** | Cria contas novas já no padrão (também via Service Catalog ou **AFT** com Terraform). |
| **Dashboard** | Conformidade de contas e OUs. |
| **Drift detection** | Detecta alterações fora do padrão. |

## Cobrança

- Sem custo próprio; paga-se os serviços usados (Config, CloudTrail, S3, Service Catalog…).

## ⚠️ Não confundir

- Organizations = estrutura e políticas. Control Tower = **automatiza boas práticas** em cima do Organizations.

## ❓ Perguntas típicas

- "Criar rapidamente um ambiente multi-conta seguro com guardrails." → Control Tower.
- "Criar novas contas já seguindo o padrão da empresa." → Account Factory.

## 🔗 Documentação oficial

- [Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
