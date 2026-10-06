# 3.2 Infraestrutura global

## 🧠 Antes de começar

**Qual é a dificuldade?** Uma aplicação precisa estar perto dos usuários e continuar atendendo se parte da infraestrutura falhar. Para planejar isso, a equipe precisa entender onde os recursos ficam.

**A ideia em palavras simples:** A infraestrutura global organiza regiões, zonas de disponibilidade e pontos de presença. São unidades com funções diferentes, não nomes intercambiáveis para o mesmo lugar.

**Exemplo do dia a dia:** A escola escolhe uma região para seus recursos e planeja partes da aplicação em zonas diferentes. Uma rede de distribuição pode entregar conteúdo por pontos de presença.

**O que não concluir?** Escolher uma região não distribui automaticamente todo recurso entre várias zonas. Localização, disponibilidade e serviços oferecidos precisam ser avaliados.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **AZ** | um ou mais datacenters isolados dentro de uma região. |
| **Edge location** | ponto de presença usado por CloudFront, Route 53 e outros serviços para ficar perto do usuário. |
| **Latência** | o tempo que a informação leva para ir e voltar. |

---

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)**

> 🔎 **Fichas detalhadas:** [AWS Outposts, Local Zones e Wavelength](../../servicos/computacao/outposts-local-zones-wavelength.md) · [Amazon CloudFront](../../servicos/redes/cloudfront.md) · [AWS Global Accelerator](../../servicos/redes/global-accelerator.md)

> ⚠️ **Atualização do exam guide (verificado em 04/10/2026):** Na lista oficial atual, **Outposts** está no escopo, **Local Zones** não aparece e **Wavelength** está **fora do escopo**. [Ver escopo oficial](../00-guia-do-exame/escopo-oficial.md).

