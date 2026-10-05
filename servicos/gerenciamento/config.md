# AWS Config

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A equipe precisa acompanhar como as configurações dos recursos mudaram e verificar se elas seguem requisitos definidos.

**Como este serviço ajuda?** AWS Config registra configurações de recursos compatíveis e permite avaliá-las com regras.

**Exemplo do dia a dia:** A escola define uma regra para uma configuração importante e acompanha os recursos avaliados como conformes ou não conformes.

**O que ele não resolve sozinho?** Config observa e avalia configuração; não é o serviço principal para medir lentidão da aplicação. Correções automáticas dependem de remediação configurada.

**Primeiras palavras para entender:**

- **Configuração:** propriedades de um recurso.
- **Regra:** critério de avaliação.
- **Remediação:** ação para corrigir uma condição inadequada.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Gerenciamento / governança e compliance · **Domínio:** 2 · **Escopo:** Regional (agregadores multi-conta/região) · **Tópico do guia:** [2.7 Logs, monitoramento e auditoria](../../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md) · [2.6 Compliance](../../docs/02-seguranca-e-conformidade/06-compliance-e-governanca.md)
>
> **Em uma frase:** registra a **configuração** dos recursos e seu histórico de mudanças, e avalia continuamente se estão **conformes** com regras.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento


**Passo 1.** Selecione os recursos e configurações compatíveis que precisam de acompanhamento.

**Passo 2.** Registre mudanças e aplique regras de avaliação para requisitos definidos.

**Passo 3.** Investigue não conformidades e configure remediação quando apropriado. Avaliar uma configuração e corrigi-la são operações diferentes.

## 2. Recursos e opções, com significado

### Componentes

**Configuration recorder**

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.


**Detalhe:** Registra *configuration items* (estado de cada recurso e relações) — todos os tipos ou selecionados; contínuo ou diário.

**Delivery channel**

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **SNS:** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis.


**Detalhe:** Envia histórico e snapshots para **S3** e notificações para **SNS**.

**Resource timeline**

**Antes de ler este trecho:**

- **CloudTrail:** Registro de atividades e chamadas AWS compatíveis. Ajuda a analisar quem realizou uma operação, em vez de medir sozinho a velocidade da aplicação.
- **security group:** Regras de tráfego associadas a interfaces ou recursos compatíveis. É um controle de rede, não uma permissão IAM para ler um arquivo ou chamar uma API.
- **evento:** Informação sobre algo que aconteceu. Uma regra pode encaminhar o evento; outro componente realiza a ação de negócio.


**Detalhe:** "Como estava este security group na terça passada e quem mudou?" (com link para o evento no CloudTrail).

**Config rules**

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **Config:** Serviço que acompanha configurações e suas avaliações em recursos compatíveis. Observar configuração é diferente de observar uma métrica de desempenho.


**Detalhe:** **Managed rules** (centenas prontas: `s3-bucket-public-read-prohibited`, `encrypted-volumes`, `restricted-ssh`, `root-account-mfa-enabled`…) ou **custom** (Lambda ou Guard). Avaliação por mudança ou periódica.

**Remediation**

**Antes de ler este trecho:**

- **Systems Manager:** Systems Manager reúne ferramentas de operação para recursos e nós gerenciados compatíveis, incluindo acesso, automação, inventário e gerenciamento de patches.


**Detalhe:** Ações corretivas manuais ou **automáticas** via **Systems Manager Automation**.

**Conformance packs**

**Antes de ler este trecho:**

- **CIS / PCI DSS:** Referências, padrões ou requisitos de segurança e conformidade com escopos distintos. A menção de um nome não é certificação automática do cliente; identifique qual requisito a seção aborda.


**Detalhe:** Pacotes de regras + remediações (ex.: boas práticas de PCI DSS, CIS) implantáveis na organização.

**Aggregators**


**Detalhe:** Visão consolidada de várias contas e regiões.

**Advanced query**

**Antes de ler este trecho:**

- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.


**Detalhe:** Consultas SQL sobre o inventário de configuração.

### Quem depende do Config

**Antes de ler este trecho:**

