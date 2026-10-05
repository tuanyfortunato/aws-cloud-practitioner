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

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon EBS (Elastic Block Store) e Instance Store](../../servicos/armazenamento/ebs.md) · [Amazon EFS (Elastic File System)](../../servicos/armazenamento/efs.md) · [Amazon FSx](../../servicos/armazenamento/fsx.md) · [AWS Storage Gateway](../../servicos/armazenamento/storage-gateway.md) · [AWS Backup](../../servicos/armazenamento/aws-backup.md) · [AWS Elastic Disaster Recovery (AWS DRS)](../../servicos/armazenamento/elastic-disaster-recovery.md) · [Família AWS Snow (Snowball Edge, Snowcone, Snowmobile)](../../servicos/migracao/snow-family.md) · [AWS DataSync e AWS Transfer Family](../../servicos/migracao/datasync-e-transfer-family.md)

> ⚠️ **Atualização do exam guide (verificado em 04/10/2026):** A **família Snow** e o **DataSync** não aparecem na lista oficial atual (o Snowball Edge está fechado a novos clientes); **FSx for Lustre** e **Transfer Family** estão **fora do escopo**. [Ver escopo oficial](../00-guia-do-exame/escopo-oficial.md).

⬅️ [3.8 Amazon S3 — armazenamento de objetos](08-s3.md) · 🏠 [Índice do domínio](README.md) · [3.10 Rede e entrega de conteúdo](10-rede-e-entrega-de-conteudo.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.


Armazenamento em blocos apresenta um disco para o sistema. Armazenamento de arquivos apresenta pastas e arquivos por uma interface de rede. Armazenamento de objetos apresenta conteúdo por operações de serviço. A forma como o programa usa os dados orienta a escolha.

Depois da compatibilidade, avalie compartilhamento, desempenho, disponibilidade e conservação. Um disco para uma máquina não é automaticamente uma pasta para várias. Um backup protege recuperação, mas não transforma sozinho um armazenamento em ambiente de atendimento ativo.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

o **EBS** é o **HD do computador**; o **EFS** é a **pasta de rede** que todos abrem ao mesmo tempo; o **Storage Gateway** é a **ponte** entre o escritório e a nuvem; a **família Snow** é um **HD blindado enviado pelo correio**.

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Amazon EBS / EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.


**Amazon EBS (Elastic Block Store):** armazenamento em **bloco** (disco) para EC2.

**Antes de ler este trecho:**

- **AZ:** Parte isolada da infraestrutura dentro de uma região, formada por um ou mais datacenters. Distribuir recursos entre zonas pode reduzir o impacto de uma falha localizada.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.


  - Persistente, preso a **uma AZ**, normalmente ligado a uma instância por vez.
**Antes de ler este trecho:**

- **IOPS:** Quantidade de operações de leitura e escrita por segundo. Ajuda a descrever o comportamento de um armazenamento, mas não mede sozinha a quantidade de bytes transferidos.
- **throughput:** Quantidade de dados ou de trabalho processada por unidade de tempo. É diferente de latência, que mede quanto uma operação demora.
- **SSD:** Tipo de armazenamento sem partes mecânicas, usado para acesso rápido a dados. A escolha de um volume também envolve sua capacidade e limites de desempenho.
- **provisionado:** Recurso ou capacidade já disponibilizado para uso. Em algumas cobranças, a disponibilidade mantida importa mesmo sem execução de trabalho de negócio.
- **HDD:** Armazenamento por disco mecânico. Seu comportamento difere de SSD; a necessidade de acesso orienta a escolha.


  - Tipos: SSD de uso geral (**gp3**/gp2), SSD de IOPS provisionado (**io2**/io1, para bancos críticos), HDD otimizado para throughput (**st1**, big data e logs) e HDD frio (**sc1**, acesso raro).
**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.


  - **Snapshots** incrementais, guardados no S3, copiáveis entre regiões; usados para backup e para criar volumes em outra AZ.
**Antes de ler este trecho:**

- **KMS:** Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.


  - Criptografia com KMS.
**Antes de ler este trecho:**

- **instance store:** Armazenamento local temporário da máquina física. Não é lugar seguro para a única cópia de dados que precisam sobreviver às ações descritas no ciclo de vida.


**Instance store:** disco físico do host. Muito rápido, mas **efêmero**: perde os dados ao parar ou encerrar a instância.

**Antes de ler este trecho:**

- **Amazon EFS / EFS:** O EFS oferece um sistema de arquivos compartilhado.
- **NFS:** NFS e SMB são protocolos para acesso a arquivos compartilhados. POSIX descreve interfaces e comportamentos de sistemas. Compatibilidade importa para a aplicação usar os arquivos corretamente.


**Amazon EFS (Elastic File System):** sistema de arquivos **compartilhado** (NFS) para **Linux**, acessado por muitas instâncias ao mesmo tempo, em várias AZs. Cresce e encolhe sozinho; paga pelo que usa. Classes Standard, Infrequent Access e Archive.

**Antes de ler este trecho:**

- **Amazon FSx / FSx:** O FSx oferece sistemas de arquivos gerenciados em modalidades diferentes.


**Amazon FSx:** sistemas de arquivos gerenciados de terceiros:

**Antes de ler este trecho:**

- **Active Directory:** Tecnologia de diretório para identidades, computadores e controles corporativos. É diferente do cadastro de clientes de uma aplicação pública.


  - **FSx for Windows File Server:** SMB, integrado ao Active Directory.
**Antes de ler este trecho:**

- **HPC:** Computação de alto desempenho: execução de cálculos intensivos, como simulações. O requisito concreto pode envolver processamento, comunicação ou outro recurso.
- **machine learning:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.


  - **FSx for Lustre:** alto desempenho para HPC e machine learning, integrado ao S3.
**Antes de ler este trecho:**

- **ONTAP:** Tecnologia de armazenamento e gerenciamento de arquivos associada a uma modalidade FSx. A aplicação precisa da compatibilidade e dos recursos daquela modalidade.
- **NAS:** Armazenamento acessível pela rede como arquivos. É diferente de apresentar um disco em blocos ou objetos por API.


  - **FSx for NetApp ONTAP** e **FSx for OpenZFS:** para migrar storages NAS existentes.
**Antes de ler este trecho:**

- **AWS Storage Gateway / Storage Gateway:** Storage Gateway faz a ligação entre o ambiente local e o armazenamento em nuvem usando interfaces de arquivos, volumes ou fitas, conforme a modalidade.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **datacenter:** Instalação física com equipamentos de computação, rede, energia e refrigeração. A nuvem continua dependendo desses equipamentos, mas o cliente não precisa manter o prédio.
- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.
- **híbrido:** Combinação de ambiente próprio e nuvem. É necessário definir quais partes ficam em cada lado e como se comunicam.


**AWS Storage Gateway:** armazenamento **híbrido**; liga o datacenter on-premises ao armazenamento na AWS.


  - **S3 File Gateway:** arquivos via NFS/SMB gravados como objetos no S3.
**Antes de ler este trecho:**

- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.


  - **FSx File Gateway:** acesso local de baixa latência ao FSx for Windows.
**Antes de ler este trecho:**

- **iSCSI:** Protocolo para apresentar armazenamento em blocos pela rede. É diferente de acessar objetos por uma API ou arquivos por um compartilhamento.
- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.


  - **Volume Gateway:** volumes iSCSI com cópia na AWS.

  - **Tape Gateway:** fitas virtuais; substitui backup em fita física, arquivando no S3 Glacier.
**Antes de ler este trecho:**

- **AWS Backup:** AWS Backup centraliza políticas e operações de backup para recursos compatíveis.
- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **Aurora:** Aurora é um banco relacional da AWS dentro da família RDS.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.


**AWS Backup:** gerencia **backups de forma centralizada** com políticas (EC2, EBS, RDS, Aurora, DynamoDB, EFS, FSx, S3 etc.), inclusive entre contas e regiões.

**Antes de ler este trecho:**

- **AWS Elastic Disaster Recovery / Elastic Disaster Recovery:** Elastic Disaster Recovery replica dados de servidores compatíveis para preparar sua recuperação em máquinas AWS.


**AWS Elastic Disaster Recovery:** replica servidores (on-premises ou na nuvem) continuamente para a AWS e permite recuperar em minutos em caso de desastre.

**Antes de ler este trecho:**

- **Família AWS Snow:** A família Snow foi associada a dispositivos físicos para transferência e processamento local.
- **campo:** Informação nomeada dentro de um registro, como nome ou data. Consultas usam os campos conforme a estrutura e o modelo do banco.


**Família AWS Snow:** dispositivos físicos para **mover grandes volumes de dados** quando a rede é lenta, cara ou inexistente, e para **computação na borda** em locais desconectados (navios, campo, áreas remotas).

**Antes de ler este trecho:**

- **TB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.


  - **Snowball Edge:** versões otimizadas para armazenamento (dezenas de TB) ou para computação.

  - Versões menores (Snowcone) e o caminhão Snowmobile foram descontinuados, mas podem aparecer em questões antigas.

  - Regra prática: se transferir pela rede levaria semanas, use Snow.
**Antes de ler este trecho:**

- **SFTP / FTP / FTPS:** Protocolos de transferência de arquivos. SFTP usa SSH; FTP não fornece a mesma proteção; FTPS adiciona TLS ao FTP. São opções de compatibilidade diferentes.


**Transferência online:** AWS DataSync (copia dados de NFS/SMB on-premises para S3, EFS ou FSx de forma automatizada) e AWS Transfer Family (SFTP/FTPS/FTP direto para S3 ou EFS).


**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **HTTP:** Protocolo de pedidos e respostas usado na web. Uma URL e um método indicam a operação; HTTP sozinho não protege o conteúdo por criptografia.
- **objeto:** Unidade de dados guardada no armazenamento de objetos: conteúdo, identificação e informações associadas. Não é uma máquina nem um programa em execução.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Tipo | Serviço | Acesso |
| --- | --- | --- |
| Objeto | S3 | Via API/HTTP, de qualquer lugar |
| Bloco | EBS, instance store | Um disco ligado a uma instância EC2 |
| Arquivo (Linux, NFS) | EFS | Muitas instâncias ao mesmo tempo |
| Arquivo (Windows, SMB) | FSx for Windows | Muitas instâncias ao mesmo tempo |
| Híbrido | Storage Gateway | Datacenter local usando armazenamento na AWS |



**Cai na prova:** "várias instâncias Linux precisam ler os mesmos arquivos" = EFS; "disco para banco de dados no EC2" = EBS io2; "substituir backup em fita" = Tape Gateway; "migrar 500 TB de um datacenter com internet lenta" = Snowball Edge.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **replicação:** Manutenção de uma cópia dos dados em outro recurso. Se uma alteração incorreta for replicada, a cópia também pode recebê-la; replicação não substitui todo backup.
- **DR:** Recuperação de desastres: plano para recuperar uma operação depois de uma interrupção grave. Inclui recursos, procedimentos e testes.


**Primeiro, identifique o funcionamento:** Bloco funciona como disco; arquivo usa protocolos de sistema de arquivos; objeto é acessado por API. Backup guarda pontos de recuperação; replicação para DR mantém dados preparados para recuperação.

**Depois, compare as escolhas:** EBS para disco de EC2; EFS para arquivos NFS compartilhados; FSx para necessidades de sistema de arquivos específico; Storage Gateway para integrar ambiente próprio ao armazenamento AWS.

**Por fim, verifique o limite:** EBS pertence a uma AZ e não é um compartilhamento NFS. Multi-Attach é limitado a configurações suportadas. Backup e replicação não dispensam teste de restauração.

## 4. Caso resolvido

Duas EC2 Linux em AZs diferentes precisam dos mesmos arquivos. Um único EBS atende diretamente?

**Raciocínio e resposta:** Não. EFS é a opção típica de arquivos compartilhados; um EBS precisa respeitar sua AZ e condições de anexação.

A resposta muda se mudar o requisito destacado. Compare a necessidade com a função da solução, em vez de apenas associar duas palavras.

## 5. Revisão do capítulo

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Sua aplicação pode precisar de um disco próprio, de pastas compartilhadas ou de ligação com arquivos mantidos na empresa. Essas necessidades não são iguais.

**2. O que a solução fornece?**

Este tópico compara armazenamento em blocos, arquivos compartilhados e integração com ambientes locais, além de cópias de segurança e recuperação.

**3. Que conclusão seria incorreta?**

Escolher armazenamento só pelo nome ou preço pode causar incompatibilidade. Primeiro descubra como a aplicação precisa ler e gravar os dados.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

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


**Fundamento explicado no capítulo:** "Qual armazenamento em bloco persistente para EC2?" → EBS.

**Pergunta:** "Um volume EBS pode ser usado em outra AZ?"

**Resposta curta:** Não diretamente; cria-se um snapshot e um novo volume na outra AZ.

**Antes de ler este trecho:**

- **snapshot:** Cópia de estado de um recurso em determinado momento, conforme o serviço. Restauração pode criar um novo recurso; não presuma uma máquina pronta e instantânea.


**Fundamento explicado no capítulo:** "Um volume EBS pode ser usado em outra AZ?" → Não diretamente; cria-se um snapshot e um novo volume na outra AZ.

**Pergunta:** "Onde ficam os snapshots do EBS?"

**Resposta curta:** No S3 (gerenciado pela AWS), de forma incremental.

**Antes de ler este trecho:**

- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.


**Fundamento explicado no capítulo:** "Onde ficam os snapshots do EBS?" → No S3 (gerenciado pela AWS), de forma incremental.

**Pergunta:** "Sistema de arquivos compartilhado para várias instâncias Linux."

**Resposta curta:** EFS.


**Fundamento explicado no capítulo:** "Sistema de arquivos compartilhado para várias instâncias Linux." → EFS.

**Pergunta:** "Compartilhamento de arquivos Windows integrado ao Active Directory."

**Resposta curta:** FSx for Windows File Server.


**Fundamento explicado no capítulo:** "Compartilhamento de arquivos Windows integrado ao Active Directory." → FSx for Windows File Server.

**Pergunta:** "Sistema de arquivos de alto desempenho para HPC."

**Resposta curta:** FSx for Lustre.


**Fundamento explicado no capítulo:** "Sistema de arquivos de alto desempenho para HPC." → FSx for Lustre.

**Pergunta:** "Aplicações locais precisam usar armazenamento da AWS."

**Resposta curta:** Storage Gateway.


**Fundamento explicado no capítulo:** "Aplicações locais precisam usar armazenamento da AWS." → Storage Gateway.

**Pergunta:** "Substituir fitas físicas de backup."

**Resposta curta:** Tape Gateway.


**Fundamento explicado no capítulo:** "Substituir fitas físicas de backup." → Tape Gateway.

**Pergunta:** "Centralizar backups de vários serviços com políticas."

**Resposta curta:** AWS Backup.


**Fundamento explicado no capítulo:** "Centralizar backups de vários serviços com políticas." → AWS Backup.

**Pergunta:** "Mover dezenas de terabytes sem depender da internet."

**Resposta curta:** Snowball Edge.


**Fundamento explicado no capítulo:** "Mover dezenas de terabytes sem depender da internet." → Snowball Edge.

**Pergunta:** "Processar dados num navio sem conexão."

**Resposta curta:** Família Snow (computação na borda).


**Fundamento explicado no capítulo:** "Processar dados num navio sem conexão." → Família Snow (computação na borda).

**Pergunta:** "Recuperar servidores em minutos após desastre."

**Resposta curta:** AWS Elastic Disaster Recovery.


**Fundamento explicado no capítulo:** "Recuperar servidores em minutos após desastre." → AWS Elastic Disaster Recovery.

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
