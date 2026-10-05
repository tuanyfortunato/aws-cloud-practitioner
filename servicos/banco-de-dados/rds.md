# Amazon RDS (Relational Database Service)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma aplicação precisa guardar registros relacionados, como alunos, cursos e matrículas. Instalar e manter o software do banco numa máquina própria exige trabalho.

**Como este serviço ajuda?** O RDS oferece bancos relacionais gerenciados. Você escolhe um mecanismo compatível, define a estrutura dos dados e usa o banco; a AWS assume tarefas de infraestrutura e administração previstas pelo serviço.

**Exemplo do dia a dia:** O sistema da escola mantém tabelas de alunos e matrículas num banco RDS e consulta quais alunos estão inscritos em cada curso.

**O que ele não resolve sozinho?** RDS não cria as regras de negócio nem as consultas da aplicação. Você continua responsável por dados, acessos e configurações; as opções de disponibilidade e recuperação precisam ser escolhidas.

**Primeiras palavras para entender:**

- **Banco relacional:** dados organizados em tabelas que podem se relacionar.
- **SQL:** linguagem para trabalhar com esses dados.
- **Mecanismo:** software do banco, como PostgreSQL.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Banco de dados relacional gerenciado · **Domínio:** 2 (responsabilidade) e 3 · **Escopo:** Regional (instância numa AZ; Multi-AZ opcional) · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)
>
> **Em uma frase:** banco relacional gerenciado — a AWS cuida de hardware, SO, patches do motor, backups e failover.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **retenção:** Tempo durante o qual dados ou registros são conservados. Depois desse prazo, o comportamento depende das regras do serviço e das configurações.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.


**Passo 1.** Escolha um mecanismo de banco compatível com a aplicação e suas necessidades de capacidade e disponibilidade.

**Passo 2.** Prepare conexão e identidade. Crie as estruturas dos dados e faça a aplicação realizar operações autorizadas.

**Passo 3.** Acompanhe desempenho, retenção e recuperação. A AWS administra tarefas previstas, mas a modelagem e o uso dos dados continuam com o cliente.

## 2. Recursos e opções, com significado

### Para que serve

**Antes de ler este trecho:**

- **OLTP:** Processamento de operações individuais do negócio, como registrar uma compra. É diferente de analisar grandes conjuntos históricos de registros.
- **CRM:** CRM trata relacionamento com clientes; CAD, projeto assistido por computador; EDI, troca eletrônica estruturada de dados. São necessidades de aplicação distintas.
- **ERP:** Tipos de aplicação: gestão de conteúdo, relacionamento com clientes e gestão empresarial. São funções de software, não nomes de um modelo de armazenamento.


Aplicações transacionais (**OLTP**): e-commerce, ERP, CRM, sistemas web.

**Antes de ler este trecho:**

- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.
- **replatform:** Mudar parte da plataforma mantendo boa parte da aplicação. Por exemplo, trocar a operação do banco sem reescrever todas as regras do programa.


**Replatform** de bancos on-premises para reduzir administração.

### Motores

**Antes de ler este trecho:**

- **Aurora:** Aurora é um banco relacional da AWS dentro da família RDS.
- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.


**MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Db2** (e **Aurora**, ver [ficha própria](aurora.md)).

