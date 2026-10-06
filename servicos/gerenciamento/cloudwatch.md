# Amazon CloudWatch

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Um sistema ficou lento ou falhou. A equipe precisa acompanhar seu comportamento e perceber problemas, em vez de esperar alguém reclamar.

**Como este serviço ajuda?** CloudWatch reúne recursos para métricas, logs e alarmes. Você observa dados do ambiente e define condições que devem gerar avisos ou ações integradas.

**Exemplo do dia a dia:** A escola acompanha uma métrica da aplicação e cria um alarme quando ela ultrapassa um limite definido. Logs ajudam a entender erros do programa.

**O que ele não resolve sozinho?** Nem todo dado é coletado automaticamente, e um alarme não corrige qualquer problema sozinho. Você precisa coletar os dados certos e configurar a resposta desejada.

**Primeiras palavras para entender:**

- **Métrica:** medida ao longo do tempo.
- **Log:** registro de acontecimentos.
- **Alarme:** condição monitorada que pode mudar de estado e acionar respostas.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Gerenciamento / observabilidade · **Domínio:** 2 e 3 · **Escopo:** Regional (dashboards e alarmes entre regiões/contas) · **Tópico do guia:** [2.7 Logs, monitoramento e auditoria](../../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)
>
> **Em uma frase:** monitoramento de **métricas, logs e alarmes** de recursos e aplicações AWS e on-premises.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Escolha quais medidas e registros ajudam a observar o problema da aplicação.

**Passo 2.** Configure coleta, visualizações e condições de alarme. Dados são acompanhados dentro dos períodos e critérios definidos.

**Passo 3.** Investigue mudanças e acione a resposta planejada. Um número isolado não explica a causa de toda falha.

## 2. Recursos e opções, com significado

### Componentes

**Metrics**

**Detalhe:** Séries temporais por *namespace* (ex.: `AWS/EC2`) e *dimensões* (ex.: InstanceId). Resolução padrão 1 min (EC2 básico: **5 min**); *high-resolution* até 1 s. Retenção de **15 meses** (agregadas).

**Custom metrics**

**Detalhe:** Enviadas pela aplicação ou pelo **CloudWatch agent** (memória, disco, processos).

**Alarms**

**Detalhe:** Estados **OK / ALARM / INSUFFICIENT_DATA**. Ações: **SNS**, **Auto Scaling**, **ações de EC2** (parar, encerrar, reiniciar, recuperar), Systems Manager. **Composite alarms** combinam vários. **Anomaly detection** cria faixas esperadas com ML.

**Billing alarm**

**Detalhe:** Alarme sobre a métrica *EstimatedCharges* (precisa ativar alertas de faturamento; métrica fica em **us-east-1**).

**Logs**

**Detalhe:** *Log groups* e *log streams*; **retenção configurável** (padrão: nunca expira); **metric filters** (transformar padrões de log em métricas); **subscription filters** (enviar a Lambda/Kinesis/OpenSearch); export para S3.

**Logs Insights**

**Detalhe:** Consultas interativas sobre logs. **Live Tail** acompanha em tempo real.

**Dashboards**

**Detalhe:** Painéis **globais** com métricas de várias regiões/contas.

**Synthetics**

**Detalhe:** *Canaries* que simulam usuários (testes de endpoints/fluxos).

**RUM**

**Detalhe:** Monitoramento de usuários reais (front-end web).

**Container / Lambda Insights, Application Signals**

**Detalhe:** Observabilidade de contêineres, funções e aplicações (APM).

**CloudWatch agent**

**Detalhe:** Instalado em EC2/on-premises para métricas do SO e envio de logs.

### Métricas padrão do EC2

✅ CPU, rede (bytes/pacotes), disco de instance store (ops/bytes), **status checks** (a cada **1 min**, mesmo no básico), créditos de CPU (T).

Monitoramento **detalhado**: todas as métricas a cada 1 min, pago por métrica.

❌ **Memória**, uso de **disco do sistema de arquivos**, processos → exigem o **agent**.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Nem todo dado é coletado automaticamente, e um alarme não corrige qualquer problema sozinho. Você precisa coletar os dados certos e configurar a resposta desejada.

### ⚠️ Não confundir

**CloudWatch** (desempenho: métricas/logs/alarmes) × **CloudTrail** (quem fez qual chamada de API) × **Config** (estado/histórico de configuração).

CloudWatch billing alarm × **AWS Budgets** (orçamentos mais completos, inclusive previsão).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Camada gratuita ✔️ (Always Free): métricas básicas, **10 métricas** (customizadas + detailed monitoring, somadas) e **10 métricas de alarme** de resolução padrão, além de cota de logs; depois por métrica customizada, alarme, GB de log ingerido/armazenado, consulta, dashboard, canary.

## 5. Caso resolvido: ligando as peças

O sistema ficou lento, e a equipe quer perceber o problema e investigar seu comportamento. A pergunta inicial é como ele funciona, não quem realizou uma ação administrativa.

A equipe coleta métricas pertinentes, registros da aplicação e cria um alarme com período e critério definidos. Um aumento de erros pode disparar uma notificação configurada. Logs ajudam a examinar o que o programa registrou durante a ocorrência.

O alarme não explica sozinho a causa nem aplica qualquer correção por padrão. Para investigar quem alterou um recurso, eventos CloudTrail podem ser necessários; para acompanhar propriedades e conformidade de configuração, Config atende outra parte da investigação.

**Recursos envolvidos:** Métricas, logs, alarmes e dashboards.

**Decisões que precisam ser tomadas:** Coleta, retenção, thresholds e ações.

**Outra situação comentada:** CPU acima da meta: métrica/alarme; quem mudou SG: CloudTrail.

**Por que não concluir mais do que isso:** Memória de EC2 não vem toda por padrão; alarme sem ação não remedia nada

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Alerta quando a CPU passar de 80%."

**Resposta curta:** Alarme do CloudWatch + SNS.

**Pergunta:** "Coletar memória usada pelo EC2."

**Resposta curta:** CloudWatch agent.

**Pergunta:** "Onde ver logs de aplicação?"

**Resposta curta:** CloudWatch Logs.

**Pergunta:** "Reiniciar automaticamente uma instância com falha de status check."

**Resposta curta:** Alarme com ação de EC2 (recover/reboot).

**Pergunta:** "Monitorar um site simulando usuários a cada 5 minutos."

**Resposta curta:** CloudWatch Synthetics.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
