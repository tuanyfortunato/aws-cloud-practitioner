# 3.10 Rede e entrega de conteúdo

## 🧠 Antes de começar

**Qual é a dificuldade?** Usuários precisam chegar ao site, a aplicação precisa chegar ao banco e a empresa pode precisar conectar sua rede à AWS. Cada comunicação tem um caminho e controles.

**A ideia em palavras simples:** Rede define conexões e rotas. VPC organiza recursos em uma rede virtual; DNS relaciona nomes a endereços; distribuição de conteúdo e aceleração atuam na entrega aos usuários.

**Exemplo do dia a dia:** O aluno digita o domínio; DNS indica o destino. O pedido chega ao serviço que atende o site, e a aplicação acessa o banco por um caminho autorizado.

**O que não concluir?** Nenhum serviço desta lista configura toda a comunicação sozinho. Organizar rede, permitir acesso, resolver nomes e distribuir conteúdo são funções distintas.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **CIDR** | a faixa de endereços IP da rede. |
| **DNS** | o sistema que traduz nomes (exemplo.com) em endereços IP. |
| **CDN** | rede de entrega de conteúdo com cópias perto dos usuários. |
| **Transitivo** | se A fala com B e B com C, A fala com C — o peering **não** é. |

---

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)**

> 🔎 **Fichas detalhadas:** [Amazon VPC (Virtual Private Cloud)](../../servicos/redes/vpc.md) · [VPC Peering, Transit Gateway, VPC Endpoints e PrivateLink](../../servicos/redes/vpc-peering-transit-gateway-e-endpoints.md) · [AWS VPN (Site-to-Site VPN e Client VPN)](../../servicos/redes/site-to-site-vpn-e-client-vpn.md) · [AWS Direct Connect](../../servicos/redes/direct-connect.md) · [Amazon Route 53](../../servicos/redes/route-53.md) · [Amazon CloudFront](../../servicos/redes/cloudfront.md) · [AWS Global Accelerator](../../servicos/redes/global-accelerator.md) · [Amazon API Gateway](../../servicos/redes/api-gateway.md)

