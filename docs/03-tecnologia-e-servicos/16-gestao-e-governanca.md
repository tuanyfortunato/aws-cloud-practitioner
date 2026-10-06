# 3.16 Gestão e governança

## 🧠 Antes de começar

**Qual é a dificuldade?** A aplicação já existe, mas a equipe precisa criar ambientes de modo repetível, administrar máquinas e acompanhar mudanças, saúde e regras.

**A ideia em palavras simples:** Gestão e governança reúnem ferramentas para operar recursos e aplicar controles. Cada ferramenta observa ou administra uma parte específica.

**Exemplo do dia a dia:** A escola descreve um ambiente com CloudFormation, administra máquinas com Systems Manager e consulta avisos relevantes no AWS Health.

**O que não concluir?** Administrar recursos não significa que qualquer serviço de gestão executa todas essas tarefas. Descubra a ação desejada antes de escolher o produto.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Stack** | o conjunto de recursos criado a partir de um template. |
| **Drift** | quando alguém altera um recurso na mão, fora do template. |
| **Cota (quota)** | limite de uso de um serviço numa região. |

---

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)**

> 🔎 **Fichas detalhadas:** [AWS CloudFormation (e CDK, SAM)](../../servicos/gerenciamento/cloudformation.md) · [AWS Systems Manager (SSM)](../../servicos/gerenciamento/systems-manager.md) · [AWS Health Dashboard](../../servicos/gerenciamento/health-dashboard.md) · [AWS Trusted Advisor](../../servicos/gerenciamento/trusted-advisor.md) · [AWS Compute Optimizer, Service Quotas, License Manager e outros](../../servicos/gerenciamento/compute-optimizer-service-quotas-e-license-manager.md) · [AWS Organizations](../../servicos/gerenciamento/organizations.md)

