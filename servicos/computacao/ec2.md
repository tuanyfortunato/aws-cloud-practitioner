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

**Antes de ler este trecho:**

- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **imagem:** Pacote ou modelo usado para iniciar um ambiente. Em EC2, a AMI é uma imagem de máquina; em containers, a imagem serve para iniciar containers.

**Passo 1.** Escolha uma imagem de sistema e a capacidade da máquina. Essa combinação define a base em que o programa executará.

**Passo 2.** Prepare disco, conexão de rede e permissões. Instale a aplicação e permita apenas os acessos de que ela precisa.

**Passo 3.** Observe a execução e mantenha o software atualizado. Decida separadamente o destino da máquina e dos dados ao parar ou encerrar.

## 2. Recursos e opções, com significado

### Para que serve

**Antes de ler este trecho:**

- **HPC:** Computação de alto desempenho: execução de cálculos intensivos, como simulações. O requisito concreto pode envolver processamento, comunicação ou outro recurso.
- **ML:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.
- **treinamento:** Ajuste de um modelo com dados. É uma etapa diferente de utilizar o modelo já treinado para responder a uma nova entrada.

Hospedar aplicações web, back-ends, bancos instalados pelo cliente, servidores de jogos, HPC, treinamento de ML.

**Antes de ler este trecho:**

- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.
- **rehost / lift-and-shift:** Mover um sistema com poucas mudanças iniciais. A infraestrutura muda, mas isso não moderniza automaticamente o software.

Migração **lift-and-shift (Rehost)** de servidores on-premises.

**Antes de ler este trecho:**

- **SO:** Software básico da máquina, como Linux ou Windows. Ele administra arquivos, memória e execução de programas; atualizar esse software é diferente de atualizar a aplicação.
- **carga:** Aplicação ou conjunto de tarefas com seus recursos e necessidades. Avaliar uma carga significa avaliar o trabalho completo, não uma única máquina isolada.
- **legado:** Sistema existente com tecnologias ou dependências que precisam ser preservadas ou avaliadas numa mudança. Antigo não significa automaticamente que pode ser desligado.

Qualquer carga que exija controle do SO, software legado ou licenças específicas.

### Conceitos e componentes

**Instância**

**Antes de ler este trecho:**

- **servidor:** Computador que atende pedidos de outros computadores. Um servidor web, por exemplo, responde aos pedidos enviados pelo navegador.
- **virtual:** Um recurso virtual é criado por software sobre equipamentos físicos. VM significa máquina virtual: computador lógico com sistema operacional e recursos de processamento.
- **AZ:** Parte isolada da infraestrutura dentro de uma região, formada por um ou mais datacenters. Distribuir recursos entre zonas pode reduzir o impacto de uma falha localizada.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.

**O que é:** Servidor virtual. Roda numa **AZ** específica.

**AMI (Amazon Machine Image)**

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.
- **AMI:** Imagem de máquina EC2: modelo com o software necessário para iniciar uma instância. A imagem precisa ser compatível com a configuração de execução escolhida.

**O que é:** Modelo com SO + software. Fontes: AWS, Marketplace, comunidade ou sua (personalizada). **AMIs são regionais** — copie para usar em outra região. **EC2 Image Builder** automatiza a criação e atualização.

**Tipo de instância**

**Antes de ler este trecho:**

- **CPU:** CPU é o processador que executa instruções. vCPU é a unidade de processamento virtual apresentada ao ambiente. Mais processamento não resolve automaticamente falta de memória ou de velocidade do disco.
- **memória:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.
- **atributo:** Informação nomeada dentro de um registro, como nome ou data. Consultas usam os campos conforme a estrutura e o modelo do banco.
- **Graviton:** Família de processadores AWS baseada em arquitetura ARM. A aplicação e sua imagem precisam ser compatíveis com essa arquitetura.

**O que é:** Combinação de CPU, memória, rede e armazenamento. Nome `m7g.large` = família **m**, geração **7**, atributo **g** (Graviton), tamanho **large**.

**Key pair**

**Antes de ler este trecho:**

- **SSH:** Protocolo para acesso remoto protegido, comum na administração de Linux. Permissão para conectar pela rede e autorização para entrar no sistema são coisas diferentes.
- **key pair:** Par de chaves usado em mecanismos de acesso: uma parte pública e uma privada. A parte privada precisa ser protegida pelo cliente.
- **chave:** Pode indicar identificação de um registro, identificação de um objeto ou elemento criptográfico. Leia o contexto: localizar um dado e protegê-lo são tarefas diferentes.

**O que é:** Chave pública/privada para SSH (Linux) ou para obter a senha de administrador (Windows). A AWS guarda só a pública.

**Security group**

