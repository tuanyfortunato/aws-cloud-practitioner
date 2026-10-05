# AWS WAF (Web Application Firewall)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Um site precisa analisar pedidos web e bloquear padrões indesejados, como tentativas de explorar campos de entrada ou volumes excessivos de chamadas.

**Como este serviço ajuda?** WAF aplica regras ao tráfego web em integrações compatíveis. Você define critérios de inspeção e ações como permitir ou bloquear.

**Exemplo do dia a dia:** A escola configura regras para inspecionar pedidos ao seu site e limitar padrões de requisições suspeitos.

**O que ele não resolve sozinho?** WAF não corrige o código vulnerável nem protege automaticamente todo protocolo e recurso AWS. A regra deve estar associada ao ponto de entrada compatível.

**Primeiras palavras para entender:**

- **Requisição:** pedido feito ao site.
- **Regra:** condição e ação de inspeção.
- **Web ACL:** conjunto de regras aplicado pelo WAF.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança / proteção de aplicações · **Domínio:** 2 · **Escopo:** Global (CloudFront) ou Regional · **Tópico do guia:** [2.8 Proteção de rede e aplicações](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)
>
> **Em uma frase:** firewall de **camada 7** que filtra requisições HTTP(S) maliciosas antes que cheguem à aplicação.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Onde se associa

**CloudFront, ALB, API Gateway (REST), AppSync, Cognito user pools**, App Runner, Verified Access, Amplify. ⚠️ **Não** em NLB nem diretamente em EC2.

## Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Web ACL** | Conjunto de regras com ação padrão (allow/block). |
| **Rules** | Condições: IP sets, países (**geo match**), strings/regex, tamanho, cabeçalhos, **SQL injection**, **XSS**. Ações: allow, block, count, CAPTCHA, challenge. |
| **Rate-based rules** | Limitam requisições por IP (ou chave) em uma janela → mitigam *HTTP floods*, *brute force*. |
| **Managed rule groups** | Prontos da AWS (Core rule set, SQLi, IP reputation, bots conhecidos, OWASP) e do **Marketplace**. |
| **Bot Control** | Identifica e controla bots (pago). |
| **Fraud Control** | Proteção contra tomada de conta (ATP) e criação fraudulenta de contas (ACFP). |
| **Logs** | Para CloudWatch Logs, S3 ou Firehose. |
| **Capacidade (WCU)** | Cada regra consome unidades 🧊. |

## Cobrança

- Por Web ACL/mês + por regra/mês + por milhão de requisições; extras para Bot/Fraud Control (🧊 valores). Sem custo extra nos recursos protegidos pelo Shield Advanced.

## ⚠️ Pegadinhas

- WAF (aplicação, camada 7) × Shield (DDoS, camadas 3/4) × Network Firewall (VPC, camadas 3–7) × Security group/NACL.
- "Bloquear países" → WAF geo match ou geo restriction do CloudFront.
- "Mesmas regras em todas as contas" → **Firewall Manager**.

## ❓ Perguntas típicas

- "Bloquear SQL injection e XSS." → WAF.
- "Limitar requisições por IP." → Rate-based rule do WAF.
- "Em quais serviços o WAF pode ser usado?" → CloudFront, ALB, API Gateway, AppSync, Cognito.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Web ACL, rules, rule groups e associação a recursos |
| **O que você decide/configura?** | Critérios HTTP, rate-based rules, ação e logging |
| **Em que ordem as coisas acontecem?** | Requisição é avaliada pelas regras antes de seguir ao recurso |
| **O que pode fazer, e em que condição?** | Pode permitir, bloquear ou contar conforme regras e suporte |
| **O que não pode presumir?** | Não é firewall universal de toda EC2 nem corrige a causa no código |

**Caso comentado:** SQL injection em aplicação web suportada: WAF; modo Count ajuda a avaliar regra antes de bloquear.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html)
