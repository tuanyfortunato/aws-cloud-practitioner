# Amazon FSx

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma aplicação precisa de arquivos compartilhados, mas depende de características de um sistema de arquivos específico, como o usado em ambientes Windows.

**Como este serviço ajuda?** O FSx oferece sistemas de arquivos gerenciados em modalidades diferentes. A escolha depende da compatibilidade e das funções de que sua aplicação precisa.

**Exemplo do dia a dia:** Uma empresa com aplicações Windows pode avaliar FSx for Windows File Server para compartilhar arquivos com as características esperadas por esse ambiente.

**O que ele não resolve sozinho?** FSx é uma família; uma modalidade não oferece automaticamente as funções de todas as outras. Confira compatibilidade, disponibilidade e escopo de cada opção.

**Primeiras palavras para entender:**

- **SMB:** protocolo comum para compartilhamento de arquivos Windows.
- **Sistema de arquivos:** forma de organizar e acessar arquivos.
- **Modalidade:** variante do serviço.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Armazenamento de arquivos gerenciado · **Domínio:** 3 · **Escopo:** Regional (Single-AZ ou Multi-AZ) · **Tópico do guia:** [3.9 Outros serviços de armazenamento](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md)
>
> **Em uma frase:** sistemas de arquivos populares de terceiros (Windows, Lustre, NetApp ONTAP, OpenZFS) totalmente gerenciados.
>
> **Escopo oficial:** 🔀 FSx ✅ · FSx for Lustre ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.


**Passo 1.** Identifique o sistema de arquivos que a aplicação espera e escolha a modalidade correspondente.

**Passo 2.** Prepare identidade, conexão e armazenamento. Os clientes compatíveis acessam os arquivos por sua interface prevista.

**Passo 3.** Planeje disponibilidade, cópias e capacidade. Cada modalidade tem seus próprios recursos e limites.

## 2. Recursos e opções, com significado

### Os quatro sabores

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **FSx:** O FSx oferece sistemas de arquivos gerenciados em modalidades diferentes.
- **IOPS:** Quantidade de operações de leitura e escrita por segundo. Ajuda a descrever o comportamento de um armazenamento, mas não mede sozinha a quantidade de bytes transferidos.
- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.
- **HPC:** Computação de alto desempenho: execução de cálculos intensivos, como simulações. O requisito concreto pode envolver processamento, comunicação ou outro recurso.
- **GB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.
- **Multi-AZ:** Configuração que utiliza mais de uma zona de disponibilidade. Seu comportamento depende do serviço: não presuma que toda cópia atende leituras ou que isso é backup de dados apagados.
- **NFS / SMB / POSIX:** NFS e SMB são protocolos para acesso a arquivos compartilhados. POSIX descreve interfaces e comportamentos de sistemas. Compatibilidade importa para a aplicação usar os arquivos corretamente.
- **iSCSI:** Protocolo para apresentar armazenamento em blocos pela rede. É diferente de acessar objetos por uma API ou arquivos por um compartilhamento.
- **Active Directory:** Tecnologia de diretório para identidades, computadores e controles corporativos. É diferente do cadastro de clientes de uma aplicação pública.
- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.
- **deduplicação:** Identificação e tratamento de entradas repetidas conforme um critério e uma janela. É diferente de garantir toda a execução da aplicação apenas uma vez.
- **ML:** Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.
- **bucket:** Recipiente que organiza objetos no S3. A aplicação usa o bucket e a identificação do objeto para pedir operações autorizadas.
- **ONTAP:** Tecnologia de armazenamento e gerenciamento de arquivos associada a uma modalidade FSx. A aplicação precisa da compatibilidade e dos recursos daquela modalidade.
- **NAS:** Armazenamento acessível pela rede como arquivos. É diferente de apresentar um disco em blocos ou objetos por API.
- **NTFS / ZFS:** Tecnologias de sistemas de arquivos com capacidades próprias. A modalidade FSx ou outro ambiente precisa da compatibilidade exigida pela aplicação.
- **DFS:** Tecnologia de organização de arquivos distribuídos em cenários compatíveis. O contexto define como nomes e destinos são apresentados aos clientes.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Sabor | Protocolos | Destaques | Uso típico |
|---|---|---|---|
| **FSx for Windows File Server** | **SMB** | Integra com **Active Directory**, ACLs NTFS, DFS, shadow copies, deduplicação; Single-AZ ou Multi-AZ | Compartilhamentos Windows, SharePoint, SQL Server, home folders |
| **FSx for Lustre** ❌ *fora do escopo* | Lustre (POSIX) | **Alto desempenho** (centenas de GB/s, milhões de IOPS); **integração com S3** (lê/grava dados do bucket); *scratch* (temporário) ou *persistent* | HPC, ML, renderização, simulações |
| **FSx for NetApp ONTAP** | **NFS, SMB e iSCSI** | Recursos ONTAP (snapshots, SnapMirror, FlexClone, deduplicação, tiering) | Migrar NAS NetApp existente; multiprotocolo |
| **FSx for OpenZFS** | NFS | Snapshots e clones instantâneos ZFS, baixa latência | Migrar storage ZFS/Linux |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