⬅️ [3.1 Formas de acessar e implantar na AWS](01-formas-de-acesso-e-implantacao.md) · 🏠 [Índice do domínio](README.md) · [3.3 Amazon EC2](03-ec2.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **ponto de presença:** Local de infraestrutura usado para aproximar determinadas funções dos usuários, como entrega de conteúdo. Não é uma região completa com todos os serviços.
- **redundância:** Existência de componentes alternativos. Duas cópias só ajudam se forem utilizáveis na falha que você pretende enfrentar.

Região, zona e ponto de presença descrevem unidades diferentes. Primeiro escolha onde o recurso será criado; depois avalie como ele distribui componentes e atende usuários. Um recurso numa região não ganhou redundância automaticamente.

Várias zonas podem ajudar com falhas locais. Pontos de presença aproximam determinadas funções, como distribuição de conteúdo. Múltiplas regiões pedem decisões adicionais sobre dados, acesso, custos e recuperação; são escolhas de projeto, não apenas nomes no mapa.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

a **região** é uma **cidade**; cada **AZ** é um **bairro** com a própria energia e rede, longe o bastante para um incêndio não atingir os outros; as **edge locations** são **lojinhas de conveniência** espalhadas que guardam cópias do que mais se pede.

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **Route 53:** Route 53 oferece DNS e recursos associados, como registro de domínios e verificações de saúde.
- **CloudFront:** CloudFront distribui conteúdo por uma rede de pontos de presença.
- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **Organizations:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.
- **regional:** O recurso ou a operação pertence a uma região. Serviços globais podem administrar objetos regionais; leia o alcance do recurso, não apenas o nome do serviço.

**Região:** área geográfica isolada e independente das outras, com várias AZs. A maioria dos serviços é **regional**; alguns são **globais** (IAM, Route 53, CloudFront, Organizations).

**Como escolher a região (4 fatores):**

**Antes de ler este trecho:**

- **compliance:** Atendimento a requisitos definidos. Usar um serviço com certificações não torna automaticamente a aplicação do cliente conforme.

  1. **Compliance e governança de dados:** leis que exigem que os dados fiquem num país.
**Antes de ler este trecho:**

- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.

  2. **Proximidade dos clientes:** menor latência.

  3. **Serviços disponíveis:** nem todo serviço ou recurso existe em todas as regiões.

  4. **Preço:** varia entre regiões.
**Antes de ler este trecho:**

- **AZ:** Parte isolada da infraestrutura dentro de uma região, formada por um ou mais datacenters. Distribuir recursos entre zonas pode reduzir o impacto de uma falha localizada.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.

**Availability Zone (AZ):** um ou mais datacenters distintos, com energia, rede e refrigeração redundantes, fisicamente separados de outras AZs (distância significativa), mas ligados por rede de baixa latência. Regiões novas têm no mínimo três AZs.

**Antes de ler este trecho:**

- **Global Accelerator:** Global Accelerator usa a rede global da AWS para encaminhar tráfego a destinos compatíveis, considerando configuração e saúde desses destinos.
- **Shield:** Shield oferece proteção contra ataques de negação de serviço distribuídos, com diferenças de cobertura e recursos entre suas modalidades.
- **WAF:** WAF aplica regras ao tráfego web em integrações compatíveis.
- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.
- **DNS:** Sistema que relaciona nomes a informações de endereço e outros registros. Resolver o nome de um site não hospeda o site nem garante que ele está funcionando.
- **cache:** Cópia mantida para reutilização rápida. A aplicação ou o serviço precisa decidir atualização e validade, para não servir conteúdo inadequado ou antigo.
- **origem:** Local de onde uma distribuição obtém conteúdo, como um servidor ou bucket. Uma cópia em cache não elimina toda necessidade de acessar a origem.

**Edge locations (pontos de presença):** muito mais numerosas que as regiões, em grandes cidades. Usadas por **CloudFront** (cache), **Route 53** (DNS), **Global Accelerator**, **Shield** e **WAF**. **Regional edge caches** ficam entre as edge locations e a origem.

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.

**AWS Local Zones:** extensão de uma região para perto de grandes centros urbanos, para latência de um dígito de milissegundo (ex.: renderização, games, mídia).

**AWS Wavelength:** infraestrutura AWS dentro das redes **5G** das operadoras, para aplicações móveis de ultrabaixa latência.

**Antes de ler este trecho:**

- **datacenter:** Instalação física com equipamentos de computação, rede, energia e refrigeração. A nuvem continua dependendo desses equipamentos, mas o cliente não precisa manter o prédio.

**AWS Outposts:** racks e servidores da AWS instalados **no seu datacenter**, com os mesmos serviços, APIs e ferramentas. Para latência local, processamento local de dados ou residência de dados.

**Antes de ler este trecho:**

- **alta disponibilidade:** Planejamento para manter o sistema acessível diante de determinadas falhas. Não é promessa de ausência de qualquer interrupção.

**Alta disponibilidade na prática:**

**Antes de ler este trecho:**

- **Multi-AZ:** Configuração que utiliza mais de uma zona de disponibilidade. Seu comportamento depende do serviço: não presuma que toda cópia atende leituras ou que isso é backup de dados apagados.

  - Falha de um datacenter → distribuir em **várias AZs** (Multi-AZ).
**Antes de ler este trecho:**

- **DR:** Recuperação de desastres: plano para recuperar uma operação depois de uma interrupção grave. Inclui recursos, procedimentos e testes.

  - Desastre regional, latência para usuários globais ou exigência de DR → **várias regiões**.

**Cai na prova:** "menor latência para usuários do mundo todo" = CloudFront/edge locations; "serviço AWS no datacenter da empresa" = Outposts; "aplicação 5G" = Wavelength; "apagão de uma AZ não derrubar a aplicação" = Multi-AZ.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.

**Primeiro, identifique o funcionamento:** Uma região reúne AZs; cada AZ é um domínio de falha com um ou mais datacenters. Edge locations aproximam entrega e serviços de usuários.

**Depois, compare as escolhas:** Multi-AZ para disponibilidade regional; múltiplas regiões para requisitos como recuperação regional, residência de dados e latência. CloudFront usa a borda para entrega de conteúdo.

**Por fim, verifique o limite:** Escolher outra região não copia automaticamente recursos e dados. Edge não equivale a uma AZ em que você instala qualquer EC2. Multi-AZ não cobre todos os desastres regionais.

## 4. Caso resolvido

A aplicação deve continuar após falha de uma AZ. Basta criar duas EC2 na mesma subnet?

**Raciocínio e resposta:** Não: uma subnet pertence a uma AZ. Distribua componentes entre AZs e considere balanceamento, estado e banco, não apenas número de instâncias.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Diferenciar **região, AZ e edge location**.
- [ ] Citar os **4 fatores** para escolher região (compliance, proximidade, serviços disponíveis, preço).
- [ ] Saber quando usar **várias AZs** (falha de datacenter) × **várias regiões** (desastre regional, usuários globais).
- [ ] Diferenciar **Outposts, Local Zones e Wavelength**.

**Dica de revisão para a prova:** "Falha de **um datacenter**" → **várias AZs**. "Lei exige dados no país" → escolher a **região**. "Usuários no mundo todo" → **CloudFront/edge**. "AWS dentro do **meu** datacenter" → **Outposts**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).
**Pergunta:** "Quais fatores considerar ao escolher uma região?"

