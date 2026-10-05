# AWS DataSync e AWS Transfer Family

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa precisa levar arquivos entre ambientes ou receber arquivos de parceiros usando protocolos conhecidos. São dois problemas relacionados, mas diferentes.

**Como este serviço ajuda?** DataSync automatiza transferências de dados entre locais compatíveis. Transfer Family oferece acesso por protocolos de transferência compatíveis integrado a armazenamento AWS.

**Exemplo do dia a dia:** Uma equipe sincroniza arquivos com DataSync. Em outro caso, um parceiro envia arquivos por SFTP a um endpoint Transfer Family preparado para isso.

**O que ele não resolve sozinho?** Sincronizar arquivos não migra sozinho toda a aplicação. Cada ferramenta tem fontes, destinos e escopo próprios; a prova não lista todos os serviços desta ficha.

**Primeiras palavras para entender:**

- **Sincronizar:** transferir para aproximar o conteúdo dos locais.
- **SFTP:** protocolo de transferência protegido.
- **Endpoint:** endereço de acesso ao serviço.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Migração / transferência online · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.9 Outros armazenamentos](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md) · [3.17 Migração](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md)
>
> **Em uma frase:** DataSync **move dados online** de forma automatizada e rápida; Transfer Family oferece **SFTP/FTPS/FTP** gerenciado com armazenamento em S3/EFS.
>
> **Escopo oficial:** 🔀 DataSync ⚪ não listado · Transfer Family ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

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
