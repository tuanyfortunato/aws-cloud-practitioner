# Amazon Cognito

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Seu aplicativo precisa que clientes criem contas, façam login e provem sua identidade sem você construir do zero todo esse mecanismo.

**Como este serviço ajuda?** Cognito oferece recursos de identidade para usuários de aplicações. User pools cuidam de cadastro e autenticação; identity pools podem fornecer credenciais AWS temporárias conforme a configuração.

**Exemplo do dia a dia:** Alunos fazem login no aplicativo da escola por um cadastro Cognito. Depois, a aplicação usa essa identidade para aplicar suas regras de acesso.

**O que ele não resolve sozinho?** Login válido não significa autorização para qualquer operação. A aplicação ainda precisa decidir quais dados e ações cada usuário pode acessar.

**Primeiras palavras para entender:**

- **Autenticação:** confirmar quem a pessoa é.
- **Autorização:** decidir o que ela pode fazer.
- **User pool:** diretório de usuários da aplicação.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança / identidade de clientes (CIAM) · **Domínio:** 2 · **Escopo:** Regional · **Tópico do guia:** [2.3 AWS IAM](../../docs/02-seguranca-e-conformidade/03-iam.md)
>
> **Em uma frase:** cadastro, login e controle de acesso para **usuários finais** de aplicações web e mobile.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.
- **autenticação:** Verificação de quem está acessando. Confirmar a identidade não autoriza qualquer ação no sistema.
- **autorização:** Decisão sobre o que uma identidade pode fazer em um recurso. Essa decisão depende das regras e do contexto da solicitação.

**Passo 1.** Escolha como cadastrar e autenticar usuários do aplicativo.

**Passo 2.** Integre o aplicativo com o recurso de identidade adequado e valide as informações de autenticação.

**Passo 3.** Aplique as regras de autorização no uso da aplicação. Saber quem entrou não permite mostrar os dados de qualquer outra pessoa.

## 2. Recursos e opções, com significado

### Componentes

**User pools**

**Antes de ler este trecho:**

- **MFA:** Verificação adicional de autenticação, além da primeira credencial. Ela protege a entrada, mas não concede permissões por si só.
- **SAML / OIDC:** Padrões de integração de identidade entre sistemas. Permitem que uma aplicação ou serviço confie em informações fornecidas por um provedor de identidade compatível.
- **JWT:** Formato de token com informações verificáveis. Receber um token não dispensa validar sua origem, condições e permissões na aplicação.

**O que faz:** Diretório de usuários: **cadastro e login**, verificação de e-mail/telefone, recuperação de senha, **MFA**, **login social** (Google, Facebook, Apple, Amazon), SAML/OIDC, UI hospedada (*managed login*), tokens JWT.

**Identity pools**

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **credenciais:** Informações usadas para comprovar ou representar uma identidade. Credenciais temporárias expiram; credenciais de longa duração precisam de proteção e administração.
- **STS:** Serviço que fornece credenciais temporárias AWS. Essas credenciais permitem uma sessão autorizada dentro das permissões aplicáveis.

**O que faz:** Trocam uma identidade (user pool, social, SAML ou visitante) por **credenciais AWS temporárias** (via STS) para acessar S3, DynamoDB etc. direto do app.

### Configurações

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **API Gateway:** API Gateway ajuda a publicar e administrar APIs.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **ALB:** Modalidades de balanceador com focos diferentes: aplicação, transporte de rede e integração de equipamentos virtuais. Os protocolos e casos de uso determinam a escolha.

Políticas de senha, MFA adaptativo e proteção contra credenciais comprometidas (*threat protection*), gatilhos Lambda (personalizar fluxos), integração com ALB e API Gateway para autenticação.

Planos de recursos: Lite, Essentials e Plus.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Login válido não significa autorização para qualquer operação. A aplicação ainda precisa decidir quais dados e ações cada usuário pode acessar.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **MAU:** Usuários ativos mensais, uma unidade usada em determinadas cobranças de identidade. A definição de atividade depende da oferta.

Por **usuário ativo mensal (MAU)**, conforme o plano; identity pools sem custo próprio.

## 5. Caso resolvido: ligando as peças

Alunos fazem login no aplicativo da escola por um cadastro Cognito. Depois, a aplicação usa essa identidade para aplicar suas regras de acesso.

**Aplicando a sequência à situação:**

**Etapa 1:** Escolha como cadastrar e autenticar usuários do aplicativo.
**Etapa 2:** Integre o aplicativo com o recurso de identidade adequado e valide as informações de autenticação.
**Etapa 3:** Aplique as regras de autorização no uso da aplicação. Saber quem entrou não permite mostrar os dados de qualquer outra pessoa.

**Resultado e responsabilidade:** Cognito oferece recursos de identidade para usuários de aplicações. User pools cuidam de cadastro e autenticação; identity pools podem fornecer credenciais AWS temporárias conforme a configuração.

**Recursos envolvidos:** User pools, app clients e identity pools.

**Decisões que precisam ser tomadas:** Métodos de login, federação, MFA e roles.

**Outra situação comentada:** App precisa login social e acesso limitado a recurso: combine capacidades conforme requisito.

**Por que não concluir mais do que isso:** User pool e identity pool não são o mesmo recurso; login não concede toda ação AWS

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Permitir login com Google num app mobile."

**Resposta curta:** Cognito.

**Antes de ler este trecho:**

- **Cognito:** Cognito oferece recursos de identidade para usuários de aplicações.

**Pergunta:** "App mobile precisa enviar fotos direto ao S3 com credenciais temporárias."

**Resposta curta:** Cognito identity pool.

**Pergunta:** "Cognito ou Identity Center para funcionários acessarem o console?"

**Resposta curta:** Identity Center.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