**Resposta curta:** Compliance/residência de dados, latência para os clientes, serviços disponíveis e preço.

**Pergunta:** "O que é uma AZ?"

**Resposta curta:** Um ou mais datacenters isolados dentro de uma região, com energia e rede redundantes.

**Pergunta:** "Para que servem as edge locations?"

**Resposta curta:** Cache do CloudFront, DNS do Route 53 e entrada do Global Accelerator, perto do usuário.

**Pergunta:** "Qual serviço é global?"

**Resposta curta:** IAM, Route 53, CloudFront ou Organizations.

**Pergunta:** "A empresa precisa rodar serviços AWS no próprio datacenter."

**Resposta curta:** AWS Outposts.

**Pergunta:** "Latência de um dígito de milissegundo para usuários de uma cidade sem região AWS."

**Resposta curta:** Local Zones.

**Pergunta:** "Aplicação móvel em rede 5G com ultrabaixa latência."

**Resposta curta:** Wavelength.

**Pergunta:** "Como sobreviver à falha de uma região inteira?"

**Resposta curta:** Arquitetura multi-região.

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- **Números atuais (🧊 aproximados):** 39 regiões geográficas e 124 AZs, com mais regiões anunciadas (Arábia Saudita, Chile). A prova cobra o conceito: **região = várias AZs (mínimo 3); AZ = um ou mais datacenters**.
- **Edge (🧊):** CloudFront com 750+ PoPs em 100+ cidades, 1.140+ PoPs embarcados em ISPs e 15 Regional Edge Caches. Simulados antigos falam em "400+" ou "450+". Basta saber que **edge locations são muito mais numerosas que regiões**.
- **AWS European Sovereign Cloud** (Brandenburg, `eusc-de-east-1`): região soberana europeia, operada separadamente. Bom saber que existe.
- ⚠️ "Várias AZs" = alta disponibilidade/tolerância a falhas. "Várias regiões" = DR geográfico, latência global ou exigência legal. **Nunca** "várias edge locations" para alta disponibilidade de computação.
- ⚠️ Local Zones (perto de cidades) × Wavelength (dentro da rede 5G) × Outposts (hardware AWS no seu datacenter).
- ✔️ **Termos da task 3.2 do exam guide (verificado em 04/10/2026):**
  - **AZs não compartilham ponto único de falha**: cada AZ tem energia, rede e refrigeração independentes; por isso várias AZs = alta disponibilidade.
  - Quando usar **várias regiões**: recuperação de desastres (**DR**), **continuidade de negócios**, **baixa latência** para usuários finais e **soberania de dados** (exigência legal de manter os dados num país ou região).
  - **Benefícios das edge locations**: conteúdo e DNS mais perto do usuário, menor latência.
- 🧊 Não decorar: contagem de AZs por região, códigos de região, lista de cidades de PoPs.
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.1 Formas de acessar e implantar na AWS](01-formas-de-acesso-e-implantacao.md) · 🏠 [Índice do domínio](README.md) · [3.3 Amazon EC2](03-ec2.md) ➡️
