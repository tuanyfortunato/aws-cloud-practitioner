# Amazon VPC (Virtual Private Cloud)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma empresa precisa decidir como suas máquinas na AWS se comunicam, quais ficam acessíveis pela internet e quais ficam em áreas privadas.

**Como este serviço ajuda?** A VPC é uma rede virtual isolada logicamente para seus recursos. Nela você organiza segmentos de rede, caminhos de comunicação e controles de acesso.

**Exemplo do dia a dia:** A loja separa os servidores que recebem visitantes e o banco que só deve ser acessado pela aplicação. Essas áreas podem ser organizadas dentro de uma VPC.

**O que ele não resolve sozinho?** Criar uma VPC não torna os recursos públicos nem seguros automaticamente. Endereços, rotas e controles precisam atender ao desenho da aplicação.

**Primeiras palavras para entender:**

- **Rede:** caminhos de comunicação entre recursos.
- **Subnet:** segmento de uma VPC.
- **Rota:** regra que indica para onde encaminhar uma comunicação.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Rede · **Domínio:** 2 (segurança de rede) e 3 · **Escopo:** **Regional** (subnets em AZs) · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) · [2.8 Proteção de rede](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)
>
> **Em uma frase:** sua rede privada, isolada logicamente, dentro de uma região da AWS.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Defina a faixa de endereços e organize segmentos de rede para os recursos.

**Passo 2.** Configure caminhos de comunicação e regras de tráfego. Ter um endereço não basta sem rota e controles apropriados.

**Passo 3.** Teste as conexões necessárias e bloqueie as desnecessárias. Identidade da aplicação e permissões de dados são controles adicionais.

## 2. Recursos e opções, com significado

### Componentes

**VPC**

**O que é:** Rede com bloco CIDR IPv4 (de /16 a /28) e opcionalmente IPv6

**Detalhe de prova:** Regional; cada região tem uma **VPC padrão**

**Subnet**

**O que é:** Faixa de IPs da VPC em **uma AZ**

**Detalhe de prova:** A AWS reserva **5 IPs** por subnet 🧊

**Subnet pública**

**O que é:** Tem rota `0.0.0.0/0` → **Internet Gateway**

**Detalhe de prova:** Web servers, NAT Gateway, bastion

**Subnet privada**

**O que é:** Sem rota direta para o IGW

**Detalhe de prova:** Bancos, back-ends

**Route table**

**O que é:** Regras de roteamento por subnet

**Detalhe de prova:** Tabela *main* + tabelas customizadas

**Internet Gateway (IGW)**

**O que é:** Entrada e saída da internet

**Detalhe de prova:** Um por VPC, escalável e redundante

**NAT Gateway**

**O que é:** **Só saída** para a internet a partir de subnets privadas

**Detalhe de prova:** Fica na subnet pública, gerenciado, por AZ; pago por hora e GB

**Egress-only IGW**

**O que é:** "NAT" para IPv6 (só saída)

**Elastic IP**

**O que é:** IPv4 público estático

**Detalhe de prova:** Cobrado por hora

**ENI**

**O que é:** Interface de rede virtual

**Detalhe de prova:** Tem SGs, IPs privados/públicos

**Security group**

**O que é:** Firewall **stateful** da ENI/instância, só regras *allow*

**Detalhe de prova:** Padrão: nega entrada, libera saída

**Network ACL**

**O que é:** Firewall **stateless** da subnet, regras *allow* e *deny* numeradas

**Detalhe de prova:** NACL padrão libera tudo; precisa liberar portas efêmeras de retorno

**VPC Flow Logs**

**O que é:** Logs de tráfego IP (aceito/rejeitado)

**Detalhe de prova:** Para CloudWatch Logs, S3 ou Firehose

**DHCP options / DNS**

**O que é:** Resolução de nomes dentro da VPC (Route 53 Resolver)

### VPC padrão

Criada em cada região: CIDR `172.31.0.0/16`, **uma subnet pública por AZ**, IGW anexado, instâncias recebem IP público.

### Security group × NACL

| | Security group | Network ACL |
|---|---|---|
| Nível | Instância / ENI | Subnet |
| Estado | **Stateful** (retorno automático) | **Stateless** (liberar ida e volta) |
| Regras | Só **allow** | **allow e deny** |
| Avaliação | Todas as regras | Em **ordem numérica**, primeira que casa |
| Padrão | Nega entrada / libera saída | (Padrão) libera tudo |
| Pode referenciar outro SG | Sim | Não |
| Bloquear IP específico | ❌ | ✅ |

### Ferramentas complementares

**Reachability Analyzer** (testa se dois pontos se alcançam), **Network Access Analyzer**, **VPC IPAM** (gestão de endereços), **Traffic Mirroring**, **VPC Lattice** (conectividade entre serviços) — 🧊.

Conectividade: ver [peering, Transit Gateway e endpoints](vpc-peering-transit-gateway-e-endpoints.md), [VPN](site-to-site-vpn-e-client-vpn.md) e [Direct Connect](direct-connect.md).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Criar uma VPC não torna os recursos públicos nem seguros automaticamente. Endereços, rotas e controles precisam atender ao desenho da aplicação.

### ⚠️ Pegadinhas e não confundir

O que torna uma subnet **pública** é a **rota para o IGW**.

**NAT Gateway** permite sair, mas **não** receber conexões de fora.

Bastion host × **Session Manager** (sem porta aberta, recomendado).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

A VPC em si é gratuita. Pagos: NAT Gateway, IPv4 públicos, VPN, endpoints de interface, Transit Gateway, Flow Logs (ingestão), transferência entre AZs.

### Segurança e responsabilidade compartilhada

**AWS:** infraestrutura de rede física e isolamento entre clientes.

**Cliente:** desenho da VPC, rotas, SGs, NACLs, Flow Logs, exposição de recursos.

## 5. Caso resolvido: ligando as peças

A escola quer receber visitantes no site, mas não quer que eles se conectem diretamente ao banco. O objetivo é definir caminhos e controles distintos para partes diferentes da aplicação.

A equipe organiza recursos em subnets e prepara rotas compatíveis com a comunicação necessária. O recurso que atende visitantes precisa de um caminho adequado de entrada; o banco precisa de comunicação apenas com componentes autorizados. Security groups e outros controles de tráfego complementam o desenho.

Uma subnet pública tem relação com rota, não é uma permissão automática para todo recurso. Uma conexão que chega ao banco ainda precisa de autenticação e autorização do próprio banco. VPC trata rede; IAM trata operações AWS. Cumprir uma parte do acesso não substitui a outra.

**Recursos envolvidos:** CIDR, subnets, rotas, gateways, endpoints, SGs e NACLs.

**Decisões que precisam ser tomadas:** Faixas de IP, AZs, caminhos e controles de rede.

**Outra situação comentada:** EC2 pública IPv4 exige rota ao IGW, endereço apropriado, regras e aplicação escutando.

**Por que não concluir mais do que isso:** SG aberto não cria rota; subnet pública não fornece endereço público automaticamente a toda carga

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "O que torna uma subnet pública?"

**Resposta curta:** Rota para um Internet Gateway.

**Pergunta:** "Instâncias privadas precisam baixar atualizações."

**Resposta curta:** NAT Gateway.

**Pergunta:** "Bloquear um IP malicioso na subnet."

**Resposta curta:** Regra *deny* na NACL.

**Pergunta:** "Firewall stateful no nível da instância."

**Resposta curta:** Security group.

**Pergunta:** "Capturar o tráfego de rede da VPC para análise."

**Resposta curta:** VPC Flow Logs.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
