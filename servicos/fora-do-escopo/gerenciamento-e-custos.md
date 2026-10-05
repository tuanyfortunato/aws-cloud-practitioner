# Gerenciamento e custos (Data Lifecycle Manager, Chatbot, Launch Wizard, Application Cost Profiler, DevPay)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Além dos serviços principais, a operação pode precisar administrar cópias de discos, enviar avisos a chats ou apoiar uma implantação específica.

**Como este serviço ajuda?** A ficha reúne ferramentas auxiliares com finalidades diferentes, incluindo opções históricas. Cada seção identifica o trabalho de uma ferramenta.

**Exemplo do dia a dia:** Uma equipe pode querer automatizar o ciclo de cópias de volumes; outra, receber um aviso operacional num chat. São necessidades de operação distintas.

**O que ele não resolve sozinho?** Não escolha uma dessas ferramentas apenas porque a pergunta fala em custo ou gerenciamento. Verifique finalidade, status comercial e escopo; a ficha é de referência.

**Primeiras palavras para entender:**

- **Ciclo de vida:** etapas e regras ao longo do tempo.
- **Notificação:** aviso enviado a um destinatário.
- **Implantação:** colocar recursos ou aplicações em funcionamento.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Gerenciamento e gestão de custos · **Domínio:** — (fora da prova) · **Escopo:** Regional / conta · **Lista oficial:** [fora do escopo](../../docs/00-guia-do-exame/escopo-oficial.md#-fora-do-escopo-lista-oficial-não-exaustiva)
>
> **Em uma frase:** ferramentas auxiliares de operação e de cobrança que existem na AWS, mas não caem na prova.
>
> **Escopo oficial:** ❌ Fora do escopo — documentado só para referência · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> ❌ **Fora do escopo da CLF-C02.** Documentados aqui apenas para referência. Veja também
> [Billing Conductor](../custos/pricing-calculator-cur-e-outras-ferramentas.md) e
> [AWS IQ, Activate e AMS](../custos/recursos-de-ajuda-e-parceiros.md), que também estão fora do escopo.

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **implantação:** Colocar uma versão ou conjunto de recursos em funcionamento. O resultado precisa ser observado e, quando necessário, revertido de modo planejado.


**Passo 1.** Diferencie conservação de cópias, comunicação operacional e assistência de implantação.

**Passo 2.** Use a ferramenta pertinente ao recurso e à tarefa, considerando sua oferta atual.

**Passo 3.** Confira o resultado no ambiente. Um complemento de operação não substitui todas as ferramentas centrais de custo e governança.

## 2. Recursos e opções, com significado

### Amazon Data Lifecycle Manager (DLM)

**Antes de ler este trecho:**

- **EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.
- **retenção:** Tempo durante o qual dados ou registros são conservados. Depois desse prazo, o comportamento depende das regras do serviço e das configurações.


**Automatiza** a criação, retenção, cópia entre regiões e exclusão de **snapshots do EBS** e de **AMIs**, com políticas baseadas em tags.

**Antes de ler este trecho:**

- **AWS Backup:** AWS Backup centraliza políticas e operações de backup para recursos compatíveis.
- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.


Na prova, a resposta para "centralizar backups com políticas" é o **AWS Backup** (no escopo).

### AWS Chatbot (Amazon Q Developer em aplicativos de chat)

**Antes de ler este trecho:**

- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.
- **Budgets:** AWS Budgets compara valores com metas configuradas e pode gerar notificações ou ações compatíveis, conforme as condições definidas.


Recebe **notificações** da AWS (alarmes do CloudWatch, eventos do Health, alertas do Budgets) no **Slack, Microsoft Teams ou Amazon Chime** e permite executar comandos de leitura e operação a partir do chat.

**Antes de ler este trecho:**

- **Amazon Q / Q:** A família Amazon Q inclui assistentes com funções diferentes: Q Developer apoia desenvolvimento; Q Business trabalha com conhecimento corporativo conectado e autorizado.


🔄 Renomeado para **Amazon Q Developer** em 19/02/2025 (no console: "in chat applications").

### AWS Launch Wizard

**Antes de ler este trecho:**

- **Active Directory:** Tecnologia de diretório para identidades, computadores e controles corporativos. É diferente do cadastro de clientes de uma aplicação pública.
- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.
- **SAP:** Tecnologias e aplicações empresariais do ecossistema SAP. Podem exigir requisitos específicos de memória, licenciamento e operação.


Assistente que dimensiona e implanta, com boas práticas, aplicações de terceiros como **SAP, Microsoft SQL Server, Active Directory e Exchange**.

### AWS Application Cost Profiler

Separava o custo de recursos **compartilhados** por **cliente (tenant)** em aplicações multi-tenant, para cobrar ou analisar o custo por cliente.


🔄 **Encerrado em 30/09/2024**.

### Amazon DevPay

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **legado:** Sistema existente com tecnologias ou dependências que precisam ser preservadas ou avaliadas numa mudança. Antigo não significa automaticamente que pode ser desligado.


Serviço **legado** de cobrança para vender AMIs e produtos baseados em S3. Hoje, vender software na AWS é feito pelo **AWS Marketplace** (no escopo).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Não escolha uma dessas ferramentas apenas porque a pergunta fala em custo ou gerenciamento. Verifique finalidade, status comercial e escopo; a ficha é de referência.

### ⚠️ Como isso aparece na prova

**Antes de ler este trecho:**

- **SNS:** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis.


"Centralizar backups" → **AWS Backup**. "Alertas de custo" → **AWS Budgets**. "Notificar o time" → **SNS**.


"Separar custos por cliente ou projeto" → **cost allocation tags** (no escopo).


"Vender software para clientes da AWS" → **AWS Marketplace**.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

## 5. Caso resolvido: ligando as peças

Uma equipe pode querer automatizar o ciclo de cópias de volumes; outra, receber um aviso operacional num chat. São necessidades de operação distintas.

**Aplicando a sequência à situação:**

**Etapa 1:** Diferencie conservação de cópias, comunicação operacional e assistência de implantação.
**Etapa 2:** Use a ferramenta pertinente ao recurso e à tarefa, considerando sua oferta atual.
**Etapa 3:** Confira o resultado no ambiente. Um complemento de operação não substitui todas as ferramentas centrais de custo e governança.

**Resultado e responsabilidade:** A ficha reúne ferramentas auxiliares com finalidades diferentes, incluindo opções históricas. Cada seção identifica o trabalho de uma ferramenta.

**Recursos envolvidos:** Ferramentas extras de lifecycle, chat, implantação e custos.

**Decisões que precisam ser tomadas:** Recurso suportado e disponibilidade do produto.


**Outra situação comentada:** Para orçamento de conta, estude Budgets; ferramenta extra de custo não substitui a escolha pelo requisito.

**Por que não concluir mais do que isso:** Fora do escopo; nomes antigos/renomeados não indicam capacidades novas automaticamente

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Além dos serviços principais, a operação pode precisar administrar cópias de discos, enviar avisos a chats ou apoiar uma implantação específica.

**2. O que a solução fornece?**

A ficha reúne ferramentas auxiliares com finalidades diferentes, incluindo opções históricas. Cada seção identifica o trabalho de uma ferramenta.

**3. Que conclusão seria incorreta?**

Não escolha uma dessas ferramentas apenas porque a pergunta fala em custo ou gerenciamento. Verifique finalidade, status comercial e escopo; a ficha é de referência.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Data Lifecycle Manager](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html) · [Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) · [Launch Wizard](https://aws.amazon.com/launchwizard/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
