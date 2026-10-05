# Amazon EFS (Elastic File System)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Várias máquinas Linux precisam ler e gravar os mesmos arquivos, sem cada uma manter uma cópia separada.

**Como este serviço ajuda?** O EFS oferece um sistema de arquivos compartilhado. Máquinas autorizadas podem montar esse armazenamento e usá-lo como um conjunto de pastas acessíveis pela rede.

**Exemplo do dia a dia:** Vários servidores de uma aplicação acessam a mesma pasta de documentos pelo EFS. Um arquivo gravado ali pode ser acessado pelos outros servidores autorizados.

**O que ele não resolve sozinho?** Ele fornece arquivos compartilhados, não um banco de dados nem armazenamento local de cada máquina. Rede, permissões e compatibilidade precisam ser configuradas.

**Primeiras palavras para entender:**

- **Sistema de arquivos:** organização de arquivos e pastas.
- **Montar:** tornar esse armazenamento acessível ao sistema.
- **NFS:** protocolo usado para acessar arquivos pela rede.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Armazenamento de arquivos · **Domínio:** 3 · **Escopo:** Regional (multi-AZ) ou One Zone · **Tópico do guia:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)
>
> **Em uma frase:** sistema de arquivos NFS gerenciado e elástico, compartilhado por milhares de instâncias Linux em várias AZs.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Para que serve

- Conteúdo web compartilhado, diretórios home, CMS, pipelines de mídia, ML, contêineres e Lambda que precisam de arquivos persistentes.

## Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Protocolo** | **NFS v4.0/4.1** — clientes **Linux** (não suporta Windows). |
| **Mount targets** | Um por AZ, com security group; instâncias montam pelo DNS do EFS. |
| **Tipo de file system** | **Regional** (dados em várias AZs — padrão) ou **One Zone** (uma AZ, mais barato). |
| **Classes de armazenamento** | **Standard**, **Infrequent Access (IA)** e **Archive**. |
| **Lifecycle management** | Move arquivos sem acesso para IA/Archive após N dias e de volta ao Standard quando acessados. |
| **Throughput mode** | ✔️ **Elastic** (padrão e recomendado, escala automática, paga pelo uso), **Provisioned** (cargas previsíveis) ou **Bursting**. |
| **Performance mode** | General Purpose (padrão, menor latência) ou Max I/O (legado). |
| **Criptografia** | Em repouso (KMS, definida na criação) e em trânsito (TLS no mount helper). |
| **Acesso** | IAM, *access points* (diretório raiz e usuário POSIX por aplicação), security groups. |
| **Replicação e backup** | EFS Replication (outra região/AZ) e integração com AWS Backup. |

## Cobrança

- Por **GB efetivamente armazenado** por mês (cresce e encolhe sozinho) + throughput (Elastic/Provisioned) + acessos a IA/Archive.

## Segurança e responsabilidade compartilhada

- **AWS:** disponibilidade, durabilidade e escala do sistema de arquivos.
- **Cliente:** security groups dos mount targets, permissões POSIX/IAM, criptografia, backup.

## ⚠️ Pegadinhas e não confundir

- **EFS × EBS:** compartilhado entre muitas instâncias e AZs × disco de uma instância numa AZ.
- **EFS × FSx for Windows:** Linux/NFS × Windows/SMB com Active Directory.
- EFS cobra pelo usado; EBS cobra pelo provisionado.

## ❓ Perguntas típicas

- "Várias instâncias Linux em AZs diferentes precisam ler e gravar os mesmos arquivos." → EFS.
- "Reduzir custo de arquivos pouco acessados no EFS." → Lifecycle para IA/Archive.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Sistema de arquivos, mount targets, access points e classes |
| **O que você decide/configura?** | Rede NFS, permissões, modalidade regional/uma zona e lifecycle |
| **Em que ordem as coisas acontecem?** | Crie pontos de montagem e monte nos clientes autorizados |
| **O que pode fazer, e em que condição?** | Compartilha arquivos entre clientes Linux compatíveis |
| **O que não pode presumir?** | Precisa de conectividade e autorização de rede/arquivo; não é disco de boot EC2 |

**Caso comentado:** Vários servidores web Linux usam o mesmo conteúdo: EFS, com configuração dos mounts.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)
