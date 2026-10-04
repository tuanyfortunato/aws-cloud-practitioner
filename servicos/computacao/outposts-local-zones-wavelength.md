# AWS Outposts, Local Zones e Wavelength

> **Categoria:** Infraestrutura híbrida e de borda · **Domínio:** 3 · **Escopo:** extensões de uma região · **Tópico do guia:** [3.2 Infraestrutura global](../../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md)
>
> **Em uma frase:** três formas de levar a infraestrutura AWS para mais perto de onde a latência ou a localização dos dados importam.
>
> **Escopo oficial:** 🔀 Outposts ✅ · Local Zones ⚪ não listado · Wavelength ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Comparação

| | **AWS Outposts** | **AWS Local Zones** | **AWS Wavelength** |
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

## 🔗 Documentação oficial

- [Outposts](https://aws.amazon.com/outposts/) · [Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) · [Wavelength](https://aws.amazon.com/wavelength/)
