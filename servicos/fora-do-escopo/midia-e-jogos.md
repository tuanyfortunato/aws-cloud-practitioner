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

## AWS Elemental Media Services

Família de serviços de vídeo profissional (broadcast e streaming).

| Serviço | O que faz | Exemplo |
|---|---|---|
| **AWS Elemental MediaConvert** | Transcodifica arquivos de vídeo (**VOD**) para vários formatos e resoluções | Converter vídeos enviados pelos usuários para HLS e DASH |
| **AWS Elemental MediaLive** | Codifica vídeo **ao vivo** em tempo real para streaming | Transmitir um evento esportivo ao vivo |
| **AWS Elemental MediaPackage** | Prepara e protege (DRM) streams para entrega em vários formatos; time-shift e DVR | Entregar o canal ao vivo para celulares, TVs e navegadores |
| **AWS Elemental MediaConnect** | Transporte confiável e seguro de vídeo ao vivo entre locais e para a nuvem | Levar o sinal do estádio para a AWS |
| **AWS Elemental MediaTailor** | Inserção de anúncios no servidor (SSAI) e montagem de canais lineares | Anúncios personalizados por espectador |
| **AWS Elemental MediaStore** | Armazenamento otimizado para mídia como origem de vídeo (🔄 **encerrado em 13/11/2025**) | Origem de baixa latência para vídeo ao vivo |
| **AWS Elemental Appliances and Software** | Codificadores e software Elemental para rodar on-premises | Emissoras com equipamento próprio |

## Amazon Interactive Video Service (IVS)

- Streaming ao vivo **gerenciado e de baixa latência**, com a mesma tecnologia da Twitch; inclui chat e recursos interativos.
- Uso: lives em aplicativos, aulas ao vivo, leilões e e-commerce ao vivo.

## Amazon Elastic Transcoder

- Serviço de transcodificação de arquivos de mídia armazenados no S3.
- 🔄 **Encerrado em 13/11/2025**; a alternativa indicada é o **MediaConvert**.

## Amazon GameLift

- Hospedagem gerenciada de **servidores dedicados para jogos multiplayer**: escalonamento, matchmaking e uso de instâncias Spot (GameLift Servers), além de streaming de jogos (GameLift Streams).

## Amazon Lumberyard

- Antigo **motor de jogos** gratuito da AWS. 🔄 **Não é mais oferecido**; foi descontinuado e deu origem ao projeto open source **Open 3D Engine (O3DE)**.

## ⚠️ Como isso aparece na prova

- "Distribuir vídeos com baixa latência para usuários globais" → a resposta da CLF-C02 é **CloudFront** (no escopo), não Elemental.
- "Armazenar vídeos" → **S3**; "processar vídeo quando chega ao bucket" → **Lambda/S3 events** no escopo da prova.
- "Analisar rostos e objetos em vídeo" → **Rekognition** (no escopo).
- "Jogo multiplayer com IPs fixos globais" → **Global Accelerator** (no escopo), não GameLift.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Serviços de mídia/transmissão e infraestrutura especializada de jogos |
| **O que você decide/configura?** | Tipo de mídia ou servidor de jogo e disponibilidade atual |
| **Em que ordem as coisas acontecem?** | Consulte a oferta específica quando houver requisito real de produção |
| **O que pode fazer, e em que condição?** | Famílias têm funções distintas de conversão, distribuição ou hospedagem |
| **O que não pode presumir?** | Estão fora do escopo; não memorize configurações como prioridade da CLF-C02 |

**Caso comentado:** Vídeo ao vivo não é sinônimo de site estático; conheça a diferença, mas estude primeiro serviços incluídos.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [AWS Elemental](https://aws.amazon.com/media-services/) · [Amazon IVS](https://aws.amazon.com/ivs/) · [Amazon GameLift](https://aws.amazon.com/gamelift/) · [Open 3D Engine](https://o3de.org/)
