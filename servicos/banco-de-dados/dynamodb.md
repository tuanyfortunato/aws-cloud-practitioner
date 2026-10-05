# Amazon DynamoDB

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma aplicação precisa buscar e atualizar muitos registros por identificadores conhecidos, sem administrar servidores de banco.

**Como este serviço ajuda?** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens. Ele é especialmente associado a modelos chave-valor e documentos; o desenho das chaves deve acompanhar a forma de consultar.

**Exemplo do dia a dia:** Um jogo guarda o perfil de cada jogador com seu identificador. A aplicação usa esse identificador para buscar e atualizar o perfil no DynamoDB.

**O que ele não resolve sozinho?** Ele não é uma troca automática por um banco SQL com consultas relacionais arbitrárias. Você precisa modelar os dados e os padrões de acesso adequadamente.

**Primeiras palavras para entender:**

- **Item:** um registro.
- **Chave:** identificação usada para localizar ou organizar itens.
- **NoSQL:** família de bancos que não segue apenas o modelo de tabelas relacionais.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Banco NoSQL serverless · **Domínio:** 3 · **Escopo:** Regional (multi-AZ automático); Global Tables multi-região · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)
>
> **Em uma frase:** banco chave-valor e de documentos, serverless, com latência de milissegundos de um dígito em qualquer escala.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.


**Passo 1.** Descreva os registros e como a aplicação precisa buscá-los. Escolha as chaves a partir desses acessos.

**Passo 2.** Crie uma tabela com modalidade de capacidade e índices adequados. A aplicação grava e consulta itens pelas operações compatíveis.

**Passo 3.** Observe consumo e distribuição do acesso. Alterar o padrão de consulta pode exigir mudanças de modelagem, não apenas mais capacidade.

## 2. Recursos e opções, com significado

### Para que serve

**Antes de ler este trecho:**

- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **IoT:** Dispositivos físicos conectados que enviam informações ou recebem comandos. Conexão não substitui autenticação, software e análise dos dados.
- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.


Carrinhos de compra, perfis de usuário, sessões, jogos (placares), IoT, catálogos, aplicações serverless com tráfego imprevisível.

### Conceitos

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **KB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.
- **schema:** Estrutura e tipos dos dados. Em migração, adaptar a estrutura é uma tarefa diferente de copiar os registros.
- **chave primária:** Informação que identifica um registro conforme o modelo do banco. O desenho da chave afeta como os dados serão buscados.
- **partition key / sort key:** Chaves de organização dos itens do DynamoDB: a primeira determina agrupamento e distribuição; a segunda, quando usada, ordena itens no grupo.
- **chave:** Pode indicar identificação de um registro, identificação de um objeto ou elemento criptográfico. Leia o contexto: localizar um dado e protegê-lo são tarefas diferentes.
- **atributo:** Informação nomeada dentro de um registro, como nome ou data. Consultas usam os campos conforme a estrutura e o modelo do banco.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.
- **ACID:** Garantias de transações: atomicidade, consistência, isolamento e durabilidade. Descrevem comportamentos de operações do banco, não uma função de autenticação.
- **GSI / LSI:** Índices secundários globais e locais do DynamoDB. Oferecem padrões de consulta adicionais com condições e limites diferentes.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Item | Detalhe |
|---|---|
| **Tabela / item / atributo** | Sem schema fixo (exceto a chave). Item até **400 KB**. |
| **Chave primária** | **Partition key** (simples) ou **partition key + sort key** (composta). |
| **Índices** | **GSI** (outra chave, criado a qualquer momento) e **LSI** (mesma partition key, sort key diferente, só na criação). |
| **Leituras** | *Eventually consistent* (padrão, metade do custo) ou *strongly consistent*. |
| **Transações** | ACID entre vários itens/tabelas. |
| **Criptografia** | **Sempre ativa** em repouso (chave AWS owned, AWS managed ou customer managed). |

### Configurações e opções importantes

**Modo de capacidade**

**Antes de ler este trecho:**

- **RCU / WCU:** Capacidade provisionada de escrita e leitura no DynamoDB. Tamanho do item e condições da operação influenciam consumo; unidades não equivalem diretamente a usuários.
- **On-Demand:** Modalidade de uso sem o compromisso de longo prazo descrito por reservas e planos. Cobrança e unidades dependem do recurso contratado.


