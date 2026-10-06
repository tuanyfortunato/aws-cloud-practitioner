# Amazon RDS (Relational Database Service)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma aplicação precisa guardar registros relacionados, como alunos, cursos e matrículas. Instalar e manter o software do banco numa máquina própria exige trabalho.

**Como este serviço ajuda?** O RDS oferece bancos relacionais gerenciados. Você escolhe um mecanismo compatível, define a estrutura dos dados e usa o banco; a AWS assume tarefas de infraestrutura e administração previstas pelo serviço.

**Exemplo do dia a dia:** O sistema da escola mantém tabelas de alunos e matrículas num banco RDS e consulta quais alunos estão inscritos em cada curso.

**O que ele não resolve sozinho?** RDS não cria as regras de negócio nem as consultas da aplicação. Você continua responsável por dados, acessos e configurações; as opções de disponibilidade e recuperação precisam ser escolhidas.

**Primeiras palavras para entender:**

- **Banco relacional:** dados organizados em tabelas que podem se relacionar.
- **SQL:** linguagem para trabalhar com esses dados.
- **Mecanismo:** software do banco, como PostgreSQL.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Banco de dados relacional gerenciado · **Domínio:** 2 (responsabilidade) e 3 · **Escopo:** Regional (instância numa AZ; Multi-AZ opcional) · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)
>
> **Em uma frase:** banco relacional gerenciado — a AWS cuida de hardware, SO, patches do motor, backups e failover.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Escolha um mecanismo de banco compatível com a aplicação e suas necessidades de capacidade e disponibilidade.

**Passo 2.** Prepare conexão e identidade. Crie as estruturas dos dados e faça a aplicação realizar operações autorizadas.

**Passo 3.** Acompanhe desempenho, retenção e recuperação. A AWS administra tarefas previstas, mas a modelagem e o uso dos dados continuam com o cliente.

## 2. Recursos e opções, com significado

### Para que serve

Aplicações transacionais (**OLTP**): e-commerce, ERP, CRM, sistemas web.

**Replatform** de bancos on-premises para reduzir administração.

### Motores

**MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Db2** (e **Aurora**, ver [ficha própria](aurora.md)).

### Conceitos e configurações

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

### Limites e números

📌 Backup automático até **35 dias**. Read replicas: até **15** (MySQL/MariaDB/PostgreSQL).

🧊 Limites de armazenamento por motor e versões.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

RDS não cria as regras de negócio nem as consultas da aplicação. Você continua responsável por dados, acessos e configurações; as opções de disponibilidade e recuperação precisam ser escolhidas.

### ⚠️ Pegadinhas e não confundir

⚠️ **Multi-AZ = disponibilidade**; **Read Replica = desempenho de leitura**.

Sem acesso ao SO (exceto RDS Custom). Precisa de acesso total ao SO → banco no **EC2**.

RDS (OLTP) × Redshift (OLAP) × DynamoDB (NoSQL).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Horas de instância (On-Demand ou **Reserved Instances** / 🔄 **Database Savings Plans**: até 20% em instâncias provisionadas, 1 ano, sem pagamento adiantado), armazenamento provisionado, IOPS provisionados, backup além do tamanho do banco, transferência de dados, Multi-AZ (≈ dobra a instância), licença (Oracle/SQL Server *license included* ou BYOL).

### Segurança e responsabilidade compartilhada

**AWS:** hardware, **SO**, **patch do motor**, backups automáticos, failover Multi-AZ.

**Cliente:** usuários e permissões do banco, security groups, **ativar criptografia**, configurar backups/retenção, schema, consultas e dados.

## 5. Caso resolvido: ligando as peças

A escola guarda alunos, cursos e matrículas relacionados e seu programa usa consultas SQL de um mecanismo compatível. O objetivo é ter um banco com menos administração de infraestrutura que uma instalação própria na EC2.

A equipe escolhe o mecanismo RDS, prepara capacidade, comunicação e usuários e cria as tabelas. A aplicação consulta e grava registros com suas permissões. A AWS administra as tarefas previstas pelo serviço; a equipe continua definindo os dados e as regras de uso.

Uma opção Multi-AZ ajuda no objetivo de disponibilidade conforme sua modalidade, mas não substitui toda recuperação de um apagamento. Réplicas de leitura atendem outro requisito. Antes de escolher, diferencie continuidade do atendimento, aumento de consultas e retorno a dados de um momento anterior.

**Recursos envolvidos:** DB instance/cluster, engine, endpoint, subnet group, SG e backups.

**Decisões que precisam ser tomadas:** Motor, tamanho, armazenamento, acesso, backup e disponibilidade.

**Outra situação comentada:** Alta disponibilidade: Multi-AZ; aliviar consultas: read replicas compatíveis, distinguindo modalidades de cluster.

**Por que não concluir mais do que isso:** RDS convencional não entrega acesso root irrestrito ao host; Multi-AZ DB instance standby não atende leituras

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Vantagem do RDS sobre banco no EC2?"

**Resposta curta:** A AWS cuida de patch, backup, hardware e failover.

**Pergunta:** "Failover automático para outra AZ."

**Resposta curta:** RDS Multi-AZ.

**Pergunta:** "Aliviar consultas de leitura pesadas."

**Resposta curta:** Read Replicas (ou ElastiCache).

**Pergunta:** "Restaurar o banco para 10:32 de ontem."

**Resposta curta:** Point-in-time recovery (backups automáticos).

**Pergunta:** "Muitas conexões curtas de Lambda sobrecarregam o banco."

**Resposta curta:** RDS Proxy.

**Pergunta:** "Quem aplica patch no motor do RDS?"

**Resposta curta:** AWS.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
