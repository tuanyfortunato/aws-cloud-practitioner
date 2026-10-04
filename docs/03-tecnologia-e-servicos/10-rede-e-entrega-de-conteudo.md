# 3.10 Rede e entrega de conteúdo

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon VPC (Virtual Private Cloud)](../../servicos/redes/vpc.md) · [VPC Peering, Transit Gateway, VPC Endpoints e PrivateLink](../../servicos/redes/vpc-peering-transit-gateway-e-endpoints.md) · [AWS VPN (Site-to-Site VPN e Client VPN)](../../servicos/redes/site-to-site-vpn-e-client-vpn.md) · [AWS Direct Connect](../../servicos/redes/direct-connect.md) · [Amazon Route 53](../../servicos/redes/route-53.md) · [Amazon CloudFront](../../servicos/redes/cloudfront.md) · [AWS Global Accelerator](../../servicos/redes/global-accelerator.md) · [Amazon API Gateway](../../servicos/redes/api-gateway.md)

⬅️ [3.9 Outros serviços de armazenamento](09-outros-armazenamentos.md) · 🏠 [Índice do domínio](README.md) · [3.11 Analytics](11-analytics.md) ➡️

---

## 🧠 Antes de começar

> 💡 **Em palavras simples:** A **VPC** é a sua rede privada na AWS. Este tópico mostra como dividi-la, ligá-la à internet, a outras VPCs e ao datacenter, e como entregar conteúdo rápido no mundo todo (DNS, CDN e aceleração).
>
> 🏠 **Analogia:** a **VPC** é um **condomínio fechado**: as **subnets** são as ruas (públicas dão para a avenida, privadas não); o **Internet Gateway** é o portão principal; o **NAT Gateway** é uma **saída só de ida** para os moradores das ruas privadas; a **VPN** é um túnel pela estrada pública; o **Direct Connect**, uma estrada particular; o **Route 53**, a lista telefônica; o **CloudFront**, lojinhas espalhadas com cópias do conteúdo.

**Ao terminar este tópico, você deve saber:**

- [ ] Diferenciar subnet **pública** de **privada** e explicar **Internet Gateway** × **NAT Gateway**.
- [ ] Diferenciar **VPC Peering** (não transitivo) de **Transit Gateway** (hub central) e saber o que são **VPC endpoints**.
- [ ] Diferenciar **Site-to-Site VPN** (pela internet, rápido) de **Direct Connect** (dedicado, leva semanas).
- [ ] Diferenciar **Route 53** (DNS), **CloudFront** (CDN com cache) e **Global Accelerator** (IPs fixos, sem cache).

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **CIDR** | a faixa de endereços IP da rede. |
| **DNS** | o sistema que traduz nomes (exemplo.com) em endereços IP. |
| **CDN** | rede de entrega de conteúdo com cópias perto dos usuários. |
| **Transitivo** | se A fala com B e B com C, A fala com C — o peering **não** é. |

> 🎯 **Como não errar na prova:** "Subnet privada baixar patches" → **NAT Gateway**. "Dezenas de VPCs" → **Transit Gateway**. "S3 sem internet" → **gateway endpoint**. "Criptografado, pronto hoje" → **VPN**; "dedicado, consistente" → **Direct Connect**. "Cache global" → **CloudFront**; "IPs estáticos, TCP/UDP" → **Global Accelerator**.

## 📖 Conteúdo

**Amazon VPC**

- **VPC:** rede virtual isolada logicamente, dentro de uma **região**, com um bloco de IPs (CIDR) definido por você. Cada região tem uma **VPC padrão** pronta.
- **Subnet:** fatia da VPC dentro de **uma AZ**.
  - **Pública:** tem rota para um Internet Gateway.
  - **Privada:** sem rota direta para a internet (bancos, back-ends).
- **Internet Gateway (IGW):** permite comunicação entre a VPC e a internet (entrada e saída).
- **NAT Gateway:** fica na subnet pública e permite que recursos em **subnets privadas saiam para a internet** (ex.: baixar atualizações) **sem receber conexões de fora**. Gerenciado e pago por hora e por dado.
- **Route tables:** definem para onde vai o tráfego de cada subnet.
- **Security groups e NACLs:** ver [2.8](../02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md).
- **VPC Peering:** liga duas VPCs (mesma conta, outra conta ou outra região) como se fossem uma rede. **Não é transitivo:** se A fala com B e B com C, A não fala com C.
- **AWS Transit Gateway:** **hub central** que conecta muitas VPCs e redes on-premises num modelo hub-and-spoke, simplificando dezenas de peerings.
- **VPC endpoints:** acessar serviços AWS **sem passar pela internet**.
  - **Gateway endpoint:** só para **S3 e DynamoDB**, gratuito.
  - **Interface endpoint (AWS PrivateLink):** cria uma interface de rede privada na sua subnet para a maioria dos serviços; pago.
- **AWS PrivateLink:** também permite expor um serviço seu para outras VPCs ou clientes de forma privada.
- **VPC Flow Logs:** registram o tráfego de rede (ver [2.7](../02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)).

**Conectividade híbrida**

| Serviço | Como funciona | Quando usar |
| --- | --- | --- |
| AWS Site-to-Site VPN | Túnel IPsec **criptografado pela internet** entre o datacenter (Customer Gateway) e a AWS (Virtual Private Gateway ou Transit Gateway) | Rápido de configurar (minutos), barato; aceita a variação da internet; também serve de backup do Direct Connect |
| AWS Client VPN | VPN gerenciada para **usuários remotos** (notebooks) acessarem a VPC | Trabalho remoto |
| AWS Direct Connect | **Conexão física dedicada e privada**, que não passa pela internet, a partir de um local Direct Connect | Banda alta e estável, latência consistente, menor custo de transferência para grandes volumes; leva semanas para instalar; não é criptografado por padrão (pode rodar VPN por cima) |

