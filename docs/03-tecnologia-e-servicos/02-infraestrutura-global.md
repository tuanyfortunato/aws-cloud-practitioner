# 3.2 Infraestrutura global

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS Outposts, Local Zones e Wavelength](../../servicos/computacao/outposts-local-zones-wavelength.md) · [Amazon CloudFront](../../servicos/redes/cloudfront.md) · [AWS Global Accelerator](../../servicos/redes/global-accelerator.md)

> ⚠️ **Atualização do exam guide (verificado em 04/10/2026):** Na lista oficial atual, **Outposts** está no escopo, **Local Zones** não aparece e **Wavelength** está **fora do escopo**. [Ver escopo oficial](../00-guia-do-exame/escopo-oficial.md).

⬅️ [3.1 Formas de acessar e implantar na AWS](01-formas-de-acesso-e-implantacao.md) · 🏠 [Índice do domínio](README.md) · [3.3 Amazon EC2](03-ec2.md) ➡️

---

## 📖 Conteúdo

- **Região:** área geográfica isolada e independente das outras, com várias AZs. A maioria dos serviços é **regional**; alguns são **globais** (IAM, Route 53, CloudFront, Organizations).
- **Como escolher a região (4 fatores):**
  1. **Compliance e governança de dados:** leis que exigem que os dados fiquem num país.
  2. **Proximidade dos clientes:** menor latência.
  3. **Serviços disponíveis:** nem todo serviço ou recurso existe em todas as regiões.
  4. **Preço:** varia entre regiões.
- **Availability Zone (AZ):** um ou mais datacenters distintos, com energia, rede e refrigeração redundantes, fisicamente separados de outras AZs (distância significativa), mas ligados por rede de baixa latência. Regiões novas têm no mínimo três AZs.
- **Edge locations (pontos de presença):** muito mais numerosas que as regiões, em grandes cidades. Usadas por **CloudFront** (cache), **Route 53** (DNS), **Global Accelerator**, **Shield** e **WAF**. **Regional edge caches** ficam entre as edge locations e a origem.
- **AWS Local Zones:** extensão de uma região para perto de grandes centros urbanos, para latência de um dígito de milissegundo (ex.: renderização, games, mídia).
- **AWS Wavelength:** infraestrutura AWS dentro das redes **5G** das operadoras, para aplicações móveis de ultrabaixa latência.
- **AWS Outposts:** racks e servidores da AWS instalados **no seu datacenter**, com os mesmos serviços, APIs e ferramentas. Para latência local, processamento local de dados ou residência de dados.
- **Alta disponibilidade na prática:**
  - Falha de um datacenter → distribuir em **várias AZs** (Multi-AZ).
  - Desastre regional, latência para usuários globais ou exigência de DR → **várias regiões**.
- **Cai na prova:** "menor latência para usuários do mundo todo" = CloudFront/edge locations; "serviço AWS no datacenter da empresa" = Outposts; "aplicação 5G" = Wavelength; "apagão de uma AZ não derrubar a aplicação" = Multi-AZ.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).

- "Quais fatores considerar ao escolher uma região?" → Compliance/residência de dados, latência para os clientes, serviços disponíveis e preço.
- "O que é uma AZ?" → Um ou mais datacenters isolados dentro de uma região, com energia e rede redundantes.
- "Para que servem as edge locations?" → Cache do CloudFront, DNS do Route 53 e entrada do Global Accelerator, perto do usuário.
- "Qual serviço é global?" → IAM, Route 53, CloudFront ou Organizations.
- "A empresa precisa rodar serviços AWS no próprio datacenter." → AWS Outposts.
- "Latência de um dígito de milissegundo para usuários de uma cidade sem região AWS." → Local Zones.
- "Aplicação móvel em rede 5G com ultrabaixa latência." → Wavelength.
- "Como sobreviver à falha de uma região inteira?" → Arquitetura multi-região.

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
