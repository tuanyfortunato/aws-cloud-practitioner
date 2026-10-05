# Amazon GuardDuty

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa precisa perceber sinais de atividade suspeita, como comportamento incomum de credenciais ou recursos, sem analisar manualmente todos os registros.

**Como este serviço ajuda?** GuardDuty analisa fontes de dados compatíveis para detectar possíveis ameaças e produzir achados de segurança.

**Exemplo do dia a dia:** O serviço identifica um padrão suspeito associado a uma identidade ou recurso e gera um achado para a equipe investigar.

**O que ele não resolve sozinho?** Um achado não confirma sozinho uma invasão. GuardDuty não é, por si só, um bloqueador de todo tráfego; respostas automáticas exigem recursos e configurações apropriados.

**Primeiras palavras para entender:**

- **Ameaça:** possível ação prejudicial.
- **Achado:** indicação de segurança para análise.
- **Detecção:** identificação de sinais suspeitos.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança / detecção de ameaças · **Domínio:** 2 · **Escopo:** Regional (multi-conta via Organizations) · **Tópico do guia:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)
>
> **Em uma frase:** detecção inteligente e contínua de **ameaças ativas** usando machine learning, detecção de anomalias e inteligência de ameaças.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento


**Passo 1.** Habilite os recursos e as fontes de detecção compatíveis com seu ambiente.

**Passo 2.** O serviço analisa sinais e produz achados quando identifica condições suspeitas.

**Passo 3.** Investigue o contexto e defina uma resposta. Um achado é uma indicação para análise, não uma ação de bloqueio universal.

## 2. Recursos e opções, com significado

### Fontes de dados

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **ECS:** O ECS coordena a execução de containers: pacotes com a aplicação e suas dependências.
- **EKS:** O EKS oferece Kubernetes gerenciado.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.
- **AWS Backup:** AWS Backup centraliza políticas e operações de backup para recursos compatíveis.
- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.
- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **Aurora:** Aurora é um banco relacional da AWS dentro da família RDS.
- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **Route 53:** Route 53 oferece DNS e recursos associados, como registro de domínios e verificações de saúde.
- **CloudTrail:** Registro de atividades e chamadas AWS compatíveis. Ajuda a analisar quem realizou uma operação, em vez de medir sozinho a velocidade da aplicação.
- **AI / IA:** Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.
- **Bedrock:** Bedrock oferece acesso gerenciado a modelos e recursos de desenvolvimento de aplicações com IA generativa, conforme a oferta e as autorizações.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **DNS:** Sistema que relaciona nomes a informações de endereço e outros registros. Resolver o nome de um site não hospeda o site nem garante que ele está funcionando.
- **Kubernetes:** Sistema que coordena containers e mantém o estado de execução desejado. Sua operação exige conceitos e configurações próprios.
- **runtime:** Ambiente que executa código de uma linguagem ou plataforma. Compatibilidade de bibliotecas e versões deve ser avaliada.
- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Fundamentais (ativadas ao ligar) | Planos de proteção opcionais |
|---|---|
| **CloudTrail management events** | **S3 Protection** (data events do S3) |
| **VPC Flow Logs** | **EKS Protection** (audit logs do Kubernetes) |
| **Logs de DNS** (Route 53 Resolver) | **Runtime Monitoring** (EC2, ECS, EKS — com agente) |
| | **Malware Protection** (EBS do EC2, objetos novos no S3 e recovery points do AWS Backup) |
| | **AI Protection** (cargas de IA, ex.: Bedrock) ✔️ |
| | **RDS Protection** (logins suspeitos no Aurora/RDS) |
| | **Lambda Protection** (tráfego de rede das funções) |


**Antes de ler este trecho:**

- **GuardDuty:** GuardDuty analisa fontes de dados compatíveis para detectar possíveis ameaças e produzir achados de segurança.


**Sem agentes** para as fontes fundamentais: o GuardDuty lê os logs de forma independente (não precisa ativar Flow Logs/CloudTrail você mesmo).


**Extended Threat Detection:** correlaciona eventos em **sequências de ataque** de vários estágios.

### Exemplos de achados (findings)

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **credenciais:** Informações usadas para comprovar ou representar uma identidade. Credenciais temporárias expiram; credenciais de longa duração precisam de proteção e administração.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.


Mineração de criptomoeda numa instância; comunicação com IPs/domínios maliciosos (C&C); chamadas de API de locais incomuns; credenciais de instância usadas fora da AWS; *port scanning*; buckets S3 tornados públicos; malware.

