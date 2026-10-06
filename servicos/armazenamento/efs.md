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

## 1. A sequência de funcionamento

**Passo 1.** Crie um sistema de arquivos e prepare os pontos de acesso de rede necessários.

**Passo 2.** Permita que máquinas compatíveis e autorizadas montem o armazenamento. Elas passam a acessar um conjunto compartilhado de arquivos.

**Passo 3.** Administre permissões, desempenho e proteção dos dados. Compartilhar não significa liberar o conteúdo a qualquer máquina.

## 2. Recursos e opções, com significado

### Para que serve

Conteúdo web compartilhado, diretórios home, CMS, pipelines de mídia, ML, contêineres e Lambda que precisam de arquivos persistentes.

### Conceitos e configurações

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

**EFS × EBS:** compartilhado entre muitas instâncias e AZs × disco de uma instância numa AZ.

**EFS × FSx for Windows:** Linux/NFS × Windows/SMB com Active Directory.

EFS cobra pelo usado; EBS cobra pelo provisionado.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por **GB efetivamente armazenado** por mês (cresce e encolhe sozinho) + throughput (Elastic/Provisioned) + acessos a IA/Archive.

### Segurança e responsabilidade compartilhada

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

**Outra situação comentada:** Vários servidores web Linux usam o mesmo conteúdo: EFS, com configuração dos mounts.

**Por que não concluir mais do que isso:** Precisa de conectividade e autorização de rede/arquivo; não é disco de boot EC2

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Várias instâncias Linux em AZs diferentes precisam ler e gravar os mesmos arquivos."

**Resposta curta:** EFS.

**Fundamento explicado no capítulo:** **Mount targets**; Um por AZ, com security group; instâncias montam pelo DNS do EFS.

**Pergunta:** "Reduzir custo de arquivos pouco acessados no EFS."

**Resposta curta:** Lifecycle para IA/Archive.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
