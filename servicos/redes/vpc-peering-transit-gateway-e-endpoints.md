# VPC Peering, Transit Gateway, VPC Endpoints e PrivateLink

> **Categoria:** Rede · **Domínio:** 3 · **Escopo:** Regional (peering e TGW podem ligar regiões) · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)
>
> **Em uma frase:** formas de conectar VPCs entre si e de acessar serviços sem passar pela internet.

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

## 🔗 Documentação oficial

- [VPC Peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) · [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) · [PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)
