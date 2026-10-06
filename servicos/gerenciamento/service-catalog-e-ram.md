<!-- autoral -->

# AWS Service Catalog e AWS Resource Access Manager (RAM)

> **Categoria:** Gerenciamento / governança · **Domínio:** 2 e 3 · **Abrangência:** Regional (compartilhável entre contas) · **Ficha:** complementar
>
> **Em uma frase:** o Service Catalog oferece um catálogo de produtos de TI aprovados para autoatendimento; o RAM compartilha recursos entre contas.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.4 Governança multi-conta](../../docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

Os professores de informática querem criar laboratórios sozinhos, mas a TI quer que usem só configurações aprovadas. O **AWS Service Catalog** oferece um catálogo de produtos de TI aprovados (servidores, bancos de dados ou arquiteturas completas), e as equipes criam o que precisam dentro das restrições definidas, como o tipo de instância permitido.

1. A TI cria os produtos, a partir de modelos, e os agrupa em portfólios.
2. Define restrições, como Região e tipo de instância.
3. Dá acesso aos portfólios a usuários ou contas.
4. Os usuários escolhem o produto e o criam sozinhos.

O **AWS Resource Access Manager** (RAM) resolve outro problema: em vez de criar o mesmo recurso em cada conta, cria-se uma vez e compartilha-se com a organização inteira, com algumas OUs ou com contas específicas, para os tipos de recurso que o RAM aceita.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [AWS Control Tower](control-tower.md) | Monta a landing zone de várias contas | "Ambiente multi-conta com boas práticas" |
| [AWS CloudFormation](cloudformation.md) | Cria recursos a partir de modelos; o Service Catalog usa modelos como produtos | "Infraestrutura como código" |
| [AWS Organizations](organizations.md) | Agrupa contas e aplica SCPs | "OU", "SCP" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html)
- [O que é o AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
