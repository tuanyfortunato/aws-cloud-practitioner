<!-- autoral -->

# Amazon Detective

> **Categoria:** Segurança / investigação · **Domínio:** 2 · **Abrangência:** Regional · **Ficha:** complementar
>
> **Em uma frase:** ajuda a investigar a causa raiz de achados de segurança e atividades suspeitas, com visualizações de como identidades, recursos e endereços se relacionaram ao longo do tempo.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

O GuardDuty avisou que uma chave de acesso da escola foi usada de um endereço estranho. A pergunta seguinte é: o que exatamente aconteceu, desde quando e o que mais foi afetado? O **Amazon Detective** coleta dados de registros dos recursos e usa aprendizado de máquina, estatística e teoria de grafos para responder.

1. Ativa-se o Detective na conta.
2. Ele passa a coletar automaticamente dados de registros, como CloudTrail e VPC Flow Logs.
3. A partir de um achado, como um do GuardDuty, a equipe abre a investigação.
4. O Detective mostra as ligações e a linha do tempo entre identidades, recursos e endereços envolvidos.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [Amazon GuardDuty](guardduty.md) | Detecta a ameaça e gera o achado | "Detectar atividade maliciosa" |
| [AWS Security Hub](security-hub.md) | Reúne e prioriza achados de vários serviços | "Visão central", "pontuação" |
| [AWS CloudTrail](../gerenciamento/cloudtrail.md) | Registra as chamadas de API | "Quem fez o quê" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon Detective](https://docs.aws.amazon.com/detective/latest/userguide/what-is-detective.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
