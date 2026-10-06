<!-- autoral -->

# Amazon EMR

> **Categoria:** Analytics / big data · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** complementar
>
> **Em uma frase:** plataforma gerenciada de clusters para rodar ferramentas de big data de código aberto, como Apache Hadoop e Apache Spark, e processar volumes muito grandes de dados.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

A rede guarda anos de registros de acesso ao portal no S3, e a equipe de dados já sabe usar o **Spark** para processar volumes grandes. Montar e manter um cluster próprio seria um projeto à parte. O **Amazon EMR** cria e gerencia o cluster; a equipe traz o conhecimento das ferramentas.

1. A equipe escolhe as ferramentas, como Spark ou Hadoop, e cria o cluster.
2. O EMR provisiona e configura as máquinas do cluster.
3. Os trabalhos leem e gravam dados em armazenamentos como o S3 e o DynamoDB.
4. Terminado o processamento, o cluster pode ser desligado.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [Amazon Athena](athena.md) | Consultas SQL direto no S3, sem cluster | "SQL sobre o S3", "sem servidor" |
| [AWS Glue](glue.md) | ETL sem servidor e catálogo de dados | "Catálogo", "preparar dados" |
| [Amazon Redshift](../banco-de-dados/redshift.md) | Data warehouse para relatórios | "Data warehouse" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
