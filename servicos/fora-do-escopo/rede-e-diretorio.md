# Rede e diretório (Cloud Map, VPC Lattice, Network Access Analyzer, Cloud Directory)

> **Categoria:** Redes e diretório · **Domínio:** — (fora da prova) · **Escopo:** Regional · **Lista oficial:** [fora do escopo](../../docs/00-guia-do-exame/escopo-oficial.md#-fora-do-escopo-lista-oficial-não-exaustiva)
>
> **Em uma frase:** serviços de rede de aplicação e de diretório que complementam a VPC, mas não caem na prova.
>
> **Escopo oficial:** ❌ Fora do escopo — documentado só para referência · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> ❌ **Fora do escopo da CLF-C02.** Documentados aqui apenas para referência. Na prova, rede = VPC, Route 53,
> CloudFront, Global Accelerator, Direct Connect, VPN, Transit Gateway, PrivateLink e API Gateway. Veja também
> [Network Firewall](../seguranca/firewall-manager-e-network-firewall.md), que também está fora do escopo.

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** são **complementos de rede e de diretório** que ficam fora da prova.

- ✅ **Escolha quando:** Só para referência — **não cai na prova**. Se aparecer como alternativa, provavelmente é distrator.
- 🚫 **Não é a resposta quando:** na prova, **rede** → [VPC](../redes/vpc.md) e [Transit Gateway e PrivateLink](../redes/vpc-peering-transit-gateway-e-endpoints.md); **Active Directory** → [Directory Service](../seguranca/directory-service.md).
- 🎯 **Palavras do enunciado que apontam para ele:** Cloud Map, VPC Lattice, Network Access Analyzer e Cloud Directory aparecem, no máximo, como alternativas erradas.
<!-- didatico:fim -->

## AWS Cloud Map

- **Descoberta de serviços**: registra os recursos de uma aplicação (microsserviços, bancos, filas) com nomes amigáveis e o local atual, para que os serviços encontrem uns aos outros por API ou DNS. Usado pelo ECS Service Connect.

## Amazon VPC Lattice

- **Rede de aplicação** gerenciada: conecta, protege (políticas de autenticação com IAM) e monitora a comunicação entre serviços em várias VPCs e contas, sem gerenciar peering, rotas ou load balancers.

## Network Access Analyzer

- Recurso da VPC que **identifica caminhos de rede não intencionais** até seus recursos (ex.: "algum banco de dados é acessível pela internet?"), comparando com requisitos que você define.

## Amazon Cloud Directory

- Banco de **diretórios hierárquicos** flexíveis (organogramas, catálogos, registros de dispositivos), com várias hierarquias sobre os mesmos dados.
- 🔄 Fechado a novos clientes desde 07/11/2025.

## ⚠️ Como isso aparece na prova

- "Ligar dezenas de VPCs" → **Transit Gateway** (no escopo). "Expor um serviço de forma privada" → **PrivateLink** (no escopo).
- "Active Directory gerenciado" → **Directory Service** (no escopo), não Cloud Directory.
- "Analisar tráfego de rede" → **VPC Flow Logs**.

## 🔗 Documentação oficial

- [Cloud Map](https://aws.amazon.com/cloud-map/) · [VPC Lattice](https://aws.amazon.com/vpc/lattice/) · [Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html) · [Cloud Directory](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/what_is_cloud_directory.html)
