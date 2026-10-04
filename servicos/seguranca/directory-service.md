# AWS Directory Service

> **Categoria:** Segurança / identidade · **Domínio:** 2 · **Escopo:** Regional (em VPC) · **Tópico do guia:** [2.3 AWS IAM](../../docs/02-seguranca-e-conformidade/03-iam.md)
>
> **Em uma frase:** Microsoft Active Directory gerenciado na AWS, ou ponte para o AD on-premises.

## Opções

| Opção | O que é | Uso |
|---|---|---|
| **AWS Managed Microsoft AD** | AD real gerenciado (controladores em 2 AZs) | Aplicações que dependem de AD (SQL Server, FSx for Windows, WorkSpaces); trust com AD on-premises |
| **AD Connector** | Proxy que redireciona autenticação para o **AD on-premises** (sem guardar dados na nuvem) | Usar o AD existente com WorkSpaces, Identity Center, console |
| **Simple AD** | Diretório compatível com AD (Samba), básico e barato | Necessidades simples |

## ❓ Perguntas típicas

- "Rodar Active Directory gerenciado na AWS." → AWS Managed Microsoft AD.
- "Usar o AD on-premises sem replicá-lo para a nuvem." → AD Connector.

## 🔗 Documentação oficial

- [Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html)
