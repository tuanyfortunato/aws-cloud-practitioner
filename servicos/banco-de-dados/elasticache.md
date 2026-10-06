# Amazon ElastiCache

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A aplicação consulta repetidamente dados parecidos e o banco principal demora mais do que o desejado.

**Como este serviço ajuda?** ElastiCache fornece armazenamento em memória para manter dados próximos da aplicação e acelerar acessos, conforme o mecanismo e a configuração.

**Exemplo do dia a dia:** Uma loja guarda temporariamente o resultado de uma consulta popular num cache. Nas próximas consultas, a aplicação pode usar esse resultado sem consultar o banco de novo.

**O que ele não resolve sozinho?** A aplicação precisa decidir quando atualizar ou invalidar o cache. Ele não acelera qualquer consulta automaticamente nem deve ser tratado sem planejamento como a única cópia de dados essenciais.

**Primeiras palavras para entender:**

- **Memória:** armazenamento de acesso rápido usado durante a execução.
- **Cache:** dados mantidos para reutilização.
- **Invalidar:** deixar de usar uma cópia desatualizada.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Cache em memória · **Domínio:** 3 · **Escopo:** Regional (nós em AZs) · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)
>
> **Em uma frase:** cache em memória gerenciado (Valkey, Redis OSS, Memcached) com latência de microssegundos.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **cache:** Cópia mantida para reutilização rápida. A aplicação ou o serviço precisa decidir atualização e validade, para não servir conteúdo inadequado ou antigo.

**Passo 1.** Identifique uma consulta ou dado que pode ser reutilizado e defina por quanto tempo a cópia serve.

**Passo 2.** Prepare um mecanismo compatível e faça a aplicação consultar e atualizar o cache conforme seu desenho.

**Passo 3.** Trate conteúdo desatualizado, falhas e expiração. Um cache acelera acesso, mas não define sozinho a verdade dos dados.

## 2. Recursos e opções, com significado

### Para que serve

**Antes de ler este trecho:**

- **latência:** Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.
- **carga:** Aplicação ou conjunto de tarefas com seus recursos e necessidades. Avaliar uma carga significa avaliar o trabalho completo, não uma única máquina isolada.
- **stateless:** Controle que avalia cada direção sem manter o mesmo estado de conexão. Regras de ida e de volta precisam ser consideradas separadamente.
- **pub/sub:** Publicação de uma mensagem para destinatários inscritos. Distribuir avisos a vários destinos é diferente de manter uma tarefa aguardando um consumidor.

Reduzir carga e latência do banco (cache de consultas), **armazenar sessões** (aplicação stateless), placares, filas simples, pub/sub, rate limiting.

### Motores

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **Multi-AZ:** Configuração que utiliza mais de uma zona de disponibilidade. Seu comportamento depende do serviço: não presuma que toda cópia atende leituras ou que isso é backup de dados apagados.
- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.
- **replicação:** Manutenção de uma cópia dos dados em outro recurso. Se uma alteração incorreta for replicada, a cópia também pode recebê-la; replicação não substitui todo backup.
- **failover:** Mudança do atendimento para um componente alternativo quando o principal fica indisponível. A forma e o tempo dependem da solução.
- **Redis / Redis OSS / Valkey / Memcached:** Tecnologias de dados em memória com comportamentos e funções diferentes. A modalidade gerenciada deve ser escolhida segundo compatibilidade e necessidade, não apenas pela palavra cache.

| Motor | Destaques |
|---|---|
| **Valkey** | Fork open source do Redis, recomendado pela AWS, mais barato. |
| **Redis OSS** | Estruturas de dados ricas, **replicação, Multi-AZ com failover, persistência/backup**, pub/sub. |
| **Memcached** | Simples, multithread, **sem persistência nem replicação**; escala horizontal por sharding. |

### Configurações

**Antes de ler este trecho:**

- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.

