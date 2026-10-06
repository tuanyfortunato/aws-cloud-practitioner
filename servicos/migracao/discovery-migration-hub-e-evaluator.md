<!-- autoral -->

# Migration Evaluator, Application Discovery Service e Migration Hub

> **Categoria:** Migração / avaliação e planejamento · **Domínio:** 1 e 3 · **Abrangência:** Regional · **Ficha:** complementar
>
> **Em uma frase:** ferramentas para antes e durante a migração: o Migration Evaluator monta o caso de negócio, o Discovery Service levanta servidores e dependências e o Migration Hub acompanha o andamento.
>
> **Escopo oficial:** ✅ No escopo (Migration Hub e Application Discovery Service fechados a novos clientes) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.17 Migração e transferência](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md) · [1.6 Estratégias de migração (os 7 Rs)](../../docs/01-conceitos-de-nuvem/06-estrategias-de-migracao.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

Antes de migrar o datacenter da secretaria, a diretoria quer saber quanto vai economizar, e a TI precisa saber quais servidores conversam entre si. Durante a migração, todos querem ver o andamento num só lugar.

1. **Migration Evaluator:** monta o caso de negócio, aponta servidores superdimensionados e compara opções de licença.
2. **Application Discovery Service:** coleta configuração, uso e conexões de rede dos servidores, sem agente (coletor no VMware vCenter), com agente ou por importação de arquivo, e revela as dependências.
3. **Migration Hub:** um lugar único para planejar e acompanhar o status de cada aplicação, recebendo o andamento do Application Migration Service e do DMS.

O Migration Hub e o Application Discovery Service não aceitam novos clientes desde 07/11/2025; a AWS indica o AWS Transform no lugar. Os dois continuam na lista do exame.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [AWS Application Migration Service](application-migration-service.md) | Faz a migração dos servidores | "Lift and shift" |
| [AWS DMS e SCT](dms-e-sct.md) | Migram os bancos de dados | "Migrar o banco" |
| [AWS Pricing Calculator](../custos/pricing-calculator-cur-e-outras-ferramentas.md) | Estima custos a partir das hipóteses informadas | "Estimar antes de criar" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [Migration Evaluator](https://aws.amazon.com/migration-evaluator/)
- [O que é o AWS Application Discovery Service](https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html)
- [O que é o AWS Migration Hub](https://docs.aws.amazon.com/migrationhub/latest/ug/whatishub.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
