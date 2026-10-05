# AWS DataSync e AWS Transfer Family

> **Categoria:** Migração / transferência online · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.9 Outros armazenamentos](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md) · [3.17 Migração](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md)
>
> **Em uma frase:** DataSync **move dados online** de forma automatizada e rápida; Transfer Family oferece **SFTP/FTPS/FTP** gerenciado com armazenamento em S3/EFS.
>
> **Escopo oficial:** 🔀 DataSync ⚪ não listado · Transfer Family ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** o DataSync é um **caminhão de dados pela rede**; o Transfer Family é uma **agência de correio SFTP** para parceiros.

- ✅ **Escolha quando:** precisa **copiar arquivos online** para S3, EFS ou FSx, ou **receber arquivos por SFTP**.
- 🚫 **Não é a resposta quando:** precisa de **acesso híbrido contínuo** → [Storage Gateway](../armazenamento/storage-gateway.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "transferir arquivos online" → DataSync; "SFTP" → Transfer Family (fora da prova).
<!-- didatico:fim -->

## AWS DataSync

| Item | Detalhe |
|---|---|
| **Origens** | NFS, SMB, HDFS, armazenamento de objetos, outras nuvens (Azure Blob, Google Cloud Storage), e serviços AWS. |
| **Destinos** | **S3** (qualquer classe), **EFS**, **FSx** (todos os sabores). |
| **Agente** | VM on-premises (VMware, Hyper-V, KVM) ou EC2; transferências entre serviços AWS dispensam agente. |
| **Recursos** | Agendamento, filtros, **verificação de integridade**, limite de banda, criptografia em trânsito, preserva metadados/permissões; até 10× mais rápido que ferramentas open source. |
| **Uso** | Migração de arquivos, replicação para DR, mover dados frios para o S3, alimentar data lakes. |
| **Cobrança** | Por GB transferido. |

## AWS Transfer Family ❌

> ❌ **Fora do escopo da CLF-C02** — documentado só para referência ([lista oficial](../../docs/00-guia-do-exame/escopo-oficial.md)).

| Item | Detalhe |
|---|---|
| **Protocolos** | **SFTP**, **FTPS**, **FTP** (só dentro da VPC) e **AS2** (B2B/EDI). |
| **Armazenamento** | Arquivos gravados direto no **S3** ou **EFS**. |
| **Identidade** | Usuários gerenciados pelo serviço, AD ou IdP customizado (Lambda/API Gateway). |
| **Extras** | Workflows pós-upload, *web apps* para usuários não técnicos, conectores SFTP para servidores externos. |
| **Uso** | Parceiros/clientes que já enviam arquivos via SFTP, sem mudar o processo deles. |

## 🔄 Escopo da prova

- **Transfer Family** está **fora do escopo** oficial; **DataSync** não aparece na lista atual.

## ⚠️ Não confundir

- **DataSync** (transferência/migração online) × **Storage Gateway** (acesso híbrido contínuo) × **Snow** (offline, dispositivo físico) × **Transfer Family** (protocolos FTP para terceiros).

## ❓ Perguntas típicas

- "Transferir arquivos online de forma automatizada do NAS para o S3." → DataSync.
- "Parceiros enviam arquivos via SFTP e queremos guardar no S3." → Transfer Family.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Locations/tasks DataSync e endpoints/users Transfer Family |
| **O que você decide/configura?** | Fonte/destino/protocolo, rede e permissões |
| **Em que ordem as coisas acontecem?** | DataSync transfere conjuntos de arquivos; Transfer oferece interface de transferência suportada |
| **O que pode fazer, e em que condição?** | Atendem movimentação de dados com objetivos diferentes |
| **O que não pode presumir?** | DataSync não aparece na lista; Transfer Family está fora do escopo; nenhum migra toda lógica da aplicação |

**Caso comentado:** Copiar arquivos periodicamente difere de dar endpoint SFTP a parceiros.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html) · [Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html)