### Configurações

Ativação com **um clique**; **teste gratuito de 30 dias** (no Free Tier novo, aparece vinculado ao **Paid plan**).


Severidade (baixa, média, alta, crítica); listas de IPs confiáveis/ameaças; filtros de supressão.

**Antes de ler este trecho:**

- **SNS:** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis.
- **EventBridge:** EventBridge recebe eventos e usa regras para encaminhá-los a destinos compatíveis.
- **SSM:** Sigla usada em recursos do Systems Manager. O serviço oferece ferramentas de administração; nós, acessos e conectividade precisam estar preparados.


**Resposta automatizada:** achados vão ao **EventBridge** → Lambda/SSM para isolar a instância, notificar via SNS.

**Antes de ler este trecho:**

- **Detective:** Detective organiza dados compatíveis e suas relações para apoiar investigações de segurança.
- **Security Hub:** Security Hub reúne achados de fontes compatíveis e oferece avaliações de controles, conforme os recursos habilitados.


Envia achados ao **Security Hub** e permite investigar no **Detective**.

**Antes de ler este trecho:**

- **Organizations:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.


Multi-conta com **administrador delegado** no Organizations.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Um achado não confirma sozinho uma invasão. GuardDuty não é, por si só, um bloqueador de todo tráfego; respostas automáticas exigem recursos e configurações apropriados.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **Inspector:** Inspector avalia recursos compatíveis para encontrar vulnerabilidades e determinados riscos de exposição.
- **Macie:** Macie ajuda a descobrir e classificar dados sensíveis em objetos S3 compatíveis e a analisar aspectos de segurança dos buckets.


GuardDuty (**ameaça em andamento**, a partir de logs) × Inspector (**vulnerabilidade** de software) × Macie (**dados sensíveis**) × Detective (**investigação**).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.


Por volume de eventos/logs analisados e por plano de proteção.

## 5. Caso resolvido: ligando as peças

O serviço identifica um padrão suspeito associado a uma identidade ou recurso e gera um achado para a equipe investigar.

**Aplicando a sequência à situação:**

**Etapa 1:** Habilite os recursos e as fontes de detecção compatíveis com seu ambiente.
**Etapa 2:** O serviço analisa sinais e produz achados quando identifica condições suspeitas.
**Etapa 3:** Investigue o contexto e defina uma resposta. Um achado é uma indicação para análise, não uma ação de bloqueio universal.

**Resultado e responsabilidade:** GuardDuty analisa fontes de dados compatíveis para detectar possíveis ameaças e produzir achados de segurança.

**Recursos envolvidos:** Detector, fontes de dados/proteções e findings.

**Decisões que precisam ser tomadas:** Região, contas, proteções e destinatários de achados.

**Antes de ler este trecho:**

- **CVE:** Identificador público de uma vulnerabilidade conhecida. Um achado precisa ser avaliado pelo impacto no recurso e pelas correções disponíveis.


**Outra situação comentada:** Credenciais usadas de forma suspeita: GuardDuty; pacote com CVE: Inspector.

**Por que não concluir mais do que isso:** Detectar não garante bloquear ou corrigir sozinho

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

A empresa precisa perceber sinais de atividade suspeita, como comportamento incomum de credenciais ou recursos, sem analisar manualmente todos os registros.

**2. O que a solução fornece?**

GuardDuty analisa fontes de dados compatíveis para detectar possíveis ameaças e produzir achados de segurança.

**3. Que conclusão seria incorreta?**

Um achado não confirma sozinho uma invasão. GuardDuty não é, por si só, um bloqueador de todo tráfego; respostas automáticas exigem recursos e configurações apropriados.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Detectar atividade maliciosa analisando CloudTrail, VPC Flow Logs e DNS."

**Resposta curta:** GuardDuty.


**Fundamento explicado no capítulo:** "Detectar atividade maliciosa analisando CloudTrail, VPC Flow Logs e DNS." → GuardDuty.

**Pergunta:** "Instância está minerando criptomoeda."

**Resposta curta:** GuardDuty.


**Fundamento explicado no capítulo:** "Instância está minerando criptomoeda." → GuardDuty.

**Pergunta:** "Responder automaticamente a um achado."

**Resposta curta:** GuardDuty → EventBridge → Lambda.


**Fundamento explicado no capítulo:** "Responder automaticamente a um achado." → GuardDuty → EventBridge → Lambda.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
