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

## 1. A sequência de funcionamento

**Passo 1.** Identifique o sistema de arquivos que a aplicação espera e escolha a modalidade correspondente.

**Passo 2.** Prepare identidade, conexão e armazenamento. Os clientes compatíveis acessam os arquivos por sua interface prevista.

**Passo 3.** Planeje disponibilidade, cópias e capacidade. Cada modalidade tem seus próprios recursos e limites.

## 2. Recursos e opções, com significado

### Os quatro sabores

| Sabor | Protocolos | Destaques | Uso típico |
|---|---|---|---|
| **FSx for Windows File Server** | **SMB** | Integra com **Active Directory**, ACLs NTFS, DFS, shadow copies, deduplicação; Single-AZ ou Multi-AZ | Compartilhamentos Windows, SharePoint, SQL Server, home folders |
| **FSx for Lustre** ❌ *fora do escopo* | Lustre (POSIX) | **Alto desempenho** (centenas de GB/s, milhões de IOPS); **integração com S3** (lê/grava dados do bucket); *scratch* (temporário) ou *persistent* | HPC, ML, renderização, simulações |
| **FSx for NetApp ONTAP** | **NFS, SMB e iSCSI** | Recursos ONTAP (snapshots, SnapMirror, FlexClone, deduplicação, tiering) | Migrar NAS NetApp existente; multiprotocolo |
| **FSx for OpenZFS** | NFS | Snapshots e clones instantâneos ZFS, baixa latência | Migrar storage ZFS/Linux |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

FSx é uma família; uma modalidade não oferece automaticamente as funções de todas as outras. Confira compatibilidade, disponibilidade e escopo de cada opção.

### ⚠️ Pegadinhas e não confundir

"Windows + SMB + Active Directory" → **FSx for Windows** (não EFS).

"HPC/ML com dados no S3" → **FSx for Lustre**.

"Já usa NetApp" → **FSx for ONTAP**.

Acesso local de baixa latência ao FSx for Windows a partir do datacenter → **FSx File Gateway** ([Storage Gateway](storage-gateway.md)).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por capacidade de armazenamento provisionada, throughput (e SSD IOPS em alguns sabores) e backups.

### Segurança e responsabilidade compartilhada

**AWS:** hardware, software do sistema de arquivos, patches, failover (Multi-AZ).

**Cliente:** acesso (AD, SGs, permissões), criptografia, backup e dados.

## 5. Caso resolvido: ligando as peças

Uma empresa com aplicações Windows pode avaliar FSx for Windows File Server para compartilhar arquivos com as características esperadas por esse ambiente.

**Aplicando a sequência à situação:**

**Etapa 1:** Identifique o sistema de arquivos que a aplicação espera e escolha a modalidade correspondente.
**Etapa 2:** Prepare identidade, conexão e armazenamento. Os clientes compatíveis acessam os arquivos por sua interface prevista.
**Etapa 3:** Planeje disponibilidade, cópias e capacidade. Cada modalidade tem seus próprios recursos e limites.

**Resultado e responsabilidade:** O FSx oferece sistemas de arquivos gerenciados em modalidades diferentes. A escolha depende da compatibilidade e das funções de que sua aplicação precisa.

**Recursos envolvidos:** Famílias de sistemas de arquivos gerenciados e endpoints.

**Decisões que precisam ser tomadas:** Família, protocolo, capacidade e opções de disponibilidade.

**Outra situação comentada:** Aplicação Windows exige SMB e integração AD: avalie FSx for Windows File Server.

**Por que não concluir mais do que isso:** Cada família tem capacidades distintas; FSx for Lustre está explicitamente fora do escopo consultado

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Compartilhamento de arquivos Windows integrado ao AD."

**Resposta curta:** FSx for Windows File Server.

**Pergunta:** "Sistema de arquivos de alto desempenho para HPC."

**Resposta curta:** FSx for Lustre.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Amazon FSx](https://aws.amazon.com/fsx/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
