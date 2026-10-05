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

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento


**Passo 1.** Identifique quais entidades e relações precisam ser representadas.

**Passo 2.** Grave nós e conexões e escreva consultas que percorram essas relações.

**Passo 3.** Avalie se as respostas atendem ao problema. O banco permite explorar relações; o julgamento de fraude ou outra regra ainda precisa ser definido.

## 2. Recursos e opções, com significado

### Destaques

**Antes de ler este trecho:**

- **RDF / SPARQL:** RDF representa informações por relações; SPARQL é uma linguagem de consulta desse modelo. São opções específicas de trabalho com grafos.


Modelos **Property Graph** (Gremlin, openCypher) e **RDF** (SPARQL).

**Antes de ler este trecho:**

- **Neptune:** Neptune é um banco de grafos: representa entidades e as conexões entre elas para consultar relações.
- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.


Até 15 réplicas de leitura, 6 cópias em 3 AZs, Neptune Serverless, Neptune Analytics, Global Database.

**Antes de ler este trecho:**

- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.


Uso: **redes sociais** ("amigos de amigos"), **motores de recomendação**, **detecção de fraude**, grafos de conhecimento, segurança de rede.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele não é a escolha padrão para qualquer dado nem decide sozinho se há fraude. Você modela as relações e as consultas necessárias.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

## 5. Caso resolvido: ligando as peças

Uma investigação de fraude procura contas ligadas ao mesmo dispositivo e a outras contas suspeitas. Um grafo permite explorar esses caminhos.

**Aplicando a sequência à situação:**

**Etapa 1:** Identifique quais entidades e relações precisam ser representadas.
**Etapa 2:** Grave nós e conexões e escreva consultas que percorram essas relações.
**Etapa 3:** Avalie se as respostas atendem ao problema. O banco permite explorar relações; o julgamento de fraude ou outra regra ainda precisa ser definido.

**Resultado e responsabilidade:** Neptune é um banco de grafos: representa entidades e as conexões entre elas para consultar relações.

**Recursos envolvidos:** Banco de grafos, vértices/arestas ou triplas e endpoints.

**Decisões que precisam ser tomadas:** Modelo e linguagem de consulta compatíveis, capacidade e acesso.


**Outra situação comentada:** Descobrir relações entre pessoas e contas para fraude: grafo com Neptune.

**Por que não concluir mais do que isso:** Não é sinônimo de dashboard nem banco relacional tradicional

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Algumas perguntas dependem das relações entre pessoas, contas ou produtos, e não apenas dos campos de um registro isolado.

**2. O que a solução fornece?**

Neptune é um banco de grafos: representa entidades e as conexões entre elas para consultar relações.

**3. Que conclusão seria incorreta?**

Ele não é a escolha padrão para qualquer dado nem decide sozinho se há fraude. Você modela as relações e as consultas necessárias.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Recomendações baseadas em relacionamentos complexos."

**Resposta curta:** Neptune.


**Fundamento explicado no capítulo:** "Recomendações baseadas em relacionamentos complexos." → Neptune.

**Pergunta:** "Detectar anéis de fraude analisando conexões."

**Resposta curta:** Neptune.


**Fundamento explicado no capítulo:** "Detectar anéis de fraude analisando conexões." → Neptune.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
