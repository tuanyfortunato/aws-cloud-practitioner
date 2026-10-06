<!-- autoral -->

# AWS Health Dashboard

> **Categoria:** Gerenciamento e operações · **Domínio:** 2 e 3 · **Abrangência:** Global · **Ficha:** núcleo
>
> **Em uma frase:** mostra os eventos da AWS que afetam os serviços e as suas contas, como falhas em andamento e manutenções planejadas.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.16 Gestão e governança](../../docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

No dia das inscrições, parte dos pais reclama de lentidão. A equipe de TI olha as métricas e não acha nada de errado na aplicação. A dúvida que sobra é: o problema é da escola ou da AWS?

O **AWS Health** dá essa resposta. O **Health Dashboard** tem duas visões. A **saúde dos serviços** (*service health*) é uma página pública com os eventos dos serviços da AWS em todas as Regiões, sem precisar de login. A **saúde da sua conta** (*your account health*) mostra os eventos que podem afetar as suas contas e recursos, inclusive manutenções planejadas, para que a escola se prepare. Ela está disponível para todos os clientes, sem configuração e sem custo adicional.

O limite: o Health fala dos eventos da AWS, não dos problemas da aplicação da escola nem de quem mudou algo na conta. Para isso existem o [CloudWatch](cloudwatch.md) e o [CloudTrail](cloudtrail.md). E consultar os eventos por programa, pela **AWS Health API**, exige um plano de suporte pago.

## Como funciona

1. A AWS publica eventos de serviço e de conta no AWS Health.
2. A página pública mostra a saúde dos serviços; o console mostra os eventos que afetam a sua conta.
3. Com o AWS Organizations, a **visão organizacional** reúne os eventos de todas as contas.
4. Regras do EventBridge podem reagir aos eventos, por exemplo avisando a equipe de uma manutenção.

## Opções principais

| Visão ou recurso | O que mostra | Quem usa |
|---|---|---|
| Saúde dos serviços | Eventos dos serviços em todas as Regiões, em página pública | Qualquer pessoa, sem login |
| Saúde da sua conta | Eventos que afetam as suas contas e recursos | Todos os clientes, sem configuração |
| Visão organizacional | Eventos de todas as contas da organização | Equipe de operações da rede |
| Integração com o EventBridge | Reage automaticamente aos eventos | Avisar a equipe ou abrir um chamado |
| AWS Health API | Consulta dos eventos por programa | Planos Business Support+, Enterprise ou Unified Operations |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Custo do Health Dashboard | Sem custo adicional | 06/10/2026 |
| Página de saúde dos serviços | Pública, sem login | 06/10/2026 |
| Planos para a Health API | Business Support+, Enterprise ou Unified Operations | 06/10/2026 |

## Como é cobrado

O Health Dashboard não tem custo adicional. O acesso à Health API vem com os planos de suporte que a incluem.

## Não confundir com

| Serviço | Diferença para o Health Dashboard | Pista no enunciado |
|---|---|---|
| [Amazon CloudWatch](cloudwatch.md) | Métricas e alarmes dos seus recursos | "CPU alta na minha instância" |
| [AWS Trusted Advisor](trusted-advisor.md) | Recomendações de boas práticas da conta | "Economizar", "limites de serviço" |
| [AWS CloudTrail](cloudtrail.md) | Quem fez cada ação na conta | "Quem alterou" |
| [Planos de suporte](../custos/planos-de-suporte.md) | Atendimento da AWS e acesso à Health API | "Abrir um caso de suporte" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Health](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html)
- [Saúde dos serviços](https://docs.aws.amazon.com/health/latest/ug/aws-health-dashboard-status.html)
- [Visão organizacional](https://docs.aws.amazon.com/health/latest/ug/aggregate-events.html)
- [Eventos do Health no EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html)
- [AWS Health API](https://docs.aws.amazon.com/health/latest/ug/health-api.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
