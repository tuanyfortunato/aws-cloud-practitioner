# AWS Directory Service

> **Categoria:** Segurança / identidade · **Domínio:** 2 · **Escopo:** Regional (em VPC) · **Tópico do guia:** [2.3 AWS IAM](../../docs/02-seguranca-e-conformidade/03-iam.md)
>
> **Em uma frase:** Microsoft Active Directory gerenciado na AWS, ou ponte para o AD on-premises.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é um **Active Directory** (o cadastro de usuários da Microsoft) rodando na AWS, ou uma ponte para o que a empresa já tem.

- ✅ **Escolha quando:** aplicações dependem de **Active Directory**, ou você quer usar o **AD on-premises** na AWS.
- 🚫 **Não é a resposta quando:** precisa de **login único nas contas AWS** → [IAM Identity Center](iam-identity-center.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "Active Directory", "AD gerenciado", "AD Connector".
<!-- didatico:fim -->

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
