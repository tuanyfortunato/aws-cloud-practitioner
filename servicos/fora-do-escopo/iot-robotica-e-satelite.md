# IoT, robótica, satélite e visão computacional na borda (Device Defender, Monitron, Panorama, RoboMaker, Ground Station)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Monitorar dispositivos, operar robôs ou comunicar-se com satélites são tarefas especializadas que não se resumem a hospedar uma aplicação web.

**Como este serviço ajuda?** A ficha reúne serviços associados a essas áreas e explica o papel de cada um, com observações sobre suas ofertas.

**Exemplo do dia a dia:** Uma equipe pode precisar avaliar a segurança de dispositivos; outra pode precisar de comunicação com satélite. A escolha depende da tarefa específica.

**O que ele não resolve sozinho?** Não trate a lista como um pacote único nem presuma que toda oferta continua disponível. O conteúdo é de referência fora do escopo e deve ser lido com seu status.

**Primeiras palavras para entender:**

- **Dispositivo:** equipamento conectado ou monitorado.
- **Borda:** local próximo da origem dos dados.
- **Telemetria:** informações enviadas por equipamentos.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** IoT, robótica e satélite · **Domínio:** — (fora da prova) · **Escopo:** Regional · **Lista oficial:** [fora do escopo](../../docs/00-guia-do-exame/escopo-oficial.md#-fora-do-escopo-lista-oficial-não-exaustiva)
>
> **Em uma frase:** serviços especializados para dispositivos, robôs, satélites e câmeras inteligentes — fora da prova, que só cobra o IoT Core.
>
> **Escopo oficial:** ❌ Fora do escopo — documentado só para referência · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> ❌ **Fora do escopo da CLF-C02.** Na prova, a única resposta de IoT é o **AWS IoT Core**.
> Documentados aqui apenas para referência. Veja também [IoT Core e Greengrass](../aplicacoes/iot-core-e-greengrass.md).

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento


**Passo 1.** Separe conexão de dispositivos, monitoramento físico, robótica e comunicação com satélites.

**Passo 2.** Leia o papel do produto específico e seus requisitos físicos e comerciais.

**Passo 3.** Confira a disponibilidade e o resultado esperado. A categoria não representa um único serviço intercambiável.

## 2. Recursos e opções, com significado

### AWS IoT Device Defender

**Antes de ler este trecho:**

- **IoT:** Dispositivos físicos conectados que enviam informações ou recebem comandos. Conexão não substitui autenticação, software e análise dos dados.
- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.


**Audita** a configuração de segurança de frotas de dispositivos IoT (certificados, políticas) e **detecta comportamento anômalo** (ex.: dispositivo enviando tráfego fora do padrão).


Gera alertas e ações de mitigação (isolar o dispositivo, revogar certificado).

### Amazon Monitron

🔄 **Fechado a novos clientes** (data de encerramento não localizada).

**Antes de ler este trecho:**

- **machine learning:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.


Solução de ponta a ponta para **monitorar equipamentos industriais**: sensores de vibração e temperatura, gateway e app com machine learning que avisa sobre falhas futuras (manutenção preditiva).

### AWS Panorama

**Antes de ler este trecho:**

- **IP:** Endereços usados para identificar interfaces e destinos na rede. IPv4 e IPv6 são versões diferentes; ter um endereço não concede permissão nem garante uma rota.
- **SDK:** SDK fornece bibliotecas para programas chamarem APIs; CLI fornece comandos de texto. As duas formas continuam exigindo identidade, autorização e configuração.


Appliance e SDK para rodar **visão computacional na borda**, usando câmeras IP já existentes (ex.: contagem de pessoas, inspeção de qualidade em linha de produção).


🔄 **Encerrado em 31/05/2026** (aplicações e dispositivos pararam de funcionar).

### Amazon Lookout for Metrics

Detectava **anomalias em métricas de negócio** (vendas, receita) com ML.


🔄 Encerrado em 12/09/2025.

### AWS RoboMaker

**Antes de ler este trecho:**

- **ROS:** Ecossistema de software para robótica. Não é o sistema operacional de qualquer servidor AWS nem uma ferramenta geral de migração.


Serviço para **desenvolver, simular e testar aplicações de robótica** (ROS) em ambientes simulados na nuvem.

**Antes de ler este trecho:**

- **AWS Batch / Batch:** O AWS Batch organiza trabalhos em filas e fornece capacidade de computação para executá-los conforme as configurações.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.


🔄 **Encerrado em 10/09/2025**; a alternativa indicada é o **AWS Batch** para simulações.

### AWS Ground Station

**Antes de ler este trecho:**

- **minuto:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.


**Estações terrestres de satélite como serviço**: controlar satélites e baixar dados deles, pagando por minuto, sem construir antenas próprias.

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.


Os dados podem ir direto para EC2 e S3 para processamento.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Não trate a lista como um pacote único nem presuma que toda oferta continua disponível. O conteúdo é de referência fora do escopo e deve ser lido com seu status.

### ⚠️ Como isso aparece na prova

"Conectar milhões de sensores à nuvem" → **IoT Core** (no escopo).

**Antes de ler este trecho:**

- **GuardDuty:** GuardDuty analisa fontes de dados compatíveis para detectar possíveis ameaças e produzir achados de segurança.


"Detectar anomalias de segurança" → na CLF-C02, pense em **GuardDuty** (contas AWS), não Device Defender.


"Reconhecer objetos em imagens" → **Rekognition** (no escopo), não Panorama.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

## 5. Caso resolvido: ligando as peças

Uma equipe pode precisar avaliar a segurança de dispositivos; outra pode precisar de comunicação com satélite. A escolha depende da tarefa específica.

**Aplicando a sequência à situação:**

**Etapa 1:** Separe conexão de dispositivos, monitoramento físico, robótica e comunicação com satélites.
**Etapa 2:** Leia o papel do produto específico e seus requisitos físicos e comerciais.
**Etapa 3:** Confira a disponibilidade e o resultado esperado. A categoria não representa um único serviço intercambiável.

**Resultado e responsabilidade:** A ficha reúne serviços associados a essas áreas e explica o papel de cada um, com observações sobre suas ofertas.

**Recursos envolvidos:** Ferramentas especializadas de dispositivos, sensores, robótica e satélite.

**Decisões que precisam ser tomadas:** Produto, requisitos físicos e situação de disponibilidade.


**Outra situação comentada:** IoT Core conecta dispositivos no escopo; serviços desta família são contexto adicional.

**Por que não concluir mais do que isso:** Estão fora do escopo; alguns serviços têm restrições/encerramento indicados na ficha

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Monitorar dispositivos, operar robôs ou comunicar-se com satélites são tarefas especializadas que não se resumem a hospedar uma aplicação web.

**2. O que a solução fornece?**

A ficha reúne serviços associados a essas áreas e explica o papel de cada um, com observações sobre suas ofertas.

**3. Que conclusão seria incorreta?**

Não trate a lista como um pacote único nem presuma que toda oferta continua disponível. O conteúdo é de referência fora do escopo e deve ser lido com seu status.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [IoT Device Defender](https://aws.amazon.com/iot-device-defender/) · [Monitron](https://aws.amazon.com/monitron/) · [RoboMaker](https://aws.amazon.com/robomaker/) · [Ground Station](https://aws.amazon.com/ground-station/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
