<!-- autoral -->

# AWS Shield

> **Categoria:** Segurança e proteção contra DDoS · **Domínio:** 2 · **Abrangência:** Recursos de borda e regionais · **Ficha:** núcleo
>
> **Em uma frase:** protege as aplicações contra ataques de negação de serviço distribuído (DDoS), de graça no nível Standard e com equipe de resposta e proteção de custo no Advanced.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.8 Proteção de rede e aplicações](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

No primeiro dia de matrícula, o portal da escola recebe uma enxurrada de pedidos vindos de milhares de máquinas ao mesmo tempo. Não é procura de verdade: é um **ataque de negação de serviço distribuído** (DDoS), feito para esgotar a capacidade do site e tirá-lo do ar para os alunos.

O **Shield Standard** já protege todos os clientes da AWS, sem custo adicional e sem ativar nada, contra os ataques mais comuns nas camadas de rede e de transporte. Quem precisa de mais contrata o **Shield Advanced**: proteção contra ataques maiores e na camada de aplicação, visibilidade dos ataques quase em tempo real, a equipe de resposta a DDoS da AWS e créditos pelo aumento de cobrança causado pelo ataque.

O limite: o Shield cuida do volume, não do conteúdo dos pedidos. Um texto malicioso digitado no formulário de busca (injeção de SQL) é trabalho do [WAF](waf.md). E o Advanced só protege os recursos que você indicar.

## Como funciona

1. O Shield Standard atua automaticamente quando você usa serviços como CloudFront, Route 53 e Elastic Load Balancing.
2. Para o Advanced, você assina o serviço (compromisso de um ano) e escolhe os recursos protegidos, como distribuições CloudFront, zonas do Route 53, aceleradores do Global Accelerator, Elastic IPs e load balancers.
3. Durante um ataque, o Advanced mostra métricas e diagnóstico; com um plano de suporte Business ou Enterprise, você aciona o **Shield Response Team** (SRT).
4. Depois do ataque, você pede créditos pelo aumento de uso que ele causou nos recursos protegidos.

## Opções principais

| | Shield Standard | Shield Advanced |
|---|---|---|
| Custo | Sem custo adicional | Taxa mensal por organização, compromisso de 1 ano, mais transferência de dados dos recursos protegidos |
| Ativação | Automática | Assinatura e escolha dos recursos |
| Ataques | Rede e transporte, os mais comuns | Também maiores, mais sofisticados e na camada de aplicação (com o WAF) |
| Equipe de resposta | Não | SRT 24 horas, com plano Business ou Enterprise |
| Proteção de custo | Não | Créditos pelo aumento de cobrança causado por DDoS |
| WAF | Pago à parte | Taxas padrão do WAF incluídas nos recursos protegidos |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Shield Standard | Sem custo adicional | 06/10/2026 |
| Shield Advanced | US$ 3.000 por mês por organização, mais transferência de dados | 06/10/2026 |
| Compromisso do Advanced | 1 ano | 06/10/2026 |
| Plano para acionar o SRT | Business ou Enterprise | 06/10/2026 |

## Como é cobrado

O Standard não tem custo adicional. O Advanced cobra a taxa mensal por organização, que cobre todas as contas dela, mais uma taxa de uso pela transferência de dados que sai de CloudFront, ELB, EC2 e Global Accelerator protegidos. Os benefícios, inclusive a proteção de custo, dependem de cumprir o compromisso de um ano.

## Não confundir com

| Serviço | Diferença para o Shield | Pista no enunciado |
|---|---|---|
| [AWS WAF](waf.md) | Filtra o conteúdo dos pedidos HTTP | "Injeção de SQL", "XSS", "bloquear país" |
| [AWS Firewall Manager](firewall-manager-e-network-firewall.md) | Aplica WAF, Shield Advanced e outras regras em todas as contas | "Mesmas regras em toda a organização" |
| [Amazon GuardDuty](guardduty.md) | Detecta ameaças nos registros da conta | "Atividade suspeita", "credencial comprometida" |
| Security groups ([VPC](../redes/vpc.md)) | Firewall de portas e endereços do recurso | "Liberar a porta 443" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [AWS Shield Standard](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-standard-summary.html)
- [AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary.html)
- [Recursos que o Shield Advanced protege](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary-protected-resources.html)
- [Shield Response Team](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-srt-support.html)
- [Preços do AWS Shield](https://aws.amazon.com/shield/pricing/)
- [Perguntas frequentes do AWS Shield](https://aws.amazon.com/shield/faqs/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
