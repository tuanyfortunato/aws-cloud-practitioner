# AWS Systems Manager (SSM)

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

## 🔗 Documentação oficial

- [Guia do Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)
