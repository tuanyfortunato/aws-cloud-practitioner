<!-- autoral -->

# Amazon ElastiCache

> **Categoria:** Cache em memória · **Domínio:** 3 · **Abrangência:** Regional (nós em uma ou várias zonas) · **Ficha:** núcleo
>
> **Em uma frase:** cache em memória gerenciado, com Valkey, Memcached ou Redis OSS, que responde em microssegundos e alivia o banco.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

No pico de janeiro, milhares de famílias consultam a mesma "situação da matrícula" ao mesmo tempo, e o banco gasta capacidade respondendo a mesma coisa várias vezes por minuto.

Um **cache** guarda os dados mais pedidos na memória, muito mais rápida que o disco, e entrega a resposta sem consultar o banco. O ElastiCache é o cache gerenciado da AWS, com os motores Valkey, Memcached e Redis OSS. Ele roda como cache serverless, sem nós para escolher, ou em clusters de nós que você dimensiona.

O limite: o cache não substitui o banco principal. A aplicação precisa decidir o que guardar e por quanto tempo, e o dado de verdade continua no [RDS](rds.md), no [Aurora](aurora.md) ou no [DynamoDB](dynamodb.md).

## Como funciona

1. Você cria um cache serverless (informando só o nome) ou um cluster de nós.
2. A aplicação procura o dado primeiro no cache.
3. Se não encontra, busca no banco e grava a resposta no cache para os próximos pedidos.
4. No serverless, o ElastiCache acompanha memória, processamento e rede e escala sozinho; ele também aplica patches e troca nós.

## Opções principais

| Opção | O que faz | Quando lembrar |
|---|---|---|
| ElastiCache Serverless | Cria um cache altamente disponível em menos de um minuto, sem nós para gerenciar | "Sem planejar capacidade do cache" |
| Cluster de nós | Você escolhe tipo e número de nós, em uma ou várias zonas | "Controle dos nós", "quando aplicar patches" |
| Valkey, Redis OSS ou Memcached | Motores de cache de código aberto | "Redis", "Memcached" no enunciado |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Latência informada pela AWS | Microssegundos | 06/10/2026 |
| Tempo para criar um cache serverless | Menos de um minuto | 06/10/2026 |

## Como é cobrado

No serverless, você paga pelos dados guardados, em GB-hora, e pelas requisições, em ElastiCache Processing Units (ECPUs), que somam tempo de processamento e dados transferidos; cada cache tem um mínimo cobrado de armazenamento, menor no Valkey. Nos clusters, você paga por hora de cada nó, com desconto em nós reservados de 1 ou 3 anos.

## Não confundir com

| Serviço | Diferença para o ElastiCache | Pista no enunciado |
|---|---|---|
| [Amazon DynamoDB](dynamodb.md) | Banco NoSQL persistente; o DAX é o cache próprio dele | "Guardar os dados de forma durável" |
| [Amazon CloudFront](../redes/cloudfront.md) | Cache de conteúdo na borda, perto dos usuários | "Entregar arquivos e páginas para o mundo" |
| [Amazon MemoryDB](memorydb.md) | Banco em memória durável (fora do escopo da prova) | "Banco principal em memória" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html)
- [Amazon ElastiCache (página do produto)](https://aws.amazon.com/elasticache/)
- [Preços do Amazon ElastiCache](https://aws.amazon.com/elasticache/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
