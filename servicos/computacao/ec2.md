# Amazon EC2 (Elastic Compute Cloud)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Você tem um programa que precisa ficar funcionando mesmo quando seu computador pessoal está desligado. Comprar uma máquina, instalar tudo e manter essa máquina na empresa dá trabalho.

**Como este serviço ajuda?** O EC2 permite alugar um computador que funciona no datacenter da AWS. Você escolhe a capacidade e o sistema operacional, instala seu programa e decide quem pode acessá-lo. A AWS cuida do equipamento físico; você continua administrando o sistema e a aplicação.

**Exemplo do dia a dia:** Uma escola quer disponibilizar seu sistema de matrícula pela internet. Ela pode instalar esse sistema numa máquina EC2, configurar o acesso e manter o programa funcionando ali. Os alunos usam o sistema; não precisam acessar a máquina como administradores.

**O que ele não resolve sozinho?** Criar a máquina não instala nem publica automaticamente o seu sistema. Você precisa configurá-lo, protegê-lo e atualizá-lo. Parar a máquina também não elimina o custo de todos os recursos associados, como os discos mantidos.

**Primeiras palavras para entender:**

- **Servidor:** computador que atende pedidos de outros computadores.
- **Instância:** uma máquina virtual criada no EC2.
- **Sistema operacional:** software básico da máquina, como Linux ou Windows.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Computação · **Domínio:** 3 (e 4: modelos de compra) · **Escopo:** Regional (cada instância vive numa AZ) · **Tópico do guia:** [3.3 Amazon EC2](../../docs/03-tecnologia-e-servicos/03-ec2.md)
>
> **Em uma frase:** servidores virtuais sob demanda, com controle total do sistema operacional (IaaS).
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Escolha uma imagem de sistema e a capacidade da máquina. Essa combinação define a base em que o programa executará.

**Passo 2.** Prepare disco, conexão de rede e permissões. Instale a aplicação e permita apenas os acessos de que ela precisa.

**Passo 3.** Observe a execução e mantenha o software atualizado. Decida separadamente o destino da máquina e dos dados ao parar ou encerrar.

## 2. Recursos e opções, com significado

### Para que serve

Hospedar aplicações web, back-ends, bancos instalados pelo cliente, servidores de jogos, HPC, treinamento de ML.

Migração **lift-and-shift (Rehost)** de servidores on-premises.

Qualquer carga que exija controle do SO, software legado ou licenças específicas.

### Conceitos e componentes

**Instância**

**O que é:** Servidor virtual. Roda numa **AZ** específica.

**AMI (Amazon Machine Image)**

**O que é:** Modelo com SO + software. Fontes: AWS, Marketplace, comunidade ou sua (personalizada). **AMIs são regionais** — copie para usar em outra região. **EC2 Image Builder** automatiza a criação e atualização.

**Tipo de instância**

**O que é:** Combinação de CPU, memória, rede e armazenamento. Nome `m7g.large` = família **m**, geração **7**, atributo **g** (Graviton), tamanho **large**.

**Key pair**

**O que é:** Chave pública/privada para SSH (Linux) ou para obter a senha de administrador (Windows). A AWS guarda só a pública.

**Security group**

**O que é:** Firewall stateful na interface de rede. Padrão: nega toda entrada, libera toda saída.

**EBS / instance store**

**O que é:** Disco persistente em rede (EBS) ou disco local efêmero (instance store). Ver [EBS](../armazenamento/ebs.md).

**ENI**

**O que é:** Interface de rede virtual (IP privado, IP público, SGs).

**Elastic IP**

**O que é:** IPv4 público estático que pode ser remapeado entre instâncias.

**User data**

**O que é:** Script executado (como root) na **primeira inicialização**.

**Instance metadata (IMDS)**

**O que é:** Endpoint `169.254.169.254` com dados da instância e credenciais temporárias da role. **IMDSv2** (com token) é o recomendado.

**Instance profile**

**O que é:** "Contêiner" da IAM role anexada à instância — forma correta de dar permissões à aplicação.

#### Famílias de instância

