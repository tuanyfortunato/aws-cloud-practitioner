# 2.4 Governança multi-conta

> **Domínio 2 — Segurança e Conformidade (30%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS Organizations](../../servicos/gerenciamento/organizations.md) · [AWS Control Tower](../../servicos/gerenciamento/control-tower.md) · [AWS Service Catalog e AWS Resource Access Manager (RAM)](../../servicos/gerenciamento/service-catalog-e-ram.md)

⬅️ [2.3 AWS IAM (Identity and Access Management)](03-iam.md) · 🏠 [Índice do domínio](README.md) · [2.5 Criptografia](05-criptografia.md) ➡️

---

## 📖 Conteúdo

- **AWS Organizations:** gerencia várias contas de forma centralizada.
  - **Conta de gerenciamento (management account)** e **contas-membro**, organizadas em **OUs** (unidades organizacionais) hierárquicas.
  - **SCPs (Service Control Policies):** definem o limite máximo de permissões das contas ou OUs. **Cai na prova:** SCP não concede permissão, só restringe; e não afeta a conta de gerenciamento.
  - **Consolidated billing:** uma fatura única; soma o uso de todas as contas para descontos por volume; compartilha Reserved Instances e Savings Plans entre as contas.
  - Criar contas por API e isolar ambientes (produção, desenvolvimento, segurança).
- **AWS Control Tower:** configura automaticamente um ambiente multi-conta seguro e padronizado (landing zone) sobre o Organizations.
  - **Controles (guardrails):** preventivos (bloqueiam ações, via SCP) e detectivos (detectam desvios, via Config).
  - **Account Factory:** cria contas novas já seguindo o padrão.
  - Painel com o status de conformidade de todas as contas.
- **AWS Resource Access Manager (RAM):** compartilha recursos entre contas (ex.: subnets, Transit Gateways, licenças).
- **AWS Service Catalog:** catálogo de produtos aprovados (templates CloudFormation) que os times podem provisionar sozinhos, dentro das regras da empresa.
- **Cai na prova:** "centralizar contas e aplicar políticas" = Organizations; "montar rapidamente um ambiente multi-conta com boas práticas" = Control Tower; "limitar o que uma conta inteira pode fazer" = SCP.

## ➕ Complemento

- SCPs são herdadas pela hierarquia: uma SCP numa OU vale para todas as contas abaixo dela.
- A permissão efetiva é a interseção entre o que a SCP permite e o que a política IAM concede.
- Estratégia multi-conta recomendada: contas separadas por ambiente e por função (produção, desenvolvimento, segurança, logs), para isolar riscos e custos.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).

- "Como impedir que todas as contas de desenvolvimento usem uma região?" → SCP no Organizations.
- "Uma SCP permite S3, mas o usuário não tem política IAM para S3. Ele consegue acessar?" → Não; a SCP só limita, não concede.
- "Como obter desconto por volume somando o uso de várias contas?" → Consolidated billing no Organizations.
- "Como criar rapidamente um ambiente multi-conta seguro com guardrails?" → AWS Control Tower.
- "Como deixar times criarem só recursos aprovados pela empresa?" → AWS Service Catalog.
- "Como compartilhar uma subnet com outra conta?" → AWS RAM.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [2.3 AWS IAM (Identity and Access Management)](03-iam.md) · 🏠 [Índice do domínio](README.md) · [2.5 Criptografia](05-criptografia.md) ➡️
