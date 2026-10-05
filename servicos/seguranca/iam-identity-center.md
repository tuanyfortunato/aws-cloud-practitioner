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

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento


**Passo 1.** Conecte ou configure a fonte de identidades da força de trabalho.

**Passo 2.** Atribua acessos a contas e aplicações, definindo permissões pertinentes a cada atribuição.

**Passo 3.** A pessoa entra pelo portal e seleciona os acessos autorizados. A sessão não dá poder sobre contas que não foram atribuídas.

## 2. Recursos e opções, com significado

### Conceitos e configurações

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **AWS Organizations / Organizations:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.
- **QuickSight:** QuickSight oferece análise visual e painéis a partir de fontes de dados compatíveis.
- **Amazon Q / Q:** A família Amazon Q inclui assistentes com funções diferentes: Q Developer apoia desenvolvimento; Q Business trabalha com conhecimento corporativo conectado e autorizado.
- **CLI:** SDK fornece bibliotecas para programas chamarem APIs; CLI fornece comandos de texto. As duas formas continuam exigindo identidade, autorização e configuração.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **SaaS:** Software como serviço: aplicação pronta disponibilizada para uso. O cliente administra seu uso e seus dados conforme a oferta, em vez de construir o software do zero.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.
- **credenciais:** Informações usadas para comprovar ou representar uma identidade. Credenciais temporárias expiram; credenciais de longa duração precisam de proteção e administração.
- **MFA:** Verificação adicional de autenticação, além da primeira credencial. Ela protege a entrada, mas não concede permissões por si só.
- **SSO:** Uma entrada para vários ambientes autorizados. O usuário ainda recebe acessos definidos para cada ambiente.
- **SAML:** Padrões de integração de identidade entre sistemas. Permitem que uma aplicação ou serviço confie em informações fornecidas por um provedor de identidade compatível.
- **AD / Active Directory:** Tecnologia de diretório para identidades, computadores e controles corporativos. É diferente do cadastro de clientes de uma aplicação pública.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.
- **Permission sets:** Conjuntos de permissões atribuídos no IAM Identity Center para acesso às contas. Uma entrada central não transforma toda sessão em administradora.
- **SCIM:** Padrão de administração de identidades entre sistemas, como provisionamento de usuários. É diferente do protocolo utilizado para o login.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

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

**Antes de ler este trecho:**

- **Cognito:** Cognito oferece recursos de identidade para usuários de aplicações.
- **Directory Service:** Directory Service oferece opções para diretórios e integração com Active Directory, conforme a modalidade.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.


Identity Center (**funcionários** → contas AWS) × **Cognito** (**clientes** de um app) × **Directory Service** (AD gerenciado).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

## 5. Caso resolvido: ligando as peças

Uma funcionária entra no portal corporativo e escolhe a conta de testes ou de produção, recebendo as permissões definidas para cada uma.

**Aplicando a sequência à situação:**

**Etapa 1:** Conecte ou configure a fonte de identidades da força de trabalho.
**Etapa 2:** Atribua acessos a contas e aplicações, definindo permissões pertinentes a cada atribuição.
**Etapa 3:** A pessoa entra pelo portal e seleciona os acessos autorizados. A sessão não dá poder sobre contas que não foram atribuídas.

**Resultado e responsabilidade:** IAM Identity Center centraliza o acesso da força de trabalho. Pessoas entram por um portal e acessam as contas e aplicações que lhes foram atribuídas.

**Recursos envolvidos:** Diretório/IdP, usuários/grupos, permission sets e assignments.

**Decisões que precisam ser tomadas:** Origem de identidade, contas, aplicações e permissões.

**Antes de ler este trecho:**

- **SCP:** Política de controle de serviços usada na organização para limitar permissões disponíveis em contas às quais se aplica. Ela não concede acesso ao usuário sozinha.


**Outra situação comentada:** Funcionários em várias contas: Identity Center; clientes do app: Cognito.

**Por que não concluir mais do que isso:** Não é cadastro de consumidores de uma aplicação pública; atribuição não ignora SCP

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Funcionários usam várias contas AWS e aplicações. Manter um login diferente e permissões separadas em cada uma dificulta a administração.

**2. O que a solução fornece?**

IAM Identity Center centraliza o acesso da força de trabalho. Pessoas entram por um portal e acessam as contas e aplicações que lhes foram atribuídas.

**3. Que conclusão seria incorreta?**

Ele não é o cadastro de clientes de um aplicativo público. Centralizar a entrada também não elimina a necessidade de definir permissões adequadas.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Login único para funcionários em várias contas AWS."

**Resposta curta:** IAM Identity Center.

**Antes de ler este trecho:**

- **IAM Identity Center:** Serviço de acesso central para a força de trabalho. Atribuições de contas e aplicações não são o cadastro de clientes de um aplicativo.


**Fundamento explicado no capítulo:** "Login único para funcionários em várias contas AWS." → IAM Identity Center.

**Pergunta:** "Usar o Active Directory da empresa para acessar o console."

**Resposta curta:** Identity Center com AD (ou federação SAML).

**Antes de ler este trecho:**

- **federação:** Uso de uma identidade de um provedor em outro ambiente por uma relação de confiança. Não significa que todos os usuários passam a ser administradores.


**Fundamento explicado no capítulo:** "Usar o Active Directory da empresa para acessar o console." → Identity Center com AD (ou federação SAML).


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
