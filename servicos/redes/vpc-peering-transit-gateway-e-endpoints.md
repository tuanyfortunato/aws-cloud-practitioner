# VPC Peering, Transit Gateway, VPC Endpoints e PrivateLink

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Duas redes privadas precisam conversar, ou uma aplicação precisa acessar um serviço AWS por conectividade privada. São necessidades diferentes.

**Como este serviço ajuda?** Peering conecta VPCs; Transit Gateway centraliza conexões entre redes; endpoints fornecem acesso a serviços compatíveis por caminhos privados. Esta ficha compara essas funções.

**Exemplo do dia a dia:** Duas VPCs podem usar peering. Uma empresa com muitas redes pode avaliar Transit Gateway. Uma aplicação pode usar um endpoint compatível para acessar um serviço AWS.

**O que ele não resolve sozinho?** Criar uma conexão não concede todas as permissões nem configura todas as rotas. Endpoints não equivalem a uma conexão geral entre todas as redes.

**Primeiras palavras para entender:**

- **Peering:** ligação entre duas VPCs.
- **Hub:** ponto central de conexões.
- **Endpoint:** ponto de acesso a um serviço.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Rede · **Domínio:** 3 · **Escopo:** Regional (peering e TGW podem ligar regiões) · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)
>
> **Em uma frase:** formas de conectar VPCs entre si e de acessar serviços sem passar pela internet.
>
> **Escopo oficial:** ✅ No escopo (Transit Gateway e PrivateLink listados) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Descreva quem precisa comunicar-se com quem: duas redes, muitas redes ou um serviço específico.

**Passo 2.** Escolha a conexão pertinente e configure suas associações, rotas e controles.

**Passo 3.** Teste o caminho autorizado. Não suponha trânsito entre redes ou permissão a dados apenas porque existe uma conexão.

## 2. Recursos e opções, com significado

### VPC Peering

**Antes de ler este trecho:**

- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.

Conexão privada **um-para-um** entre duas VPCs (mesma conta, outra conta, outra região).

⚠️ **Não é transitivo:** A↔B e B↔C não permite A↔C.

CIDRs **não podem se sobrepor**. Precisa atualizar route tables e SGs dos dois lados.

**Antes de ler este trecho:**

- **hora:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.

Sem custo por hora; paga transferência de dados.

### AWS Transit Gateway

**Antes de ler este trecho:**

- **Direct Connect:** Direct Connect permite estabelecer essa conectividade por conexões e locais compatíveis, com interfaces e rotas configuradas para o ambiente.
- **Connect:** Amazon Connect oferece uma plataforma de contact center em nuvem com canais e recursos compatíveis.
- **regional:** O recurso ou a operação pertence a uma região. Serviços globais podem administrar objetos regionais; leia o alcance do recurso, não apenas o nome do serviço.
- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.

**Hub regional** que conecta milhares de VPCs, VPNs, Direct Connect e outros TGWs (peering entre regiões) — modelo *hub-and-spoke*.

**Antes de ler este trecho:**

- **TGW:** Transit Gateway: ponto central para ligações entre redes compatíveis. Rotas e associações determinam a comunicação; criar o ponto não libera tudo automaticamente.

Route tables do TGW permitem segmentar (ex.: prod não fala com dev).

**Antes de ler este trecho:**

- **RAM:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.

Compartilhável entre contas via **RAM**.

**Antes de ler este trecho:**

- **GB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.

Pago por anexo-hora + GB processado.

