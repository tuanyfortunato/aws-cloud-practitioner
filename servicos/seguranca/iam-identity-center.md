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

## 1. A sequência de funcionamento

**Passo 1.** Conecte ou configure a fonte de identidades da força de trabalho.

**Passo 2.** Atribua acessos a contas e aplicações, definindo permissões pertinentes a cada atribuição.

**Passo 3.** A pessoa entra pelo portal e seleciona os acessos autorizados. A sessão não dá poder sobre contas que não foram atribuídas.

## 2. Recursos e opções, com significado

### Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Fonte de identidade** | Diretório próprio do Identity Center, **Active Directory** (AWS Managed AD ou AD Connector) ou **IdP externo** via SAML 2.0/SCIM (Okta, Entra ID, Google Workspace). |
| **Permission sets** | Modelos de permissão (políticas IAM) atribuídos a usuários/grupos em contas específicas; viram roles nas contas. |
| **AWS access portal** | Portal onde o usuário escolhe conta e permissão; credenciais temporárias para console e CLI (`aws sso login`). |
| **Aplicações** | SSO para apps SaaS (SAML) e apps AWS (QuickSight, Amazon Q…). |
| **MFA** | Configurável centralmente. |
| **Integração** | Com AWS Organizations (instância de organização) — forma recomendada de acesso humano multi-conta. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele não é o cadastro de clientes de um aplicativo público. Centralizar a entrada também não elimina a necessidade de definir permissões adequadas.

### ⚠️ Não confundir

Identity Center (**funcionários** → contas AWS) × **Cognito** (**clientes** de um app) × **Directory Service** (AD gerenciado).

## 4. Caso resolvido: ligando as peças

Uma funcionária entra no portal corporativo e escolhe a conta de testes ou de produção, recebendo as permissões definidas para cada uma.

**Aplicando a sequência à situação:**

**Etapa 1:** Conecte ou configure a fonte de identidades da força de trabalho.
**Etapa 2:** Atribua acessos a contas e aplicações, definindo permissões pertinentes a cada atribuição.
**Etapa 3:** A pessoa entra pelo portal e seleciona os acessos autorizados. A sessão não dá poder sobre contas que não foram atribuídas.

**Resultado e responsabilidade:** IAM Identity Center centraliza o acesso da força de trabalho. Pessoas entram por um portal e acessam as contas e aplicações que lhes foram atribuídas.

**Recursos envolvidos:** Diretório/IdP, usuários/grupos, permission sets e assignments.

**Decisões que precisam ser tomadas:** Origem de identidade, contas, aplicações e permissões.

**Outra situação comentada:** Funcionários em várias contas: Identity Center; clientes do app: Cognito.

**Por que não concluir mais do que isso:** Não é cadastro de consumidores de uma aplicação pública; atribuição não ignora SCP

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Login único para funcionários em várias contas AWS."

**Resposta curta:** IAM Identity Center.

**Pergunta:** "Usar o Active Directory da empresa para acessar o console."

**Resposta curta:** Identity Center com AD (ou federação SAML).

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
