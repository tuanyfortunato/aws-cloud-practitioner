# Serviços de mídia e jogos (Elemental, IVS, Elastic Transcoder, GameLift, Lumberyard)

> **Categoria:** Mídia e Game Tech · **Domínio:** — (fora da prova) · **Escopo:** Regional · **Lista oficial:** [fora do escopo](../../docs/00-guia-do-exame/escopo-oficial.md#-fora-do-escopo-lista-oficial-não-exaustiva)
>
> **Em uma frase:** serviços para processar e transmitir vídeo e para hospedar jogos — úteis para conhecer, mas a prova os usa só como distratores.
>
> **Escopo oficial:** ❌ Fora do escopo — documentado só para referência · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> ❌ **Fora do escopo da CLF-C02.** Todos os serviços desta ficha estão declarados fora do escopo na lista oficial.
> Se aparecerem como alternativa, quase sempre são **distratores**. Documentados aqui apenas para referência.

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** são os serviços de **TV e games** da AWS: processar vídeo, transmitir ao vivo e hospedar jogos.

- ✅ **Escolha quando:** Só para referência — **não cai na prova**. Se aparecer como alternativa, provavelmente é distrator.
- 🚫 **Não é a resposta quando:** na prova, **entregar vídeo com baixa latência** → [CloudFront](../redes/cloudfront.md); **jogo com IPs fixos globais** → [Global Accelerator](../redes/global-accelerator.md).
- 🎯 **Palavras do enunciado que apontam para ele:** Elemental, IVS e GameLift aparecem, no máximo, como alternativas erradas.
<!-- didatico:fim -->

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

## 🔗 Documentação oficial

- [AWS Elemental](https://aws.amazon.com/media-services/) · [Amazon IVS](https://aws.amazon.com/ivs/) · [Amazon GameLift](https://aws.amazon.com/gamelift/) · [Open 3D Engine](https://o3de.org/)