**Detalhe:** **On-demand** (paga por requisição, sem planejamento) ou **Provisioned** (RCU/WCU + Auto Scaling; capacidade reservada para desconto).

**Table class**


**Detalhe:** Standard ou **Standard-IA** (armazenamento mais barato para tabelas pouco acessadas).

**Global Tables**

**Antes de ler este trecho:**

- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.
- **replicação:** Manutenção de uma cópia dos dados em outro recurso. Se uma alteração incorreta for replicada, a cópia também pode recebê-la; replicação não substitui todo backup.


**Detalhe:** Replicação **multi-região ativa-ativa** (leitura e escrita em todas as regiões).

**DAX**

**Antes de ler este trecho:**

- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **memória:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.
- **cache:** Cópia mantida para reutilização rápida. A aplicação ou o serviço precisa decidir atualização e validade, para não servir conteúdo inadequado ou antigo.
- **DAX:** Cache compatível com DynamoDB para determinados acessos. É uma camada de aceleração, não uma cópia independente de qualquer banco.


**Detalhe:** Cache em memória **exclusivo do DynamoDB**: leituras em **microssegundos**.

**Streams**

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.


**Detalhe:** Fluxo ordenado de mudanças (24 h) para disparar Lambda, replicar, auditar.

**TTL**

**Antes de ler este trecho:**

- **TTL:** Tempo de vida de uma informação. Em DNS pode orientar cache; em um banco pode indicar expiração de itens. O efeito concreto depende do serviço.


**Detalhe:** Expira itens automaticamente (sem custo de escrita).

**Backups**

**Antes de ler este trecho:**

- **AWS Backup:** AWS Backup centraliza políticas e operações de backup para recursos compatíveis.
- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.
- **segundo:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.
- **PITR:** Recuperação para um ponto no tempo conforme o serviço e a janela configurada. É diferente de manter continuamente uma aplicação alternativa atendendo.


**Detalhe:** **PITR** com período configurável de **1 a 35 dias** (padrão 35, desde 01/2025), restauração ao segundo, e backups on-demand; integração com AWS Backup.

**Export/Import S3**

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **Athena:** Athena permite consultar dados em formatos e fontes compatíveis usando SQL.


**Detalhe:** Exporta para análise (Athena) sem consumir capacidade.

**Zero-ETL**

**Antes de ler este trecho:**

- **Redshift:** Redshift é um ambiente de banco voltado à análise de dados, conhecido como data warehouse.


**Detalhe:** Integrações com OpenSearch e Redshift.

**VPC gateway endpoint**

**Antes de ler este trecho:**

- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **endpoint:** Ponto de acesso a um serviço ou componente. Pode ser um endereço de API ou um recurso de conectividade; identifique qual sentido a seção usa.


**Detalhe:** Acesso privado e gratuito a partir da VPC.

### Limites e números

📌 Item máximo **400 KB** → blobs grandes vão para o **S3** com referência na tabela.


🧊 RCU/WCU por tamanho de item, limites de partição.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

**Antes de ler este trecho:**

- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.


Ele não é uma troca automática por um banco SQL com consultas relacionais arbitrárias. Você precisa modelar os dados e os padrões de acesso adequadamente.

### ⚠️ Pegadinhas e não confundir

**Antes de ler este trecho:**

- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **NoSQL:** Família de modelos de banco que não se limita à estrutura relacional tradicional. Não significa ausência de estrutura ou que todo produto NoSQL faz o mesmo trabalho.


DynamoDB × RDS: NoSQL sem joins, escala massiva × relacional com SQL.

**Antes de ler este trecho:**

- **ElastiCache:** ElastiCache fornece armazenamento em memória para manter dados próximos da aplicação e acelerar acessos, conforme o mecanismo e a configuração.


**DAX** (cache só do DynamoDB) × **ElastiCache** (cache genérico).


"Multi-região ativa-ativa" → **Global Tables**.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

On-demand: por requisição de leitura/escrita. Provisioned: por RCU/WCU-hora. + armazenamento GB-mês, backups, Global Tables (escritas replicadas), DAX, Streams.


