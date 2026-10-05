# AWS X-Ray

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Um pedido passa por vários componentes e demora muito. A equipe precisa descobrir em qual parte do caminho o tempo foi gasto ou houve erro.

**Como este serviço ajuda?** X-Ray ajuda a acompanhar requisições em aplicações instrumentadas, reunindo rastreamentos e relações entre componentes.

**Exemplo do dia a dia:** Ao consultar uma matrícula, a aplicação chama outro serviço e um banco. O rastreamento ajuda a localizar a etapa mais lenta.

**O que ele não resolve sozinho?** Ele não coleta todos os detalhes sem preparação nem corrige a etapa lenta. A aplicação e suas integrações precisam fornecer dados de rastreamento compatíveis.

**Primeiras palavras para entender:**

- **Trace:** caminho de uma requisição.
- **Instrumentação:** preparação para emitir dados de observação.
- **Segmento:** parte registrada desse caminho.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Ferramentas de desenvolvedor / observabilidade · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.15 Ferramentas de desenvolvimento](../../docs/03-tecnologia-e-servicos/15-ferramentas-de-desenvolvimento.md)
>
> **Em uma frase:** **rastreamento distribuído** — acompanha cada requisição através dos microsserviços para achar gargalos e erros.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento


**Passo 1.** Prepare a aplicação para emitir dados de rastreamento nas partes que precisa observar.

**Passo 2.** Acompanhe o caminho de uma requisição e os tempos de cada segmento registrado.

**Passo 3.** Investigue a etapa problemática e valide a correção. Um rastreamento não observa automaticamente todo detalhe que não foi instrumentado.

## 2. Recursos e opções, com significado

### Conceitos

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **ECS:** O ECS coordena a execução de containers: pacotes com a aplicação e suas dependências.
- **Elastic Beanstalk:** O Elastic Beanstalk ajuda a implantar aplicações em plataformas compatíveis, provisionando e coordenando recursos AWS para esse ambiente.
- **API Gateway:** API Gateway ajuda a publicar e administrar APIs.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.
- **X-Ray:** X-Ray ajuda a acompanhar requisições em aplicações instrumentadas, reunindo rastreamentos e relações entre componentes.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.
- **HTTP:** Protocolo de pedidos e respostas usado na web. Uma URL e um método indicam a operação; HTTP sozinho não protege o conteúdo por criptografia.
- **trace:** Rastreamento do caminho de uma requisição em componentes instrumentados. Permite examinar etapas, mas depende dos dados emitidos pela aplicação.
- **instrumentação:** Preparação do software para emitir informações de observação. Sem os dados necessários, a ferramenta não consegue mostrar todos os detalhes da execução.
- **sampling:** Amostragem: observar parte das ocorrências. Uma amostra reduz volume, mas não deve ser tratada como o registro completo de cada pedido.
- **SDK:** SDK fornece bibliotecas para programas chamarem APIs; CLI fornece comandos de texto. As duas formas continuam exigindo identidade, autorização e configuração.
- **ADOT:** Distribuição AWS de OpenTelemetry para instrumentação e coleta de dados de observação compatíveis.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Item | Detalhe |
|---|---|
| **Trace** | Caminho completo de uma requisição. |
| **Segments / subsegments** | Tempo gasto em cada serviço e chamada (banco, HTTP, AWS SDK). |
| **Service map** | Mapa visual das dependências com latência e taxa de erro. |
| **Sampling** | Regras para registrar só uma amostra das requisições (controla custo). |
| **Instrumentação** | SDKs do X-Ray ou **OpenTelemetry (ADOT)**; integração nativa com Lambda, API Gateway, ECS, Elastic Beanstalk, App Runner. |
| **Integração** | Visualização no CloudWatch (Application Signals / Transaction Search). |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele não coleta todos os detalhes sem preparação nem corrige a etapa lenta. A aplicação e suas integrações precisam fornecer dados de rastreamento compatíveis.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **CloudTrail:** Registro de atividades e chamadas AWS compatíveis. Ajuda a analisar quem realizou uma operação, em vez de medir sozinho a velocidade da aplicação.


**X-Ray** (rastreia requisições entre serviços) × **CloudWatch** (métricas/logs) × **CloudTrail** (chamadas de API da conta).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

## 5. Caso resolvido: ligando as peças

Ao consultar uma matrícula, a aplicação chama outro serviço e um banco. O rastreamento ajuda a localizar a etapa mais lenta.

**Aplicando a sequência à situação:**

**Etapa 1:** Prepare a aplicação para emitir dados de rastreamento nas partes que precisa observar.
**Etapa 2:** Acompanhe o caminho de uma requisição e os tempos de cada segmento registrado.
**Etapa 3:** Investigue a etapa problemática e valide a correção. Um rastreamento não observa automaticamente todo detalhe que não foi instrumentado.

**Resultado e responsabilidade:** X-Ray ajuda a acompanhar requisições em aplicações instrumentadas, reunindo rastreamentos e relações entre componentes.

**Recursos envolvidos:** Traces, segments, subsegments e mapa de serviços.

**Decisões que precisam ser tomadas:** Instrumentação, amostragem e envio autorizado.

**Antes de ler este trecho:**

- **CPU:** CPU é o processador que executa instruções. vCPU é a unidade de processamento virtual apresentada ao ambiente. Mais processamento não resolve automaticamente falta de memória ou de velocidade do disco.


**Outra situação comentada:** Latência entre API e banco: X-Ray; tendência de CPU: CloudWatch.

**Por que não concluir mais do que isso:** Sem instrumentação não há trace completo; não registra automaticamente toda requisição sem amostragem

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Um pedido passa por vários componentes e demora muito. A equipe precisa descobrir em qual parte do caminho o tempo foi gasto ou houve erro.

**2. O que a solução fornece?**

X-Ray ajuda a acompanhar requisições em aplicações instrumentadas, reunindo rastreamentos e relações entre componentes.

**3. Que conclusão seria incorreta?**

Ele não coleta todos os detalhes sem preparação nem corrige a etapa lenta. A aplicação e suas integrações precisam fornecer dados de rastreamento compatíveis.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Encontrar qual microsserviço deixa a requisição lenta."

**Resposta curta:** X-Ray.


**Fundamento explicado no capítulo:** "Encontrar qual microsserviço deixa a requisição lenta." → X-Ray.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
