<!-- autoral -->

# Planos de AWS Support

> **Categoria:** Suporte · **Domínio:** 4 · **Abrangência:** Por conta · **Ficha:** núcleo
>
> **Em uma frase:** os quatro planos de suporte da AWS (Basic, Business Support+, Enterprise Support e Unified Operations), que vão do atendimento de conta incluído para todos até especialistas designados com resposta em minutos.
>
> **Escopo oficial:** ✅ No escopo (AWS Support — distinguir exemplos do guia e oferta comercial atual) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [4.5 Planos de AWS Support](../../docs/04-cobranca-precos-e-suporte/05-planos-de-suporte.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

São 22h de um domingo, e o sistema de matrícula da rede parou. A equipe técnica, de duas pessoas, não achou a causa. Dá para chamar um engenheiro da AWS agora, e em quanto tempo ele responde?

Depende do plano. O **Basic** está incluído para todos: atendimento de **conta e faturamento**, pedidos de aumento de cota, documentação, o **re:Post**, as verificações principais do **Trusted Advisor** e o **AWS Health**, mas **não abre caso técnico**. O **Business Support+**, mínimo recomendado para produção, dá acesso 24/7 a engenheiros por telefone, web e chat, todas as verificações do Trusted Advisor e resposta em menos de 30 minutos quando um sistema crítico cai. O **Enterprise Support** acrescenta um **Technical Account Manager (TAM)** designado e resposta em até 15 minutos. O **Unified Operations**, para missão crítica, responde em até 5 minutos e monitora as cargas 24/7.

O limite: o suporte ajuda a resolver, mas a operação continua sendo da escola, no modelo de responsabilidade compartilhada. E os planos antigos (Developer, Business e Enterprise On-Ramp) acabam em **01/01/2027**; materiais antigos ainda os citam.

## Como funciona

1. A conta começa no Basic, sem custo.
2. Quem precisa de mais contrata um plano pago, cobrado por mês, sem contrato de longo prazo.
3. No AWS Support Center, abre-se um caso: conta e faturamento, aumento de cota ou técnico (este, só nos planos pagos).
4. Escolhe-se a gravidade do caso, que define o tempo de resposta do plano.

## Opções principais

| Plano | O que acrescenta | Na escola |
|---|---|---|
| Basic | Conta e faturamento, documentação, re:Post, Trusted Advisor principal, AWS Health | Só dúvidas da fatura |
| Business Support+ | Engenheiros 24/7, IA generativa, todas as verificações do Trusted Advisor, Support API | Matrícula em produção |
| Enterprise Support | TAM designado, revisões estratégicas, AWS Countdown | Rede grande com vários sistemas |
| Unified Operations | Resposta em 5 min, engenheiros designados, monitoramento 24/7 | Missão crítica |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Business Support+ | Maior entre US$ 29 por mês por conta e uma porcentagem da fatura | 06/10/2026 |
| Enterprise Support | A partir de US$ 5.000 por mês | 06/10/2026 |
| Unified Operations | A partir de US$ 50.000 por mês | 06/10/2026 |
| Sistema crítico fora do ar | Menos de 30 min, 15 min e 5 min (Business Support+, Enterprise, Unified Operations) | 06/10/2026 |
| Sistema de produção fora do ar | Menos de 1 h nos três planos | 06/10/2026 |
| Orientação geral | Menos de 24 h nos três planos | 06/10/2026 |
| Fim de Developer, Business e Enterprise On-Ramp | 01/01/2027 | 06/10/2026 |

## Como é cobrado

O Basic é incluído. Os planos pagos são cobrados por mês, sem contrato de longo prazo, pelo maior valor entre um mínimo mensal e uma porcentagem da fatura da AWS.

## Não confundir com

| Serviço | Diferença para os planos | Pista no enunciado |
|---|---|---|
| [AWS Trusted Advisor](../gerenciamento/trusted-advisor.md) | Verificações automáticas; o plano define quantas | "Recomendações de economia e segurança" |
| [AWS Health Dashboard](../gerenciamento/health-dashboard.md) | Eventos que afetam a conta; a Health API pede plano pago | "Manutenção programada" |
| [AWS Professional Services e parceiros](recursos-de-ajuda-e-parceiros.md) | Projetos de consultoria, não atendimento de casos | "Ajuda para migrar o datacenter" |
| [AWS re:Post](recursos-de-ajuda-e-parceiros.md) | Comunidade aberta, sem tempo de resposta | "Perguntar à comunidade" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [Planos de AWS Support](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html)
- [Comparar os planos de AWS Support](https://aws.amazon.com/premiumsupport/plans/)
- [Preços do AWS Support](https://aws.amazon.com/premiumsupport/pricing/)
- [Gerenciamento de casos](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
