# Amazon EC2 Auto Scaling

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma loja tem poucos visitantes de madrugada e muitos durante uma promoção. Manter sempre a mesma quantidade de máquinas pode desperdiçar dinheiro ou deixar o site lento.

**Como este serviço ajuda?** O EC2 Auto Scaling aumenta ou diminui a quantidade de máquinas EC2 seguindo regras que você configura. Ele também pode substituir máquinas consideradas sem saúde pelo grupo.

**Exemplo do dia a dia:** A loja configura um grupo que adiciona máquinas quando a demanda aumenta e reduz a quantidade depois da promoção. O programa precisa estar preparado para funcionar em várias máquinas.

**O que ele não resolve sozinho?** Ele gerencia a quantidade de máquinas; não distribui sozinho cada pedido dos visitantes entre elas. Essa distribuição costuma ser feita por um balanceador.

**Primeiras palavras para entender:**

- **Escalar:** ajustar capacidade.
- **Grupo:** conjunto de máquinas administrado em conjunto.
- **Política:** regra para decidir quando ajustar esse conjunto.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Computação · **Domínio:** 1 (elasticidade) e 3 · **Escopo:** Regional (grupo distribuído entre AZs) · **Tópico do guia:** [3.4 Escalabilidade e balanceamento](../../docs/03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md)
>
> **Em uma frase:** aumenta e reduz automaticamente o número de instâncias EC2 conforme a demanda e substitui as que falham.
>
> **Escopo oficial:** ✅ No escopo (AWS Auto Scaling) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **métrica:** Medida observada ao longo do tempo, como utilização ou número de erros. O número precisa de unidade, período e contexto para ter significado.


**Passo 1.** Defina a configuração das máquinas e a quantidade mínima, desejada e máxima do grupo.

**Passo 2.** Escolha condições que ajustam a quantidade, como uma métrica de utilização. O grupo cria ou remove máquinas dentro desses limites.

**Passo 3.** Observe se a capacidade acompanha a demanda. A aplicação deve funcionar com cópias que podem ser substituídas.

## 2. Recursos e opções, com significado

### Para que serve

**Antes de ler este trecho:**

- **elasticidade:** Ajuste da capacidade para crescer e reduzir conforme a necessidade, dentro das regras e dos limites da solução.
- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.


**Elasticidade:** acompanhar picos e vales de tráfego sem intervenção manual.

**Antes de ler este trecho:**

- **alta disponibilidade:** Planejamento para manter o sistema acessível diante de determinadas falhas. Não é promessa de ausência de qualquer interrupção.


**Alta disponibilidade:** manter um número mínimo de instâncias saudáveis distribuídas em várias AZs.


**Otimização de custos:** não pagar por capacidade ociosa.

### Conceitos e componentes

**Auto Scaling Group (ASG)**

**Antes de ler este trecho:**

- **ASG:** Grupo de Auto Scaling: conjunto cuja quantidade e saúde são administradas conforme uma configuração e suas regras.


**O que é:** Conjunto lógico de instâncias com capacidade **mínima**, **desejada** e **máxima**.

**Launch template**

**Antes de ler este trecho:**

- **SG:** Regras de tráfego associadas a interfaces ou recursos compatíveis. É um controle de rede, não uma permissão IAM para ler um arquivo ou chamar uma API.
- **AMI:** Imagem de máquina EC2: modelo com o software necessário para iniciar uma instância. A imagem precisa ser compatível com a configuração de execução escolhida.
- **key pair:** Par de chaves usado em mecanismos de acesso: uma parte pública e uma privada. A parte privada precisa ser protegida pelo cliente.
- **user data:** Dados ou instruções fornecidos à inicialização da máquina. Um script configurado pode preparar o ambiente; ele não instala qualquer sistema sem você descrever as ações.
- **launch template:** Modelo versionado de parâmetros para iniciar máquinas. Facilita repetir configurações; não contém por si só todas as regras da aplicação.


