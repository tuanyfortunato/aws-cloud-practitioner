# AWS Compute Optimizer, Service Quotas, License Manager e outros

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A equipe pode estar usando capacidade inadequada, alcançar um limite de serviço ou perder controle sobre licenças. Cada dificuldade exige uma ferramenta diferente.

**Como este serviço ajuda?** Compute Optimizer recomenda ajustes de recursos compatíveis; Service Quotas acompanha limites de uso; License Manager ajuda a administrar licenças de software.

**Exemplo do dia a dia:** Uma máquina parece maior que o necessário: a equipe avalia recomendações. Se precisa criar mais recursos e encontra uma quota, consulta o limite e a possibilidade de aumento.

**O que ele não resolve sozinho?** Uma recomendação não é uma quota, e aumentar uma quota não otimiza custo. Gerenciar licença também não compra automaticamente os direitos de uso do software.

**Primeiras palavras para entender:**

- **Dimensionar:** escolher capacidade adequada.
- **Quota:** limite de uso.
- **Licença:** direito de usar software sob determinadas condições.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Gerenciamento / otimização e governança · **Domínio:** 3 e 4 · **Escopo:** Regional · **Tópico do guia:** [3.16 Gestão e governança](../../docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md)
>
> **Em uma frase:** ferramentas para dimensionar recursos, controlar limites e licenças, e organizar o ambiente.
>
> **Escopo oficial:** ✅ No escopo (Launch Wizard ❌ fora do escopo) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **licença:** Direito de usar um software sob condições. Instalar o programa ou inventariá-lo não concede automaticamente esse direito.

**Passo 1.** Descubra se o problema é dimensão do recurso, limite de uso ou administração de licença.

**Passo 2.** Consulte a ferramenta pertinente e os dados que fundamentam a decisão.

**Passo 3.** Ajuste recursos, solicite aumento elegível ou revise licenças conforme o caso. Essas ações não são intercambiáveis.

## 2. Recursos e opções, com significado

### AWS Compute Optimizer

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **ECS:** O ECS coordena a execução de containers: pacotes com a aplicação e suas dependências.
- **Fargate:** Fargate fornece a capacidade para executar containers com ECS ou EKS, sem você administrar diretamente os servidores dessa execução.
- **EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.
- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.
- **memória:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.
- **machine learning:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.

Usa **machine learning** sobre métricas do CloudWatch (14 dias por padrão; até 93 com métricas avançadas) para recomendar o **tamanho ideal** de: **EC2**, **Auto Scaling groups**, **volumes EBS**, **funções Lambda** (memória), **tasks ECS no Fargate**, RDS e licenças comerciais.

Classifica recursos como *under-provisioned*, *over-provisioned* ou *optimized* e estima a economia.

Gratuito no básico (opt-in). Recomendações também aparecem no **Cost Optimization Hub**.

### Service Quotas

**Antes de ler este trecho:**

- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.

Mostra as **cotas (limites)** de cada serviço por região, valores padrão e aplicados.

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **quota:** Limite de uso de um serviço ou recurso. Algumas quotas podem ser aumentadas mediante solicitação; limite não significa capacidade já reservada.

**Solicitar aumento** pelo console/API; *quota request templates* para contas novas da organização.

Alarmes do CloudWatch quando o uso se aproxima do limite.

### AWS License Manager

**Antes de ler este trecho:**

- **vCPU:** CPU é o processador que executa instruções. vCPU é a unidade de processamento virtual apresentada ao ambiente. Mais processamento não resolve automaticamente falta de memória ou de velocidade do disco.
- **SAP:** Tecnologias e aplicações empresariais do ecossistema SAP. Podem exigir requisitos específicos de memória, licenciamento e operação.

Controla o uso de **licenças de software** (Microsoft, Oracle, SAP, IBM): regras por vCPU/núcleo/socket, limites rígidos ou alertas.

