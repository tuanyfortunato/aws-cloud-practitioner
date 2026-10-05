# Amazon EFS (Elastic File System)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Várias máquinas Linux precisam ler e gravar os mesmos arquivos, sem cada uma manter uma cópia separada.

**Como este serviço ajuda?** O EFS oferece um sistema de arquivos compartilhado. Máquinas autorizadas podem montar esse armazenamento e usá-lo como um conjunto de pastas acessíveis pela rede.

**Exemplo do dia a dia:** Vários servidores de uma aplicação acessam a mesma pasta de documentos pelo EFS. Um arquivo gravado ali pode ser acessado pelos outros servidores autorizados.

**O que ele não resolve sozinho?** Ele fornece arquivos compartilhados, não um banco de dados nem armazenamento local de cada máquina. Rede, permissões e compatibilidade precisam ser configuradas.

**Primeiras palavras para entender:**

- **Sistema de arquivos:** organização de arquivos e pastas.
- **Montar:** tornar esse armazenamento acessível ao sistema.
- **NFS:** protocolo usado para acessar arquivos pela rede.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Armazenamento de arquivos · **Domínio:** 3 · **Escopo:** Regional (multi-AZ) ou One Zone · **Tópico do guia:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)
>
> **Em uma frase:** sistema de arquivos NFS gerenciado e elástico, compartilhado por milhares de instâncias Linux em várias AZs.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.


**Passo 1.** Crie um sistema de arquivos e prepare os pontos de acesso de rede necessários.

**Passo 2.** Permita que máquinas compatíveis e autorizadas montem o armazenamento. Elas passam a acessar um conjunto compartilhado de arquivos.

**Passo 3.** Administre permissões, desempenho e proteção dos dados. Compartilhar não significa liberar o conteúdo a qualquer máquina.

## 2. Recursos e opções, com significado

### Para que serve

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **ML:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.
- **CMS:** Tipos de aplicação: gestão de conteúdo, relacionamento com clientes e gestão empresarial. São funções de software, não nomes de um modelo de armazenamento.


Conteúdo web compartilhado, diretórios home, CMS, pipelines de mídia, ML, contêineres e Lambda que precisam de arquivos persistentes.

### Conceitos e configurações

**Antes de ler este trecho:**

- **EFS:** O EFS oferece um sistema de arquivos compartilhado.
- **AWS Backup:** AWS Backup centraliza políticas e operações de backup para recursos compatíveis.
- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.
- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **KMS:** Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.
- **IA:** Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **throughput:** Quantidade de dados ou de trabalho processada por unidade de tempo. É diferente de latência, que mede quanto uma operação demora.
- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.
- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **AZ:** Parte isolada da infraestrutura dentro de uma região, formada por um ou mais datacenters. Distribuir recursos entre zonas pode reduzir o impacto de uma falha localizada.
- **regional:** O recurso ou a operação pertence a uma região. Serviços globais podem administrar objetos regionais; leia o alcance do recurso, não apenas o nome do serviço.
- **replicação:** Manutenção de uma cópia dos dados em outro recurso. Se uma alteração incorreta for replicada, a cópia também pode recebê-la; replicação não substitui todo backup.
- **protocolo:** Conjunto de regras da comunicação. Um protocolo define o formato e o comportamento da troca; produtos precisam ser compatíveis com ele.
- **TLS:** HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.
- **DNS:** Sistema que relaciona nomes a informações de endereço e outros registros. Resolver o nome de um site não hospeda o site nem garante que ele está funcionando.
- **security group:** Regras de tráfego associadas a interfaces ou recursos compatíveis. É um controle de rede, não uma permissão IAM para ler um arquivo ou chamar uma API.
- **NFS / POSIX:** NFS e SMB são protocolos para acesso a arquivos compartilhados. POSIX descreve interfaces e comportamentos de sistemas. Compatibilidade importa para a aplicação usar os arquivos corretamente.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.
- **legado:** Sistema existente com tecnologias ou dependências que precisam ser preservadas ou avaliadas numa mudança. Antigo não significa automaticamente que pode ser desligado.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Item | Detalhe |
|---|---|
| **Protocolo** | **NFS v4.0/4.1** — clientes **Linux** (não suporta Windows). |
| **Mount targets** | Um por AZ, com security group; instâncias montam pelo DNS do EFS. |
| **Tipo de file system** | **Regional** (dados em várias AZs — padrão) ou **One Zone** (uma AZ, mais barato). |
| **Classes de armazenamento** | **Standard**, **Infrequent Access (IA)** e **Archive**. |
| **Lifecycle management** | Move arquivos sem acesso para IA/Archive após N dias e de volta ao Standard quando acessados. |
| **Throughput mode** | ✔️ **Elastic** (padrão e recomendado, escala automática, paga pelo uso), **Provisioned** (cargas previsíveis) ou **Bursting**. |
| **Performance mode** | General Purpose (padrão, menor latência) ou Max I/O (legado). |
| **Criptografia** | Em repouso (KMS, definida na criação) e em trânsito (TLS no mount helper). |
| **Acesso** | IAM, *access points* (diretório raiz e usuário POSIX por aplicação), security groups. |
| **Replicação e backup** | EFS Replication (outra região/AZ) e integração com AWS Backup. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele fornece arquivos compartilhados, não um banco de dados nem armazenamento local de cada máquina. Rede, permissões e compatibilidade precisam ser configuradas.

