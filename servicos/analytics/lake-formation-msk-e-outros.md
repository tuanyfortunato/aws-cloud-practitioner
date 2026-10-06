<!-- autoral -->

# Lake Formation, MSK, Data Exchange, AppFlow e Clean Rooms

> **Categoria:** Analytics / dados · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** referência
>
> **Em uma frase:** serviços de dados fora da prova: governança de data lake, Kafka gerenciado, troca de dados com outras organizações, integração com aplicações SaaS e análise conjunta sem expor dados.
>
> **Escopo oficial:** 🔀 MSK, AppFlow, Data Exchange, Clean Rooms e DataZone ❌ fora do escopo · Lake Formation ⚪ não listado · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.18 Serviços menos conhecidos](../../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

Estes serviços aparecem em materiais de estudo, mas nenhum está na lista no escopo. Saber o que cada nome faz ajuda a descartá-los como alternativa.

1. **AWS Lake Formation:** governa o acesso aos dados do data lake no S3 e ao Glue Data Catalog, com permissões finas por coluna, linha e célula. Não aparece na lista.
2. **Amazon MSK:** Apache Kafka totalmente gerenciado, para aplicações que já usam Kafka em fluxos de dados. Fora do escopo.
3. **AWS Data Exchange:** compartilha e gerencia acessos a dados de outras organizações, inclusive produtos de dados do AWS Marketplace. Fora do escopo.
4. **Amazon AppFlow:** troca dados entre aplicações SaaS, como Salesforce e Zendesk, e serviços como S3 e Redshift, sem código. Fora do escopo.
5. **AWS Clean Rooms:** permite que parceiros analisem dados em conjunto sem revelar os dados brutos uns aos outros. Fora do escopo.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [AWS Glue](glue.md) | ETL e catálogo de dados, no escopo | "Preparar dados", "catálogo" |
| [Amazon Kinesis](kinesis.md) | Fluxos de dados em tempo real, no escopo | "Streaming" sem citar Kafka |
| [Amazon Athena](athena.md) | SQL sobre o S3, no escopo | "Consultar o data lake" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html)
- [O que é o Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html)
- [O que é o AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/what-is.html)
- [O que é o Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/what-is-appflow.html)
- [O que é o AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/what-is.html)
- [Serviços fora do escopo da prova](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-out-of-scope-services.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