### Conceitos e configurações

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **KMS:** Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.
- **SO:** Software básico da máquina, como Linux ou Windows. Ele administra arquivos, memória e execução de programas; atualizar esse software é diferente de atualizar a aplicação.
- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **AZ:** Parte isolada da infraestrutura dentro de uma região, formada por um ou mais datacenters. Distribuir recursos entre zonas pode reduzir o impacto de uma falha localizada.
- **Multi-AZ:** Configuração que utiliza mais de uma zona de disponibilidade. Seu comportamento depende do serviço: não presuma que toda cópia atende leituras ou que isso é backup de dados apagados.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
- **carga:** Aplicação ou conjunto de tarefas com seus recursos e necessidades. Avaliar uma carga significa avaliar o trabalho completo, não uma única máquina isolada.
- **snapshot:** Cópia de estado de um recurso em determinado momento, conforme o serviço. Restauração pode criar um novo recurso; não presuma uma máquina pronta e instantânea.
- **DR:** Recuperação de desastres: plano para recuperar uma operação depois de uma interrupção grave. Inclui recursos, procedimentos e testes.
- **failover:** Mudança do atendimento para um componente alternativo quando o principal fica indisponível. A forma e o tempo dependem da solução.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **TLS:** HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.
- **DNS:** Sistema que relaciona nomes a informações de endereço e outros registros. Resolver o nome de um site não hospeda o site nem garante que ele está funcionando.
- **subnet:** Segmento de uma rede virtual. Na VPC, uma subnet pertence a uma zona de disponibilidade; suas rotas e controles ajudam a definir a conectividade.
- **endpoint:** Ponto de acesso a um serviço ou componente. Pode ser um endereço de API ou um recurso de conectividade; identifique qual sentido a seção usa.
- **transação:** Conjunto de operações tratado com garantias definidas pelo banco. As garantias e limites variam conforme o serviço e a modalidade.
- **cluster:** Conjunto de recursos que trabalham de forma coordenada. O termo aparece em computação, banco e outras áreas, com papéis diferentes.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.
- **DB:** Abreviação de database, ou banco de dados. Cada mecanismo oferece formas e garantias próprias de armazenamento e consulta.
- **DB cluster:** Conjunto coordenado de componentes de banco. A função de cada membro e seu comportamento de leitura, escrita ou recuperação dependem do serviço.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Item | Detalhe |
|---|---|
| **Instância de banco** | Classe (db.t, db.m, db.r…) e armazenamento (gp2/gp3, io1/io2). **Storage auto scaling** aumenta o disco sozinho. |
| **Multi-AZ (instância)** | Standby **síncrono** em outra AZ, **failover automático** (mesmo endpoint DNS). Standby **não atende leitura**. Objetivo: **disponibilidade**. |
| **Multi-AZ DB cluster** | ✔️ 1 writer + **2 readers** em 3 AZs (RDS for MySQL e PostgreSQL), que também servem de failover. |
| **Read Replicas** | Cópias **assíncronas**, só leitura, na mesma região ou **cross-region**; até **15** (MySQL, MariaDB, PostgreSQL), até **5** (Oracle, SQL Server), até **3** (Db2). Podem ser **promovidas** a banco independente (DR). Objetivo: **escalar leitura**. |
| **Backups automáticos** | Diários + logs de transação → **point-in-time recovery**; retenção de **0 a 35 dias** (0 desativa). |
| **Snapshots manuais** | Persistem até você apagar; copiáveis entre regiões e contas. |
| **Criptografia** | KMS, definida **na criação** (para criptografar um banco existente: snapshot → cópia criptografada → restaurar). TLS em trânsito. |
| **Parameter / option groups** | Configurações do motor. |
| **Janela de manutenção** | Quando a AWS aplica patches do motor/SO. |
| **IAM database authentication** | Login com token IAM (MySQL, PostgreSQL). |
| **RDS Proxy** | Pool de conexões gerenciado (ótimo para Lambda), failover mais rápido. |
| **Blue/Green Deployments** | Ambiente de staging sincronizado para upgrades com troca rápida. |
| **Performance Insights / Enhanced Monitoring** | Diagnóstico de carga e métricas do SO. |
| **RDS Custom** | Oracle e SQL Server **com acesso ao SO** (para customizações que exigem). |
| **Acesso de rede** | Em subnets da VPC (DB subnet group); *publicly accessible* sim/não; security groups. |

### Limites e números

**Antes de ler este trecho:**

- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.


📌 Backup automático até **35 dias**. Read replicas: até **15** (MySQL/MariaDB/PostgreSQL).


🧊 Limites de armazenamento por motor e versões.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

RDS não cria as regras de negócio nem as consultas da aplicação. Você continua responsável por dados, acessos e configurações; as opções de disponibilidade e recuperação precisam ser escolhidas.

### ⚠️ Pegadinhas e não confundir

**Antes de ler este trecho:**

- **read replica:** Cópia de banco que pode atender consultas em cenários suportados. Ela não deve ser confundida com toda modalidade de standby para recuperação.


⚠️ **Multi-AZ = disponibilidade**; **Read Replica = desempenho de leitura**.

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.


Sem acesso ao SO (exceto RDS Custom). Precisa de acesso total ao SO → banco no **EC2**.

**Antes de ler este trecho:**

- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **Redshift:** Redshift é um ambiente de banco voltado à análise de dados, conhecido como data warehouse.
- **NoSQL:** Família de modelos de banco que não se limita à estrutura relacional tradicional. Não significa ausência de estrutura ou que todo produto NoSQL faz o mesmo trabalho.
- **OLAP:** Análise de conjuntos de dados, como comparar vendas de vários meses. Prioriza perguntas e agregações, não apenas registrar uma operação individual.


RDS (OLTP) × Redshift (OLAP) × DynamoDB (NoSQL).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **IOPS:** Quantidade de operações de leitura e escrita por segundo. Ajuda a descrever o comportamento de um armazenamento, mas não mede sozinha a quantidade de bytes transferidos.
- **On-Demand:** Modalidade de uso sem o compromisso de longo prazo descrito por reservas e planos. Cobrança e unidades dependem do recurso contratado.
- **Reserved Instances:** Benefício e condições de reserva para configurações compatíveis. Não confunda desconto com qualquer garantia universal de capacidade.
- **Savings Plans:** Compromisso de gasto por período em troca de condições de preço para uso elegível. Se a necessidade diminuir, o compromisso não desaparece automaticamente.
- **BYOL:** Trazer licença própria elegível. É necessário verificar o direito de uso e as condições do software; a AWS não cria automaticamente essa licença.
- **licença:** Direito de usar um software sob condições. Instalar o programa ou inventariá-lo não concede automaticamente esse direito.
- **provisionado:** Recurso ou capacidade já disponibilizado para uso. Em algumas cobranças, a disponibilidade mantida importa mesmo sem execução de trabalho de negócio.


