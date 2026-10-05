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

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

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

**Antes de ler este trecho:**

- **AWS CloudFormation:** CloudFormation usa um arquivo de descrição para criar e atualizar conjuntos de recursos AWS compatíveis, com suas dependências.
- **CloudFormation:** Infraestrutura como código descreve recursos em arquivos. CloudFormation usa templates e stacks para criar e administrar recursos compatíveis.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.


**AWS CloudFormation:** infraestrutura como código nativa.

**Antes de ler este trecho:**

- **JSON:** Formatos de dados com estruturas diferentes. O formato influencia como uma ferramenta lê e processa os arquivos; não muda sozinho o significado dos registros.
- **YAML:** Formatos de representação de dados e configurações. Um arquivo nesses formatos descreve informações; ele não cria permissões nem recursos sem ser usado por uma ferramenta.
- **stack:** Conjunto de recursos administrados a partir de uma descrição CloudFormation. Excluir ou atualizar a stack pode afetar os recursos conforme suas políticas.


  - **Templates** em JSON ou YAML descrevem os recursos; cada execução cria uma **stack** (pilha) gerenciada como uma unidade.

  - **StackSets:** implantam a mesma stack em várias contas e regiões.

  - **Drift detection:** detecta recursos alterados manualmente fora do template.

  - O serviço é gratuito; paga-se só pelos recursos criados.
**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **AWS Systems Manager / Systems Manager:** Systems Manager reúne ferramentas de operação para recursos e nós gerenciados compatíveis, incluindo acesso, automação, inventário e gerenciamento de patches.
- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.
- **SSM:** Sigla usada em recursos do Systems Manager. O serviço oferece ferramentas de administração; nós, acessos e conectividade precisam estar preparados.


**AWS Systems Manager:** central de operações para gerenciar frotas de instâncias EC2 e servidores on-premises (via agente SSM).

**Antes de ler este trecho:**

- **porta:** Número que ajuda a identificar o serviço de destino de uma comunicação. Liberar uma porta autoriza tráfego segundo a regra, mas não configura a aplicação para responder.
- **SSH:** Protocolo para acesso remoto protegido, comum na administração de Linux. Permissão para conectar pela rede e autorização para entrar no sistema são coisas diferentes.


  - **Session Manager:** acesso ao shell sem abrir porta SSH nem usar bastion host.

  - **Run Command:** executa comandos em várias instâncias de uma vez.
**Antes de ler este trecho:**

- **patch:** Atualização corretiva de software. A responsabilidade de aplicá-la depende da camada e do serviço usado.


  - **Patch Manager:** automatiza a aplicação de patches.
**Antes de ler este trecho:**

- **Parameter Store:** Recurso de armazenamento de parâmetros do Systems Manager. É necessário configurar proteção e permissão, inclusive para valores sensíveis.


  - **Parameter Store:** guarda configurações e segredos (ver [2.3](../02-seguranca-e-conformidade/03-iam.md)).

  - **Automation** e **Inventory:** runbooks automatizados e inventário de software.
**Antes de ler este trecho:**

- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.
- **CloudTrail:** Registro de atividades e chamadas AWS compatíveis. Ajuda a analisar quem realizou uma operação, em vez de medir sozinho a velocidade da aplicação.
- **Config:** Serviço que acompanha configurações e suas avaliações em recursos compatíveis. Observar configuração é diferente de observar uma métrica de desempenho.


**Monitoramento e auditoria:** CloudWatch, CloudTrail e Config (ver [2.7](../02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)).

**Antes de ler este trecho:**

- **Organizations:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.
- **Control Tower:** Control Tower ajuda a estabelecer e governar esse ambiente usando serviços AWS integrados e controles compatíveis.
- **RAM:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.


**Governança multi-conta:** Organizations, Control Tower, Service Catalog e RAM (ver [2.4](../02-seguranca-e-conformidade/04-governanca-multi-conta.md)).

**Antes de ler este trecho:**

- **AWS Health Dashboard / Health Dashboard:** AWS Health apresenta eventos sobre a saúde dos serviços e informações relevantes aos recursos da conta, conforme a visão consultada.


**AWS Health Dashboard:**


  - **Service health:** status público de todos os serviços em todas as regiões.

  - **Your account health:** eventos que afetam **os seus** recursos (manutenções agendadas, falhas, avisos), com orientação de correção.
**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.


  - A **AWS Health API** está disponível a partir do plano Business Support+ (no modelo clássico, Business).
**Antes de ler este trecho:**

- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.


**Service Quotas:** mostra os limites (cotas) dos serviços por região e permite **pedir aumento**. Pode gerar alarmes quando o uso se aproxima do limite.

**Antes de ler este trecho:**

- **SAP:** Tecnologias e aplicações empresariais do ecossistema SAP. Podem exigir requisitos específicos de memória, licenciamento e operação.


**AWS License Manager:** controla o uso de **licenças de software** (Microsoft, Oracle, SAP) para evitar excesso e multas.

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **ECS:** O ECS coordena a execução de containers: pacotes com a aplicação e suas dependências.
- **Fargate:** Fargate fornece a capacidade para executar containers com ECS ou EKS, sem você administrar diretamente os servidores dessa execução.
- **EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.
- **machine learning:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.


**AWS Compute Optimizer:** usa machine learning sobre as métricas de uso para recomendar o **tamanho ideal** de EC2, Auto Scaling groups, EBS, Lambda e tasks ECS no Fargate.

**Antes de ler este trecho:**

- **AWS Trusted Advisor / Trusted Advisor:** Trusted Advisor oferece verificações e recomendações em áreas como custos, segurança e operação, conforme o acesso disponível.


