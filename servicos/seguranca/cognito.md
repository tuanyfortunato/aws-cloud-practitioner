# Amazon Cognito

> **Categoria:** Segurança / identidade de clientes (CIAM) · **Domínio:** 2 · **Escopo:** Regional · **Tópico do guia:** [2.3 AWS IAM](../../docs/02-seguranca-e-conformidade/03-iam.md)
>
> **Em uma frase:** cadastro, login e controle de acesso para **usuários finais** de aplicações web e mobile.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é a **tela de "Entrar / Criar conta" pronta** para o seu aplicativo, inclusive com "Entrar com Google".

- ✅ **Escolha quando:** **usuários finais** (clientes) de apps web ou mobile precisam se cadastrar e fazer login.
- 🚫 **Não é a resposta quando:** são **funcionários** acessando a AWS → [IAM Identity Center](iam-identity-center.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "usuários do aplicativo", "login social", "cadastro e login", "app mobile".
<!-- didatico:fim -->

## Componentes

| Componente | O que faz |
|---|---|
| **User pools** | Diretório de usuários: **cadastro e login**, verificação de e-mail/telefone, recuperação de senha, **MFA**, **login social** (Google, Facebook, Apple, Amazon), SAML/OIDC, UI hospedada (*managed login*), tokens JWT. |
| **Identity pools** | Trocam uma identidade (user pool, social, SAML ou visitante) por **credenciais AWS temporárias** (via STS) para acessar S3, DynamoDB etc. direto do app. |

## Configurações

- Políticas de senha, MFA adaptativo e proteção contra credenciais comprometidas (*threat protection*), gatilhos Lambda (personalizar fluxos), integração com ALB e API Gateway para autenticação.
- Planos de recursos: Lite, Essentials e Plus.

## Cobrança

- Por **usuário ativo mensal (MAU)**, conforme o plano; identity pools sem custo próprio.

## ❓ Perguntas típicas

- "Permitir login com Google num app mobile." → Cognito.
- "App mobile precisa enviar fotos direto ao S3 com credenciais temporárias." → Cognito identity pool.
- "Cognito ou Identity Center para funcionários acessarem o console?" → Identity Center.

## 🔗 Documentação oficial

- [Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html)
