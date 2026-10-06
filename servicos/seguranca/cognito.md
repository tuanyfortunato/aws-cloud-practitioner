<!-- autoral -->

# Amazon Cognito

> **Categoria:** Segurança e identidade de clientes · **Domínio:** 2 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** cadastro, login e controle de acesso para os usuários de aplicativos web e móveis.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.3 AWS IAM](../../docs/02-seguranca-e-conformidade/03-iam.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

Os pais precisam se cadastrar no site da matrícula, entrar com e-mail e senha (ou com a conta do Google) e enviar documentos. Criar um usuário do IAM para cada pai misturaria clientes com as pessoas que administram a conta, e escrever o sistema de login do zero dá trabalho e abre brechas.

O Cognito cuida dessa parte. Um **pool de usuários** (*user pool*) é o diretório do aplicativo: cadastro, login, MFA e entrada com contas sociais como Google e Apple ou provedores SAML e OIDC. Um **pool de identidades** (*identity pool*) troca esse login por credenciais temporárias e limitadas da AWS, para o aplicativo acessar serviços como o S3 em nome do usuário.

O limite: o Cognito é para clientes do aplicativo. Funcionários acessando contas da AWS usam o [IAM Identity Center](iam-identity-center.md).

## Como funciona

1. Você cria um pool de usuários e escolhe as formas de login.
2. O aplicativo usa o login gerenciado do Cognito ou telas próprias; o usuário se cadastra e entra.
3. O pool de usuários devolve tokens (JWT) que o aplicativo ou a API conferem.
4. Se o aplicativo precisa acessar a AWS diretamente, um pool de identidades troca o token por credenciais temporárias.

## Opções principais

| Opção | O que faz | Pista no enunciado |
|---|---|---|
| Pool de usuários | Diretório com cadastro e login, inclusive social | "Login no aplicativo", "entrar com Google" |
| Pool de identidades | Credenciais temporárias da AWS para o usuário do aplicativo | "Aplicativo grava direto no S3" |
| Planos Lite, Essentials e Plus | Recursos crescentes; o Plus acrescenta proteção contra login suspeito e senhas vazadas | "Detectar login de local incomum" |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Nível gratuito (planos Lite e Essentials) | 10.000 usuários ativos por mês | 06/10/2026 |
| Plano padrão de pools novos | Essentials | 06/10/2026 |

## Como é cobrado

O pool de usuários cobra por **usuário ativo por mês** (MAU), com preço que depende do plano. Os planos Lite e Essentials têm nível gratuito de 10.000 usuários ativos por mês para login direto ou social; o Plus não tem nível gratuito. Usuários federados por SAML ou OIDC têm nível gratuito de 50 por mês.

## Não confundir com

| Serviço | Diferença para o Cognito | Pista no enunciado |
|---|---|---|
| [AWS IAM Identity Center](iam-identity-center.md) | Login único de funcionários nas contas da AWS | "Funcionários", "várias contas" |
| [AWS IAM](iam.md) | Identidades de quem administra e dos programas da conta | "Permissão para a instância" |
| [Amazon API Gateway](../redes/api-gateway.md) | Recebe os pedidos da API; pode exigir o token do Cognito | "Proteger a API com login do usuário" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html)
- [Planos de recursos dos pools de usuários](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sign-in-feature-plans.html)
- [Preços do Amazon Cognito](https://aws.amazon.com/cognito/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
