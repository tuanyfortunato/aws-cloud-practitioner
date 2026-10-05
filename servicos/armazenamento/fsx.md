# Amazon FSx

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma aplicação precisa de arquivos compartilhados, mas depende de características de um sistema de arquivos específico, como o usado em ambientes Windows.

**Como este serviço ajuda?** O FSx oferece sistemas de arquivos gerenciados em modalidades diferentes. A escolha depende da compatibilidade e das funções de que sua aplicação precisa.

**Exemplo do dia a dia:** Uma empresa com aplicações Windows pode avaliar FSx for Windows File Server para compartilhar arquivos com as características esperadas por esse ambiente.

**O que ele não resolve sozinho?** FSx é uma família; uma modalidade não oferece automaticamente as funções de todas as outras. Confira compatibilidade, disponibilidade e escopo de cada opção.

**Primeiras palavras para entender:**

- **SMB:** protocolo comum para compartilhamento de arquivos Windows.
- **Sistema de arquivos:** forma de organizar e acessar arquivos.
- **Modalidade:** variante do serviço.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Armazenamento de arquivos gerenciado · **Domínio:** 3 · **Escopo:** Regional (Single-AZ ou Multi-AZ) · **Tópico do guia:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)
>
> **Em uma frase:** sistemas de arquivos populares de terceiros (Windows, Lustre, NetApp ONTAP, OpenZFS) totalmente gerenciados.
>
> **Escopo oficial:** 🔀 FSx ✅ · FSx for Lustre ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Os quatro sabores

| Sabor | Protocolos | Destaques | Uso típico |
|---|---|---|---|
| **FSx for Windows File Server** | **SMB** | Integra com **Active Directory**, ACLs NTFS, DFS, shadow copies, deduplicação; Single-AZ ou Multi-AZ | Compartilhamentos Windows, SharePoint, SQL Server, home folders |
| **FSx for Lustre** ❌ *fora do escopo* | Lustre (POSIX) | **Alto desempenho** (centenas de GB/s, milhões de IOPS); **integração com S3** (lê/grava dados do bucket); *scratch* (temporário) ou *persistent* | HPC, ML, renderização, simulações |
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

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Famílias de sistemas de arquivos gerenciados e endpoints |
| **O que você decide/configura?** | Família, protocolo, capacidade e opções de disponibilidade |
| **Em que ordem as coisas acontecem?** | Escolha pelo sistema/protocolo exigido e conecte os clientes |
| **O que pode fazer, e em que condição?** | Atende necessidades como arquivos Windows/SMB com a família apropriada |
| **O que não pode presumir?** | Cada família tem capacidades distintas; FSx for Lustre está explicitamente fora do escopo consultado |

**Caso comentado:** Aplicação Windows exige SMB e integração AD: avalie FSx for Windows File Server.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Amazon FSx](https://aws.amazon.com/fsx/)