⬅️ [3.15 Ferramentas de desenvolvimento](15-ferramentas-de-desenvolvimento.md) · 🏠 [Índice do domínio](README.md) · [3.17 Migração e transferência](17-migracao-e-transferencia.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

Operar um ambiente inclui repetir configurações, executar procedimentos, acompanhar mudanças e verificar condições de saúde. Governança define e acompanha regras comuns. São tarefas complementares, não uma única ação realizada por qualquer serviço de administração.

Descrever infraestrutura ajuda a repetir recursos. Preparar máquinas para administração ajuda a operar tarefas. Registrar alterações ajuda a investigar. Comece pela ação desejada e pelos recursos envolvidos, então escolha a ferramenta que tem essa função.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

o **CloudFormation** é a **planta da casa**; o **Systems Manager** é o **controle remoto** de todos os servidores; o **Health Dashboard** é o **aviso do condomínio**; o **Service Quotas** é a **lista de limites** do contrato; o **Compute Optimizer** é uma **balança** que mostra o que está grande ou pequeno demais.

</details>

## 2. Conceitos e opções explicados

**AWS CloudFormation:** infraestrutura como código nativa.

  - **Templates** em JSON ou YAML descrevem os recursos; cada execução cria uma **stack** (pilha) gerenciada como uma unidade.

  - **StackSets:** implantam a mesma stack em várias contas e regiões.

  - **Drift detection:** detecta recursos alterados manualmente fora do template.

  - O serviço é gratuito; paga-se só pelos recursos criados.

**AWS Systems Manager:** central de operações para gerenciar frotas de instâncias EC2 e servidores on-premises (via agente SSM).

  - **Session Manager:** acesso ao shell sem abrir porta SSH nem usar bastion host.

  - **Run Command:** executa comandos em várias instâncias de uma vez.

  - **Patch Manager:** automatiza a aplicação de patches.

  - **Parameter Store:** guarda configurações e segredos (ver [2.3](../02-seguranca-e-conformidade/03-iam.md)).

  - **Automation** e **Inventory:** runbooks automatizados e inventário de software.

**Monitoramento e auditoria:** CloudWatch, CloudTrail e Config (ver [2.7](../02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)).

**Governança multi-conta:** Organizations, Control Tower, Service Catalog e RAM (ver [2.4](../02-seguranca-e-conformidade/04-governanca-multi-conta.md)).

**AWS Health Dashboard:**

  - **Service health:** status público de todos os serviços em todas as regiões.

  - **Your account health:** eventos que afetam **os seus** recursos (manutenções agendadas, falhas, avisos), com orientação de correção.

  - A **AWS Health API** está disponível a partir do plano Business Support+ (no modelo clássico, Business).

**Service Quotas:** mostra os limites (cotas) dos serviços por região e permite **pedir aumento**. Pode gerar alarmes quando o uso se aproxima do limite.

**AWS License Manager:** controla o uso de **licenças de software** (Microsoft, Oracle, SAP) para evitar excesso e multas.

**AWS Compute Optimizer:** usa machine learning sobre as métricas de uso para recomendar o **tamanho ideal** de EC2, Auto Scaling groups, EBS, Lambda e tasks ECS no Fargate.

**AWS Trusted Advisor:** ver [2.9](../02-seguranca-e-conformidade/09-deteccao-de-ameacas.md). **Well-Architected Tool:** ver [1.4](../01-conceitos-de-nuvem/04-well-architected-framework.md).

**AWS Management Console:** inclui o aplicativo móvel para acompanhar recursos e alarmes.

**Cai na prova:** "acessar instância sem SSH nem bastion" = Session Manager; "aplicar patch em 500 servidores" = Systems Manager Patch Manager; "evento da AWS que afeta minhas instâncias" = Health Dashboard; "preciso de mais instâncias do que o limite permite" = Service Quotas; "instância superdimensionada" = Compute Optimizer; "mesma infraestrutura em várias contas" = CloudFormation StackSets.

### ➕ Complemento

**Tags:** pares chave-valor nos recursos, usados para organizar, controlar acesso e separar custos (ver cost allocation tags em [4.4](../04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)).

**Disponibilidade do Health Dashboard:** gratuito para todos os clientes; a API exige plano Business Support+ ou superior (no modelo clássico, Business).

## 3. Como analisar uma situação

**Primeiro, identifique o funcionamento:** CloudFormation cria stacks; Systems Manager opera recursos gerenciados; Config avalia configuração; CloudWatch observa operação; Trusted Advisor recomenda; Health informa eventos AWS.

**Depois, compare as escolhas:** Para criar: IaC. Para executar comandos/patches: Systems Manager. Para comparar regras: Config. Para recomendações de tamanho: Compute Optimizer. Para quota: Service Quotas.

**Por fim, verifique o limite:** Uma recomendação não altera o recurso automaticamente. Aumentar quota não é garantia de capacidade física disponível. Agentes, roles, suporte e integração variam por ferramenta.

## 4. Caso resolvido

Você quer aplicar patches em vários servidores e consultar limites da conta. Qual ferramenta para cada tarefa?

**Raciocínio e resposta:** Systems Manager Patch Manager para a operação de patch, com pré-requisitos atendidos; Service Quotas para limites e solicitações de aumento.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Explicar **template**, **stack**, **StackSets** e **drift detection** do CloudFormation.
- [ ] Citar os recursos do **Systems Manager** (Session Manager, Run Command, Patch Manager, Parameter Store).
- [ ] Diferenciar **Health Dashboard** (eventos da AWS) de **CloudWatch** (métricas dos seus recursos).
- [ ] Saber para que servem **Service Quotas**, **License Manager** e **Compute Optimizer**.

**Dica de revisão para a prova:** "Acessar sem SSH" → **Session Manager**. "Patch em 500 servidores" → **Patch Manager**. "Evento da AWS afeta minhas instâncias" → **Health Dashboard**. "Passar do limite" → **Service Quotas**. "Tamanho ideal" → **Compute Optimizer**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).
**Pergunta:** "Provisionar infraestrutura a partir de templates JSON/YAML."

**Resposta curta:** CloudFormation.

**Pergunta:** "Implantar a mesma stack em várias contas e regiões."

**Resposta curta:** CloudFormation StackSets.

**Pergunta:** "Gerenciar e aplicar patches em uma frota de instâncias, inclusive on-premises."

**Resposta curta:** Systems Manager.

**Pergunta:** "Acessar a instância sem abrir a porta 22."

**Resposta curta:** Systems Manager Session Manager.

**Pergunta:** "Ver eventos de manutenção da AWS que afetam meus recursos."

**Resposta curta:** AWS Health Dashboard.

**Pergunta:** "Pedir aumento do limite de instâncias."

**Resposta curta:** Service Quotas.

**Pergunta:** "Controlar quantas licenças de SQL Server estão em uso."

**Resposta curta:** License Manager.

**Pergunta:** "Recomendar o tamanho ideal das instâncias com base no uso."

**Resposta curta:** Compute Optimizer.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.15 Ferramentas de desenvolvimento](15-ferramentas-de-desenvolvimento.md) · 🏠 [Índice do domínio](README.md) · [3.17 Migração e transferência](17-migracao-e-transferencia.md) ➡️
