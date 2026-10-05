# AWS Shield

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Muitos pedidos maliciosos podem tentar sobrecarregar um serviço e impedir que pessoas legítimas o utilizem.

**Como este serviço ajuda?** Shield oferece proteção contra ataques de negação de serviço distribuídos, com diferenças de cobertura e recursos entre suas modalidades.

**Exemplo do dia a dia:** Um site público usa os recursos de proteção aplicáveis à sua arquitetura para reduzir o impacto de tentativas de sobrecarga.

**O que ele não resolve sozinho?** Shield não elimina todos os riscos de segurança nem substitui regras de acesso, proteção da aplicação ou planejamento de capacidade. Standard e Advanced têm condições diferentes.

**Primeiras palavras para entender:**

- **DDoS:** ataque distribuído para sobrecarregar um serviço.
- **Disponibilidade:** conseguir usar o sistema quando necessário.
- **Mitigação:** reduzir o impacto de um ataque.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

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
- ✔️ Para acionar o SRT é preciso plano **Business Support+, Enterprise ou Unified Operations** (a fonte cita "Business Support") (documentação do AWS CloudFormation, 10/2026) e uma IAM role que autorize o SRT (política gerenciada `AWSShieldDRTAccessPolicy`).

## ⚠️ Pegadinhas

- "DDoS volumétrico" → Shield. "SQL injection/XSS" → WAF.
- "Reembolso do custo de escalonamento + especialistas 24/7" → **Shield Advanced**.
- "Proteção DDoS que todo cliente tem sem custo" → **Shield Standard**.

## ❓ Perguntas típicas

- "Qual proteção DDoS todo cliente tem sem custo?" → Shield Standard.
- "Acesso a especialistas 24/7 e proteção de custo durante ataques." → Shield Advanced.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Proteção Standard e assinatura Advanced para recursos elegíveis |
| **O que você decide/configura?** | Recursos protegidos e recursos extras contratados |
| **Em que ordem as coisas acontecem?** | Proteção e mitigação atuam contra ataques DDoS conforme cobertura |
| **O que pode fazer, e em que condição?** | Standard cobre proteção básica; Advanced acrescenta capacidades e apoio |
| **O que não pode presumir?** | Não equivale a filtro de SQL injection nem corrige vulnerabilidades no código |

**Caso comentado:** Ataque volumétrico: Shield; requisição HTTP maliciosa: WAF pode complementar.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html)
