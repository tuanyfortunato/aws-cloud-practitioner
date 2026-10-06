<!-- autoral -->

# Amazon RDS (Relational Database Service)

> **Categoria:** Banco de dados relacional gerenciado · **Domínio:** 2 (responsabilidade compartilhada) e 3 · **Abrangência:** Regional (instância numa zona; Multi-AZ opcional) · **Ficha:** núcleo
>
> **Em uma frase:** banco relacional gerenciado: a AWS cuida de hardware, sistema operacional, patches do banco, backups e failover.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) · base em [2.1 Modelo de responsabilidade compartilhada](../../docs/02-seguranca-e-conformidade/01-responsabilidade-compartilhada.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

O banco do sistema de matrícula roda numa instância do EC2. Quem o instalou já saiu da empresa, ninguém sabe se os backups funcionam, e os patches do sistema operacional e do banco estão atrasados.

O RDS entrega o banco relacional como serviço gerenciado. A empresa escolhe um motor conhecido (IBM Db2, MariaDB, Microsoft SQL Server, MySQL, Oracle Database ou PostgreSQL), e a AWS cuida de instalar e aplicar patches no sistema operacional e no banco, fazer backups, detectar falhas e recuperar. A AWS o recomenda como escolha padrão para a maioria dos bancos relacionais.

O limite: a equipe continua responsável por otimizar a aplicação e as consultas, e não tem acesso ao sistema operacional. Quem precisa desse acesso instala o banco no [EC2](../computacao/ec2.md). E o RDS é relacional: para chave-valor em escala enorme, a resposta é o [DynamoDB](dynamodb.md).

## Como funciona

1. Você cria uma **instância de banco**, escolhendo motor, tamanho e armazenamento.
2. O RDS faz backups automáticos na janela de backup, que permitem restaurar o banco para qualquer momento do período de retenção.
3. Com **Multi-AZ**, o RDS mantém uma cópia de espera (standby) em outra zona, atualizada de forma síncrona, e passa a usá-la se a principal falhar.
4. Com **réplicas de leitura**, cópias atualizadas de forma assíncrona recebem as consultas e aliviam a instância principal.

## Opções principais

| Recurso | Para que serve | Pista no enunciado |
|---|---|---|
| Multi-AZ com uma standby | Disponibilidade: failover para outra zona; a standby não atende leituras | "Continuar no ar se uma AZ falhar" |
| Multi-AZ com duas standbys (cluster) | Disponibilidade, com standbys que também atendem leituras | "Failover e leituras nas cópias" |
| Réplica de leitura | Desempenho de leitura, na mesma Região ou em outra | "Muitas consultas deixam o banco lento" |
| Backup automático | Restaurar para um momento dentro da retenção | "Voltar o banco para ontem às 15h" |
| Snapshot manual | Cópia guardada até você apagar | "Guardar antes de uma mudança grande" |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Retenção dos backups automáticos | De 0 a 35 dias (0 desliga); padrão de 7 dias no console | 06/10/2026 |
| Motores | Db2, MariaDB, SQL Server, MySQL, Oracle e PostgreSQL (mais o Aurora) | 06/10/2026 |
| Desconto das instâncias reservadas | Até 69% sobre o preço sob demanda | 06/10/2026 |

## Como é cobrado

Você paga pela instância **por hora** em que ela roda (sob demanda) ou com desconto por compromisso (instâncias reservadas ou Database Savings Plans, de 1 ano), mais o armazenamento provisionado e a transferência de dados. Cada réplica de leitura é cobrada como uma instância comum; a replicação para uma réplica na mesma Região não cobra transferência.

## Não confundir com

| Serviço | Diferença para o RDS | Pista no enunciado |
|---|---|---|
| [Amazon Aurora](aurora.md) | Motor relacional da AWS para MySQL e PostgreSQL, com armazenamento próprio em três zonas | "Mais desempenho", "feito pela AWS" |
| [Amazon EC2](../computacao/ec2.md) | Banco instalado por você, com controle e responsabilidade totais | "Acesso ao sistema operacional do banco" |
| [Amazon DynamoDB](dynamodb.md) | NoSQL serverless, sem junções entre tabelas | "Chave-valor", "milhões de acessos" |
| [Amazon Redshift](redshift.md) | Data warehouse para análises sobre grandes volumes | "Relatórios analíticos sobre petabytes" |
| [AWS DMS](../migracao/dms-e-sct.md) | Migra os dados de um banco para o RDS | "Migrar o banco sem parar" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
- [Backups automáticos](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)
- [Período de retenção de backup](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.BackupRetention.html)
- [Implantações Multi-AZ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)
- [Réplicas de leitura](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
- [Preços do Amazon RDS](https://aws.amazon.com/rds/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
