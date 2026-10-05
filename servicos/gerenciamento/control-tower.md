# AWS Control Tower

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa quer começar um ambiente com várias contas AWS seguindo uma estrutura organizada e controles comuns, sem montar tudo isoladamente.

**Como este serviço ajuda?** Control Tower ajuda a estabelecer e governar esse ambiente usando serviços AWS integrados e controles compatíveis.

**Exemplo do dia a dia:** A equipe cria uma base para contas de trabalho e utiliza os mecanismos previstos para acompanhar controles no ambiente.

**O que ele não resolve sozinho?** Ele não é uma certificação automática de segurança nem administra toda configuração de cada aplicação. Os controles têm alcances e requisitos diferentes.

**Primeiras palavras para entender:**

- **Landing zone:** base organizada para um ambiente AWS de várias contas.
- **Controle:** regra ou verificação de governança.
- **Governança:** definição e acompanhamento de regras.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Gerenciamento / governança multi-conta · **Domínio:** 2 · **Escopo:** Organização (região *home*) · **Tópico do guia:** [2.4 Governança multi-conta](../../docs/02-seguranca-e-conformidade/04-governanca-multi-conta.md)
>
> **Em uma frase:** monta e governa automaticamente um ambiente multi-conta seguro e padronizado (**landing zone**) sobre o Organizations.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **landing zone:** Base organizada de um ambiente AWS com várias contas e controles. Ainda é necessário definir aplicações, acessos e operação dentro dela.


**Passo 1.** Defina a base de várias contas e os controles necessários para seu ambiente.

**Passo 2.** Estabeleça a landing zone e use os mecanismos compatíveis de criação e governança das contas.

**Passo 3.** Acompanhe controles e mantenha as aplicações dentro das regras. A base não resolve toda configuração específica dos sistemas.

## 2. Recursos e opções, com significado

### O que configura

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **IAM Identity Center:** Serviço de acesso central para a força de trabalho. Atribuições de contas e aplicações não são o cadastro de clientes de um aplicativo.
- **CloudTrail:** Registro de atividades e chamadas AWS compatíveis. Ajuda a analisar quem realizou uma operação, em vez de medir sozinho a velocidade da aplicação.
- **Config:** Serviço que acompanha configurações e suas avaliações em recursos compatíveis. Observar configuração é diferente de observar uma métrica de desempenho.
- **CloudFormation:** Infraestrutura como código descreve recursos em arquivos. CloudFormation usa templates e stacks para criar e administrar recursos compatíveis.
- **conformidade:** Atendimento a requisitos definidos. Usar um serviço com certificações não torna automaticamente a aplicação do cliente conforme.
- **log:** Registro de acontecimentos para análise. A aplicação e os serviços podem produzir registros diferentes; é necessário definir coleta, retenção e acesso.
- **AFT:** Automação de criação e preparação de contas em ambiente Control Tower usando Terraform conforme a solução. Não configura toda aplicação de cada conta.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Item | Detalhe |
|---|---|
| **Landing zone** | Organização com OUs (Security, Sandbox…) e contas compartilhadas: **Log Archive** (logs centralizados de CloudTrail e Config) e **Audit** (acesso de segurança). Integra IAM Identity Center. |
| **Controls (guardrails)** | **Preventivos** (SCPs/RCPs — impedem ações), **detectivos** (regras do **Config** — detectam desvios) e **proativos** (hooks do CloudFormation — barram recursos não conformes antes de criar). Categorias: obrigatórios, fortemente recomendados, eletivos. |
| **Account Factory** | Cria contas novas já no padrão (também via Service Catalog ou **AFT** com Terraform). |
| **Dashboard** | Conformidade de contas e OUs. |
| **Drift detection** | Detecta alterações fora do padrão. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele não é uma certificação automática de segurança nem administra toda configuração de cada aplicação. Os controles têm alcances e requisitos diferentes.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **Organizations:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.
- **Control Tower:** Control Tower ajuda a estabelecer e governar esse ambiente usando serviços AWS integrados e controles compatíveis.


Organizations = estrutura e políticas. Control Tower = **automatiza boas práticas** em cima do Organizations.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.


Sem custo próprio; paga-se os serviços usados (Config, CloudTrail, S3, Service Catalog…).

## 5. Caso resolvido: ligando as peças

A equipe cria uma base para contas de trabalho e utiliza os mecanismos previstos para acompanhar controles no ambiente.

**Aplicando a sequência à situação:**

**Etapa 1:** Defina a base de várias contas e os controles necessários para seu ambiente.
**Etapa 2:** Estabeleça a landing zone e use os mecanismos compatíveis de criação e governança das contas.
**Etapa 3:** Acompanhe controles e mantenha as aplicações dentro das regras. A base não resolve toda configuração específica dos sistemas.

**Resultado e responsabilidade:** Control Tower ajuda a estabelecer e governar esse ambiente usando serviços AWS integrados e controles compatíveis.

**Recursos envolvidos:** Landing zone, contas compartilhadas, OUs e controls.

**Decisões que precisam ser tomadas:** Contas/regiões governadas e controles.

**Antes de ler este trecho:**

- **política:** Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.


**Outra situação comentada:** Criar base padronizada para novas contas: Control Tower, com responsabilidades de governança continuadas.

**Por que não concluir mais do que isso:** Não substitui Organizations nem toda política específica da empresa

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

A empresa quer começar um ambiente com várias contas AWS seguindo uma estrutura organizada e controles comuns, sem montar tudo isoladamente.

**2. O que a solução fornece?**

Control Tower ajuda a estabelecer e governar esse ambiente usando serviços AWS integrados e controles compatíveis.

**3. Que conclusão seria incorreta?**

Ele não é uma certificação automática de segurança nem administra toda configuração de cada aplicação. Os controles têm alcances e requisitos diferentes.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Criar rapidamente um ambiente multi-conta seguro com guardrails."

**Resposta curta:** Control Tower.


**Fundamento explicado no capítulo:** "Criar rapidamente um ambiente multi-conta seguro com guardrails." → Control Tower.

**Pergunta:** "Criar novas contas já seguindo o padrão da empresa."

**Resposta curta:** Account Factory.


**Fundamento explicado no capítulo:** "Criar novas contas já seguindo o padrão da empresa." → Account Factory.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
