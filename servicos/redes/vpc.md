# Amazon VPC (Virtual Private Cloud)

> **Categoria:** Rede · **Domínio:** 2 (segurança de rede) e 3 · **Escopo:** **Regional** (subnets em AZs) · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) · [2.8 Proteção de rede](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)
>
> **Em uma frase:** sua rede privada, isolada logicamente, dentro de uma região da AWS.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Componentes

| Componente | O que é | Detalhe de prova |
|---|---|---|
| **VPC** | Rede com bloco CIDR IPv4 (de /16 a /28) e opcionalmente IPv6 | Regional; cada região tem uma **VPC padrão** |
| **Subnet** | Faixa de IPs da VPC em **uma AZ** | A AWS reserva **5 IPs** por subnet 🧊 |
| **Subnet pública** | Tem rota `0.0.0.0/0` → **Internet Gateway** | Web servers, NAT Gateway, bastion |
| **Subnet privada** | Sem rota direta para o IGW | Bancos, back-ends |
| **Route table** | Regras de roteamento por subnet | Tabela *main* + tabelas customizadas |
| **Internet Gateway (IGW)** | Entrada e saída da internet | Um por VPC, escalável e redundante |
| **NAT Gateway** | **Só saída** para a internet a partir de subnets privadas | Fica na subnet pública, gerenciado, por AZ; pago por hora e GB |
| **Egress-only IGW** | "NAT" para IPv6 (só saída) | — |
| **Elastic IP** | IPv4 público estático | Cobrado por hora |
| **ENI** | Interface de rede virtual | Tem SGs, IPs privados/públicos |
| **Security group** | Firewall **stateful** da ENI/instância, só regras *allow* | Padrão: nega entrada, libera saída |
| **Network ACL** | Firewall **stateless** da subnet, regras *allow* e *deny* numeradas | NACL padrão libera tudo; precisa liberar portas efêmeras de retorno |
| **VPC Flow Logs** | Logs de tráfego IP (aceito/rejeitado) | Para CloudWatch Logs, S3 ou Firehose |
| **DHCP options / DNS** | Resolução de nomes dentro da VPC (Route 53 Resolver) | — |

## VPC padrão

- Criada em cada região: CIDR `172.31.0.0/16`, **uma subnet pública por AZ**, IGW anexado, instâncias recebem IP público.

## Security group × NACL

| | Security group | Network ACL |
|---|---|---|
| Nível | Instância / ENI | Subnet |
| Estado | **Stateful** (retorno automático) | **Stateless** (liberar ida e volta) |
| Regras | Só **allow** | **allow e deny** |
| Avaliação | Todas as regras | Em **ordem numérica**, primeira que casa |
| Padrão | Nega entrada / libera saída | (Padrão) libera tudo |
| Pode referenciar outro SG | Sim | Não |
| Bloquear IP específico | ❌ | ✅ |

## Ferramentas complementares

- **Reachability Analyzer** (testa se dois pontos se alcançam), **Network Access Analyzer**, **VPC IPAM** (gestão de endereços), **Traffic Mirroring**, **VPC Lattice** (conectividade entre serviços) — 🧊.
- Conectividade: ver [peering, Transit Gateway e endpoints](vpc-peering-transit-gateway-e-endpoints.md), [VPN](site-to-site-vpn-e-client-vpn.md) e [Direct Connect](direct-connect.md).

## Cobrança

- A VPC em si é gratuita. Pagos: NAT Gateway, IPv4 públicos, VPN, endpoints de interface, Transit Gateway, Flow Logs (ingestão), transferência entre AZs.

## Segurança e responsabilidade compartilhada

- **AWS:** infraestrutura de rede física e isolamento entre clientes.
- **Cliente:** desenho da VPC, rotas, SGs, NACLs, Flow Logs, exposição de recursos.

## ⚠️ Pegadinhas e não confundir

- O que torna uma subnet **pública** é a **rota para o IGW**.
- **NAT Gateway** permite sair, mas **não** receber conexões de fora.
- Bastion host × **Session Manager** (sem porta aberta, recomendado).

## ❓ Perguntas típicas

- "O que torna uma subnet pública?" → Rota para um Internet Gateway.
- "Instâncias privadas precisam baixar atualizações." → NAT Gateway.
- "Bloquear um IP malicioso na subnet." → Regra *deny* na NACL.
- "Firewall stateful no nível da instância." → Security group.
- "Capturar o tráfego de rede da VPC para análise." → VPC Flow Logs.

## 🔗 Documentação oficial

- [Guia do Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