**Antes de ler este trecho:**

- **security group:** Regras de tráfego associadas a interfaces ou recursos compatíveis. É um controle de rede, não uma permissão IAM para ler um arquivo ou chamar uma API.
- **stateful:** Controle que acompanha o estado da comunicação e trata respostas conforme esse estado. No security group, isso evita exigir uma regra independente para a resposta de uma conexão permitida.
- **firewall:** Controle que permite ou bloqueia comunicação segundo regras. Sua cobertura depende da camada e do ponto em que é aplicado.

**O que é:** Firewall stateful na interface de rede. Padrão: nega toda entrada, libera toda saída.

**EBS / instance store**

**Antes de ler este trecho:**

- **EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.
- **instance store:** Armazenamento local temporário da máquina física. Não é lugar seguro para a única cópia de dados que precisam sobreviver às ações descritas no ciclo de vida.

**O que é:** Disco persistente em rede (EBS) ou disco local efêmero (instance store). Ver [EBS](../armazenamento/ebs.md).

**ENI**

**Antes de ler este trecho:**

- **IP:** Endereços usados para identificar interfaces e destinos na rede. IPv4 e IPv6 são versões diferentes; ter um endereço não concede permissão nem garante uma rota.
- **ENI:** Interface de rede virtual. Ela associa endereços e configurações de comunicação a recursos compatíveis.

**O que é:** Interface de rede virtual (IP privado, IP público, SGs).

**Elastic IP**

**O que é:** IPv4 público estático que pode ser remapeado entre instâncias.

**User data**

**Antes de ler este trecho:**

- **root:** Na conta AWS, é a identidade principal com poderes especiais. Dentro de Linux, root é o administrador do sistema operacional. Administrar Linux não é o mesmo que administrar a conta AWS.
- **user data:** Dados ou instruções fornecidos à inicialização da máquina. Um script configurado pode preparar o ambiente; ele não instala qualquer sistema sem você descrever as ações.
- **script:** Programa de instruções usado para automatizar tarefas. O script realiza o que foi descrito; não decide sozinho como instalar ou proteger qualquer sistema.

**O que é:** Script executado (como root) na **primeira inicialização**.

**Instance metadata (IMDS)**

**Antes de ler este trecho:**

- **endpoint:** Ponto de acesso a um serviço ou componente. Pode ser um endereço de API ou um recurso de conectividade; identifique qual sentido a seção usa.
- **credenciais:** Informações usadas para comprovar ou representar uma identidade. Credenciais temporárias expiram; credenciais de longa duração precisam de proteção e administração.
- **role:** Papel que fornece permissões a uma sessão que o assume. O termo função IAM não significa um trecho de código como uma função Lambda.
- **IMDS / IMDSv2:** Serviço de metadados da instância. A versão 2 usa um mecanismo de token; metadados e credenciais devem ser usados conforme as recomendações de segurança.

**O que é:** Endpoint `169.254.169.254` com dados da instância e credenciais temporárias da role. **IMDSv2** (com token) é o recomendado.

**Instance profile**

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **instance profile:** Forma de associar uma role IAM a uma máquina EC2. A aplicação obtém permissões temporárias em vez de manter chaves fixas no código.

**O que é:** "Contêiner" da IAM role anexada à instância — forma correta de dar permissões à aplicação.

#### Famílias de instância

**Antes de ler este trecho:**

- **Batch:** O AWS Batch organiza trabalhos em filas e fornece capacidade de computação para executá-los conforme as configurações.
- **IOPS:** Quantidade de operações de leitura e escrita por segundo. Ajuda a descrever o comportamento de um armazenamento, mas não mede sozinha a quantidade de bytes transferidos.
- **NoSQL:** Família de modelos de banco que não se limita à estrutura relacional tradicional. Não significa ausência de estrutura ou que todo produto NoSQL faz o mesmo trabalho.
- **inferência:** Uso de um modelo para produzir um resultado com uma nova entrada. Pode acontecer sem um novo treinamento em cada solicitação.
- **burstable:** Capacidade com comportamento de créditos para atender uso acima de determinada base, conforme a modalidade. Avalie uso sustentado, créditos e cobrança aplicáveis.
- **HDFS:** Sistema de arquivos distribuído do ecossistema Hadoop. Divide armazenamento entre nós; não é o mesmo modelo de objetos S3.
- **HANA / SAP:** Tecnologias e aplicações empresariais do ecossistema SAP. Podem exigir requisitos específicos de memória, licenciamento e operação.
- **FPGA:** Hardware programável para tarefas especializadas. A escolha precisa de software e requisitos compatíveis; não é necessário para todo processamento.