### VPC Endpoints

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **IP:** Endereços usados para identificar interfaces e destinos na rede. IPv4 e IPv6 são versões diferentes; ter um endereço não concede permissão nem garante uma rota.
- **DNS:** Sistema que relaciona nomes a informações de endereço e outros registros. Resolver o nome de um site não hospeda o site nem garante que ele está funcionando.
- **subnet:** Segmento de uma rede virtual. Na VPC, uma subnet pertence a uma zona de disponibilidade; suas rotas e controles ajudam a definir a conectividade.
- **route table:** Conjunto de regras que indica para onde encaminhar tráfego destinado a determinadas faixas. A rota é parte do caminho, não uma autorização de identidade.
- **endpoint:** Ponto de acesso a um serviço ou componente. Pode ser um endereço de API ou um recurso de conectividade; identifique qual sentido a seção usa.
- **load balancer:** Recurso que distribui tráfego entre destinos configurados. Ele não cria sozinho todas as máquinas necessárias nem conserta seu programa.
- **GWLB:** Modalidades de balanceador com focos diferentes: aplicação, transporte de rede e integração de equipamentos virtuais. Os protocolos e casos de uso determinam a escolha.
- **ENI:** Interface de rede virtual. Ela associa endereços e configurações de comunicação a recursos compatíveis.
- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.

| Tipo | Serviços | Como funciona | Custo |
|---|---|---|---|
| **Gateway endpoint** | **Só S3 e DynamoDB** | Entrada na route table | **Gratuito** |
| **Interface endpoint** (PrivateLink) | Maioria dos serviços AWS e serviços de parceiros | ENI com IP privado na sua subnet + DNS privado | Por hora + GB |
| **Gateway Load Balancer endpoint** | Appliances de segurança | Encaminha tráfego para o GWLB | Por hora + GB |

Endpoint policies restringem o que pode ser acessado pelo endpoint.

### AWS PrivateLink

**Antes de ler este trecho:**

- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.

Tecnologia dos interface endpoints. Também permite **expor um serviço seu** (atrás de um NLB) para outras VPCs/contas/clientes de forma privada, sem peering e sem expor a VPC inteira.

### Comparação rápida

**Antes de ler este trecho:**

- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.

| Necessidade | Solução |
|---|---|
| Ligar 2 VPCs | VPC Peering |
| Ligar dezenas de VPCs + on-premises | Transit Gateway |
| Acessar S3/DynamoDB sem internet | Gateway endpoint (grátis) |
| Acessar outros serviços AWS sem internet | Interface endpoint |
| Oferecer seu serviço privadamente a outras contas | PrivateLink (endpoint service) |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Criar uma conexão não concede todas as permissões nem configura todas as rotas. Endpoints não equivalem a uma conexão geral entre todas as redes.

## 4. Caso resolvido: ligando as peças

Duas VPCs podem usar peering. Uma empresa com muitas redes pode avaliar Transit Gateway. Uma aplicação pode usar um endpoint compatível para acessar um serviço AWS.

**Aplicando a sequência à situação:**

**Etapa 1:** Descreva quem precisa comunicar-se com quem: duas redes, muitas redes ou um serviço específico.
**Etapa 2:** Escolha a conexão pertinente e configure suas associações, rotas e controles.
**Etapa 3:** Teste o caminho autorizado. Não suponha trânsito entre redes ou permissão a dados apenas porque existe uma conexão.

**Resultado e responsabilidade:** Peering conecta VPCs; Transit Gateway centraliza conexões entre redes; endpoints fornecem acesso a serviços compatíveis por caminhos privados. Esta ficha compara essas funções.

**Recursos envolvidos:** Peering entre VPCs; hub Transit Gateway; endpoints e PrivateLink.

**Decisões que precisam ser tomadas:** Redes envolvidas, rotas, serviço exposto e permissões.

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **consumidor:** Programa que recebe e processa dados ou tarefas. Ele precisa realizar o trabalho e tratar falhas, não apenas receber a mensagem.

**Outra situação comentada:** Três redes precisam comunicação por hub: TGW; consumidor só precisa de serviço privado: PrivateLink.

**Por que não concluir mais do que isso:** Peering não é transitivo; endpoint não substitui IAM

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Conectar duas VPCs de contas diferentes."

**Resposta curta:** VPC Peering.

**Pergunta:** "A falou com B e B com C; A fala com C via peering?"

**Resposta curta:** Não, peering não é transitivo.

**Pergunta:** "Conectar 50 VPCs e o datacenter num hub."

**Resposta curta:** Transit Gateway.

**Pergunta:** "Acessar o S3 a partir da VPC sem passar pela internet."

**Resposta curta:** Gateway VPC endpoint.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [VPC Peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) · [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) · [PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
