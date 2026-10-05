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

## Componentes

| Componente | Detalhe |
|---|---|
| **Metrics** | Séries temporais por *namespace* (ex.: `AWS/EC2`) e *dimensões* (ex.: InstanceId). Resolução padrão 1 min (EC2 básico: **5 min**); *high-resolution* até 1 s. Retenção de **15 meses** (agregadas). |
| **Custom metrics** | Enviadas pela aplicação ou pelo **CloudWatch agent** (memória, disco, processos). |
| **Alarms** | Estados **OK / ALARM / INSUFFICIENT_DATA**. Ações: **SNS**, **Auto Scaling**, **ações de EC2** (parar, encerrar, reiniciar, recuperar), Systems Manager. **Composite alarms** combinam vários. **Anomaly detection** cria faixas esperadas com ML. |
| **Billing alarm** | Alarme sobre a métrica *EstimatedCharges* (precisa ativar alertas de faturamento; métrica fica em **us-east-1**). |
| **Logs** | *Log groups* e *log streams*; **retenção configurável** (padrão: nunca expira); **metric filters** (transformar padrões de log em métricas); **subscription filters** (enviar a Lambda/Kinesis/OpenSearch); export para S3. |
| **Logs Insights** | Consultas interativas sobre logs. **Live Tail** acompanha em tempo real. |
| **Dashboards** | Painéis **globais** com métricas de várias regiões/contas. |
| **Synthetics** | *Canaries* que simulam usuários (testes de endpoints/fluxos). |
| **RUM** | Monitoramento de usuários reais (front-end web). |
| **Container / Lambda Insights, Application Signals** | Observabilidade de contêineres, funções e aplicações (APM). |
| **CloudWatch agent** | Instalado em EC2/on-premises para métricas do SO e envio de logs. |

## Métricas padrão do EC2

- ✅ CPU, rede (bytes/pacotes), disco de instance store (ops/bytes), **status checks** (a cada **1 min**, mesmo no básico), créditos de CPU (T).
- Monitoramento **detalhado**: todas as métricas a cada 1 min, pago por métrica.
- ❌ **Memória**, uso de **disco do sistema de arquivos**, processos → exigem o **agent**.

## Cobrança

- Camada gratuita ✔️ (Always Free): métricas básicas, **10 métricas** (customizadas + detailed monitoring, somadas) e **10 métricas de alarme** de resolução padrão, além de cota de logs; depois por métrica customizada, alarme, GB de log ingerido/armazenado, consulta, dashboard, canary.

## ⚠️ Não confundir

- **CloudWatch** (desempenho: métricas/logs/alarmes) × **CloudTrail** (quem fez qual chamada de API) × **Config** (estado/histórico de configuração).
- CloudWatch billing alarm × **AWS Budgets** (orçamentos mais completos, inclusive previsão).

## ❓ Perguntas típicas

- "Alerta quando a CPU passar de 80%." → Alarme do CloudWatch + SNS.
- "Coletar memória usada pelo EC2." → CloudWatch agent.
- "Onde ver logs de aplicação?" → CloudWatch Logs.
- "Reiniciar automaticamente uma instância com falha de status check." → Alarme com ação de EC2 (recover/reboot).
- "Monitorar um site simulando usuários a cada 5 minutos." → CloudWatch Synthetics.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Métricas, logs, alarmes e dashboards |
| **O que você decide/configura?** | Coleta, retenção, thresholds e ações |
| **Em que ordem as coisas acontecem?** | Recurso/agente envia dados; alarme avalia condição e pode acionar integração |
| **O que pode fazer, e em que condição?** | Observa saúde operacional e tendência |
| **O que não pode presumir?** | Memória de EC2 não vem toda por padrão; alarme sem ação não remedia nada |

**Caso comentado:** CPU acima da meta: métrica/alarme; quem mudou SG: CloudTrail.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
