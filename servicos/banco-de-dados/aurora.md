# Amazon Aurora

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma aplicação usa banco relacional e quer uma opção AWS compatível com MySQL ou PostgreSQL, com arquitetura própria para armazenamento e disponibilidade.

**Como este serviço ajuda?** Aurora é um banco relacional da AWS dentro da família RDS. Ele combina compatibilidade com esses mecanismos e uma arquitetura gerenciada com recursos próprios.

**Exemplo do dia a dia:** Uma loja que usa PostgreSQL avalia Aurora PostgreSQL para seu banco de pedidos, verificando a compatibilidade da aplicação e as necessidades de capacidade.

**O que ele não resolve sozinho?** Aurora não é compatível com todos os mecanismos disponíveis no RDS. Compatibilidade também não significa que toda extensão e configuração funcionará sem avaliação.

**Primeiras palavras para entender:**

- **Relacional:** dados em tabelas relacionadas.
- **Compatibilidade:** capacidade de usar interfaces e comportamentos esperados.
- **Réplica de leitura:** cópia usada para consultas.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Banco relacional nativo da AWS · **Domínio:** 3 · **Escopo:** Regional (cluster multi-AZ); Global Database multi-região · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)
>
> **Em uma frase:** banco relacional compatível com MySQL e PostgreSQL, com desempenho e disponibilidade de nível comercial a custo de open source.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Escolha a compatibilidade MySQL ou PostgreSQL e a modalidade que atende à aplicação.

**Passo 2.** Defina as instâncias ou opções de capacidade, os acessos e os pontos de conexão do conjunto.

**Passo 3.** Distribua leitura e escrita de forma compatível e planeje recuperação. Compatibilidade e arquitetura precisam ser avaliadas antes de migrar.

## 2. Recursos e opções, com significado

### Para que serve

OLTP que exige alto desempenho e alta disponibilidade gerenciada.

Migrações de Oracle/SQL Server para um motor open source compatível (com DMS + SCT).

### Arquitetura

| Item | Detalhe |
|---|---|
| **Compatibilidade** | **MySQL** e **PostgreSQL** (a AWS cita até 5x e 3x o desempenho do padrão). |
| **Armazenamento distribuído** | **6 cópias em 3 AZs**, cresce automaticamente (o volume é dividido em segmentos de 10 GiB); tolera perder 2 cópias para escrita e 3 para leitura; *self-healing*. |
| **Cluster** | 1 instância **writer** + até **15 Aurora Replicas** (leitura e failover, normalmente < 30 s). |
| **Endpoints** | *Cluster (writer) endpoint*, *reader endpoint* (balanceia leituras), endpoints customizados. |

### Configurações e opções importantes

**Aurora Serverless v2**

**Detalhe:** Capacidade em ACUs ajustada automaticamente em segundos, em incrementos de 0,5 ACU; ✔️ com *auto-pause* pode escalar até **0 ACU**.

**Aurora Global Database**

**Detalhe:** Replicação entre regiões com lag tipicamente < 1 s; região secundária pode ser promovida (DR) e servir leituras locais.

**Backtrack (MySQL)**

**Detalhe:** "Voltar no tempo" o cluster sem restaurar backup.

**Cloning**

**Detalhe:** Cópia rápida *copy-on-write* para testes.

**Configuração de storage**

**Detalhe:** *Standard* (paga por I/O) ou *I/O-Optimized* (sem cobrança por I/O, para cargas intensivas).

**Zero-ETL com Redshift**

**Detalhe:** Replicação quase em tempo real para análise.

**Aurora DSQL**

**Detalhe:** 🔄 Banco SQL distribuído, serverless, ativo-ativo multi-região (2025) — 🧊 fora da prova.

### Limites e números

📌 **6 cópias / 3 AZs**, **15 réplicas**.

🧊 Tamanho máximo do volume, limites de ACU.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Aurora não é compatível com todos os mecanismos disponíveis no RDS. Compatibilidade também não significa que toda extensão e configuração funcionará sem avaliação.

### ⚠️ Pegadinhas e não confundir

Aurora × RDS: Aurora é motor próprio da AWS (MySQL/PostgreSQL), mais rápido e resiliente; RDS oferece vários motores comerciais e open source.

"Relacional + máxima disponibilidade gerenciada + compatível com MySQL" → **Aurora**.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Instâncias (ou ACU-hora no Serverless), armazenamento GB-mês, I/O (configuração Standard), backup extra, transferência; replicação do Global Database.

### Segurança e responsabilidade compartilhada

Igual ao [RDS](rds.md): AWS cuida de infra, SO, patch, replicação de armazenamento; cliente de usuários, acesso de rede, criptografia, dados.

## 5. Caso resolvido: ligando as peças

Uma loja que usa PostgreSQL avalia Aurora PostgreSQL para seu banco de pedidos, verificando a compatibilidade da aplicação e as necessidades de capacidade.

**Aplicando a sequência à situação:**

**Etapa 1:** Escolha a compatibilidade MySQL ou PostgreSQL e a modalidade que atende à aplicação.
**Etapa 2:** Defina as instâncias ou opções de capacidade, os acessos e os pontos de conexão do conjunto.
**Etapa 3:** Distribua leitura e escrita de forma compatível e planeje recuperação. Compatibilidade e arquitetura precisam ser avaliadas antes de migrar.

**Resultado e responsabilidade:** Aurora é um banco relacional da AWS dentro da família RDS. Ele combina compatibilidade com esses mecanismos e uma arquitetura gerenciada com recursos próprios.

**Recursos envolvidos:** Cluster, writer, readers, endpoints e armazenamento compartilhado.

**Decisões que precisam ser tomadas:** Compatibilidade MySQL/PostgreSQL, capacidade e disponibilidade.

**Outra situação comentada:** Relacional compatível MySQL com leitores: Aurora; não confunda reader com writer.

**Por que não concluir mais do que isso:** Não é engine compatível com qualquer banco SQL; endpoints e opções dependem da configuração

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Banco relacional compatível com MySQL/PostgreSQL de maior desempenho."

**Resposta curta:** Aurora.

**Pergunta:** "Quantas cópias dos dados o Aurora mantém?"

**Resposta curta:** 6 cópias em 3 AZs.

**Pergunta:** "Banco relacional com leituras de baixa latência em várias regiões e DR."

**Resposta curta:** Aurora Global Database.

**Pergunta:** "Carga intermitente sem gerenciar capacidade."

**Resposta curta:** Aurora Serverless.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