Horas de instância (On-Demand ou **Reserved Instances** / 🔄 **Database Savings Plans**: até 20% em instâncias provisionadas, 1 ano, sem pagamento adiantado), armazenamento provisionado, IOPS provisionados, backup além do tamanho do banco, transferência de dados, Multi-AZ (≈ dobra a instância), licença (Oracle/SQL Server *license included* ou BYOL).

### Segurança e responsabilidade compartilhada

**Antes de ler este trecho:**

- **patch:** Atualização corretiva de software. A responsabilidade de aplicá-la depende da camada e do serviço usado.


**AWS:** hardware, **SO**, **patch do motor**, backups automáticos, failover Multi-AZ.

**Antes de ler este trecho:**

- **schema:** Estrutura e tipos dos dados. Em migração, adaptar a estrutura é uma tarefa diferente de copiar os registros.


**Cliente:** usuários e permissões do banco, security groups, **ativar criptografia**, configurar backups/retenção, schema, consultas e dados.

## 5. Caso resolvido: ligando as peças


A escola guarda alunos, cursos e matrículas relacionados e seu programa usa consultas SQL de um mecanismo compatível. O objetivo é ter um banco com menos administração de infraestrutura que uma instalação própria na EC2.

A equipe escolhe o mecanismo RDS, prepara capacidade, comunicação e usuários e cria as tabelas. A aplicação consulta e grava registros com suas permissões. A AWS administra as tarefas previstas pelo serviço; a equipe continua definindo os dados e as regras de uso.

Uma opção Multi-AZ ajuda no objetivo de disponibilidade conforme sua modalidade, mas não substitui toda recuperação de um apagamento. Réplicas de leitura atendem outro requisito. Antes de escolher, diferencie continuidade do atendimento, aumento de consultas e retorno a dados de um momento anterior.

**Recursos envolvidos:** DB instance/cluster, engine, endpoint, subnet group, SG e backups.

**Decisões que precisam ser tomadas:** Motor, tamanho, armazenamento, acesso, backup e disponibilidade.

**Antes de ler este trecho:**

- **alta disponibilidade:** Planejamento para manter o sistema acessível diante de determinadas falhas. Não é promessa de ausência de qualquer interrupção.
- **root:** Na conta AWS, é a identidade principal com poderes especiais. Dentro de Linux, root é o administrador do sistema operacional. Administrar Linux não é o mesmo que administrar a conta AWS.


**Outra situação comentada:** Alta disponibilidade: Multi-AZ; aliviar consultas: read replicas compatíveis, distinguindo modalidades de cluster.

**Por que não concluir mais do que isso:** RDS convencional não entrega acesso root irrestrito ao host; Multi-AZ DB instance standby não atende leituras

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Uma aplicação precisa guardar registros relacionados, como alunos, cursos e matrículas. Instalar e manter o software do banco numa máquina própria exige trabalho.

**2. O que a solução fornece?**

O RDS oferece bancos relacionais gerenciados. Você escolhe um mecanismo compatível, define a estrutura dos dados e usa o banco; a AWS assume tarefas de infraestrutura e administração previstas pelo serviço.

**3. Que conclusão seria incorreta?**

RDS não cria as regras de negócio nem as consultas da aplicação. Você continua responsável por dados, acessos e configurações; as opções de disponibilidade e recuperação precisam ser escolhidas.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Vantagem do RDS sobre banco no EC2?"

**Resposta curta:** A AWS cuida de patch, backup, hardware e failover.


**Fundamento explicado no capítulo:** "Vantagem do RDS sobre banco no EC2?" → A AWS cuida de patch, backup, hardware e failover.

**Pergunta:** "Failover automático para outra AZ."

**Resposta curta:** RDS Multi-AZ.


**Fundamento explicado no capítulo:** "Failover automático para outra AZ." → RDS Multi-AZ.

**Pergunta:** "Aliviar consultas de leitura pesadas."

**Resposta curta:** Read Replicas (ou ElastiCache).

**Antes de ler este trecho:**

- **ElastiCache:** ElastiCache fornece armazenamento em memória para manter dados próximos da aplicação e acelerar acessos, conforme o mecanismo e a configuração.


**Fundamento explicado no capítulo:** "Aliviar consultas de leitura pesadas." → Read Replicas (ou ElastiCache).

**Pergunta:** "Restaurar o banco para 10:32 de ontem."

**Resposta curta:** Point-in-time recovery (backups automáticos).


**Fundamento explicado no capítulo:** "Restaurar o banco para 10:32 de ontem." → Point-in-time recovery (backups automáticos).

**Pergunta:** "Muitas conexões curtas de Lambda sobrecarregam o banco."

**Resposta curta:** RDS Proxy.


**Fundamento explicado no capítulo:** "Muitas conexões curtas de Lambda sobrecarregam o banco." → RDS Proxy.

**Pergunta:** "Quem aplica patch no motor do RDS?"

**Resposta curta:** AWS.


**Fundamento explicado no capítulo:** "Quem aplica patch no motor do RDS?" → AWS.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
