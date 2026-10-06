<!-- autoral -->

# AWS Directory Service

> **Categoria:** Segurança / identidade · **Domínio:** 2 · **Abrangência:** Regional (na VPC) · **Ficha:** complementar
>
> **Em uma frase:** formas de usar o Microsoft Active Directory com os serviços da AWS: um diretório gerenciado pela AWS ou a ligação com o diretório que a empresa já tem.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.3 Identidades e acessos](../../docs/02-seguranca-e-conformidade/03-iam.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

A secretaria de educação já tem todos os funcionários no **Active Directory** (AD), o diretório de usuários e computadores da Microsoft, e quer que eles entrem nas máquinas Windows e nos WorkSpaces da AWS com a mesma senha. O **AWS Directory Service** oferece três opções para isso.

1. Escolhe-se a opção: **AWS Managed Microsoft AD** (um AD de verdade gerenciado pela AWS), **AD Connector** (repassa o login ao AD local, sem copiar os usuários) ou **Simple AD** (diretório básico, baseado em Samba 4).
2. Cria-se o diretório na VPC.
3. Os serviços da AWS, como WorkSpaces, Quick Sight e instâncias Windows do EC2, passam a usar esse diretório para o login.
4. No Managed Microsoft AD, a AWS cuida do monitoramento, dos snapshots diários e da recuperação.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [AWS IAM Identity Center](iam-identity-center.md) | Acesso de funcionários a várias contas AWS e aplicações; pode usar o AD como fonte | "Várias contas", "portal de acesso" |
| [Amazon Cognito](cognito.md) | Login dos clientes de um aplicativo | "Usuários do app" |
| [AWS IAM](iam.md) | Usuários, funções e permissões da própria conta | "Política", "função" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
