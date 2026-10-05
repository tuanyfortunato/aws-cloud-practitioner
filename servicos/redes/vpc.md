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

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.
- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.


**Passo 1.** Defina a faixa de endereços e organize segmentos de rede para os recursos.

**Passo 2.** Configure caminhos de comunicação e regras de tráfego. Ter um endereço não basta sem rota e controles apropriados.

**Passo 3.** Teste as conexões necessárias e bloqueie as desnecessárias. Identidade da aplicação e permissões de dados são controles adicionais.

## 2. Recursos e opções, com significado

### Componentes

**VPC**

**Antes de ler este trecho:**

- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **regional:** O recurso ou a operação pertence a uma região. Serviços globais podem administrar objetos regionais; leia o alcance do recurso, não apenas o nome do serviço.
- **IPv4 / IPv6:** Endereços usados para identificar interfaces e destinos na rede. IPv4 e IPv6 são versões diferentes; ter um endereço não concede permissão nem garante uma rota.
- **CIDR:** Notação de faixa de endereços de rede, como um endereço acompanhado de /24. A faixa define um conjunto de endereços, não uma senha ou uma permissão.


**O que é:** Rede com bloco CIDR IPv4 (de /16 a /28) e opcionalmente IPv6

**Detalhe de prova:** Regional; cada região tem uma **VPC padrão**

**Subnet**

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **AZ:** Parte isolada da infraestrutura dentro de uma região, formada por um ou mais datacenters. Distribuir recursos entre zonas pode reduzir o impacto de uma falha localizada.
- **subnet:** Segmento de uma rede virtual. Na VPC, uma subnet pertence a uma zona de disponibilidade; suas rotas e controles ajudam a definir a conectividade.


**O que é:** Faixa de IPs da VPC em **uma AZ**

**Detalhe de prova:** A AWS reserva **5 IPs** por subnet 🧊

**Subnet pública**

**Antes de ler este trecho:**

- **Internet Gateway:** Componente que permite conectividade da VPC com a internet conforme as rotas, endereços e controles usados. Não torna todo recurso público automaticamente.
- **NAT:** Tradução de endereços de rede. Um NAT Gateway pode permitir conexões de saída de determinados recursos privados sem oferecer entrada direta iniciada pela internet.


**O que é:** Tem rota `0.0.0.0/0` → **Internet Gateway**

**Detalhe de prova:** Web servers, NAT Gateway, bastion

**Subnet privada**


**O que é:** Sem rota direta para o IGW

**Detalhe de prova:** Bancos, back-ends

**Route table**

**Antes de ler este trecho:**

- **route table:** Conjunto de regras que indica para onde encaminhar tráfego destinado a determinadas faixas. A rota é parte do caminho, não uma autorização de identidade.


**O que é:** Regras de roteamento por subnet

**Detalhe de prova:** Tabela *main* + tabelas customizadas

**Internet Gateway (IGW)**


**O que é:** Entrada e saída da internet

**Detalhe de prova:** Um por VPC, escalável e redundante

**NAT Gateway**

**Antes de ler este trecho:**

- **GB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.
- **hora:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.


**O que é:** **Só saída** para a internet a partir de subnets privadas

**Detalhe de prova:** Fica na subnet pública, gerenciado, por AZ; pago por hora e GB

**Egress-only IGW**


**O que é:** "NAT" para IPv6 (só saída)

**Elastic IP**


**O que é:** IPv4 público estático

**Detalhe de prova:** Cobrado por hora

**ENI**

**Antes de ler este trecho:**

- **virtual:** Um recurso virtual é criado por software sobre equipamentos físicos. VM significa máquina virtual: computador lógico com sistema operacional e recursos de processamento.
- **ENI:** Interface de rede virtual. Ela associa endereços e configurações de comunicação a recursos compatíveis.


**O que é:** Interface de rede virtual

**Detalhe de prova:** Tem SGs, IPs privados/públicos

