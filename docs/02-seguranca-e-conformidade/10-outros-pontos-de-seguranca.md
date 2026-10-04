# 2.10 Outros pontos de segurança

> **Domínio 2 — Segurança e Conformidade (30%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon GuardDuty](../../servicos/seguranca/guardduty.md) · [AWS Security Hub](../../servicos/seguranca/security-hub.md) · [Recursos de ajuda, parceiros e serviços ao cliente (AWS IQ, Managed Services, Professional Services, re:Post…)](../../servicos/custos/recursos-de-ajuda-e-parceiros.md)

⬅️ [2.9 Detecção de ameaças e postura de segurança](09-deteccao-de-ameacas.md) · 🏠 [Índice do domínio](README.md)

---

## 📖 Conteúdo

- **Testes de intrusão (pentest):** permitidos sem aprovação prévia para uma lista de serviços (ex.: EC2, RDS, Lambda); ataques DDoS simulados e alguns testes são proibidos ou exigem aprovação.
- **AWS Trust & Safety:** time para reportar abuso de recursos AWS (spam, phishing, ataques vindos de IPs da AWS).
- **Onde buscar informação de segurança:** AWS Security Center, AWS Security Blog, Security Bulletins, Knowledge Center, AWS re:Post e documentação. Ferramentas de segurança de terceiros: AWS Marketplace.
- **Cai na prova:** "recebi phishing vindo de um IP da AWS" = AWS Trust & Safety.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).

- "É preciso pedir autorização para fazer pentest no EC2?" → Não, para os serviços da lista permitida; simulação de DDoS e alguns testes são proibidos.
- "Uma instância da AWS está enviando spam para a sua empresa. Quem contatar?" → AWS Trust & Safety.
- "Onde encontrar boletins e boas práticas de segurança?" → AWS Security Center, Security Blog e Knowledge Center.
- "Onde comprar ferramentas de segurança de terceiros?" → AWS Marketplace.

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> ✔️ Verificado em fontes oficiais em 04/10/2026 ([relatório](../../fontes/verificacao-pendencias-2026-10-rodada-2.md)), na página [Penetration Testing](https://aws.amazon.com/security/penetration-testing/).

- **Pentest sem aprovação prévia** (na infraestrutura do próprio cliente): EC2, WAF, NAT Gateways, ELB, RDS, Aurora, CloudFront, API Gateway, AppSync, Lambda e Lambda@Edge, Lightsail, Elastic Beanstalk, ECS, Fargate, OpenSearch, FSx, Transit Gateway, Global Accelerator e Bedrock AgentCore.
- **Exige aprovação prévia:** qualquer teste que inclua *Command and Control* (C2).
- **Proibido:** enumeração de zonas, sequestro (*hijacking*) e *pharming* de DNS via Route 53; DoS/DDoS e simulações de DoS (salvo a política própria); *flooding* de portas, protocolos e requisições; tomada (*takeover*) de buckets S3 e de subdomínios.
- **Simulação de DDoS:** tem política própria — só com parceiro de testes pré-aprovado, com Shield Advanced e respeitando limites de volume.
- 📌 Na prova: "pentest no EC2 precisa de autorização?" → **não**; "simular DDoS livremente?" → **não**.
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [2.9 Detecção de ameaças e postura de segurança](09-deteccao-de-ameacas.md) · 🏠 [Índice do domínio](README.md)