| Família | Letras | Uso |
|---|---|---|
| Uso geral | **T** (burstable, créditos de CPU), **M**, Mac | Web, repositórios de código, ambientes de dev |
| Otimizada para computação | **C** | Batch, servidores de jogos, HPC, codificação de mídia, inferência |
| Otimizada para memória | **R**, **X**, z, u (High Memory) | Bancos em memória, SAP HANA, análise em tempo real |
| Computação acelerada | **P**, **G**, **Inf** (Inferentia), **Trn** (Trainium), F (FPGA) | Treino/inferência de ML, gráficos, cálculos científicos |
| Otimizada para armazenamento | **I**, **D**, H | Alto IOPS em disco local, data warehouses, NoSQL, HDFS |
| HPC | **Hpc** | Simulações fortemente acopladas |

**Graviton** (ARM, sufixo `g`): melhor preço/desempenho e menor consumo de energia → pilar **Sustentabilidade**.

**Nitro System:** hipervisor leve + hardware dedicado da AWS; base das instâncias modernas (e requisito para EBS Multi-Attach).

### Configurações e opções importantes

**Tenancy**

**O que faz:** Shared (padrão), **Dedicated Instance** ou **Dedicated Host**

**Quando usar:** Compliance ou licenças por socket/núcleo (Host)

**Placement groups**

**O que faz:** **Cluster** (mesmo rack, baixa latência), **Spread** (hardware distinto, máx. 7 por AZ), **Partition** (até 7 partições por AZ, isoladas — Hadoop, Cassandra, Kafka)

**Quando usar:** HPC (cluster), alta disponibilidade de poucas instâncias críticas (spread)

**Monitoramento detalhado**

**O que faz:** Métricas a cada **1 min** em vez de 5 min (pago)

**Quando usar:** Auto Scaling mais reativo

**Hibernação**

**O que faz:** Salva a RAM no volume EBS raiz (criptografado) e para a instância

**Quando usar:** Aplicações com inicialização demorada

**Termination protection**

**O que faz:** Impede encerrar pelo console/API por engano

**Quando usar:** Instâncias críticas

**Shutdown behavior**

**O que faz:** Ao desligar pelo SO: *stop* ou *terminate*

**EBS-optimized**

**O que faz:** Banda dedicada para EBS (padrão nas instâncias atuais)

**Launch template**

**O que faz:** Modelo versionado de configuração (AMI, tipo, SG, user data…)

**Quando usar:** Usado por Auto Scaling, Spot Fleet, EC2 Fleet

**Session Manager**

**O que faz:** Acesso ao shell sem abrir porta 22 nem bastion

**Quando usar:** Boas práticas de segurança

**EC2 Instance Connect**

**O que faz:** SSH com chave temporária enviada pela API

**Quando usar:** Acesso pontual

#### Ciclo de vida

| Estado | Cobrança de computação | EBS | Instance store | IP público |
|---|---|---|---|---|
| `running` | Sim | Mantido | Mantido | Mantido |
| `stopped` | **Não** (EBS continua cobrado) | Mantido | **Perdido** | Liberado (Elastic IP fica) |
| `hibernated` | Não | Mantido (com a RAM) | Perdido | Liberado |
| `terminated` | Não | Raiz apagado por padrão (*DeleteOnTermination*) | Perdido | Liberado |
| `reboot` | Sim | Mantido | **Mantido** | Mantido |

### Limites e números

📌 Cobrança **por segundo** com **mínimo de 60 s** (maioria das AMIs Linux/Windows).

📌 Spot: até **90%** de desconto, aviso de **2 minutos**.

📌 Métricas padrão a cada **5 min**; detalhado **1 min**. **Memória e disco** exigem o **CloudWatch agent**.

🧊 vCPUs por região (quota em vCPUs, ajustável via Service Quotas), ENIs por tipo, banda por tamanho.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Criar a máquina não instala nem publica automaticamente o seu sistema. Você precisa configurá-lo, protegê-lo e atualizá-lo. Parar a máquina também não elimina o custo de todos os recursos associados, como os discos mantidos.

### ⚠️ Pegadinhas e não confundir

**Dedicated Host × Dedicated Instance:** só o **Host** dá visibilidade de sockets/núcleos (BYOL por núcleo).

