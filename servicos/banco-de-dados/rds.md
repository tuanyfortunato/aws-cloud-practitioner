# Amazon RDS (Relational Database Service)

> **Categoria:** Banco de dados relacional gerenciado · **Domínio:** 2 (responsabilidade) e 3 · **Escopo:** Regional (instância numa AZ; Multi-AZ opcional) · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)
>
> **Em uma frase:** banco relacional gerenciado — a AWS cuida de hardware, SO, patches do motor, backups e failover.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é um **banco relacional com zelador**: a AWS cuida de instalação, patches, backups e failover; você cuida das tabelas e das consultas.

- ✅ **Escolha quando:** aplicações **transacionais (OLTP)** com SQL: lojas virtuais, ERPs, sistemas web.
- 🚫 **Não é a resposta quando:** precisa de **NoSQL em escala massiva** → [DynamoDB](dynamodb.md); de **análise de grandes volumes** (BI) → [Redshift](redshift.md); de **acesso ao sistema operacional** → banco instalado no [EC2](../computacao/ec2.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "banco relacional gerenciado", "MySQL, PostgreSQL, Oracle, SQL Server"; "Multi-AZ" → disponibilidade; "read replica" → escalar leitura.
<!-- didatico:fim -->

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
| **Multi-AZ DB cluster** | ✔️ 1 writer + **2 readers** em 3 AZs (RDS for MySQL e PostgreSQL), que também servem de failover. |
| **Read Replicas** | Cópias **assíncronas**, só leitura, na mesma região ou **cross-region**; até **15** (MySQL, MariaDB, PostgreSQL), até **5** (Oracle, SQL Server), até **3** (Db2). Podem ser **promovidas** a banco independente (DR). Objetivo: **escalar leitura**. |
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
- 🧊 Limites de armazenamento por motor e versões.

## Cobrança

- Horas de instância (On-Demand ou **Reserved Instances** / 🔄 **Database Savings Plans**: até 20% em instâncias provisionadas, 1 ano, sem pagamento adiantado), armazenamento provisionado, IOPS provisionados, backup além do tamanho do banco, transferência de dados, Multi-AZ (≈ dobra a instância), licença (Oracle/SQL Server *license included* ou BYOL).

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | DB instance/cluster, engine, endpoint, subnet group, SG e backups |
| **O que você decide/configura?** | Motor, tamanho, armazenamento, acesso, backup e disponibilidade |
| **Em que ordem as coisas acontecem?** | Provisione banco e conecte aplicação ao endpoint autorizado |
| **O que pode fazer, e em que condição?** | Administra SO e tarefas comuns; cliente administra esquema, consultas e acesso |
| **O que não pode presumir?** | RDS convencional não entrega acesso root irrestrito ao host; Multi-AZ DB instance standby não atende leituras |

**Caso comentado:** Alta disponibilidade: Multi-AZ; aliviar consultas: read replicas compatíveis, distinguindo modalidades de cluster.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
