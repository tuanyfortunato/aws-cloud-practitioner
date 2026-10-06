# Amazon MemoryDB

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma aplicação precisa trabalhar com dados em memória e também preservar esses dados de forma durável, em vez de manter apenas cópias temporárias.

**Como este serviço ajuda?** MemoryDB oferece um banco em memória com mecanismos de durabilidade. Ele atende aplicações compatíveis com sua interface de acesso.

**Exemplo do dia a dia:** Um sistema que trabalha intensamente com estruturas compatíveis pode avaliar MemoryDB como banco principal, em vez de usar apenas um cache na frente de outro banco.

**O que ele não resolve sozinho?** Não confunda banco em memória durável com qualquer cache. O serviço está fora do escopo indicado nesta ficha; o exemplo explica sua função, não recomenda priorizá-lo para a prova.

**Primeiras palavras para entender:**

- **Durabilidade:** preservação de dados confirmados.
- **Banco principal:** fonte central dos registros.
- **Em memória:** processamento com dados mantidos na memória.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Banco em memória durável · **Domínio:** 3 · **Escopo:** Regional (multi-AZ) · **Tópico do guia:** [3.18 Serviços menos conhecidos](../../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md)
>
> **Em uma frase:** banco de dados **primário** em memória, compatível com Valkey/Redis, com durabilidade multi-AZ.
>
> **Escopo oficial:** ❌ Fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> ❌ **Fora do escopo da CLF-C02** — documentado só para referência. Na prova, "cache em memória" → **ElastiCache** (no escopo).

## 1. A sequência de funcionamento

**Passo 1.** Avalie a compatibilidade da aplicação e a necessidade de manter dados em memória com durabilidade.

**Passo 2.** Prepare o banco e a conexão autorizada. A aplicação usa as estruturas e operações compatíveis.

**Passo 3.** Planeje disponibilidade e recuperação. Não transfira para este produto as suposições de um cache temporário nem de todo banco relacional.

## 2. Recursos e opções, com significado

### Diferencial

Grava as alterações num **log transacional distribuído em várias AZs** → não perde dados se um nó falhar (ao contrário de um cache).

Leituras em microssegundos, escritas em milissegundos de um dígito.

Uso: microsserviços que usam estruturas Redis como banco principal, sessões críticas, placares, feeds, busca vetorial.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Não confunda banco em memória durável com qualquer cache. O serviço está fora do escopo indicado nesta ficha; o exemplo explica sua função, não recomenda priorizá-lo para a prova.

### ⚠️ Não confundir

ElastiCache = **cache** (pode ser reconstruído). MemoryDB = **banco durável**.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por nó-hora + dados gravados + snapshots.

## 5. Caso resolvido: ligando as peças

Um sistema que trabalha intensamente com estruturas compatíveis pode avaliar MemoryDB como banco principal, em vez de usar apenas um cache na frente de outro banco.

**Aplicando a sequência à situação:**

**Etapa 1:** Avalie a compatibilidade da aplicação e a necessidade de manter dados em memória com durabilidade.
**Etapa 2:** Prepare o banco e a conexão autorizada. A aplicação usa as estruturas e operações compatíveis.
**Etapa 3:** Planeje disponibilidade e recuperação. Não transfira para este produto as suposições de um cache temporário nem de todo banco relacional.

**Resultado e responsabilidade:** MemoryDB oferece um banco em memória com mecanismos de durabilidade. Ele atende aplicações compatíveis com sua interface de acesso.

**Recursos envolvidos:** Banco compatível com APIs Redis/Valkey conforme oferta, shards e réplicas.

**Decisões que precisam ser tomadas:** Motor, capacidade, acesso e disponibilidade.

**Outra situação comentada:** Necessidade de banco durável de baixa latência difere de cache descartável; preserve essa diferença sem priorizar na CLF-C02.

**Por que não concluir mais do que isso:** Está fora do escopo consultado; cache e banco durável não têm o mesmo objetivo

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Banco principal com latência de microssegundos e durabilidade, compatível com Redis."

**Resposta curta:** MemoryDB.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/what-is-memorydb.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
