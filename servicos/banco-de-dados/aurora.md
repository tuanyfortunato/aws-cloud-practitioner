# Amazon Aurora

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma aplicação usa banco relacional e quer uma opção AWS compatível com MySQL ou PostgreSQL, com arquitetura própria para armazenamento e disponibilidade.

**Como este serviço ajuda?** Aurora é um banco relacional da AWS dentro da família RDS. Ele combina compatibilidade com esses mecanismos e uma arquitetura gerenciada com recursos próprios.

**Exemplo do dia a dia:** Uma loja que usa PostgreSQL avalia Aurora PostgreSQL para seu banco de pedidos, verificando a compatibilidade da aplicação e as necessidades de capacidade.

**O que ele não resolve sozinho?** Aurora não é compatível com todos os mecanismos disponíveis no RDS. Compatibilidade também não significa que toda extensão e configuração funcionará sem avaliação.

**Primeiras palavras para entender:**

- **Relacional:** dados em tabelas relacionadas.
- **Compatibilidade:** capacidade de usar interfaces e comportamentos esperados.
- **Réplica de leitura:** cópia usada para consultas.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Banco relacional nativo da AWS · **Domínio:** 3 · **Escopo:** Regional (cluster multi-AZ); Global Database multi-região · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)
>
> **Em uma frase:** banco relacional compatível com MySQL e PostgreSQL, com desempenho e disponibilidade de nível comercial a custo de open source.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.


**Passo 1.** Escolha a compatibilidade MySQL ou PostgreSQL e a modalidade que atende à aplicação.

**Passo 2.** Defina as instâncias ou opções de capacidade, os acessos e os pontos de conexão do conjunto.

**Passo 3.** Distribua leitura e escrita de forma compatível e planeje recuperação. Compatibilidade e arquitetura precisam ser avaliadas antes de migrar.

## 2. Recursos e opções, com significado

### Para que serve

**Antes de ler este trecho:**

- **alta disponibilidade:** Planejamento para manter o sistema acessível diante de determinadas falhas. Não é promessa de ausência de qualquer interrupção.
- **OLTP:** Processamento de operações individuais do negócio, como registrar uma compra. É diferente de analisar grandes conjuntos históricos de registros.


OLTP que exige alto desempenho e alta disponibilidade gerenciada.

**Antes de ler este trecho:**

- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.
- **SCT:** Ferramenta de conversão de estrutura de banco em migrações compatíveis. Nem toda estrutura ou regra da aplicação é convertida automaticamente.
- **DMS:** Database Migration Service: transferência ou replicação de dados entre bancos compatíveis. Conversão de estrutura e ajuste da aplicação são trabalhos relacionados, mas diferentes.


Migrações de Oracle/SQL Server para um motor open source compatível (com DMS + SCT).

### Arquitetura

**Antes de ler este trecho:**

- **Aurora:** Aurora é um banco relacional da AWS dentro da família RDS.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **GiB:** Unidades em escala binária: cada nível corresponde a 1.024 do anterior. MiB e MB não são a mesma unidade; preserve a unidade indicada pelo serviço.
- **failover:** Mudança do atendimento para um componente alternativo quando o principal fica indisponível. A forma e o tempo dependem da solução.
- **endpoint:** Ponto de acesso a um serviço ou componente. Pode ser um endereço de API ou um recurso de conectividade; identifique qual sentido a seção usa.
- **cluster:** Conjunto de recursos que trabalham de forma coordenada. O termo aparece em computação, banco e outras áreas, com papéis diferentes.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.
- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Item | Detalhe |
|---|---|
| **Compatibilidade** | **MySQL** e **PostgreSQL** (a AWS cita até 5x e 3x o desempenho do padrão). |
| **Armazenamento distribuído** | **6 cópias em 3 AZs**, cresce automaticamente (o volume é dividido em segmentos de 10 GiB); tolera perder 2 cópias para escrita e 3 para leitura; *self-healing*. |
| **Cluster** | 1 instância **writer** + até **15 Aurora Replicas** (leitura e failover, normalmente < 30 s). |
| **Endpoints** | *Cluster (writer) endpoint*, *reader endpoint* (balanceia leituras), endpoints customizados. |

### Configurações e opções importantes

**Aurora Serverless v2**

**Antes de ler este trecho:**

- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **ACU:** Unidade de capacidade de determinadas ofertas Aurora. Ela expressa capacidade conforme a oferta; não é uma contagem de usuários do aplicativo.


**Detalhe:** Capacidade em ACUs ajustada automaticamente em segundos, em incrementos de 0,5 ACU; ✔️ com *auto-pause* pode escalar até **0 ACU**.

**Aurora Global Database**

**Antes de ler este trecho:**

- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.
- **replicação:** Manutenção de uma cópia dos dados em outro recurso. Se uma alteração incorreta for replicada, a cópia também pode recebê-la; replicação não substitui todo backup.
- **DR:** Recuperação de desastres: plano para recuperar uma operação depois de uma interrupção grave. Inclui recursos, procedimentos e testes.


**Detalhe:** Replicação entre regiões com lag tipicamente < 1 s; região secundária pode ser promovida (DR) e servir leituras locais.

**Backtrack (MySQL)**

**Antes de ler este trecho:**

- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.


**Detalhe:** "Voltar no tempo" o cluster sem restaurar backup.

**Cloning**


**Detalhe:** Cópia rápida *copy-on-write* para testes.

**Configuração de storage**


