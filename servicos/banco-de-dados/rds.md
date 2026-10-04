# Amazon RDS (Relational Database Service)

> **Categoria:** Banco de dados relacional gerenciado · **Domínio:** 2 (responsabilidade) e 3 · **Escopo:** Regional (instância numa AZ; Multi-AZ opcional) · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)
>
> **Em uma frase:** banco relacional gerenciado — a AWS cuida de hardware, SO, patches do motor, backups e failover.

## Para que serve

- Aplicações transacionais (**OLTP**): e-commerce, ERP, CRM, sistemas web.
- **Replatform** de bancos on-premises para reduzir administração.

## Motores

**MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Db2** (e **Aurora**, ver [ficha própria](aurora.md)).

## Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Instância de banco** | Classe (db.t, db.m, db.r…) e armazenamento (gp2/gp3, io1/io2). **Storage auto scaling** aumenta o disco sozinho. |
| **Multi-AZ (instância)** | Standby **síncrono** em outra AZ, **failover automático** (mesmo endpoint DNS). Standby **não atende leitura**. Objetivo: **disponibilidade**. |
| **Multi-AZ DB cluster** | 1 escritor + **2 standbys legíveis** em 3 AZs (MySQL/PostgreSQL); failover mais rápido. |
| **Read Replicas** | Cópias **assíncronas**, só leitura, na mesma região ou **cross-region**; até 15 (MySQL, MariaDB, PostgreSQL). Podem ser **promovidas** a banco independente (DR). Objetivo: **escalar leitura**. |
| **Backups automáticos** | Diários + logs de transação → **point-in-time recovery**; retenção de **0 a 35 dias** (0 desativa). |
| **Snapshots manuais** | Persistem até você apagar; copiáveis entre regiões e contas. |
| **Criptografia** | KMS, definida **na criação** (para criptografar um banco existente: snapshot → cópia criptografada → restaurar). TLS em trânsito. |
| **Parameter / option groups** | Configurações do motor. |
| **Janela de manutenção** | Quando a AWS aplica patches do motor/SO. |
| **IAM database authentication** | Login com token IAM (MySQL, PostgreSQL). |
| **RDS Proxy** | Pool de conexões gerenciado (ótimo para Lambda), failover mais rápido. |
| **Blue/Green Deployments** | Ambiente de staging sincronizado para upgrades com troca rápida. |
| **Performance Insights / Enhanced Monitoring** | Diagnóstico de carga e métricas do SO. |
| **RDS Custom** | Oracle e SQL Server **com acesso ao SO** (para customizações que exigem). |
| **Acesso de rede** | Em subnets da VPC (DB subnet group); *publicly accessible* sim/não; security groups. |

## Limites e números

- 📌 Backup automático até **35 dias**. Read replicas: até **15** (MySQL/MariaDB/PostgreSQL).
- 🧊 Limites de armazenamento por motor, versões, réplicas de Oracle/SQL Server (fontes divergem).

## Cobrança

- Horas de instância (On-Demand ou **Reserved Instances** / Database Savings Plans 🔄), armazenamento provisionado, IOPS provisionados, backup além do tamanho do banco, transferência de dados, Multi-AZ (≈ dobra a instância), licença (Oracle/SQL Server *license included* ou BYOL).

## Segurança e responsabilidade compartilhada

- **AWS:** hardware, **SO**, **patch do motor**, backups automáticos, failover Multi-AZ.
- **Cliente:** usuários e permissões do banco, security groups, **ativar criptografia**, configurar backups/retenção, schema, consultas e dados.

## ⚠️ Pegadinhas e não confundir

- ⚠️ **Multi-AZ = disponibilidade**; **Read Replica = desempenho de leitura**.
- Sem acesso ao SO (exceto RDS Custom). Precisa de acesso total ao SO → banco no **EC2**.
- RDS (OLTP) × Redshift (OLAP) × DynamoDB (NoSQL).

## ❓ Perguntas típicas

- "Vantagem do RDS sobre banco no EC2?" → A AWS cuida de patch, backup, hardware e failover.
- "Failover automático para outra AZ." → RDS Multi-AZ.
- "Aliviar consultas de leitura pesadas." → Read Replicas (ou ElastiCache).
- "Restaurar o banco para 10:32 de ontem." → Point-in-time recovery (backups automáticos).
- "Muitas conexões curtas de Lambda sobrecarregam o banco." → RDS Proxy.
- "Quem aplica patch no motor do RDS?" → AWS.

## 🔗 Documentação oficial

- [Guia do RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
