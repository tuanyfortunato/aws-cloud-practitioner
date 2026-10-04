# Gerenciamento e custos (Data Lifecycle Manager, Chatbot, Launch Wizard, Application Cost Profiler, DevPay)

> **Categoria:** Gerenciamento e gestão de custos · **Domínio:** — (fora da prova) · **Escopo:** Regional / conta · **Lista oficial:** [fora do escopo](../../docs/00-guia-do-exame/escopo-oficial.md#-fora-do-escopo-lista-oficial-não-exaustiva)
>
> **Em uma frase:** ferramentas auxiliares de operação e de cobrança que existem na AWS, mas não caem na prova.
>
> **Escopo oficial:** ❌ Fora do escopo — documentado só para referência · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> ❌ **Fora do escopo da CLF-C02.** Documentados aqui apenas para referência. Veja também
> [Billing Conductor](../custos/pricing-calculator-cur-e-outras-ferramentas.md) e
> [AWS IQ, Activate e AMS](../custos/recursos-de-ajuda-e-parceiros.md), que também estão fora do escopo.

## Amazon Data Lifecycle Manager (DLM)

- **Automatiza** a criação, retenção, cópia entre regiões e exclusão de **snapshots do EBS** e de **AMIs**, com políticas baseadas em tags.
- Na prova, a resposta para "centralizar backups com políticas" é o **AWS Backup** (no escopo).

## AWS Chatbot (Amazon Q Developer em aplicativos de chat)

- Recebe **notificações** da AWS (alarmes do CloudWatch, eventos do Health, alertas do Budgets) no **Slack, Microsoft Teams ou Amazon Chime** e permite executar comandos de leitura e operação a partir do chat.
- 🔄 Passou a se chamar **Amazon Q Developer in chat applications**.

## AWS Launch Wizard

- Assistente que dimensiona e implanta, com boas práticas, aplicações de terceiros como **SAP, Microsoft SQL Server, Active Directory e Exchange**.

## AWS Application Cost Profiler

- Separava o custo de recursos **compartilhados** por **cliente (tenant)** em aplicações multi-tenant, para cobrar ou analisar o custo por cliente.

## Amazon DevPay

- Serviço **legado** de cobrança para vender AMIs e produtos baseados em S3. Hoje, vender software na AWS é feito pelo **AWS Marketplace** (no escopo).

## ⚠️ Como isso aparece na prova

- "Centralizar backups" → **AWS Backup**. "Alertas de custo" → **AWS Budgets**. "Notificar o time" → **SNS**.
- "Separar custos por cliente ou projeto" → **cost allocation tags** (no escopo).
- "Vender software para clientes da AWS" → **AWS Marketplace**.

## 🔗 Documentação oficial

- [Data Lifecycle Manager](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html) · [Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) · [Launch Wizard](https://aws.amazon.com/launchwizard/)