**Instance store** perde os dados ao **parar/encerrar** (mas não no reboot).

**Parar** a instância libera o IP público dinâmico — para IP fixo use **Elastic IP**.

"Quem aplica patch no SO da EC2?" → **cliente** (no RDS é a AWS).

EC2 × Lightsail × Elastic Beanstalk: controle total × preço fixo simples × PaaS.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Modelos de compra: On-Demand, Savings Plans, Reserved Instances, Spot, Dedicated Hosts/Instances, Capacity Reservations — ver [4.2](../../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md).

Também cobrados: volumes EBS (provisionados), snapshots, **todo IPv4 público** (por hora), transferência de saída, Elastic IP, monitoramento detalhado, licenças incluídas (Windows, SQL Server, RHEL).

Instância parada não cobra computação, mas o EBS continua cobrado.

### Segurança e responsabilidade compartilhada

**AWS:** hardware, datacenter, rede física, hipervisor (Nitro).

**Cliente:** **patch do SO convidado**, aplicações, security groups, firewall do SO, dados, criptografia de EBS, IAM roles, key pairs.

Boas práticas: IAM role (instance profile) em vez de access keys na instância; IMDSv2; Session Manager; Inspector para vulnerabilidades.

## 5. Caso resolvido: ligando as peças

A escola já tem um programa de matrícula que precisa de Linux e de instalação própria. O objetivo não é guardar somente arquivos: é executar esse programa e atender os alunos. A equipe escolhe EC2 porque precisa administrar esse ambiente.

Ela escolhe uma AMI compatível, isto é, uma base com o sistema; depois um tipo de instância com capacidade adequada. Um volume EBS fornece disco. A conexão de rede permite o caminho dos visitantes; o security group limita tráfego permitido. A aplicação ainda precisa ser instalada e configurada para responder. Se ela chamar serviços AWS, uma role pode fornecer permissões temporárias.

Ao encerrar o estudo, parar a máquina interrompe sua execução nas condições aplicáveis, mas não apaga necessariamente volumes e cópias. Por isso, confira cada recurso conservado. S3 resolveria guardar PDFs, mas não executaria esse programa Linux. Lambda seria outra forma de execução, com modelo e limites diferentes; não é uma troca direta para qualquer servidor.

**Recursos envolvidos:** Instância, AMI, tipo, subnet, security group, volume e role.

**Decisões que precisam ser tomadas:** Sistema operacional, capacidade, rede e persistência.

**Outra situação comentada:** Servidor legado com controle de Linux: EC2; lembre que patch do SO é tarefa do cliente.

**Por que não concluir mais do que isso:** EC2 encerrada não volta a iniciar; volumes preservados e compromissos podem continuar cobrados

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Qual família para aplicação com uso intenso de CPU?"

**Resposta curta:** Otimizada para computação (C).

**Pergunta:** "Qual família para banco em memória?"

**Resposta curta:** Otimizada para memória (R, X).

**Pergunta:** "Qual família para treinar modelos com GPU?"

**Resposta curta:** Computação acelerada (P, G, Trn).

**Pergunta:** "Como instalar pacotes automaticamente no primeiro boot?"

**Resposta curta:** User data.

**Pergunta:** "Como manter IP público fixo ao trocar de instância?"

**Resposta curta:** Elastic IP.

**Fundamento explicado no capítulo:** **Parar** a instância libera o IP público dinâmico — para IP fixo use **Elastic IP**.

**Pergunta:** "Como dar permissão para a aplicação no EC2 ler o S3?"

**Resposta curta:** IAM role (instance profile).

**Pergunta:** "Como acessar a instância sem abrir a porta 22?"

**Resposta curta:** Systems Manager Session Manager.

**Pergunta:** "Instâncias precisam de latência mínima entre si para HPC."

**Resposta curta:** Placement group *cluster*.

**Pergunta:** "Licença Oracle cobrada por núcleo físico."

**Resposta curta:** Dedicated Host.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do usuário do EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)
- [Tipos de instância](https://aws.amazon.com/ec2/instance-types/)
- [Preços do EC2](https://aws.amazon.com/ec2/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
