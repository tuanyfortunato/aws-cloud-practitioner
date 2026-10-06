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

## 1. A sequência de funcionamento

**Passo 1.** Identifique o ponto web compatível e o padrão de pedidos que deseja permitir, observar ou bloquear.

**Passo 2.** Crie regras e associe o conjunto ao recurso. Os pedidos são inspecionados conforme a configuração.

**Passo 3.** Acompanhe resultados e ajuste regras. Um bloqueio incorreto pode afetar usuários legítimos; a correção do programa também precisa ser planejada.

## 2. Recursos e opções, com significado

### Onde se associa

**CloudFront, ALB, API Gateway (REST), AppSync, Cognito user pools**, App Runner, Verified Access, Amplify. ⚠️ **Não** em NLB nem diretamente em EC2.

### Conceitos e configurações

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

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

WAF não corrige o código vulnerável nem protege automaticamente todo protocolo e recurso AWS. A regra deve estar associada ao ponto de entrada compatível.

### ⚠️ Pegadinhas

WAF (aplicação, camada 7) × Shield (DDoS, camadas 3/4) × Network Firewall (VPC, camadas 3–7) × Security group/NACL.

"Bloquear países" → WAF geo match ou geo restriction do CloudFront.

"Mesmas regras em todas as contas" → **Firewall Manager**.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por Web ACL/mês + por regra/mês + por milhão de requisições; extras para Bot/Fraud Control (🧊 valores). Sem custo extra nos recursos protegidos pelo Shield Advanced.

## 5. Caso resolvido: ligando as peças

A escola configura regras para inspecionar pedidos ao seu site e limitar padrões de requisições suspeitos.

**Aplicando a sequência à situação:**

**Etapa 1:** Identifique o ponto web compatível e o padrão de pedidos que deseja permitir, observar ou bloquear.
**Etapa 2:** Crie regras e associe o conjunto ao recurso. Os pedidos são inspecionados conforme a configuração.
**Etapa 3:** Acompanhe resultados e ajuste regras. Um bloqueio incorreto pode afetar usuários legítimos; a correção do programa também precisa ser planejada.

**Resultado e responsabilidade:** WAF aplica regras ao tráfego web em integrações compatíveis. Você define critérios de inspeção e ações como permitir ou bloquear.

**Recursos envolvidos:** Web ACL, rules, rule groups e associação a recursos.

**Decisões que precisam ser tomadas:** Critérios HTTP, rate-based rules, ação e logging.

**Outra situação comentada:** SQL injection em aplicação web suportada: WAF; modo Count ajuda a avaliar regra antes de bloquear.

**Por que não concluir mais do que isso:** Não é firewall universal de toda EC2 nem corrige a causa no código

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Bloquear SQL injection e XSS."

**Resposta curta:** WAF.

**Pergunta:** "Limitar requisições por IP."

**Resposta curta:** Rate-based rule do WAF.

**Pergunta:** "Em quais serviços o WAF pode ser usado?"

**Resposta curta:** CloudFront, ALB, API Gateway, AppSync, Cognito.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
