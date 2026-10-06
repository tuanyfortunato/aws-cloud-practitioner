# AWS Outposts, Local Zones e Wavelength

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Algumas aplicações precisam executar perto de equipamentos, pessoas ou redes específicas. Uma região AWS distante pode não atender ao requisito de proximidade.

**Como este serviço ajuda?** Esta ficha compara formas de aproximar infraestrutura AWS: Outposts no local do cliente, Local Zones perto de centros urbanos e Wavelength em redes de operadoras compatíveis.

**Exemplo do dia a dia:** Uma fábrica pode precisar processar dados perto das máquinas e avaliar Outposts. Uma aplicação urbana pode avaliar uma Local Zone, conforme a disponibilidade.

**O que ele não resolve sozinho?** As três opções não são o mesmo produto nem oferecem todos os serviços de uma região. Disponibilidade e escopo da prova diferem entre elas; confira a identificação abaixo.

**Primeiras palavras para entender:**

- **Latência:** tempo de uma comunicação.
- **Datacenter:** local onde ficam servidores.
- **Borda:** execução próxima da origem ou do consumidor dos dados.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Infraestrutura híbrida e de borda · **Domínio:** 3 · **Escopo:** extensões de uma região · **Tópico do guia:** [3.2 Infraestrutura global](../../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md)
>
> **Em uma frase:** três formas de levar a infraestrutura AWS para mais perto de onde a latência ou a localização dos dados importam.
>
> **Escopo oficial:** 🔀 Outposts ✅ · Local Zones ⚪ não listado · Wavelength ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Identifique onde o processamento precisa ocorrer e qual tempo de comunicação é aceitável.

**Passo 2.** Compare as localizações e os serviços disponíveis em cada oferta. Não confunda equipamento no cliente com infraestrutura em outro local.

**Passo 3.** Planeje comunicação e operação conforme a opção. Confira restrições antes de supor que toda região e toda oferta atendem o cenário.

## 2. Recursos e opções, com significado

### Comparação

| | **AWS Outposts** ✅ | **AWS Local Zones** ⚪ | **AWS Wavelength** ❌ *fora do escopo* |
|---|---|---|---|
| Onde fica | **No seu datacenter** ou instalação | Em grandes cidades, operada pela AWS | **Dentro da rede 5G** de operadoras |
| Para quê | Latência local, processamento local, **residência de dados** | Latência de **um dígito de ms** para usuários de uma cidade | Ultrabaixa latência para dispositivos **móveis 5G** |
| Exemplos | Fábricas, hospitais, bancos com dados que não podem sair do local | Renderização, games, mídia ao vivo, VDI | Carros conectados, AR/VR, jogos em nuvem móveis |
| Quem opera o hardware | AWS (instala, monitora, atualiza); você cuida da energia, rede e segurança física do local | AWS | AWS + operadora |
| Como usar | Formatos **rack** (42U) ou **servidores** (1U/2U); mesmas APIs e console | Ativar a zona e criar uma subnet nela | Criar subnet na Wavelength Zone |

### 🎯 Escopo da prova

**Outposts** está na lista oficial; **Local Zones** não aparece; **Wavelength** está declarado **fora do escopo**.

### Serviços disponíveis

**Outposts:** EC2, EBS, S3 on Outposts, ECS, EKS, RDS, EMR, ElastiCache (varia por formato).

**Local Zones / Wavelength:** subconjunto (EC2, EBS, ECS/EKS, ALB…), conectado à região-mãe.

### Responsabilidade compartilhada (Outposts)

**AWS:** hardware, software, manutenção e substituição.

**Cliente:** **segurança física e ambiente do local** (energia, refrigeração, rede), além do que já seria dele na nuvem.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

As três opções não são o mesmo produto nem oferecem todos os serviços de uma região. Disponibilidade e escopo da prova diferem entre elas; confira a identificação abaixo.

### ⚠️ Pegadinhas e não confundir

"Serviço AWS **no datacenter da empresa**" → Outposts. "Perto de uma **cidade** sem região" → Local Zones. "Rede **5G**" → Wavelength.

Nenhum deles é "edge location" do CloudFront.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### 🔄 Atualizações 2025-2026

Com o fim da família Snow para novos clientes, a AWS indica **Outposts** para computação de borda. Ver [Snow Family](../migracao/snow-family.md).

## 5. Caso resolvido: ligando as peças

Uma fábrica pode precisar processar dados perto das máquinas e avaliar Outposts. Uma aplicação urbana pode avaliar uma Local Zone, conforme a disponibilidade.

**Aplicando a sequência à situação:**

**Etapa 1:** Identifique onde o processamento precisa ocorrer e qual tempo de comunicação é aceitável.
**Etapa 2:** Compare as localizações e os serviços disponíveis em cada oferta. Não confunda equipamento no cliente com infraestrutura em outro local.
**Etapa 3:** Planeje comunicação e operação conforme a opção. Confira restrições antes de supor que toda região e toda oferta atendem o cenário.

**Resultado e responsabilidade:** Esta ficha compara formas de aproximar infraestrutura AWS: Outposts no local do cliente, Local Zones perto de centros urbanos e Wavelength em redes de operadoras compatíveis.

**Recursos envolvidos:** Outposts no local do cliente; Local Zones próximas de cidades; Wavelength junto à rede de operadoras.

**Decisões que precisam ser tomadas:** Localidade, serviço disponível e infraestrutura/conectividade exigida.

**Outra situação comentada:** Requisito de manter computação no prédio: avalie Outposts; não confunda com região inteiramente nova.

**Por que não concluir mais do que isso:** Não oferece todo o catálogo em qualquer local; os três nomes têm status de escopo diferentes

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "A empresa precisa rodar serviços AWS no próprio datacenter."

**Resposta curta:** Outposts.

**Pergunta:** "Latência de um dígito de milissegundo numa cidade sem região AWS."

**Resposta curta:** Local Zones.

**Pergunta:** "Aplicação móvel 5G com ultrabaixa latência."

**Resposta curta:** Wavelength.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Outposts](https://aws.amazon.com/outposts/) · [Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) · [Wavelength](https://aws.amazon.com/wavelength/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
