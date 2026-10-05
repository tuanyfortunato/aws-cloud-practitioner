# Amazon Aurora

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma aplicação usa banco relacional e quer uma opção AWS compatível com MySQL ou PostgreSQL, com arquitetura própria para armazenamento e disponibilidade.

**Como este serviço ajuda?** Aurora é um banco relacional da AWS dentro da família RDS. Ele combina compatibilidade com esses mecanismos e uma arquitetura gerenciada com recursos próprios.

**Exemplo do dia a dia:** Uma loja que usa PostgreSQL avalia Aurora PostgreSQL para seu banco de pedidos, verificando a compatibilidade da aplicação e as necessidades de capacidade.

**O que ele não resolve sozinho?** Aurora não é compatível com todos os mecanismos disponíveis no RDS. Compatibilidade também não significa que toda extensão e configuração funcionará sem avaliação.

**Primeiras palavras para entender:**

- **Relacional:** dados em tabelas relacionadas.
- **Compatibilidade:** capacidade de usar interfaces e comportamentos esperados.
- **Réplica de leitura:** cópia usada para consultas.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Banco relacional nativo da AWS · **Domínio:** 3 · **Escopo:** Regional (cluster multi-AZ); Global Database multi-região · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)
>
> **Em uma frase:** banco relacional compatível com MySQL e PostgreSQL, com desempenho e disponibilidade de nível comercial a custo de open source.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Para que serve

- OLTP que exige alto desempenho e alta disponibilidade gerenciada.
- Migrações de Oracle/SQL Server para um motor open source compatível (com DMS + SCT).

## Arquitetura

| Item | Detalhe |
|---|---|
| **Compatibilidade** | **MySQL** e **PostgreSQL** (a AWS cita até 5x e 3x o desempenho do padrão). |
| **Armazenamento distribuído** | **6 cópias em 3 AZs**, cresce automaticamente (o volume é dividido em segmentos de 10 GiB); tolera perder 2 cópias para escrita e 3 para leitura; *self-healing*. |
| **Cluster** | 1 instância **writer** + até **15 Aurora Replicas** (leitura e failover, normalmente < 30 s). |
| **Endpoints** | *Cluster (writer) endpoint*, *reader endpoint* (balanceia leituras), endpoints customizados. |

## Configurações e opções importantes

| Opção | Detalhe |
|---|---|
| **Aurora Serverless v2** | Capacidade em ACUs ajustada automaticamente em segundos, em incrementos de 0,5 ACU; ✔️ com *auto-pause* pode escalar até **0 ACU**. |
| **Aurora Global Database** | Replicação entre regiões com lag tipicamente < 1 s; região secundária pode ser promovida (DR) e servir leituras locais. |
| **Backtrack** (MySQL) | "Voltar no tempo" o cluster sem restaurar backup. |
| **Cloning** | Cópia rápida *copy-on-write* para testes. |
| **Configuração de storage** | *Standard* (paga por I/O) ou *I/O-Optimized* (sem cobrança por I/O, para cargas intensivas). |
| **Zero-ETL com Redshift** | Replicação quase em tempo real para análise. |
| **Aurora DSQL** | 🔄 Banco SQL distribuído, serverless, ativo-ativo multi-região (2025) — 🧊 fora da prova. |

## Limites e números

- 📌 **6 cópias / 3 AZs**, **15 réplicas**.
- 🧊 Tamanho máximo do volume, limites de ACU.

## Cobrança

- Instâncias (ou ACU-hora no Serverless), armazenamento GB-mês, I/O (configuração Standard), backup extra, transferência; replicação do Global Database.

## Segurança e responsabilidade compartilhada

- Igual ao [RDS](rds.md): AWS cuida de infra, SO, patch, replicação de armazenamento; cliente de usuários, acesso de rede, criptografia, dados.

## ⚠️ Pegadinhas e não confundir

- Aurora × RDS: Aurora é motor próprio da AWS (MySQL/PostgreSQL), mais rápido e resiliente; RDS oferece vários motores comerciais e open source.
- "Relacional + máxima disponibilidade gerenciada + compatível com MySQL" → **Aurora**.

## ❓ Perguntas típicas

- "Banco relacional compatível com MySQL/PostgreSQL de maior desempenho." → Aurora.
- "Quantas cópias dos dados o Aurora mantém?" → 6 cópias em 3 AZs.
- "Banco relacional com leituras de baixa latência em várias regiões e DR." → Aurora Global Database.
- "Carga intermitente sem gerenciar capacidade." → Aurora Serverless.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Cluster, writer, readers, endpoints e armazenamento compartilhado |
| **O que você decide/configura?** | Compatibilidade MySQL/PostgreSQL, capacidade e disponibilidade |
| **Em que ordem as coisas acontecem?** | Aplicação escreve no writer e pode distribuir leituras aos readers |
| **O que pode fazer, e em que condição?** | Oferece banco relacional gerenciado com arquitetura própria |
| **O que não pode presumir?** | Não é engine compatível com qualquer banco SQL; endpoints e opções dependem da configuração |

**Caso comentado:** Relacional compatível MySQL com leitores: Aurora; não confunda reader com writer.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
