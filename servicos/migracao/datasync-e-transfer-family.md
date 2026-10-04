# AWS DataSync e AWS Transfer Family

> **Categoria:** Migração / transferência online · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.9 Outros armazenamentos](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md) · [3.17 Migração](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md)
>
> **Em uma frase:** DataSync **move dados online** de forma automatizada e rápida; Transfer Family oferece **SFTP/FTPS/FTP** gerenciado com armazenamento em S3/EFS.

## AWS DataSync

| Item | Detalhe |
|---|---|
| **Origens** | NFS, SMB, HDFS, armazenamento de objetos, outras nuvens (Azure Blob, Google Cloud Storage), e serviços AWS. |
| **Destinos** | **S3** (qualquer classe), **EFS**, **FSx** (todos os sabores). |
| **Agente** | VM on-premises (VMware, Hyper-V, KVM) ou EC2; transferências entre serviços AWS dispensam agente. |
| **Recursos** | Agendamento, filtros, **verificação de integridade**, limite de banda, criptografia em trânsito, preserva metadados/permissões; até 10× mais rápido que ferramentas open source. |
| **Uso** | Migração de arquivos, replicação para DR, mover dados frios para o S3, alimentar data lakes. |
| **Cobrança** | Por GB transferido. |

## AWS Transfer Family

| Item | Detalhe |
|---|---|
| **Protocolos** | **SFTP**, **FTPS**, **FTP** (só dentro da VPC) e **AS2** (B2B/EDI). |
| **Armazenamento** | Arquivos gravados direto no **S3** ou **EFS**. |
| **Identidade** | Usuários gerenciados pelo serviço, AD ou IdP customizado (Lambda/API Gateway). |
| **Extras** | Workflows pós-upload, *web apps* para usuários não técnicos, conectores SFTP para servidores externos. |
| **Uso** | Parceiros/clientes que já enviam arquivos via SFTP, sem mudar o processo deles. |

## ⚠️ Não confundir

- **DataSync** (transferência/migração online) × **Storage Gateway** (acesso híbrido contínuo) × **Snow** (offline, dispositivo físico) × **Transfer Family** (protocolos FTP para terceiros).

## ❓ Perguntas típicas

- "Transferir arquivos online de forma automatizada do NAS para o S3." → DataSync.
- "Parceiros enviam arquivos via SFTP e queremos guardar no S3." → Transfer Family.

## 🔗 Documentação oficial

- [DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html) · [Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html)
