<!-- autoral -->

# Amazon CloudWatch

> **Categoria:** Gerenciamento e observabilidade · **Domínio:** 2 e 3 · **Abrangência:** Regional (painéis e alarmes podem reunir Regiões e contas) · **Ficha:** núcleo
>
> **Em uma frase:** monitora recursos e aplicações com métricas, alarmes, painéis e logs, para ver como estão funcionando e agir quando algo passa do limite.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.7 Logs, monitoramento e auditoria](../../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

Na manhã da matrícula, o portal da escola ficou lento e ninguém soube dizer por quê. O técnico só descobriu o pico de CPU horas depois, entrando na instância. E ninguém foi avisado quando a conta do mês passou do orçamento.

O **CloudWatch** acompanha o funcionamento em tempo real. Os serviços da AWS enviam **métricas** sem custo, como o uso de CPU de uma instância EC2. Um **alarme** observa uma métrica e age quando ela passa de um limite por um período: avisa por um tópico do SNS, para ou reinicia a instância, ou aciona o Auto Scaling. O **CloudWatch Logs** reúne os registros de sistemas e aplicações num só lugar, e os **painéis** mostram tudo numa tela.

O limite: o CloudWatch mostra como os recursos estão funcionando, não quem fez cada mudança (isso é o [CloudTrail](cloudtrail.md)) nem como a configuração estava antes (isso é o [Config](config.md)). E algumas medidas de dentro do sistema operacional, como a memória usada numa instância EC2, só chegam com o **agente do CloudWatch** instalado.

## Como funciona

1. Os serviços da AWS enviam métricas automaticamente; o agente do CloudWatch coleta métricas e logs de dentro das instâncias.
2. Você cria alarmes com um limite e uma ação, por exemplo "CPU acima de 80% por 5 minutos avisa a equipe".
3. Os logs chegam aos grupos de log, onde ficam guardados pelo tempo definido e podem ser consultados com o Logs Insights.
4. Painéis reúnem métricas e alarmes; o alarme de cobrança avisa quando os gastos estimados passam de um valor.

## Opções principais

| Peça | O que faz | Exemplo na escola |
|---|---|---|
| Métricas | Medidas numéricas ao longo do tempo | CPU do servidor do portal |
| Alarmes | Agem quando a métrica passa do limite | Avisar a equipe e criar mais instâncias |
| CloudWatch Logs | Centraliza e guarda os registros | Erros da aplicação de matrícula |
| Logs Insights | Consulta os logs com uma linguagem própria | Quantos erros por hora na matrícula |
| Painéis | Uma tela com métricas e alarmes | Painel do dia da matrícula |
| Agente do CloudWatch | Coleta memória, disco e logs de dentro da instância | Memória usada no servidor |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Monitoramento básico do EC2 | Métricas a cada 5 minutos, sem custo | 06/10/2026 |
| Monitoramento detalhado do EC2 | Métricas a cada 1 minuto, cobrado | 06/10/2026 |
| Memória e espaço em disco do EC2 | Só com o agente do CloudWatch | 06/10/2026 |
| Métrica de cobrança | Região Leste dos EUA (Norte da Virgínia) | 06/10/2026 |
| Retenção padrão do CloudWatch Logs | Indefinida, ajustável por grupo de log | 06/10/2026 |
| Nível gratuito | 10 métricas, 10 alarmes, 3 painéis e 5 GB de logs por mês | 06/10/2026 |

## Como é cobrado

As métricas que os serviços enviam por padrão não custam nada. Acima do nível gratuito, paga-se por métrica personalizada ou de monitoramento detalhado, por alarme, por painel, pelos logs ingeridos e guardados e pelos dados lidos nas consultas.

## Não confundir com

| Serviço | Diferença para o CloudWatch | Pista no enunciado |
|---|---|---|
| [AWS CloudTrail](cloudtrail.md) | Registra quem fez cada chamada de API | "Quem apagou", "quem alterou" |
| [AWS Config](config.md) | Guarda o histórico de configuração | "Como estava configurado" |
| [AWS Health Dashboard](health-dashboard.md) | Eventos do lado da AWS | "O problema é da AWS?" |
| [AWS Budgets](../custos/budgets.md) | Orçamentos e alertas de custo e uso | "Orçamento mensal", "previsão de gasto" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
- [Alarmes do CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html)
- [Monitoramento detalhado do EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-detailed-monitoring.html)
- [Métricas coletadas pelo agente](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/metrics-collected-by-CloudWatch-agent.html)
- [Alarme de cobrança](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html)
- [Retenção dos logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html)
- [Preços do Amazon CloudWatch](https://aws.amazon.com/cloudwatch/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
