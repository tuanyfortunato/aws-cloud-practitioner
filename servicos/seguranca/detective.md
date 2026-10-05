# Amazon Detective

> **Categoria:** Segurança / investigação · **Domínio:** 2 · **Escopo:** Regional · **Tópico do guia:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)
>
> **Em uma frase:** facilita **investigar a causa raiz** de achados de segurança, montando um grafo de comportamento a partir dos logs.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é o **detetive que chega depois do alarme**: reconstrói o que aconteceu e mostra a causa raiz.

- ✅ **Escolha quando:** precisa **investigar a origem** de um achado de segurança.
- 🚫 **Não é a resposta quando:** precisa **detectar** a ameaça → [GuardDuty](guardduty.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "investigar", "causa raiz", "achado de segurança".
<!-- didatico:fim -->

## Como funciona

- Coleta automaticamente CloudTrail, **VPC Flow Logs**, achados do **GuardDuty**, audit logs do EKS e achados do Security Hub.
- Constrói um **behavior graph** (ML + estatística) mostrando relações entre usuários, roles, IPs, instâncias, ao longo de até 1 ano.
- Visualizações prontas: "o que este IP fez?", "esse usuário costuma chamar essa API?", *finding groups* que agrupam achados relacionados.
- Teste gratuito de 30 dias; cobrado por volume de dados ingeridos.

## ⚠️ Não confundir

- **GuardDuty detecta → Detective investiga → Security Hub centraliza.**

## ❓ Perguntas típicas

- "Investigar a causa raiz de um achado de segurança." → Detective.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Behavior graph e investigação de entidades/eventos |
| **O que você decide/configura?** | Conta, região, fontes e acesso |
| **Em que ordem as coisas acontecem?** | Agrega contexto para explorar relações em atividade suspeita |
| **O que pode fazer, e em que condição?** | Ajuda investigação após sinais ou achados |
| **O que não pode presumir?** | Não é firewall ou substituto automático da detecção/remediação |

**Caso comentado:** Após finding GuardDuty, investigar contexto: Detective; bloquear requer ação apropriada.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Amazon Detective](https://docs.aws.amazon.com/detective/latest/userguide/what-is-detective.html)
