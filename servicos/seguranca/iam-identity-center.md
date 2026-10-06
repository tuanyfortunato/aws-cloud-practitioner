<!-- autoral -->

# AWS IAM Identity Center (antigo AWS SSO)

> **Categoria:** Segurança e identidade · **Domínio:** 2 · **Abrangência:** Instância na conta de gerenciamento, com acesso a todas as contas da organização · **Ficha:** núcleo
>
> **Em uma frase:** login único para funcionários acessarem várias contas da AWS e aplicações com uma só identidade.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.3 AWS IAM](../../docs/02-seguranca-e-conformidade/03-iam.md) · base em [2.4 Governança multi-conta](../../docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

A rede de escolas separou os sistemas em várias contas da AWS no AWS Organizations: produção, testes e contabilidade. Criar um usuário do IAM em cada conta para cada funcionário multiplica senhas, e ninguém sabe quem ainda tem acesso a quê.

O IAM Identity Center dá a cada funcionário uma identidade só. Os usuários são criados nele ou sincronizados do provedor de identidade que a empresa já usa, e entram por um **portal de acesso**, onde veem as contas e aplicações liberadas. **Conjuntos de permissões** (*permission sets*) definem o acesso de cada função de trabalho e são aplicados nas contas. A AWS recomenda criar nele o usuário administrativo do dia a dia, em vez de usar o root.

O limite: ele serve para a força de trabalho. Clientes de um aplicativo usam o [Cognito](cognito.md); e o acesso de um programa a outro serviço continua sendo uma função do [IAM](iam.md).

## Como funciona

1. Você ativa uma **instância de organização** na conta de gerenciamento do AWS Organizations.
2. Escolhe a fonte de identidades: o próprio Identity Center ou um provedor externo (por exemplo, o Active Directory).
3. Cria conjuntos de permissões e os atribui a usuários e grupos em contas específicas.
4. O funcionário entra no portal de acesso e escolhe a conta ou aplicação; recebe credenciais temporárias.

## Opções principais

| Opção | O que é | Quando lembrar |
|---|---|---|
| Instância de organização | A recomendada; a única que gerencia acesso às contas da AWS | Várias contas no Organizations |
| Instância de conta | Ligada a uma conta só, para algumas aplicações gerenciadas da AWS | Implantação isolada de uma aplicação |
| Conjunto de permissões | Modelo de permissões por função de trabalho, aplicado em várias contas | "Administrador em todas as contas de teste" |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Cobrança do Identity Center | Nenhuma | 06/10/2026 |
| Tipos de instância | 2 (organização e conta) | 06/10/2026 |

## Como é cobrado

O IAM Identity Center não tem cobrança adicional.

## Não confundir com

| Serviço | Diferença para o Identity Center | Pista no enunciado |
|---|---|---|
| [AWS IAM](iam.md) | Identidades e políticas dentro de uma conta | "Uma conta", "função para a instância" |
| [Amazon Cognito](cognito.md) | Login de clientes de um aplicativo | "Usuários do aplicativo" |
| [AWS Directory Service](directory-service.md) | Active Directory gerenciado; pode ser a fonte de identidades do Identity Center | "Active Directory" |
| [AWS Organizations](../gerenciamento/organizations.md) | Agrupa as contas; o Identity Center dá o acesso a elas | "Gerenciar várias contas" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [Instâncias de organização e de conta](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-instances.html)
- [Active Directory como fonte de identidades](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-ad.html)
- [Credenciais temporárias no IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