**AWS Trusted Advisor:** ver [2.9](../02-seguranca-e-conformidade/09-deteccao-de-ameacas.md). **Well-Architected Tool:** ver [1.4](../01-conceitos-de-nuvem/04-well-architected-framework.md).


**AWS Management Console:** inclui o aplicativo móvel para acompanhar recursos e alarmes.

**Antes de ler este trecho:**

- **evento:** Informação sobre algo que aconteceu. Uma regra pode encaminhar o evento; outro componente realiza a ação de negócio.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.


**Cai na prova:** "acessar instância sem SSH nem bastion" = Session Manager; "aplicar patch em 500 servidores" = Systems Manager Patch Manager; "evento da AWS que afeta minhas instâncias" = Health Dashboard; "preciso de mais instâncias do que o limite permite" = Service Quotas; "instância superdimensionada" = Compute Optimizer; "mesma infraestrutura em várias contas" = CloudFormation StackSets.

### ➕ Complemento

**Tags:** pares chave-valor nos recursos, usados para organizar, controlar acesso e separar custos (ver cost allocation tags em [4.4](../04-cobranca-precos-e-suporte/04-ferramentas-de-custo.md)).


**Disponibilidade do Health Dashboard:** gratuito para todos os clientes; a API exige plano Business Support+ ou superior (no modelo clássico, Business).

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **quota:** Limite de uso de um serviço ou recurso. Algumas quotas podem ser aumentadas mediante solicitação; limite não significa capacidade já reservada.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **suporte:** Suporte oferece ajuda conforme um plano e suas condições. Um prazo de resposta inicial não é garantia de tempo de resolução de todo incidente.


**Primeiro, identifique o funcionamento:** CloudFormation cria stacks; Systems Manager opera recursos gerenciados; Config avalia configuração; CloudWatch observa operação; Trusted Advisor recomenda; Health informa eventos AWS.

**Depois, compare as escolhas:** Para criar: IaC. Para executar comandos/patches: Systems Manager. Para comparar regras: Config. Para recomendações de tamanho: Compute Optimizer. Para quota: Service Quotas.

**Por fim, verifique o limite:** Uma recomendação não altera o recurso automaticamente. Aumentar quota não é garantia de capacidade física disponível. Agentes, roles, suporte e integração variam por ferramenta.

## 4. Caso resolvido

Você quer aplicar patches em vários servidores e consultar limites da conta. Qual ferramenta para cada tarefa?

**Raciocínio e resposta:** Systems Manager Patch Manager para a operação de patch, com pré-requisitos atendidos; Service Quotas para limites e solicitações de aumento.

A resposta muda se mudar o requisito destacado. Compare a necessidade com a função da solução, em vez de apenas associar duas palavras.

## 5. Revisão do capítulo

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

A aplicação já existe, mas a equipe precisa criar ambientes de modo repetível, administrar máquinas e acompanhar mudanças, saúde e regras.

**2. O que a solução fornece?**

Gestão e governança reúnem ferramentas para operar recursos e aplicar controles. Cada ferramenta observa ou administra uma parte específica.

**3. Que conclusão seria incorreta?**

Administrar recursos não significa que qualquer serviço de gestão executa todas essas tarefas. Descubra a ação desejada antes de escolher o produto.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

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

**Antes de ler este trecho:**

- **provisionar:** Criar ou disponibilizar capacidade e recursos. Um recurso provisionado pode ter cobrança mesmo enquanto está esperando trabalho.


**Fundamento explicado no capítulo:** "Provisionar infraestrutura a partir de templates JSON/YAML." → CloudFormation.

**Pergunta:** "Implantar a mesma stack em várias contas e regiões."

**Resposta curta:** CloudFormation StackSets.


**Fundamento explicado no capítulo:** "Implantar a mesma stack em várias contas e regiões." → CloudFormation StackSets.

**Pergunta:** "Gerenciar e aplicar patches em uma frota de instâncias, inclusive on-premises."

**Resposta curta:** Systems Manager.


**Fundamento explicado no capítulo:** "Gerenciar e aplicar patches em uma frota de instâncias, inclusive on-premises." → Systems Manager.

**Pergunta:** "Acessar a instância sem abrir a porta 22."

**Resposta curta:** Systems Manager Session Manager.


**Fundamento explicado no capítulo:** "Acessar a instância sem abrir a porta 22." → Systems Manager Session Manager.

**Pergunta:** "Ver eventos de manutenção da AWS que afetam meus recursos."

**Resposta curta:** AWS Health Dashboard.


**Fundamento explicado no capítulo:** "Ver eventos de manutenção da AWS que afetam meus recursos." → AWS Health Dashboard.

**Pergunta:** "Pedir aumento do limite de instâncias."

**Resposta curta:** Service Quotas.


**Fundamento explicado no capítulo:** "Pedir aumento do limite de instâncias." → Service Quotas.

**Pergunta:** "Controlar quantas licenças de SQL Server estão em uso."

**Resposta curta:** License Manager.

**Antes de ler este trecho:**

- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.


**Fundamento explicado no capítulo:** "Controlar quantas licenças de SQL Server estão em uso." → License Manager.

**Pergunta:** "Recomendar o tamanho ideal das instâncias com base no uso."

**Resposta curta:** Compute Optimizer.


**Fundamento explicado no capítulo:** "Recomendar o tamanho ideal das instâncias com base no uso." → Compute Optimizer.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.15 Ferramentas de desenvolvimento](15-ferramentas-de-desenvolvimento.md) · 🏠 [Índice do domínio](README.md) · [3.17 Migração e transferência](17-migracao-e-transferencia.md) ➡️
