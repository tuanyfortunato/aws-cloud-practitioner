# Amazon FSx

> **Categoria:** Armazenamento de arquivos gerenciado · **Domínio:** 3 · **Escopo:** Regional (Single-AZ ou Multi-AZ) · **Tópico do guia:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)
>
> **Em uma frase:** sistemas de arquivos populares de terceiros (Windows, Lustre, NetApp ONTAP, OpenZFS) totalmente gerenciados.

## Os quatro sabores

| Sabor | Protocolos | Destaques | Uso típico |
|---|---|---|---|
| **FSx for Windows File Server** | **SMB** | Integra com **Active Directory**, ACLs NTFS, DFS, shadow copies, deduplicação; Single-AZ ou Multi-AZ | Compartilhamentos Windows, SharePoint, SQL Server, home folders |
| **FSx for Lustre** | Lustre (POSIX) | **Alto desempenho** (centenas de GB/s, milhões de IOPS); **integração com S3** (lê/grava dados do bucket); *scratch* (temporário) ou *persistent* | HPC, ML, renderização, simulações |
| **FSx for NetApp ONTAP** | **NFS, SMB e iSCSI** | Recursos ONTAP (snapshots, SnapMirror, FlexClone, deduplicação, tiering) | Migrar NAS NetApp existente; multiprotocolo |
| **FSx for OpenZFS** | NFS | Snapshots e clones instantâneos ZFS, baixa latência | Migrar storage ZFS/Linux |

## Cobrança

- Por capacidade de armazenamento provisionada, throughput (e SSD IOPS em alguns sabores) e backups.

## Segurança e responsabilidade compartilhada

- **AWS:** hardware, software do sistema de arquivos, patches, failover (Multi-AZ).
- **Cliente:** acesso (AD, SGs, permissões), criptografia, backup e dados.

## ⚠️ Pegadinhas e não confundir

- "Windows + SMB + Active Directory" → **FSx for Windows** (não EFS).
- "HPC/ML com dados no S3" → **FSx for Lustre**.
- "Já usa NetApp" → **FSx for ONTAP**.
- Acesso local de baixa latência ao FSx for Windows a partir do datacenter → **FSx File Gateway** ([Storage Gateway](storage-gateway.md)).

## ❓ Perguntas típicas

- "Compartilhamento de arquivos Windows integrado ao AD." → FSx for Windows File Server.
- "Sistema de arquivos de alto desempenho para HPC." → FSx for Lustre.

## 🔗 Documentação oficial

- [Amazon FSx](https://aws.amazon.com/fsx/)
