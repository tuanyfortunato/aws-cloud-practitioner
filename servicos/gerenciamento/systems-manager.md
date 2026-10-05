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

## Pré-requisitos

- **SSM Agent** instalado (vem nas AMIs da AWS) + **IAM role** com `AmazonSSMManagedInstanceCore` + conectividade com os endpoints do SSM (internet/NAT ou VPC endpoints).
- On-premises: *hybrid activations*.

## Capacidades principais

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

## Cobrança

- A maioria das capacidades é **gratuita** para EC2; pagos: nós on-premises avançados, Automation acima da cota, Parameter Store Advanced, OpsCenter etc.

## ⚠️ Não confundir

- Systems Manager (opera **dentro** das instâncias) × Config (avalia **configuração** dos recursos) × CloudFormation (cria a infraestrutura).

## ❓ Perguntas típicas

- "Gerenciar e aplicar patches numa frota, inclusive on-premises." → Systems Manager (Patch Manager).
- "Acessar a instância sem abrir a porta 22." → Session Manager.
- "Executar o mesmo comando em centenas de instâncias." → Run Command.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Managed nodes, Session Manager, Run Command, Patch Manager e Automation |
| **O que você decide/configura?** | Agente/conectividade/role e documentos de operação |
| **Em que ordem as coisas acontecem?** | Registre o nó e use capacidade operacional autorizada |
| **O que pode fazer, e em que condição?** | Permite comandos, sessões e patches em recursos elegíveis |
| **O que não pode presumir?** | Session Manager exige pré-requisitos; fechar SSH não dispensa configuração do serviço |

**Caso comentado:** Operar EC2 sem porta 22 aberta: Session Manager com agente, role e endpoints/rede adequados.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)
