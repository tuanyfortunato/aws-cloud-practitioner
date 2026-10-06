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

## 1. A sequência de funcionamento

**Passo 1.** Descreva os registros e como a aplicação precisa buscá-los. Escolha as chaves a partir desses acessos.

**Passo 2.** Crie uma tabela com modalidade de capacidade e índices adequados. A aplicação grava e consulta itens pelas operações compatíveis.

**Passo 3.** Observe consumo e distribuição do acesso. Alterar o padrão de consulta pode exigir mudanças de modelagem, não apenas mais capacidade.

## 2. Recursos e opções, com significado

### Para que serve

Carrinhos de compra, perfis de usuário, sessões, jogos (placares), IoT, catálogos, aplicações serverless com tráfego imprevisível.

### Conceitos

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

**Detalhe:** **On-demand** (paga por requisição, sem planejamento) ou **Provisioned** (RCU/WCU + Auto Scaling; capacidade reservada para desconto).

**Table class**

**Detalhe:** Standard ou **Standard-IA** (armazenamento mais barato para tabelas pouco acessadas).

**Global Tables**

**Detalhe:** Replicação **multi-região ativa-ativa** (leitura e escrita em todas as regiões).

**DAX**

**Detalhe:** Cache em memória **exclusivo do DynamoDB**: leituras em **microssegundos**.

**Streams**

**Detalhe:** Fluxo ordenado de mudanças (24 h) para disparar Lambda, replicar, auditar.

**TTL**

**Detalhe:** Expira itens automaticamente (sem custo de escrita).

**Backups**

**Detalhe:** **PITR** com período configurável de **1 a 35 dias** (padrão 35, desde 01/2025), restauração ao segundo, e backups on-demand; integração com AWS Backup.

**Export/Import S3**

**Detalhe:** Exporta para análise (Athena) sem consumir capacidade.

**Zero-ETL**

**Detalhe:** Integrações com OpenSearch e Redshift.

**VPC gateway endpoint**

**Detalhe:** Acesso privado e gratuito a partir da VPC.

### Limites e números

📌 Item máximo **400 KB** → blobs grandes vão para o **S3** com referência na tabela.

🧊 RCU/WCU por tamanho de item, limites de partição.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele não é uma troca automática por um banco SQL com consultas relacionais arbitrárias. Você precisa modelar os dados e os padrões de acesso adequadamente.

### ⚠️ Pegadinhas e não confundir

DynamoDB × RDS: NoSQL sem joins, escala massiva × relacional com SQL.

**DAX** (cache só do DynamoDB) × **ElastiCache** (cache genérico).

"Multi-região ativa-ativa" → **Global Tables**.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

On-demand: por requisição de leitura/escrita. Provisioned: por RCU/WCU-hora. + armazenamento GB-mês, backups, Global Tables (escritas replicadas), DAX, Streams.

Free Tier "sempre gratuito" (planos Free e Paid): **25 GB** de armazenamento, **25 WCU e 25 RCU** provisionadas.

### Segurança e responsabilidade compartilhada

**AWS:** infraestrutura, SO, software, replicação em 3 AZs, escalonamento, patches.

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

**Outra situação comentada:** Sessão de usuário acessada pelo identificador: DynamoDB pode servir; consultas relacionais complexas apontam para outro modelo.

**Por que não concluir mais do que isso:** Não funciona como relacional com joins arbitrários; escolha de chave influencia distribuição e consultas

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Banco NoSQL serverless com latência de milissegundos."

**Resposta curta:** DynamoDB.

**Pergunta:** "Replicação multi-região ativa-ativa."

**Resposta curta:** Global Tables.

**Pergunta:** "Cache de microssegundos para DynamoDB."

**Resposta curta:** DAX.

**Pergunta:** "Tráfego imprevisível sem planejar capacidade."

**Resposta curta:** Modo on-demand.

**Pergunta:** "Apagar sessões expiradas automaticamente."

**Resposta curta:** TTL.

**Pergunta:** "Guardar vídeos e manter metadados no banco."

**Resposta curta:** Vídeo no S3, referência no DynamoDB.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
