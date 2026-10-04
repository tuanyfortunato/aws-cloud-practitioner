# AWS WAF (Web Application Firewall)

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

## 🔗 Documentação oficial

- [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html)
