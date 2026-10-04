# AWS VPN (Site-to-Site VPN e Client VPN)

> **Categoria:** Rede / conectividade híbrida · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)
>
> **Em uma frase:** túneis criptografados (IPsec/TLS) pela internet para ligar redes ou usuários à sua VPC.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## AWS Site-to-Site VPN

| Item | Detalhe |
|---|---|
| **Objetivo** | Ligar o **datacenter/escritório** à VPC por **IPsec pela internet**. |
| **Componentes** | **Customer Gateway** (seu roteador/firewall) ↔ **Virtual Private Gateway** (na VPC) ou **Transit Gateway**. |
| **Redundância** | Cada conexão tem **2 túneis** em endpoints diferentes. |
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

## 🔗 Documentação oficial

- [Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) · [Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)
