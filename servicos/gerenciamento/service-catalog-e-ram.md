# AWS Service Catalog e AWS Resource Access Manager (RAM)

> **Categoria:** Gerenciamento / governança · **Domínio:** 2 e 3 · **Escopo:** Regional (compartilháveis entre contas) · **Tópico do guia:** [2.4 Governança multi-conta](../../docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md)
>
> **Em uma frase:** Service Catalog oferece um **catálogo de produtos aprovados** para autoatendimento; RAM **compartilha recursos** entre contas.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** o Service Catalog é um **cardápio aprovado pela TI**; o RAM é o **empréstimo de recursos entre contas**.

- ✅ **Escolha quando:** quer que os times criem **só recursos aprovados** (Service Catalog) ou precisa **compartilhar recursos entre contas** (RAM).
- 🚫 **Não é a resposta quando:** quer **limitar o que uma conta pode fazer** → SCP, na ficha do [Organizations](organizations.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "produtos aprovados", "autoatendimento" → Service Catalog; "compartilhar subnet ou Transit Gateway" → RAM.
<!-- didatico:fim -->

## AWS Service Catalog

| Item | Detalhe |
|---|---|
| **Produto** | Template CloudFormation (ou Terraform) aprovado (ex.: "servidor web padrão", "bucket criptografado"). |
| **Portfólio** | Conjunto de produtos com permissões de acesso (usuários, grupos, roles). |
| **Constraints** | Restringem parâmetros (tipos de instância permitidos), definem a role de lançamento (o usuário não precisa de permissões amplas), tags obrigatórias. |
| **Compartilhamento** | Portfólios entre contas da organização. |
| **Uso** | Times provisionam sozinhos, dentro das regras e da governança da empresa. |

## AWS RAM

| Item | Detalhe |
|---|---|
| **O que compartilha** | **Subnets** (VPC compartilhada), **Transit Gateways**, regras do Route 53 Resolver, License Manager, Aurora clusters, prefix lists, Network Firewall policies, entre outros. |
| **Com quem** | Contas específicas, OUs ou a organização inteira. |
| **Benefício** | Evita duplicar recursos e reduz custo/complexidade. Sem custo próprio. |

## ❓ Perguntas típicas

- "Deixar times criarem só recursos aprovados pela empresa." → Service Catalog.
- "Compartilhar uma subnet com outra conta." → AWS RAM.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Portfolios/products/constraints no Catalog; resource shares no RAM |
| **O que você decide/configura?** | Produto aprovado ou recurso compartilhável e destinatários |
| **Em que ordem as coisas acontecem?** | Catalog provisiona produto autorizado; RAM compartilha recurso suportado |
| **O que pode fazer, e em que condição?** | Evita configurações repetidas e distribui recursos conforme permissões |
| **O que não pode presumir?** | Compartilhar não transfere propriedade nem permite qualquer tipo de recurso |

**Caso comentado:** Catálogo de stacks aprovadas: Service Catalog; compartilhar subnet compatível: RAM.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) · [RAM](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html)
