# AWS Storage Gateway

> **Categoria:** Armazenamento híbrido · **Domínio:** 3 · **Escopo:** gateway on-premises ligado a uma região · **Tópico do guia:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)
>
> **Em uma frase:** liga aplicações on-premises ao armazenamento da AWS usando protocolos padrão (NFS, SMB, iSCSI), com cache local.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Para que serve

- Arquitetura **híbrida**: aplicações locais usando armazenamento em nuvem quase ilimitado.
- Substituir backup em **fita física**; *tiering* de arquivos para a nuvem; DR.

## Tipos de gateway

| Tipo | Protocolo | Onde os dados ficam | Uso |
|---|---|---|---|
| **S3 File Gateway** | NFS / SMB | Como **objetos no S3** (um arquivo = um objeto) | Arquivos locais com cópia na nuvem, data lake, backups de bancos |
| **FSx File Gateway** | SMB | **FSx for Windows** | Acesso local de baixa latência a compartilhamentos Windows na AWS |
| **Volume Gateway** | iSCSI | Volumes na AWS com snapshots EBS | *Cached volumes* (dados na AWS, cache local) ou *stored volumes* (dados locais, backup assíncrono na AWS) |
| **Tape Gateway** | iSCSI VTL | Fitas virtuais no S3, arquivadas no **S3 Glacier / Deep Archive** | **Substituir fitas físicas** sem mudar o software de backup |

## Implantação

- Como **VM** (VMware, Hyper-V, KVM), em instância EC2 ou appliance de hardware.
- Cache local para dados acessados recentemente; transferência otimizada e criptografada (TLS) para a AWS.

## Cobrança

- Armazenamento usado na AWS + requisições + transferência de saída; Tape Gateway por fita virtual armazenada/recuperada.

## ⚠️ Pegadinhas e não confundir

- **Storage Gateway × DataSync:** acesso **contínuo** híbrido × **transferência/migração** de dados.
- "Substituir backup em fita" → **Tape Gateway**.

## ❓ Perguntas típicas

- "Aplicações locais precisam usar armazenamento da AWS." → Storage Gateway.
- "Substituir fitas físicas de backup." → Tape Gateway.
- "Arquivos via NFS/SMB gravados como objetos no S3." → S3 File Gateway.

## 🔗 Documentação oficial

- [Storage Gateway](https://docs.aws.amazon.com/storagegateway/)