**Serverless** (sem planejar nós; paga por dados armazenados e ECPUs) ou **clusters de nós** (tipo de nó, shards, réplicas).

**Antes de ler este trecho:**

- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.
- **autenticação:** Verificação de quem está acessando. Confirmar a identidade não autoriza qualquer ação no sistema.
- **RBAC:** Controle de acesso baseado em papéis. As permissões dependem do papel atribuído à identidade e das regras do sistema.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.
- **AUTH:** Abreviação de autenticação ou autorização conforme a interface. Identificar um usuário e permitir uma ação são etapas distintas.

Criptografia em repouso e em trânsito, autenticação (RBAC/AUTH), backups (Valkey/Redis), *Global Datastore* (replicação entre regiões).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

A aplicação precisa decidir quando atualizar ou invalidar o cache. Ele não acelera qualquer consulta automaticamente nem deve ser tratado sem planejamento como a única cópia de dados essenciais.

### ⚠️ Pegadinhas e não confundir

**Antes de ler este trecho:**

- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **ElastiCache:** ElastiCache fornece armazenamento em memória para manter dados próximos da aplicação e acelerar acessos, conforme o mecanismo e a configuração.
- **MemoryDB:** MemoryDB oferece um banco em memória com mecanismos de durabilidade.
- **DAX:** Cache compatível com DynamoDB para determinados acessos. É uma camada de aceleração, não uma cópia independente de qualquer banco.

**ElastiCache** (cache, dados podem ser recriados) × **MemoryDB** (banco primário durável) × **DAX** (cache só do DynamoDB).

**Antes de ler este trecho:**

- **servidor:** Computador que atende pedidos de outros computadores. Um servidor web, por exemplo, responde aos pedidos enviados pelo navegador.

"Guardar sessão fora do servidor para escalar horizontalmente" → ElastiCache (ou DynamoDB).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

**Antes de ler este trecho:**

- **Savings Plans:** Compromisso de gasto por período em troca de condições de preço para uso elegível. Se a necessidade diminuir, o compromisso não desaparece automaticamente.

Por nó-hora (ou nós reservados) ou, no serverless, por GB-hora armazenado + ECPUs. 🔄 Coberto por Database Savings Plans.

## 5. Caso resolvido: ligando as peças

Uma loja guarda temporariamente o resultado de uma consulta popular num cache. Nas próximas consultas, a aplicação pode usar esse resultado sem consultar o banco de novo.

**Aplicando a sequência à situação:**

**Etapa 1:** Identifique uma consulta ou dado que pode ser reutilizado e defina por quanto tempo a cópia serve.
**Etapa 2:** Prepare um mecanismo compatível e faça a aplicação consultar e atualizar o cache conforme seu desenho.
**Etapa 3:** Trate conteúdo desatualizado, falhas e expiração. Um cache acelera acesso, mas não define sozinho a verdade dos dados.

**Resultado e responsabilidade:** ElastiCache fornece armazenamento em memória para manter dados próximos da aplicação e acelerar acessos, conforme o mecanismo e a configuração.

**Recursos envolvidos:** Cache, motores suportados, endpoints e política de expiração.

**Decisões que precisam ser tomadas:** Motor, capacidade, rede e estratégia de cache.

**Antes de ler este trecho:**

- **TTL:** Tempo de vida de uma informação. Em DNS pode orientar cache; em um banco pode indicar expiração de itens. O efeito concreto depende do serviço.

**Outra situação comentada:** Resultado muito consultado: cache com TTL; aplicação deve tratar expiração e indisponibilidade.

**Por que não concluir mais do que isso:** Não acelera automaticamente código que nunca usa o cache; não trate toda modalidade como armazenamento definitivo

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Reduzir a carga de leitura do RDS com cache em memória."

**Resposta curta:** ElastiCache.

**Pergunta:** "Armazenar sessões de usuário para aplicação stateless."

**Resposta curta:** ElastiCache.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
