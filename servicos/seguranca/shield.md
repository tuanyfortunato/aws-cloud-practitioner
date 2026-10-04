# AWS Shield

> **Categoria:** Segurança / proteção DDoS · **Domínio:** 2 · **Escopo:** Global (borda) e regional · **Tópico do guia:** [2.8 Proteção de rede e aplicações](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)
>
> **Em uma frase:** proteção gerenciada contra ataques de negação de serviço distribuída (DDoS).
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Standard × Advanced

| | **Shield Standard** | **Shield Advanced** |
|---|---|---|
| Custo | **Gratuito**, automático para todos | 📌 **US$ 3.000/mês por organização**, compromisso de **1 ano** + data transfer out dos recursos protegidos |
| Camadas | 3 e 4 (SYN flood, UDP reflection…) | 3, 4 e **7** (com WAF) |
| Recursos | Todos (melhor em CloudFront e Route 53) | EC2 (Elastic IP), ELB, CloudFront, Route 53, Global Accelerator |
| Time de resposta | — | **Shield Response Team (SRT) 24/7** |
| **Proteção de custo** | — | **Créditos** pelo aumento de uso (escalonamento) causado por DDoS |
| Visibilidade | Básica | Métricas, relatórios e diagnóstico de ataques em tempo quase real |
| WAF | Pago à parte | **Sem custo adicional** nos recursos protegidos |
| Outros | — | Detecção e mitigação automática na camada 7, health-based detection, proteção de grupos, integração com Firewall Manager |

- A assinatura do Advanced cobre **todas as contas** da Organization.
- A documentação do SRT ainda exige plano **Business ou Enterprise** (nomes antigos); qual plano novo atende não foi encontrado na verificação de 10/2026 — na prática, Business Support+ ou superior.

## ⚠️ Pegadinhas

- "DDoS volumétrico" → Shield. "SQL injection/XSS" → WAF.
- "Reembolso do custo de escalonamento + especialistas 24/7" → **Shield Advanced**.
- "Proteção DDoS que todo cliente tem sem custo" → **Shield Standard**.

## ❓ Perguntas típicas

- "Qual proteção DDoS todo cliente tem sem custo?" → Shield Standard.
- "Acesso a especialistas 24/7 e proteção de custo durante ataques." → Shield Advanced.

## 🔗 Documentação oficial

- [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html)
