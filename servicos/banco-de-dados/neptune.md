<!-- autoral -->

# Amazon Neptune

> **Categoria:** Banco de grafos · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** complementar
>
> **Em uma frase:** banco de grafos totalmente gerenciado, que guarda itens e as ligações entre eles, para recomendações, detecção de fraude e grafos de conhecimento.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

A biblioteca quer recomendar livros pelo que os colegas de turma leram. A pergunta é sobre **ligações**: aluno estuda com aluno, aluno leu livro. O **Amazon Neptune** é um banco de **grafos**, feito para guardar bilhões dessas relações e percorrê-las em milissegundos.

1. Cria-se um cluster do Neptune, com réplicas de leitura e replicação entre Zonas de Disponibilidade.
2. Carregam-se os itens e as ligações entre eles.
3. A aplicação consulta o grafo com as linguagens Gremlin, openCypher ou SPARQL.
4. A AWS cuida do hardware, das atualizações e dos backups contínuos no S3.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [Amazon DocumentDB](documentdb.md) | Banco de documentos para aplicações MongoDB | "MongoDB" |
| [Amazon DynamoDB](dynamodb.md) | NoSQL chave-valor sem servidor | "Chave-valor", "sem servidor" |
| [Amazon Redshift](redshift.md) | Data warehouse para análise | "Relatórios analíticos" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
