# Amazon Redshift

> **Categoria:** Data warehouse · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) · [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)
>
> **Em uma frase:** data warehouse colunar e massivamente paralelo (MPP) para análises SQL (OLAP) sobre terabytes a petabytes.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é um **armazém de dados** para fazer perguntas sobre o histórico inteiro da empresa — feito para analisar, não para registrar as vendas uma a uma.

- ✅ **Escolha quando:** precisa de **relatórios de BI e análises SQL** sobre terabytes ou petabytes (OLAP).
- 🚫 **Não é a resposta quando:** precisa registrar as **transações do dia a dia** → [RDS](rds.md); quer consultar **arquivos no S3 sem carregar nada** → [Athena](../analytics/athena.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "data warehouse", "OLAP", "BI", "petabytes", "armazenamento colunar".
<!-- didatico:fim -->

## Para que serve

- Relatórios de BI, dashboards (QuickSight), análises históricas, consolidação de dados de várias fontes.

## Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Armazenamento colunar + compressão** | Consultas analíticas rápidas lendo só as colunas necessárias. |
| **Cluster provisionado** | Nó líder + nós de computação; **RA3** separa computação de armazenamento gerenciado (S3). |
| **Redshift Serverless** | Sem gerenciar cluster; paga por RPU-hora usada. |
| **Redshift Spectrum** | Consulta dados **direto no S3** (data lake) junto com tabelas locais. |
| **Concurrency scaling** | Capacidade extra temporária em picos de consultas. |
| **Data sharing** | Compartilha dados entre clusters/contas sem copiar. |
| **Zero-ETL** | Integra Aurora, RDS, DynamoDB e aplicações SaaS quase em tempo real. |
| **Redshift ML** | Cria modelos (SageMaker) com SQL. |
| **Segurança** | VPC, criptografia KMS, auditoria, controle por coluna/linha. |

## Cobrança

- Nó-hora (ou nós reservados) ou RPU-hora (Serverless) + armazenamento gerenciado + Spectrum por TB escaneado.

## ⚠️ Pegadinhas e não confundir

- **Redshift (OLAP)** × **RDS/Aurora (OLTP)**.
- **Redshift** (data warehouse sempre disponível) × **Athena** (SQL sob demanda direto no S3, paga por dado escaneado).

## ❓ Perguntas típicas

- "Data warehouse para relatórios de BI sobre petabytes." → Redshift.
- "Consultar dados do S3 junto com o data warehouse." → Redshift Spectrum.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Warehouse, tabelas, endpoints e modalidades provisionada/serverless |
| **O que você decide/configura?** | Capacidade, dados, acesso e carregamento/consulta |
| **Em que ordem as coisas acontecem?** | Ingestão organiza dados para análise SQL; ferramentas consultam e visualizam |
| **O que pode fazer, e em que condição?** | Prioriza grandes análises e agregações |
| **O que não pode presumir?** | Não é a escolha típica de transação individual de aplicação OLTP |

**Caso comentado:** Agregar anos de vendas: Redshift; processar cada venda do caixa: banco transacional apropriado.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html)
