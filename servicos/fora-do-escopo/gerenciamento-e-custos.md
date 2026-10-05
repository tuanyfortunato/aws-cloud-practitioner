# Gerenciamento e custos (Data Lifecycle Manager, Chatbot, Launch Wizard, Application Cost Profiler, DevPay)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Além dos serviços principais, a operação pode precisar administrar cópias de discos, enviar avisos a chats ou apoiar uma implantação específica.

**Como este serviço ajuda?** A ficha reúne ferramentas auxiliares com finalidades diferentes, incluindo opções históricas. Cada seção identifica o trabalho de uma ferramenta.

**Exemplo do dia a dia:** Uma equipe pode querer automatizar o ciclo de cópias de volumes; outra, receber um aviso operacional num chat. São necessidades de operação distintas.

**O que ele não resolve sozinho?** Não escolha uma dessas ferramentas apenas porque a pergunta fala em custo ou gerenciamento. Verifique finalidade, status comercial e escopo; a ficha é de referência.

**Primeiras palavras para entender:**

- **Ciclo de vida:** etapas e regras ao longo do tempo.
- **Notificação:** aviso enviado a um destinatário.
- **Implantação:** colocar recursos ou aplicações em funcionamento.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

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
- 🔄 Renomeado para **Amazon Q Developer** em 19/02/2025 (no console: "in chat applications").

## AWS Launch Wizard

- Assistente que dimensiona e implanta, com boas práticas, aplicações de terceiros como **SAP, Microsoft SQL Server, Active Directory e Exchange**.

## AWS Application Cost Profiler

- Separava o custo de recursos **compartilhados** por **cliente (tenant)** em aplicações multi-tenant, para cobrar ou analisar o custo por cliente.
- 🔄 **Encerrado em 30/09/2024**.

## Amazon DevPay

- Serviço **legado** de cobrança para vender AMIs e produtos baseados em S3. Hoje, vender software na AWS é feito pelo **AWS Marketplace** (no escopo).

## ⚠️ Como isso aparece na prova

- "Centralizar backups" → **AWS Backup**. "Alertas de custo" → **AWS Budgets**. "Notificar o time" → **SNS**.
- "Separar custos por cliente ou projeto" → **cost allocation tags** (no escopo).
- "Vender software para clientes da AWS" → **AWS Marketplace**.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Ferramentas extras de lifecycle, chat, implantação e custos |
| **O que você decide/configura?** | Recurso suportado e disponibilidade do produto |
| **Em que ordem as coisas acontecem?** | Identifique se a necessidade é operar, implantar, comunicar ou contabilizar |
| **O que pode fazer, e em que condição?** | Produtos resolvem problemas distintos de governança |
| **O que não pode presumir?** | Fora do escopo; nomes antigos/renomeados não indicam capacidades novas automaticamente |

**Caso comentado:** Para orçamento de conta, estude Budgets; ferramenta extra de custo não substitui a escolha pelo requisito.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Data Lifecycle Manager](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html) · [Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) · [Launch Wizard](https://aws.amazon.com/launchwizard/)
