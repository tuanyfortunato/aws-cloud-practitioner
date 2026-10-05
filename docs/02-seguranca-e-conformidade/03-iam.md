# 2.3 AWS IAM (Identity and Access Management)

> **Domínio 2 — Segurança e Conformidade (30%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS IAM (Identity and Access Management) e AWS STS](../../servicos/seguranca/iam.md) · [AWS IAM Identity Center (antigo AWS SSO)](../../servicos/seguranca/iam-identity-center.md) · [Amazon Cognito](../../servicos/seguranca/cognito.md) · [AWS Directory Service](../../servicos/seguranca/directory-service.md) · [AWS Secrets Manager e Systems Manager Parameter Store](../../servicos/seguranca/secrets-manager-e-parameter-store.md)

⬅️ [2.2 Usuário root](02-usuario-root.md) · 🏠 [Índice do domínio](README.md) · [2.4 Governança multi-conta](04-governanca-multi-conta.md) ➡️

---

## 🧠 Antes de começar

> 💡 **Em palavras simples:** O IAM decide **quem entra** (autenticação) e **o que cada um pode fazer** (autorização) na conta AWS, usando usuários, grupos, roles e políticas em JSON.
>
> 🏠 **Analogia:** é o **sistema de crachás de uma empresa**: o usuário é a pessoa com crachá; o grupo é o departamento; a role é um **crachá de visitante** temporário que alguém pega emprestado; a política é a lista de salas que o crachá abre.

**Ao terminar este tópico, você deve saber:**

- [ ] Diferenciar **usuário, grupo, role e política**.
- [ ] Aplicar a regra de avaliação: tudo começa **negado**, um **Allow** libera e um **Deny explícito sempre vence**.
- [ ] Explicar o **menor privilégio** e por que usar **roles** em vez de access keys no EC2.
- [ ] Diferenciar **IAM Identity Center** (funcionários, várias contas) de **Cognito** (clientes de um app).

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Autenticação** | provar quem você é (login). |
| **Autorização** | o que você tem permissão de fazer. |
| **Role** | identidade com credenciais temporárias, assumida por quem precisa. |
| **Federação** | entrar com uma identidade de fora (AD, Google, Okta) sem criar usuário IAM. |

> 🎯 **Como não errar na prova:** "Aplicação no EC2 precisa acessar o S3" → **role**, nunca access key. "Login único em várias contas" → **Identity Center**. "Usuários do aplicativo" → **Cognito**. "Rotação automática de senhas" → **Secrets Manager**.

## 📖 Conteúdo

- **Serviço global e gratuito** para controlar quem (autenticação) pode fazer o quê (autorização) na conta.
- **Usuário IAM:** identidade com credenciais de longo prazo (senha para console, access keys para CLI/SDK). Representa uma pessoa ou aplicação.
- **Grupo IAM:** coleção de usuários que recebem as mesmas permissões. Grupos não contêm outros grupos e não são identidades (não fazem login).
- **Role IAM:** identidade com credenciais **temporárias**, assumida por quem precisa: serviços AWS (ex.: EC2 ou Lambda acessando S3), usuários de outra conta (cross-account) ou usuários federados. Não tem senha nem access key fixa.
- **Policies:** documentos JSON com Effect (Allow/Deny), Action, Resource e Condition.
  - **Identity-based:** anexadas a usuários, grupos ou roles.
  - **Resource-based:** anexadas ao recurso (ex.: bucket policy no S3) e indicam quem pode acessá-lo.
  - **AWS managed** (prontas, mantidas pela AWS), **customer managed** (criadas por você, reutilizáveis) e **inline** (embutidas em uma só identidade).
  - **Regra de avaliação:** tudo começa negado (implicit deny); um Allow libera; um Deny explícito sempre vence.
- **Princípio do menor privilégio:** conceder só as permissões necessárias para a tarefa. Aparece em muitas respostas corretas.
- **Credenciais e boas práticas:**
  - **MFA:** apps de autenticação (virtual), chaves físicas FIDO/passkeys e tokens de hardware TOTP.
  - **Password policy:** tamanho mínimo, complexidade, expiração e reuso de senhas dos usuários IAM.
  - **Access keys:** para CLI, SDK e API. Nunca colocar no código; rotacionar; preferir roles.
  - **Roles para EC2 (instance profile):** forma correta de dar permissão a uma aplicação em EC2, em vez de guardar access keys na instância.
- **Ferramentas de auditoria do IAM:**
  - **Credential report:** relatório da conta com todos os usuários e o status das credenciais (senha, MFA, idade das access keys).
  - **Access Advisor (last accessed):** mostra quais serviços um usuário ou role realmente usou, para remover permissões sobrando.
  - **IAM Access Analyzer:** identifica recursos compartilhados com entidades externas e ajuda a gerar políticas de menor privilégio.
