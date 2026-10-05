# Amazon QuickSight (Amazon Quick Sight)

> **Categoria:** Analytics / BI · **Domínio:** 3 · **Escopo:** Regional (conta) · **Tópico do guia:** [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)
>
> **Em uma frase:** BI **serverless** para criar dashboards e relatórios interativos, inclusive com perguntas em linguagem natural.
>
> **Escopo oficial:** ✅ No escopo (como Amazon Quick Sight) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é o **painel de gráficos da diretoria**: transforma dados em dashboards interativos.

- ✅ **Escolha quando:** precisa criar **dashboards e relatórios de BI**.
- 🚫 **Não é a resposta quando:** precisa **guardar e consultar** os dados → [Redshift](../banco-de-dados/redshift.md) ou [Athena](athena.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "dashboards", "BI", "visualização", "relatórios interativos".
<!-- didatico:fim -->

## Destaques

| Item | Detalhe |
|---|---|
| **Fontes** | S3 (via Athena), Redshift, RDS/Aurora, OpenSearch, Snowflake, Salesforce, arquivos, entre outras. |
| **SPICE** | Motor **em memória** que acelera as análises e reduz consultas à fonte. |
| **Dashboards e análises** | Visualizações interativas, filtros, drill-down, relatórios paginados, alertas. |
| **IA generativa (Amazon Q in QuickSight)** | Perguntas em linguagem natural, histórias de dados, criação assistida de visuais. |
| **Embedding** | Dashboards dentro de aplicações. |
| **Segurança** | Integração com IAM Identity Center, segurança em nível de linha/coluna. |

## Cobrança

- Por usuário (autores, leitores) — leitores podem ser **por sessão**; capacidade SPICE adicional.

## 🔄 Atualizações 2025-2026

- Nomes: Amazon QuickSight → **Amazon Quick Suite** → hoje **"Amazon Quick"**. A parte de BI continua como **Amazon Quick Sight**, nome usado no exam guide e na lista de serviços. Na prova pode aparecer também "QuickSight".

## ❓ Perguntas típicas

- "Criar dashboards interativos de BI para executivos." → QuickSight.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Data sources, datasets, analyses e dashboards |
| **O que você decide/configura?** | Conexão, atualização, permissões e compartilhamento |
| **Em que ordem as coisas acontecem?** | Conecte dados, modele visualização e publique dashboard autorizado |
| **O que pode fazer, e em que condição?** | Entrega BI para usuários e aplicações conforme modalidade |
| **O que não pode presumir?** | Não é ferramenta principal de ETL nem acesso irrestrito de qualquer usuário |

**Caso comentado:** Gerentes precisam gráficos de vendas: Quick Sight sobre uma fonte preparada.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html)
