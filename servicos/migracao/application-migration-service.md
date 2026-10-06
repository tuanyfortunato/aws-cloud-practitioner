# AWS Application Migration Service (AWS MGN)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa quer mover servidores existentes para a AWS mantendo inicialmente boa parte de sua aplicação e configuração, sem reescrever tudo antes da mudança.

**Como este serviço ajuda?** Application Migration Service replica servidores compatíveis e apoia testes e a transição para execução na AWS.

**Exemplo do dia a dia:** A equipe replica um servidor do sistema interno, testa sua execução na AWS e planeja o momento de trocar o ambiente em uso.

**O que ele não resolve sozinho?** Replicar não moderniza automaticamente o programa nem garante que bancos, DNS e integrações externas estejam prontos. A migração precisa ser testada.

**Primeiras palavras para entender:**

- **Rehost:** mover com poucas mudanças iniciais.
- **Replicação:** cópia contínua de dados.
- **Cutover:** troca para o ambiente de destino.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Migração de servidores · **Domínio:** 1 (Rehost) e 3 · **Escopo:** Regional · **Tópico do guia:** [3.17 Migração e transferência](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md)
>
> **Em uma frase:** migração **lift-and-shift (Rehost)** de servidores físicos, virtuais ou de outras nuvens para EC2, com mínima indisponibilidade.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **servidor:** Computador que atende pedidos de outros computadores. Um servidor web, por exemplo, responde aos pedidos enviados pelo navegador.
- **replicação:** Manutenção de uma cópia dos dados em outro recurso. Se uma alteração incorreta for replicada, a cópia também pode recebê-la; replicação não substitui todo backup.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.

**Passo 1.** Prepare servidores compatíveis e o destino de replicação.

**Passo 2.** Replique dados e teste a execução no destino com as dependências da aplicação.

**Passo 3.** Planeje e realize a troca do ambiente em uso. Mover o servidor não dispensa validar rede, dados e integrações.

## 2. Recursos e opções, com significado

### Como funciona

**Antes de ler este trecho:**

- **origem:** Local de onde uma distribuição obtém conteúdo, como um servidor ou bucket. Uma cópia em cache não elimina toda necessidade de acessar a origem.

1. Instala o **agente de replicação** no servidor de origem (Windows/Linux).

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.

2. Replicação **contínua em nível de bloco** para uma *staging area* na AWS.

3. **Instâncias de teste** sem afetar a origem.

**Antes de ler este trecho:**

- **cutover:** Momento planejado de trocar o ambiente em uso pelo destino da migração. Requer validar dependências e planejar a transição dos dados.

4. **Cutover**: lança as instâncias finais em minutos; a origem pode ser desligada.

5. Ações pós-lançamento automatizam ajustes (instalar agentes, converter licenças, modernizar).

### 🔄 Nome atual

**Antes de ler este trecho:**

- **AWS Application Migration Service / Application Migration Service:** Application Migration Service replica servidores compatíveis e apoia testes e a transição para execução na AWS.
- **MGN:** Sigla usada para Application Migration Service. Apoia a migração de servidores compatíveis; não reescreve automaticamente a aplicação.

O serviço hoje se chama **AWS Transform MGN**. O exam guide e a lista de serviços ainda usam **AWS Application Migration Service** — é esse o nome que aparece na prova.

### Destaques

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.

Suporta qualquer aplicação/banco que rode no servidor; converte automaticamente para rodar em EC2.

**Gratuito por 2.160 horas (90 dias de uso contínuo) por servidor de origem** (paga só os recursos de staging e as instâncias).

**Antes de ler este trecho:**

- **SMS:** Mensagem de texto para dispositivos móveis. Integrações e condições de envio são diferentes de e-mail e de entrega a uma fila.

Substitui o antigo CloudEndure Migration e o Server Migration Service (SMS).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

**Antes de ler este trecho:**

- **DNS:** Sistema que relaciona nomes a informações de endereço e outros registros. Resolver o nome de um site não hospeda o site nem garante que ele está funcionando.

Replicar não moderniza automaticamente o programa nem garante que bancos, DNS e integrações externas estejam prontos. A migração precisa ser testada.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **Elastic Disaster Recovery:** Elastic Disaster Recovery replica dados de servidores compatíveis para preparar sua recuperação em máquinas AWS.
- **DR:** Recuperação de desastres: plano para recuperar uma operação depois de uma interrupção grave. Inclui recursos, procedimentos e testes.
- **DMS:** Database Migration Service: transferência ou replicação de dados entre bancos compatíveis. Conversão de estrutura e ajuste da aplicação são trabalhos relacionados, mas diferentes.

**MGN** (servidores inteiros) × **DMS** (bancos de dados) × **Elastic Disaster Recovery** (mesma tecnologia, objetivo de DR contínuo).

## 4. Caso resolvido: ligando as peças

A equipe replica um servidor do sistema interno, testa sua execução na AWS e planeja o momento de trocar o ambiente em uso.

**Aplicando a sequência à situação:**

**Etapa 1:** Prepare servidores compatíveis e o destino de replicação.
**Etapa 2:** Replique dados e teste a execução no destino com as dependências da aplicação.
**Etapa 3:** Planeje e realize a troca do ambiente em uso. Mover o servidor não dispensa validar rede, dados e integrações.

**Resultado e responsabilidade:** Application Migration Service replica servidores compatíveis e apoia testes e a transição para execução na AWS.

**Recursos envolvidos:** Servidores origem, replicação, staging e launch settings.

**Decisões que precisam ser tomadas:** Rede, agente, destino, teste e cutover.

**Outra situação comentada:** Mover servidor como está: Application Migration Service; copiar banco e converter esquema: outras ferramentas.

**Por que não concluir mais do que isso:** Não refatora aplicação nem elimina teste; nomes comerciais podem mudar

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Migrar servidores físicos e VMs para EC2 sem mudar nada, com pouca indisponibilidade."

**Resposta curta:** Application Migration Service.

**Pergunta:** "Ferramenta da estratégia Rehost."

**Resposta curta:** Application Migration Service.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Application Migration Service](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