- **Federação:** usar identidades externas (Active Directory, Google, Okta) via SAML 2.0 ou OIDC, sem criar usuários IAM.
- **AWS IAM Identity Center** (antigo AWS SSO): login único centralizado para várias contas do Organizations e aplicações SaaS, com conjuntos de permissões (permission sets). É a forma recomendada de dar acesso humano a ambientes multi-conta.
- **Amazon Cognito:** autenticação de **usuários finais** de aplicações web e mobile (cadastro, login, login social). Não é para funcionários acessarem a AWS.
- **AWS Directory Service:** Microsoft Active Directory gerenciado na AWS, ou conector para o AD on-premises.
- **Secrets Manager:** Guarda segredos (senhas de banco, chaves de API) criptografados com KMS. **Cai na prova:** é o serviço com **rotação automática** de segredos, com integração nativa com RDS. É pago por segredo.
- **Systems Manager Parameter Store:** guarda parâmetros e segredos simples; tem camada gratuita; não faz rotação automática nativa.
- **Formas de acessar a AWS:** Console (usuário/senha + MFA), CLI e SDKs (access keys ou credenciais temporárias), CloudShell (terminal no navegador, já autenticado).

## ➕ Complemento — boas práticas do IAM

- Atribuir permissões a **grupos**, não diretamente a usuários.
- Preferir **credenciais temporárias** (roles, Identity Center) a usuários com access keys de longo prazo.
- Exigir MFA, aplicar política de senhas, rotacionar credenciais e remover usuários e permissões sem uso.
- Usar **condições** nas políticas (ex.: exigir MFA, limitar por IP).
- IAM é **global** (não regional) e **gratuito**.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).

- "Uma aplicação no EC2 precisa ler um bucket S3. Qual a forma mais segura?" → Anexar uma IAM role à instância.
- "Dez desenvolvedores precisam das mesmas permissões." → Criar um grupo IAM e anexar a política ao grupo.
- "Uma política tem Allow e outra tem Deny explícito para a mesma ação. O que vale?" → Deny explícito.
- "Qual princípio diz para dar só as permissões necessárias?" → Menor privilégio.
- "Qual relatório lista os usuários e o status de MFA e access keys?" → IAM credential report.
- "Como dar login único a funcionários em várias contas?" → IAM Identity Center.
- "Como permitir login com Google em um app mobile?" → Amazon Cognito.
- "Onde guardar a senha do banco com rotação automática?" → Secrets Manager.
- "Funcionários usam o Active Directory da empresa e precisam acessar a AWS." → Federação (via Identity Center ou SAML) ou AWS Directory Service.
- "Como acessar a AWS por linha de comando?" → AWS CLI com access keys (ou credenciais temporárias).

<!-- aprofundamento:inicio -->
## 🔬 Aprofundamento para a prova — sem abrir o console

**Como funciona:** Autenticação confirma a identidade; autorização avalia a ação sobre o recurso. Policies definem permissões; roles fornecem sessões temporárias. Grupos agrupam usuários IAM, não roles.

**Como escolher:** Funcionários em várias contas: IAM Identity Center. Aplicação na EC2: role. Clientes de um aplicativo: Cognito. API requer credenciais apropriadas, normalmente temporárias.

**O que não concluir:** Um Allow pode ser limitado por boundary ou SCP, e um Deny explícito prevalece. MFA não concede autorização. Criar usuário não fornece acesso automaticamente.

### Exercício de decisão

Uma aplicação na EC2 precisa ler um bucket e não deve guardar chaves de longa duração. O que usar?

<details>
<summary>Resposta e por que as alternativas confundem</summary>

IAM role associada à instância. A aplicação obtém credenciais temporárias; ainda é preciso permitir as operações no bucket e, se aplicável, na chave KMS.

</details>

**Verifique seu entendimento:** explique a escolha em voz alta e cite uma condição que mudaria a resposta. Nomear um serviço sem explicar o motivo ainda não demonstra domínio.

> Escopo e limites de estudo: [como estudar sem console](../00-guia-do-exame/estudar-sem-console.md). Os cenários são autorais; não são questões oficiais nem previsão do que cairá.
<!-- aprofundamento:fim -->

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- **Secrets Manager × Parameter Store (📌):** a **rotação automática nativa** de credenciais (ex.: RDS) é do **Secrets Manager**. O Parameter Store guarda configurações e segredos simples, **sem rotação nativa**.
- 🔄 **MFA obrigatório para o root:** a AWS passou a exigir MFA para usuários root (primeiro nas contas de gerenciamento do Organizations, depois nas contas independentes). Em Organizations também existe o **gerenciamento centralizado de acesso root**, que permite remover as credenciais root das contas-membro.
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [2.2 Usuário root](02-usuario-root.md) · 🏠 [Índice do domínio](README.md) · [2.4 Governança multi-conta](04-governanca-multi-conta.md) ➡️
