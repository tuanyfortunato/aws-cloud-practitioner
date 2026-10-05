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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Banco de grafos, vértices/arestas ou triplas e endpoints |
| **O que você decide/configura?** | Modelo e linguagem de consulta compatíveis, capacidade e acesso |
| **Em que ordem as coisas acontecem?** | Modele relações e percorra conexões com consultas de grafo |
| **O que pode fazer, e em que condição?** | Ajuda a explorar redes de relações complexas |
| **O que não pode presumir?** | Não é sinônimo de dashboard nem banco relacional tradicional |

**Caso comentado:** Descobrir relações entre pessoas e contas para fraude: grafo com Neptune.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html)
