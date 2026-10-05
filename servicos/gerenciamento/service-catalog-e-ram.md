# AWS Service Catalog e AWS Resource Access Manager (RAM)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa quer padronizar o que suas equipes podem provisionar e, em outro caso, compartilhar recursos compatíveis entre contas sem duplicá-los.

**Como este serviço ajuda?** Service Catalog organiza produtos de infraestrutura aprovados. RAM compartilha recursos compatíveis com outros destinatários autorizados. São duas funções diferentes.

**Exemplo do dia a dia:** Uma equipe escolhe um ambiente aprovado no catálogo. Separadamente, a empresa compartilha um recurso compatível com outra conta pelo RAM.

**O que ele não resolve sozinho?** Aprovar um produto é diferente de compartilhar um recurso já existente. RAM não permite compartilhar qualquer coisa sem restrições nem concede todo acesso aos dados.

**Primeiras palavras para entender:**

- **Produto:** definição provisionável no catálogo.
- **Provisionar:** criar recursos.
- **Compartilhamento:** disponibilizar um recurso compatível a destinatários definidos.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Gerenciamento / governança · **Domínio:** 2 e 3 · **Escopo:** Regional (compartilháveis entre contas) · **Tópico do guia:** [2.4 Governança multi-conta](../../docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md)
>
> **Em uma frase:** Service Catalog oferece um **catálogo de produtos aprovados** para autoatendimento; RAM **compartilha recursos** entre contas.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

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
