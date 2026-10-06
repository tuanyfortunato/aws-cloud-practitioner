# 3.9 Outros serviços de armazenamento

## 🧠 Antes de começar

**Qual é a dificuldade?** Sua aplicação pode precisar de um disco próprio, de pastas compartilhadas ou de ligação com arquivos mantidos na empresa. Essas necessidades não são iguais.

**A ideia em palavras simples:** Este tópico compara armazenamento em blocos, arquivos compartilhados e integração com ambientes locais, além de cópias de segurança e recuperação.

**Exemplo do dia a dia:** Uma máquina usa EBS como disco. Várias máquinas podem precisar de EFS para compartilhar pastas. Uma aplicação Windows pode exigir uma modalidade FSx compatível.

**O que não concluir?** Escolher armazenamento só pelo nome ou preço pode causar incompatibilidade. Primeiro descubra como a aplicação precisa ler e gravar os dados.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Bloco** | armazenamento tipo disco, ligado a uma máquina. |
| **NFS / SMB** | protocolos de compartilhamento de arquivos (Linux / Windows). |
| **Snapshot** | cópia de um volume num ponto no tempo. |

---

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)**

> 🔎 **Fichas detalhadas:** [Amazon EBS (Elastic Block Store) e Instance Store](../../servicos/armazenamento/ebs.md) · [Amazon EFS (Elastic File System)](../../servicos/armazenamento/efs.md) · [Amazon FSx](../../servicos/armazenamento/fsx.md) · [AWS Storage Gateway](../../servicos/armazenamento/storage-gateway.md) · [AWS Backup](../../servicos/armazenamento/aws-backup.md) · [AWS Elastic Disaster Recovery (AWS DRS)](../../servicos/armazenamento/elastic-disaster-recovery.md) · [Família AWS Snow (Snowball Edge, Snowcone, Snowmobile)](../../servicos/migracao/snow-family.md) · [AWS DataSync e AWS Transfer Family](../../servicos/migracao/datasync-e-transfer-family.md)

> ⚠️ **Atualização do exam guide (verificado em 04/10/2026):** A **família Snow** e o **DataSync** não aparecem na lista oficial atual (o Snowball Edge está fechado a novos clientes); **FSx for Lustre** e **Transfer Family** estão **fora do escopo**. [Ver escopo oficial](../00-guia-do-exame/escopo-oficial.md).

