<!-- autoral -->

# Amazon Aurora

> **Categoria:** Banco de dados relacional da AWS · **Domínio:** 3 · **Abrangência:** Regional (armazenamento em três zonas); Global Database em várias Regiões · **Ficha:** núcleo
>
> **Em uma frase:** motor relacional da AWS que funciona com MySQL e PostgreSQL, com armazenamento que cresce sozinho e cópias em três zonas.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

O sistema de matrícula usa MySQL e cresce todo ano. A escola quer mais desempenho e disponibilidade sem reescrever a aplicação nem dimensionar disco para o pior caso.

O Aurora é um motor relacional da própria AWS, totalmente gerenciado e parte do Amazon RDS. Ele fala a mesma língua do MySQL e do PostgreSQL: o código e as ferramentas usados com esses bancos funcionam com ele. O armazenamento é um volume próprio, que cresce sozinho e guarda cópias dos dados em três zonas de disponibilidade. A AWS informa até 6 vezes a vazão do MySQL e do PostgreSQL padrão em hardware semelhante.

O limite: o Aurora só atende aplicações MySQL e PostgreSQL. Um banco Oracle ou SQL Server vai para o [RDS](rds.md) com o mesmo motor, ou passa por conversão de esquema antes ([DMS e SCT](../migracao/dms-e-sct.md)).

## Como funciona

1. Você cria um **cluster**: uma instância principal, que lê e grava, e um volume de armazenamento compartilhado.
2. O volume replica os dados em três zonas e cresce sozinho com o banco.
3. Você adiciona **réplicas do Aurora**, que atendem leituras e assumem se a principal falhar.
4. Para várias Regiões, o **Aurora Global Database** replica o cluster com atraso normalmente menor que um segundo.

## Opções principais

| Opção | O que faz | Quando lembrar |
|---|---|---|
| Réplicas do Aurora | Até 15 cópias de leitura no cluster, distribuídas entre as zonas | "Escalar leituras", "failover" |
| Aurora Serverless | Ajusta a capacidade sozinho com a demanda e cobra só o que usa | "Carga imprevisível", "ambiente de testes" |
| Aurora Global Database | Uma Região principal que grava e até 10 Regiões secundárias de leitura | "Usuários no mundo todo", "recuperar de falha de uma Região" |
| Aurora Standard ou I/O-Optimized | Standard cobra cada operação de E/S; I/O-Optimized não cobra E/S | "Muita leitura e gravação, custo previsível" |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Vazão informada pela AWS | Até 6 vezes a do MySQL e do PostgreSQL padrão | 06/10/2026 |
| Zonas com cópias dos dados | 3 | 06/10/2026 |
| Réplicas do Aurora por cluster | Até 15 | 06/10/2026 |
| Regiões secundárias no Global Database | Até 10 | 06/10/2026 |

## Como é cobrado

Você paga pelas instâncias (a principal e as réplicas) ou pela capacidade consumida no Aurora Serverless, pelo armazenamento usado e, no Aurora Standard, por requisição de E/S. No I/O-Optimized não há cobrança de E/S; a AWS indica economia de até 40% quando a E/S passa de 25% do gasto com o Aurora.

## Não confundir com

| Serviço | Diferença para o Aurora | Pista no enunciado |
|---|---|---|
| [Amazon RDS](rds.md) | Motores tradicionais (incluindo Oracle e SQL Server) com armazenamento de instância | "Oracle", "SQL Server", "motor que a equipe já usa" |
| [Amazon DynamoDB](dynamodb.md) | NoSQL serverless; também tem tabelas globais | "Chave-valor", "sem JOIN" |
| [Amazon Redshift](redshift.md) | Data warehouse para análise, não para o sistema transacional | "Relatórios sobre petabytes" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
- [Armazenamento do Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.html)
- [Replicação no Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html)
- [Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html)
- [Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html)
- [Preços do Amazon Aurora](https://aws.amazon.com/rds/aurora/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
