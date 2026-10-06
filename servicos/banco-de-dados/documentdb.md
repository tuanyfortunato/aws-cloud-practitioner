<!-- autoral -->

# Amazon DocumentDB

> **Categoria:** Banco de documentos · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** complementar
>
> **Em uma frase:** banco de documentos totalmente gerenciado para aplicações feitas para o MongoDB, que roda o mesmo código, drivers e ferramentas.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

O aplicativo de atividades extracurriculares da escola foi escrito para o MongoDB e guarda cada atividade como um **documento** (um registro com campos flexíveis). A equipe quer parar de cuidar dos servidores do banco. O **Amazon DocumentDB** roda o mesmo código e os mesmos drivers usados com o MongoDB, gerenciado pela AWS.

1. Cria-se um cluster: baseado em instâncias ou elástico, para milhões de leituras e gravações por segundo.
2. A aplicação se conecta com os mesmos drivers do MongoDB.
3. O armazenamento cresce sozinho à medida que os dados aumentam, sem provisionar espaço antes.
4. Réplicas de leitura aumentam a capacidade de leitura.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [Amazon DynamoDB](dynamodb.md) | NoSQL chave-valor e documentos, sem servidor, da própria AWS | "Milissegundos em qualquer escala" |
| [Amazon Neptune](neptune.md) | Banco de grafos | "Relações", "recomendações" |
| [Amazon RDS](rds.md) | Bancos relacionais gerenciados | "SQL", "MySQL" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/devguide/what-is.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