⬅️ [3.9 Outros serviços de armazenamento](09-outros-armazenamentos.md) · 🏠 [Índice do domínio](README.md) · [3.11 Analytics](11-analytics.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

Para uma conexão funcionar, o nome deve indicar um destino, o caminho deve existir e os controles devem permitir o tráfego. A identidade da aplicação pode ainda precisar de autorização para os dados. É possível cumprir um desses requisitos e falhar em outro.

Separe rede virtual, ligação entre redes, acesso remoto, resolução de nomes e distribuição de conteúdo. Uma CDN mantém e entrega conteúdo conforme regras; aceleração de rede encaminha tráfego; DNS informa destinos. As três funções não são a mesma etapa.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

a **VPC** é um **condomínio fechado**: as **subnets** são as ruas (públicas dão para a avenida, privadas não); o **Internet Gateway** é o portão principal; o **NAT Gateway** é uma **saída só de ida** para os moradores das ruas privadas; a **VPN** é um túnel pela estrada pública; o **Direct Connect**, uma estrada particular; o **Route 53**, a lista telefônica; o **CloudFront**, lojinhas espalhadas com cópias do conteúdo.

</details>

## 2. Conceitos e opções explicados

**Amazon VPC**

**VPC:** rede virtual isolada logicamente, dentro de uma **região**, com um bloco de IPs (CIDR) definido por você. Cada região tem uma **VPC padrão** pronta.

**Subnet:** fatia da VPC dentro de **uma AZ**.

  - **Pública:** tem rota para um Internet Gateway.

  - **Privada:** sem rota direta para a internet (bancos, back-ends).

**Internet Gateway (IGW):** permite comunicação entre a VPC e a internet (entrada e saída).

**NAT Gateway:** fica na subnet pública e permite que recursos em **subnets privadas saiam para a internet** (ex.: baixar atualizações) **sem receber conexões de fora**. Gerenciado e pago por hora e por dado.

**Route tables:** definem para onde vai o tráfego de cada subnet.

**Security groups e NACLs:** ver [2.8](../02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md).

**VPC Peering:** liga duas VPCs (mesma conta, outra conta ou outra região) como se fossem uma rede. **Não é transitivo:** se A fala com B e B com C, A não fala com C.

**AWS Transit Gateway:** **hub central** que conecta muitas VPCs e redes on-premises num modelo hub-and-spoke, simplificando dezenas de peerings.

**VPC endpoints:** acessar serviços AWS **sem passar pela internet**.

  - **Gateway endpoint:** só para **S3 e DynamoDB**, gratuito.

  - **Interface endpoint (AWS PrivateLink):** cria uma interface de rede privada na sua subnet para a maioria dos serviços; pago.

**AWS PrivateLink:** também permite expor um serviço seu para outras VPCs ou clientes de forma privada.

**VPC Flow Logs:** registram o tráfego de rede (ver [2.7](../02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)).

**Conectividade híbrida**

| Serviço | Como funciona | Quando usar |
| --- | --- | --- |
| AWS Site-to-Site VPN | Túnel IPsec **criptografado pela internet** entre o datacenter (Customer Gateway) e a AWS (Virtual Private Gateway ou Transit Gateway) | Rápido de configurar (minutos), barato; aceita a variação da internet; também serve de backup do Direct Connect |
| AWS Client VPN | VPN gerenciada para **usuários remotos** (notebooks) acessarem a VPC | Trabalho remoto |
| AWS Direct Connect | **Conexão física dedicada e privada**, que não passa pela internet, a partir de um local Direct Connect | Banda alta e estável, latência consistente, menor custo de transferência para grandes volumes; leva semanas para instalar; não é criptografado por padrão (pode rodar VPN por cima) |

**DNS, CDN e aceleração**

**Amazon Route 53:** DNS gerenciado, altamente disponível. Registra domínios, roteia usuários para recursos e faz **health checks**.

  - **Políticas de roteamento:** simple, **weighted** (divide tráfego por percentual, ex.: testes A/B), **latency-based** (região com menor latência), **failover** (ativo-passivo), **geolocation** (por país/continente do usuário), **geoproximity** (por distância, com ajuste), **multivalue answer** e IP-based.

**Amazon CloudFront:** **CDN** global. Faz **cache** de conteúdo estático e dinâmico nas edge locations, reduzindo latência e carga na origem.

  - Origens: S3, ALB, EC2, API Gateway ou qualquer servidor HTTP.

  - **Origin Access Control (OAC):** deixa o bucket S3 privado, acessível só pelo CloudFront.

  - HTTPS com certificado do ACM; restrição geográfica; inclui **Shield Standard** e integra com **WAF**.

  - Lambda@Edge e CloudFront Functions rodam código nas edge locations.

**AWS Global Accelerator:** fornece **IPs estáticos anycast** e leva o tráfego pela **rede global da AWS** até o endpoint regional mais saudável e próximo. Melhora performance de aplicações TCP/UDP e faz failover rápido entre regiões. **Não faz cache.**

**Amazon API Gateway:** Pontos de prova: cria APIs REST, HTTP e WebSocket em qualquer escala; faz controle de tráfego (throttling), autenticação (IAM, Cognito, Lambda authorizer) e cache; integração clássica com Lambda para back-ends serverless; cobrado por chamada.

**Cai na prova:** "subnet privada precisa baixar patches da internet" = NAT Gateway; "conectar 50 VPCs e o datacenter" = Transit Gateway; "acessar o S3 sem sair para a internet" = gateway endpoint; "link privado com banda dedicada" = Direct Connect; "conexão rápida e criptografada com o datacenter" = Site-to-Site VPN; "site com usuários no mundo todo, conteúdo estático" = CloudFront; "jogo multiplayer UDP com IPs fixos globais" = Global Accelerator; "mandar usuários para a região mais rápida" = Route 53 latency-based.

### ➕ Complemento

**CloudFront signed URLs e signed cookies:** restringem o acesso a conteúdo privado distribuído pelo CloudFront (ex.: cursos pagos).

**Route 53 health checks + failover:** se o endpoint principal cair, o DNS passa a responder com o secundário.

**Bastion host**: instância na subnet pública usada para acessar recursos privados; o Session Manager é a alternativa sem porta aberta.

## 3. Como analisar uma situação

**Primeiro, identifique o funcionamento:** VPC fornece rede lógica; subnets e tabelas de rota definem caminhos; gateways e endpoints conectam destinos; SG/NACL controlam tráfego. DNS encontra endereços, CDN entrega conteúdo.

**Depois, compare as escolhas:** Route 53 para DNS; CloudFront para cache/distribuição; API Gateway para entrada de API; VPN para túnel; Direct Connect para conexão dedicada; PrivateLink para serviço privado suportado.

**Por fim, verifique o limite:** Subnet pública sozinha não torna EC2 acessível: precisa endereço adequado, rota, controles e aplicação. Direct Connect não cifra tudo por padrão; use criptografia quando requerida.

## 4. Caso resolvido

Uma instância privada precisa iniciar downloads na internet sem aceitar conexões iniciadas de fora. Qual componente típico?

**Raciocínio e resposta:** NAT Gateway para saída IPv4 com rotas adequadas. Internet Gateway sem endereço público e sem configurar o restante não resolve sozinho.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Diferenciar subnet **pública** de **privada** e explicar **Internet Gateway** × **NAT Gateway**.
- [ ] Diferenciar **VPC Peering** (não transitivo) de **Transit Gateway** (hub central) e saber o que são **VPC endpoints**.
- [ ] Diferenciar **Site-to-Site VPN** (pela internet, rápido) de **Direct Connect** (dedicado, leva semanas).
- [ ] Diferenciar **Route 53** (DNS), **CloudFront** (CDN com cache) e **Global Accelerator** (IPs fixos, sem cache).

**Dica de revisão para a prova:** "Subnet privada baixar patches" → **NAT Gateway**. "Dezenas de VPCs" → **Transit Gateway**. "S3 sem internet" → **gateway endpoint**. "Criptografado, pronto hoje" → **VPN**; "dedicado, consistente" → **Direct Connect**. "Cache global" → **CloudFront**; "IPs estáticos, TCP/UDP" → **Global Accelerator**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).
**Pergunta:** "O que torna uma subnet pública?"

