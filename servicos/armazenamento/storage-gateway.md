<!-- autoral -->

# AWS Storage Gateway

> **Categoria:** Armazenamento híbrido · **Domínio:** 3 · **Abrangência:** Gateway no local do cliente ligado a uma Região · **Ficha:** núcleo
>
> **Em uma frase:** liga servidores e pessoas no datacenter local ao armazenamento da AWS por NFS, SMB, iSCSI ou fitas virtuais, com cache local.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

A unidade de Lisboa tem um servidor de arquivos local que enche todo ano e um software de backup que grava em fitas guardadas numa sala. As pessoas querem continuar usando a pasta de rede de sempre, sem lentidão.

O Storage Gateway instala no local do cliente uma máquina virtual (ou um aparelho físico) que conversa com o armazenamento da AWS. Os dados ficam na nuvem, e o gateway mantém um **cache local** com o que é acessado com frequência, para o acesso continuar rápido. Por isso o guia do exame o chama de sistema de arquivos com cache.

O limite: o gateway faz a ponte entre o local e a AWS; ele não é um serviço de arquivos dentro da AWS (isso é o [EFS](efs.md) ou o [FSx](fsx.md)) nem uma ferramenta de migração única de grandes volumes, papel do [DataSync](../migracao/datasync-e-transfer-family.md).

## Como funciona

1. Você instala o gateway como máquina virtual (VMware ESXi, Hyper-V, KVM ou Nutanix AHV), como aparelho físico ou como instância do EC2.
2. Ativa o gateway na Região escolhida e escolhe o tipo.
3. Servidores e pessoas usam o gateway por protocolos de sempre: pasta de rede, disco iSCSI ou biblioteca de fitas.
4. O gateway grava os dados na AWS e guarda localmente o que é mais usado.

## Opções principais

| Tipo | O que apresenta no local | Onde os dados ficam |
|---|---|---|
| S3 File Gateway | Pasta de rede (NFS ou SMB) | Objetos no S3, com classes e ciclo de vida |
| Volume Gateway | Volumes de disco (iSCSI): em cache (dados no S3, cópia local do mais usado) ou armazenados (tudo local, com snapshots na AWS) | Na AWS, com snapshots do EBS |
| Tape Gateway | Fitas virtuais para o software de backup | Arquivamento no S3 Glacier Flexible Retrieval ou Deep Archive |

O FSx File Gateway não está mais disponível para novos clientes.

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Tipos de gateway para novos clientes | 3 (S3 File, Volume e Tape) | 06/10/2026 |

## Como é cobrado

Você paga o armazenamento onde os dados ficam (objetos do S3, volumes e snapshots, fitas virtuais e seu arquivamento no Glacier), uma taxa por GB gravado na AWS pelo gateway, as recuperações de fitas arquivadas e a transferência de dados para fora da AWS.

## Não confundir com

| Serviço | Diferença para o Storage Gateway | Pista no enunciado |
|---|---|---|
| [AWS DataSync](../migracao/datasync-e-transfer-family.md) | Move e sincroniza dados entre o local e a AWS; não serve de pasta de uso diário | "Migrar", "copiar grandes volumes" |
| [Amazon EFS](efs.md) | Pasta compartilhada dentro da AWS para instâncias Linux | "Instâncias na AWS" |
| [AWS Backup](aws-backup.md) | Centraliza backups de serviços da AWS; não oferece interface de fita | "Painel único de backups" |
| [AWS Snow Family](../migracao/snow-family.md) | Aparelhos físicos para levar dados offline | "Sem rede suficiente", "enviar dados por transporte" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o S3 File Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/what-is-file-s3.html)
- [O que é o Volume Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/WhatIsStorageGateway.html)
- [O que é o Tape Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/WhatIsStorageGateway.html)
- [O que é o FSx File Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/what-is-file-fsxw.html)
- [Preços do AWS Storage Gateway](https://aws.amazon.com/storagegateway/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
