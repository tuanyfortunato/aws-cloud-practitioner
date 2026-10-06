# AWS Storage Gateway

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa ainda usa aplicações locais, mas quer aproveitar armazenamento AWS sem mudar de uma vez a forma como essas aplicações acessam os dados.

**Como este serviço ajuda?** Storage Gateway faz a ligação entre o ambiente local e o armazenamento em nuvem usando interfaces de arquivos, volumes ou fitas, conforme a modalidade.

**Exemplo do dia a dia:** Um sistema local pode acessar um compartilhamento de arquivos fornecido por um gateway, enquanto o armazenamento em nuvem fica associado ao serviço.

**O que ele não resolve sozinho?** Ele não move toda a aplicação para a AWS nem elimina os requisitos de rede e configuração. Cada modalidade apresenta uma interface e um comportamento diferentes.

**Primeiras palavras para entender:**

- **Gateway:** ponte entre ambientes.
- **Local:** no ambiente da empresa.
- **Cache:** cópia próxima para facilitar acesso a determinados dados.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Armazenamento híbrido · **Domínio:** 3 · **Escopo:** gateway on-premises ligado a uma região · **Tópico do guia:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)
>
> **Em uma frase:** liga aplicações on-premises ao armazenamento da AWS usando protocolos padrão (NFS, SMB, iSCSI), com cache local.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **cache:** Cópia mantida para reutilização rápida. A aplicação ou o serviço precisa decidir atualização e validade, para não servir conteúdo inadequado ou antigo.

**Passo 1.** Descubra se a aplicação local precisa de arquivos, volumes ou interface de fitas.

**Passo 2.** Prepare um gateway compatível, seu armazenamento local e sua conexão com a AWS. A aplicação usa a interface apresentada.

**Passo 3.** Acompanhe envio, cache e conservação conforme a modalidade. O gateway conecta armazenamento; não migra sozinho o programa.

## 2. Recursos e opções, com significado

### Para que serve

Arquitetura **híbrida**: aplicações locais usando armazenamento em nuvem quase ilimitado.

**Antes de ler este trecho:**

- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.
- **DR:** Recuperação de desastres: plano para recuperar uma operação depois de uma interrupção grave. Inclui recursos, procedimentos e testes.

Substituir backup em **fita física**; *tiering* de arquivos para a nuvem; DR.

### Tipos de gateway

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.
- **FSx:** O FSx oferece sistemas de arquivos gerenciados em modalidades diferentes.
- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.
- **protocolo:** Conjunto de regras da comunicação. Um protocolo define o formato e o comportamento da troca; produtos precisam ser compatíveis com ele.
- **NFS / SMB:** NFS e SMB são protocolos para acesso a arquivos compartilhados. POSIX descreve interfaces e comportamentos de sistemas. Compatibilidade importa para a aplicação usar os arquivos corretamente.
- **iSCSI:** Protocolo para apresentar armazenamento em blocos pela rede. É diferente de acessar objetos por uma API ou arquivos por um compartilhamento.
- **data lake:** Conjunto de dados mantido para usos diversos, frequentemente em armazenamento de objetos. Organização, catálogo e permissões continuam necessários.
- **objeto:** Unidade de dados guardada no armazenamento de objetos: conteúdo, identificação e informações associadas. Não é uma máquina nem um programa em execução.
- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.
- **VTL:** Biblioteca virtual de fitas: interface que apresenta armazenamento como fitas para aplicações compatíveis.

| Tipo | Protocolo | Onde os dados ficam | Uso |
|---|---|---|---|
| **S3 File Gateway** | NFS / SMB | Como **objetos no S3** (um arquivo = um objeto) | Arquivos locais com cópia na nuvem, data lake, backups de bancos |
| **FSx File Gateway** | SMB | **FSx for Windows** | Acesso local de baixa latência a compartilhamentos Windows na AWS. 🔄 **Descontinuado para novos clientes** ✔️ |
| **Volume Gateway** | iSCSI | Volumes na AWS com snapshots EBS | *Cached volumes* (dados na AWS, cache local) ou *stored volumes* (dados locais, backup assíncrono na AWS) |
| **Tape Gateway** | iSCSI VTL | Fitas virtuais no S3, arquivadas no **S3 Glacier / Deep Archive** | **Substituir fitas físicas** sem mudar o software de backup. (A versão do Tape Gateway em hardware **Snowball Edge** foi descontinuada para novos clientes ✔️) |

### Implantação

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **VM:** Um recurso virtual é criado por software sobre equipamentos físicos. VM significa máquina virtual: computador lógico com sistema operacional e recursos de processamento.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.
- **KVM:** Tecnologia de virtualização associada a Linux. É uma camada de execução de máquinas, não o programa de negócio instalado nelas.

Como **VM** (VMware, Hyper-V, KVM), em instância EC2 ou appliance de hardware.

**Antes de ler este trecho:**

- **TLS:** HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.

Cache local para dados acessados recentemente; transferência otimizada e criptografada (TLS) para a AWS.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

**Antes de ler este trecho:**

- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.

Ele não move toda a aplicação para a AWS nem elimina os requisitos de rede e configuração. Cada modalidade apresenta uma interface e um comportamento diferentes.

### ⚠️ Pegadinhas e não confundir

**Antes de ler este trecho:**

- **Storage Gateway:** Storage Gateway faz a ligação entre o ambiente local e o armazenamento em nuvem usando interfaces de arquivos, volumes ou fitas, conforme a modalidade.
- **híbrido:** Combinação de ambiente próprio e nuvem. É necessário definir quais partes ficam em cada lado e como se comunicam.

**Storage Gateway × DataSync:** acesso **contínuo** híbrido × **transferência/migração** de dados.

"Substituir backup em fita" → **Tape Gateway**.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Armazenamento usado na AWS + requisições + transferência de saída; Tape Gateway por fita virtual armazenada/recuperada.

## 5. Caso resolvido: ligando as peças

Um sistema local pode acessar um compartilhamento de arquivos fornecido por um gateway, enquanto o armazenamento em nuvem fica associado ao serviço.

**Aplicando a sequência à situação:**

**Etapa 1:** Descubra se a aplicação local precisa de arquivos, volumes ou interface de fitas.
**Etapa 2:** Prepare um gateway compatível, seu armazenamento local e sua conexão com a AWS. A aplicação usa a interface apresentada.
**Etapa 3:** Acompanhe envio, cache e conservação conforme a modalidade. O gateway conecta armazenamento; não migra sozinho o programa.

**Resultado e responsabilidade:** Storage Gateway faz a ligação entre o ambiente local e o armazenamento em nuvem usando interfaces de arquivos, volumes ou fitas, conforme a modalidade.

**Recursos envolvidos:** Gateway no ambiente do cliente, cache local e armazenamento AWS.

**Decisões que precisam ser tomadas:** Modalidade de arquivos, volumes ou fitas e capacidade local.

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.

**Outra situação comentada:** Sistema de backup usa interface de fita: Tape Gateway, em vez de reescrever o sistema para API S3.

**Por que não concluir mais do que isso:** Não é migração instantânea de toda aplicação; precisa host, cache e conectividade conforme modalidade

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Aplicações locais precisam usar armazenamento da AWS."

**Resposta curta:** Storage Gateway.

**Pergunta:** "Substituir fitas físicas de backup."

**Resposta curta:** Tape Gateway.

**Pergunta:** "Arquivos via NFS/SMB gravados como objetos no S3."

**Resposta curta:** S3 File Gateway.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Storage Gateway](https://docs.aws.amazon.com/storagegateway/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
