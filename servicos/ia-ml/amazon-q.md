# Amazon Q

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma pessoa quer assistência para tarefas de desenvolvimento ou para consultar informações corporativas, conforme seu contexto de trabalho.

**Como este serviço ajuda?** A família Amazon Q inclui assistentes com funções diferentes: Q Developer apoia desenvolvimento; Q Business trabalha com conhecimento corporativo conectado e autorizado.

**Exemplo do dia a dia:** Uma desenvolvedora pede ajuda para entender código. Em outro caso, uma funcionária faz uma pergunta sobre documentos disponibilizados ao assistente corporativo.

**O que ele não resolve sozinho?** Os produtos não acessam automaticamente todo o conhecimento da empresa. Respostas e código precisam ser revisados; fontes, permissões e integrações dependem da modalidade.

**Primeiras palavras para entender:**

- **Assistente:** ferramenta que responde a pedidos.
- **Fonte de dados:** conteúdo disponibilizado ao produto.
- **Contexto:** informação usada para formular a resposta.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** IA generativa / assistentes · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.12 IA e machine learning](../../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)
>
> **Em uma frase:** família de **assistentes de IA generativa** prontos para desenvolvedores e para dados corporativos.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento


**Passo 1.** Escolha o produto do assistente conforme desenvolvimento ou conhecimento corporativo.

**Passo 2.** Prepare o contexto e as integrações autorizadas e faça uma solicitação relacionada à tarefa.

**Passo 3.** Revise a resposta antes de usar. Um assistente não deve ter acesso presumido a todos os documentos nem substituir a validação do trabalho.

## 2. Recursos e opções, com significado

### Variantes

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **QuickSight:** QuickSight oferece análise visual e painéis a partir de fontes de dados compatíveis.
- **Amazon Q / Q:** A família Amazon Q inclui assistentes com funções diferentes: Q Developer apoia desenvolvimento; Q Business trabalha com conhecimento corporativo conectado e autorizado.
- **CLI:** SDK fornece bibliotecas para programas chamarem APIs; CLI fornece comandos de texto. As duas formas continuam exigindo identidade, autorização e configuração.
- **Connect:** Amazon Connect oferece uma plataforma de contact center em nuvem com canais e recursos compatíveis.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **BI:** Análise e apresentação de dados para apoiar decisões. Um painel depende de dados adequados e de uma interpretação correta dos indicadores.
- **IDE:** Ambiente de desenvolvimento com ferramentas para editar e trabalhar com código. Não é necessariamente o local que hospeda a aplicação em produção.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Variante | Para quem | O que faz |
|---|---|---|
| **Amazon Q Developer** (✔️ o CodeWhisperer passou a integrá-lo em 30/04/2024) | Desenvolvedores e times de operação | Sugestões e geração de código na IDE e CLI, agentes que implementam funcionalidades, **varredura de segurança**, upgrade de código (ex.: Java), explicar e diagnosticar recursos e **erros no console AWS**, chat sobre a conta. |
| **Amazon Q Business** | Funcionários | Responde perguntas, resume e gera conteúdo com base nos **dados da empresa** (40+ conectores: S3, SharePoint, Confluence, Salesforce), respeitando permissões. |
| **Amazon Q in QuickSight** | Analistas | BI em linguagem natural. |
| **Amazon Q in Connect** | Agentes de contact center | Respostas e ações sugeridas em tempo real. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Os produtos não acessam automaticamente todo o conhecimento da empresa. Respostas e código precisam ser revisados; fontes, permissões e integrações dependem da modalidade.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### 🔄 Atualizações 2025-2026

**Antes de ler este trecho:**

- **suporte:** Suporte oferece ajuda conforme um plano e suas condições. Um prazo de resposta inicial não é garantia de tempo de resolução de todo incidente.


✔️ Os **plugins de IDE do Amazon Q Developer** têm fim de suporte em **30/04/2027**; a documentação aponta o **Kiro** como alternativa.

**Antes de ler este trecho:**

- **IA:** Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.


**Amazon Q Business** entrou em manutenção e **não aceita novos clientes desde 30/07/2026**; aplicações existentes podem ser **conectadas** ao Amazon Quick Suite. O **Amazon Q** continua na lista oficial: "assistente de IA generativa para funcionários/desenvolvedores" → **Amazon Q**.

## 5. Caso resolvido: ligando as peças

Uma desenvolvedora pede ajuda para entender código. Em outro caso, uma funcionária faz uma pergunta sobre documentos disponibilizados ao assistente corporativo.

**Aplicando a sequência à situação:**

**Etapa 1:** Escolha o produto do assistente conforme desenvolvimento ou conhecimento corporativo.
**Etapa 2:** Prepare o contexto e as integrações autorizadas e faça uma solicitação relacionada à tarefa.
**Etapa 3:** Revise a resposta antes de usar. Um assistente não deve ter acesso presumido a todos os documentos nem substituir a validação do trabalho.

**Resultado e responsabilidade:** A família Amazon Q inclui assistentes com funções diferentes: Q Developer apoia desenvolvimento; Q Business trabalha com conhecimento corporativo conectado e autorizado.

**Recursos envolvidos:** Variantes voltadas a desenvolvimento e ao uso de informações de negócio.

**Decisões que precisam ser tomadas:** Variante, identidades, fontes e permissões.


**Outra situação comentada:** Apoio ao desenvolvedor: Q Developer; informações de negócio dependem da variante e das fontes autorizadas.

**Por que não concluir mais do que isso:** Não é um único banco com acesso automático a todos os documentos da empresa

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Uma pessoa quer assistência para tarefas de desenvolvimento ou para consultar informações corporativas, conforme seu contexto de trabalho.

**2. O que a solução fornece?**

A família Amazon Q inclui assistentes com funções diferentes: Q Developer apoia desenvolvimento; Q Business trabalha com conhecimento corporativo conectado e autorizado.

**3. Que conclusão seria incorreta?**

Os produtos não acessam automaticamente todo o conhecimento da empresa. Respostas e código precisam ser revisados; fontes, permissões e integrações dependem da modalidade.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Assistente de IA generativa para escrever código na IDE."

**Resposta curta:** Amazon Q Developer.


**Fundamento explicado no capítulo:** "Assistente de IA generativa para escrever código na IDE." → Amazon Q Developer.

**Pergunta:** "Assistente que responde com base nos documentos internos da empresa."

**Resposta curta:** Amazon Q Business.


**Fundamento explicado no capítulo:** "Assistente que responde com base nos documentos internos da empresa." → Amazon Q Business.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Amazon Q](https://aws.amazon.com/q/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
