<!-- autoral -->

# Amazon MemoryDB

> **Categoria:** Banco em memória durável · **Domínio:** 3 · **Abrangência:** Regional (Multi-AZ) · **Ficha:** referência
>
> **Em uma frase:** banco de dados em memória e durável, que trabalha com Valkey e Redis OSS e pode ser o banco principal de uma aplicação, não só um cache.
>
> **Escopo oficial:** ❌ Fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.18 Serviços menos conhecidos](../../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

O ElastiCache acelera um banco, mas é um cache: os dados de verdade ficam em outro lugar. O **Amazon MemoryDB** guarda todos os dados em memória, com leituras em microssegundos, e também os grava de forma durável em várias Zonas de Disponibilidade, para servir de banco principal. Ele está fora do escopo da prova.

1. Cria-se um cluster do MemoryDB, com Valkey ou Redis OSS.
2. A aplicação usa as mesmas estruturas de dados, APIs e comandos que já usa com eles.
3. Cada gravação vai para um registro de transações replicado em várias Zonas de Disponibilidade.
4. Se um nó falhar, o MemoryDB troca de nó e recupera os dados a partir desse registro.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [Amazon ElastiCache](elasticache.md) | Cache em memória na frente de outro banco (no escopo) | "Cache", "acelerar consultas" |
| [Amazon DynamoDB](dynamodb.md) | NoSQL sem servidor, no escopo | "Milissegundos em qualquer escala" |
| [Amazon RDS](rds.md) | Bancos relacionais | "SQL" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/what-is-memorydb.html)
- [Serviços fora do escopo da prova](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-out-of-scope-services.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
