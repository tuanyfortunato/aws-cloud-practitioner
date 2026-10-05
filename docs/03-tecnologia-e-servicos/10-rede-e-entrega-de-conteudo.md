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

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon VPC (Virtual Private Cloud)](../../servicos/redes/vpc.md) · [VPC Peering, Transit Gateway, VPC Endpoints e PrivateLink](../../servicos/redes/vpc-peering-transit-gateway-e-endpoints.md) · [AWS VPN (Site-to-Site VPN e Client VPN)](../../servicos/redes/site-to-site-vpn-e-client-vpn.md) · [AWS Direct Connect](../../servicos/redes/direct-connect.md) · [Amazon Route 53](../../servicos/redes/route-53.md) · [Amazon CloudFront](../../servicos/redes/cloudfront.md) · [AWS Global Accelerator](../../servicos/redes/global-accelerator.md) · [Amazon API Gateway](../../servicos/redes/api-gateway.md)

⬅️ [3.9 Outros serviços de armazenamento](09-outros-armazenamentos.md) · 🏠 [Índice do domínio](README.md) · [3.11 Analytics](11-analytics.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **virtual:** Um recurso virtual é criado por software sobre equipamentos físicos. VM significa máquina virtual: computador lógico com sistema operacional e recursos de processamento.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **DNS:** Sistema que relaciona nomes a informações de endereço e outros registros. Resolver o nome de um site não hospeda o site nem garante que ele está funcionando.
- **CDN:** Rede de distribuição de conteúdo. Ela aproxima entrega de conteúdo dos usuários e pode manter cópias em cache conforme as regras.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.
- **autorização:** Decisão sobre o que uma identidade pode fazer em um recurso. Essa decisão depende das regras e do contexto da solicitação.
- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.


Para uma conexão funcionar, o nome deve indicar um destino, o caminho deve existir e os controles devem permitir o tráfego. A identidade da aplicação pode ainda precisar de autorização para os dados. É possível cumprir um desses requisitos e falhar em outro.

Separe rede virtual, ligação entre redes, acesso remoto, resolução de nomes e distribuição de conteúdo. Uma CDN mantém e entrega conteúdo conforme regras; aceleração de rede encaminha tráfego; DNS informa destinos. As três funções não são a mesma etapa.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

a **VPC** é um **condomínio fechado**: as **subnets** são as ruas (públicas dão para a avenida, privadas não); o **Internet Gateway** é o portão principal; o **NAT Gateway** é uma **saída só de ida** para os moradores das ruas privadas; a **VPN** é um túnel pela estrada pública; o **Direct Connect**, uma estrada particular; o **Route 53**, a lista telefônica; o **CloudFront**, lojinhas espalhadas com cópias do conteúdo.

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **Amazon VPC / VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.


**Amazon VPC**

**Antes de ler este trecho:**

- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **CIDR:** Notação de faixa de endereços de rede, como um endereço acompanhado de /24. A faixa define um conjunto de endereços, não uma senha ou uma permissão.


**VPC:** rede virtual isolada logicamente, dentro de uma **região**, com um bloco de IPs (CIDR) definido por você. Cada região tem uma **VPC padrão** pronta.

**Antes de ler este trecho:**

- **AZ:** Parte isolada da infraestrutura dentro de uma região, formada por um ou mais datacenters. Distribuir recursos entre zonas pode reduzir o impacto de uma falha localizada.
- **subnet:** Segmento de uma rede virtual. Na VPC, uma subnet pertence a uma zona de disponibilidade; suas rotas e controles ajudam a definir a conectividade.


**Subnet:** fatia da VPC dentro de **uma AZ**.

**Antes de ler este trecho:**

- **Internet Gateway:** Componente que permite conectividade da VPC com a internet conforme as rotas, endereços e controles usados. Não torna todo recurso público automaticamente.


  - **Pública:** tem rota para um Internet Gateway.

  - **Privada:** sem rota direta para a internet (bancos, back-ends).

**Internet Gateway (IGW):** permite comunicação entre a VPC e a internet (entrada e saída).

**Antes de ler este trecho:**

- **hora:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
- **NAT:** Tradução de endereços de rede. Um NAT Gateway pode permitir conexões de saída de determinados recursos privados sem oferecer entrada direta iniciada pela internet.


**NAT Gateway:** fica na subnet pública e permite que recursos em **subnets privadas saiam para a internet** (ex.: baixar atualizações) **sem receber conexões de fora**. Gerenciado e pago por hora e por dado.


**Route tables:** definem para onde vai o tráfego de cada subnet.


**Security groups e NACLs:** ver [2.8](../02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md).


**VPC Peering:** liga duas VPCs (mesma conta, outra conta ou outra região) como se fossem uma rede. **Não é transitivo:** se A fala com B e B com C, A não fala com C.

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.
- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.


**AWS Transit Gateway:** **hub central** que conecta muitas VPCs e redes on-premises num modelo hub-and-spoke, simplificando dezenas de peerings.


**VPC endpoints:** acessar serviços AWS **sem passar pela internet**.

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **endpoint:** Ponto de acesso a um serviço ou componente. Pode ser um endereço de API ou um recurso de conectividade; identifique qual sentido a seção usa.


  - **Gateway endpoint:** só para **S3 e DynamoDB**, gratuito.

  - **Interface endpoint (AWS PrivateLink):** cria uma interface de rede privada na sua subnet para a maioria dos serviços; pago.

**AWS PrivateLink:** também permite expor um serviço seu para outras VPCs ou clientes de forma privada.


**VPC Flow Logs:** registram o tráfego de rede (ver [2.7](../02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)).



**Conectividade híbrida**

**Antes de ler este trecho:**

- **VPN:** Conexão lógica protegida que liga usuários ou redes. Um túnel VPN não concede automaticamente acesso a todos os recursos do destino.
- **AWS Direct Connect / Direct Connect:** Direct Connect permite estabelecer essa conectividade por conexões e locais compatíveis, com interfaces e rotas configuradas para o ambiente.
- **Connect:** Amazon Connect oferece uma plataforma de contact center em nuvem com canais e recursos compatíveis.
- **datacenter:** Instalação física com equipamentos de computação, rede, energia e refrigeração. A nuvem continua dependendo desses equipamentos, mas o cliente não precisa manter o prédio.
- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.
- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Serviço | Como funciona | Quando usar |
| --- | --- | --- |
| AWS Site-to-Site VPN | Túnel IPsec **criptografado pela internet** entre o datacenter (Customer Gateway) e a AWS (Virtual Private Gateway ou Transit Gateway) | Rápido de configurar (minutos), barato; aceita a variação da internet; também serve de backup do Direct Connect |
| AWS Client VPN | VPN gerenciada para **usuários remotos** (notebooks) acessarem a VPC | Trabalho remoto |
| AWS Direct Connect | **Conexão física dedicada e privada**, que não passa pela internet, a partir de um local Direct Connect | Banda alta e estável, latência consistente, menor custo de transferência para grandes volumes; leva semanas para instalar; não é criptografado por padrão (pode rodar VPN por cima) |



**DNS, CDN e aceleração**

**Antes de ler este trecho:**

- **Amazon Route 53 / Route 53:** Route 53 oferece DNS e recursos associados, como registro de domínios e verificações de saúde.


**Amazon Route 53:** DNS gerenciado, altamente disponível. Registra domínios, roteia usuários para recursos e faz **health checks**.

**Antes de ler este trecho:**

- **failover:** Mudança do atendimento para um componente alternativo quando o principal fica indisponível. A forma e o tempo dependem da solução.
- **ativo-passivo:** Um ambiente atende normalmente e outro fica preparado para assumir. O preparo da alternativa pode variar bastante.


  - **Políticas de roteamento:** simple, **weighted** (divide tráfego por percentual, ex.: testes A/B), **latency-based** (região com menor latência), **failover** (ativo-passivo), **geolocation** (por país/continente do usuário), **geoproximity** (por distância, com ajuste), **multivalue answer** e IP-based.
**Antes de ler este trecho:**

- **Amazon CloudFront / CloudFront:** CloudFront distribui conteúdo por uma rede de pontos de presença.
- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.
- **carga:** Aplicação ou conjunto de tarefas com seus recursos e necessidades. Avaliar uma carga significa avaliar o trabalho completo, não uma única máquina isolada.
- **cache:** Cópia mantida para reutilização rápida. A aplicação ou o serviço precisa decidir atualização e validade, para não servir conteúdo inadequado ou antigo.
- **origem:** Local de onde uma distribuição obtém conteúdo, como um servidor ou bucket. Uma cópia em cache não elimina toda necessidade de acessar a origem.


**Amazon CloudFront:** **CDN** global. Faz **cache** de conteúdo estático e dinâmico nas edge locations, reduzindo latência e carga na origem.

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **API Gateway:** API Gateway ajuda a publicar e administrar APIs.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **servidor:** Computador que atende pedidos de outros computadores. Um servidor web, por exemplo, responde aos pedidos enviados pelo navegador.
- **HTTP:** Protocolo de pedidos e respostas usado na web. Uma URL e um método indicam a operação; HTTP sozinho não protege o conteúdo por criptografia.
- **ALB:** Modalidades de balanceador com focos diferentes: aplicação, transporte de rede e integração de equipamentos virtuais. Os protocolos e casos de uso determinam a escolha.


  - Origens: S3, ALB, EC2, API Gateway ou qualquer servidor HTTP.
**Antes de ler este trecho:**

- **OAC:** Controle de acesso à origem em integrações CloudFront compatíveis. Ajuda a restringir acesso direto à origem conforme a configuração.
- **bucket:** Recipiente que organiza objetos no S3. A aplicação usa o bucket e a identificação do objeto para pedir operações autorizadas.


  - **Origin Access Control (OAC):** deixa o bucket S3 privado, acessível só pelo CloudFront.
**Antes de ler este trecho:**

- **Shield:** Shield oferece proteção contra ataques de negação de serviço distribuídos, com diferenças de cobertura e recursos entre suas modalidades.
- **WAF:** WAF aplica regras ao tráfego web em integrações compatíveis.
- **HTTPS:** HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.
- **ACM:** ACM administra certificados em integrações compatíveis. CA significa autoridade certificadora, responsável por emitir certificados sob suas regras.


  - HTTPS com certificado do ACM; restrição geográfica; inclui **Shield Standard** e integra com **WAF**.
**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.


  - Lambda@Edge e CloudFront Functions rodam código nas edge locations.
**Antes de ler este trecho:**

- **AWS Global Accelerator / Global Accelerator:** Global Accelerator usa a rede global da AWS para encaminhar tráfego a destinos compatíveis, considerando configuração e saúde desses destinos.
- **regional:** O recurso ou a operação pertence a uma região. Serviços globais podem administrar objetos regionais; leia o alcance do recurso, não apenas o nome do serviço.
- **TCP:** Protocolo de transporte orientado a conexão, com mecanismos de entrega e ordem. É usado por muitas aplicações; não acrescenta criptografia por si só.
- **UDP:** Protocolo de transporte por datagramas, sem as mesmas garantias de entrega e ordem do TCP. A aplicação precisa lidar com os requisitos que o protocolo não fornece.


**AWS Global Accelerator:** fornece **IPs estáticos anycast** e leva o tráfego pela **rede global da AWS** até o endpoint regional mais saudável e próximo. Melhora performance de aplicações TCP/UDP e faz failover rápido entre regiões. **Não faz cache.**

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **Cognito:** Cognito oferece recursos de identidade para usuários de aplicações.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **WebSocket:** Comunicação que mantém uma conexão para troca de mensagens entre cliente e servidor. É diferente de uma sequência de pedidos web independentes.
- **REST:** Estilo de API que usa recursos e operações, frequentemente por HTTP. O código integrado continua sendo responsável pelo comportamento da aplicação.
- **autenticação:** Verificação de quem está acessando. Confirmar a identidade não autoriza qualquer ação no sistema.


**Amazon API Gateway:** Pontos de prova: cria APIs REST, HTTP e WebSocket em qualquer escala; faz controle de tráfego (throttling), autenticação (IAM, Cognito, Lambda authorizer) e cache; integração clássica com Lambda para back-ends serverless; cobrado por chamada.


**Cai na prova:** "subnet privada precisa baixar patches da internet" = NAT Gateway; "conectar 50 VPCs e o datacenter" = Transit Gateway; "acessar o S3 sem sair para a internet" = gateway endpoint; "link privado com banda dedicada" = Direct Connect; "conexão rápida e criptografada com o datacenter" = Site-to-Site VPN; "site com usuários no mundo todo, conteúdo estático" = CloudFront; "jogo multiplayer UDP com IPs fixos globais" = Global Accelerator; "mandar usuários para a região mais rápida" = Route 53 latency-based.

### ➕ Complemento

**CloudFront signed URLs e signed cookies:** restringem o acesso a conteúdo privado distribuído pelo CloudFront (ex.: cursos pagos).


**Route 53 health checks + failover:** se o endpoint principal cair, o DNS passa a responder com o secundário.

**Antes de ler este trecho:**

- **porta:** Número que ajuda a identificar o serviço de destino de uma comunicação. Liberar uma porta autoriza tráfego segundo a regra, mas não configura a aplicação para responder.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.


**Bastion host**: instância na subnet pública usada para acessar recursos privados; o Session Manager é a alternativa sem porta aberta.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **SG:** Regras de tráfego associadas a interfaces ou recursos compatíveis. É um controle de rede, não uma permissão IAM para ler um arquivo ou chamar uma API.
- **NACL:** ACL significa lista de controle de acesso. A NACL da VPC controla tráfego no segmento de rede; ACL de armazenamento tem outro contexto. Não trate as duas como a mesma função.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.


**Primeiro, identifique o funcionamento:** VPC fornece rede lógica; subnets e tabelas de rota definem caminhos; gateways e endpoints conectam destinos; SG/NACL controlam tráfego. DNS encontra endereços, CDN entrega conteúdo.

**Depois, compare as escolhas:** Route 53 para DNS; CloudFront para cache/distribuição; API Gateway para entrada de API; VPN para túnel; Direct Connect para conexão dedicada; PrivateLink para serviço privado suportado.

**Por fim, verifique o limite:** Subnet pública sozinha não torna EC2 acessível: precisa endereço adequado, rota, controles e aplicação. Direct Connect não cifra tudo por padrão; use criptografia quando requerida.

## 4. Caso resolvido

Uma instância privada precisa iniciar downloads na internet sem aceitar conexões iniciadas de fora. Qual componente típico?

**Raciocínio e resposta:** NAT Gateway para saída IPv4 com rotas adequadas. Internet Gateway sem endereço público e sem configurar o restante não resolve sozinho.

A resposta muda se mudar o requisito destacado. Compare a necessidade com a função da solução, em vez de apenas associar duas palavras.

## 5. Revisão do capítulo

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Usuários precisam chegar ao site, a aplicação precisa chegar ao banco e a empresa pode precisar conectar sua rede à AWS. Cada comunicação tem um caminho e controles.

**2. O que a solução fornece?**

Rede define conexões e rotas. VPC organiza recursos em uma rede virtual; DNS relaciona nomes a endereços; distribuição de conteúdo e aceleração atuam na entrega aos usuários.

**3. Que conclusão seria incorreta?**

Nenhum serviço desta lista configura toda a comunicação sozinho. Organizar rede, permitir acesso, resolver nomes e distribuir conteúdo são funções distintas.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

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


**Fundamento explicado no capítulo:** "O que torna uma subnet pública?" → Ter rota para um Internet Gateway.

**Pergunta:** "Instâncias em subnet privada precisam baixar atualizações."

**Resposta curta:** NAT Gateway.


**Fundamento explicado no capítulo:** "Instâncias em subnet privada precisam baixar atualizações." → NAT Gateway.

**Pergunta:** "Conectar duas VPCs de contas diferentes."

**Resposta curta:** VPC Peering.


**Fundamento explicado no capítulo:** "Conectar duas VPCs de contas diferentes." → VPC Peering.

**Pergunta:** "Conectar dezenas de VPCs e o datacenter num hub."

**Resposta curta:** Transit Gateway.


**Fundamento explicado no capítulo:** "Conectar dezenas de VPCs e o datacenter num hub." → Transit Gateway.

**Pergunta:** "Acessar o S3 a partir da VPC sem passar pela internet."

**Resposta curta:** Gateway VPC endpoint.


**Fundamento explicado no capítulo:** "Acessar o S3 a partir da VPC sem passar pela internet." → Gateway VPC endpoint.

**Pergunta:** "Conexão privada e dedicada, sem internet, com desempenho consistente."

**Resposta curta:** Direct Connect.


**Fundamento explicado no capítulo:** "Conexão privada e dedicada, sem internet, com desempenho consistente." → Direct Connect.

**Pergunta:** "Conexão criptografada com o datacenter, pronta hoje."

**Resposta curta:** Site-to-Site VPN.


**Fundamento explicado no capítulo:** "Conexão criptografada com o datacenter, pronta hoje." → Site-to-Site VPN.

**Pergunta:** "Funcionários em casa precisam acessar a VPC."

**Resposta curta:** Client VPN.


**Fundamento explicado no capítulo:** "Funcionários em casa precisam acessar a VPC." → Client VPN.

**Pergunta:** "Registrar domínio e gerenciar DNS."

**Resposta curta:** Route 53.


**Fundamento explicado no capítulo:** "Registrar domínio e gerenciar DNS." → Route 53.

**Pergunta:** "Mandar 10% dos usuários para a nova versão."

**Resposta curta:** Route 53 weighted routing.


**Fundamento explicado no capítulo:** "Mandar 10% dos usuários para a nova versão." → Route 53 weighted routing.

**Pergunta:** "Reduzir latência de conteúdo para usuários globais."

**Resposta curta:** CloudFront.


**Fundamento explicado no capítulo:** "Reduzir latência de conteúdo para usuários globais." → CloudFront.

**Pergunta:** "IPs estáticos globais e failover rápido entre regiões para TCP/UDP."

**Resposta curta:** Global Accelerator.


**Fundamento explicado no capítulo:** "IPs estáticos globais e failover rápido entre regiões para TCP/UDP." → Global Accelerator.

**Pergunta:** "Criar e proteger uma API REST para funções Lambda."

**Resposta curta:** API Gateway.


**Fundamento explicado no capítulo:** "Criar e proteger uma API REST para funções Lambda." → API Gateway.

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
