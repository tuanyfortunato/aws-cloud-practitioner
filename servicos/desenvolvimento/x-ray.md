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

## Conceitos

| Item | Detalhe |
|---|---|
| **Trace** | Caminho completo de uma requisição. |
| **Segments / subsegments** | Tempo gasto em cada serviço e chamada (banco, HTTP, AWS SDK). |
| **Service map** | Mapa visual das dependências com latência e taxa de erro. |
| **Sampling** | Regras para registrar só uma amostra das requisições (controla custo). |
| **Instrumentação** | SDKs do X-Ray ou **OpenTelemetry (ADOT)**; integração nativa com Lambda, API Gateway, ECS, Elastic Beanstalk, App Runner. |
| **Integração** | Visualização no CloudWatch (Application Signals / Transaction Search). |

## ⚠️ Não confundir

- **X-Ray** (rastreia requisições entre serviços) × **CloudWatch** (métricas/logs) × **CloudTrail** (chamadas de API da conta).

## ❓ Perguntas típicas

- "Encontrar qual microsserviço deixa a requisição lenta." → X-Ray.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Traces, segments, subsegments e mapa de serviços |
| **O que você decide/configura?** | Instrumentação, amostragem e envio autorizado |
| **Em que ordem as coisas acontecem?** | Requisições instrumentadas produzem traces entre componentes |
| **O que pode fazer, e em que condição?** | Ajuda localizar latência e erros no caminho distribuído |
| **O que não pode presumir?** | Sem instrumentação não há trace completo; não registra automaticamente toda requisição sem amostragem |

**Caso comentado:** Latência entre API e banco: X-Ray; tendência de CPU: CloudWatch.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
