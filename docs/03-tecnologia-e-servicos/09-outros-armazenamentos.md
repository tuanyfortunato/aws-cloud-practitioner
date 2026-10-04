# 3.9 Outros serviços de armazenamento

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon EBS (Elastic Block Store) e Instance Store](../../servicos/armazenamento/ebs.md) · [Amazon EFS (Elastic File System)](../../servicos/armazenamento/efs.md) · [Amazon FSx](../../servicos/armazenamento/fsx.md) · [AWS Storage Gateway](../../servicos/armazenamento/storage-gateway.md) · [AWS Backup](../../servicos/armazenamento/aws-backup.md) · [AWS Elastic Disaster Recovery (AWS DRS)](../../servicos/armazenamento/elastic-disaster-recovery.md) · [Família AWS Snow (Snowball Edge, Snowcone, Snowmobile)](../../servicos/migracao/snow-family.md) · [AWS DataSync e AWS Transfer Family](../../servicos/migracao/datasync-e-transfer-family.md)

⬅️ [3.8 Amazon S3 — armazenamento de objetos](08-s3.md) · 🏠 [Índice do domínio](README.md) · [3.10 Rede e entrega de conteúdo](10-rede-e-entrega-de-conteudo.md) ➡️

---

## 📖 Conteúdo

- **Amazon EBS (Elastic Block Store):** armazenamento em **bloco** (disco) para EC2.
  - Persistente, preso a **uma AZ**, normalmente ligado a uma instância por vez.
  - Tipos: SSD de uso geral (**gp3**/gp2), SSD de IOPS provisionado (**io2**/io1, para bancos críticos), HDD otimizado para throughput (**st1**, big data e logs) e HDD frio (**sc1**, acesso raro).
  - **Snapshots** incrementais, guardados no S3, copiáveis entre regiões; usados para backup e para criar volumes em outra AZ.
  - Criptografia com KMS.
- **Instance store:** disco físico do host. Muito rápido, mas **efêmero**: perde os dados ao parar ou encerrar a instância.
- **Amazon EFS (Elastic File System):** sistema de arquivos **compartilhado** (NFS) para **Linux**, acessado por muitas instâncias ao mesmo tempo, em várias AZs. Cresce e encolhe sozinho; paga pelo que usa. Classes Standard, Infrequent Access e Archive.
- **Amazon FSx:** sistemas de arquivos gerenciados de terceiros:
  - **FSx for Windows File Server:** SMB, integrado ao Active Directory.
  - **FSx for Lustre:** alto desempenho para HPC e machine learning, integrado ao S3.
  - **FSx for NetApp ONTAP** e **FSx for OpenZFS:** para migrar storages NAS existentes.
- **AWS Storage Gateway:** armazenamento **híbrido**; liga o datacenter on-premises ao armazenamento na AWS.
  - **S3 File Gateway:** arquivos via NFS/SMB gravados como objetos no S3.
  - **FSx File Gateway:** acesso local de baixa latência ao FSx for Windows.
  - **Volume Gateway:** volumes iSCSI com cópia na AWS.
  - **Tape Gateway:** fitas virtuais; substitui backup em fita física, arquivando no S3 Glacier.
- **AWS Backup:** gerencia **backups de forma centralizada** com políticas (EC2, EBS, RDS, Aurora, DynamoDB, EFS, FSx, S3 etc.), inclusive entre contas e regiões.
- **AWS Elastic Disaster Recovery:** replica servidores (on-premises ou na nuvem) continuamente para a AWS e permite recuperar em minutos em caso de desastre.
- **Família AWS Snow:** dispositivos físicos para **mover grandes volumes de dados** quando a rede é lenta, cara ou inexistente, e para **computação na borda** em locais desconectados (navios, campo, áreas remotas).
  - **Snowball Edge:** versões otimizadas para armazenamento (dezenas de TB) ou para computação.
  - Versões menores (Snowcone) e o caminhão Snowmobile foram descontinuados, mas podem aparecer em questões antigas.
  - Regra prática: se transferir pela rede levaria semanas, use Snow.
- **Transferência online:** AWS DataSync (copia dados de NFS/SMB on-premises para S3, EFS ou FSx de forma automatizada) e AWS Transfer Family (SFTP/FTPS/FTP direto para S3 ou EFS).

| Tipo | Serviço | Acesso |
| --- | --- | --- |
| Objeto | S3 | Via API/HTTP, de qualquer lugar |
| Bloco | EBS, instance store | Um disco ligado a uma instância EC2 |
| Arquivo (Linux, NFS) | EFS | Muitas instâncias ao mesmo tempo |
| Arquivo (Windows, SMB) | FSx for Windows | Muitas instâncias ao mesmo tempo |
| Híbrido | Storage Gateway | Datacenter local usando armazenamento na AWS |

- **Cai na prova:** "várias instâncias Linux precisam ler os mesmos arquivos" = EFS; "disco para banco de dados no EC2" = EBS io2; "substituir backup em fita" = Tape Gateway; "migrar 500 TB de um datacenter com internet lenta" = Snowball Edge.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).

- "Qual armazenamento em bloco persistente para EC2?" → EBS.
- "Um volume EBS pode ser usado em outra AZ?" → Não diretamente; cria-se um snapshot e um novo volume na outra AZ.
- "Onde ficam os snapshots do EBS?" → No S3 (gerenciado pela AWS), de forma incremental.
- "Sistema de arquivos compartilhado para várias instâncias Linux." → EFS.
- "Compartilhamento de arquivos Windows integrado ao Active Directory." → FSx for Windows File Server.
- "Sistema de arquivos de alto desempenho para HPC." → FSx for Lustre.
- "Aplicações locais precisam usar armazenamento da AWS." → Storage Gateway.
- "Substituir fitas físicas de backup." → Tape Gateway.
- "Centralizar backups de vários serviços com políticas." → AWS Backup.
- "Mover dezenas de terabytes sem depender da internet." → Snowball Edge.
- "Processar dados num navio sem conexão." → Família Snow (computação na borda).
- "Recuperar servidores em minutos após desastre." → AWS Elastic Disaster Recovery.

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- **EBS Multi-Attach (📌):** só **io1/io2**, até **16 instâncias Nitro na mesma AZ**. ⚠️ "Compartilhar um volume entre muitas instâncias em várias AZs" → **EFS**, não EBS.
- EBS fica preso a uma AZ; para mudar de AZ/região use **snapshot** (armazenado regionalmente no S3 e copiável entre regiões).
- 🔄 **Família Snow:**
  - **Snowmobile** (100 PB): aposentado em 2024.
  - **Snowcone:** sem novos pedidos desde 12/11/2024; suporte encerrado em 12/11/2025.
  - **Snowball Edge:** desde **07/11/2025**, só para **clientes existentes**. Novos clientes: **DataSync** (online), **AWS Data Transfer Terminal** (transferência física em local seguro) ou parceiros; para borda, **Outposts**. Restam o Storage Optimized de 210 TB e o Compute Optimized de 104 vCPUs.
  - ⚠️ **Na prova** o exam guide ainda cita Snowball Edge/Snowmobile: "migrar petabytes com banda limitada" → **Snowball Edge**; "exabytes / 100 PB" → Snowmobile (questões antigas).
- 🧊 Não decorar: IOPS por tipo de EBS, throughput st1/sc1, tamanhos antigos de Snowball (80 TB), preços por GB.
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.8 Amazon S3 — armazenamento de objetos](08-s3.md) · 🏠 [Índice do domínio](README.md) · [3.10 Rede e entrega de conteúdo](10-rede-e-entrega-de-conteudo.md) ➡️