**Resposta curta:** Ter rota para um Internet Gateway.

**Pergunta:** "Instâncias em subnet privada precisam baixar atualizações."

**Resposta curta:** NAT Gateway.

**Pergunta:** "Conectar duas VPCs de contas diferentes."

**Resposta curta:** VPC Peering.

**Pergunta:** "Conectar dezenas de VPCs e o datacenter num hub."

**Resposta curta:** Transit Gateway.

**Pergunta:** "Acessar o S3 a partir da VPC sem passar pela internet."

**Resposta curta:** Gateway VPC endpoint.

**Pergunta:** "Conexão privada e dedicada, sem internet, com desempenho consistente."

**Resposta curta:** Direct Connect.

**Pergunta:** "Conexão criptografada com o datacenter, pronta hoje."

**Resposta curta:** Site-to-Site VPN.

**Pergunta:** "Funcionários em casa precisam acessar a VPC."

**Resposta curta:** Client VPN.

**Pergunta:** "Registrar domínio e gerenciar DNS."

**Resposta curta:** Route 53.

**Pergunta:** "Mandar 10% dos usuários para a nova versão."

**Resposta curta:** Route 53 weighted routing.

**Pergunta:** "Reduzir latência de conteúdo para usuários globais."

**Resposta curta:** CloudFront.

**Pergunta:** "IPs estáticos globais e failover rápido entre regiões para TCP/UDP."

**Resposta curta:** Global Accelerator.

**Pergunta:** "Criar e proteger uma API REST para funções Lambda."

**Resposta curta:** API Gateway.

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