FSx é uma família; uma modalidade não oferece automaticamente as funções de todas as outras. Confira compatibilidade, disponibilidade e escopo de cada opção.

### ⚠️ Pegadinhas e não confundir

**Antes de ler este trecho:**

- **EFS:** O EFS oferece um sistema de arquivos compartilhado.


"Windows + SMB + Active Directory" → **FSx for Windows** (não EFS).


"HPC/ML com dados no S3" → **FSx for Lustre**.


"Já usa NetApp" → **FSx for ONTAP**.

**Antes de ler este trecho:**

- **Storage Gateway:** Storage Gateway faz a ligação entre o ambiente local e o armazenamento em nuvem usando interfaces de arquivos, volumes ou fitas, conforme a modalidade.
- **datacenter:** Instalação física com equipamentos de computação, rede, energia e refrigeração. A nuvem continua dependendo desses equipamentos, mas o cliente não precisa manter o prédio.


Acesso local de baixa latência ao FSx for Windows a partir do datacenter → **FSx File Gateway** ([Storage Gateway](storage-gateway.md)).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **throughput:** Quantidade de dados ou de trabalho processada por unidade de tempo. É diferente de latência, que mede quanto uma operação demora.
- **SSD:** Tipo de armazenamento sem partes mecânicas, usado para acesso rápido a dados. A escolha de um volume também envolve sua capacidade e limites de desempenho.


Por capacidade de armazenamento provisionada, throughput (e SSD IOPS em alguns sabores) e backups.

### Segurança e responsabilidade compartilhada

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **failover:** Mudança do atendimento para um componente alternativo quando o principal fica indisponível. A forma e o tempo dependem da solução.


**AWS:** hardware, software do sistema de arquivos, patches, failover (Multi-AZ).

**Antes de ler este trecho:**

- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.


**Cliente:** acesso (AD, SGs, permissões), criptografia, backup e dados.

## 5. Caso resolvido: ligando as peças

Uma empresa com aplicações Windows pode avaliar FSx for Windows File Server para compartilhar arquivos com as características esperadas por esse ambiente.

**Aplicando a sequência à situação:**

**Etapa 1:** Identifique o sistema de arquivos que a aplicação espera e escolha a modalidade correspondente.
**Etapa 2:** Prepare identidade, conexão e armazenamento. Os clientes compatíveis acessam os arquivos por sua interface prevista.
**Etapa 3:** Planeje disponibilidade, cópias e capacidade. Cada modalidade tem seus próprios recursos e limites.

**Resultado e responsabilidade:** O FSx oferece sistemas de arquivos gerenciados em modalidades diferentes. A escolha depende da compatibilidade e das funções de que sua aplicação precisa.

**Recursos envolvidos:** Famílias de sistemas de arquivos gerenciados e endpoints.

**Decisões que precisam ser tomadas:** Família, protocolo, capacidade e opções de disponibilidade.


**Outra situação comentada:** Aplicação Windows exige SMB e integração AD: avalie FSx for Windows File Server.

**Por que não concluir mais do que isso:** Cada família tem capacidades distintas; FSx for Lustre está explicitamente fora do escopo consultado

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Uma aplicação precisa de arquivos compartilhados, mas depende de características de um sistema de arquivos específico, como o usado em ambientes Windows.

**2. O que a solução fornece?**

O FSx oferece sistemas de arquivos gerenciados em modalidades diferentes. A escolha depende da compatibilidade e das funções de que sua aplicação precisa.

**3. Que conclusão seria incorreta?**

FSx é uma família; uma modalidade não oferece automaticamente as funções de todas as outras. Confira compatibilidade, disponibilidade e escopo de cada opção.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Compartilhamento de arquivos Windows integrado ao AD."

**Resposta curta:** FSx for Windows File Server.


**Fundamento explicado no capítulo:** "Compartilhamento de arquivos Windows integrado ao AD." → FSx for Windows File Server.

**Pergunta:** "Sistema de arquivos de alto desempenho para HPC."

**Resposta curta:** FSx for Lustre.


**Fundamento explicado no capítulo:** "Sistema de arquivos de alto desempenho para HPC." → FSx for Lustre.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Amazon FSx](https://aws.amazon.com/fsx/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
