# AWS Compute Optimizer, Service Quotas, License Manager e outros

> **Categoria:** Gerenciamento / otimização e governança · **Domínio:** 3 e 4 · **Escopo:** Regional · **Tópico do guia:** [3.16 Gestão e governança](../../docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md)
>
> **Em uma frase:** ferramentas para dimensionar recursos, controlar limites e licenças, e organizar o ambiente.

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
| **AWS Launch Wizard** | Implantar SAP, SQL Server, Active Directory com boas práticas |
| **AWS AppConfig** | Feature flags e configuração dinâmica de aplicações (parte do Systems Manager) |
| **Well-Architected Tool** | Revisão gratuita de cargas contra os 6 pilares ([1.4](../../docs/01-conceitos-de-nuvem/04-well-architected-framework.md)) |
| **AWS Management Console mobile app** | Acompanhar recursos, alarmes e Health no celular |

## ❓ Perguntas típicas

- "Recomendar o tamanho ideal das instâncias com base no uso." → Compute Optimizer.
- "Pedir aumento do limite de instâncias." → Service Quotas.
- "Controlar quantas licenças de SQL Server estão em uso." → License Manager.

## 🔗 Documentação oficial

- [Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) · [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) · [License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager.html)
