# 2.8 Proteção de rede e aplicações

> **Domínio 2 — Segurança e Conformidade (30%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon VPC (Virtual Private Cloud)](../../servicos/redes/vpc.md) · [AWS Shield](../../servicos/seguranca/shield.md) · [AWS WAF (Web Application Firewall)](../../servicos/seguranca/waf.md) · [AWS Firewall Manager e AWS Network Firewall](../../servicos/seguranca/firewall-manager-e-network-firewall.md)

⬅️ [2.7 Logs, monitoramento e auditoria](07-logs-monitoramento-e-auditoria.md) · 🏠 [Índice do domínio](README.md) · [2.9 Detecção de ameaças e postura de segurança](09-deteccao-de-ameacas.md) ➡️

---

## 📖 Conteúdo

- **Security group:** Firewall virtual no nível da **instância/ENI**. **Stateful** (a resposta volta automaticamente); só tem regras de **permissão**; por padrão bloqueia toda entrada e libera toda saída.
- **Network ACL (NACL):** firewall no nível da **subnet**. **Stateless** (precisa liberar entrada e saída); tem regras de **permitir e negar**, avaliadas em ordem numérica. A NACL padrão libera tudo.
- **AWS Shield:** proteção contra **DDoS**.
  - **Shield Standard:** gratuito e automático para todos os clientes, protege contra ataques comuns de camada 3 e 4.
  - **Shield Advanced:** pago, com proteção ampliada (inclusive camada 7 junto com o WAF), acesso 24/7 ao **Shield Response Team (SRT)**, visibilidade dos ataques e **proteção de custo** (créditos pelo aumento de uso causado por ataque).
- **AWS WAF:** firewall de **aplicação web (camada 7)**. Usa web ACLs com regras para bloquear SQL injection, XSS, IPs, países (geo) e limitar requisições (rate-based). Tem regras gerenciadas prontas. Associado a **CloudFront, ALB, API Gateway, AppSync e Cognito**.
- **AWS Firewall Manager:** gerencia de forma central regras de WAF, Shield Advanced, security groups e firewalls de rede em **todas as contas** do Organizations.
- **Cai na prova:** "bloquear um IP específico na subnet" = NACL (security group não nega); "ataque de SQL injection" = WAF; "ataque DDoS volumétrico" = Shield; "time especialista 24/7 durante ataque DDoS" = Shield Advanced.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).

- "Qual firewall atua no nível da instância e é stateful?" → Security group.
- "Qual firewall atua no nível da subnet e é stateless?" → Network ACL.
- "Como bloquear um endereço IP malicioso?" → Regra de negação na NACL (ou regra no WAF para tráfego web).
- "Qual proteção DDoS todo cliente tem sem custo?" → Shield Standard.
- "Qual serviço dá acesso a especialistas 24/7 e proteção de custo durante ataques DDoS?" → Shield Advanced.
- "Como bloquear SQL injection e XSS?" → AWS WAF.
- "Como bloquear acesso de certos países ao site?" → WAF (regra geográfica) ou restrição geográfica do CloudFront.
- "Em quais serviços o WAF pode ser usado?" → CloudFront, ALB, API Gateway, AppSync e Cognito.
- "Como aplicar as mesmas regras de WAF em todas as contas?" → AWS Firewall Manager.

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- **Shield Advanced (📌):** **US$ 3.000/mês por organização**, compromisso mínimo de **1 ano**, mais data transfer out dos recursos protegidos. Inclui camada 7 (com WAF), **Shield Response Team 24/7**, **proteção de custo** (créditos por escalonamento causado por DDoS) e **WAF sem custo adicional** nos recursos protegidos. A taxa cobre todas as contas da Organization.
  - *Questão-modelo:* "reembolso de custos de escalonamento causados por DDoS + especialistas 24/7" → **Shield Advanced**.
- **WAF:** cobra por Web ACL, por regra e por milhão de requisições (🧊 valores). Camada 7: SQL injection, XSS, rate-based rules, geo-blocking. ⚠️ Atua em CloudFront, ALB, API Gateway, AppSync e Cognito — **não** atua em NLB.
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [2.7 Logs, monitoramento e auditoria](07-logs-monitoramento-e-auditoria.md) · 🏠 [Índice do domínio](README.md) · [2.9 Detecção de ameaças e postura de segurança](09-deteccao-de-ameacas.md) ➡️