**Detalhe:** *Standard* (paga por I/O) ou *I/O-Optimized* (sem cobrança por I/O, para cargas intensivas).

**Zero-ETL com Redshift**

**Antes de ler este trecho:**

- **Redshift:** Redshift é um ambiente de banco voltado à análise de dados, conhecido como data warehouse.


**Detalhe:** Replicação quase em tempo real para análise.

**Aurora DSQL**

**Antes de ler este trecho:**

- **ativo-ativo:** Mais de um ambiente atende ao mesmo tempo. Isso exige tratar distribuição de tráfego e consistência dos dados conforme a aplicação.
- **DSQL:** Nome de uma oferta distribuída de SQL da família Aurora. Sua arquitetura e compatibilidade precisam ser avaliadas separadamente das demais modalidades Aurora.


**Detalhe:** 🔄 Banco SQL distribuído, serverless, ativo-ativo multi-região (2025) — 🧊 fora da prova.

### Limites e números

📌 **6 cópias / 3 AZs**, **15 réplicas**.


🧊 Tamanho máximo do volume, limites de ACU.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

**Antes de ler este trecho:**

- **RDS:** O RDS oferece bancos relacionais gerenciados.


Aurora não é compatível com todos os mecanismos disponíveis no RDS. Compatibilidade também não significa que toda extensão e configuração funcionará sem avaliação.

### ⚠️ Pegadinhas e não confundir

Aurora × RDS: Aurora é motor próprio da AWS (MySQL/PostgreSQL), mais rápido e resiliente; RDS oferece vários motores comerciais e open source.


"Relacional + máxima disponibilidade gerenciada + compatível com MySQL" → **Aurora**.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Instâncias (ou ACU-hora no Serverless), armazenamento GB-mês, I/O (configuração Standard), backup extra, transferência; replicação do Global Database.

### Segurança e responsabilidade compartilhada

**Antes de ler este trecho:**

- **SO:** Software básico da máquina, como Linux ou Windows. Ele administra arquivos, memória e execução de programas; atualizar esse software é diferente de atualizar a aplicação.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.
- **patch:** Atualização corretiva de software. A responsabilidade de aplicá-la depende da camada e do serviço usado.


Igual ao [RDS](rds.md): AWS cuida de infra, SO, patch, replicação de armazenamento; cliente de usuários, acesso de rede, criptografia, dados.

## 5. Caso resolvido: ligando as peças

Uma loja que usa PostgreSQL avalia Aurora PostgreSQL para seu banco de pedidos, verificando a compatibilidade da aplicação e as necessidades de capacidade.

**Aplicando a sequência à situação:**

**Etapa 1:** Escolha a compatibilidade MySQL ou PostgreSQL e a modalidade que atende à aplicação.
**Etapa 2:** Defina as instâncias ou opções de capacidade, os acessos e os pontos de conexão do conjunto.
**Etapa 3:** Distribua leitura e escrita de forma compatível e planeje recuperação. Compatibilidade e arquitetura precisam ser avaliadas antes de migrar.

**Resultado e responsabilidade:** Aurora é um banco relacional da AWS dentro da família RDS. Ele combina compatibilidade com esses mecanismos e uma arquitetura gerenciada com recursos próprios.

**Recursos envolvidos:** Cluster, writer, readers, endpoints e armazenamento compartilhado.

**Decisões que precisam ser tomadas:** Compatibilidade MySQL/PostgreSQL, capacidade e disponibilidade.


**Outra situação comentada:** Relacional compatível MySQL com leitores: Aurora; não confunda reader com writer.

**Por que não concluir mais do que isso:** Não é engine compatível com qualquer banco SQL; endpoints e opções dependem da configuração

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Uma aplicação usa banco relacional e quer uma opção AWS compatível com MySQL ou PostgreSQL, com arquitetura própria para armazenamento e disponibilidade.

**2. O que a solução fornece?**

Aurora é um banco relacional da AWS dentro da família RDS. Ele combina compatibilidade com esses mecanismos e uma arquitetura gerenciada com recursos próprios.

**3. Que conclusão seria incorreta?**

Aurora não é compatível com todos os mecanismos disponíveis no RDS. Compatibilidade também não significa que toda extensão e configuração funcionará sem avaliação.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Banco relacional compatível com MySQL/PostgreSQL de maior desempenho."

**Resposta curta:** Aurora.


**Fundamento explicado no capítulo:** "Banco relacional compatível com MySQL/PostgreSQL de maior desempenho." → Aurora.

**Pergunta:** "Quantas cópias dos dados o Aurora mantém?"

**Resposta curta:** 6 cópias em 3 AZs.


**Fundamento explicado no capítulo:** "Quantas cópias dos dados o Aurora mantém?" → 6 cópias em 3 AZs.

**Pergunta:** "Banco relacional com leituras de baixa latência em várias regiões e DR."

**Resposta curta:** Aurora Global Database.

**Antes de ler este trecho:**

- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.


**Fundamento explicado no capítulo:** "Banco relacional com leituras de baixa latência em várias regiões e DR." → Aurora Global Database.

**Pergunta:** "Carga intermitente sem gerenciar capacidade."

**Resposta curta:** Aurora Serverless.

**Antes de ler este trecho:**

- **carga:** Aplicação ou conjunto de tarefas com seus recursos e necessidades. Avaliar uma carga significa avaliar o trabalho completo, não uma única máquina isolada.


**Fundamento explicado no capítulo:** "Carga intermitente sem gerenciar capacidade." → Aurora Serverless.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
