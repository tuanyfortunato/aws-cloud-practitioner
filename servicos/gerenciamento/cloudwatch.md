# Amazon CloudWatch

> **Categoria:** Gerenciamento / observabilidade · **Domínio:** 2 e 3 · **Escopo:** Regional (dashboards e alarmes entre regiões/contas) · **Tópico do guia:** [2.7 Logs, monitoramento e auditoria](../../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)
>
> **Em uma frase:** monitoramento de **métricas, logs e alarmes** de recursos e aplicações AWS e on-premises.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é o **painel do carro**: mostra os indicadores (métricas), guarda o diário de bordo (logs) e acende a luz de alerta (alarmes).

- ✅ **Escolha quando:** precisa **monitorar desempenho**, coletar **logs** e criar **alarmes**.
- 🚫 **Não é a resposta quando:** quer saber **quem fez** uma ação → [CloudTrail](cloudtrail.md); quer o **histórico de configuração** → [Config](config.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "métricas", "alarme", "CPU acima de 80%", "logs da aplicação", "dashboard".
<!-- didatico:fim -->

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

## 🔗 Documentação oficial

- [Guia do CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
