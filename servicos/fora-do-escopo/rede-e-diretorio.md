# Rede e diretório (Cloud Map, VPC Lattice, Network Access Analyzer, Cloud Directory)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Aplicações podem precisar localizar outros serviços ou controlar a comunicação entre eles, além de apenas ter uma rede virtual criada.

**Como este serviço ajuda?** A ficha distingue descoberta de serviços, comunicação de aplicações, análise de caminhos e diretórios especializados. Cada ferramenta trata uma dessas necessidades.

**Exemplo do dia a dia:** Se uma parte da aplicação precisa descobrir onde está outra, descoberta de serviços é uma função pertinente. Isso é diferente de cadastrar funcionários para login.

**O que ele não resolve sozinho?** Esses produtos não substituem uns aos outros nem tornam toda rede acessível automaticamente. O conteúdo é de referência fora do escopo indicado.

**Primeiras palavras para entender:**

- **Descoberta de serviços:** localizar recursos de uma aplicação.
- **Diretório:** organização de entidades e relações.
- **Caminho de rede:** percurso de uma comunicação.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Redes e diretório · **Domínio:** — (fora da prova) · **Escopo:** Regional · **Lista oficial:** [fora do escopo](../../docs/00-guia-do-exame/escopo-oficial.md#-fora-do-escopo-lista-oficial-não-exaustiva)
>
> **Em uma frase:** serviços de rede de aplicação e de diretório que complementam a VPC, mas não caem na prova.
>
> **Escopo oficial:** ❌ Fora do escopo — documentado só para referência · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> ❌ **Fora do escopo da CLF-C02.** Documentados aqui apenas para referência. Na prova, rede = VPC, Route 53,
> CloudFront, Global Accelerator, Direct Connect, VPN, Transit Gateway, PrivateLink e API Gateway. Veja também
> [Network Firewall](../seguranca/firewall-manager-e-network-firewall.md), que também está fora do escopo.

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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Descoberta de serviços, conectividade de aplicações e diretórios especializados |
| **O que você decide/configura?** | Escopo de rede, identidade e serviço |
| **Em que ordem as coisas acontecem?** | Use a ferramenta compatível com a necessidade específica |
| **O que pode fazer, e em que condição?** | Complementam redes e serviços de diretório |
| **O que não pode presumir?** | Fora do escopo; não são substitutos universais de VPC, DNS ou IAM |

**Caso comentado:** DNS Route 53 e identidade IAM são conceitos centrais; ferramentas especializadas pedem contexto próprio.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Cloud Map](https://aws.amazon.com/cloud-map/) · [VPC Lattice](https://aws.amazon.com/vpc/lattice/) · [Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html) · [Cloud Directory](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/what_is_cloud_directory.html)
