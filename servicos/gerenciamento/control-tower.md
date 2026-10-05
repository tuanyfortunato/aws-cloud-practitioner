# AWS Control Tower

> **Categoria:** Gerenciamento / governança multi-conta · **Domínio:** 2 · **Escopo:** Organização (região *home*) · **Tópico do guia:** [2.4 Governança multi-conta](../../docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md)
>
> **Em uma frase:** monta e governa automaticamente um ambiente multi-conta seguro e padronizado (**landing zone**) sobre o Organizations.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é um **kit "casa pronta" para várias contas**: monta a estrutura já com as regras de segurança instaladas.

- ✅ **Escolha quando:** precisa criar rapidamente um **ambiente multi-conta seguro e padronizado** (landing zone).
- 🚫 **Não é a resposta quando:** quer só **agrupar contas e aplicar SCPs** → [Organizations](organizations.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "landing zone", "guardrails", "ambiente multi-conta com boas práticas".
<!-- didatico:fim -->

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Landing zone, contas compartilhadas, OUs e controls |
| **O que você decide/configura?** | Contas/regiões governadas e controles |
| **Em que ordem as coisas acontecem?** | Estabeleça baseline e acompanhe conformidade dos ambientes inscritos |
| **O que pode fazer, e em que condição?** | Automatiza partes da configuração de governança multi-conta |
| **O que não pode presumir?** | Não substitui Organizations nem toda política específica da empresa |

**Caso comentado:** Criar base padronizada para novas contas: Control Tower, com responsabilidades de governança continuadas.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