**Antes de ler este trecho:**

- **BYOL:** Trazer licença própria elegível. É necessário verificar o direito de uso e as condições do software; a AWS não cria automaticamente essa licença.

Ajuda com **BYOL** em Dedicated Hosts (automatiza alocação de hosts) e evita multas de auditoria.

### Outros utilitários de organização

**Tags + Tag Editor**

**Antes de ler este trecho:**

- **tag:** Par de nome e valor associado a recursos ou objetos compatíveis. Ajuda organização; usos em permissões e cobrança dependem de configuração e suporte.
- **ABAC:** Controle de acesso baseado em atributos, como tags, dentro das condições de políticas compatíveis. Não concede acesso sem regras aplicáveis.

**Função:** Pares chave-valor para organizar, controlar acesso (ABAC) e separar custos

**Resource Groups**

**Antes de ler este trecho:**

- **stack:** Conjunto de recursos administrados a partir de uma descrição CloudFormation. Excluir ou atualizar a stack pode afetar os recursos conforme suas políticas.

**Função:** Agrupar recursos por tag/stack para operar juntos

**Resource Explorer**

**Função:** Buscar recursos em todas as regiões/contas

**AWS Launch Wizard ❌ fora do escopo**

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **Active Directory:** Tecnologia de diretório para identidades, computadores e controles corporativos. É diferente do cadastro de clientes de uma aplicação pública.
- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.

**Função:** Implantar SAP, SQL Server, Active Directory com boas práticas

**AWS AppConfig ❌ fora do escopo**

**Antes de ler este trecho:**

- **Systems Manager:** Systems Manager reúne ferramentas de operação para recursos e nós gerenciados compatíveis, incluindo acesso, automação, inventário e gerenciamento de patches.

**Função:** Feature flags e configuração dinâmica de aplicações (parte do Systems Manager)

**Well-Architected Tool**

**Função:** Revisão gratuita de cargas contra os 6 pilares ([1.4](../../docs/01-conceitos-de-nuvem/04-well-architected-framework.md))

**AWS Management Console mobile app**

**Função:** Acompanhar recursos, alarmes e Health no celular

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Uma recomendação não é uma quota, e aumentar uma quota não otimiza custo. Gerenciar licença também não compra automaticamente os direitos de uso do software.

## 4. Caso resolvido: ligando as peças

Uma máquina parece maior que o necessário: a equipe avalia recomendações. Se precisa criar mais recursos e encontra uma quota, consulta o limite e a possibilidade de aumento.

**Aplicando a sequência à situação:**

**Etapa 1:** Descubra se o problema é dimensão do recurso, limite de uso ou administração de licença.
**Etapa 2:** Consulte a ferramenta pertinente e os dados que fundamentam a decisão.
**Etapa 3:** Ajuste recursos, solicite aumento elegível ou revise licenças conforme o caso. Essas ações não são intercambiáveis.

**Resultado e responsabilidade:** Compute Optimizer recomenda ajustes de recursos compatíveis; Service Quotas acompanha limites de uso; License Manager ajuda a administrar licenças de software.

**Recursos envolvidos:** Recomendações, quotas e configurações de licenças.

**Decisões que precisam ser tomadas:** Opt-in/métricas, quota ajustável e regra de licença.

**Antes de ler este trecho:**

- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.

**Outra situação comentada:** Instância grande demais: Compute Optimizer; limite da conta: Service Quotas; direito comercial: contrato da licença.

**Por que não concluir mais do que isso:** Quota não garante capacidade disponível; License Manager não compra licença

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Recomendar o tamanho ideal das instâncias com base no uso."

**Resposta curta:** Compute Optimizer.

**Pergunta:** "Pedir aumento do limite de instâncias."

**Resposta curta:** Service Quotas.

**Pergunta:** "Controlar quantas licenças de SQL Server estão em uso."

**Resposta curta:** License Manager.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) · [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) · [License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
