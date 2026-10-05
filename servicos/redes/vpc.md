# Amazon VPC (Virtual Private Cloud)

> **Categoria:** Rede · **Domínio:** 2 (segurança de rede) e 3 · **Escopo:** **Regional** (subnets em AZs) · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) · [2.8 Proteção de rede](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)
>
> **Em uma frase:** sua rede privada, isolada logicamente, dentro de uma região da AWS.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é o **seu terreno particular dentro da AWS**: você desenha os lotes (subnets), as ruas (rotas), os portões (gateways) e os seguranças (security groups e NACLs).

- ✅ **Escolha quando:** qualquer recurso precisa de uma **rede isolada e controlada** — é a base de quase tudo na AWS.
- 🚫 **Não é a resposta quando:** precisa ligar a VPC ao **datacenter** → [VPN](site-to-site-vpn-e-client-vpn.md) ou [Direct Connect](direct-connect.md); precisa ligar **várias VPCs** → [Peering ou Transit Gateway](vpc-peering-transit-gateway-e-endpoints.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "subnet pública ou privada", "Internet Gateway", "NAT Gateway", "security group × NACL", "Flow Logs".
<!-- didatico:fim -->

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | CIDR, subnets, rotas, gateways, endpoints, SGs e NACLs |
| **O que você decide/configura?** | Faixas de IP, AZs, caminhos e controles de rede |
| **Em que ordem as coisas acontecem?** | Crie rede e subnets; associe rotas e controles; conecte recursos |
| **O que pode fazer, e em que condição?** | Isola logicamente a rede e permite conectividade pública/privada planejada |
| **O que não pode presumir?** | SG aberto não cria rota; subnet pública não fornece endereço público automaticamente a toda carga |

**Caso comentado:** EC2 pública IPv4 exige rota ao IGW, endereço apropriado, regras e aplicação escutando.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
