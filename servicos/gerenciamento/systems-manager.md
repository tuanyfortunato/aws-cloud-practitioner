# AWS Systems Manager (SSM)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A equipe administra muitas máquinas e precisa executar comandos, aplicar atualizações e acessar ambientes sem repetir cada tarefa manualmente.

**Como este serviço ajuda?** Systems Manager reúne ferramentas de operação para recursos e nós gerenciados compatíveis, incluindo acesso, automação, inventário e gerenciamento de patches.

**Exemplo do dia a dia:** A equipe usa Session Manager para uma sessão autorizada e planeja atualizações com ferramentas de patch, em vez de entrar separadamente em cada máquina.

**O que ele não resolve sozinho?** Não basta o recurso existir na conta: agente, identidade, rede e demais requisitos variam conforme a função. Automatizar exige permissões e procedimentos definidos.

**Primeiras palavras para entender:**

- **Nó gerenciado:** máquina preparada para usar essas ferramentas.
- **Patch:** atualização corretiva.
- **Runbook:** procedimento de automação.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Gerenciamento / operações · **Domínio:** 3 · **Escopo:** Regional (EC2, on-premises e outras nuvens) · **Tópico do guia:** [3.16 Gestão e governança](../../docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md)
>
> **Em uma frase:** central de operações para gerenciar **frotas** de servidores (EC2, on-premises, VMs) em escala, sem acesso manual.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.


**Passo 1.** Prepare as máquinas para torná-las nós gerenciados, com requisitos de agente, rede e identidade atendidos.

**Passo 2.** Escolha a ferramenta operacional correspondente, como sessão, comando ou atualização. Execute a ação autorizada.

**Passo 3.** Confira resultados e falhas em cada alvo. Administrar muitas máquinas não torna toda operação segura sem planejamento.

## 2. Recursos e opções, com significado

### Pré-requisitos

**Antes de ler este trecho:**

- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **NAT:** Tradução de endereços de rede. Um NAT Gateway pode permitir conexões de saída de determinados recursos privados sem oferecer entrada direta iniciada pela internet.
- **role:** Papel que fornece permissões a uma sessão que o assume. O termo função IAM não significa um trecho de código como uma função Lambda.
- **SSM:** Sigla usada em recursos do Systems Manager. O serviço oferece ferramentas de administração; nós, acessos e conectividade precisam estar preparados.


**SSM Agent** instalado (vem nas AMIs da AWS) + **IAM role** com `AmazonSSMManagedInstanceCore` + conectividade com os endpoints do SSM (internet/NAT ou VPC endpoints).

**Antes de ler este trecho:**

- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.


On-premises: *hybrid activations*.

### Capacidades principais

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.
- **Config:** Serviço que acompanha configurações e suas avaliações em recursos compatíveis. Observar configuração é diferente de observar uma métrica de desempenho.
- **CLI:** SDK fornece bibliotecas para programas chamarem APIs; CLI fornece comandos de texto. As duas formas continuam exigindo identidade, autorização e configuração.
- **SO:** Software básico da máquina, como Linux ou Windows. Ele administra arquivos, memória e execução de programas; atualizar esse software é diferente de atualizar a aplicação.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **porta:** Número que ajuda a identificar o serviço de destino de uma comunicação. Liberar uma porta autoriza tráfego segundo a regra, mas não configura a aplicação para responder.
- **SSH:** Protocolo para acesso remoto protegido, comum na administração de Linux. Permissão para conectar pela rede e autorização para entrar no sistema são coisas diferentes.
- **AMI:** Imagem de máquina EC2: modelo com o software necessário para iniciar uma instância. A imagem precisa ser compatível com a configuração de execução escolhida.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.
- **script:** Programa de instruções usado para automatizar tarefas. O script realiza o que foi descrito; não decide sozinho como instalar ou proteger qualquer sistema.
- **patch:** Atualização corretiva de software. A responsabilidade de aplicá-la depende da camada e do serviço usado.
- **Parameter Store:** Recurso de armazenamento de parâmetros do Systems Manager. É necessário configurar proteção e permissão, inclusive para valores sensíveis.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Capacidade | O que faz | Exemplo de prova |
|---|---|---|
| **Session Manager** | Shell/PowerShell no navegador ou CLI **sem porta 22/3389, sem bastion, sem chaves SSH**; sessões auditadas (logs no S3/CloudWatch) | "Acessar instância sem abrir SSH" |
| **Run Command** | Executa comandos/scripts em muitas instâncias ao mesmo tempo | "Rodar script em 200 servidores" |
| **Patch Manager** | Aplica patches de SO/aplicações com **patch baselines** e **maintenance windows** | "Aplicar patches em 500 servidores" |
| **State Manager** | Mantém configuração desejada (ex.: agente instalado) | — |
| **Automation** | **Runbooks** para tarefas operacionais (criar AMI, remediar achados do Config) | "Remediação automática" |
| **Parameter Store** | Configurações e segredos ([ficha](../seguranca/secrets-manager-e-parameter-store.md)) | — |
| **Inventory** | Software instalado, configurações | "Quais servidores têm a versão X?" |
| **Fleet Manager** | Console para gerenciar os nós remotamente | — |
| **Distributor** | Distribui pacotes de software | — |
| **OpsCenter / Explorer** | Itens operacionais e visão agregada | — |
| **Incident Manager / Change Manager** | Resposta a incidentes / aprovação de mudanças | 🔄 Fechados a novos clientes desde 07/11/2025 |
| **Maintenance Windows** | Janelas agendadas para tarefas | — |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.


