# AWS Firewall Manager e AWS Network Firewall

> **Categoria:** Segurança de rede · **Domínio:** 2 · **Escopo:** Organização (Firewall Manager) / VPC (Network Firewall) · **Tópico do guia:** [2.8 Proteção de rede e aplicações](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)
>
> **Em uma frase:** o Firewall Manager **governa** regras de firewall em todas as contas; o Network Firewall **é** um firewall gerenciado para a VPC.
>
> **Escopo oficial:** 🔀 Firewall Manager ✅ · Network Firewall ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** o Firewall Manager é o **síndico que aplica as mesmas regras em todos os prédios** (contas); o Network Firewall é um **firewall de verdade na entrada da VPC**.

- ✅ **Escolha quando:** precisa aplicar regras de WAF, Shield ou security groups em **todas as contas** da organização (Firewall Manager).
- 🚫 **Não é a resposta quando:** as regras são para **uma aplicação só** → [WAF](waf.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "mesmas regras em todas as contas" → Firewall Manager; "inspecionar todo o tráfego da VPC (IPS)" → Network Firewall (fora da prova).
<!-- didatico:fim -->

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Políticas centralizadas do Firewall Manager; endpoints/regras de Network Firewall |
| **O que você decide/configura?** | Escopo de contas/recursos e regras |
| **Em que ordem as coisas acontecem?** | Defina políticas comuns e aplique a recursos elegíveis com pré-requisitos |
| **O que pode fazer, e em que condição?** | Firewall Manager reduz repetição de administração entre contas |
| **O que não pode presumir?** | Não são o mesmo produto; Network Firewall está fora do escopo consultado |

**Caso comentado:** Mesma política WAF em várias contas: Firewall Manager, com Organizations e configuração necessária.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html) · [Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)
