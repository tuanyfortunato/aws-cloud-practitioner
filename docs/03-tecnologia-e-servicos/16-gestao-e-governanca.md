# 3.16 Gestão e governança

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS CloudFormation (e CDK, SAM)](../../servicos/gerenciamento/cloudformation.md) · [AWS Systems Manager (SSM)](../../servicos/gerenciamento/systems-manager.md) · [AWS Health Dashboard](../../servicos/gerenciamento/health-dashboard.md) · [AWS Trusted Advisor](../../servicos/gerenciamento/trusted-advisor.md) · [AWS Compute Optimizer, Service Quotas, License Manager e outros](../../servicos/gerenciamento/compute-optimizer-service-quotas-e-license-manager.md) · [AWS Organizations](../../servicos/gerenciamento/organizations.md)

⬅️ [3.15 Ferramentas de desenvolvimento](15-ferramentas-de-desenvolvimento.md) · 🏠 [Índice do domínio](README.md) · [3.17 Migração e transferência](17-migracao-e-transferencia.md) ➡️

---

## 🧠 Antes de começar

> 💡 **Em palavras simples:** Ferramentas para **administrar o ambiente**: criar infraestrutura por código, operar muitos servidores, saber de eventos da AWS, ver limites, controlar licenças e ajustar o tamanho dos recursos.
>
> 🏠 **Analogia:** o **CloudFormation** é a **planta da casa**; o **Systems Manager** é o **controle remoto** de todos os servidores; o **Health Dashboard** é o **aviso do condomínio**; o **Service Quotas** é a **lista de limites** do contrato; o **Compute Optimizer** é uma **balança** que mostra o que está grande ou pequeno demais.

**Ao terminar este tópico, você deve saber:**

- [ ] Explicar **template**, **stack**, **StackSets** e **drift detection** do CloudFormation.
- [ ] Citar os recursos do **Systems Manager** (Session Manager, Run Command, Patch Manager, Parameter Store).
- [ ] Diferenciar **Health Dashboard** (eventos da AWS) de **CloudWatch** (métricas dos seus recursos).
- [ ] Saber para que servem **Service Quotas**, **License Manager** e **Compute Optimizer**.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Stack** | o conjunto de recursos criado a partir de um template. |
| **Drift** | quando alguém altera um recurso na mão, fora do template. |
| **Cota (quota)** | limite de uso de um serviço numa região. |

> 🎯 **Como não errar na prova:** "Acessar sem SSH" → **Session Manager**. "Patch em 500 servidores" → **Patch Manager**. "Evento da AWS afeta minhas instâncias" → **Health Dashboard**. "Passar do limite" → **Service Quotas**. "Tamanho ideal" → **Compute Optimizer**.

## 📖 Conteúdo

- **AWS CloudFormation:** infraestrutura como código nativa.
  - **Templates** em JSON ou YAML descrevem os recursos; cada execução cria uma **stack** (pilha) gerenciada como uma unidade.
  - **StackSets:** implantam a mesma stack em várias contas e regiões.
  - **Drift detection:** detecta recursos alterados manualmente fora do template.
  - O serviço é gratuito; paga-se só pelos recursos criados.
- **AWS Systems Manager:** central de operações para gerenciar frotas de instâncias EC2 e servidores on-premises (via agente SSM).
  - **Session Manager:** acesso ao shell sem abrir porta SSH nem usar bastion host.
  - **Run Command:** executa comandos em várias instâncias de uma vez.
  - **Patch Manager:** automatiza a aplicação de patches.
  - **Parameter Store:** guarda configurações e segredos (ver [2.3](../02-seguranca-e-conformidade/03-iam.md)).
  - **Automation** e **Inventory:** runbooks automatizados e inventário de software.
- **Monitoramento e auditoria:** CloudWatch, CloudTrail e Config (ver [2.7](../02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)).
- **Governança multi-conta:** Organizations, Control Tower, Service Catalog e RAM (ver [2.4](../02-seguranca-e-conformidade/04-governanca-multi-conta.md)).
- **AWS Health Dashboard:**
  - **Service health:** status público de todos os serviços em todas as regiões.
  - **Your account health:** eventos que afetam **os seus** recursos (manutenções agendadas, falhas, avisos), com orientação de correção.
  - A **AWS Health API** está disponível a partir do plano Business Support+ (no modelo clássico, Business).
- **Service Quotas:** mostra os limites (cotas) dos serviços por região e permite **pedir aumento**. Pode gerar alarmes quando o uso se aproxima do limite.
- **AWS License Manager:** controla o uso de **licenças de software** (Microsoft, Oracle, SAP) para evitar excesso e multas.
- **AWS Compute Optimizer:** usa machine learning sobre as métricas de uso para recomendar o **tamanho ideal** de EC2, Auto Scaling groups, EBS, Lambda e tasks ECS no Fargate.
- **AWS Trusted Advisor:** ver [2.9](../02-seguranca-e-conformidade/09-deteccao-de-ameacas.md). **Well-Architected Tool:** ver [1.4](../01-conceitos-de-nuvem/04-well-architected-framework.md).
- **AWS Management Console:** inclui o aplicativo móvel para acompanhar recursos e alarmes.
- **Cai na prova:** "acessar instância sem SSH nem bastion" = Session Manager; "aplicar patch em 500 servidores" = Systems Manager Patch Manager; "evento da AWS que afeta minhas instâncias" = Health Dashboard; "preciso de mais instâncias do que o limite permite" = Service Quotas; "instância superdimensionada" = Compute Optimizer; "mesma infraestrutura em várias contas" = CloudFormation StackSets.

## ➕ Complemento

- **Tags:** pares chave-valor nos recursos, usados para organizar, controlar acesso e separar custos (ver cost allocation tags em [4.4](../04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)).
- **Disponibilidade do Health Dashboard:** gratuito para todos os clientes; a API exige plano Business Support+ ou superior (no modelo clássico, Business).

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).

- "Provisionar infraestrutura a partir de templates JSON/YAML." → CloudFormation.
- "Implantar a mesma stack em várias contas e regiões." → CloudFormation StackSets.
- "Gerenciar e aplicar patches em uma frota de instâncias, inclusive on-premises." → Systems Manager.
- "Acessar a instância sem abrir a porta 22." → Systems Manager Session Manager.
- "Ver eventos de manutenção da AWS que afetam meus recursos." → AWS Health Dashboard.
- "Pedir aumento do limite de instâncias." → Service Quotas.
- "Controlar quantas licenças de SQL Server estão em uso." → License Manager.
- "Recomendar o tamanho ideal das instâncias com base no uso." → Compute Optimizer.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.15 Ferramentas de desenvolvimento](15-ferramentas-de-desenvolvimento.md) · 🏠 [Índice do domínio](README.md) · [3.17 Migração e transferência](17-migracao-e-transferencia.md) ➡️
