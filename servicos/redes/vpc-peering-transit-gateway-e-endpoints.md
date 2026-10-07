<!-- autoral -->

# VPC Peering, Transit Gateway, VPC Endpoints e PrivateLink

> **Categoria:** Rede · **Domínio:** 3 · **Abrangência:** Regional (peering e Transit Gateway também ligam Regiões) · **Ficha:** núcleo
>
> **Em uma frase:** formas de ligar VPCs entre si e de acessar serviços de forma privada, sem passar pela internet.
>
> **Escopo oficial:** ✅ No escopo (Transit Gateway e PrivateLink listados) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.10 Redes e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

A rede de escolas passou a ter várias VPCs: uma para a matrícula, outra para o portal, outra para a contabilidade. Agora elas precisam conversar, e as instâncias privadas precisam gravar no S3 sem sair pela internet.

Três peças resolvem isso. O **VPC peering** liga duas VPCs, que passam a conversar por endereços privados. O **Transit Gateway** é um ponto central (hub) que interliga muitas VPCs e as redes locais. O **PrivateLink** e os **VPC endpoints** conectam a VPC, de forma privada, a serviços como se estivessem dentro dela.

O limite: o peering **não é transitivo** e vira um emaranhado com muitas VPCs; aí entra o Transit Gateway. E nenhuma dessas peças liga o datacenter da empresa sozinha: para isso há a [VPN](site-to-site-vpn-e-client-vpn.md) e o [Direct Connect](direct-connect.md), que podem se ligar ao Transit Gateway.

## Como funciona

1. **Peering:** uma VPC pede a conexão, a outra aceita, e as tabelas de rotas das duas apontam uma para a outra. Funciona entre contas e entre Regiões.
2. **Transit Gateway:** cada VPC, VPN ou Direct Connect se liga uma vez ao hub, que roteia entre todos.
3. **Endpoint de interface (PrivateLink):** cria uma interface de rede na sua sub-rede para falar com o serviço, sem internet gateway, NAT ou endereço público.
4. **Gateway endpoint:** uma rota na tabela leva o tráfego para o S3 ou o DynamoDB sem sair da rede da AWS.

## Opções principais

| Peça | O que faz | Pista no enunciado |
|---|---|---|
| VPC peering | Liga duas VPCs um a um; não é transitivo | "Duas VPCs precisam conversar" |
| AWS Transit Gateway | Hub que interliga muitas VPCs e redes locais | "Dezenas de VPCs", "simplificar a topologia" |
| Endpoint de interface (PrivateLink) | Acesso privado a serviços da AWS, de parceiros ou próprios | "Sem passar pela internet", "oferecer um serviço a outras contas" |
| Gateway endpoint | Acesso privado ao S3 e ao DynamoDB, sem cobrança adicional | "Instância privada gravando no S3" |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Serviços com gateway endpoint | 2 (S3 e DynamoDB) | 06/10/2026 |
| Taxa para criar um peering | Nenhuma (paga-se a transferência) | 06/10/2026 |

## Como é cobrado

Criar um peering não tem custo; a transferência de dados pelo peering é cobrada, inclusive entre zonas da mesma Região. O Transit Gateway cobra por hora de cada anexo (VPC, VPN, Direct Connect) e por GB processado. O endpoint de interface cobra por hora em cada zona e por GB processado. O gateway endpoint não tem cobrança adicional.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [Amazon VPC](vpc.md) | A rede em si, com sub-redes e gateways | "Rede isolada na Região" |
| [AWS Site-to-Site VPN](site-to-site-vpn-e-client-vpn.md) | Liga a rede local à AWS pela internet | "Datacenter", "IPsec" |
| [AWS Direct Connect](direct-connect.md) | Liga a rede local à AWS por conexão dedicada | "Sem passar pela internet pública" |
| NAT gateway ([VPC](vpc.md)) | Saída para a internet, não acesso privado aos serviços | "Baixar atualizações da internet" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [Conceitos do VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html)
- [Perguntas frequentes da Amazon VPC](https://aws.amazon.com/vpc/faqs/)
- [O que é um transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)
- [O que é o AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)
- [Gateway endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html)
- [Preços do AWS Transit Gateway](https://aws.amazon.com/transit-gateway/pricing/)
- [Preços do AWS PrivateLink](https://aws.amazon.com/privatelink/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
