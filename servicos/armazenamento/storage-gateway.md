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

## Para que serve

- Arquitetura **híbrida**: aplicações locais usando armazenamento em nuvem quase ilimitado.
- Substituir backup em **fita física**; *tiering* de arquivos para a nuvem; DR.

## Tipos de gateway

| Tipo | Protocolo | Onde os dados ficam | Uso |
|---|---|---|---|
| **S3 File Gateway** | NFS / SMB | Como **objetos no S3** (um arquivo = um objeto) | Arquivos locais com cópia na nuvem, data lake, backups de bancos |
| **FSx File Gateway** | SMB | **FSx for Windows** | Acesso local de baixa latência a compartilhamentos Windows na AWS. 🔄 **Descontinuado para novos clientes** ✔️ |
| **Volume Gateway** | iSCSI | Volumes na AWS com snapshots EBS | *Cached volumes* (dados na AWS, cache local) ou *stored volumes* (dados locais, backup assíncrono na AWS) |
| **Tape Gateway** | iSCSI VTL | Fitas virtuais no S3, arquivadas no **S3 Glacier / Deep Archive** | **Substituir fitas físicas** sem mudar o software de backup. (A versão do Tape Gateway em hardware **Snowball Edge** foi descontinuada para novos clientes ✔️) |

## Implantação

- Como **VM** (VMware, Hyper-V, KVM), em instância EC2 ou appliance de hardware.
- Cache local para dados acessados recentemente; transferência otimizada e criptografada (TLS) para a AWS.

## Cobrança

- Armazenamento usado na AWS + requisições + transferência de saída; Tape Gateway por fita virtual armazenada/recuperada.

## ⚠️ Pegadinhas e não confundir

- **Storage Gateway × DataSync:** acesso **contínuo** híbrido × **transferência/migração** de dados.
- "Substituir backup em fita" → **Tape Gateway**.

## ❓ Perguntas típicas

- "Aplicações locais precisam usar armazenamento da AWS." → Storage Gateway.
- "Substituir fitas físicas de backup." → Tape Gateway.
- "Arquivos via NFS/SMB gravados como objetos no S3." → S3 File Gateway.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Gateway no ambiente do cliente, cache local e armazenamento AWS |
| **O que você decide/configura?** | Modalidade de arquivos, volumes ou fitas e capacidade local |
| **Em que ordem as coisas acontecem?** | Aplicação usa protocolo compatível; gateway integra o armazenamento remoto |
| **O que pode fazer, e em que condição?** | Permite adoção híbrida mantendo interfaces familiares |
| **O que não pode presumir?** | Não é migração instantânea de toda aplicação; precisa host, cache e conectividade conforme modalidade |

**Caso comentado:** Sistema de backup usa interface de fita: Tape Gateway, em vez de reescrever o sistema para API S3.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Storage Gateway](https://docs.aws.amazon.com/storagegateway/)
