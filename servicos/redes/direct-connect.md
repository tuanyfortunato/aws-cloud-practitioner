<!-- autoral -->

# AWS Direct Connect

> **Categoria:** Rede e conectividade híbrida · **Domínio:** 3 · **Abrangência:** Local do Direct Connect ligado a Regiões · **Ficha:** núcleo
>
> **Em uma frase:** conexão de rede dedicada e privada entre o datacenter e a AWS, por fibra, sem passar pelos provedores de internet.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.10 Redes e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) · base em [3.1 Formas de acessar e implantar na AWS](../../docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

A rede de escolas passou a enviar todo dia grandes volumes de vídeos e backups para a AWS. Pela VPN, a velocidade varia com a internet, e a equipe não consegue prever quanto tempo cada envio vai levar.

O Direct Connect liga a rede da empresa à AWS por um cabo de fibra até um **local do Direct Connect**, sem passar pelos provedores de internet. O resultado é mais banda e uma experiência de rede mais consistente do que numa VPN pela internet.

O limite: o Direct Connect **não é criptografado por padrão**. Para criptografar, roda-se uma VPN por cima ou usa-se MACsec nas conexões que o suportam. E, diferente de uma VPN, exige uma conexão física até o local do Direct Connect, feita diretamente ou por um parceiro.

## Como funciona

1. Você pede uma **conexão** num local do Direct Connect: dedicada (só sua, pedida à AWS) ou hospedada (provisionada por um parceiro).
2. A rede da empresa chega ao local por fibra, diretamente ou por meio de um parceiro.
3. **Interfaces virtuais** levam o tráfego para as VPCs (privadas) ou para serviços públicos da AWS.
4. Para criptografar, combina-se o Direct Connect com o Site-to-Site VPN ou usa-se MACsec.

## Opções principais

| Opção | O que é | Velocidades |
|---|---|---|
| Conexão dedicada | Porta física exclusiva de um cliente | 1, 10, 100 ou 400 Gbps |
| Conexão hospedada | Provisionada por um parceiro do Direct Connect | De 50 Mbps a 25 Gbps |
| Direct Connect com VPN | Conexão privada com criptografia IPsec | Pista: "dedicado e criptografado" |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Velocidades da conexão dedicada | 1, 10, 100 e 400 Gbps | 06/10/2026 |
| Criptografia por padrão | Não (VPN por cima ou MACsec) | 06/10/2026 |
| Entrada de dados na AWS pelo Direct Connect | Sem cobrança | 06/10/2026 |

## Como é cobrado

São dois elementos: **horas de porta**, que dependem da capacidade e do tipo de conexão (dedicada ou hospedada), e **transferência de dados de saída** da AWS. A entrada de dados na AWS pelo Direct Connect não é cobrada.

## Não confundir com

| Serviço | Diferença para o Direct Connect | Pista no enunciado |
|---|---|---|
| [AWS Site-to-Site VPN](site-to-site-vpn-e-client-vpn.md) | Pela internet, criptografada com IPsec, sem conexão física nova | "Usar a internet que já existe" |
| [AWS Transit Gateway](vpc-peering-transit-gateway-e-endpoints.md) | Hub que recebe o Direct Connect e distribui para muitas VPCs | "Muitas VPCs" |
| [AWS Global Accelerator](global-accelerator.md) | Leva os usuários da internet pela rede da AWS; não liga o datacenter | "Usuários no mundo todo" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
- [Conexões dedicadas e hospedadas](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithConnections.html)
- [Conexões dedicadas](https://docs.aws.amazon.com/directconnect/latest/UserGuide/dedicated_connection.html)
- [Conexões hospedadas](https://docs.aws.amazon.com/directconnect/latest/UserGuide/hosted_connection.html)
- [Criptografia em trânsito](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html)
- [Preços do AWS Direct Connect](https://aws.amazon.com/directconnect/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
