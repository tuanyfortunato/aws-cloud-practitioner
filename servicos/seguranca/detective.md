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

## 🔗 Documentação oficial

- [Amazon Detective](https://docs.aws.amazon.com/detective/latest/userguide/what-is-detective.html)
