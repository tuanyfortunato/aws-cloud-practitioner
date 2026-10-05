# AWS Elastic Disaster Recovery (AWS DRS)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma falha grave pode interromper os servidores de uma empresa. Ela precisa de uma forma de recuperar suas aplicações na AWS, além de simplesmente guardar arquivos.

**Como este serviço ajuda?** Elastic Disaster Recovery replica dados de servidores compatíveis para preparar sua recuperação em máquinas AWS. O processo inclui configuração, testes e acionamento da recuperação.

**Exemplo do dia a dia:** Uma empresa prepara a recuperação de seu sistema interno e realiza um teste para verificar se consegue iniciar os servidores necessários na AWS.

**O que ele não resolve sozinho?** Replicar dados não garante que todas as dependências e conexões da aplicação estejam prontas. É preciso planejar a recuperação e manter os requisitos do serviço.

**Primeiras palavras para entender:**

- **Desastre:** interrupção grave do ambiente.
- **Replicação:** manter outra cópia atualizada.
- **Recuperação:** voltar a disponibilizar o sistema.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Recuperação de desastres · **Domínio:** 1 (DR) e 3 · **Escopo:** Regional · **Tópico do guia:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)
>
> **Em uma frase:** replica servidores continuamente (on-premises, outra nuvem ou outra região AWS) para a AWS e permite recuperá-los em minutos.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **replicação:** Manutenção de uma cópia dos dados em outro recurso. Se uma alteração incorreta for replicada, a cópia também pode recebê-la; replicação não substitui todo backup.


**Passo 1.** Prepare os servidores compatíveis, permissões e destino de replicação.

**Passo 2.** Mantenha os dados replicados e realize testes de recuperação na AWS. A aplicação precisa ser validada com suas dependências.

**Passo 3.** Durante uma interrupção, acione o procedimento planejado e confira o atendimento. Replicação é a preparação, não a operação completa do negócio.

## 2. Recursos e opções, com significado

### Como funciona

**Antes de ler este trecho:**

- **origem:** Local de onde uma distribuição obtém conteúdo, como um servidor ou bucket. Uma cópia em cache não elimina toda necessidade de acessar a origem.


1. Instala-se o **agente de replicação** nos servidores de origem.

**Antes de ler este trecho:**

- **EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.


2. Os discos são replicados continuamente (nível de bloco) para uma *staging area* barata na AWS (instâncias pequenas + EBS).

**Antes de ler este trecho:**

- **RTO:** Objetivo de tempo de recuperação: quanto tempo a organização aceita ficar sem o sistema após uma interrupção.
- **RPO:** Objetivo de ponto de recuperação: quanto histórico de dados a organização aceita perder, medido como intervalo de tempo.
- **DRS:** Sigla usada para Elastic Disaster Recovery. Replicação prepara uma recuperação; testes e dependências continuam necessários.


3. Em um desastre ou teste, o DRS **lança instâncias de recuperação** totalmente provisionadas — **RPO de segundos (normalmente subsegundo), RTO de minutos** ✔️.

**Antes de ler este trecho:**

- **failback:** Retorno planejado ao ambiente principal depois de uma recuperação. Não deve ser confundido com simplesmente criar uma cópia de dados.


4. Depois, *failback* para a origem.

### Configurações importantes

Point-in-time recovery (útil contra ransomware), *drills* de recuperação sem afetar a produção, launch templates de recuperação.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Replicar dados não garante que todas as dependências e conexões da aplicação estejam prontas. É preciso planejar a recuperação e manter os requisitos do serviço.

### ⚠️ Pegadinhas e não confundir

**Antes de ler este trecho:**

- **AWS Backup:** AWS Backup centraliza políticas e operações de backup para recursos compatíveis.
- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.
- **Application Migration Service:** Application Migration Service replica servidores compatíveis e apoia testes e a transição para execução na AWS.
- **DR:** Recuperação de desastres: plano para recuperar uma operação depois de uma interrupção grave. Inclui recursos, procedimentos e testes.


**DRS** (DR contínuo, RPO/RTO baixos) × **AWS Backup** (backups periódicos) × **Application Migration Service** (migração única — mesma tecnologia, outro objetivo).

**Antes de ler este trecho:**

- **pilot light:** Estratégia de recuperação que mantém uma base essencial ativa e amplia os demais recursos quando necessário. É mais que apenas guardar um backup.
- **warm standby:** Ambiente alternativo reduzido já em execução, que pode ser ampliado na recuperação. O objetivo é reduzir preparação depois da falha.


Estratégias de DR (Backup & Restore → Pilot Light → Warm Standby → Multi-site): DRS se aproxima de *pilot light* com custo baixo.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **servidor:** Computador que atende pedidos de outros computadores. Um servidor web, por exemplo, responde aos pedidos enviados pelo navegador.
- **hora:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.


Por servidor de origem replicado por hora + recursos da staging area e das instâncias lançadas.

## 5. Caso resolvido: ligando as peças

Uma empresa prepara a recuperação de seu sistema interno e realiza um teste para verificar se consegue iniciar os servidores necessários na AWS.

**Aplicando a sequência à situação:**

**Etapa 1:** Prepare os servidores compatíveis, permissões e destino de replicação.
**Etapa 2:** Mantenha os dados replicados e realize testes de recuperação na AWS. A aplicação precisa ser validada com suas dependências.
**Etapa 3:** Durante uma interrupção, acione o procedimento planejado e confira o atendimento. Replicação é a preparação, não a operação completa do negócio.

**Resultado e responsabilidade:** Elastic Disaster Recovery replica dados de servidores compatíveis para preparar sua recuperação em máquinas AWS. O processo inclui configuração, testes e acionamento da recuperação.

**Recursos envolvidos:** Servidores origem, agente, área de staging e recovery instances.

**Decisões que precisam ser tomadas:** Rede de replicação, destino e configuração de lançamento.


**Outra situação comentada:** Recuperar servidores após desastre: DRS; migrar definitivamente: avalie a ferramenta de migração.

**Por que não concluir mais do que isso:** RTO/RPO dependem do ambiente; replicação não substitui backup histórico

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Uma falha grave pode interromper os servidores de uma empresa. Ela precisa de uma forma de recuperar suas aplicações na AWS, além de simplesmente guardar arquivos.

**2. O que a solução fornece?**

Elastic Disaster Recovery replica dados de servidores compatíveis para preparar sua recuperação em máquinas AWS. O processo inclui configuração, testes e acionamento da recuperação.

**3. Que conclusão seria incorreta?**

Replicar dados não garante que todas as dependências e conexões da aplicação estejam prontas. É preciso planejar a recuperação e manter os requisitos do serviço.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Recuperar servidores on-premises na AWS em minutos após um desastre."

**Resposta curta:** Elastic Disaster Recovery.

**Antes de ler este trecho:**

- **Elastic Disaster Recovery:** Elastic Disaster Recovery replica dados de servidores compatíveis para preparar sua recuperação em máquinas AWS.
- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.


**Fundamento explicado no capítulo:** "Recuperar servidores on-premises na AWS em minutos após um desastre." → Elastic Disaster Recovery.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