| Família | Letras | Uso |
|---|---|---|
| Uso geral | **T** (burstable, créditos de CPU), **M**, Mac | Web, repositórios de código, ambientes de dev |
| Otimizada para computação | **C** | Batch, servidores de jogos, HPC, codificação de mídia, inferência |
| Otimizada para memória | **R**, **X**, z, u (High Memory) | Bancos em memória, SAP HANA, análise em tempo real |
| Computação acelerada | **P**, **G**, **Inf** (Inferentia), **Trn** (Trainium), F (FPGA) | Treino/inferência de ML, gráficos, cálculos científicos |
| Otimizada para armazenamento | **I**, **D**, H | Alto IOPS em disco local, data warehouses, NoSQL, HDFS |
| HPC | **Hpc** | Simulações fortemente acopladas |

**Antes de ler este trecho:**

- **ARM:** Família de arquitetura de processadores. O software precisa ser compatível com a arquitetura escolhida; não basta comparar a quantidade de processadores.

**Graviton** (ARM, sufixo `g`): melhor preço/desempenho e menor consumo de energia → pilar **Sustentabilidade**.

**Antes de ler este trecho:**

- **hipervisor:** Camada que permite executar máquinas virtuais sobre equipamentos físicos. No EC2, ela não é administrada pelo cliente como o sistema dentro de sua máquina.

**Nitro System:** hipervisor leve + hardware dedicado da AWS; base das instâncias modernas (e requisito para EBS Multi-Attach).

### Configurações e opções importantes

**Tenancy**

**Antes de ler este trecho:**

- **compliance:** Atendimento a requisitos definidos. Usar um serviço com certificações não torna automaticamente a aplicação do cliente conforme.
- **tenancy:** Forma de compartilhamento ou dedicação de infraestrutura física. Uma máquina virtual dedicada e um host físico dedicado têm controles e usos de licença distintos.

**O que faz:** Shared (padrão), **Dedicated Instance** ou **Dedicated Host**

**Quando usar:** Compliance ou licenças por socket/núcleo (Host)

**Placement groups**

**Antes de ler este trecho:**

- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.
- **alta disponibilidade:** Planejamento para manter o sistema acessível diante de determinadas falhas. Não é promessa de ausência de qualquer interrupção.
- **Kafka:** Kafka é uma plataforma de fluxo de eventos; MSK é a oferta gerenciada compatível da AWS. A aplicação ainda precisa produzir e consumir os registros.
- **cluster:** Conjunto de recursos que trabalham de forma coordenada. O termo aparece em computação, banco e outras áreas, com papéis diferentes.

**O que faz:** **Cluster** (mesmo rack, baixa latência), **Spread** (hardware distinto, máx. 7 por AZ), **Partition** (até 7 partições por AZ, isoladas — Hadoop, Cassandra, Kafka)

**Quando usar:** HPC (cluster), alta disponibilidade de poucas instâncias críticas (spread)

**Monitoramento detalhado**

**O que faz:** Métricas a cada **1 min** em vez de 5 min (pago)

**Quando usar:** Auto Scaling mais reativo

**Hibernação**

**Antes de ler este trecho:**

- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.

**O que faz:** Salva a RAM no volume EBS raiz (criptografado) e para a instância

**Quando usar:** Aplicações com inicialização demorada

**Termination protection**

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.

**O que faz:** Impede encerrar pelo console/API por engano

**Quando usar:** Instâncias críticas

**Shutdown behavior**

**O que faz:** Ao desligar pelo SO: *stop* ou *terminate*

**EBS-optimized**

**O que faz:** Banda dedicada para EBS (padrão nas instâncias atuais)

**Launch template**

**Antes de ler este trecho:**

- **launch template:** Modelo versionado de parâmetros para iniciar máquinas. Facilita repetir configurações; não contém por si só todas as regras da aplicação.

**O que faz:** Modelo versionado de configuração (AMI, tipo, SG, user data…)

**Quando usar:** Usado por Auto Scaling, Spot Fleet, EC2 Fleet

**Session Manager**

**Antes de ler este trecho:**

- **porta:** Número que ajuda a identificar o serviço de destino de uma comunicação. Liberar uma porta autoriza tráfego segundo a regra, mas não configura a aplicação para responder.

**O que faz:** Acesso ao shell sem abrir porta 22 nem bastion

**Quando usar:** Boas práticas de segurança

**EC2 Instance Connect**

**Antes de ler este trecho:**

- **Connect:** Amazon Connect oferece uma plataforma de contact center em nuvem com canais e recursos compatíveis.

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

**Antes de ler este trecho:**

- **segundo:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.

📌 Cobrança **por segundo** com **mínimo de 60 s** (maioria das AMIs Linux/Windows).

📌 Spot: até **90%** de desconto, aviso de **2 minutos**.

