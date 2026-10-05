# AWS Compute Optimizer, Service Quotas, License Manager e outros

> **Categoria:** Gerenciamento / otimização e governança · **Domínio:** 3 e 4 · **Escopo:** Regional · **Tópico do guia:** [3.16 Gestão e governança](../../docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md)
>
> **Em uma frase:** ferramentas para dimensionar recursos, controlar limites e licenças, e organizar o ambiente.
>
> **Escopo oficial:** ✅ No escopo (Launch Wizard ❌ fora do escopo) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é uma **balança para os recursos** (mostra o que está grande ou pequeno demais), junto com a **lista de limites** da conta e o **controle de licenças**.

- ✅ **Escolha quando:** precisa ajustar o **tamanho dos recursos** (Compute Optimizer), **pedir aumento de limite** (Service Quotas) ou **controlar licenças** (License Manager).
- 🚫 **Não é a resposta quando:** quer **recomendações amplas** de boas práticas → [Trusted Advisor](trusted-advisor.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "tamanho ideal das instâncias" → Compute Optimizer; "aumentar o limite" → Service Quotas; "licenças por núcleo" → License Manager.
<!-- didatico:fim -->

## AWS Compute Optimizer

- Usa **machine learning** sobre métricas do CloudWatch (14 dias por padrão; até 93 com métricas avançadas) para recomendar o **tamanho ideal** de: **EC2**, **Auto Scaling groups**, **volumes EBS**, **funções Lambda** (memória), **tasks ECS no Fargate**, RDS e licenças comerciais.
- Classifica recursos como *under-provisioned*, *over-provisioned* ou *optimized* e estima a economia.
- Gratuito no básico (opt-in). Recomendações também aparecem no **Cost Optimization Hub**.

## Service Quotas

- Mostra as **cotas (limites)** de cada serviço por região, valores padrão e aplicados.
- **Solicitar aumento** pelo console/API; *quota request templates* para contas novas da organização.
- Alarmes do CloudWatch quando o uso se aproxima do limite.

## AWS License Manager

- Controla o uso de **licenças de software** (Microsoft, Oracle, SAP, IBM): regras por vCPU/núcleo/socket, limites rígidos ou alertas.
- Ajuda com **BYOL** em Dedicated Hosts (automatiza alocação de hosts) e evita multas de auditoria.

## Outros utilitários de organização

| Ferramenta | Função |
|---|---|
| **Tags + Tag Editor** | Pares chave-valor para organizar, controlar acesso (ABAC) e separar custos |
| **Resource Groups** | Agrupar recursos por tag/stack para operar juntos |
| **Resource Explorer** | Buscar recursos em todas as regiões/contas |
| **AWS Launch Wizard** ❌ *fora do escopo* | Implantar SAP, SQL Server, Active Directory com boas práticas |
| **AWS AppConfig** ❌ *fora do escopo* | Feature flags e configuração dinâmica de aplicações (parte do Systems Manager) |
| **Well-Architected Tool** | Revisão gratuita de cargas contra os 6 pilares ([1.4](../../docs/01-conceitos-de-nuvem/04-well-architected-framework.md)) |
| **AWS Management Console mobile app** | Acompanhar recursos, alarmes e Health no celular |

## ❓ Perguntas típicas

- "Recomendar o tamanho ideal das instâncias com base no uso." → Compute Optimizer.
- "Pedir aumento do limite de instâncias." → Service Quotas.
- "Controlar quantas licenças de SQL Server estão em uso." → License Manager.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Recomendações, quotas e configurações de licenças |
| **O que você decide/configura?** | Opt-in/métricas, quota ajustável e regra de licença |
| **Em que ordem as coisas acontecem?** | Analise dimensionamento, solicite quota ou acompanhe uso de licença |
| **O que pode fazer, e em que condição?** | Resolve três necessidades diferentes de otimização/governança |
| **O que não pode presumir?** | Quota não garante capacidade disponível; License Manager não compra licença |

**Caso comentado:** Instância grande demais: Compute Optimizer; limite da conta: Service Quotas; direito comercial: contrato da licença.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) · [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) · [License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager.html)
