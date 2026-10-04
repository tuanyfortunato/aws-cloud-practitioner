# 2.2 Usuário root

> **Domínio 2 — Segurança e Conformidade (30%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS IAM (Identity and Access Management) e AWS STS](../../servicos/seguranca/iam.md)

⬅️ [2.1 Modelo de responsabilidade compartilhada](01-responsabilidade-compartilhada.md) · 🏠 [Índice do domínio](README.md) · [2.3 AWS IAM (Identity and Access Management)](03-iam.md) ➡️

---

## 📖 Conteúdo

- Criado junto com a conta, com o e-mail de cadastro; tem acesso irrestrito e não pode ser limitado por políticas IAM.
- **Boas práticas:** ativar MFA, não criar access keys (apagar se existirem), usar só para tarefas que exigem root, criar usuários/identidades administrativas para o dia a dia, senha forte e e-mail protegido.
- **Tarefas que só o root pode fazer:**
  - Alterar configurações da conta (nome da conta, e-mail, senha do root e access keys do root).
  - Fechar a conta AWS.
  - Mudar ou cancelar o plano de AWS Support.
  - Restaurar permissões de um administrador IAM que se trancou fora.
  - Ativar o acesso de usuários IAM ao console de Billing.
  - Registrar-se como vendedor no Reserved Instance Marketplace.
  - Configurar MFA Delete em um bucket S3.
  - Editar ou apagar uma política de bucket S3 que bloqueou todo mundo.
- **Cai na prova:** "qual tarefa exige o usuário root?" com uma lista de opções. Criar usuários IAM e ver a fatura **não** exigem root.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).

- "Qual é a boa prática para o usuário root?" → Ativar MFA, não criar access keys e usá-lo só para tarefas que o exigem.
- "Qual destas tarefas exige o root?" → Fechar a conta, mudar o plano de suporte, alterar dados da conta ou restaurar permissões de administrador.
- "Qual tarefa NÃO exige o root?" → Criar usuários IAM, ver a fatura (com permissão) ou lançar instâncias.
- "O que fazer logo após criar a conta?" → Proteger o root com MFA e criar identidades administrativas para o dia a dia.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [2.1 Modelo de responsabilidade compartilhada](01-responsabilidade-compartilhada.md) · 🏠 [Índice do domínio](README.md) · [2.3 AWS IAM (Identity and Access Management)](03-iam.md) ➡️
