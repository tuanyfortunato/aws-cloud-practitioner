# AWS Direct Connect

> **Categoria:** Rede / conectividade híbrida · **Domínio:** 3 · **Escopo:** Local Direct Connect ↔ regiões · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)
>
> **Em uma frase:** conexão de rede **física, dedicada e privada** entre seu datacenter e a AWS, sem passar pela internet.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Para que serve

- Banda alta e **desempenho consistente** (latência previsível).
- **Reduzir custo de transferência** de grandes volumes (tarifa de saída menor que a da internet).
- Requisitos de conectividade privada (sem internet pública).

## Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Local Direct Connect** | Datacenter de colocation onde você (ou o parceiro) se conecta à AWS. |
| **Dedicated connection** | Porta física de **1, 10, 100 ou 400 Gbps** só sua. |
| **Hosted connection** | Via **parceiro**, de **50 Mbps a 25 Gbps**. |
| **Virtual interfaces (VIF)** | **Private VIF** (acessa VPC via VGW/DX Gateway), **Public VIF** (serviços públicos da AWS, ex.: S3) e **Transit VIF** (Transit Gateway). |
| **Direct Connect Gateway** | Uma conexão alcança VPCs de várias regiões/contas. |
| **LAG** | Agrega várias conexões como uma. |
| **SiteLink** | Liga seus sites entre si pela rede da AWS. |
| **Resiliência** | Recomendação: conexões em **dois locais** DX; VPN como backup. |
| **Criptografia** | ⚠️ **Não é criptografado por padrão.** **MACsec** em portas dedicadas de 10/100/400 Gbps (locais selecionados) ou **VPN IPsec sobre o DX**. |
| **Prazo** | **Semanas** (provisionamento físico). |

## Cobrança

- Por **porta-hora** + **transferência de dados de saída** (mais barata que pela internet). Entrada grátis.

## ⚠️ Pegadinhas e não confundir

- Direct Connect × VPN: dedicado/estável/semanas × internet/criptografado/minutos.
- "Precisa de conexão já" → VPN (pode usar enquanto o DX é instalado).

## ❓ Perguntas típicas

- "Conexão privada, dedicada, sem internet, desempenho consistente." → Direct Connect.
- "O Direct Connect é criptografado por padrão?" → Não (use MACsec ou VPN sobre DX).
- "Reduzir custo de transferir grandes volumes todo mês para a AWS." → Direct Connect.

## 🔗 Documentação oficial

- [Guia do Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
