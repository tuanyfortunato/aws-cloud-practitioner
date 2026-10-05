# AWS Database Migration Service (DMS) e Schema Conversion Tool (SCT)

> **Categoria:** Migração de bancos de dados · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.17 Migração e transferência](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md)
>
> **Em uma frase:** o DMS **move os dados** (com o banco de origem funcionando); o SCT **converte o schema** entre motores diferentes.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** o DMS é a **transportadora que leva os dados com a loja aberta**; o SCT é o **tradutor** que adapta a estrutura de um banco para outro.

- ✅ **Escolha quando:** precisa **migrar bancos de dados** com pouca indisponibilidade.
- 🚫 **Não é a resposta quando:** precisa migrar **servidores inteiros** → [Application Migration Service](application-migration-service.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "migrar banco sem parar a aplicação" → DMS; "Oracle para PostgreSQL" → SCT + DMS.
<!-- didatico:fim -->

## AWS DMS

| Item | Detalhe |
|---|---|
| **Componentes** | **Endpoints** de origem e destino + **replication instance** (ou **DMS Serverless**) + **tasks**. |
| **Tipos de migração** | **Full load**, **full load + CDC** (*change data capture*: replica mudanças contínuas → mínima indisponibilidade) ou só CDC. |
| **Origens/destinos** | Oracle, SQL Server, MySQL, PostgreSQL, MongoDB, Db2, SAP… → RDS, Aurora, Redshift, DynamoDB, S3, OpenSearch, Kinesis, DocumentDB. |
| **Homogêneas** | Mesmo motor (MySQL → RDS MySQL): só DMS (inclusive *homogeneous data migrations* com ferramentas nativas). |
| **Heterogêneas** | Motores diferentes (Oracle → Aurora PostgreSQL): **SCT/DMS Schema Conversion** + DMS. |
| **Outros usos** | Replicação contínua para análise, consolidação de bancos, DR. |

## AWS SCT e DMS Schema Conversion

- Converte **schema, views, stored procedures e funções** entre motores; gera relatório de avaliação (o que converte automaticamente e o que exige trabalho manual).
- **SCT:** aplicativo de desktop. **DMS Schema Conversion:** versão gerenciada no console, com assistência de IA generativa.
- Também converte schemas de data warehouses (Teradata, Oracle, Netezza → Redshift).

## Cobrança

- DMS: por hora da replication instance (ou DCU no Serverless) + armazenamento + transferência. SCT: gratuito.

## ❓ Perguntas típicas

- "Migrar um banco sem desligar a aplicação." → DMS (full load + CDC).
- "Converter um banco Oracle para Aurora PostgreSQL." → SCT + DMS.
- "Migrar MySQL on-premises para RDS MySQL." → DMS (homogênea, sem SCT).

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Endpoints, tarefas de migração/replicação e conversão de esquema |
| **O que você decide/configura?** | Origem/destino suportados, rede, full load/CDC e mapeamentos |
| **Em que ordem as coisas acontecem?** | Prepare esquema, carregue dados e replique mudanças quando suportado |
| **O que pode fazer, e em que condição?** | DMS transfere dados; SCT/conversão suportada ajuda schema/código |
| **O que não pode presumir?** | Nem toda função/stored procedure é convertida; CDC exige pré-requisitos da origem |

**Caso comentado:** Oracle para PostgreSQL: conversão e avaliação mais DMS, não promessa de compatibilidade total.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) · [AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)
