# Amazon Lightsail

> **Categoria:** Computação simplificada · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.6 Outros serviços de computação](../../docs/03-tecnologia-e-servicos/06-outros-servicos-de-computacao.md)
>
> **Em uma frase:** servidores virtuais e serviços prontos com **preço mensal fixo e previsível**, para quem está começando.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é como um **plano pré-pago de servidor**: pacote fechado, preço fixo por mês e nenhuma surpresa na conta.

- ✅ **Escolha quando:** quem está começando quer um **site simples** (como WordPress) com **custo previsível**.
- 🚫 **Não é a resposta quando:** precisa **escalar automaticamente** ou de controle fino → [EC2](ec2.md) ou [Elastic Beanstalk](elastic-beanstalk.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "preço mensal fixo", "simples", "WordPress", "pequena empresa", "custo previsível".
<!-- didatico:fim -->

## Para que serve

- Sites WordPress, lojas pequenas, blogs, ambientes de teste, aplicações simples.
- Usuários com pouca experiência em AWS que querem previsibilidade de custo.

## O que oferece

| Recurso | Detalhe |
|---|---|
| **Instâncias** | Linux/Windows com blueprints prontos (WordPress, LAMP, Node.js, cPanel…). |
| **Planos (bundles)** | Preço mensal fixo que inclui vCPU, memória, SSD e **cota de transferência de dados**. |
| **Bancos gerenciados** | MySQL e PostgreSQL. |
| **Outros** | Load balancer, contêineres, armazenamento em objetos e em bloco, CDN, DNS, snapshots. |
| **Upgrade** | Snapshot pode ser exportado para EC2 quando a aplicação crescer. |

## Cobrança

- Preço **mensal fixo** por plano (cobrado por hora até o teto mensal). Transferência acima da cota é cobrada.

## ⚠️ Pegadinhas e não confundir

- "Preço fixo e previsível, simples" → **Lightsail**. "Escala automática gerenciada a partir do código" → **Elastic Beanstalk**. "Controle total" → **EC2**.

## ❓ Perguntas típicas

- "Site WordPress simples com preço mensal fixo." → Lightsail.
- "Pequena empresa sem experiência quer um servidor com custo previsível." → Lightsail.

## 🔗 Documentação oficial

- [Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html)
