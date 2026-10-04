# 2.2 Usuário root

> **Domínio 2 — Segurança e Conformidade (30%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS IAM (Identity and Access Management) e AWS STS](../../servicos/seguranca/iam.md)

> ⚠️ **Atualização do exam guide (verificado em 04/10/2026):** A lista oficial de tarefas do root mudou: **alterar o nome da conta** e **mudar o plano de suporte não exigem mais o root**. Continuam exclusivos, entre outros: alterar e-mail/senha do root, fechar conta standalone, restaurar administrador IAM, MFA Delete e desbloquear políticas de S3/SQS. [Ver escopo oficial](../00-guia-do-exame/escopo-oficial.md).

⬅️ [2.1 Modelo de responsabilidade compartilhada](01-responsabilidade-compartilhada.md) · 🏠 [Índice do domínio](README.md) · [2.3 AWS IAM (Identity and Access Management)](03-iam.md) ➡️

---

## 🧠 Antes de começar

> 💡 **Em palavras simples:** O usuário root é o **dono da conta**, criado com o e-mail de cadastro. Ele pode tudo e não pode ser limitado por IAM — por isso deve ser protegido e usado só nas poucas tarefas que exigem ele.
>
> 🏠 **Analogia:** é a **chave-mestra do prédio**: abre todas as portas, então fica guardada no cofre (com MFA) e só sai para situações especiais. No dia a dia, cada um usa o próprio crachá (identidades IAM).

**Ao terminar este tópico, você deve saber:**

- [ ] Citar as **boas práticas** do root (MFA, sem access keys, não usar no dia a dia).
- [ ] Reconhecer as **tarefas exclusivas do root** (ex.: alterar e-mail/senha do root, fechar a conta standalone, MFA Delete no S3).
- [ ] Saber o que **não** exige root (criar usuários IAM, ver a fatura, e agora mudar o plano de suporte e o nome da conta).

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **MFA** | autenticação multifator: senha + um segundo fator (app, chave física). |
| **Access key** | credencial para usar a AWS por linha de comando ou programa. |

> 🎯 **Como não errar na prova:** Na lista de alternativas, procure a tarefa que **só o dono da conta** poderia fazer. Tarefas comuns de administração (criar usuário, ver fatura) **não** exigem root.

## 📖 Conteúdo

- Criado junto com a conta, com o e-mail de cadastro; tem acesso irrestrito e não pode ser limitado por políticas IAM.
- **Boas práticas:** ativar MFA, não criar access keys (apagar se existirem), usar só para tarefas que exigem root, criar usuários/identidades administrativas para o dia a dia, senha forte e e-mail protegido.
- **Tarefas que só o root pode fazer:**
  - 🔄 Alterar o **e-mail**, a **senha** e as **access keys** do root (conta standalone). *O nome da conta, contatos e regiões **não** exigem root.*
  - Fechar a conta AWS (standalone).
  - 🔄 *Mudar o plano de AWS Support **saiu** da lista oficial atual (verificação de 10/2026).*
  - Restaurar permissões de um administrador IAM que se trancou fora.
  - Ativar o acesso de usuários IAM ao console de Billing.
  - Registrar-se como vendedor no Reserved Instance Marketplace.
  - Configurar MFA Delete em um bucket S3.
  - Editar ou apagar uma política de bucket S3 (ou de fila SQS) que bloqueou todo mundo.
  - 🔄 Também na lista oficial: certas operações de Billing e faturas fiscais, inscrição no GovCloud, autorizar a recuperação de uma chave KMS que ficou sem gerenciamento.
  - 🔄 Em AWS Organizations, a conta de gerenciamento pode executar centralmente tarefas privilegiadas das contas-membro (gerenciamento centralizado de acesso root).
- **Cai na prova:** "qual tarefa exige o usuário root?" com uma lista de opções. Criar usuários IAM e ver a fatura **não** exigem root.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).

- "Qual é a boa prática para o usuário root?" → Ativar MFA, não criar access keys e usá-lo só para tarefas que o exigem.
- "Qual destas tarefas exige o root?" → Fechar a conta, alterar o e-mail ou a senha do root, restaurar permissões de administrador ou configurar MFA Delete. (🔄 Mudar o plano de suporte e alterar o nome da conta **não** estão mais na lista oficial.)
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
