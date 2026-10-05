# AWS Direct Connect

> **Categoria:** Rede / conectividade híbrida · **Domínio:** 3 · **Escopo:** Local Direct Connect ↔ regiões · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)
>
> **Em uma frase:** conexão de rede **física, dedicada e privada** entre seu datacenter e a AWS, sem passar pela internet.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é uma **estrada particular** entre o seu datacenter e a AWS: não pega o trânsito da internet, mas leva semanas para ficar pronta.

- ✅ **Escolha quando:** precisa de conexão **privada, dedicada**, com banda alta e **desempenho consistente**.
- 🚫 **Não é a resposta quando:** precisa de conexão **já**, ou **criptografada por padrão** → [Site-to-Site VPN](site-to-site-vpn-e-client-vpn.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "conexão dedicada", "privada", "não passa pela internet", "desempenho consistente", "grandes volumes todo dia".
<!-- didatico:fim -->

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Conexão, interfaces virtuais e gateways associados |
| **O que você decide/configura?** | Localidade, banda, conexão e redundância |
| **Em que ordem as coisas acontecem?** | Conecte o ambiente próprio à AWS por caminho dedicado e configure roteamento |
| **O que pode fazer, e em que condição?** | Ajuda a ter conectividade privada e características previsíveis |
| **O que não pode presumir?** | Criptografia não é automática em toda modalidade; resiliência exige planejamento |

**Caso comentado:** Conexão dedicada de datacenter: Direct Connect; criptografia adicional pode usar VPN conforme requisito.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
