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

## 1. A sequência de funcionamento

**Passo 1.** Prepare a aplicação para emitir dados de rastreamento nas partes que precisa observar.

**Passo 2.** Acompanhe o caminho de uma requisição e os tempos de cada segmento registrado.

**Passo 3.** Investigue a etapa problemática e valide a correção. Um rastreamento não observa automaticamente todo detalhe que não foi instrumentado.

## 2. Recursos e opções, com significado

### Conceitos

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

**X-Ray** (rastreia requisições entre serviços) × **CloudWatch** (métricas/logs) × **CloudTrail** (chamadas de API da conta).

## 4. Caso resolvido: ligando as peças

Ao consultar uma matrícula, a aplicação chama outro serviço e um banco. O rastreamento ajuda a localizar a etapa mais lenta.

**Aplicando a sequência à situação:**

**Etapa 1:** Prepare a aplicação para emitir dados de rastreamento nas partes que precisa observar.
**Etapa 2:** Acompanhe o caminho de uma requisição e os tempos de cada segmento registrado.
**Etapa 3:** Investigue a etapa problemática e valide a correção. Um rastreamento não observa automaticamente todo detalhe que não foi instrumentado.

**Resultado e responsabilidade:** X-Ray ajuda a acompanhar requisições em aplicações instrumentadas, reunindo rastreamentos e relações entre componentes.

**Recursos envolvidos:** Traces, segments, subsegments e mapa de serviços.

**Decisões que precisam ser tomadas:** Instrumentação, amostragem e envio autorizado.

**Outra situação comentada:** Latência entre API e banco: X-Ray; tendência de CPU: CloudWatch.

**Por que não concluir mais do que isso:** Sem instrumentação não há trace completo; não registra automaticamente toda requisição sem amostragem

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Encontrar qual microsserviço deixa a requisição lenta."

**Resposta curta:** X-Ray.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
