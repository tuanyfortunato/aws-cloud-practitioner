# AWS IAM Identity Center (antigo AWS SSO)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Funcionários usam várias contas AWS e aplicações. Manter um login diferente e permissões separadas em cada uma dificulta a administração.

**Como este serviço ajuda?** IAM Identity Center centraliza o acesso da força de trabalho. Pessoas entram por um portal e acessam as contas e aplicações que lhes foram atribuídas.

**Exemplo do dia a dia:** Uma funcionária entra no portal corporativo e escolhe a conta de testes ou de produção, recebendo as permissões definidas para cada uma.

**O que ele não resolve sozinho?** Ele não é o cadastro de clientes de um aplicativo público. Centralizar a entrada também não elimina a necessidade de definir permissões adequadas.

**Primeiras palavras para entender:**

- **Força de trabalho:** funcionários e colaboradores.
- **SSO:** uma entrada para vários ambientes autorizados.
- **Permission set:** conjunto de permissões atribuído para acesso às contas.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Diretório/IdP, usuários/grupos, permission sets e assignments |
| **O que você decide/configura?** | Origem de identidade, contas, aplicações e permissões |
| **Em que ordem as coisas acontecem?** | Usuário entra no portal e assume acesso atribuído |
| **O que pode fazer, e em que condição?** | Centraliza acesso de força de trabalho a contas/apps |
| **O que não pode presumir?** | Não é cadastro de consumidores de uma aplicação pública; atribuição não ignora SCP |

**Caso comentado:** Funcionários em várias contas: Identity Center; clientes do app: Cognito.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
