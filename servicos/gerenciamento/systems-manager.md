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

## 1. A sequência de funcionamento

**Passo 1.** Prepare as máquinas para torná-las nós gerenciados, com requisitos de agente, rede e identidade atendidos.

**Passo 2.** Escolha a ferramenta operacional correspondente, como sessão, comando ou atualização. Execute a ação autorizada.

**Passo 3.** Confira resultados e falhas em cada alvo. Administrar muitas máquinas não torna toda operação segura sem planejamento.

## 2. Recursos e opções, com significado

### Pré-requisitos

**SSM Agent** instalado (vem nas AMIs da AWS) + **IAM role** com `AmazonSSMManagedInstanceCore` + conectividade com os endpoints do SSM (internet/NAT ou VPC endpoints).

On-premises: *hybrid activations*.

### Capacidades principais

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

Não basta o recurso existir na conta: agente, identidade, rede e demais requisitos variam conforme a função. Automatizar exige permissões e procedimentos definidos.

### ⚠️ Não confundir

Systems Manager (opera **dentro** das instâncias) × Config (avalia **configuração** dos recursos) × CloudFormation (cria a infraestrutura).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

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

### ❓ Perguntas típicas

**Pergunta:** "Gerenciar e aplicar patches numa frota, inclusive on-premises."

**Resposta curta:** Systems Manager (Patch Manager).

**Pergunta:** "Acessar a instância sem abrir a porta 22."

**Resposta curta:** Session Manager.

**Pergunta:** "Executar o mesmo comando em centenas de instâncias."

**Resposta curta:** Run Command.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
