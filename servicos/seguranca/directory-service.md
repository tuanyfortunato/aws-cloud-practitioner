# AWS Directory Service

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa já organiza usuários e computadores com Active Directory e precisa usar esse tipo de identidade com aplicações e recursos na AWS.

**Como este serviço ajuda?** Directory Service oferece opções para diretórios e integração com Active Directory, conforme a modalidade. Ele atende necessidades corporativas de identidade e compatibilidade.

**Exemplo do dia a dia:** Uma aplicação Windows na AWS precisa reconhecer os usuários do diretório da empresa. A equipe escolhe uma modalidade compatível com essa integração.

**O que ele não resolve sozinho?** As modalidades não são equivalentes: encaminhar autenticação para um diretório existente é diferente de manter um diretório gerenciado. Ele também não substitui qualquer mecanismo de login de aplicativos.

**Primeiras palavras para entender:**

- **Diretório:** cadastro organizado de identidades.
- **Active Directory:** tecnologia corporativa de diretório.
- **Domínio:** conjunto administrado por esse diretório.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança / identidade · **Domínio:** 2 · **Escopo:** Regional (em VPC) · **Tópico do guia:** [2.3 AWS IAM](../../docs/02-seguranca-e-conformidade/03-iam.md)
>
> **Em uma frase:** Microsoft Active Directory gerenciado na AWS, ou ponte para o AD on-premises.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Opções

| Opção | O que é | Uso |
|---|---|---|
| **AWS Managed Microsoft AD** | AD real gerenciado (controladores em 2 AZs) | Aplicações que dependem de AD (SQL Server, FSx for Windows, WorkSpaces); trust com AD on-premises |
| **AD Connector** | Proxy que redireciona autenticação para o **AD on-premises** (sem guardar dados na nuvem) | Usar o AD existente com WorkSpaces, Identity Center, console |
| **Simple AD** | Diretório compatível com AD (Samba), básico e barato | 🔄 Fechado a novos clientes desde 30/07/2026 |

## ❓ Perguntas típicas

- "Rodar Active Directory gerenciado na AWS." → AWS Managed Microsoft AD.
- "Usar o AD on-premises sem replicá-lo para a nuvem." → AD Connector.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Diretórios gerenciados/conectores e integração de rede |
| **O que você decide/configura?** | Tipo de diretório, DNS, rede e trusts suportados |
| **Em que ordem as coisas acontecem?** | Conecte workloads ao diretório para autenticação compatível |
| **O que pode fazer, e em que condição?** | Integra necessidades de Active Directory ao ambiente AWS |
| **O que não pode presumir?** | AD Connector não equivale a criar nova cópia de diretório gerenciado |

**Caso comentado:** Aplicação Windows precisa AD: avalie modalidade correta, em vez de presumir que IAM substitui qualquer protocolo de diretório.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html)
