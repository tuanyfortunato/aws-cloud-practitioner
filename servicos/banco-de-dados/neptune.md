# Amazon Neptune

> **Categoria:** Banco de grafos · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)
>
> **Em uma frase:** banco de grafos gerenciado para dados altamente conectados (relacionamentos).
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é um **mapa de conexões**: em vez de tabelas, guarda quem está ligado a quem.

- ✅ **Escolha quando:** os **relacionamentos** importam mais que os dados: redes sociais, recomendações, detecção de fraude.
- 🚫 **Não é a resposta quando:** são dados **relacionais comuns** → [RDS](rds.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "banco de grafos", "amigos de amigos", "recomendação", "fraude por conexões".
<!-- didatico:fim -->

## Destaques

- Modelos **Property Graph** (Gremlin, openCypher) e **RDF** (SPARQL).
- Até 15 réplicas de leitura, 6 cópias em 3 AZs, Neptune Serverless, Neptune Analytics, Global Database.
- Uso: **redes sociais** ("amigos de amigos"), **motores de recomendação**, **detecção de fraude**, grafos de conhecimento, segurança de rede.

## ❓ Perguntas típicas

- "Recomendações baseadas em relacionamentos complexos." → Neptune.
- "Detectar anéis de fraude analisando conexões." → Neptune.

## 🔗 Documentação oficial

- [Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html)
