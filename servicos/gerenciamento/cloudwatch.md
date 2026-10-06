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

**Antes de ler este trecho:**

- **alarme:** Condição acompanhada sobre dados de monitoramento. Uma mudança de estado pode gerar ações configuradas; o alarme não diagnostica todo problema sozinho.

**Passo 1.** Escolha quais medidas e registros ajudam a observar o problema da aplicação.

**Passo 2.** Configure coleta, visualizações e condições de alarme. Dados são acompanhados dentro dos períodos e critérios definidos.

**Passo 3.** Investigue mudanças e acione a resposta planejada. Um número isolado não explica a causa de toda falha.

## 2. Recursos e opções, com significado

### Componentes

**Metrics**

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **retenção:** Tempo durante o qual dados ou registros são conservados. Depois desse prazo, o comportamento depende das regras do serviço e das configurações.

**Detalhe:** Séries temporais por *namespace* (ex.: `AWS/EC2`) e *dimensões* (ex.: InstanceId). Resolução padrão 1 min (EC2 básico: **5 min**); *high-resolution* até 1 s. Retenção de **15 meses** (agregadas).

**Custom metrics**

**Antes de ler este trecho:**

- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.
- **memória:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.

**Detalhe:** Enviadas pela aplicação ou pelo **CloudWatch agent** (memória, disco, processos).

**Alarms**

**Antes de ler este trecho:**

- **Systems Manager:** Systems Manager reúne ferramentas de operação para recursos e nós gerenciados compatíveis, incluindo acesso, automação, inventário e gerenciamento de patches.
- **SNS:** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis.
- **ML:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.
- **ALARM / OK:** Estados de alarme CloudWatch: condição de alarme, condição normal e falta de dados suficientes. Estado não é diagnóstico completo da causa.

**Detalhe:** Estados **OK / ALARM / INSUFFICIENT_DATA**. Ações: **SNS**, **Auto Scaling**, **ações de EC2** (parar, encerrar, reiniciar, recuperar), Systems Manager. **Composite alarms** combinam vários. **Anomaly detection** cria faixas esperadas com ML.

**Billing alarm**

**Antes de ler este trecho:**

- **métrica:** Medida observada ao longo do tempo, como utilização ou número de erros. O número precisa de unidade, período e contexto para ter significado.

**Detalhe:** Alarme sobre a métrica *EstimatedCharges* (precisa ativar alertas de faturamento; métrica fica em **us-east-1**).

**Logs**

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **log:** Registro de acontecimentos para análise. A aplicação e os serviços podem produzir registros diferentes; é necessário definir coleta, retenção e acesso.

**Detalhe:** *Log groups* e *log streams*; **retenção configurável** (padrão: nunca expira); **metric filters** (transformar padrões de log em métricas); **subscription filters** (enviar a Lambda/Kinesis/OpenSearch); export para S3.

**Logs Insights**

**Detalhe:** Consultas interativas sobre logs. **Live Tail** acompanha em tempo real.

**Dashboards**

**Detalhe:** Painéis **globais** com métricas de várias regiões/contas.

**Synthetics**

**Detalhe:** *Canaries* que simulam usuários (testes de endpoints/fluxos).

**RUM**

**Antes de ler este trecho:**

- **front-end:** Parte da aplicação com que a pessoa interage. Publicá-la não cria automaticamente todas as operações e bancos da parte interna.
- **RUM:** Observação da experiência de usuários reais por dados coletados da aplicação. A coleta precisa de integração e deve refletir o que se deseja medir.

**Detalhe:** Monitoramento de usuários reais (front-end web).

**Container / Lambda Insights, Application Signals**

**Antes de ler este trecho:**

- **container:** Ambiente que executa uma aplicação a partir de uma imagem com software e dependências. É diferente de criar uma máquina virtual completa para cada pacote.
- **APM:** Acompanhamento de desempenho de aplicações. Requer sinais e contexto adequados, não apenas uma métrica isolada de infraestrutura.

**Detalhe:** Observabilidade de contêineres, funções e aplicações (APM).

**CloudWatch agent**

**Antes de ler este trecho:**

- **SO:** Software básico da máquina, como Linux ou Windows. Ele administra arquivos, memória e execução de programas; atualizar esse software é diferente de atualizar a aplicação.
- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.

**Detalhe:** Instalado em EC2/on-premises para métricas do SO e envio de logs.

### Métricas padrão do EC2

**Antes de ler este trecho:**

- **CPU:** CPU é o processador que executa instruções. vCPU é a unidade de processamento virtual apresentada ao ambiente. Mais processamento não resolve automaticamente falta de memória ou de velocidade do disco.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **instance store:** Armazenamento local temporário da máquina física. Não é lugar seguro para a única cópia de dados que precisam sobreviver às ações descritas no ciclo de vida.

✅ CPU, rede (bytes/pacotes), disco de instance store (ops/bytes), **status checks** (a cada **1 min**, mesmo no básico), créditos de CPU (T).

Monitoramento **detalhado**: todas as métricas a cada 1 min, pago por métrica.

❌ **Memória**, uso de **disco do sistema de arquivos**, processos → exigem o **agent**.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Nem todo dado é coletado automaticamente, e um alarme não corrige qualquer problema sozinho. Você precisa coletar os dados certos e configurar a resposta desejada.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **CloudTrail:** Registro de atividades e chamadas AWS compatíveis. Ajuda a analisar quem realizou uma operação, em vez de medir sozinho a velocidade da aplicação.
- **Config:** Serviço que acompanha configurações e suas avaliações em recursos compatíveis. Observar configuração é diferente de observar uma métrica de desempenho.

**CloudWatch** (desempenho: métricas/logs/alarmes) × **CloudTrail** (quem fez qual chamada de API) × **Config** (estado/histórico de configuração).

**Antes de ler este trecho:**

- **AWS Budgets / Budgets:** AWS Budgets compara valores com metas configuradas e pode gerar notificações ou ações compatíveis, conforme as condições definidas.

CloudWatch billing alarm × **AWS Budgets** (orçamentos mais completos, inclusive previsão).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **GB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.

Camada gratuita ✔️ (Always Free): métricas básicas, **10 métricas** (customizadas + detailed monitoring, somadas) e **10 métricas de alarme** de resolução padrão, além de cota de logs; depois por métrica customizada, alarme, GB de log ingerido/armazenado, consulta, dashboard, canary.

## 5. Caso resolvido: ligando as peças

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **conformidade:** Atendimento a requisitos definidos. Usar um serviço com certificações não torna automaticamente a aplicação do cliente conforme.

O sistema ficou lento, e a equipe quer perceber o problema e investigar seu comportamento. A pergunta inicial é como ele funciona, não quem realizou uma ação administrativa.

A equipe coleta métricas pertinentes, registros da aplicação e cria um alarme com período e critério definidos. Um aumento de erros pode disparar uma notificação configurada. Logs ajudam a examinar o que o programa registrou durante a ocorrência.

O alarme não explica sozinho a causa nem aplica qualquer correção por padrão. Para investigar quem alterou um recurso, eventos CloudTrail podem ser necessários; para acompanhar propriedades e conformidade de configuração, Config atende outra parte da investigação.

**Recursos envolvidos:** Métricas, logs, alarmes e dashboards.

**Decisões que precisam ser tomadas:** Coleta, retenção, thresholds e ações.

**Antes de ler este trecho:**

- **SG:** Regras de tráfego associadas a interfaces ou recursos compatíveis. É um controle de rede, não uma permissão IAM para ler um arquivo ou chamar uma API.

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