**O que é:** Configuração das instâncias (AMI, tipo, SG, key pair, user data). Substitui as antigas *launch configurations*.

**Health check**

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **load balancer / ELB:** Recurso que distribui tráfego entre destinos configurados. Ele não cria sozinho todas as máquinas necessárias nem conserta seu programa.
- **health check:** Teste de resposta usado para avaliar um destino. O teste e os limites precisam refletir a função observada; não equivale a uma investigação completa da aplicação.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.


**O que é:** EC2 (status da instância) e/ou **ELB** (health check do load balancer). Instância não saudável é substituída.

**Scaling policy**

**Antes de ler este trecho:**

- **policy:** Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.


**O que é:** Regra que muda a capacidade desejada.

**Lifecycle hooks**


**O que é:** Pausam a instância ao entrar/sair do grupo para rodar ações (ex.: instalar agente, drenar logs).

**Warm pools**


**O que é:** Instâncias pré-inicializadas para escalar mais rápido.

**Instance refresh**


**O que é:** Substitui gradualmente as instâncias para aplicar nova AMI/template.

### Configurações e opções importantes

**Antes de ler este trecho:**

- **CPU:** CPU é o processador que executa instruções. vCPU é a unidade de processamento virtual apresentada ao ambiente. Mais processamento não resolve automaticamente falta de memória ou de velocidade do disco.
- **alarme:** Condição acompanhada sobre dados de monitoramento. Uma mudança de estado pode gerar ações configuradas; o alarme não diagnostica todo problema sozinho.
- **ML:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.
- **legado:** Sistema existente com tecnologias ou dependências que precisam ser preservadas ou avaliadas numa mudança. Antigo não significa automaticamente que pode ser desligado.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Política | Como funciona | Exemplo |
|---|---|---|
| **Target tracking** | Mantém uma métrica num alvo | CPU média em 50% |
| **Step scaling** | Ajustes em degraus conforme o tamanho do desvio do alarme | +2 instâncias se CPU > 70%, +4 se > 90% |
| **Simple scaling** | Um ajuste por alarme, com cooldown | Legado |
| **Scheduled** | Capacidade em horários conhecidos | Pico toda sexta às 18h |
| **Predictive** | ML prevê a demanda com base no histórico e escala antes | Padrões diários/semanais |


**Antes de ler este trecho:**

- **On-Demand:** Modalidade de uso sem o compromisso de longo prazo descrito por reservas e planos. Cobrança e unidades dependem do recurso contratado.


**Mixed instances policy:** combina On-Demand e **Spot** e vários tipos de instância no mesmo grupo.


**Termination policy:** define qual instância sai primeiro (padrão: equilibra AZs, depois a com template mais antigo…).

**Antes de ler este trecho:**

- **AZ:** Parte isolada da infraestrutura dentro de uma região, formada por um ou mais datacenters. Distribuir recursos entre zonas pode reduzir o impacto de uma falha localizada.


**Rebalanceamento entre AZs:** o ASG tenta manter o mesmo número de instâncias por AZ.

### Limites e números

**Antes de ler este trecho:**

- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.


🧊 Quotas de ASGs e templates por região não caem.


📌 Monitoramento detalhado (1 min) deixa o escalonamento mais rápido.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele gerencia a quantidade de máquinas; não distribui sozinho cada pedido dos visitantes entre elas. Essa distribuição costuma ser feita por um balanceador.

### ⚠️ Pegadinhas e não confundir

**Antes de ler este trecho:**

- **EC2 Auto Scaling:** O EC2 Auto Scaling aumenta ou diminui a quantidade de máquinas EC2 seguindo regras que você configura.
- **ECS:** O ECS coordena a execução de containers: pacotes com a aplicação e suas dependências.
- **Aurora:** Aurora é um banco relacional da AWS dentro da família RDS.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.


**EC2 Auto Scaling** (instâncias) × **AWS Auto Scaling** (planos de escalonamento para vários recursos: EC2, ECS, DynamoDB, Aurora).


