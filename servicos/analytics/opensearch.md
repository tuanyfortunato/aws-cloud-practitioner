# Amazon OpenSearch Service

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A aplicação precisa encontrar textos e explorar registros rapidamente, com filtros e busca, em vez de abrir cada documento manualmente.

**Como este serviço ajuda?** OpenSearch oferece busca e análise de dados indexados. Você envia dados, define seu índice e usa consultas ou visualizações compatíveis.

**Exemplo do dia a dia:** Uma equipe envia logs da aplicação para procurar erros por palavra, horário e outros campos.

**O que ele não resolve sozinho?** O serviço não é um substituto universal de banco nem armazena automaticamente todos os logs da conta. Ingestão, índices e permissões precisam ser configurados.

**Primeiras palavras para entender:**

- **Índice:** estrutura organizada para busca.
- **Ingestão:** envio dos dados ao serviço.
- **Log:** registro de acontecimentos.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Analytics / busca e logs · **Domínio:** 3 · **Escopo:** Regional (VPC) · **Tópico do guia:** [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)
>
> **Em uma frase:** busca de texto, análise de logs e observabilidade com OpenSearch (sucessor do Elasticsearch gerenciado).
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **índice:** Estrutura adicional para apoiar consultas. Pode melhorar um padrão de acesso, mas possui condições de atualização, capacidade e custo.


**Passo 1.** Prepare dados e defina como eles serão indexados para busca.

**Passo 2.** Envie registros e consulte palavras, campos ou relações compatíveis com o índice.

**Passo 3.** Acompanhe atualização, armazenamento e acesso. A ferramenta só busca no conteúdo efetivamente disponibilizado ao ambiente.

## 2. Recursos e opções, com significado

### Destaques

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.
- **IA:** Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.
- **Multi-AZ:** Configuração que utiliza mais de uma zona de disponibilidade. Seu comportamento depende do serviço: não presuma que toda cópia atende leituras ou que isso é backup de dados apagados.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **RAG:** Recuperar informações de uma fonte e usá-las como contexto de geração. Isso não elimina erros nem autoriza acesso a todos os documentos.
- **SIEM:** Ferramentas e processos para reunir e analisar informações de segurança. A qualidade depende das fontes, regras e investigação.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Item | Detalhe |
|---|---|
| **Domínios gerenciados** | Clusters com nós de dados, nós master dedicados, Multi-AZ, camadas UltraWarm/cold. |
| **OpenSearch Serverless** | Coleções sem gerenciar clusters (busca, séries temporais, **vetores**). |
| **OpenSearch Dashboards** | Visualização (equivalente ao Kibana). |
| **Ingestão** | Data Firehose, OpenSearch Ingestion, CloudWatch Logs, zero-ETL com S3/DynamoDB. |
| **Usos** | Busca de produtos em e-commerce, análise de logs (SIEM), monitoramento de aplicações, **busca vetorial** para IA generativa (RAG). |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

O serviço não é um substituto universal de banco nem armazena automaticamente todos os logs da conta. Ingestão, índices e permissões precisam ser configurados.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

## 5. Caso resolvido: ligando as peças

Uma equipe envia logs da aplicação para procurar erros por palavra, horário e outros campos.

**Aplicando a sequência à situação:**

**Etapa 1:** Prepare dados e defina como eles serão indexados para busca.
**Etapa 2:** Envie registros e consulte palavras, campos ou relações compatíveis com o índice.
**Etapa 3:** Acompanhe atualização, armazenamento e acesso. A ferramenta só busca no conteúdo efetivamente disponibilizado ao ambiente.

**Resultado e responsabilidade:** OpenSearch oferece busca e análise de dados indexados. Você envia dados, define seu índice e usa consultas ou visualizações compatíveis.

**Recursos envolvidos:** Índices, documentos e domínios/collections conforme modalidade.

**Decisões que precisam ser tomadas:** Ingestão, indexação, capacidade e acesso.


**Outra situação comentada:** Busca por texto em catálogo: OpenSearch; transações de compra: banco apropriado.

**Por que não concluir mais do que isso:** Não substitui automaticamente sistema transacional de registros

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

A aplicação precisa encontrar textos e explorar registros rapidamente, com filtros e busca, em vez de abrir cada documento manualmente.

**2. O que a solução fornece?**

OpenSearch oferece busca e análise de dados indexados. Você envia dados, define seu índice e usa consultas ou visualizações compatíveis.

**3. Que conclusão seria incorreta?**

O serviço não é um substituto universal de banco nem armazena automaticamente todos os logs da conta. Ingestão, índices e permissões precisam ser configurados.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Busca de texto completo no catálogo de produtos."

**Resposta curta:** OpenSearch Service.

**Antes de ler este trecho:**

- **OpenSearch Service:** OpenSearch oferece busca e análise de dados indexados.


**Fundamento explicado no capítulo:** "Busca de texto completo no catálogo de produtos." → OpenSearch Service.

**Pergunta:** "Analisar e visualizar logs em tempo quase real."

**Resposta curta:** OpenSearch (+ Dashboards).


**Fundamento explicado no capítulo:** "Analisar e visualizar logs em tempo quase real." → OpenSearch (+ Dashboards).


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