**Antes de ler este trecho:**

- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.

📌 Métricas padrão a cada **5 min**; detalhado **1 min**. **Memória e disco** exigem o **CloudWatch agent**.

**Antes de ler este trecho:**

- **quota:** Limite de uso de um serviço ou recurso. Algumas quotas podem ser aumentadas mediante solicitação; limite não significa capacidade já reservada.

🧊 vCPUs por região (quota em vCPUs, ajustável via Service Quotas), ENIs por tipo, banda por tamanho.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Criar a máquina não instala nem publica automaticamente o seu sistema. Você precisa configurá-lo, protegê-lo e atualizá-lo. Parar a máquina também não elimina o custo de todos os recursos associados, como os discos mantidos.

### ⚠️ Pegadinhas e não confundir

**Antes de ler este trecho:**

- **BYOL:** Trazer licença própria elegível. É necessário verificar o direito de uso e as condições do software; a AWS não cria automaticamente essa licença.

**Dedicated Host × Dedicated Instance:** só o **Host** dá visibilidade de sockets/núcleos (BYOL por núcleo).

**Instance store** perde os dados ao **parar/encerrar** (mas não no reboot).

**Parar** a instância libera o IP público dinâmico — para IP fixo use **Elastic IP**.

**Antes de ler este trecho:**

- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **patch:** Atualização corretiva de software. A responsabilidade de aplicá-la depende da camada e do serviço usado.

"Quem aplica patch no SO da EC2?" → **cliente** (no RDS é a AWS).

**Antes de ler este trecho:**

- **Elastic Beanstalk:** O Elastic Beanstalk ajuda a implantar aplicações em plataformas compatíveis, provisionando e coordenando recursos AWS para esse ambiente.
- **Lightsail:** O Lightsail reúne recursos como servidores virtuais, armazenamento e rede em ofertas simplificadas.
- **PaaS:** Plataforma como serviço: parte da infraestrutura e do ambiente de execução é administrada para você entregar a aplicação. O código e suas regras continuam sendo do cliente.

EC2 × Lightsail × Elastic Beanstalk: controle total × preço fixo simples × PaaS.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **On-Demand:** Modalidade de uso sem o compromisso de longo prazo descrito por reservas e planos. Cobrança e unidades dependem do recurso contratado.
- **Reserved Instances:** Benefício e condições de reserva para configurações compatíveis. Não confunda desconto com qualquer garantia universal de capacidade.
- **Savings Plans:** Compromisso de gasto por período em troca de condições de preço para uso elegível. Se a necessidade diminuir, o compromisso não desaparece automaticamente.

Modelos de compra: On-Demand, Savings Plans, Reserved Instances, Spot, Dedicated Hosts/Instances, Capacity Reservations — ver [4.2](../../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md).

**Antes de ler este trecho:**

- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.
- **RHEL:** Red Hat Enterprise Linux: distribuição de sistema operacional Linux. Imagem, suporte e licença devem ser avaliados conforme a oferta.

Também cobrados: volumes EBS (provisionados), snapshots, **todo IPv4 público** (por hora), transferência de saída, Elastic IP, monitoramento detalhado, licenças incluídas (Windows, SQL Server, RHEL).

Instância parada não cobra computação, mas o EBS continua cobrado.

### Segurança e responsabilidade compartilhada

**Antes de ler este trecho:**

- **datacenter:** Instalação física com equipamentos de computação, rede, energia e refrigeração. A nuvem continua dependendo desses equipamentos, mas o cliente não precisa manter o prédio.

**AWS:** hardware, datacenter, rede física, hipervisor (Nitro).

**Antes de ler este trecho:**

- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.

**Cliente:** **patch do SO convidado**, aplicações, security groups, firewall do SO, dados, criptografia de EBS, IAM roles, key pairs.

**Antes de ler este trecho:**

- **Inspector:** Inspector avalia recursos compatíveis para encontrar vulnerabilidades e determinados riscos de exposição.

Boas práticas: IAM role (instance profile) em vez de access keys na instância; IMDSv2; Session Manager; Inspector para vulnerabilidades.

## 5. Caso resolvido: ligando as peças

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.

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

**Antes de ler este trecho:**

- **Systems Manager:** Systems Manager reúne ferramentas de operação para recursos e nós gerenciados compatíveis, incluindo acesso, automação, inventário e gerenciamento de patches.

**Pergunta:** "Instâncias precisam de latência mínima entre si para HPC."

**Resposta curta:** Placement group *cluster*.

**Antes de ler este trecho:**

- **placement group:** Forma de organizar posicionamento de instâncias para requisitos específicos de comunicação ou isolamento. Os modos atendem objetivos diferentes.

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