⬅️ [3.8 Amazon S3 — armazenamento de objetos](08-s3.md) · 🏠 [Índice do domínio](README.md) · [3.10 Rede e entrega de conteúdo](10-rede-e-entrega-de-conteudo.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

Armazenamento em blocos apresenta um disco para o sistema. Armazenamento de arquivos apresenta pastas e arquivos por uma interface de rede. Armazenamento de objetos apresenta conteúdo por operações de serviço. A forma como o programa usa os dados orienta a escolha.

Depois da compatibilidade, avalie compartilhamento, desempenho, disponibilidade e conservação. Um disco para uma máquina não é automaticamente uma pasta para várias. Um backup protege recuperação, mas não transforma sozinho um armazenamento em ambiente de atendimento ativo.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

o **EBS** é o **HD do computador**; o **EFS** é a **pasta de rede** que todos abrem ao mesmo tempo; o **Storage Gateway** é a **ponte** entre o escritório e a nuvem; a **família Snow** é um **HD blindado enviado pelo correio**.

</details>

## 2. Conceitos e opções explicados

**Amazon EBS (Elastic Block Store):** armazenamento em **bloco** (disco) para EC2.

  - Persistente, preso a **uma AZ**, normalmente ligado a uma instância por vez.

  - Tipos: SSD de uso geral (**gp3**/gp2), SSD de IOPS provisionado (**io2**/io1, para bancos críticos), HDD otimizado para throughput (**st1**, big data e logs) e HDD frio (**sc1**, acesso raro).

  - **Snapshots** incrementais, guardados no S3, copiáveis entre regiões; usados para backup e para criar volumes em outra AZ.

  - Criptografia com KMS.

**Instance store:** disco físico do host. Muito rápido, mas **efêmero**: perde os dados ao parar ou encerrar a instância.

**Amazon EFS (Elastic File System):** sistema de arquivos **compartilhado** (NFS) para **Linux**, acessado por muitas instâncias ao mesmo tempo, em várias AZs. Cresce e encolhe sozinho; paga pelo que usa. Classes Standard, Infrequent Access e Archive.

**Amazon FSx:** sistemas de arquivos gerenciados de terceiros:

  - **FSx for Windows File Server:** SMB, integrado ao Active Directory.

  - **FSx for Lustre:** alto desempenho para HPC e machine learning, integrado ao S3.

  - **FSx for NetApp ONTAP** e **FSx for OpenZFS:** para migrar storages NAS existentes.

**AWS Storage Gateway:** armazenamento **híbrido**; liga o datacenter on-premises ao armazenamento na AWS.

  - **S3 File Gateway:** arquivos via NFS/SMB gravados como objetos no S3.

  - **FSx File Gateway:** acesso local de baixa latência ao FSx for Windows.

  - **Volume Gateway:** volumes iSCSI com cópia na AWS.

  - **Tape Gateway:** fitas virtuais; substitui backup em fita física, arquivando no S3 Glacier.

**AWS Backup:** gerencia **backups de forma centralizada** com políticas (EC2, EBS, RDS, Aurora, DynamoDB, EFS, FSx, S3 etc.), inclusive entre contas e regiões.

**AWS Elastic Disaster Recovery:** replica servidores (on-premises ou na nuvem) continuamente para a AWS e permite recuperar em minutos em caso de desastre.

**Família AWS Snow:** dispositivos físicos para **mover grandes volumes de dados** quando a rede é lenta, cara ou inexistente, e para **computação na borda** em locais desconectados (navios, campo, áreas remotas).

  - **Snowball Edge:** versões otimizadas para armazenamento (dezenas de TB) ou para computação.

  - Versões menores (Snowcone) e o caminhão Snowmobile foram descontinuados, mas podem aparecer em questões antigas.

  - Regra prática: se transferir pela rede levaria semanas, use Snow.

**Transferência online:** AWS DataSync (copia dados de NFS/SMB on-premises para S3, EFS ou FSx de forma automatizada) e AWS Transfer Family (SFTP/FTPS/FTP direto para S3 ou EFS).

| Tipo | Serviço | Acesso |
| --- | --- | --- |
| Objeto | S3 | Via API/HTTP, de qualquer lugar |
| Bloco | EBS, instance store | Um disco ligado a uma instância EC2 |
| Arquivo (Linux, NFS) | EFS | Muitas instâncias ao mesmo tempo |
| Arquivo (Windows, SMB) | FSx for Windows | Muitas instâncias ao mesmo tempo |
| Híbrido | Storage Gateway | Datacenter local usando armazenamento na AWS |

**Cai na prova:** "várias instâncias Linux precisam ler os mesmos arquivos" = EFS; "disco para banco de dados no EC2" = EBS io2; "substituir backup em fita" = Tape Gateway; "migrar 500 TB de um datacenter com internet lenta" = Snowball Edge.

## 3. Como analisar uma situação

**Primeiro, identifique o funcionamento:** Bloco funciona como disco; arquivo usa protocolos de sistema de arquivos; objeto é acessado por API. Backup guarda pontos de recuperação; replicação para DR mantém dados preparados para recuperação.

**Depois, compare as escolhas:** EBS para disco de EC2; EFS para arquivos NFS compartilhados; FSx para necessidades de sistema de arquivos específico; Storage Gateway para integrar ambiente próprio ao armazenamento AWS.

**Por fim, verifique o limite:** EBS pertence a uma AZ e não é um compartilhamento NFS. Multi-Attach é limitado a configurações suportadas. Backup e replicação não dispensam teste de restauração.

## 4. Caso resolvido

Duas EC2 Linux em AZs diferentes precisam dos mesmos arquivos. Um único EBS atende diretamente?

**Raciocínio e resposta:** Não. EFS é a opção típica de arquivos compartilhados; um EBS precisa respeitar sua AZ e condições de anexação.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Diferenciar **objeto (S3)**, **bloco (EBS)** e **arquivo (EFS/FSx)**.
- [ ] Diferenciar **EFS** (Linux, NFS) de **FSx for Windows** (SMB, Active Directory).
- [ ] Saber os tipos de **Storage Gateway** (Tape Gateway substitui fitas).
- [ ] Saber quando usar **Snow** (rede lenta, volumes enormes) e **AWS Backup** (backup central).

**Dica de revisão para a prova:** "Várias instâncias **Linux** lendo os mesmos arquivos" → **EFS**. "**Windows** com AD" → **FSx for Windows**. "Substituir fitas" → **Tape Gateway**. "500 TB com internet lenta" → **Snowball Edge**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).
**Pergunta:** "Qual armazenamento em bloco persistente para EC2?"

