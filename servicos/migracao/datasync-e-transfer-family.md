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

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **protocolo:** Conjunto de regras da comunicação. Um protocolo define o formato e o comportamento da troca; produtos precisam ser compatíveis com ele.
- **autorização:** Decisão sobre o que uma identidade pode fazer em um recurso. Essa decisão depende das regras e do contexto da solicitação.


**Passo 1.** Separe sincronização entre locais de recebimento por protocolo de arquivo.

**Passo 2.** Prepare a ferramenta correspondente, seus locais e sua autorização; então execute a transferência compatível.

**Passo 3.** Compare resultados e trate falhas. Arquivos movidos não equivalem à migração completa das aplicações que os usam.

## 2. Recursos e opções, com significado

### AWS DataSync

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **EFS:** O EFS oferece um sistema de arquivos compartilhado.
- **FSx:** O FSx oferece sistemas de arquivos gerenciados em modalidades diferentes.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **VM:** Um recurso virtual é criado por software sobre equipamentos físicos. VM significa máquina virtual: computador lógico com sistema operacional e recursos de processamento.
- **GB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.
- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.
- **replicação:** Manutenção de uma cópia dos dados em outro recurso. Se uma alteração incorreta for replicada, a cópia também pode recebê-la; replicação não substitui todo backup.
- **DR:** Recuperação de desastres: plano para recuperar uma operação depois de uma interrupção grave. Inclui recursos, procedimentos e testes.
- **NFS / SMB:** NFS e SMB são protocolos para acesso a arquivos compartilhados. POSIX descreve interfaces e comportamentos de sistemas. Compatibilidade importa para a aplicação usar os arquivos corretamente.
- **metadados:** Informações que descrevem outros dados, como características de um objeto. Conhecer a descrição não significa ler todo o conteúdo.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.
- **HDFS:** Sistema de arquivos distribuído do ecossistema Hadoop. Divide armazenamento entre nós; não é o mesmo modelo de objetos S3.
- **KVM:** Tecnologia de virtualização associada a Linux. É uma camada de execução de máquinas, não o programa de negócio instalado nelas.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Item | Detalhe |
|---|---|
| **Origens** | NFS, SMB, HDFS, armazenamento de objetos, outras nuvens (Azure Blob, Google Cloud Storage), e serviços AWS. |
| **Destinos** | **S3** (qualquer classe), **EFS**, **FSx** (todos os sabores). |
| **Agente** | VM on-premises (VMware, Hyper-V, KVM) ou EC2; transferências entre serviços AWS dispensam agente. |
| **Recursos** | Agendamento, filtros, **verificação de integridade**, limite de banda, criptografia em trânsito, preserva metadados/permissões; até 10× mais rápido que ferramentas open source. |
| **Uso** | Migração de arquivos, replicação para DR, mover dados frios para o S3, alimentar data lakes. |
| **Cobrança** | Por GB transferido. |

### AWS Transfer Family ❌

> ❌ **Fora do escopo da CLF-C02** — documentado só para referência ([lista oficial](../../docs/00-guia-do-exame/escopo-oficial.md)).

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **API Gateway:** API Gateway ajuda a publicar e administrar APIs.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **SFTP / FTP / FTPS:** Protocolos de transferência de arquivos. SFTP usa SSH; FTP não fornece a mesma proteção; FTPS adiciona TLS ao FTP. São opções de compatibilidade diferentes.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.
- **AD:** Tecnologia de diretório para identidades, computadores e controles corporativos. É diferente do cadastro de clientes de uma aplicação pública.
- **B2B:** Relação entre empresas. Em integração, identifica o contexto dos participantes, não um protocolo único.
- **EDI:** CRM trata relacionamento com clientes; CAD, projeto assistido por computador; EDI, troca eletrônica estruturada de dados. São necessidades de aplicação distintas.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Item | Detalhe |
|---|---|
| **Protocolos** | **SFTP**, **FTPS**, **FTP** (só dentro da VPC) e **AS2** (B2B/EDI). |
| **Armazenamento** | Arquivos gravados direto no **S3** ou **EFS**. |
| **Identidade** | Usuários gerenciados pelo serviço, AD ou IdP customizado (Lambda/API Gateway). |
| **Extras** | Workflows pós-upload, *web apps* para usuários não técnicos, conectores SFTP para servidores externos. |
| **Uso** | Parceiros/clientes que já enviam arquivos via SFTP, sem mudar o processo deles. |

