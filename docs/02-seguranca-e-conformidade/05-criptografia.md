# 2.5 Criptografia

> **Domínio 2 — Segurança e Conformidade (30%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS KMS (Key Management Service)](../../servicos/seguranca/kms.md) · [AWS CloudHSM](../../servicos/seguranca/cloudhsm.md) · [AWS Certificate Manager (ACM) e AWS Private CA](../../servicos/seguranca/certificate-manager.md) · [Amazon S3 (Simple Storage Service)](../../servicos/armazenamento/s3.md)

⬅️ [2.4 Governança multi-conta](04-governanca-multi-conta.md) · 🏠 [Índice do domínio](README.md) · [2.6 Compliance e governança](06-compliance-e-governanca.md) ➡️

---

## 🧠 Antes de começar

> 💡 **Em palavras simples:** Criptografar é **embaralhar os dados** para que só quem tem a chave consiga ler. Este tópico mostra quando criptografar (guardado ou trafegando) e qual serviço cuida das chaves e dos certificados.
>
> 🏠 **Analogia:** a criptografia é um **cadeado**; a chave é o que abre. O **KMS** é um chaveiro gerenciado pela AWS; o **CloudHSM** é um **cofre só seu**; o **ACM** fornece o cadeado do HTTPS (o ícone de cadeado no navegador).

**Ao terminar este tópico, você deve saber:**

- [ ] Diferenciar criptografia **em repouso** de **em trânsito**.
- [ ] Diferenciar **KMS** (chaves gerenciadas e integradas) de **CloudHSM** (hardware dedicado, só você controla).
- [ ] Saber que o **ACM** emite e renova certificados SSL/TLS e que o S3 criptografa objetos novos por padrão.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Em repouso** | dados guardados em disco, banco ou bucket. |
| **Em trânsito** | dados viajando pela rede. |
| **HSM** | equipamento físico feito para guardar chaves com segurança. |
| **TLS/SSL** | o protocolo que protege o HTTPS. |

> 🎯 **Como não errar na prova:** "Hardware **dedicado**" ou "controle **exclusivo** das chaves" → **CloudHSM**. "Chaves integradas aos serviços" → **KMS**. "Certificado HTTPS" → **ACM**. Quem **ativa** a criptografia dos dados é o **cliente**.

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

<!-- aprofundamento:inicio -->
## 🔬 Aprofundamento para a prova — sem abrir o console

**Como funciona:** TLS protege o caminho da comunicação; criptografia em repouso protege os dados armazenados. KMS administra chaves e autoriza operações criptográficas; ACM administra certificados.

**Como escolher:** Necessidade de chave para EBS/S3: KMS. Certificado TLS: ACM. HSM dedicado com controle de usuários e chaves: CloudHSM. Segredo de aplicação: Secrets Manager.

**O que não concluir:** Dado criptografado não fica automaticamente inacessível a um usuário autorizado. Criptografia não substitui IAM, backup ou requisitos de localização dos dados.

### Exercício de decisão

Um arquivo está em S3 com SSE-KMS. Dar apenas permissão de leitura no S3 é suficiente?

<details>
<summary>Resposta e por que as alternativas confundem</summary>

Pode não ser: o leitor também precisa de autorização adequada para usar a chave KMS. Criptografia e acesso ao objeto são camadas diferentes.

</details>

**Verifique seu entendimento:** explique a escolha em voz alta e cite uma condição que mudaria a resposta. Nomear um serviço sem explicar o motivo ainda não demonstra domínio.

> Escopo e limites de estudo: [como estudar sem console](../00-guia-do-exame/estudar-sem-console.md). Os cenários são autorais; não são questões oficiais nem previsão do que cairá.
<!-- aprofundamento:fim -->

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
