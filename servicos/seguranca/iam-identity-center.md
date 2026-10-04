# AWS IAM Identity Center (antigo AWS SSO)

> **Categoria:** Segurança / identidade · **Domínio:** 2 · **Escopo:** instância de organização numa região, acesso a todas as contas · **Gratuito** · **Tópico do guia:** [2.3 AWS IAM](../../docs/02-seguranca-e-conformidade/03-iam.md)
>
> **Em uma frase:** login único (SSO) para que **funcionários** acessem várias contas AWS e aplicações SaaS com um só usuário.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Fonte de identidade** | Diretório próprio do Identity Center, **Active Directory** (AWS Managed AD ou AD Connector) ou **IdP externo** via SAML 2.0/SCIM (Okta, Entra ID, Google Workspace). |
| **Permission sets** | Modelos de permissão (políticas IAM) atribuídos a usuários/grupos em contas específicas; viram roles nas contas. |
| **AWS access portal** | Portal onde o usuário escolhe conta e permissão; credenciais temporárias para console e CLI (`aws sso login`). |
| **Aplicações** | SSO para apps SaaS (SAML) e apps AWS (QuickSight, Amazon Q…). |
| **MFA** | Configurável centralmente. |
| **Integração** | Com AWS Organizations (instância de organização) — forma recomendada de acesso humano multi-conta. |

## ⚠️ Não confundir

- Identity Center (**funcionários** → contas AWS) × **Cognito** (**clientes** de um app) × **Directory Service** (AD gerenciado).

## ❓ Perguntas típicas

- "Login único para funcionários em várias contas AWS." → IAM Identity Center.
- "Usar o Active Directory da empresa para acessar o console." → Identity Center com AD (ou federação SAML).

## 🔗 Documentação oficial

- [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