Free Tier "sempre gratuito" (planos Free e Paid): **25 GB** de armazenamento, **25 WCU e 25 RCU** provisionadas.

### Segurança e responsabilidade compartilhada

**Antes de ler este trecho:**

- **SO:** Software básico da máquina, como Linux ou Windows. Ele administra arquivos, memória e execução de programas; atualizar esse software é diferente de atualizar a aplicação.


**AWS:** infraestrutura, SO, software, replicação em 3 AZs, escalonamento, patches.

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **KMS:** Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.


**Cliente:** acesso via **IAM** (políticas por tabela/item), escolha da chave KMS, modelagem dos dados, backups/PITR ativados.

## 5. Caso resolvido: ligando as peças

Um jogo guarda o perfil de cada jogador com seu identificador. A aplicação usa esse identificador para buscar e atualizar o perfil no DynamoDB.

**Aplicando a sequência à situação:**

**Etapa 1:** Descreva os registros e como a aplicação precisa buscá-los. Escolha as chaves a partir desses acessos.
**Etapa 2:** Crie uma tabela com modalidade de capacidade e índices adequados. A aplicação grava e consulta itens pelas operações compatíveis.
**Etapa 3:** Observe consumo e distribuição do acesso. Alterar o padrão de consulta pode exigir mudanças de modelagem, não apenas mais capacidade.

**Resultado e responsabilidade:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens. Ele é especialmente associado a modelos chave-valor e documentos; o desenho das chaves deve acompanhar a forma de consultar.

**Recursos envolvidos:** Tabelas, itens, atributos, partition key, sort key opcional e índices.

**Decisões que precisam ser tomadas:** Chave, modo de capacidade, backups, streams e replicação.

**Antes de ler este trecho:**

- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.


**Outra situação comentada:** Sessão de usuário acessada pelo identificador: DynamoDB pode servir; consultas relacionais complexas apontam para outro modelo.

**Por que não concluir mais do que isso:** Não funciona como relacional com joins arbitrários; escolha de chave influencia distribuição e consultas

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Uma aplicação precisa buscar e atualizar muitos registros por identificadores conhecidos, sem administrar servidores de banco.

**2. O que a solução fornece?**

DynamoDB é um banco gerenciado que organiza dados em tabelas de itens. Ele é especialmente associado a modelos chave-valor e documentos; o desenho das chaves deve acompanhar a forma de consultar.

**3. Que conclusão seria incorreta?**

Ele não é uma troca automática por um banco SQL com consultas relacionais arbitrárias. Você precisa modelar os dados e os padrões de acesso adequadamente.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Banco NoSQL serverless com latência de milissegundos."

**Resposta curta:** DynamoDB.

**Antes de ler este trecho:**

- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.


**Fundamento explicado no capítulo:** "Banco NoSQL serverless com latência de milissegundos." → DynamoDB.

**Pergunta:** "Replicação multi-região ativa-ativa."

**Resposta curta:** Global Tables.


**Fundamento explicado no capítulo:** "Replicação multi-região ativa-ativa." → Global Tables.

**Pergunta:** "Cache de microssegundos para DynamoDB."

**Resposta curta:** DAX.


**Fundamento explicado no capítulo:** "Cache de microssegundos para DynamoDB." → DAX.

**Pergunta:** "Tráfego imprevisível sem planejar capacidade."

**Resposta curta:** Modo on-demand.


**Fundamento explicado no capítulo:** "Tráfego imprevisível sem planejar capacidade." → Modo on-demand.

**Pergunta:** "Apagar sessões expiradas automaticamente."

**Resposta curta:** TTL.


**Fundamento explicado no capítulo:** "Apagar sessões expiradas automaticamente." → TTL.

**Pergunta:** "Guardar vídeos e manter metadados no banco."

**Resposta curta:** Vídeo no S3, referência no DynamoDB.

**Antes de ler este trecho:**

- **metadados:** Informações que descrevem outros dados, como características de um objeto. Conhecer a descrição não significa ler todo o conteúdo.


**Fundamento explicado no capítulo:** "Guardar vídeos e manter metadados no banco." → Vídeo no S3, referência no DynamoDB.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