### 🔄 Escopo da prova

**Transfer Family** está **fora do escopo** oficial; **DataSync** não aparece na lista atual.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Sincronizar arquivos não migra sozinho toda a aplicação. Cada ferramenta tem fontes, destinos e escopo próprios; a prova não lista todos os serviços desta ficha.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **Storage Gateway:** Storage Gateway faz a ligação entre o ambiente local e o armazenamento em nuvem usando interfaces de arquivos, volumes ou fitas, conforme a modalidade.
- **híbrido:** Combinação de ambiente próprio e nuvem. É necessário definir quais partes ficam em cada lado e como se comunicam.


**DataSync** (transferência/migração online) × **Storage Gateway** (acesso híbrido contínuo) × **Snow** (offline, dispositivo físico) × **Transfer Family** (protocolos FTP para terceiros).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

## 5. Caso resolvido: ligando as peças

Uma equipe sincroniza arquivos com DataSync. Em outro caso, um parceiro envia arquivos por SFTP a um endpoint Transfer Family preparado para isso.

**Aplicando a sequência à situação:**

**Etapa 1:** Separe sincronização entre locais de recebimento por protocolo de arquivo.
**Etapa 2:** Prepare a ferramenta correspondente, seus locais e sua autorização; então execute a transferência compatível.
**Etapa 3:** Compare resultados e trate falhas. Arquivos movidos não equivalem à migração completa das aplicações que os usam.

**Resultado e responsabilidade:** DataSync automatiza transferências de dados entre locais compatíveis. Transfer Family oferece acesso por protocolos de transferência compatíveis integrado a armazenamento AWS.

**Recursos envolvidos:** Locations/tasks DataSync e endpoints/users Transfer Family.

**Decisões que precisam ser tomadas:** Fonte/destino/protocolo, rede e permissões.

**Antes de ler este trecho:**

- **endpoint:** Ponto de acesso a um serviço ou componente. Pode ser um endereço de API ou um recurso de conectividade; identifique qual sentido a seção usa.


**Outra situação comentada:** Copiar arquivos periodicamente difere de dar endpoint SFTP a parceiros.

**Por que não concluir mais do que isso:** DataSync não aparece na lista; Transfer Family está fora do escopo; nenhum migra toda lógica da aplicação

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

A empresa precisa levar arquivos entre ambientes ou receber arquivos de parceiros usando protocolos conhecidos. São dois problemas relacionados, mas diferentes.

**2. O que a solução fornece?**

DataSync automatiza transferências de dados entre locais compatíveis. Transfer Family oferece acesso por protocolos de transferência compatíveis integrado a armazenamento AWS.

**3. Que conclusão seria incorreta?**

Sincronizar arquivos não migra sozinho toda a aplicação. Cada ferramenta tem fontes, destinos e escopo próprios; a prova não lista todos os serviços desta ficha.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Transferir arquivos online de forma automatizada do NAS para o S3."

**Resposta curta:** DataSync.

**Antes de ler este trecho:**

- **NAS:** Armazenamento acessível pela rede como arquivos. É diferente de apresentar um disco em blocos ou objetos por API.


**Fundamento explicado no capítulo:** "Transferir arquivos online de forma automatizada do NAS para o S3." → DataSync.

**Pergunta:** "Parceiros enviam arquivos via SFTP e queremos guardar no S3."

**Resposta curta:** Transfer Family.


**Fundamento explicado no capítulo:** "Parceiros enviam arquivos via SFTP e queremos guardar no S3." → Transfer Family.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html) · [Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
