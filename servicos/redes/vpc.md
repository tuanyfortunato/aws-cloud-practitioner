<!-- autoral -->

# Amazon VPC (Virtual Private Cloud)

> **Categoria:** Rede · **Domínio:** 2 (segurança de rede) e 3 · **Abrangência:** Regional (cada sub-rede numa zona de disponibilidade) · **Ficha:** núcleo
>
> **Em uma frase:** rede virtual isolada logicamente, definida por você, onde ficam os recursos da AWS numa Região.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.10 Redes e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) · base em [0.2 Rede: endereço IP, porta, DNS e HTTPS](../../docs/fundamentos/02-rede.md) e [2.8 Proteção de rede e aplicações](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

O sistema de matrícula tem um site que precisa ser acessível pela internet e um banco de dados que não pode ser. As instâncias da aplicação precisam baixar atualizações sem ficar expostas.

A VPC é a rede da escola dentro da AWS: uma rede virtual **isolada logicamente**, parecida com a de um datacenter próprio, numa Região e abrangendo várias zonas de disponibilidade. Dentro dela, **sub-redes** separam o que fala com a internet (públicas) do que fica protegido (privadas), e **tabelas de rotas** e **gateways** decidem por onde o tráfego sai.

O limite: a VPC organiza e isola a rede, mas não protege sozinha. Os filtros (security groups e ACLs de rede) precisam ser configurados, e ligar a VPC a outras redes exige peças próprias: [peering, Transit Gateway e endpoints](vpc-peering-transit-gateway-e-endpoints.md), [VPN](site-to-site-vpn-e-client-vpn.md) ou [Direct Connect](direct-connect.md).

## Como funciona

1. Você cria a VPC numa Região, com uma faixa de endereços IP; toda conta já tem uma **VPC padrão** em cada Região.
2. Cria sub-redes, cada uma numa única zona de disponibilidade, e espalha os recursos entre zonas.
3. A tabela de rotas define o tipo: a sub-rede **pública** tem rota para o **internet gateway**; a **privada** não tem.
4. Instâncias privadas saem para a internet pelo **NAT gateway**, sem que alguém de fora inicie conexão com elas.
5. **Security groups** filtram cada recurso, e **ACLs de rede** filtram cada sub-rede.

## Opções principais

| Peça | O que faz | Pista no enunciado |
|---|---|---|
| Sub-rede pública | Rota direta para o internet gateway | "Balanceador acessível pela internet" |
| Sub-rede privada | Sem rota de entrada a partir da internet | "Banco que ninguém de fora alcança" |
| Internet gateway | Liga a VPC à internet; redundante e gerenciado pela AWS | "Acesso à internet" |
| NAT gateway | Deixa recursos privados iniciarem conexões para fora | "Instância privada precisa baixar atualizações" |
| Security group | Firewall do recurso: só regras de permitir, resposta volta sozinha (stateful) | "Liberar a porta 443 para a instância" |
| ACL de rede | Filtro da sub-rede: permitir e negar, em ordem, resposta precisa de regra (stateless) | "Bloquear um endereço IP", "regra de negar" |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Zonas por sub-rede | Uma | 06/10/2026 |
| Endereços reservados pela AWS em cada sub-rede | 5 (os quatro primeiros e o último) | 06/10/2026 |
| Tamanho de uma sub-rede IPv4 | De /28 a /16 | 06/10/2026 |
| VPCs por Região (cota padrão, ajustável) | 5 | 06/10/2026 |

## Como é cobrado

A VPC não tem cobrança adicional. Alguns componentes são cobrados, como o NAT gateway (por hora disponível e por GB processado) e os endereços IPv4 públicos; os endereços IPv4 privados não são cobrados.

## Não confundir com

| Serviço | Diferença para a VPC | Pista no enunciado |
|---|---|---|
| [VPC peering, Transit Gateway e endpoints](vpc-peering-transit-gateway-e-endpoints.md) | Ligam VPCs entre si e aos serviços da AWS | "Conectar várias VPCs" |
| [AWS Site-to-Site VPN](site-to-site-vpn-e-client-vpn.md) | Liga a rede local à VPC pela internet, criptografado | "Datacenter até a VPC" |
| [AWS WAF](../seguranca/waf.md) | Filtra pedidos web (camada de aplicação), não pacotes da sub-rede | "Injeção de SQL", "XSS" |
| [Amazon Inspector](../seguranca/inspector.md) | Encontra exposição de rede não intencional e vulnerabilidades | "Porta aberta sem necessidade" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é a Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [Sub-redes](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)
- [Tamanho das sub-redes](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-sizing.html)
- [Cotas da Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html)
- [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)
- [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)
- [Preços da Amazon VPC](https://aws.amazon.com/vpc/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
