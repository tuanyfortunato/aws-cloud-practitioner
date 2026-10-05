# AWS Health Dashboard

> **Categoria:** Gerenciamento / operações · **Domínio:** 2 e 3 · **Escopo:** Global · **Gratuito** · **Tópico do guia:** [3.16 Gestão e governança](../../docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md)
>
> **Em uma frase:** mostra o status dos serviços AWS e, principalmente, os eventos que afetam **os seus** recursos.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é o **aviso de manutenção do condomínio**: avisa quando a AWS vai mexer em algo que afeta os seus recursos.

- ✅ **Escolha quando:** precisa ver **eventos e manutenções da AWS** que afetam a sua conta.
- 🚫 **Não é a resposta quando:** quer **métricas dos seus recursos** → [CloudWatch](cloudwatch.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "evento da AWS", "manutenção programada", "afeta minhas instâncias".
<!-- didatico:fim -->

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Eventos públicos e eventos específicos da conta |
| **O que você decide/configura?** | Conta, região, serviço e integrações de evento |
| **Em que ordem as coisas acontecem?** | Consulte impacto/avisos da infraestrutura e planeje ação |
| **O que pode fazer, e em que condição?** | Mostra ocorrências AWS e manutenção relevante |
| **O que não pode presumir?** | Ausência de evento AWS não prova que o código da aplicação está saudável |

**Caso comentado:** Manutenção de recurso específico: Health; erro interno do app: logs/métricas da aplicação.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [AWS Health](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html)
