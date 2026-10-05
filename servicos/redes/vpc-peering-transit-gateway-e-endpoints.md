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

## VPC Peering

- Conexão privada **um-para-um** entre duas VPCs (mesma conta, outra conta, outra região).
- ⚠️ **Não é transitivo:** A↔B e B↔C não permite A↔C.
- CIDRs **não podem se sobrepor**. Precisa atualizar route tables e SGs dos dois lados.
- Sem custo por hora; paga transferência de dados.

## AWS Transit Gateway

- **Hub regional** que conecta milhares de VPCs, VPNs, Direct Connect e outros TGWs (peering entre regiões) — modelo *hub-and-spoke*.
- Route tables do TGW permitem segmentar (ex.: prod não fala com dev).
- Compartilhável entre contas via **RAM**.
- Pago por anexo-hora + GB processado.

## VPC Endpoints

| Tipo | Serviços | Como funciona | Custo |
|---|---|---|---|
| **Gateway endpoint** | **Só S3 e DynamoDB** | Entrada na route table | **Gratuito** |
| **Interface endpoint** (PrivateLink) | Maioria dos serviços AWS e serviços de parceiros | ENI com IP privado na sua subnet + DNS privado | Por hora + GB |
| **Gateway Load Balancer endpoint** | Appliances de segurança | Encaminha tráfego para o GWLB | Por hora + GB |

- Endpoint policies restringem o que pode ser acessado pelo endpoint.

## AWS PrivateLink

- Tecnologia dos interface endpoints. Também permite **expor um serviço seu** (atrás de um NLB) para outras VPCs/contas/clientes de forma privada, sem peering e sem expor a VPC inteira.

## Comparação rápida

| Necessidade | Solução |
|---|---|
| Ligar 2 VPCs | VPC Peering |
| Ligar dezenas de VPCs + on-premises | Transit Gateway |
| Acessar S3/DynamoDB sem internet | Gateway endpoint (grátis) |
| Acessar outros serviços AWS sem internet | Interface endpoint |
| Oferecer seu serviço privadamente a outras contas | PrivateLink (endpoint service) |

## ❓ Perguntas típicas

- "Conectar duas VPCs de contas diferentes." → VPC Peering.
- "A falou com B e B com C; A fala com C via peering?" → Não, peering não é transitivo.
- "Conectar 50 VPCs e o datacenter num hub." → Transit Gateway.
- "Acessar o S3 a partir da VPC sem passar pela internet." → Gateway VPC endpoint.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Peering entre VPCs; hub Transit Gateway; endpoints e PrivateLink |
| **O que você decide/configura?** | Redes envolvidas, rotas, serviço exposto e permissões |
| **Em que ordem as coisas acontecem?** | Escolha conexão de redes ou acesso privado a serviço e configure ambos os lados |
| **O que pode fazer, e em que condição?** | TGW atende topologia hub; PrivateLink expõe serviços compatíveis sem abrir conectividade inteira |
| **O que não pode presumir?** | Peering não é transitivo; endpoint não substitui IAM |

**Caso comentado:** Três redes precisam comunicação por hub: TGW; consumidor só precisa de serviço privado: PrivateLink.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [VPC Peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) · [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) · [PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)