- **Security Hub:** Security Hub reúne achados de fontes compatíveis e oferece avaliações de controles, conforme os recursos habilitados.
- **Audit Manager:** Audit Manager ajuda a coletar e organizar evidências em avaliações baseadas em estruturas de controles compatíveis.
- **Control Tower:** Control Tower ajuda a estabelecer e governar esse ambiente usando serviços AWS integrados e controles compatíveis.
- **firewall:** Controle que permite ou bloqueia comunicação segundo regras. Sua cobertura depende da camada e do ponto em que é aplicado.


**Security Hub** (verificações de padrões), **Firewall Manager**, **Control Tower** (controles detectivos), **Audit Manager**.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Config observa e avalia configuração; não é o serviço principal para medir lentidão da aplicação. Correções automáticas dependem de remediação configurada.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.
- **conformidade:** Atendimento a requisitos definidos. Usar um serviço com certificações não torna automaticamente a aplicação do cliente conforme.


Config (**estado/conformidade**) × CloudTrail (**quem fez**) × CloudWatch (**métricas**).

**Antes de ler este trecho:**

- **SCP:** Política de controle de serviços usada na organização para limitar permissões disponíveis em contas às quais se aplica. Ela não concede acesso ao usuário sozinha.


Config **detecta e pode remediar**; **SCP** previne.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por **configuration item registrado** + por **avaliação de regra** + conformance packs.

## 5. Caso resolvido: ligando as peças

A escola define uma regra para uma configuração importante e acompanha os recursos avaliados como conformes ou não conformes.

**Aplicando a sequência à situação:**

**Etapa 1:** Selecione os recursos e configurações compatíveis que precisam de acompanhamento.
**Etapa 2:** Registre mudanças e aplique regras de avaliação para requisitos definidos.
**Etapa 3:** Investigue não conformidades e configure remediação quando apropriado. Avaliar uma configuração e corrigi-la são operações diferentes.

**Resultado e responsabilidade:** AWS Config registra configurações de recursos compatíveis e permite avaliá-las com regras.

**Recursos envolvidos:** Recorder, configuration items, rules e aggregators.

**Decisões que precisam ser tomadas:** Tipos de recurso, cobertura e regras.

**Antes de ler este trecho:**

- **bucket:** Recipiente que organiza objetos no S3. A aplicação usa o bucket e a identificação do objeto para pedir operações autorizadas.


**Outra situação comentada:** Saber se bucket atende regra e seu estado anterior: Config; quem mudou: CloudTrail.

**Por que não concluir mais do que isso:** Avaliar regra não bloqueia necessariamente criação; remediação depende de integração

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

A equipe precisa acompanhar como as configurações dos recursos mudaram e verificar se elas seguem requisitos definidos.

**2. O que a solução fornece?**

AWS Config registra configurações de recursos compatíveis e permite avaliá-las com regras.

**3. Que conclusão seria incorreta?**

Config observa e avalia configuração; não é o serviço principal para medir lentidão da aplicação. Correções automáticas dependem de remediação configurada.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Histórico de configuração de um recurso e se segue as regras."

**Resposta curta:** AWS Config.

**Antes de ler este trecho:**

- **AWS Config:** AWS Config registra configurações de recursos compatíveis e permite avaliá-las com regras.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.


**Fundamento explicado no capítulo:** "Histórico de configuração de um recurso e se segue as regras." → AWS Config.

**Pergunta:** "Como estava o security group semana passada?"

**Resposta curta:** Config.


**Fundamento explicado no capítulo:** "Como estava o security group semana passada?" → Config.

**Pergunta:** "Verificar continuamente se todos os buckets estão criptografados e corrigir automaticamente."

**Resposta curta:** Config rule + remediação (SSM Automation).

**Antes de ler este trecho:**

- **SSM:** Sigla usada em recursos do Systems Manager. O serviço oferece ferramentas de administração; nós, acessos e conectividade precisam estar preparados.


**Fundamento explicado no capítulo:** "Verificar continuamente se todos os buckets estão criptografados e corrigir automaticamente." → Config rule + remediação (SSM Automation).


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
