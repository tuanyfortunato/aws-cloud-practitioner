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

## 1. A sequência de funcionamento

**Passo 1.** Identifique os recursos e o tipo de exposição que precisam de proteção contra sobrecarga.

**Passo 2.** Avalie a modalidade e sua cobertura para a arquitetura. Os mecanismos de proteção atuam conforme suas condições.

**Passo 3.** Observe eventos e prepare resposta. Proteção contra DDoS não corrige vulnerabilidades do código nem substitui todos os controles de aplicação.

## 2. Recursos e opções, com significado

### Standard × Advanced

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

A assinatura do Advanced cobre **todas as contas** da Organization.

✔️ Para acionar o SRT é preciso plano **Business Support+, Enterprise ou Unified Operations** (a fonte cita "Business Support") (documentação do AWS CloudFormation, 10/2026) e uma IAM role que autorize o SRT (política gerenciada `AWSShieldDRTAccessPolicy`).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Shield não elimina todos os riscos de segurança nem substitui regras de acesso, proteção da aplicação ou planejamento de capacidade. Standard e Advanced têm condições diferentes.

### ⚠️ Pegadinhas

"DDoS volumétrico" → Shield. "SQL injection/XSS" → WAF.

"Reembolso do custo de escalonamento + especialistas 24/7" → **Shield Advanced**.

"Proteção DDoS que todo cliente tem sem custo" → **Shield Standard**.

## 4. Caso resolvido: ligando as peças

Um site público usa os recursos de proteção aplicáveis à sua arquitetura para reduzir o impacto de tentativas de sobrecarga.

**Aplicando a sequência à situação:**

**Etapa 1:** Identifique os recursos e o tipo de exposição que precisam de proteção contra sobrecarga.
**Etapa 2:** Avalie a modalidade e sua cobertura para a arquitetura. Os mecanismos de proteção atuam conforme suas condições.
**Etapa 3:** Observe eventos e prepare resposta. Proteção contra DDoS não corrige vulnerabilidades do código nem substitui todos os controles de aplicação.

**Resultado e responsabilidade:** Shield oferece proteção contra ataques de negação de serviço distribuídos, com diferenças de cobertura e recursos entre suas modalidades.

**Recursos envolvidos:** Proteção Standard e assinatura Advanced para recursos elegíveis.

**Decisões que precisam ser tomadas:** Recursos protegidos e recursos extras contratados.

**Outra situação comentada:** Ataque volumétrico: Shield; requisição HTTP maliciosa: WAF pode complementar.

**Por que não concluir mais do que isso:** Não equivale a filtro de SQL injection nem corrige vulnerabilidades no código

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Qual proteção DDoS todo cliente tem sem custo?"

**Resposta curta:** Shield Standard.

**Pergunta:** "Acesso a especialistas 24/7 e proteção de custo durante ataques."

**Resposta curta:** Shield Advanced.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
