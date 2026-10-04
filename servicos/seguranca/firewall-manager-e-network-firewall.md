# AWS Firewall Manager e AWS Network Firewall

> **Categoria:** Segurança de rede · **Domínio:** 2 · **Escopo:** Organização (Firewall Manager) / VPC (Network Firewall) · **Tópico do guia:** [2.8 Proteção de rede e aplicações](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)
>
> **Em uma frase:** o Firewall Manager **governa** regras de firewall em todas as contas; o Network Firewall **é** um firewall gerenciado para a VPC.
>
> **Escopo oficial:** 🔀 Firewall Manager ✅ · Network Firewall ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## AWS Firewall Manager

| Item | Detalhe |
|---|---|
| **Função** | Gerenciamento **central** de políticas de segurança em todas as contas e recursos do **AWS Organizations**, aplicando-as automaticamente a novos recursos. |
| **Políticas** | **WAF**, **Shield Advanced**, **security groups** (auditoria e regras comuns), **Network Firewall**, **Route 53 Resolver DNS Firewall**, firewalls de terceiros do Marketplace. |
| **Pré-requisitos** | AWS Organizations (todos os recursos), **AWS Config** ativado, conta administradora do Firewall Manager. |
| **Cobrança** | Por política por região/mês + recursos subjacentes (WAF, Config). |

## AWS Network Firewall ❌

> ❌ **Fora do escopo da CLF-C02** — documentado só para referência ([lista oficial](../../docs/00-guia-do-exame/escopo-oficial.md)).

| Item | Detalhe |
|---|---|
| **Função** | Firewall de rede **stateful**, gerenciado e escalável, para filtrar todo o tráfego que entra, sai ou atravessa a VPC. |
| **Regras** | Stateless e stateful; compatível com regras **Suricata** (IPS); filtragem por **domínio** (FQDN), IP, porta, protocolo; inspeção TLS. |
| **Implantação** | Endpoints numa *firewall subnet*; rotas direcionam o tráfego por ele; pode ficar centralizado com Transit Gateway. |
| **Uso** | Prevenção de intrusão (IPS), bloquear saída para domínios não autorizados, inspeção entre VPCs. |
| **Cobrança** | Por endpoint-hora + GB processado. |

## Comparação de "firewalls" da AWS

| Ferramenta | Camada | Onde |
|---|---|---|
| Security group | 3/4 | Instância/ENI (stateful) |
| Network ACL | 3/4 | Subnet (stateless) |
| **Network Firewall** | 3–7 | VPC (stateful, IPS, domínios) |
| **WAF** | 7 | CloudFront, ALB, API Gateway… |
| **Shield** | 3/4 (+7 Advanced) | DDoS |
| **Firewall Manager** | — | Governança central de todos acima |

## ❓ Perguntas típicas

- "Aplicar as mesmas regras de WAF em todas as contas." → Firewall Manager.
- "Inspecionar e filtrar todo o tráfego que entra na VPC (IPS)." → Network Firewall.

## 🔗 Documentação oficial

- [Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html) · [Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)
