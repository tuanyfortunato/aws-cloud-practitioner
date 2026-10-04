# AWS IAM (Identity and Access Management) e AWS STS

> **Categoria:** Segurança / identidade · **Domínio:** 2 · **Escopo:** **Global** · **Gratuito** · **Tópico do guia:** [2.3 AWS IAM](../../docs/02-seguranca-e-conformidade/03-iam.md) · [2.2 Usuário root](../../docs/02-seguranca-e-conformidade/02-usuario-root.md)
>
> **Em uma frase:** controla **quem** pode se autenticar e **o que** cada identidade pode fazer em quais recursos da conta.
>
> **Escopo oficial:** ✅ No escopo (STS ⚪ não listado) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é o **crachá e as regras de acesso do prédio**: diz quem pode entrar (autenticação) e em quais salas (autorização).

- ✅ **Escolha quando:** precisa controlar **quem pode fazer o quê** na conta: usuários, grupos, roles e políticas.
- 🚫 **Não é a resposta quando:** funcionários precisam de **login único em várias contas** → [IAM Identity Center](iam-identity-center.md); **clientes de um app** precisam de login → [Cognito](cognito.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "menor privilégio", "role", "política", "MFA", "credenciais temporárias", "global e gratuito".
<!-- didatico:fim -->

## Identidades

| Identidade | Credenciais | Uso |
|---|---|---|
| **Usuário root** | E-mail + senha (+ MFA) | Só tarefas que exigem root. **Não** pode ser limitado por políticas IAM (só por SCP, na Organization). |
| **Usuário IAM** | **Longo prazo**: senha (console) e até **2 access keys** (CLI/SDK) | Pessoa ou aplicação — hoje prefira Identity Center/roles. |
| **Grupo IAM** | — (não faz login) | Agrupar usuários e atribuir permissões. Grupos **não** contêm grupos. |
| **Role IAM** | **Temporárias** (via STS) | Serviços AWS (EC2, Lambda), **cross-account**, usuários federados, Identity Center. |

### Roles em detalhe

- **Trust policy:** quem pode **assumir** a role (principal: serviço, conta, IdP).
- **Permission policy:** o que a role pode fazer.
- **Instance profile:** entrega a role a uma instância EC2 (credenciais via IMDS, rotacionadas automaticamente).
- **Service-linked role:** criada e gerenciada por um serviço AWS.

## Políticas

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:GetObject"],
    "Resource": "arn:aws:s3:::meu-bucket/*",
    "Condition": {"Bool": {"aws:MultiFactorAuthPresent": "true"}}
  }]
}
```

| Tipo | Anexada a | Observação |
|---|---|---|
| **Identity-based** | Usuário, grupo, role | AWS managed, customer managed ou inline |
| **Resource-based** | Recurso (bucket policy, key policy, política de fila SQS, Lambda) | Tem `Principal`; permite acesso **cross-account** |
| **Permissions boundary** | Usuário/role | **Teto** de permissões (delegar criação de usuários com segurança) |
| **SCP / RCP** | Contas/OUs (Organizations) | Teto para a conta inteira — não concedem nada |
| **Session policy** | Sessão temporária | Restringe uma sessão assumida |

### Lógica de avaliação

1. Tudo começa **negado** (implicit deny).
2. Um **Deny explícito** em qualquer política → **negado** (sempre vence).
3. SCP/boundary/session limitam; precisa haver um **Allow** em identity- ou resource-based.

## Credenciais e boas práticas

| Prática | Detalhe |
|---|---|
| **MFA** | Virtual (app), chave de segurança FIDO2/**passkey**, token de hardware TOTP ✔️; até 8 dispositivos por identidade. Pode ser exigido via condição. |
| **Password policy** | Tamanho, complexidade, expiração, reuso. |
| **Menor privilégio** | Começar com o mínimo; usar Access Analyzer para gerar políticas. |
| **Credenciais temporárias** | Preferir roles e Identity Center a access keys de longo prazo. |
| **Access keys** | Nunca no código/repositório; rotacionar; apagar as sem uso. |
| **Root** | MFA, sem access keys, uso mínimo. |
| **Grupos** | Permissões em grupos, não em usuários. |
| **ABAC** | Controle por tags (ex.: só acessar recursos com `projeto=x`). |

## Ferramentas de auditoria

| Ferramenta | O que mostra |
|---|---|
| **Credential report** | Todos os usuários da conta e status de senha, MFA, idade das access keys (CSV). |
| **Access Advisor / last accessed** | Quais serviços cada identidade realmente usou → remover permissões sobrando. |
| **IAM Access Analyzer** | Recursos compartilhados com **entidades externas**, acessos não usados, validação e **geração de políticas** de menor privilégio. |
| **Policy simulator** | Testa se uma ação seria permitida. |

## AWS STS (Security Token Service)

- Emite **credenciais temporárias** (access key + secret + session token, com expiração de minutos a horas).
- APIs: `AssumeRole` (roles e cross-account), `AssumeRoleWithSAML`, `AssumeRoleWithWebIdentity` (federação), `GetSessionToken` (MFA).
- É o que está por trás de toda role.

## 🔄 Atualizações 2025-2026

- **MFA obrigatório para root:** contas de gerenciamento (maio/2024), contas standalone (junho/2024) e contas-membro (2025).
- **Gerenciamento centralizado de acesso root** (Organizations, novembro/2024): remove credenciais root das contas-membro e executa ações privilegiadas de forma central.

## Segurança e responsabilidade compartilhada

- **AWS:** disponibilidade e segurança do serviço IAM.
- **Cliente:** **tudo o que é configurado**: identidades, políticas, MFA, rotação de credenciais (controle **específico do cliente**).

## ⚠️ Pegadinhas e não confundir

- IAM é **global** e **gratuito**.
- **User × Role:** longo prazo × temporário.
- **SCP não concede** permissão.
- **Identity Center** (funcionários, SSO multi-conta) × **Cognito** (usuários finais de apps).
- Criar usuários IAM e ver a fatura (com permissão) **não** exigem root.
- ✔️ 🔄 **Alterar o nome da conta**, contatos, contatos alternativos, moeda de pagamento e regiões **não exigem root**; **mudar o plano de suporte** também saiu da lista oficial de tarefas do root.
- ✔️ Até **8 dispositivos MFA** de qualquer tipo por usuário IAM e para o root.

## ❓ Perguntas típicas

- "Aplicação no EC2 precisa ler o S3 com segurança." → IAM role na instância.
- "Dez desenvolvedores com as mesmas permissões." → Grupo IAM.
- "Allow e Deny explícito para a mesma ação." → Deny vence.
- "Relatório com status de MFA e access keys de todos os usuários." → Credential report.
- "Quais serviços um usuário nunca usa?" → Access Advisor (last accessed).
- "Recursos compartilhados com contas externas." → IAM Access Analyzer.
- "Serviço que emite credenciais temporárias." → AWS STS.
- "Acesso de uma conta a recursos de outra." → Role cross-account.

## 🔗 Documentação oficial

- [Guia do IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
- [Boas práticas do IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Tarefas que exigem root](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks)