**Security group**

**Antes de ler este trecho:**

- **security group:** Regras de tráfego associadas a interfaces ou recursos compatíveis. É um controle de rede, não uma permissão IAM para ler um arquivo ou chamar uma API.
- **stateful:** Controle que acompanha o estado da comunicação e trata respostas conforme esse estado. No security group, isso evita exigir uma regra independente para a resposta de uma conexão permitida.
- **firewall:** Controle que permite ou bloqueia comunicação segundo regras. Sua cobertura depende da camada e do ponto em que é aplicado.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.


**O que é:** Firewall **stateful** da ENI/instância, só regras *allow*

**Detalhe de prova:** Padrão: nega entrada, libera saída

**Network ACL**

**Antes de ler este trecho:**

- **stateless:** Controle que avalia cada direção sem manter o mesmo estado de conexão. Regras de ida e de volta precisam ser consideradas separadamente.
- **ACL / NACL / Network ACL:** ACL significa lista de controle de acesso. A NACL da VPC controla tráfego no segmento de rede; ACL de armazenamento tem outro contexto. Não trate as duas como a mesma função.


**O que é:** Firewall **stateless** da subnet, regras *allow* e *deny* numeradas

**Detalhe de prova:** NACL padrão libera tudo; precisa liberar portas efêmeras de retorno

**VPC Flow Logs**

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.


**O que é:** Logs de tráfego IP (aceito/rejeitado)

**Detalhe de prova:** Para CloudWatch Logs, S3 ou Firehose

**DHCP options / DNS**

**Antes de ler este trecho:**

- **Route 53:** Route 53 oferece DNS e recursos associados, como registro de domínios e verificações de saúde.
- **DNS:** Sistema que relaciona nomes a informações de endereço e outros registros. Resolver o nome de um site não hospeda o site nem garante que ele está funcionando.
- **DHCP:** Mecanismo para fornecer configuração de rede a dispositivos, como endereços e parâmetros. É diferente de encaminhar tráfego ou autorizar uma chamada AWS.


**O que é:** Resolução de nomes dentro da VPC (Route 53 Resolver)

### VPC padrão

Criada em cada região: CIDR `172.31.0.0/16`, **uma subnet pública por AZ**, IGW anexado, instâncias recebem IP público.

### Security group × NACL

Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

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

**Antes de ler este trecho:**

- **IPAM:** Gerenciamento de endereços IP: organização e acompanhamento de faixas e utilização. Não substitui as rotas e os controles de comunicação.


**Reachability Analyzer** (testa se dois pontos se alcançam), **Network Access Analyzer**, **VPC IPAM** (gestão de endereços), **Traffic Mirroring**, **VPC Lattice** (conectividade entre serviços) — 🧊.

**Antes de ler este trecho:**

- **VPN:** Conexão lógica protegida que liga usuários ou redes. Um túnel VPN não concede automaticamente acesso a todos os recursos do destino.
- **Direct Connect:** Direct Connect permite estabelecer essa conectividade por conexões e locais compatíveis, com interfaces e rotas configuradas para o ambiente.
- **Connect:** Amazon Connect oferece uma plataforma de contact center em nuvem com canais e recursos compatíveis.


Conectividade: ver [peering, Transit Gateway e endpoints](vpc-peering-transit-gateway-e-endpoints.md), [VPN](site-to-site-vpn-e-client-vpn.md) e [Direct Connect](direct-connect.md).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Criar uma VPC não torna os recursos públicos nem seguros automaticamente. Endereços, rotas e controles precisam atender ao desenho da aplicação.

### ⚠️ Pegadinhas e não confundir

O que torna uma subnet **pública** é a **rota para o IGW**.


**NAT Gateway** permite sair, mas **não** receber conexões de fora.

**Antes de ler este trecho:**

- **porta:** Número que ajuda a identificar o serviço de destino de uma comunicação. Liberar uma porta autoriza tráfego segundo a regra, mas não configura a aplicação para responder.