Não basta o recurso existir na conta: agente, identidade, rede e demais requisitos variam conforme a função. Automatizar exige permissões e procedimentos definidos.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **Systems Manager:** Systems Manager reúne ferramentas de operação para recursos e nós gerenciados compatíveis, incluindo acesso, automação, inventário e gerenciamento de patches.
- **CloudFormation:** Infraestrutura como código descreve recursos em arquivos. CloudFormation usa templates e stacks para criar e administrar recursos compatíveis.


Systems Manager (opera **dentro** das instâncias) × Config (avalia **configuração** dos recursos) × CloudFormation (cria a infraestrutura).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.


A maioria das capacidades é **gratuita** para EC2; pagos: nós on-premises avançados, Automation acima da cota, Parameter Store Advanced, OpsCenter etc.

## 5. Caso resolvido: ligando as peças

A equipe usa Session Manager para uma sessão autorizada e planeja atualizações com ferramentas de patch, em vez de entrar separadamente em cada máquina.

**Aplicando a sequência à situação:**

**Etapa 1:** Prepare as máquinas para torná-las nós gerenciados, com requisitos de agente, rede e identidade atendidos.
**Etapa 2:** Escolha a ferramenta operacional correspondente, como sessão, comando ou atualização. Execute a ação autorizada.
**Etapa 3:** Confira resultados e falhas em cada alvo. Administrar muitas máquinas não torna toda operação segura sem planejamento.

**Resultado e responsabilidade:** Systems Manager reúne ferramentas de operação para recursos e nós gerenciados compatíveis, incluindo acesso, automação, inventário e gerenciamento de patches.

**Recursos envolvidos:** Managed nodes, Session Manager, Run Command, Patch Manager e Automation.

**Decisões que precisam ser tomadas:** Agente/conectividade/role e documentos de operação.


**Outra situação comentada:** Operar EC2 sem porta 22 aberta: Session Manager com agente, role e endpoints/rede adequados.

**Por que não concluir mais do que isso:** Session Manager exige pré-requisitos; fechar SSH não dispensa configuração do serviço

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

A equipe administra muitas máquinas e precisa executar comandos, aplicar atualizações e acessar ambientes sem repetir cada tarefa manualmente.

**2. O que a solução fornece?**

Systems Manager reúne ferramentas de operação para recursos e nós gerenciados compatíveis, incluindo acesso, automação, inventário e gerenciamento de patches.

**3. Que conclusão seria incorreta?**

Não basta o recurso existir na conta: agente, identidade, rede e demais requisitos variam conforme a função. Automatizar exige permissões e procedimentos definidos.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Gerenciar e aplicar patches numa frota, inclusive on-premises."

**Resposta curta:** Systems Manager (Patch Manager).


**Fundamento explicado no capítulo:** "Gerenciar e aplicar patches numa frota, inclusive on-premises." → Systems Manager (Patch Manager).

**Pergunta:** "Acessar a instância sem abrir a porta 22."

**Resposta curta:** Session Manager.


**Fundamento explicado no capítulo:** "Acessar a instância sem abrir a porta 22." → Session Manager.

**Pergunta:** "Executar o mesmo comando em centenas de instâncias."

**Resposta curta:** Run Command.


**Fundamento explicado no capítulo:** "Executar o mesmo comando em centenas de instâncias." → Run Command.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
