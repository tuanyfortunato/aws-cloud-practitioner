<!-- autoral -->

# AWS VPN (Site-to-Site VPN e Client VPN)

> **Categoria:** Rede e conectividade híbrida · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** túneis criptografados pela internet que ligam uma rede local (Site-to-Site) ou cada usuário (Client VPN) à AWS.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.10 Redes e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) · base em [3.1 Formas de acessar e implantar na AWS](../../docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

A secretaria quer acessar a VPC da escola a partir da rede local, de forma privada e criptografada, usando a internet que já tem. E os professores querem entrar na rede de casa.

O **Site-to-Site VPN** cria uma conexão criptografada (IPsec) pela internet entre a rede local e a AWS. O **Client VPN** é a VPN para pessoas: cada usuário conecta o computador de onde estiver, com um cliente baseado em OpenVPN e conexão TLS criptografada.

O limite: o caminho é a internet, então banda e latência variam. Para volumes grandes e desempenho previsível, a resposta é o [Direct Connect](direct-connect.md), que pode ser combinado com a VPN para ter uma conexão privada e criptografada.

## Como funciona

1. **Site-to-Site:** do lado da AWS fica um **virtual private gateway** (ou um Transit Gateway); do lado da escola, um **customer gateway**, o equipamento de rede local.
2. Cada conexão tem **dois túneis**, cada um terminando numa zona de disponibilidade diferente; se um cai, o tráfego passa pelo outro.
3. **Client VPN:** você cria um endpoint e associa sub-redes da VPC a ele.
4. Cada usuário baixa um cliente OpenVPN e o arquivo de configuração e se conecta de qualquer lugar.

## Opções principais

| Opção | Quem se conecta | Pista no enunciado |
|---|---|---|
| Site-to-Site VPN | A rede inteira de um escritório ou datacenter | "Ligar a rede local à VPC pela internet" |
| Client VPN | Cada pessoa, do próprio computador | "Funcionários em casa", "acesso remoto" |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Túneis por conexão Site-to-Site | 2, em zonas diferentes | 06/10/2026 |
| Criptografia | IPsec (Site-to-Site); TLS (Client VPN) | 06/10/2026 |

## Como é cobrado

O Site-to-Site VPN cobra por hora de conexão provisionada, mais a transferência de dados de saída. O Client VPN cobra por hora de cada sub-rede associada ao endpoint e por hora de cada conexão de usuário ativa.

## Não confundir com

| Serviço | Diferença para a VPN | Pista no enunciado |
|---|---|---|
| [AWS Direct Connect](direct-connect.md) | Conexão dedicada, sem passar pelos provedores de internet; sem criptografia por padrão | "Banda alta e consistente", "conexão dedicada" |
| [AWS Transit Gateway](vpc-peering-transit-gateway-e-endpoints.md) | Hub onde várias VPNs e VPCs se encontram | "Muitas VPCs e escritórios" |
| [Amazon VPC](vpc.md) | A rede onde a VPN chega | "Rede isolada" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
- [Túneis do Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNTunnels.html)
- [O que é o AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)
- [Preços do AWS VPN](https://aws.amazon.com/vpn/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
