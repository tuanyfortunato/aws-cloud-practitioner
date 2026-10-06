<!-- autoral -->

# Amazon DynamoDB

> **Categoria:** Banco de dados NoSQL serverless · **Domínio:** 3 · **Abrangência:** Regional; tabelas globais em várias Regiões · **Ficha:** núcleo
>
> **Em uma frase:** banco NoSQL serverless, de chave-valor e documento, com respostas em milissegundos de um dígito em qualquer escala.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md) · base em [0.3 Dados: arquivo, bloco, objeto e banco de dados](../../docs/fundamentos/03-dados.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

O aplicativo novo da escola precisa guardar a sessão de milhões de acessos, cada uma buscada pela sua chave, sem cruzar tabela nenhuma. Num banco relacional, isso exigiria dimensionar servidores para o pico de janeiro e pagar por eles o ano todo.

O DynamoDB é um banco NoSQL serverless e totalmente gerenciado, nos modelos chave-valor e documento. Não há servidor para escolher: no modo sob demanda, a tabela escala sozinha, até zero quando não há tráfego, e você paga pelas leituras e gravações feitas. O desempenho é o mesmo com 10 usuários ou 100 milhões, no exemplo da própria AWS.

O limite: para escalar assim, o DynamoDB deixa de fora recursos que não escalam bem, como as junções (JOIN) entre tabelas. Os relatórios que cruzam alunos, turmas e notas ficam num banco relacional, como o [RDS](rds.md).

## Como funciona

1. Você cria uma **tabela** e define a **chave primária**, que identifica cada **item**.
2. A aplicação grava e lê itens pela chave; cada item tem atributos próprios, sem esquema fixo.
3. O DynamoDB replica os dados em três zonas de disponibilidade e escala a capacidade de acordo com o modo escolhido.
4. Recursos opcionais acrescentam réplicas em outras Regiões, backups contínuos e cache em memória.

## Opções principais

| Opção | O que faz | Quando lembrar |
|---|---|---|
| Modo sob demanda | Paga por requisição e escala sozinho | "Tráfego imprevisível", "não planejar capacidade" |
| Modo provisionado | Você define a capacidade de leitura e gravação por segundo | "Tráfego previsível", "controlar custo" |
| Tabelas globais | Replica a tabela em várias Regiões, com leitura e gravação local | "Usuários em vários continentes" |
| Recuperação a um ponto no tempo (PITR) | Backup contínuo, com restauração a qualquer segundo | "Desfazer uma gravação errada" |
| DynamoDB Accelerator (DAX) | Cache em memória que leva as leituras a microssegundos | "Microssegundos no DynamoDB" |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Latência típica | Milissegundos de um dígito | 06/10/2026 |
| Tamanho máximo de um item | 400 KB | 06/10/2026 |
| Janela da recuperação a um ponto no tempo | Até 35 dias | 06/10/2026 |
| Nível gratuito de armazenamento | 25 GB por mês, por Região | 06/10/2026 |

## Como é cobrado

No modo sob demanda, você paga por requisição de leitura e de gravação; no provisionado, pela capacidade reservada por hora. Somam-se o armazenamento, os backups, as réplicas de tabelas globais e a transferência de dados. O nível gratuito inclui 25 GB de armazenamento e 25 unidades de capacidade de leitura e de gravação por mês, por Região.

## Não confundir com

| Serviço | Diferença para o DynamoDB | Pista no enunciado |
|---|---|---|
| [Amazon RDS](rds.md) e [Amazon Aurora](aurora.md) | Relacionais, com SQL e junções | "Tabelas relacionadas", "transações com JOIN" |
| [Amazon ElastiCache](elasticache.md) | Cache em memória na frente de qualquer banco | "Aliviar o banco com cache" |
| [Amazon DocumentDB](documentdb.md) | Banco de documentos para aplicações feitas para o MongoDB | "MongoDB" |
| [Amazon S3](../armazenamento/s3.md) | Guarda arquivos inteiros como objetos, não itens consultados pela chave | "Fotos, vídeos, backups" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
- [Modos de capacidade](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html)
- [Limites de itens e atributos](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Constraints.html)
- [Recuperação a um ponto no tempo](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Point-in-time-recovery.html)
- [DynamoDB Accelerator (DAX)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html)
- [Preços do Amazon DynamoDB](https://aws.amazon.com/dynamodb/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
