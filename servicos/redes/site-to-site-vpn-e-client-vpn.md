# AWS VPN (Site-to-Site VPN e Client VPN)

> **Categoria:** Rede / conectividade híbrida · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)
>
> **Em uma frase:** túneis criptografados (IPsec/TLS) pela internet para ligar redes ou usuários à sua VPC.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é um **túnel secreto pela estrada pública** (a internet): rápido de construir e criptografado, mas o trânsito pode variar.

- ✅ **Escolha quando:** precisa conectar o **escritório** ou os **funcionários remotos** à VPC com criptografia, **rapidamente**.
- 🚫 **Não é a resposta quando:** precisa de banda **dedicada e estável, sem internet** → [Direct Connect](direct-connect.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "criptografado pela internet", "pronto hoje", "IPsec" → Site-to-Site VPN; "funcionários em casa" → Client VPN.
<!-- didatico:fim -->

## AWS Site-to-Site VPN

| Item | Detalhe |
|---|---|
| **Objetivo** | Ligar o **datacenter/escritório** à VPC por **IPsec pela internet**. |
| **Componentes** | **Customer Gateway** (seu roteador/firewall) ↔ **Virtual Private Gateway** (na VPC) ou **Transit Gateway**. |
| **Redundância** | ✔️ Cada conexão tem **2 túneis**, cada um com IP público próprio, terminando em AZs distintas; configure os dois. |
| **Roteamento** | Estático ou dinâmico (**BGP**). |
| **Accelerated VPN** | Usa a rede do Global Accelerator para melhor desempenho. |
| **VPN CloudHub** | Vários escritórios se comunicam via o mesmo VGW (hub-and-spoke). |
| **VPN sobre Direct Connect** | Criptografia ponta a ponta no link dedicado. |
| **Prazo** | **Minutos** para configurar. |
| **Limite** | 🧊 Throughput por túnel limitado (≈1,25 Gbps); depende da qualidade da internet. |

## AWS Client VPN

- VPN gerenciada (baseada em OpenVPN) para **usuários remotos** (notebooks) acessarem VPCs e redes on-premises.
- Autenticação por certificados, Active Directory ou SAML; escala automaticamente.
- Pago por associação de subnet-hora + conexão-hora.

## Comparação

| | Site-to-Site VPN | Client VPN | Direct Connect |
|---|---|---|---|
| Quem conecta | Rede inteira | Usuários individuais | Rede inteira |
| Meio | Internet (IPsec) | Internet (TLS) | Link físico dedicado |
| Criptografado | ✅ | ✅ | ❌ por padrão |
| Tempo de setup | Minutos | Minutos | Semanas |
| Desempenho | Variável | Variável | Consistente |

## ❓ Perguntas típicas

- "Conexão criptografada com o datacenter, pronta hoje." → Site-to-Site VPN.
- "Funcionários em casa precisam acessar a VPC." → Client VPN.
- "Backup barato do Direct Connect." → Site-to-Site VPN.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Túneis Site-to-Site entre redes; endpoint Client VPN para usuários |
| **O que você decide/configura?** | Endereços, autenticação, rotas e regras de autorização |
| **Em que ordem as coisas acontecem?** | Estabeleça túnel/conexão e permita destinos específicos |
| **O que pode fazer, e em que condição?** | Fornece conectividade criptografada nas modalidades apropriadas |
| **O que não pode presumir?** | Não torna toda rede acessível sem rotas e autorização; Site-to-Site não é cliente remoto individual |

**Caso comentado:** Filial inteira: Site-to-Site VPN; funcionário remoto individual: Client VPN.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) · [Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)
