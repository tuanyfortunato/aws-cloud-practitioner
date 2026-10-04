# IoT, robótica, satélite e visão computacional na borda (Device Defender, Monitron, Panorama, RoboMaker, Ground Station)

> **Categoria:** IoT, robótica e satélite · **Domínio:** — (fora da prova) · **Escopo:** Regional · **Lista oficial:** [fora do escopo](../../docs/00-guia-do-exame/escopo-oficial.md#-fora-do-escopo-lista-oficial-não-exaustiva)
>
> **Em uma frase:** serviços especializados para dispositivos, robôs, satélites e câmeras inteligentes — fora da prova, que só cobra o IoT Core.
>
> **Escopo oficial:** ❌ Fora do escopo — documentado só para referência · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> ❌ **Fora do escopo da CLF-C02.** Na prova, a única resposta de IoT é o **AWS IoT Core**.
> Documentados aqui apenas para referência. Veja também [IoT Core e Greengrass](../aplicacoes/iot-core-e-greengrass.md).

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

## 🔗 Documentação oficial

- [IoT Device Defender](https://aws.amazon.com/iot-device-defender/) · [Monitron](https://aws.amazon.com/monitron/) · [RoboMaker](https://aws.amazon.com/robomaker/) · [Ground Station](https://aws.amazon.com/ground-station/)