**DNS, CDN e aceleração**

- **Amazon Route 53:** DNS gerenciado, altamente disponível. Registra domínios, roteia usuários para recursos e faz **health checks**.
  - **Políticas de roteamento:** simple, **weighted** (divide tráfego por percentual, ex.: testes A/B), **latency-based** (região com menor latência), **failover** (ativo-passivo), **geolocation** (por país/continente do usuário), **geoproximity** (por distância, com ajuste), **multivalue answer** e IP-based.
- **Amazon CloudFront:** **CDN** global. Faz **cache** de conteúdo estático e dinâmico nas edge locations, reduzindo latência e carga na origem.
  - Origens: S3, ALB, EC2, API Gateway ou qualquer servidor HTTP.
  - **Origin Access Control (OAC):** deixa o bucket S3 privado, acessível só pelo CloudFront.
  - HTTPS com certificado do ACM; restrição geográfica; inclui **Shield Standard** e integra com **WAF**.
  - Lambda@Edge e CloudFront Functions rodam código nas edge locations.
- **AWS Global Accelerator:** fornece **IPs estáticos anycast** e leva o tráfego pela **rede global da AWS** até o endpoint regional mais saudável e próximo. Melhora performance de aplicações TCP/UDP e faz failover rápido entre regiões. **Não faz cache.**
- **Amazon API Gateway:** Pontos de prova: cria APIs REST, HTTP e WebSocket em qualquer escala; faz controle de tráfego (throttling), autenticação (IAM, Cognito, Lambda authorizer) e cache; integração clássica com Lambda para back-ends serverless; cobrado por chamada.
- **Cai na prova:** "subnet privada precisa baixar patches da internet" = NAT Gateway; "conectar 50 VPCs e o datacenter" = Transit Gateway; "acessar o S3 sem sair para a internet" = gateway endpoint; "link privado com banda dedicada" = Direct Connect; "conexão rápida e criptografada com o datacenter" = Site-to-Site VPN; "site com usuários no mundo todo, conteúdo estático" = CloudFront; "jogo multiplayer UDP com IPs fixos globais" = Global Accelerator; "mandar usuários para a região mais rápida" = Route 53 latency-based.

## ➕ Complemento

- **CloudFront signed URLs e signed cookies:** restringem o acesso a conteúdo privado distribuído pelo CloudFront (ex.: cursos pagos).
- **Route 53 health checks + failover:** se o endpoint principal cair, o DNS passa a responder com o secundário.
- **Bastion host**: instância na subnet pública usada para acessar recursos privados; o Session Manager é a alternativa sem porta aberta.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).

- "O que torna uma subnet pública?" → Ter rota para um Internet Gateway.
- "Instâncias em subnet privada precisam baixar atualizações." → NAT Gateway.
- "Conectar duas VPCs de contas diferentes." → VPC Peering.
- "Conectar dezenas de VPCs e o datacenter num hub." → Transit Gateway.
- "Acessar o S3 a partir da VPC sem passar pela internet." → Gateway VPC endpoint.
- "Conexão privada e dedicada, sem internet, com desempenho consistente." → Direct Connect.
- "Conexão criptografada com o datacenter, pronta hoje." → Site-to-Site VPN.
- "Funcionários em casa precisam acessar a VPC." → Client VPN.
- "Registrar domínio e gerenciar DNS." → Route 53.
- "Mandar 10% dos usuários para a nova versão." → Route 53 weighted routing.
- "Reduzir latência de conteúdo para usuários globais." → CloudFront.
- "IPs estáticos globais e failover rápido entre regiões para TCP/UDP." → Global Accelerator.
- "Criar e proteger uma API REST para funções Lambda." → API Gateway.

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- **Direct Connect (📌):**
  - **Dedicated:** portas de **1, 10, 100 e 400 Gbps**. **Hosted** (via parceiro): **50 Mbps a 25 Gbps**.
  - ⚠️ **Não é criptografado por padrão.** **MACsec** existe em conexões dedicadas de 10/100/400 Gbps em locais selecionados; fora isso, use **VPN IPsec sobre o Direct Connect**.
  - "Privada, banda consistente, sem internet" → Direct Connect · "criptografada e rápida de configurar" → Site-to-Site VPN · "funcionários remotos" → **Client VPN**.
- **Route 53 — SLA de 100% (📌):** crédito para qualquer disponibilidade mensal < 100% do DNS autoritativo (API e console fora do SLA). "Único serviço com SLA de 100%" → Route 53.
  - Failover usa health checks · Geolocation = país/regulação · Latency = menor latência · Weighted = A/B e migração gradual.
- **CloudFront × Global Accelerator (📌):** CloudFront = **cache** HTTP/HTTPS nas edge locations. Global Accelerator = **sem cache**, **2 IPs anycast estáticos**, TCP/UDP pela rede global da AWS até o endpoint mais saudável (jogos, VoIP, failover regional rápido).
- 🧊 Não decorar: número de VIFs (51), regras de LAG, preços por GB, quotas de VPC/subnet.
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.9 Outros serviços de armazenamento](09-outros-armazenamentos.md) · 🏠 [Índice do domínio](README.md) · [3.11 Analytics](11-analytics.md) ➡️
