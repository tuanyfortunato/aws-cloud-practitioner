# Amazon EFS (Elastic File System)

> **Categoria:** Armazenamento de arquivos · **Domínio:** 3 · **Escopo:** Regional (multi-AZ) ou One Zone · **Tópico do guia:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)
>
> **Em uma frase:** sistema de arquivos NFS gerenciado e elástico, compartilhado por milhares de instâncias Linux em várias AZs.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é como uma **pasta de rede compartilhada**: vários computadores Linux abrem e gravam os mesmos arquivos ao mesmo tempo, e ela cresce sozinha.

- ✅ **Escolha quando:** várias instâncias **Linux**, em **várias AZs**, precisam do **mesmo sistema de arquivos**.
- 🚫 **Não é a resposta quando:** o compartilhamento é **Windows (SMB)** → [FSx for Windows](fsx.md); é o disco de **uma única instância** → [EBS](ebs.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "sistema de arquivos compartilhado", "NFS", "várias instâncias Linux", "cresce automaticamente".
<!-- didatico:fim -->

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

## 🔗 Documentação oficial

- [Guia do EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)
