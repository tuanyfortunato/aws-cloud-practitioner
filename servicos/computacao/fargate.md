# AWS Fargate

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Você quer executar containers, mas não quer escolher, atualizar e manter as máquinas que ficam por baixo deles.

**Como este serviço ajuda?** Fargate fornece a capacidade para executar containers com ECS ou EKS, sem você administrar diretamente os servidores dessa execução. Você define, entre outras coisas, os recursos necessários ao container.

**Exemplo do dia a dia:** A equipe informa que seu serviço de pedidos precisa de determinada capacidade e o executa pelo ECS com Fargate, sem criar um grupo próprio de máquinas EC2.

**O que ele não resolve sozinho?** Fargate não substitui a aplicação nem o coordenador ECS/EKS. Configuração, permissões, rede e custo continuam exigindo decisões.

**Primeiras palavras para entender:**

- **Container:** pacote em execução com a aplicação.
- **Capacidade:** recursos como processamento e memória.
- **Gerenciado:** parte do trabalho operacional fica com a AWS.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Computação serverless para contêineres · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.5 Containers e serverless](../../docs/03-tecnologia-e-servicos/05-containers-e-serverless.md)
>
> **Em uma frase:** motor serverless que executa contêineres do ECS ou EKS sem você provisionar ou gerenciar servidores.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Descreva os containers pelo ECS ou EKS e selecione uma modalidade de execução compatível com Fargate.

**Passo 2.** Defina capacidade, comunicação e permissões. Fargate fornece a infraestrutura de execução sem você administrar diretamente as máquinas.

**Passo 3.** Observe os containers e seus resultados. A AWS administrar servidores não elimina a responsabilidade pelo código e pelos acessos.

## 2. Recursos e opções, com significado

### Para que serve

Rodar contêineres sem cuidar de instâncias, patch de SO ou escalonamento do cluster.

Jobs longos que **excedem os 15 min do Lambda** (sem limite de duração).

Cargas variáveis em que o *bin packing* de instâncias não compensa.

### Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Tamanho da task/pod** | Você escolhe vCPU e memória (combinações predefinidas, de 0,25 vCPU até **32 vCPU / 244 GB** 🧊). |
| **Isolamento** | Cada task roda em seu próprio ambiente isolado (micro-VM). |
| **Armazenamento** | Efêmero (20 GB padrão, ampliável) + volumes **EFS** e **EBS** persistentes. |
| **Arquitetura** | x86_64 ou ARM (Graviton). |
| **Fargate Spot** | Até ~70% mais barato, pode ser interrompido (aviso de 2 min) — só no ECS. |
| **Rede** | Modo `awsvpc`: cada task recebe sua ENI e security group. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Fargate não substitui a aplicação nem o coordenador ECS/EKS. Configuração, permissões, rede e custo continuam exigindo decisões.

### ⚠️ Pegadinhas e não confundir

Fargate **não é orquestrador**: é usado **com** ECS ou EKS.

Fargate × Lambda: contêiner sem limite de tempo × função Lambda convencional até 15 min por invocação; workflows e outras modalidades têm modelos próprios.

Fargate × EC2 launch type: menos controle (sem GPU, sem acesso ao host) e menos operação.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por **vCPU e memória alocadas**, por segundo (mínimo de 1 minuto), + armazenamento efêmero extra.

Coberto pelo **Compute Savings Plans**.

### Segurança e responsabilidade compartilhada

**AWS:** hosts, SO, runtime de contêiner, isolamento, patch da infraestrutura.

**Cliente:** imagem do contêiner e suas dependências, task role, rede, dados.

## 5. Caso resolvido: ligando as peças

A equipe informa que seu serviço de pedidos precisa de determinada capacidade e o executa pelo ECS com Fargate, sem criar um grupo próprio de máquinas EC2.

**Aplicando a sequência à situação:**

**Etapa 1:** Descreva os containers pelo ECS ou EKS e selecione uma modalidade de execução compatível com Fargate.
**Etapa 2:** Defina capacidade, comunicação e permissões. Fargate fornece a infraestrutura de execução sem você administrar diretamente as máquinas.
**Etapa 3:** Observe os containers e seus resultados. A AWS administrar servidores não elimina a responsabilidade pelo código e pelos acessos.

**Resultado e responsabilidade:** Fargate fornece a capacidade para executar containers com ECS ou EKS, sem você administrar diretamente os servidores dessa execução. Você define, entre outras coisas, os recursos necessários ao container.

**Recursos envolvidos:** Tasks ECS ou workloads EKS compatíveis e interfaces de rede.

**Decisões que precisam ser tomadas:** Recursos de CPU/memória suportados, imagem, roles e rede.

**Outra situação comentada:** Container de worker: ECR guarda imagem, ECS organiza, Fargate executa.

**Por que não concluir mais do que isso:** Não armazena imagens nem substitui ECS/EKS; aplicações ainda exigem segurança e dados persistentes adequados

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Rodar contêineres sem gerenciar instâncias."

**Resposta curta:** Fargate (com ECS ou EKS).

**Pergunta:** "Processar arquivo por 2 horas sem gerenciar servidores."

**Resposta curta:** Fargate (ou AWS Batch).

**Pergunta:** "Como o Fargate é cobrado?"

**Resposta curta:** Por vCPU e memória alocadas, por segundo.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Fargate no ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
