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

**Passo 1.** Descubra se a aplicação local precisa de arquivos, volumes ou interface de fitas.

**Passo 2.** Prepare um gateway compatível, seu armazenamento local e sua conexão com a AWS. A aplicação usa a interface apresentada.

**Passo 3.** Acompanhe envio, cache e conservação conforme a modalidade. O gateway conecta armazenamento; não migra sozinho o programa.

## 2. Recursos e opções, com significado

### Para que serve

Arquitetura **híbrida**: aplicações locais usando armazenamento em nuvem quase ilimitado.

Substituir backup em **fita física**; *tiering* de arquivos para a nuvem; DR.

### Tipos de gateway

| Tipo | Protocolo | Onde os dados ficam | Uso |
|---|---|---|---|
| **S3 File Gateway** | NFS / SMB | Como **objetos no S3** (um arquivo = um objeto) | Arquivos locais com cópia na nuvem, data lake, backups de bancos |
| **FSx File Gateway** | SMB | **FSx for Windows** | Acesso local de baixa latência a compartilhamentos Windows na AWS. 🔄 **Descontinuado para novos clientes** ✔️ |
| **Volume Gateway** | iSCSI | Volumes na AWS com snapshots EBS | *Cached volumes* (dados na AWS, cache local) ou *stored volumes* (dados locais, backup assíncrono na AWS) |
| **Tape Gateway** | iSCSI VTL | Fitas virtuais no S3, arquivadas no **S3 Glacier / Deep Archive** | **Substituir fitas físicas** sem mudar o software de backup. (A versão do Tape Gateway em hardware **Snowball Edge** foi descontinuada para novos clientes ✔️) |

### Implantação

Como **VM** (VMware, Hyper-V, KVM), em instância EC2 ou appliance de hardware.

Cache local para dados acessados recentemente; transferência otimizada e criptografada (TLS) para a AWS.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele não move toda a aplicação para a AWS nem elimina os requisitos de rede e configuração. Cada modalidade apresenta uma interface e um comportamento diferentes.

### ⚠️ Pegadinhas e não confundir

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
