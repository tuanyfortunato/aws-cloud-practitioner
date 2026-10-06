# Serviços de mídia e jogos (Elemental, IVS, Elastic Transcoder, GameLift, Lumberyard)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Vídeo ao vivo, processamento de mídia e sessões de jogos exigem funções específicas, além de simplesmente guardar um arquivo ou executar uma página.

**Como este serviço ajuda?** Esta ficha compara produtos para preparar e distribuir mídia e para operar jogos. Cada produto cobre uma parte do processo, conforme sua oferta.

**Exemplo do dia a dia:** Compare preparar um vídeo em vários formatos, transmitir uma sessão ao vivo e hospedar partidas. São problemas diferentes, mesmo que todos envolvam conteúdo digital.

**O que ele não resolve sozinho?** Os produtos não são intercambiáveis; há ofertas antigas no material. A ficha serve para referência fora do escopo indicado, e não para decorar alternativas como respostas universais.

**Primeiras palavras para entender:**

- **Transcodificação:** conversão de formato ou qualidade de mídia.
- **Streaming:** transmissão contínua.
- **Sessão de jogo:** execução compartilhada de uma partida.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Mídia e Game Tech · **Domínio:** — (fora da prova) · **Escopo:** Regional · **Lista oficial:** [fora do escopo](../../docs/00-guia-do-exame/escopo-oficial.md#-fora-do-escopo-lista-oficial-não-exaustiva)
>
> **Em uma frase:** serviços para processar e transmitir vídeo e para hospedar jogos — úteis para conhecer, mas a prova os usa só como distratores.
>
> **Escopo oficial:** ❌ Fora do escopo — documentado só para referência · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> ❌ **Fora do escopo da CLF-C02.** Todos os serviços desta ficha estão declarados fora do escopo na lista oficial.
> Se aparecerem como alternativa, quase sempre são **distratores**. Documentados aqui apenas para referência.

## 1. A sequência de funcionamento

**Passo 1.** Separe preparação de mídia, transmissão ao vivo e hospedagem de partidas.

**Passo 2.** Identifique o produto associado à etapa específica e confira sua oferta e suas restrições.

**Passo 3.** Compare o resultado com a necessidade. Esta ficha é de referência e não uma recomendação de uso de ofertas antigas.

## 2. Recursos e opções, com significado

### AWS Elemental Media Services

**Antes de ler este trecho:**

- **streaming:** Fluxo contínuo de dados ou mídia. É diferente de esperar um arquivo completo antes de iniciar o trabalho.

Família de serviços de vídeo profissional (broadcast e streaming).

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **servidor:** Computador que atende pedidos de outros computadores. Um servidor web, por exemplo, responde aos pedidos enviados pelo navegador.
- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.
- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.
- **origem:** Local de onde uma distribuição obtém conteúdo, como um servidor ou bucket. Uma cópia em cache não elimina toda necessidade de acessar a origem.
- **evento:** Informação sobre algo que aconteceu. Uma regra pode encaminhar o evento; outro componente realiza a ação de negócio.
- **HLS / DASH:** Formatos e tecnologias de distribuição adaptativa de vídeo. Permitem alternativas de qualidade e entrega conforme o ecossistema compatível.
- **VOD / DVR:** Vídeo sob demanda e funções de gravação ou acesso temporal de transmissão. São experiências diferentes de simples armazenamento de arquivos.
- **DRM / SSAI:** Proteção de direitos de mídia e inserção de publicidade no servidor. São funções especializadas da distribuição de conteúdo, não controles IAM genéricos.

| Serviço | O que faz | Exemplo |
|---|---|---|
| **AWS Elemental MediaConvert** | Transcodifica arquivos de vídeo (**VOD**) para vários formatos e resoluções | Converter vídeos enviados pelos usuários para HLS e DASH |
| **AWS Elemental MediaLive** | Codifica vídeo **ao vivo** em tempo real para streaming | Transmitir um evento esportivo ao vivo |
| **AWS Elemental MediaPackage** | Prepara e protege (DRM) streams para entrega em vários formatos; time-shift e DVR | Entregar o canal ao vivo para celulares, TVs e navegadores |
| **AWS Elemental MediaConnect** | Transporte confiável e seguro de vídeo ao vivo entre locais e para a nuvem | Levar o sinal do estádio para a AWS |
| **AWS Elemental MediaTailor** | Inserção de anúncios no servidor (SSAI) e montagem de canais lineares | Anúncios personalizados por espectador |
| **AWS Elemental MediaStore** | Armazenamento otimizado para mídia como origem de vídeo (🔄 **encerrado em 13/11/2025**) | Origem de baixa latência para vídeo ao vivo |
| **AWS Elemental Appliances and Software** | Codificadores e software Elemental para rodar on-premises | Emissoras com equipamento próprio |

### Amazon Interactive Video Service (IVS)

**Antes de ler este trecho:**

- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.

Streaming ao vivo **gerenciado e de baixa latência**, com a mesma tecnologia da Twitch; inclui chat e recursos interativos.

Uso: lives em aplicativos, aulas ao vivo, leilões e e-commerce ao vivo.

### Amazon Elastic Transcoder

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.

Serviço de transcodificação de arquivos de mídia armazenados no S3.

🔄 **Encerrado em 13/11/2025**; a alternativa indicada é o **MediaConvert**.

### Amazon GameLift

Hospedagem gerenciada de **servidores dedicados para jogos multiplayer**: escalonamento, matchmaking e uso de instâncias Spot (GameLift Servers), além de streaming de jogos (GameLift Streams).

### Amazon Lumberyard

**Antes de ler este trecho:**

- **O3DE:** Motor de desenvolvimento 3D. Desenvolver o conteúdo e operar os recursos necessários são trabalhos diferentes.

Antigo **motor de jogos** gratuito da AWS. 🔄 **Não é mais oferecido**; foi descontinuado e deu origem ao projeto open source **Open 3D Engine (O3DE)**.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Os produtos não são intercambiáveis; há ofertas antigas no material. A ficha serve para referência fora do escopo indicado, e não para decorar alternativas como respostas universais.

### ⚠️ Como isso aparece na prova

**Antes de ler este trecho:**

- **CloudFront:** CloudFront distribui conteúdo por uma rede de pontos de presença.

"Distribuir vídeos com baixa latência para usuários globais" → a resposta da CLF-C02 é **CloudFront** (no escopo), não Elemental.

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **bucket:** Recipiente que organiza objetos no S3. A aplicação usa o bucket e a identificação do objeto para pedir operações autorizadas.

"Armazenar vídeos" → **S3**; "processar vídeo quando chega ao bucket" → **Lambda/S3 events** no escopo da prova.

"Analisar rostos e objetos em vídeo" → **Rekognition** (no escopo).

**Antes de ler este trecho:**

- **Global Accelerator:** Global Accelerator usa a rede global da AWS para encaminhar tráfego a destinos compatíveis, considerando configuração e saúde desses destinos.
- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.

"Jogo multiplayer com IPs fixos globais" → **Global Accelerator** (no escopo), não GameLift.

## 4. Caso resolvido: ligando as peças

Compare preparar um vídeo em vários formatos, transmitir uma sessão ao vivo e hospedar partidas. São problemas diferentes, mesmo que todos envolvam conteúdo digital.

**Aplicando a sequência à situação:**

**Etapa 1:** Separe preparação de mídia, transmissão ao vivo e hospedagem de partidas.
**Etapa 2:** Identifique o produto associado à etapa específica e confira sua oferta e suas restrições.
**Etapa 3:** Compare o resultado com a necessidade. Esta ficha é de referência e não uma recomendação de uso de ofertas antigas.

**Resultado e responsabilidade:** Esta ficha compara produtos para preparar e distribuir mídia e para operar jogos. Cada produto cobre uma parte do processo, conforme sua oferta.

**Recursos envolvidos:** Serviços de mídia/transmissão e infraestrutura especializada de jogos.

**Decisões que precisam ser tomadas:** Tipo de mídia ou servidor de jogo e disponibilidade atual.

**Antes de ler este trecho:**

- **site estático:** Conteúdo entregue como arquivos, sem executar ali toda uma aplicação de processamento de negócio. Pode integrar-se a outros serviços para funções adicionais.

**Outra situação comentada:** Vídeo ao vivo não é sinônimo de site estático; conheça a diferença, mas estude primeiro serviços incluídos.

**Por que não concluir mais do que isso:** Estão fora do escopo; não memorize configurações como prioridade da CLF-C02

## 5. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [AWS Elemental](https://aws.amazon.com/media-services/) · [Amazon IVS](https://aws.amazon.com/ivs/) · [Amazon GameLift](https://aws.amazon.com/gamelift/) · [Open 3D Engine](https://o3de.org/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
