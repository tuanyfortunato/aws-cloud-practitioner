<!-- autoral -->

# Amazon Athena

> **Categoria:** Analytics e consulta interativa · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** consulta com SQL padrão os dados guardados no Amazon S3, sem servidor e sem mover os dados, cobrando pelos dados lidos em cada consulta.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

A direção quer saber em que horário o site da escola recebe mais acessos nos últimos dois anos. Os registros de acesso já estão no S3, em arquivos de texto. A equipe de TI é pequena e não quer montar um banco só para responder uma pergunta.

O **Athena** consulta os arquivos onde eles estão. Você aponta o Athena para os dados no S3, descreve a estrutura das tabelas (ou usa o catálogo do [Glue](glue.md)) e escreve SQL padrão. É **serverless**: não há servidor para montar, e a resposta chega em segundos. Paga-se pelos dados lidos em cada consulta.

O limite é o outro lado da cobrança: uma consulta que varre arquivos grandes, sem compressão nem partição, lê tudo e custa mais, mesmo que a resposta seja pequena. Comprimir, particionar e converter os dados para formatos colunares reduz o custo em até 90%. E para relatórios pesados e frequentes sobre dados estruturados, o lugar é um data warehouse como o [Redshift](../banco-de-dados/redshift.md).

## Como funciona

1. Os dados ficam no S3, em formatos como CSV, JSON, Avro ou colunares, como Parquet e ORC.
2. Uma tabela descreve a estrutura dos arquivos; o catálogo do Glue pode guardar essa descrição.
3. Você escreve a consulta SQL no console ou por API, e o Athena lê os dados direto no S3 (com partições, só as partes que a consulta pede).
4. O resultado sai em segundos, fica guardado num local de resultados e pode alimentar painéis do [Quick Sight](quicksight.md).

## Opções principais

| Opção | O que faz | Quando usar |
|---|---|---|
| Cobrança por consulta | Paga pelos dados lidos | Consultas pontuais ou variáveis |
| Reservas de capacidade | Capacidade dedicada com preço por hora | Muitas consultas com custo previsível |
| Apache Spark no Athena | Roda código Spark sem gerenciar recursos | Análises em Python com Spark |
| Partição e formato colunar | Faz a consulta ler menos dados | Reduzir custo e tempo |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Cobrança | Por dados lidos, com mínimo de 10 MB por consulta | 06/10/2026 |
| Economia com compressão, partição e formato colunar | Até 90% por consulta | 06/10/2026 |
| Consultas com erro e comandos DDL | Sem cobrança | 06/10/2026 |

## Como é cobrado

Paga-se por terabyte de dados lidos, arredondado para o megabyte acima, com mínimo de 10 MB por consulta. Comandos que só definem tabelas (DDL) e consultas que falham não são cobrados; consultas canceladas pagam o que já leram. O armazenamento no S3 é cobrado à parte.

## Não confundir com

| Serviço | Diferença para o Athena | Pista no enunciado |
|---|---|---|
| [Amazon Redshift](../banco-de-dados/redshift.md) | Data warehouse para relatórios grandes e frequentes | "Data warehouse", "petabytes" |
| [AWS Glue](glue.md) | Descobre, cataloga e transforma os dados | "ETL", "catálogo de dados" |
| [Amazon EMR](emr.md) | Clusters de Hadoop e Spark | "Hadoop", "Spark" |
| [Amazon Quick Sight](quicksight.md) | Mostra os resultados em painéis | "Dashboard", "BI" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)
- [Preços do Amazon Athena](https://aws.amazon.com/athena/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
