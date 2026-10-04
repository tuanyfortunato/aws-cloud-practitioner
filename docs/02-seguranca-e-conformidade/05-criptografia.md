# 2.5 Criptografia

> **Domínio 2 — Segurança e Conformidade (30%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS KMS (Key Management Service)](../../servicos/seguranca/kms.md) · [AWS CloudHSM](../../servicos/seguranca/cloudhsm.md) · [AWS Certificate Manager (ACM) e AWS Private CA](../../servicos/seguranca/certificate-manager.md) · [Amazon S3 (Simple Storage Service)](../../servicos/armazenamento/s3.md)

⬅️ [2.4 Governança multi-conta](04-governanca-multi-conta.md) · 🏠 [Índice do domínio](README.md) · [2.6 Compliance e governança](06-compliance-e-governanca.md) ➡️

---

## 📖 Conteúdo

- **Em repouso (at rest):** dados armazenados (S3, EBS, RDS, DynamoDB) criptografados com chaves do KMS.
- **Em trânsito (in transit):** dados trafegando pela rede, protegidos com TLS/SSL (HTTPS).
- **AWS KMS (Key Management Service):** cria e gerencia chaves de criptografia; integrado à maioria dos serviços.
  - **AWS owned keys** (invisíveis para você), **AWS managed keys** (criadas pela AWS na sua conta para um serviço) e **customer managed keys** (criadas e controladas por você, com política de chave, rotação e auditoria).
  - Toda utilização de chave fica registrada no CloudTrail.
  - As chaves ficam em HSMs compartilhados e gerenciados pela AWS; são regionais.
- **AWS CloudHSM:** HSM **dedicado e exclusivo** (single-tenant) na nuvem. Você gerencia as chaves e a AWS não tem acesso a elas. Para exigências regulatórias fortes.
- **AWS Certificate Manager (ACM):** emite, gerencia e **renova automaticamente** certificados SSL/TLS. Certificados públicos do ACM são gratuitos e usados em ELB, CloudFront e API Gateway.
- **S3:** todo objeto novo é criptografado por padrão com SSE-S3. Opções: SSE-S3 (chave da AWS), SSE-KMS (chave do KMS, com auditoria), SSE-C (chave fornecida pelo cliente) e criptografia no lado do cliente.
- **Cai na prova:** "chave controlada pelo cliente em hardware dedicado" = CloudHSM; "criar e gerenciar chaves integradas aos serviços" = KMS; "certificado HTTPS para o load balancer" = ACM; "quem ativa a criptografia dos dados?" = cliente.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).

- "Qual serviço cria e controla chaves de criptografia integradas a S3, EBS e RDS?" → AWS KMS.
- "A empresa exige HSM dedicado, com chaves sob controle exclusivo dela." → AWS CloudHSM.
- "Como obter certificados SSL/TLS gratuitos com renovação automática?" → AWS Certificate Manager.
- "Como proteger dados em trânsito?" → TLS/HTTPS. "E em repouso?" → Criptografia com KMS.
- "Quem é responsável por ativar a criptografia dos dados?" → O cliente.
- "Como auditar quem usou uma chave do KMS?" → CloudTrail.

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- **KMS × CloudHSM (📌):** "hardware **single-tenant**, controle **exclusivo** das chaves, FIPS 140 nível 3" → **CloudHSM**. "Chaves gerenciadas e integradas a vários serviços" → **KMS**.
- 🔄 O ACM passou a oferecer **certificados públicos exportáveis** (pagos) para uso fora dos serviços integrados. Na prova continua valendo: "certificado público gratuito com renovação automática para ELB/CloudFront" → ACM.
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [2.4 Governança multi-conta](04-governanca-multi-conta.md) · 🏠 [Índice do domínio](README.md) · [2.6 Compliance e governança](06-compliance-e-governanca.md) ➡️
