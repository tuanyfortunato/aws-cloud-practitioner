<!-- autoral -->

# AWS Audit Manager

> **Categoria:** Conformidade · **Domínio:** 2 · **Abrangência:** Regional · **Ficha:** referência
>
> **Em uma frase:** automatiza a coleta de evidências para auditorias, com frameworks prontos de controles; está em modo de manutenção e fora da lista atual do exame.
>
> **Escopo oficial:** ⚪ Não listado (saiu da lista atual) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.6 Compliance e governança](../../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Como funciona

Na auditoria anual, a escola precisa provar que seus controles funcionam o tempo todo, não só no dia da visita. O **AWS Audit Manager** coleta continuamente dados das contas e os transforma em evidências ligadas a cada controle. Desde 30/04/2026 ele está em modo de manutenção: não pode ser configurado em contas novas, e quem já usa continua usando.

1. Escolhe-se um framework pronto, um conjunto de controles organizado por norma, como SOC 2, PCI DSS ou HIPAA.
2. Cria-se uma avaliação para as contas que entram na auditoria.
3. O Audit Manager coleta as evidências automaticamente; evidências de fora da AWS podem ser enviadas à mão.
4. A auditoria usa as evidências; o Audit Manager não declara se a escola está em conformidade.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [AWS Artifact](artifact.md) | Relatórios de conformidade da própria AWS | "Relatório SOC da AWS" |
| [AWS Config](../gerenciamento/config.md) | Registra a configuração e avalia regras | "Configuração desejada" |
| [AWS Security Hub](security-hub.md) | Reúne achados e verifica padrões de segurança | "Pontuação de segurança" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html)
- [Mudança de disponibilidade do Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html)
- [Serviços no escopo da prova](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
