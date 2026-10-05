# IoT, robótica, satélite e visão computacional na borda (Device Defender, Monitron, Panorama, RoboMaker, Ground Station)

> **Categoria:** IoT, robótica e satélite · **Domínio:** — (fora da prova) · **Escopo:** Regional · **Lista oficial:** [fora do escopo](../../docs/00-guia-do-exame/escopo-oficial.md#-fora-do-escopo-lista-oficial-não-exaustiva)
>
> **Em uma frase:** serviços especializados para dispositivos, robôs, satélites e câmeras inteligentes — fora da prova, que só cobra o IoT Core.
>
> **Escopo oficial:** ❌ Fora do escopo — documentado só para referência · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> ❌ **Fora do escopo da CLF-C02.** Na prova, a única resposta de IoT é o **AWS IoT Core**.
> Documentados aqui apenas para referência. Veja também [IoT Core e Greengrass](../aplicacoes/iot-core-e-greengrass.md).

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** são serviços **especializados** para dispositivos, robôs, satélites e câmeras inteligentes.

- ✅ **Escolha quando:** Só para referência — **não cai na prova**. Se aparecer como alternativa, provavelmente é distrator.
- 🚫 **Não é a resposta quando:** na prova, **IoT** → [IoT Core](../aplicacoes/iot-core-e-greengrass.md); **imagens** → Rekognition, em [serviços de IA prontos](../ia-ml/servicos-de-ia-prontos.md).
- 🎯 **Palavras do enunciado que apontam para ele:** Device Defender, Monitron, Panorama, RoboMaker e Ground Station aparecem, no máximo, como alternativas erradas.
<!-- didatico:fim -->

## AWS IoT Device Defender

- **Audita** a configuração de segurança de frotas de dispositivos IoT (certificados, políticas) e **detecta comportamento anômalo** (ex.: dispositivo enviando tráfego fora do padrão).
- Gera alertas e ações de mitigação (isolar o dispositivo, revogar certificado).

## Amazon Monitron

- 🔄 **Fechado a novos clientes** (data de encerramento não localizada).
- Solução de ponta a ponta para **monitorar equipamentos industriais**: sensores de vibração e temperatura, gateway e app com machine learning que avisa sobre falhas futuras (manutenção preditiva).

## AWS Panorama

- Appliance e SDK para rodar **visão computacional na borda**, usando câmeras IP já existentes (ex.: contagem de pessoas, inspeção de qualidade em linha de produção).
- 🔄 **Encerrado em 31/05/2026** (aplicações e dispositivos pararam de funcionar).

## Amazon Lookout for Metrics

- Detectava **anomalias em métricas de negócio** (vendas, receita) com ML.
- 🔄 Encerrado em 12/09/2025.

## AWS RoboMaker

- Serviço para **desenvolver, simular e testar aplicações de robótica** (ROS) em ambientes simulados na nuvem.
- 🔄 **Encerrado em 10/09/2025**; a alternativa indicada é o **AWS Batch** para simulações.

## AWS Ground Station

- **Estações terrestres de satélite como serviço**: controlar satélites e baixar dados deles, pagando por minuto, sem construir antenas próprias.
- Os dados podem ir direto para EC2 e S3 para processamento.

## ⚠️ Como isso aparece na prova

- "Conectar milhões de sensores à nuvem" → **IoT Core** (no escopo).
- "Detectar anomalias de segurança" → na CLF-C02, pense em **GuardDuty** (contas AWS), não Device Defender.
- "Reconhecer objetos em imagens" → **Rekognition** (no escopo), não Panorama.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Ferramentas especializadas de dispositivos, sensores, robótica e satélite |
| **O que você decide/configura?** | Produto, requisitos físicos e situação de disponibilidade |
| **Em que ordem as coisas acontecem?** | Avalie documentação e elegibilidade antes de qualquer adoção |
| **O que pode fazer, e em que condição?** | Atendem domínios específicos, diferentes de compute genérico |
| **O que não pode presumir?** | Estão fora do escopo; alguns serviços têm restrições/encerramento indicados na ficha |

**Caso comentado:** IoT Core conecta dispositivos no escopo; serviços desta família são contexto adicional.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [IoT Device Defender](https://aws.amazon.com/iot-device-defender/) · [Monitron](https://aws.amazon.com/monitron/) · [RoboMaker](https://aws.amazon.com/robomaker/) · [Ground Station](https://aws.amazon.com/ground-station/)
