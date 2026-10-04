# Amazon DynamoDB

> **Categoria:** Banco NoSQL serverless · **Domínio:** 3 · **Escopo:** Regional (multi-AZ automático); Global Tables multi-região · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)
>
> **Em uma frase:** banco chave-valor e de documentos, serverless, com latência de milissegundos de um dígito em qualquer escala.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Para que serve

- Carrinhos de compra, perfis de usuário, sessões, jogos (placares), IoT, catálogos, aplicações serverless com tráfego imprevisível.

## Conceitos

| Item | Detalhe |
|---|---|
| **Tabela / item / atributo** | Sem schema fixo (exceto a chave). Item até **400 KB**. |
| **Chave primária** | **Partition key** (simples) ou **partition key + sort key** (composta). |
| **Índices** | **GSI** (outra chave, criado a qualquer momento) e **LSI** (mesma partition key, sort key diferente, só na criação). |
| **Leituras** | *Eventually consistent* (padrão, metade do custo) ou *strongly consistent*. |
| **Transações** | ACID entre vários itens/tabelas. |
| **Criptografia** | **Sempre ativa** em repouso (chave AWS owned, AWS managed ou customer managed). |

## Configurações e opções importantes

| Opção | Detalhe |
|---|---|
| **Modo de capacidade** | **On-demand** (paga por requisição, sem planejamento) ou **Provisioned** (RCU/WCU + Auto Scaling; capacidade reservada para desconto). |
| **Table class** | Standard ou **Standard-IA** (armazenamento mais barato para tabelas pouco acessadas). |
| **Global Tables** | Replicação **multi-região ativa-ativa** (leitura e escrita em todas as regiões). |
| **DAX** | Cache em memória **exclusivo do DynamoDB**: leituras em **microssegundos**. |
| **Streams** | Fluxo ordenado de mudanças (24 h) para disparar Lambda, replicar, auditar. |
| **TTL** | Expira itens automaticamente (sem custo de escrita). |
| **Backups** | **PITR** com período configurável de **1 a 35 dias** (padrão 35, desde 01/2025), restauração ao segundo, e backups on-demand; integração com AWS Backup. |
| **Export/Import S3** | Exporta para análise (Athena) sem consumir capacidade. |
| **Zero-ETL** | Integrações com OpenSearch e Redshift. |
| **VPC gateway endpoint** | Acesso privado e gratuito a partir da VPC. |

## Limites e números

- 📌 Item máximo **400 KB** → blobs grandes vão para o **S3** com referência na tabela.
- 🧊 RCU/WCU por tamanho de item, limites de partição.

## Cobrança

- On-demand: por requisição de leitura/escrita. Provisioned: por RCU/WCU-hora. + armazenamento GB-mês, backups, Global Tables (escritas replicadas), DAX, Streams.
- Free Tier "sempre gratuito" (planos Free e Paid): **25 GB** de armazenamento, **25 WCU e 25 RCU** provisionadas.

## Segurança e responsabilidade compartilhada

- **AWS:** infraestrutura, SO, software, replicação em 3 AZs, escalonamento, patches.
- **Cliente:** acesso via **IAM** (políticas por tabela/item), escolha da chave KMS, modelagem dos dados, backups/PITR ativados.

## ⚠️ Pegadinhas e não confundir

- DynamoDB × RDS: NoSQL sem joins, escala massiva × relacional com SQL.
- **DAX** (cache só do DynamoDB) × **ElastiCache** (cache genérico).
- "Multi-região ativa-ativa" → **Global Tables**.

## ❓ Perguntas típicas

- "Banco NoSQL serverless com latência de milissegundos." → DynamoDB.
- "Replicação multi-região ativa-ativa." → Global Tables.
- "Cache de microssegundos para DynamoDB." → DAX.
- "Tráfego imprevisível sem planejar capacidade." → Modo on-demand.
- "Apagar sessões expiradas automaticamente." → TTL.
- "Guardar vídeos e manter metadados no banco." → Vídeo no S3, referência no DynamoDB.

## 🔗 Documentação oficial

- [Guia do DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
