# Migration Evaluator, Application Discovery Service e Migration Hub

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Antes de mover sistemas para a AWS, a empresa precisa saber o que tem, suas dependências, custos e o andamento da migração.

**Como este serviço ajuda?** A ficha distingue descoberta do ambiente, avaliação econômica e acompanhamento da migração. Essas ferramentas ajudam a planejar e acompanhar o trabalho.

**Exemplo do dia a dia:** Uma empresa inventaria seus servidores e avalia o uso atual para preparar uma estimativa e uma sequência de migração.

**O que ele não resolve sozinho?** Planejar e acompanhar não significa transferir automaticamente todas as aplicações. Algumas ofertas têm restrições para novos clientes, descritas no conteúdo da ficha.

**Primeiras palavras para entender:**

- **Inventário:** lista de recursos.
- **Dependência:** recurso de que outro precisa.
- **Migração:** mudança de um sistema para outro ambiente.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Migração / avaliação e planejamento · **Domínio:** 1 (migração) e 3 · **Escopo:** Regional · **Tópico do guia:** [3.17 Migração e transferência](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md) · [1.6 Estratégias de migração](../../docs/01-conceitos-de-nuvem/06-estrategias-de-migracao.md)
>
> **Em uma frase:** as ferramentas das fases **avaliar → planejar → acompanhar** de uma migração.
>
> **Escopo oficial:** ✅ No escopo (Migration Hub e Application Discovery Service fechados a novos clientes) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Levante recursos, dependências e necessidades do ambiente atual.

**Passo 2.** Use a ferramenta compatível para descoberta, avaliação de custos ou acompanhamento da mudança.

**Passo 3.** Organize o plano e valide as hipóteses. Inventário e acompanhamento não transferem sozinhos a aplicação.

## 2. Recursos e opções, com significado

### Comparação

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **workflow:** Fluxo de trabalho descrito por etapas, decisões e estados. Coordenar etapas é diferente de escrever o programa que realiza cada tarefa.
- **TCO:** Custo total de propriedade: inclui infraestrutura e operação, não apenas o preço de uma máquina. A comparação depende das hipóteses adotadas.
- **rightsizing:** Ajustar capacidade à necessidade observada. Reduzir demais pode prejudicar a aplicação; a recomendação precisa ser avaliada pelo uso real.
- **MGN:** Sigla usada para Application Migration Service. Apoia a migração de servidores compatíveis; não reescreve automaticamente a aplicação.
- **DMS:** Database Migration Service: transferência ou replicação de dados entre bancos compatíveis. Conversão de estrutura e ajuste da aplicação são trabalhos relacionados, mas diferentes.

| Serviço | Fase | O que faz | Detalhes |
|---|---|---|---|
| **Migration Evaluator** (antigo TSO Logic) | Avaliar | Monta o **caso de negócio (TCO)**: quanto custaria o ambiente atual na AWS | Coletor sem agente ou importação de inventário; recomendações de *rightsizing* e licenças; **gratuito** |
| **AWS Application Discovery Service** | Avaliar | Levanta **inventário**, **uso** e **dependências** entre servidores on-premises | **Agentless Collector** (VMware) ou **Discovery Agent** (físicos/VMs, mais detalhado: processos e conexões de rede); dados vão para o Migration Hub |
| **AWS Migration Hub** | Acompanhar | **Painel único** do progresso de migrações feitas com várias ferramentas (MGN, DMS, parceiros) | Agrupamento em aplicações, *Strategy Recommendations* (sugere o "R" de cada aplicação), *Orchestrator* (modelos de workflow) |

### Sequência típica de migração

1. **Avaliar:** Migration Evaluator (custo) + Application Discovery Service (inventário e dependências).

**Antes de ler este trecho:**

- **Control Tower:** Control Tower ajuda a estabelecer e governar esse ambiente usando serviços AWS integrados e controles compatíveis.
- **landing zone:** Base organizada de um ambiente AWS com várias contas e controles. Ainda é necessário definir aplicações, acessos e operação dentro dela.

2. **Mobilizar/planejar:** Migration Hub, escolha dos 7 Rs, landing zone (Control Tower).

**Antes de ler este trecho:**

- **Application Migration Service:** Application Migration Service replica servidores compatíveis e apoia testes e a transição para execução na AWS.
- **SCT:** Ferramenta de conversão de estrutura de banco em migrações compatíveis. Nem toda estrutura ou regra da aplicação é convertida automaticamente.

3. **Migrar:** [Application Migration Service](application-migration-service.md), [DMS/SCT](dms-e-sct.md), [DataSync/Snow](datasync-e-transfer-family.md).

4. **Acompanhar:** Migration Hub.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Planejar e acompanhar não significa transferir automaticamente todas as aplicações. Algumas ofertas têm restrições para novos clientes, descritas no conteúdo da ficha.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### 🔄 Atualizações 2025-2026

**AWS Migration Hub** e **AWS Application Discovery Service** estão **fechados a novos clientes desde 07/11/2025**, mas continuam na lista oficial da prova — estude a função de cada um.

**Migration Evaluator** entrou explicitamente na lista de serviços no escopo.

**Antes de ler este trecho:**

- **IA:** Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.

A AWS lançou o **AWS Transform**, que usa agentes de IA generativa para acelerar migrações e modernizações (VMware, mainframe, .NET, Java) — 🧊 fora da prova.

## 5. Caso resolvido: ligando as peças

Uma empresa inventaria seus servidores e avalia o uso atual para preparar uma estimativa e uma sequência de migração.

**Aplicando a sequência à situação:**

**Etapa 1:** Levante recursos, dependências e necessidades do ambiente atual.
**Etapa 2:** Use a ferramenta compatível para descoberta, avaliação de custos ou acompanhamento da mudança.
**Etapa 3:** Organize o plano e valide as hipóteses. Inventário e acompanhamento não transferem sozinhos a aplicação.

**Resultado e responsabilidade:** A ficha distingue descoberta do ambiente, avaliação econômica e acompanhamento da migração. Essas ferramentas ajudam a planejar e acompanhar o trabalho.

**Recursos envolvidos:** Inventário/dependências, avaliações e acompanhamento de migração.

**Decisões que precisam ser tomadas:** Fontes, acesso e disponibilidade de cada produto.

**Antes de ler este trecho:**

- **carga:** Aplicação ou conjunto de tarefas com seus recursos e necessidades. Avaliar uma carga significa avaliar o trabalho completo, não uma única máquina isolada.

**Outra situação comentada:** Mapear dependências antes de mover servidores: Discovery; custo do cenário: Evaluator.

**Por que não concluir mais do que isso:** Planejar/acompanhamento não move toda carga; produtos podem estar fechados a novos clientes

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Estimar quanto a empresa vai economizar ao migrar."

**Resposta curta:** Migration Evaluator.

**Pergunta:** "Levantar servidores e dependências antes de migrar."

**Resposta curta:** Application Discovery Service.

**Pergunta:** "Acompanhar todas as migrações num painel central."

**Resposta curta:** Migration Hub.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Migration Evaluator](https://aws.amazon.com/migration-evaluator/) · [Application Discovery Service](https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html) · [Migration Hub](https://docs.aws.amazon.com/migrationhub/latest/ug/whatishub.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