Auto Scaling **não distribui tráfego** — quem faz isso é o [ELB](elastic-load-balancing.md). Juntos dão HA + elasticidade.


Escalar **horizontalmente** (scale out) é o que o ASG faz; aumentar o tamanho da instância é **vertical** (scale up) e exige parar a instância.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.


**Sem custo próprio:** paga-se as instâncias EC2 e alarmes/métricas do CloudWatch usados.

### Segurança e responsabilidade compartilhada

**AWS:** executa o serviço de escalonamento.

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.


**Cliente:** define políticas, AMIs atualizadas, IAM, security groups.

## 5. Caso resolvido: ligando as peças

A loja configura um grupo que adiciona máquinas quando a demanda aumenta e reduz a quantidade depois da promoção. O programa precisa estar preparado para funcionar em várias máquinas.

**Aplicando a sequência à situação:**

**Etapa 1:** Defina a configuração das máquinas e a quantidade mínima, desejada e máxima do grupo.
**Etapa 2:** Escolha condições que ajustam a quantidade, como uma métrica de utilização. O grupo cria ou remove máquinas dentro desses limites.
**Etapa 3:** Observe se a capacidade acompanha a demanda. A aplicação deve funcionar com cópias que podem ser substituídas.

**Resultado e responsabilidade:** O EC2 Auto Scaling aumenta ou diminui a quantidade de máquinas EC2 seguindo regras que você configura. Ele também pode substituir máquinas consideradas sem saúde pelo grupo.

**Recursos envolvidos:** Grupo, launch template, mínimo, máximo, capacidade desejada e políticas.

**Decisões que precisam ser tomadas:** Número de instâncias e critérios de saúde/escala.


**Outra situação comentada:** Pico previsível: política agendada; demanda variável: política dinâmica com métrica adequada.

**Por que não concluir mais do que isso:** Não remove gargalos de aplicação/banco nem copia arquivos locais entre instâncias

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Uma loja tem poucos visitantes de madrugada e muitos durante uma promoção. Manter sempre a mesma quantidade de máquinas pode desperdiçar dinheiro ou deixar o site lento.

**2. O que a solução fornece?**

O EC2 Auto Scaling aumenta ou diminui a quantidade de máquinas EC2 seguindo regras que você configura. Ele também pode substituir máquinas consideradas sem saúde pelo grupo.

**3. Que conclusão seria incorreta?**

Ele gerencia a quantidade de máquinas; não distribui sozinho cada pedido dos visitantes entre elas. Essa distribuição costuma ser feita por um balanceador.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Ajustar automaticamente o número de instâncias à demanda."

**Resposta curta:** EC2 Auto Scaling.


**Fundamento explicado no capítulo:** "Ajustar automaticamente o número de instâncias à demanda." → EC2 Auto Scaling.

**Pergunta:** "A loja tem pico toda sexta às 18h."

**Resposta curta:** Scheduled scaling.


**Fundamento explicado no capítulo:** "A loja tem pico toda sexta às 18h." → Scheduled scaling.

**Pergunta:** "Manter a CPU média em 50%."

**Resposta curta:** Target tracking.


**Fundamento explicado no capítulo:** "Manter a CPU média em 50%." → Target tracking.

**Pergunta:** "Escalar antes do pico com base no histórico."

**Resposta curta:** Predictive scaling.


**Fundamento explicado no capítulo:** "Escalar antes do pico com base no histórico." → Predictive scaling.

**Pergunta:** "Substituir automaticamente instâncias com falha."

**Resposta curta:** ASG com health checks.


**Fundamento explicado no capítulo:** "Substituir automaticamente instâncias com falha." → ASG com health checks.

**Pergunta:** "O Auto Scaling tem custo?"

**Resposta curta:** Não; paga-se só os recursos.


**Fundamento explicado no capítulo:** "O Auto Scaling tem custo?" → Não; paga-se só os recursos.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
