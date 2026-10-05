# 2.10 Outros pontos de segurança

> **Domínio 2 — Segurança e Conformidade (30%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon GuardDuty](../../servicos/seguranca/guardduty.md) · [AWS Security Hub](../../servicos/seguranca/security-hub.md) · [Recursos de ajuda, parceiros e serviços ao cliente (AWS IQ, Managed Services, Professional Services, re:Post…)](../../servicos/custos/recursos-de-ajuda-e-parceiros.md)

⬅️ [2.9 Detecção de ameaças e postura de segurança](09-deteccao-de-ameacas.md) · 🏠 [Índice do domínio](README.md)

---

## 🧠 Antes de começar

> 💡 **Em palavras simples:** Pontos soltos de segurança: o que pode ser testado sem pedir autorização, **a quem denunciar abuso** vindo da AWS e **onde buscar informação** de segurança.
>
> 🏠 **Analogia:** o **Trust & Safety** é a **ouvidoria** da AWS para denúncias: se alguém usa a AWS para te atacar (spam, phishing), é para lá que você reclama — não para o suporte técnico.

**Ao terminar este tópico, você deve saber:**

- [ ] Saber que **pentest** é permitido sem aprovação prévia numa lista de serviços, mas DDoS simulado não.
- [ ] Saber que abuso vindo de IPs da AWS vai para o **AWS Trust & Safety**.
- [ ] Citar fontes de informação de segurança (Security Center, Security Blog, Bulletins, re:Post, Knowledge Center).

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Pentest** | teste de intrusão: atacar o próprio sistema, de propósito, para achar falhas. |
| **Phishing** | golpe que imita uma empresa para roubar dados. |

> 🎯 **Como não errar na prova:** "Recebi spam/phishing **vindo de um IP da AWS**" → **Trust & Safety**. "Ferramenta de segurança de terceiros" → **Marketplace**.

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

<!-- aprofundamento:inicio -->
## 🔬 Aprofundamento para a prova — sem abrir o console

**Como funciona:** Documentação, Security Blog e Knowledge Center explicam práticas e problemas; Marketplace oferece soluções de terceiros; Trust and Safety recebe denúncias de abuso.

**Como escolher:** Diferencie proteção da sua carga, suporte técnico e denúncia de atividade abusiva em recursos AWS. As ferramentas cumprem papéis complementares.

**O que não concluir:** Comprar um produto de segurança não transfere todas as obrigações ao fornecedor. Testes de segurança devem observar a política AWS e a titularidade dos recursos.

### Exercício de decisão

Uma empresa recebe tráfego abusivo de um recurso AWS de outra conta. Deve tentar alterar esse recurso com IAM?

<details>
<summary>Resposta e por que as alternativas confundem</summary>

Não. Pode denunciar ao Trust and Safety com evidências. Suas permissões IAM administram recursos autorizados, não os de terceiros.

</details>

**Verifique seu entendimento:** explique a escolha em voz alta e cite uma condição que mudaria a resposta. Nomear um serviço sem explicar o motivo ainda não demonstra domínio.

> Escopo e limites de estudo: [como estudar sem console](../00-guia-do-exame/estudar-sem-console.md). Os cenários são autorais; não são questões oficiais nem previsão do que cairá.
<!-- aprofundamento:fim -->

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
