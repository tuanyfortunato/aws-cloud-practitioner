# Amazon Inspector

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Aplicações e sistemas podem usar software com vulnerabilidades conhecidas. A equipe precisa identificar esses pontos antes de uma exploração.

**Como este serviço ajuda?** Inspector avalia recursos compatíveis para encontrar vulnerabilidades e determinados riscos de exposição.

**Exemplo do dia a dia:** A equipe avalia o software de um recurso compatível e recebe achados que ajudam a priorizar atualizações e correções.

**O que ele não resolve sozinho?** Encontrar uma vulnerabilidade não instala automaticamente a correção. Compatibilidade, cobertura e habilitação dos recursos de avaliação precisam ser verificadas.

**Primeiras palavras para entender:**

- **Vulnerabilidade:** falha que pode ser explorada.
- **Avaliação:** exame de um recurso.
- **Correção:** mudança para resolver a falha.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança / gestão de vulnerabilidades · **Domínio:** 2 · **Escopo:** Regional (multi-conta) · **Tópico do guia:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)
>
> **Em uma frase:** varre continuamente cargas de trabalho em busca de **vulnerabilidades de software (CVEs)** e exposição de rede não intencional.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.

**Passo 1.** Prepare e habilite a avaliação dos tipos de recurso compatíveis.

**Passo 2.** O serviço identifica vulnerabilidades e riscos cobertos pela avaliação.

**Passo 3.** Priorize correções e verifique o resultado. Encontrar uma vulnerabilidade não instala a atualização necessária.

## 2. Recursos e opções, com significado

### O que varre

**EC2**

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.
- **SO:** Software básico da máquina, como Linux ou Windows. Ele administra arquivos, memória e execução de programas; atualizar esse software é diferente de atualizar a aplicação.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **CIS:** Referências, padrões ou requisitos de segurança e conformidade com escopos distintos. A menção de um nome não é certificação automática do cliente; identifique qual requisito a seção aborda.
- **SSM:** Sigla usada em recursos do Systems Manager. O serviço oferece ferramentas de administração; nós, acessos e conectividade precisam estar preparados.

**Como:** Agente do **SSM** ou *agentless* (snapshots EBS)

**O que encontra:** CVEs de pacotes do SO e de aplicações; **alcance de rede** (portas expostas); CIS benchmarks

**Imagens no ECR**

**Antes de ler este trecho:**

- **ECR:** O ECR é um repositório de imagens de containers.
- **push:** Em pull, o consumidor busca dados. Em push, o envio é iniciado para o destinatário. A forma de entrega não executa automaticamente a regra de negócio.

**Como:** Ao fazer push e continuamente

**O que encontra:** CVEs no SO e em pacotes de linguagem

**Funções Lambda**

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.

**Como:** Código e dependências

**O que encontra:** CVEs e falhas no código (*code scanning*)

**Repositórios de código / CI-CD**

**Antes de ler este trecho:**

- **deploy:** Colocar uma versão ou conjunto de recursos em funcionamento. O resultado precisa ser observado e, quando necessário, revertido de modo planejado.

**Como:** Integração com pipelines

**O que encontra:** Vulnerabilidades antes do deploy

### Destaques

**Antes de ler este trecho:**

- **CVE:** Identificador público de uma vulnerabilidade conhecida. Um achado precisa ser avaliado pelo impacto no recurso e pelas correções disponíveis.

**Contínuo e automático:** reavalia quando surge um novo CVE ou o recurso muda.

**Antes de ler este trecho:**

- **Inspector:** Inspector avalia recursos compatíveis para encontrar vulnerabilidades e determinados riscos de exposição.
- **CVSS:** Sistema de classificação de gravidade de vulnerabilidades. A prioridade no ambiente também depende de exposição e impacto do recurso.

**Inspector risk score** contextualizado (CVSS + exposição de rede + exploit conhecido).

**Antes de ler este trecho:**

- **SBOM:** Lista de componentes de software de um pacote ou aplicação. Ajuda a identificar dependências; não corrige automaticamente uma vulnerabilidade.

Exporta **SBOM** (lista de componentes de software).

**Antes de ler este trecho:**

- **Security Hub:** Security Hub reúne achados de fontes compatíveis e oferece avaliações de controles, conforme os recursos habilitados.
- **EventBridge:** EventBridge recebe eventos e usa regras para encaminhá-los a destinos compatíveis.

Integra com Security Hub e EventBridge; **teste gratuito de 15 dias**.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Encontrar uma vulnerabilidade não instala automaticamente a correção. Compatibilidade, cobertura e habilitação dos recursos de avaliação precisam ser verificadas.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **GuardDuty:** GuardDuty analisa fontes de dados compatíveis para detectar possíveis ameaças e produzir achados de segurança.
- **Macie:** Macie ajuda a descobrir e classificar dados sensíveis em objetos S3 compatíveis e a analisar aspectos de segurança dos buckets.
- **PII:** Informação que pode identificar uma pessoa. Sua identificação ajuda a planejar proteção de dados, mas não substitui avaliação do contexto e das regras aplicáveis.

**Inspector** (vulnerabilidades/CVE) × **GuardDuty** (ameaças ativas) × **Macie** (PII no S3).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **imagem:** Pacote ou modelo usado para iniciar um ambiente. Em EC2, a AMI é uma imagem de máquina; em containers, a imagem serve para iniciar containers.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.

Por instância EC2 escaneada/mês, por imagem do ECR, por função Lambda.

## 5. Caso resolvido: ligando as peças

A equipe avalia o software de um recurso compatível e recebe achados que ajudam a priorizar atualizações e correções.

**Aplicando a sequência à situação:**

**Etapa 1:** Prepare e habilite a avaliação dos tipos de recurso compatíveis.
**Etapa 2:** O serviço identifica vulnerabilidades e riscos cobertos pela avaliação.
**Etapa 3:** Priorize correções e verifique o resultado. Encontrar uma vulnerabilidade não instala a atualização necessária.

**Resultado e responsabilidade:** Inspector avalia recursos compatíveis para encontrar vulnerabilidades e determinados riscos de exposição.

**Recursos envolvidos:** Recursos elegíveis, cobertura de varredura e findings.

**Decisões que precisam ser tomadas:** Cobertura, acesso e pré-requisitos conforme recurso.

**Antes de ler este trecho:**

- **patch:** Atualização corretiva de software. A responsabilidade de aplicá-la depende da camada e do serviço usado.

**Outra situação comentada:** Dependência vulnerável numa imagem: Inspector integrado à varredura adequada; equipe corrige e republica.

**Por que não concluir mais do que isso:** Não substitui patch nem cobre automaticamente qualquer recurso da conta

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Varrer EC2 e imagens de contêiner em busca de vulnerabilidades."

**Resposta curta:** Inspector.

**Pergunta:** "Descobrir instâncias com portas acessíveis da internet sem necessidade."

**Resposta curta:** Inspector (alcance de rede).

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
