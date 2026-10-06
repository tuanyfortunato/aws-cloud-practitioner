<!-- autoral -->

# Amazon Redshift

> **Categoria:** Data warehouse · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** data warehouse gerenciado na escala de petabytes, consultado com SQL e ferramentas de relatório (BI).
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md) · base em [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

A direção quer relatórios que cruzem anos de matrículas, notas e frequência de todas as unidades. Rodar essas consultas no banco do sistema de matrícula deixa o sistema lento para as famílias, e o banco não foi feito para varrer volumes tão grandes.

Um **data warehouse** é um banco otimizado para analisar dados vindos dos sistemas da empresa, com a estrutura definida antes de os dados entrarem. O Redshift é o data warehouse gerenciado da AWS, na escala de petabytes, consultado com as mesmas ferramentas de SQL e de BI que a equipe já usa. Ele guarda os dados por coluna, o que acelera consultas que leem poucas colunas de muitas linhas.

O limite: o Redshift serve para análise, não para o sistema do dia a dia, que continua no [RDS](rds.md) ou no [Aurora](aurora.md). Para uma consulta pontual sobre arquivos no S3, sem carregar dados, o [Athena](../analytics/athena.md) é mais simples.

## Como funciona

1. Os dados chegam dos sistemas da empresa e do data lake no S3, por exemplo com o [Glue](../analytics/glue.md) ou o Data Firehose.
2. No **Redshift Serverless**, a capacidade é provisionada e escalada sozinha; num **cluster provisionado**, você escolhe os nós.
3. Analistas consultam com SQL e ferramentas de BI, como o [Quick Sight](../analytics/quicksight.md).
4. O **Redshift Spectrum** consulta arquivos no S3 sem carregá-los nas tabelas.

## Opções principais

| Opção | O que faz | Quando lembrar |
|---|---|---|
| Redshift Serverless | Provisiona e escala a capacidade sozinho; não cobra parado | "Sem gerenciar o data warehouse", "uso irregular" |
| Cluster provisionado | Você escolhe e gerencia os nós | "Carga constante", "instâncias reservadas" |
| Redshift Spectrum | Consulta dados no S3 sem carregar | "Data lake no S3 junto com o data warehouse" |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Escala | Petabytes | 06/10/2026 |
| Cobrança do Serverless | RPU-hora, por segundo, com mínimo de 60 segundos | 06/10/2026 |

## Como é cobrado

No Redshift Serverless, você paga a capacidade usada em RPU-hora (Redshift Processing Units), por segundo, com mínimo de 60 segundos e sem cobrança parado; o Spectrum já está incluído. No cluster provisionado, você paga os nós por hora, com desconto em instâncias reservadas, e o Spectrum cobra pelos bytes lidos no S3. O armazenamento gerenciado é cobrado separado da computação.

## Não confundir com

| Serviço | Diferença para o Redshift | Pista no enunciado |
|---|---|---|
| [Amazon Athena](../analytics/athena.md) | Consulta serverless direto no S3, paga por dados lidos | "Consulta pontual em arquivos no S3" |
| [Amazon RDS](rds.md) e [Amazon Aurora](aurora.md) | Bancos transacionais do sistema do dia a dia | "Sistema de matrícula", "transações" |
| [Amazon EMR](../analytics/emr.md) | Processamento com Hadoop e Spark | "Spark", "Hadoop" |
| [Amazon Quick Sight](../analytics/quicksight.md) | Painéis e relatórios visuais sobre os dados | "Dashboard" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html)
- [O que é o Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-whatis.html)
- [Armazenamento colunar](https://docs.aws.amazon.com/redshift/latest/dg/c_columnar_storage_disk_mem_mgmnt.html)
- [Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html)
- [Preços do Amazon Redshift](https://aws.amazon.com/redshift/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