### ⚠️ Pegadinhas e não confundir

**Antes de ler este trecho:**

- **EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.


**EFS × EBS:** compartilhado entre muitas instâncias e AZs × disco de uma instância numa AZ.

**Antes de ler este trecho:**

- **FSx:** O FSx oferece sistemas de arquivos gerenciados em modalidades diferentes.
- **Active Directory:** Tecnologia de diretório para identidades, computadores e controles corporativos. É diferente do cadastro de clientes de uma aplicação pública.


**EFS × FSx for Windows:** Linux/NFS × Windows/SMB com Active Directory.

**Antes de ler este trecho:**

- **provisionado:** Recurso ou capacidade já disponibilizado para uso. Em algumas cobranças, a disponibilidade mantida importa mesmo sem execução de trabalho de negócio.


EFS cobra pelo usado; EBS cobra pelo provisionado.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **GB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.


Por **GB efetivamente armazenado** por mês (cresce e encolhe sozinho) + throughput (Elastic/Provisioned) + acessos a IA/Archive.

### Segurança e responsabilidade compartilhada

**Antes de ler este trecho:**

- **durabilidade:** Capacidade de preservar os dados armazenados. É diferente de disponibilidade, que trata de conseguir acessá-los quando necessário.


**AWS:** disponibilidade, durabilidade e escala do sistema de arquivos.


**Cliente:** security groups dos mount targets, permissões POSIX/IAM, criptografia, backup.

## 5. Caso resolvido: ligando as peças

Vários servidores de uma aplicação acessam a mesma pasta de documentos pelo EFS. Um arquivo gravado ali pode ser acessado pelos outros servidores autorizados.

**Aplicando a sequência à situação:**

**Etapa 1:** Crie um sistema de arquivos e prepare os pontos de acesso de rede necessários.
**Etapa 2:** Permita que máquinas compatíveis e autorizadas montem o armazenamento. Elas passam a acessar um conjunto compartilhado de arquivos.
**Etapa 3:** Administre permissões, desempenho e proteção dos dados. Compartilhar não significa liberar o conteúdo a qualquer máquina.

**Resultado e responsabilidade:** O EFS oferece um sistema de arquivos compartilhado. Máquinas autorizadas podem montar esse armazenamento e usá-lo como um conjunto de pastas acessíveis pela rede.

**Recursos envolvidos:** Sistema de arquivos, mount targets, access points e classes.

**Decisões que precisam ser tomadas:** Rede NFS, permissões, modalidade regional/uma zona e lifecycle.

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **autorização:** Decisão sobre o que uma identidade pode fazer em um recurso. Essa decisão depende das regras e do contexto da solicitação.


**Outra situação comentada:** Vários servidores web Linux usam o mesmo conteúdo: EFS, com configuração dos mounts.

**Por que não concluir mais do que isso:** Precisa de conectividade e autorização de rede/arquivo; não é disco de boot EC2

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Várias máquinas Linux precisam ler e gravar os mesmos arquivos, sem cada uma manter uma cópia separada.

**2. O que a solução fornece?**

O EFS oferece um sistema de arquivos compartilhado. Máquinas autorizadas podem montar esse armazenamento e usá-lo como um conjunto de pastas acessíveis pela rede.

**3. Que conclusão seria incorreta?**

Ele fornece arquivos compartilhados, não um banco de dados nem armazenamento local de cada máquina. Rede, permissões e compatibilidade precisam ser configuradas.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Várias instâncias Linux em AZs diferentes precisam ler e gravar os mesmos arquivos."

**Resposta curta:** EFS.


**Fundamento explicado no capítulo:** "Várias instâncias Linux em AZs diferentes precisam ler e gravar os mesmos arquivos." → EFS.

**Pergunta:** "Reduzir custo de arquivos pouco acessados no EFS."

**Resposta curta:** Lifecycle para IA/Archive.


**Fundamento explicado no capítulo:** "Reduzir custo de arquivos pouco acessados no EFS." → Lifecycle para IA/Archive.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
