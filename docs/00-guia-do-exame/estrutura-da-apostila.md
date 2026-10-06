# Como esta apostila ensina: do problema à decisão

<!-- didatico:inicio -->
## 🧭 Antes de ler

**Por que esta página existe?** Uma lista de nomes e valores ajuda na revisão, mas não ensina sozinha quem começa do zero.

**Como usar?** Esta página apresenta a sequência dos capítulos e o motivo de cada parte. Use-a para ler o material ou manter novas aulas no mesmo padrão.

**Exemplo:** Ao estudar uma fila, entenda primeiro quem envia e quem executa o trabalho. Só depois compare ordenação, conservação e repetição de mensagens.
<!-- didatico:fim -->

## Público e objetivo

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.

O material é dirigido a quem está começando em tecnologia e em AWS. Não exige conhecer o console para compreender os fundamentos. Ele prepara a leitura e a decisão no nível da Cloud Practitioner; não substitui a documentação de implementação de todos os recursos.

Uma apostila deve construir entendimento antes de pedir memorização. A estrutura abaixo é uma escolha editorial para esse público, não uma norma universal para todo livro técnico.

## 1. Comece por uma dificuldade real

Mostre o que a pessoa precisa realizar. ‘Gerar certificados sem deixar o site esperando’ dá sentido a uma fila; dizer apenas ‘serviço de mensageria’ não apresenta o problema ao iniciante.

**Antes de ler este trecho:**

- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.

Explique o que a solução entrega e o que permanece com o cliente. O leitor deve distinguir contratar uma capacidade de receber um programa pronto.

## 2. Explique as peças antes de combiná-las

**Antes de ler este trecho:**

- **servidor:** Computador que atende pedidos de outros computadores. Um servidor web, por exemplo, responde aos pedidos enviados pelo navegador.
- **memória:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.
- **protocolo:** Conjunto de regras da comunicação. Um protocolo define o formato e o comportamento da troca; produtos precisam ser compatíveis com ele.

Defina termos onde eles serão usados. Servidor, memória, armazenamento, protocolo e permissão são conceitos de base, não conhecimentos que todo leitor já possui.

**Antes de ler este trecho:**

- **root:** Na conta AWS, é a identidade principal com poderes especiais. Dentro de Linux, root é o administrador do sistema operacional. Administrar Linux não é o mesmo que administrar a conta AWS.

Uma mesma palavra pode ter sentidos diferentes: root da conta AWS não é o administrador Linux de uma máquina; RAM de memória não é o nome do Resource Access Manager. O contexto precisa tornar isso claro.

## 3. Mostre a sequência

Descreva preparação, uso e resultado. Identifique quem envia a entrada, quem executa o trabalho, onde o resultado fica e o que acontece com falhas. Uma lista de componentes não mostra sozinha essa relação.

A sequência é conceitual. Não é necessário listar todos os botões da tela para explicar o funcionamento.

## 4. Explique opções e consequências

**Antes de ler este trecho:**

- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.

Apresente cada recurso com significado e condições. Só depois use uma tabela para comparar alternativas pelo mesmo critério. Capacidade, disponibilidade, duração, acesso e preço são critérios diferentes.

**Antes de ler este trecho:**

- **segundo:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.
- **retenção:** Tempo durante o qual dados ou registros são conservados. Depois desse prazo, o comportamento depende das regras do serviço e das configurações.

Em números, indique a unidade e o que ela mede. Um limite por mensagem não é limite de mensagens por segundo; retenção não é tempo de invisibilidade.

## 5. Resolva uma situação completa

Ligue a necessidade aos recursos e às decisões. Explique por que a alternativa serve e por que uma opção parecida atenderia outro problema. Inclua o trabalho que ainda precisa ser realizado e uma consequência de falha ou encerramento.

Os exemplos desta apostila são autorais. Não representam questões oficiais nem garantem previsão da prova.

## 6. Revise com explicação

Peça ao leitor que descreva a função, acompanhe a sequência e reconheça um limite. Disponibilize o raciocínio, além da resposta curta. Depois use as perguntas típicas para recuperar o conteúdo aprendido.

Se o leitor sabe apenas associar duas siglas, ele ainda precisa voltar à relação entre as peças. Se explica a escolha e identifica uma condição que mudaria a resposta, demonstrou um entendimento mais útil.

## Como ler um capítulo

Leia a abertura, siga a sequência e examine os conceitos. Use o caso resolvido como ligação entre eles. Faça a revisão sem olhar o comentário e retorne à parte em que faltou explicação.

**Antes de ler este trecho:**

- **implantação:** Colocar uma versão ou conjunto de recursos em funcionamento. O resultado precisa ser observado e, quando necessário, revertido de modo planejado.

As referências oficiais ficam ao final para verificar alterações, compatibilidade e detalhes de implantação. O vocabulário necessário aos fundamentos aparece no próprio capítulo.

## Referências de escrita técnica

[Conhecer o público](https://developers.google.com/tech-writing/one/audience)

[Definir termos](https://developers.google.com/tech-writing/one/words)

[Organizar documentos longos](https://developers.google.com/tech-writing/two/large-docs)
