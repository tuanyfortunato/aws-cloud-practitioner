# Amazon Neptune

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Algumas perguntas dependem das relações entre pessoas, contas ou produtos, e não apenas dos campos de um registro isolado.

**Como este serviço ajuda?** Neptune é um banco de grafos: representa entidades e as conexões entre elas para consultar relações.

**Exemplo do dia a dia:** Uma investigação de fraude procura contas ligadas ao mesmo dispositivo e a outras contas suspeitas. Um grafo permite explorar esses caminhos.

**O que ele não resolve sozinho?** Ele não é a escolha padrão para qualquer dado nem decide sozinho se há fraude. Você modela as relações e as consultas necessárias.

**Primeiras palavras para entender:**

- **Grafo:** dados organizados por relações.
- **Nó:** entidade, como uma conta.
- **Aresta:** conexão entre entidades.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Banco de grafos · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)
>
> **Em uma frase:** banco de grafos gerenciado para dados altamente conectados (relacionamentos).
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

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