**Resposta curta:** EBS.

**Pergunta:** "Um volume EBS pode ser usado em outra AZ?"

**Resposta curta:** Não diretamente; cria-se um snapshot e um novo volume na outra AZ.

**Pergunta:** "Onde ficam os snapshots do EBS?"

**Resposta curta:** No S3 (gerenciado pela AWS), de forma incremental.

**Pergunta:** "Sistema de arquivos compartilhado para várias instâncias Linux."

**Resposta curta:** EFS.

**Pergunta:** "Compartilhamento de arquivos Windows integrado ao Active Directory."

**Resposta curta:** FSx for Windows File Server.

**Pergunta:** "Sistema de arquivos de alto desempenho para HPC."

**Resposta curta:** FSx for Lustre.

**Pergunta:** "Aplicações locais precisam usar armazenamento da AWS."

**Resposta curta:** Storage Gateway.

**Pergunta:** "Substituir fitas físicas de backup."

**Resposta curta:** Tape Gateway.

**Pergunta:** "Centralizar backups de vários serviços com políticas."

**Resposta curta:** AWS Backup.

**Pergunta:** "Mover dezenas de terabytes sem depender da internet."

**Resposta curta:** Snowball Edge.

**Pergunta:** "Processar dados num navio sem conexão."

**Resposta curta:** Família Snow (computação na borda).

**Pergunta:** "Recuperar servidores em minutos após desastre."

**Resposta curta:** AWS Elastic Disaster Recovery.

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- **EBS Multi-Attach (📌):** só **io1/io2**, até **16 instâncias Nitro na mesma AZ**. ⚠️ "Compartilhar um volume entre muitas instâncias em várias AZs" → **EFS**, não EBS.
- EBS fica preso a uma AZ; para mudar de AZ/região use **snapshot** (armazenado regionalmente no S3 e copiável entre regiões).
- 🔄 **Família Snow:**
  - **Snowmobile** (100 PB): aposentado em 2024.
  - **Snowcone:** sem novos pedidos desde 12/11/2024; suporte encerrado em 12/11/2025.
  - **Snowball Edge:** desde **07/11/2025**, só para **clientes existentes**. Novos clientes: **DataSync** (online), **AWS Data Transfer Terminal** (transferência física em local seguro) ou parceiros; para borda, **Outposts**. Restam o Storage Optimized de 210 TB e o Compute Optimized de 104 vCPUs.
  - ✔️ Verificado em 04/10/2026: a família Snow **saiu** da lista oficial de serviços. Em questões antigas, "migrar petabytes com banda limitada" → **Snowball Edge**; "exabytes / 100 PB" → Snowmobile (questões antigas).
- 🧊 Não decorar: IOPS por tipo de EBS, throughput st1/sc1, tamanhos antigos de Snowball (80 TB), preços por GB.
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.8 Amazon S3 — armazenamento de objetos](08-s3.md) · 🏠 [Índice do domínio](README.md) · [3.10 Rede e entrega de conteúdo](10-rede-e-entrega-de-conteudo.md) ➡️
