# Amazon EC2 (Elastic Compute Cloud)

> **Categoria:** Computação · **Domínio:** 3 (e 4: modelos de compra) · **Escopo:** Regional (cada instância vive numa AZ) · **Tópico do guia:** [3.3 Amazon EC2](../../docs/03-tecnologia-e-servicos/03-ec2.md)
>
> **Em uma frase:** servidores virtuais sob demanda, com controle total do sistema operacional (IaaS).
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é como **alugar um computador** num datacenter da AWS: você escolhe o tamanho, instala o que quiser e paga pelo tempo em que ele fica ligado.

- ✅ **Escolha quando:** precisa de **controle total do sistema operacional**, de software legado ou de licenças específicas, ou vai mover servidores sem mudanças (lift-and-shift).
- 🚫 **Não é a resposta quando:** não quer gerenciar servidores → [Lambda](lambda.md) ou [Fargate](fargate.md); quer só enviar o código → [Elastic Beanstalk](elastic-beanstalk.md); quer preço fixo e simples → [Lightsail](lightsail.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "servidor virtual", "instância", "controle do sistema operacional", "tipo de instância", "lift-and-shift".
<!-- didatico:fim -->

## Para que serve

- Hospedar aplicações web, back-ends, bancos instalados pelo cliente, servidores de jogos, HPC, treinamento de ML.
- Migração **lift-and-shift (Rehost)** de servidores on-premises.
- Qualquer carga que exija controle do SO, software legado ou licenças específicas.

## Conceitos e componentes

| Componente | O que é |
|---|---|
| **Instância** | Servidor virtual. Roda numa **AZ** específica. |
| **AMI** (Amazon Machine Image) | Modelo com SO + software. Fontes: AWS, Marketplace, comunidade ou sua (personalizada). **AMIs são regionais** — copie para usar em outra região. **EC2 Image Builder** automatiza a criação e atualização. |
| **Tipo de instância** | Combinação de CPU, memória, rede e armazenamento. Nome `m7g.large` = família **m**, geração **7**, atributo **g** (Graviton), tamanho **large**. |
| **Key pair** | Chave pública/privada para SSH (Linux) ou para obter a senha de administrador (Windows). A AWS guarda só a pública. |
| **Security group** | Firewall stateful na interface de rede. Padrão: nega toda entrada, libera toda saída. |
| **EBS / instance store** | Disco persistente em rede (EBS) ou disco local efêmero (instance store). Ver [EBS](../armazenamento/ebs.md). |
| **ENI** | Interface de rede virtual (IP privado, IP público, SGs). |
| **Elastic IP** | IPv4 público estático que pode ser remapeado entre instâncias. |
| **User data** | Script executado (como root) na **primeira inicialização**. |
| **Instance metadata (IMDS)** | Endpoint `169.254.169.254` com dados da instância e credenciais temporárias da role. **IMDSv2** (com token) é o recomendado. |
| **Instance profile** | "Contêiner" da IAM role anexada à instância — forma correta de dar permissões à aplicação. |

### Famílias de instância

| Família | Letras | Uso |
|---|---|---|
| Uso geral | **T** (burstable, créditos de CPU), **M**, Mac | Web, repositórios de código, ambientes de dev |
| Otimizada para computação | **C** | Batch, servidores de jogos, HPC, codificação de mídia, inferência |
| Otimizada para memória | **R**, **X**, z, u (High Memory) | Bancos em memória, SAP HANA, análise em tempo real |
| Computação acelerada | **P**, **G**, **Inf** (Inferentia), **Trn** (Trainium), F (FPGA) | Treino/inferência de ML, gráficos, cálculos científicos |
| Otimizada para armazenamento | **I**, **D**, H | Alto IOPS em disco local, data warehouses, NoSQL, HDFS |
| HPC | **Hpc** | Simulações fortemente acopladas |

- **Graviton** (ARM, sufixo `g`): melhor preço/desempenho e menor consumo de energia → pilar **Sustentabilidade**.
- **Nitro System:** hipervisor leve + hardware dedicado da AWS; base das instâncias modernas (e requisito para EBS Multi-Attach).

## Configurações e opções importantes

| Opção | O que faz | Quando usar |
|---|---|---|
| **Tenancy** | Shared (padrão), **Dedicated Instance** ou **Dedicated Host** | Compliance ou licenças por socket/núcleo (Host) |
| **Placement groups** | **Cluster** (mesmo rack, baixa latência), **Spread** (hardware distinto, máx. 7 por AZ), **Partition** (até 7 partições por AZ, isoladas — Hadoop, Cassandra, Kafka) | HPC (cluster), alta disponibilidade de poucas instâncias críticas (spread) |
| **Monitoramento detalhado** | Métricas a cada **1 min** em vez de 5 min (pago) | Auto Scaling mais reativo |
| **Hibernação** | Salva a RAM no volume EBS raiz (criptografado) e para a instância | Aplicações com inicialização demorada |
| **Termination protection** | Impede encerrar pelo console/API por engano | Instâncias críticas |
| **Shutdown behavior** | Ao desligar pelo SO: *stop* ou *terminate* | — |
| **EBS-optimized** | Banda dedicada para EBS (padrão nas instâncias atuais) | — |
| **Launch template** | Modelo versionado de configuração (AMI, tipo, SG, user data…) | Usado por Auto Scaling, Spot Fleet, EC2 Fleet |
| **Session Manager** | Acesso ao shell sem abrir porta 22 nem bastion | Boas práticas de segurança |
| **EC2 Instance Connect** | SSH com chave temporária enviada pela API | Acesso pontual |

### Ciclo de vida

| Estado | Cobrança de computação | EBS | Instance store | IP público |
|---|---|---|---|---|
| `running` | Sim | Mantido | Mantido | Mantido |
| `stopped` | **Não** (EBS continua cobrado) | Mantido | **Perdido** | Liberado (Elastic IP fica) |
| `hibernated` | Não | Mantido (com a RAM) | Perdido | Liberado |
| `terminated` | Não | Raiz apagado por padrão (*DeleteOnTermination*) | Perdido | Liberado |
| `reboot` | Sim | Mantido | **Mantido** | Mantido |

## Limites e números

- 📌 Cobrança **por segundo** com **mínimo de 60 s** (maioria das AMIs Linux/Windows).
- 📌 Spot: até **90%** de desconto, aviso de **2 minutos**.
- 📌 Métricas padrão a cada **5 min**; detalhado **1 min**. **Memória e disco** exigem o **CloudWatch agent**.
- 🧊 vCPUs por região (quota em vCPUs, ajustável via Service Quotas), ENIs por tipo, banda por tamanho.

## Cobrança

- Modelos de compra: On-Demand, Savings Plans, Reserved Instances, Spot, Dedicated Hosts/Instances, Capacity Reservations — ver [4.2](../../docs/04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md).
- Também cobrados: volumes EBS (provisionados), snapshots, **todo IPv4 público** (por hora), transferência de saída, Elastic IP, monitoramento detalhado, licenças incluídas (Windows, SQL Server, RHEL).
- Instância parada não cobra computação, mas o EBS continua cobrado.

## Segurança e responsabilidade compartilhada

- **AWS:** hardware, datacenter, rede física, hipervisor (Nitro).
- **Cliente:** **patch do SO convidado**, aplicações, security groups, firewall do SO, dados, criptografia de EBS, IAM roles, key pairs.
- Boas práticas: IAM role (instance profile) em vez de access keys na instância; IMDSv2; Session Manager; Inspector para vulnerabilidades.

## ⚠️ Pegadinhas e não confundir

- **Dedicated Host × Dedicated Instance:** só o **Host** dá visibilidade de sockets/núcleos (BYOL por núcleo).
- **Instance store** perde os dados ao **parar/encerrar** (mas não no reboot).
- **Parar** a instância libera o IP público dinâmico — para IP fixo use **Elastic IP**.
- "Quem aplica patch no SO da EC2?" → **cliente** (no RDS é a AWS).
- EC2 × Lightsail × Elastic Beanstalk: controle total × preço fixo simples × PaaS.

## ❓ Perguntas típicas

- "Qual família para aplicação com uso intenso de CPU?" → Otimizada para computação (C).
- "Qual família para banco em memória?" → Otimizada para memória (R, X).
- "Qual família para treinar modelos com GPU?" → Computação acelerada (P, G, Trn).
- "Como instalar pacotes automaticamente no primeiro boot?" → User data.
- "Como manter IP público fixo ao trocar de instância?" → Elastic IP.
- "Como dar permissão para a aplicação no EC2 ler o S3?" → IAM role (instance profile).
- "Como acessar a instância sem abrir a porta 22?" → Systems Manager Session Manager.
- "Instâncias precisam de latência mínima entre si para HPC." → Placement group *cluster*.
- "Licença Oracle cobrada por núcleo físico." → Dedicated Host.

## 🔗 Documentação oficial

- [Guia do usuário do EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)
- [Tipos de instância](https://aws.amazon.com/ec2/instance-types/)
- [Preços do EC2](https://aws.amazon.com/ec2/pricing/)
