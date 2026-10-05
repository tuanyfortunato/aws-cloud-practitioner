# AWS Outposts, Local Zones e Wavelength

> **Categoria:** Infraestrutura híbrida e de borda · **Domínio:** 3 · **Escopo:** extensões de uma região · **Tópico do guia:** [3.2 Infraestrutura global](../../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md)
>
> **Em uma frase:** três formas de levar a infraestrutura AWS para mais perto de onde a latência ou a localização dos dados importam.
>
> **Escopo oficial:** 🔀 Outposts ✅ · Local Zones ⚪ não listado · Wavelength ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** são três jeitos de **trazer a AWS para mais perto**: o Outposts é uma "filial" da AWS **dentro do seu prédio**; a Local Zone, uma filial **numa cidade**; o Wavelength, uma filial **dentro da rede 5G** da operadora.

- ✅ **Escolha quando:** precisa de **latência muito baixa** ou de **manter os dados num local específico**.
- 🚫 **Não é a resposta quando:** só quer entregar **conteúdo mais perto** dos usuários → [CloudFront](../redes/cloudfront.md) (edge locations).
- 🎯 **Palavras do enunciado que apontam para ele:** "serviços AWS no próprio datacenter" → Outposts; "latência de um dígito de milissegundo numa cidade" → Local Zones; "5G" → Wavelength.
<!-- didatico:fim -->

## Comparação

| | **AWS Outposts** ✅ | **AWS Local Zones** ⚪ | **AWS Wavelength** ❌ *fora do escopo* |
|---|---|---|---|
| Onde fica | **No seu datacenter** ou instalação | Em grandes cidades, operada pela AWS | **Dentro da rede 5G** de operadoras |
| Para quê | Latência local, processamento local, **residência de dados** | Latência de **um dígito de ms** para usuários de uma cidade | Ultrabaixa latência para dispositivos **móveis 5G** |
| Exemplos | Fábricas, hospitais, bancos com dados que não podem sair do local | Renderização, games, mídia ao vivo, VDI | Carros conectados, AR/VR, jogos em nuvem móveis |
| Quem opera o hardware | AWS (instala, monitora, atualiza); você cuida da energia, rede e segurança física do local | AWS | AWS + operadora |
| Como usar | Formatos **rack** (42U) ou **servidores** (1U/2U); mesmas APIs e console | Ativar a zona e criar uma subnet nela | Criar subnet na Wavelength Zone |

## 🎯 Escopo da prova

- **Outposts** está na lista oficial; **Local Zones** não aparece; **Wavelength** está declarado **fora do escopo**.

## Serviços disponíveis

- **Outposts:** EC2, EBS, S3 on Outposts, ECS, EKS, RDS, EMR, ElastiCache (varia por formato).
- **Local Zones / Wavelength:** subconjunto (EC2, EBS, ECS/EKS, ALB…), conectado à região-mãe.

## Responsabilidade compartilhada (Outposts)

- **AWS:** hardware, software, manutenção e substituição.
- **Cliente:** **segurança física e ambiente do local** (energia, refrigeração, rede), além do que já seria dele na nuvem.

## 🔄 Atualizações 2025-2026

- Com o fim da família Snow para novos clientes, a AWS indica **Outposts** para computação de borda. Ver [Snow Family](../migracao/snow-family.md).

## ⚠️ Pegadinhas e não confundir

- "Serviço AWS **no datacenter da empresa**" → Outposts. "Perto de uma **cidade** sem região" → Local Zones. "Rede **5G**" → Wavelength.
- Nenhum deles é "edge location" do CloudFront.

## ❓ Perguntas típicas

- "A empresa precisa rodar serviços AWS no próprio datacenter." → Outposts.
- "Latência de um dígito de milissegundo numa cidade sem região AWS." → Local Zones.
- "Aplicação móvel 5G com ultrabaixa latência." → Wavelength.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Outposts no local do cliente; Local Zones próximas de cidades; Wavelength junto à rede de operadoras |
| **O que você decide/configura?** | Localidade, serviço disponível e infraestrutura/conectividade exigida |
| **Em que ordem as coisas acontecem?** | Selecione oferta pelo requisito de localização e use recursos compatíveis |
| **O que pode fazer, e em que condição?** | Outposts atende workloads locais com serviços AWS suportados |
| **O que não pode presumir?** | Não oferece todo o catálogo em qualquer local; os três nomes têm status de escopo diferentes |

**Caso comentado:** Requisito de manter computação no prédio: avalie Outposts; não confunda com região inteiramente nova.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Outposts](https://aws.amazon.com/outposts/) · [Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) · [Wavelength](https://aws.amazon.com/wavelength/)
