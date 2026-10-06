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

## 1. A sequência de funcionamento

**Passo 1.** Identifique se quer oferecer uma configuração aprovada ou compartilhar um recurso já existente.

**Passo 2.** Use produtos e portfólios do catálogo no primeiro caso; compartilhamentos compatíveis no RAM no segundo.

**Passo 3.** Verifique acessos e alcance. Um produto provisionável e um recurso compartilhado são objetos diferentes.

## 2. Recursos e opções, com significado

### AWS Service Catalog

| Item | Detalhe |
|---|---|
| **Produto** | Template CloudFormation (ou Terraform) aprovado (ex.: "servidor web padrão", "bucket criptografado"). |
| **Portfólio** | Conjunto de produtos com permissões de acesso (usuários, grupos, roles). |
| **Constraints** | Restringem parâmetros (tipos de instância permitidos), definem a role de lançamento (o usuário não precisa de permissões amplas), tags obrigatórias. |
| **Compartilhamento** | Portfólios entre contas da organização. |
| **Uso** | Times provisionam sozinhos, dentro das regras e da governança da empresa. |

### AWS RAM

| Item | Detalhe |
|---|---|
| **O que compartilha** | **Subnets** (VPC compartilhada), **Transit Gateways**, regras do Route 53 Resolver, License Manager, Aurora clusters, prefix lists, Network Firewall policies, entre outros. |
| **Com quem** | Contas específicas, OUs ou a organização inteira. |
| **Benefício** | Evita duplicar recursos e reduz custo/complexidade. Sem custo próprio. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Aprovar um produto é diferente de compartilhar um recurso já existente. RAM não permite compartilhar qualquer coisa sem restrições nem concede todo acesso aos dados.

## 4. Caso resolvido: ligando as peças

Uma equipe escolhe um ambiente aprovado no catálogo. Separadamente, a empresa compartilha um recurso compatível com outra conta pelo RAM.

**Aplicando a sequência à situação:**

**Etapa 1:** Identifique se quer oferecer uma configuração aprovada ou compartilhar um recurso já existente.
**Etapa 2:** Use produtos e portfólios do catálogo no primeiro caso; compartilhamentos compatíveis no RAM no segundo.
**Etapa 3:** Verifique acessos e alcance. Um produto provisionável e um recurso compartilhado são objetos diferentes.

**Resultado e responsabilidade:** Service Catalog organiza produtos de infraestrutura aprovados. RAM compartilha recursos compatíveis com outros destinatários autorizados. São duas funções diferentes.

**Recursos envolvidos:** Portfolios/products/constraints no Catalog; resource shares no RAM.

**Decisões que precisam ser tomadas:** Produto aprovado ou recurso compartilhável e destinatários.

**Outra situação comentada:** Catálogo de stacks aprovadas: Service Catalog; compartilhar subnet compatível: RAM.

**Por que não concluir mais do que isso:** Compartilhar não transfere propriedade nem permite qualquer tipo de recurso

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Deixar times criarem só recursos aprovados pela empresa."

**Resposta curta:** Service Catalog.

**Pergunta:** "Compartilhar uma subnet com outra conta."

**Resposta curta:** AWS RAM.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) · [RAM](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