Bastion host × **Session Manager** (sem porta aberta, recomendado).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

A VPC em si é gratuita. Pagos: NAT Gateway, IPv4 públicos, VPN, endpoints de interface, Transit Gateway, Flow Logs (ingestão), transferência entre AZs.

### Segurança e responsabilidade compartilhada

**AWS:** infraestrutura de rede física e isolamento entre clientes.


**Cliente:** desenho da VPC, rotas, SGs, NACLs, Flow Logs, exposição de recursos.

## 5. Caso resolvido: ligando as peças

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **autenticação:** Verificação de quem está acessando. Confirmar a identidade não autoriza qualquer ação no sistema.
- **autorização:** Decisão sobre o que uma identidade pode fazer em um recurso. Essa decisão depende das regras e do contexto da solicitação.


A escola quer receber visitantes no site, mas não quer que eles se conectem diretamente ao banco. O objetivo é definir caminhos e controles distintos para partes diferentes da aplicação.

A equipe organiza recursos em subnets e prepara rotas compatíveis com a comunicação necessária. O recurso que atende visitantes precisa de um caminho adequado de entrada; o banco precisa de comunicação apenas com componentes autorizados. Security groups e outros controles de tráfego complementam o desenho.

Uma subnet pública tem relação com rota, não é uma permissão automática para todo recurso. Uma conexão que chega ao banco ainda precisa de autenticação e autorização do próprio banco. VPC trata rede; IAM trata operações AWS. Cumprir uma parte do acesso não substitui a outra.

**Recursos envolvidos:** CIDR, subnets, rotas, gateways, endpoints, SGs e NACLs.

**Decisões que precisam ser tomadas:** Faixas de IP, AZs, caminhos e controles de rede.

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **carga:** Aplicação ou conjunto de tarefas com seus recursos e necessidades. Avaliar uma carga significa avaliar o trabalho completo, não uma única máquina isolada.


**Outra situação comentada:** EC2 pública IPv4 exige rota ao IGW, endereço apropriado, regras e aplicação escutando.

**Por que não concluir mais do que isso:** SG aberto não cria rota; subnet pública não fornece endereço público automaticamente a toda carga

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Uma empresa precisa decidir como suas máquinas na AWS se comunicam, quais ficam acessíveis pela internet e quais ficam em áreas privadas.

**2. O que a solução fornece?**

A VPC é uma rede virtual isolada logicamente para seus recursos. Nela você organiza segmentos de rede, caminhos de comunicação e controles de acesso.

**3. Que conclusão seria incorreta?**

Criar uma VPC não torna os recursos públicos nem seguros automaticamente. Endereços, rotas e controles precisam atender ao desenho da aplicação.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "O que torna uma subnet pública?"

**Resposta curta:** Rota para um Internet Gateway.


**Fundamento explicado no capítulo:** "O que torna uma subnet pública?" → Rota para um Internet Gateway.

**Pergunta:** "Instâncias privadas precisam baixar atualizações."

**Resposta curta:** NAT Gateway.


**Fundamento explicado no capítulo:** "Instâncias privadas precisam baixar atualizações." → NAT Gateway.

**Pergunta:** "Bloquear um IP malicioso na subnet."

**Resposta curta:** Regra *deny* na NACL.


**Fundamento explicado no capítulo:** "Bloquear um IP malicioso na subnet." → Regra *deny* na NACL.

**Pergunta:** "Firewall stateful no nível da instância."

**Resposta curta:** Security group.


**Fundamento explicado no capítulo:** "Firewall stateful no nível da instância." → Security group.

**Pergunta:** "Capturar o tráfego de rede da VPC para análise."

**Resposta curta:** VPC Flow Logs.


**Fundamento explicado no capítulo:** "Capturar o tráfego de rede da VPC para análise." → VPC Flow Logs.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
