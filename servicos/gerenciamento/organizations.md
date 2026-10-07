<!-- autoral -->

# AWS Organizations

> **Categoria:** Gerenciamento e governança de várias contas · **Domínio:** 2 e 4 · **Abrangência:** Global · **Ficha:** núcleo
>
> **Em uma frase:** reúne várias contas da AWS numa organização, com políticas aplicadas por grupo de contas e uma fatura única.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.4 Governança multi-conta](../../docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

A escola separou produção, testes e registros de auditoria em três contas, como a AWS recomenda. Agora são três faturas, três conjuntos de regras e nenhum jeito de impedir que um administrador da conta de testes crie recursos fora da Região escolhida.

O **Organizations** junta as contas numa **organização**. A conta que a cria vira a **conta de gerenciamento**; as outras são **contas-membro**, agrupadas em **unidades organizacionais** (OUs), como pastas. Uma **política de controle de serviço** (SCP) anexada a uma OU define o máximo que os usuários e funções das contas abaixo dela podem fazer, inclusive o root dessas contas. E o **faturamento consolidado** gera uma fatura única e soma o uso de todas as contas para os descontos por volume, de Instâncias Reservadas e de Savings Plans.

O limite: uma SCP não concede permissão nenhuma, só estabelece o teto; ainda é preciso uma política do IAM que permita a ação. As SCPs não afetam a conta de gerenciamento. E juntar a cobrança não junta os dados: cada conta continua isolada.

## Como funciona

1. A conta de gerenciamento cria a organização, com todos os recursos habilitados.
2. Ela convida contas existentes ou cria contas novas e as organiza em OUs, com até cinco níveis abaixo da raiz.
3. Políticas, como SCPs, são anexadas à raiz, a uma OU ou a uma conta e valem para tudo abaixo.
4. A conta de gerenciamento paga a fatura de todas; contas-membro podem ser administradoras delegadas de serviços como o GuardDuty.

## Opções principais

| Recurso | O que faz | Exemplo na escola |
|---|---|---|
| Unidades organizacionais (OUs) | Agrupam contas, como pastas | OU "Matrícula" com produção e testes |
| SCP | Teto de permissões das identidades das contas-membro | Negar ações fora da Região escolhida |
| RCP | Teto de acesso aos recursos por identidades de fora | Impedir acesso externo aos buckets |
| Faturamento consolidado | Fatura única e descontos somados | Uma conta paga tudo |
| Administrador delegado | Conta-membro administra um serviço para todos | Equipe de segurança cuida do GuardDuty |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Custo | Sem custo adicional | 06/10/2026 |
| Níveis de OUs | Até 5 abaixo da raiz | 06/10/2026 |
| Contas por organização (padrão) | 10, ajustável pelo Service Quotas | 06/10/2026 |
| Organizações por conta | Uma de cada vez | 06/10/2026 |
| SCPs na conta de gerenciamento | Não se aplicam | 06/10/2026 |

## Como é cobrado

O Organizations não tem custo adicional, e o faturamento consolidado também não. A conta de gerenciamento paga todo o uso das contas da organização.

## Não confundir com

| Serviço | Diferença para o Organizations | Pista no enunciado |
|---|---|---|
| [AWS Control Tower](control-tower.md) | Monta e governa a organização segundo boas práticas | "Landing zone", "guardrails" |
| [AWS IAM](../seguranca/iam.md) | Concede permissões dentro de uma conta | "Dar acesso a um usuário" |
| [AWS IAM Identity Center](../seguranca/iam-identity-center.md) | Login único para as contas da organização | "Um login para várias contas" |
| [AWS Resource Access Manager](service-catalog-e-ram.md) | Compartilha recursos entre contas | "Usar a mesma sub-rede em outra conta" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
- [Terminologia e conceitos](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html)
- [Políticas de controle de serviço](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
- [Cotas do AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html)
- [Faturamento consolidado](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html)
- [Perguntas frequentes do AWS Organizations](https://aws.amazon.com/organizations/faqs/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
