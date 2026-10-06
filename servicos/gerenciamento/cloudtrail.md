<!-- autoral -->

# AWS CloudTrail

> **Categoria:** Gerenciamento e auditoria · **Domínio:** 2 · **Abrangência:** Regional (trilhas podem cobrir todas as Regiões e a organização) · **Ficha:** núcleo
>
> **Em uma frase:** registra as ações feitas na conta como eventos, dizendo quem fez o quê, quando, de onde e em qual recurso.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.7 Logs, monitoramento e auditoria](../../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

Na segunda-feira da matrícula, a pasta de documentos dos pais apareceu aberta para a internet. A diretora quer saber quem mudou a política do bucket e quando.

Tudo na AWS é feito por chamadas de API, pelo console, pela linha de comando ou por código. O **CloudTrail** registra essas chamadas como **eventos**: identidade, ação, horário, endereço de origem e recurso. Ele já vem ativo em toda conta: o **histórico de eventos** guarda os últimos 90 dias de eventos de gerenciamento de cada Região, sem configuração, num registro que pode ser pesquisado e baixado, mas não alterado. É ali que a escola encontra quem mudou a política.

O limite: por padrão, só os **eventos de gerenciamento** (operações sobre os recursos) são registrados. Quem leu um documento específico no S3 é um **evento de dados**, e só aparece se a escola tiver ativado esse registro numa trilha antes. E o CloudTrail registra a ação, não o estado da configuração; o antes e depois é o [Config](config.md).

## Como funciona

1. Toda conta já tem o histórico de eventos com 90 dias de eventos de gerenciamento.
2. Para guardar mais tempo, você cria uma **trilha**, que entrega os eventos num bucket S3, com cópia opcional para o CloudWatch Logs.
3. A trilha pode cobrir todas as Regiões e, criada pela conta de gerenciamento, todas as contas da organização, sem que as contas-membro possam alterá-la.
4. Opcionalmente, você ativa eventos de dados, o CloudTrail Insights e a validação de integridade dos arquivos de log.

## Opções principais

| Recurso | O que faz | Quando usar |
|---|---|---|
| Histórico de eventos | 90 dias de eventos de gerenciamento, sem configuração | Investigar uma mudança recente |
| Trilha | Entrega contínua de eventos no S3 | Guardar por anos, para auditoria |
| Trilha da organização | Uma trilha para todas as contas | Registro central que as contas-membro não apagam |
| Eventos de dados | Operações dentro dos recursos, como ler objetos no S3 | "Quem baixou o arquivo" |
| CloudTrail Insights | Detecta volume incomum de chamadas ou de erros | Pico estranho de chamadas de API |
| Validação de integridade | Mostra se um arquivo de log foi alterado ou apagado | Provar à auditoria que o log é íntegro |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Histórico de eventos | 90 dias, sem custo e sem configuração | 06/10/2026 |
| Registrado por padrão | Só eventos de gerenciamento | 06/10/2026 |
| Primeira cópia de eventos de gerenciamento numa trilha | Sem cobrança do CloudTrail | 06/10/2026 |
| CloudTrail Lake | Fechado a novos clientes desde 31/05/2026 | 06/10/2026 |

## Como é cobrado

O histórico de eventos e a primeira cópia dos eventos de gerenciamento entregue no S3 não têm cobrança do CloudTrail; paga-se o armazenamento no S3. Cópias adicionais, eventos de dados e o Insights são cobrados por quantidade de eventos.

## Não confundir com

| Serviço | Diferença para o CloudTrail | Pista no enunciado |
|---|---|---|
| [AWS Config](config.md) | Guarda o estado e o histórico de configuração | "Como estava configurado antes" |
| [Amazon CloudWatch](cloudwatch.md) | Métricas, alarmes e logs de funcionamento | "CPU acima de 80%" |
| [Amazon GuardDuty](../seguranca/guardduty.md) | Analisa os eventos em busca de ameaças | "Atividade suspeita" |
| VPC Flow Logs ([VPC](../redes/vpc.md)) | Registram o tráfego de rede, não chamadas de API | "Que tráfego passou" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [Histórico de eventos](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html)
- [Conceitos: eventos de gerenciamento e de dados](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html)
- [Trilhas](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html)
- [Validação de integridade dos logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html)
- [CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html)
- [Preços do AWS CloudTrail](https://aws.amazon.com/cloudtrail/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
