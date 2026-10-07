<!-- autoral -->

# AWS IAM (Identity and Access Management) e AWS STS

> **Categoria:** Segurança e identidade · **Domínio:** 2 · **Abrangência:** Global · **Ficha:** núcleo
>
> **Em uma frase:** controla quem pode se autenticar na conta e o que cada identidade pode fazer em cada recurso.
>
> **Escopo oficial:** ✅ No escopo (STS ⚪ não listado) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.3 AWS IAM](../../docs/02-seguranca-e-conformidade/03-iam.md) · base em [2.2 Usuário root](../../docs/02-seguranca-e-conformidade/02-usuario-root.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

Na escola, o técnico precisa criar servidores, a funcionária da fatura precisa ver os custos, as professoras consultam relatórios e o sistema de matrícula, numa instância do EC2, grava documentos no S3. Dar a todos o acesso do usuário root seria entregar a chave mestra a cada um.

O IAM responde as duas perguntas de qualquer pedido: quem é você (autenticação) e o que pode fazer (autorização). Cada pessoa ou programa recebe a própria identidade, e **políticas** dizem quais ações ela pode fazer em quais recursos. O **AWS STS** entrega **credenciais temporárias** a quem assume uma função, para que nada dependa de senhas e chaves permanentes.

O limite: o IAM só faz o que as políticas dizem. Permissões largas demais continuam perigosas, e o menor privilégio é responsabilidade do cliente. Para funcionários em várias contas, o caminho recomendado é o [IAM Identity Center](iam-identity-center.md); para clientes de um aplicativo, o [Cognito](cognito.md).

## Como funciona

1. Você cria identidades: **usuários** (credenciais de longo prazo), **grupos** de usuários e **funções** (*roles*), que são assumidas.
2. Anexa **políticas** em JSON, que permitem ou negam ações em recursos.
3. Cada pedido começa negado; uma permissão explícita libera; uma negação explícita vence tudo.
4. Quem assume uma função recebe do STS credenciais temporárias, que expiram sozinhas.

## Opções principais

| Peça | O que é | Pista no enunciado |
|---|---|---|
| Usuário do IAM | Identidade com senha e, se preciso, chaves de acesso de longo prazo | "Ferramenta que não aceita funções" |
| Grupo | Conjunto de usuários que recebe as mesmas permissões; não contém outros grupos | "Mesmas permissões para várias pessoas" |
| Função (*role*) | Identidade assumida, com credenciais temporárias | "Instância do EC2 acessando o S3", "acesso entre contas" |
| Política gerenciada pela AWS, pelo cliente ou em linha | Onde as permissões ficam escritas | "Menor privilégio", "AdministratorAccess" |
| Relatório de credenciais, último acesso e IAM Access Analyzer | Ferramentas para revisar o acesso | "Quem tem chave sem MFA?", "recurso compartilhado com outra conta" |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Chaves de acesso por usuário do IAM | Até 2 | 06/10/2026 |
| Duração máxima da sessão de uma função | De 1 a 12 horas (padrão de 1 hora) | 06/10/2026 |
| Dispositivos de MFA no usuário root | Até 8 | 06/10/2026 |
| Cobrança do IAM e do STS | Nenhuma | 06/10/2026 |

## Como é cobrado

O IAM, o STS e o IAM Identity Center não têm cobrança adicional. Você paga só pelos outros serviços que as identidades usam.

## Não confundir com

| Serviço | Diferença para o IAM | Pista no enunciado |
|---|---|---|
| [AWS IAM Identity Center](iam-identity-center.md) | Login único de funcionários em várias contas e aplicações | "Várias contas do Organizations", "SSO" |
| [Amazon Cognito](cognito.md) | Cadastro e login de usuários de um aplicativo | "Clientes do site", "login com Google" |
| [AWS Organizations](../gerenciamento/organizations.md) | Suas SCPs limitam o máximo que as contas podem fazer, sem dar permissão | "Proibir uma ação em todas as contas" |
| [AWS Directory Service](directory-service.md) | Microsoft Active Directory gerenciado ou conectado | "Active Directory" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
- [Credenciais temporárias](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)
- [Lógica de avaliação de políticas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)
- [Chaves de acesso](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)
- [Cotas do IAM e do STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html)
- [Resiliência do IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/disaster-recovery-resiliency.html)
- [Boas práticas do usuário root](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
