# Especificação das melhorias da apostila digital e impressa

**Status geral:** Pendente — especificação registrada; correções ainda não implementadas.

**Data da avaliação:** 05/10/2026.

**Base avaliada:** `main`, commit `ba3ba4e0fbbe4d5b861999527b899a3e707ff5f0`, incluindo as alterações de estrutura didática e do README.

**Objetivo:** transformar o material em uma apostila que ensine uma pessoa iniciante em tecnologia e AWS, permita estudar para a CLF-C02 e sirva de base para uma futura edição impressa.

**Público:** leitor que pode não conhecer servidor, CPU, memória, rede, banco de dados, API, identidade ou implantação. O entendimento central não deve depender de pesquisar essas explicações fora da apostila.

## 1. Escopo e limites

Esta especificação reúne os problemas identificados na avaliação pedagógica, as alterações necessárias, os arquivos envolvidos, as dependências e os critérios de aceite. Os itens são trabalho futuro: criar este documento não resolve as pendências.

O objetivo é compreensão conceitual e escolha de serviços no nível da Cloud Practitioner. O percurso obrigatório não deve exigir implementar uma arquitetura, programar, fazer troubleshooting ou decorar telas. A prática de console será opcional e identificada como tal.

O material deve explicar o necessário para acompanhar a aula. As referências oficiais ficam disponíveis para confirmação, atualização e aprofundamento, sem substituir a explicação principal. Não se promete cobrir todas as questões possíveis do exame.

A avaliação teve inspeção estrutural do conjunto e leitura aprofundada de arquivos selecionados. As métricas não representam teste de aprendizagem com alunos nem revalidação linha a linha de preços, quotas e capacidades AWS.

## 2. Evidências da versão avaliada

| Evidência | Resultado | Consequência para o trabalho |
|---|---|---|
| Aulas nos quatro domínios | 41 | Revisar o percurso inteiro após validar um piloto. |
| Fichas de serviços/famílias | 105 | Selecionar aprofundamentos; não tornar todo o catálogo obrigatório. |
| Blocos “Antes de ler este trecho” | 400 nas aulas e 894 nas fichas | Reduzir interrupções e eliminar definições fora de contexto. |
| Perguntas típicas | 618; 616 contêm repetição literal de pergunta → resposta no bloco posterior | Substituir repetição por raciocínio autoral. A métrica não é sobre os comentários do simulado. |
| Seção “Operação, segurança e custo” | 39 fichas têm apenas a introdução padrão sob esse título | Escrever conteúdo específico ou ajustar a promessa da seção. Informações podem existir em outras partes. |
| Figuras no núcleo | Nenhuma imagem Markdown ou bloco Mermaid nas 41 aulas e 105 fichas | Criar representações das relações centrais. Existe um diagrama em página de apoio. |
| Banco de múltipla escolha | 65 questões, reutilizadas nas páginas por domínio | Criar avaliações com cenários inéditos e cobertura rastreável. |
| Aulas sem vínculo direto a questão no simulado | 2.10, 3.1, 3.6, 3.14, 3.15, 3.16, 3.18, 4.1 e 4.6 | Completar o mapeamento de treino. Isso não significa ausência de perguntas típicas ou menções indiretas. |
| Testes de apostila | 8 passaram | Manter os controles, ampliando regressões de significado quando necessário. |
| Verificação de links | 1.793 destinos internos; 0 quebrados | Manter a navegação; acrescentar validação de âncoras. URLs externas não foram validadas pelo script. |

As contagens devem ser atualizadas quando o conteúdo mudar, registrando a versão e o método. Elas identificam problemas e não devem virar metas artificiais de quantidade de texto ou perguntas.

## 3. Regras para a implementação

- Seguir [CLAUDE.md](../CLAUDE.md): branch nova, PR para `main` e merge depois que as verificações passam.
- Alterar fontes editoriais e geradores, não apenas os Markdown gerados.
- Preservar os documentos históricos em `fontes/`; correções do guia original seguem os mecanismos `CORRECOES` e `AVISOS` do gerador.
- Preservar blocos de anotações e complementos previstos nas regras do projeto.
- Confirmar novas afirmações técnicas em documentação oficial AWS. Informação ainda não confirmada vai para a página existente de pendências de verificação.
- Não acrescentar preços, limites ou promessas de comportamento a partir de suposição.
- Usar português do Brasil, exemplos concretos, termos explicados no primeiro uso e comparações pelos mesmos critérios.
- Manter uma base editorial comum para digital e impresso, com transformações de apresentação por formato.
- Evitar expansão automática que apenas aumente o texto; não preencher seções com parágrafos genéricos.
- Não marcar validação com iniciantes como concluída sem que a atividade tenha realmente ocorrido.

## 4. Mapa de fontes e saídas

| Alteração | Fonte a editar | Saída ou material afetado |
|---|---|---|
| Organização das seções, revisão e montagem | [apostila.py](../scripts/apostila.py) | Aulas, fichas e páginas de apoio geradas. |
| Definições e reconhecimento de termos | [vocabulario_apostila.py](../scripts/vocabulario_apostila.py) | Vocabulário inserido nos textos. |
| Aberturas, objetivos e domínios | [didatica_docs.py](../scripts/didatica_docs.py) | Aberturas e objetivos de `docs/`. |
| Explicações das aulas | [licoes_topicos.py](../scripts/licoes_topicos.py) | Desenvolvimento dos capítulos. |
| Aberturas de serviços | [introducoes_servicos.py](../scripts/introducoes_servicos.py) | Problema, solução, exemplo e limite. |
| Sequência dos serviços | [sequencias_servicos.py](../scripts/sequencias_servicos.py) | Passos conceituais das fichas. |
| Casos estendidos | [casos_apostila.py](../scripts/casos_apostila.py) | Exemplos com relações e decisões. |
| Casos e dados de aprofundamento | [aprofundamento.py](../scripts/aprofundamento.py) | Funcionamento, escolhas e situações comentadas. |
| Conteúdo-base das fichas | [conteudo_servicos/](../scripts/conteudo_servicos/) | Componentes, opções, custos e referências de `servicos/`. |
| Orientações de apoio | [conteudo_apoio.json](../scripts/conteudo_apoio.json) | Páginas de `docs/00-guia-do-exame/`. |
| Correções e índices | [gerar_docs.py](../scripts/gerar_docs.py) | Tópicos, índices, flashcards e resumos. |
| Questões de múltipla escolha | [banco_questoes.py](../scripts/banco_questoes.py) | Banco de treino. |
| Montagem das avaliações | [gerar_simulado.py](../scripts/gerar_simulado.py) | Simulados e páginas por domínio. |
| Modelos de contribuição | [topico.md](../templates/topico.md), [servico.md](../templates/servico.md) | Orientação para novas aulas e fichas. |
| Navegação e acompanhamento | [README](../README.md), [progresso](../progresso.md), [labs](../labs/README.md) | Entrada do aluno e uso do material. |

Novos arquivos previstos nesta especificação devem ser registrados nos geradores e nas bases necessárias antes de serem usados. Seus nomes ainda são propostas; não há links para arquivos inexistentes.

## 5. Controle das pendências

| ID | Entrega | Prioridade | Dependências | Status |
|---|---|---|---|---|
| [AP-01](#ap-01) | Vocabulário correto por contexto | P0 | — | Substituído: vocabulário automático desligado (PR 1.1 do [plano](plano-de-implementacao.md)) |
| [AP-02](#ap-02) | Justificativas reais nas perguntas | P1 | AP-01 | Pendente |
| [AP-03](#ap-03) | Revisão de regras técnicas e simplificações | P0 | — | Pendente |
| [AP-04](#ap-04) | Fundamentos e percurso por pré-requisitos | P1 | AP-01, AP-03 | Pendente |
| [AP-05](#ap-05) | Modelo de aula e revisão do piloto | P1 | AP-01 a AP-04 | Pendente |
| [AP-06](#ap-06) | Revisão didática das 41 aulas | P1 | AP-05, AP-14 | Pendente |
| [AP-07](#ap-07) | Fichas com profundidade adequada | P1 | AP-05, AP-14 | Pendente |
| [AP-08](#ap-08) | Caso recorrente e figuras | P1 | AP-04; piloto em AP-05 | Pendente |
| [AP-09](#ap-09) | Exercícios variados e simulados inéditos | P1 | AP-02, AP-05; concluir após AP-06/AP-07 | Pendente |
| [AP-10](#ap-10) | Navegação, orientações e modelos coerentes | P2 | AP-04, AP-05 | Pendente |
| [AP-11](#ap-11) | Progresso utilizável e plano realista | P2 | AP-06, AP-09 | Pendente |
| [AP-12](#ap-12) | Atividades sem console e labs opcionais claros | P2 | AP-05 | Pendente |
| [AP-13](#ap-13) | Rastreabilidade e atualização de fontes | P1 | Iniciar com AP-03; concluir após AP-06/AP-09 | Pendente |
| [AP-14](#ap-14) | Validação pedagógica do piloto | P1 | AP-05, versão piloto de AP-08/AP-09 | Pendente |
| [AP-15](#ap-15) | Geração da edição impressa | P3 | AP-06 a AP-14 | Pendente |
| [AP-16](#ap-16) | Verificações e fechamento da edição | P2/P3 | Contínua; encerramento após AP-15 | Pendente |

Cada item deve registrar: status, responsável quando definido, PRs, evidências de aceite e limitações restantes. Dependências de piloto não exigem completar todo o catálogo para testar o modelo.

## 6. Especificações por item

<a id="ap-01"></a>
### AP-01 — Corrigir o vocabulário conforme o contexto

**Problema:** o reconhecimento automático por palavras injeta definições de outro domínio e repete termos já explicados na abertura.

**Arquivos:** `scripts/vocabulario_apostila.py`, `scripts/apostila.py` e fontes editoriais das seções afetadas.

**Alterações obrigatórias:**

- [ ] No contexto de Shield, explicar SRT como Shield Response Team, não protocolo de transporte de mídia.
- [ ] Não inserir Amazon Connect ao reconhecer o nome completo EC2 Instance Connect.
- [ ] Não usar a definição de campo de banco para “atributo” no nome de um tipo EC2.
- [ ] Distinguir volume EBS de volume de consumo na aula de preços.
- [ ] Distinguir índice de banco de dados de índice/sumário da apostila.
- [ ] Diferenciar os sentidos de root, chave, imagem, modelo, função e RAM sempre que o contexto exigir.
- [ ] Usar identificadores editoriais específicos para sentidos diferentes; nomes completos de produto têm precedência sobre fragmentos.
- [ ] Declarar os termos necessários por seção ou manter seleção explícita revisável. A detecção automática pode sugerir termos, mas não deve decidir seu significado sem contexto.
- [ ] Considerar os termos explicados na abertura antes de inserir novas definições no corpo.
- [ ] Substituir listas extensas de definições por explicações junto da primeira utilização quando isso melhorar a leitura.

**Aceite:** os cinco erros concretos não aparecem na saída gerada; os sentidos alternativos têm exemplos de regressão pertinentes; revisão humana do piloto confirma que as definições correspondem ao parágrafo. Não usar apenas presença de palavras como teste de correção.

**Evidências iniciais:** [aula 2.8](../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md), [ficha EC2](../servicos/computacao/ec2.md), [aula 4.1](../docs/04-cobranca-precos-e-suporte/01-principios-de-preco.md), [auditoria](../docs/00-guia-do-exame/auditoria-conteudo-2026-10.md).

<a id="ap-02"></a>
### AP-02 — Substituir repetição por comentários que ensinam

**Problema:** `fundamentos_resposta` pode selecionar a própria linha da pergunta como fundamento. “Resposta curta” e “Fundamento explicado” passam a repetir a mesma associação.

**Arquivos:** `scripts/apostila.py` e fontes das perguntas e de seus comentários; ajustar o modelo de dados se necessário.

**Alterações obrigatórias:**

- [ ] Excluir perguntas e gabaritos do conjunto de trechos candidatos a fundamento.
- [ ] Preferir comentário autoral explícito a busca lexical como mecanismo de justificativa.
- [ ] Explicar o requisito decisivo, por que a resposta atende e por que uma alternativa plausível atenderia outro problema.
- [ ] Nas perguntas de conceito, explicar o significado e dar um exemplo, sem forçar comparações artificiais.
- [ ] Substituir a revisão genérica “qual dificuldade / o que fornece / conclusão incorreta” por perguntas específicas dos objetivos da aula.
- [ ] Apresentar a tarefa antes da resposta; recolher o gabarito no digital e identificá-lo separadamente para exportação impressa.
- [ ] Manter perguntas curtas de memorização nos flashcards, sem tratá-las como a única avaliação da compreensão.

**Aceite:** todos os comentários revisados explicam o raciocínio; nenhum é apenas a repetição literal da pergunta com a resposta; o aluno consegue tentar o exercício sem visualizar imediatamente seu gabarito. As perguntas continuam rastreáveis à aula e ao objetivo.

<a id="ap-03"></a>
### AP-03 — Corrigir regras técnicas e simplificações incompatíveis

**Problema:** atalhos podem ensinar regras universais onde existem condições importantes, ou contradizer a explicação mais cuidadosa do mesmo capítulo.

**Alterações obrigatórias:**

- [ ] Distinguir security group novo, inicialmente sem regras de entrada, do grupo `default` da VPC, que permite entrada de recursos associados ao próprio grupo.
- [ ] Revisar “PaaS: a plataforma cuida do resto” e “SaaS: nada, só usa”; explicitar que responsabilidades sobre uso, dados e acessos permanecem conforme a oferta.
- [ ] Revisar generalizações como pagar só quando há usuários, parar elimina todo custo, serverless dispensa configuração e gerenciado transfere toda responsabilidade.
- [ ] Distinguir alta disponibilidade, replicação e backup; disponibilidade não significa durabilidade, e replicação não resolve toda exclusão indevida.
- [ ] Explicar separadamente conectividade de rede, autenticação e autorização.
- [ ] Conferir classificações de exemplos IaaS/PaaS/SaaS e sua utilidade para o iniciante, preservando as condições da oferta e evitando categorias rígidas sem justificativa.
- [ ] Explicitar unidade e condição de números; distinguir quota ajustável, limite técnico e requisito de modalidade.
- [ ] Revisar nomes, planos, preços e status voláteis com fonte e data antes de fechar a edição.

**Arquivos:** fontes em `scripts/conteudo_servicos/`, `scripts/didatica_docs.py`, `scripts/licoes_topicos.py`, `scripts/gerar_docs.py` e demais fontes apontadas no mapa. Não editar o guia original para remover divergências.

**Aceite:** os exemplos confirmados estão corrigidos e não há regras contraditórias nos arquivos revisados; cada afirmação técnica nova ou corrigida tem fonte oficial verificável. Sem confirmação, registrar a pendência de fonte, não inventar uma resposta.

<a id="ap-04"></a>
### AP-04 — Criar os fundamentos e organizar a sequência de estudo

**Problema:** a primeira aula cita muitos serviços e conceitos; parte da segurança exige uma compreensão de rede ensinada depois. Glossário isolado não substitui pré-requisitos.

**Alterações obrigatórias:**

- [ ] Criar uma unidade curta de fundamentos: aplicação/navegador/servidor/SO; CPU/memória/armazenamento; rede/endereço/porta/pedido-resposta; arquivo/registro/banco; conta/identidade/autenticação/autorização.
- [ ] Usar uma situação concreta para conectar esses conceitos, com exercício de compreensão.
- [ ] Declarar pré-requisitos e objetivos no início das aulas.
- [ ] Mapear dependências antes de fixar a sequência; antecipar os fundamentos de rede necessários à proteção de rede.
- [ ] Evitar apresentar longas listas de nomes AWS antes de explicar a necessidade correspondente.
- [ ] Manter domínios e tasks oficiais como metadados, mesmo quando a sequência pedagógica for diferente.
- [ ] Distinguir “aula 3.7” de “task oficial 3.7”; a numeração local não equivale à do guia oficial.
- [ ] Atualizar o sumário e os caminhos de anterior/próxima; manter remissões existentes ou oferecer destinos equivalentes quando houver reorganização.

**Proposta de organização:** orientação → fundamentos → percurso principal → revisões e avaliações → caderno de serviços → apêndices. A localização exata dos novos arquivos será definida na implementação e registrada no gerador.

**Aceite:** cada conceito necessário já foi ensinado ou é explicado no próprio trecho; o iniciante encontra a próxima leitura sem escolher entre vários caminhos obrigatórios; a rastreabilidade ao guia é mantida.

<a id="ap-05"></a>
### AP-05 — Definir e aplicar um modelo de aula no piloto

**Problema:** reorganizar listas em blocos dá aparência de capítulo sem desenvolver necessariamente a explicação.

**Modelo obrigatório, adaptável ao assunto:**

1. Objetivos observáveis e pré-requisitos.
2. Problema concreto.
3. Explicação em sequência: peças, entrada, trabalho e resultado.
4. Figura ou exemplo de dados quando ajudar.
5. Opções, consequências e limites.
6. Caso resolvido: necessidade, opções consideradas, decisão, justificativa e resultado.
7. Exercícios com variação de requisitos.
8. Síntese essencial e aprofundamento opcional.
9. Gabarito comentado e referências relacionadas.

**Alterações obrigatórias:**

- [ ] Implementar o modelo nas fontes e na montagem, preservando notas e links.
- [ ] Colocar objetivos antes do conteúdo, não apenas na revisão final.
- [ ] Escrever parágrafos conectados que expliquem as relações, em vez de apenas expandir células e bullets.
- [ ] Usar analogias com limites claros; garantir que a explicação técnica continue suficiente sem a analogia.
- [ ] Evitar títulos que prometem mais do que o conteúdo oferece e frases genéricas repetidas em toda aula.
- [ ] Revisar um piloto com fundamentos, introdução à nuvem, EC2, armazenamento, IAM e rede. A ordem do piloto segue os pré-requisitos de AP-04.
- [ ] Criar figuras e exercícios novos para o piloto antes de expandir o padrão.

**Arquivos:** `scripts/apostila.py`, fontes didáticas e de exemplos, modelos de contribuição e registros do gerador.

**Aceite:** o piloto permite explicar o que cada componente faz e como se relaciona com os demais; contém objetivos, caso e exercício realmente específicos; passa nas verificações técnicas. A expansão depende do resultado de AP-14.

<a id="ap-06"></a>
### AP-06 — Revisar as 41 aulas do percurso principal

**Alterações obrigatórias:**

- [ ] Aplicar o modelo validado, por domínio, sem exigir o mesmo tamanho para todos os assuntos.
- [ ] Converter resumos telegráficos em explicações suficientes para os objetivos.
- [ ] Relacionar serviço, necessidade e resultado antes de memorizar nomes.
- [ ] Dividir aulas que acumulam muitos objetivos em unidades menores quando isso melhorar a aprendizagem.
- [ ] Explicar as bases antes de recursos menos conhecidos ou especializados.
- [ ] Usar tabelas para comparações, depois da explicação dos critérios e alternativas.
- [ ] Indicar exatamente os trechos das fichas necessários para complementar cada aula.
- [ ] Eliminar duplicações entre abertura, corpo, caso e revisão sem retirar informações necessárias.
- [ ] Revisar flashcards e resumos derivados para que preservem as condições das regras corrigidas.
- [ ] Manter um registro por aula: objetivos, pré-requisitos, nível, exercícios, fontes, revisão editorial e PR.

**Aceite:** as 41 aulas foram avaliadas individualmente contra o modelo; cada objetivo tem explicação e treino; nenhum trecho essencial depende de uma pesquisa externa para ter sentido. A contagem pode mudar se houver divisão de unidades, desde que o mapa anterior/novo e a cobertura sejam registrados.

<a id="ap-07"></a>
### AP-07 — Revisar as fichas e delimitar o aprofundamento

**Problema:** fichas longas misturam fundamentos e detalhes operacionais; outras mantêm seções genéricas sem conteúdo próprio.

**Alterações obrigatórias:**

- [ ] Classificar trechos como fundamento, preparação conceitual CLF-C02 ou aprofundamento opcional. Esta é classificação editorial, não previsão de prova.
- [ ] Priorizar fichas centrais do piloto antes de revisar o restante do catálogo.
- [ ] Explicar componentes pelo significado e pela função no problema; evitar listas de recursos sem conexão.
- [ ] Examinar as 39 seções com apenas introdução padrão e escrever conteúdo específico ou integrar/remover a seção conforme sua finalidade.
- [ ] Revisar as demais seções também: conter algum texto não comprova suficiência didática.
- [ ] Em serviços secundários, adotar ficha curta com problema, função, comparação útil, limite e referência, em vez de preencher sete seções artificiais.
- [ ] Separar dados de implementação que não são necessários ao objetivo conceitual, como detalhes operacionais de IMDS, de fundamentos obrigatórios.
- [ ] Nas fichas que reúnem famílias, identificar a função e o status de cada serviço quando forem diferentes.
- [ ] Dar destaque ao que AWS administra, ao que o cliente decide e às unidades de custo relevantes, sem repetir advertências genéricas.
- [ ] Incluir retorno claro à aula relacionada e referências oficiais específicas.

**Aceite:** todas as fichas têm decisão editorial registrada; os trechos obrigatórios são compreensíveis sem detalhes opcionais; não há seções com promessa de conteúdo não atendida. Escopo da prova e nível de aprofundamento não são tratados como a mesma coisa.

<a id="ap-08"></a>
### AP-08 — Conectar os exemplos e criar figuras úteis

**Alterações obrigatórias:**

- [ ] Usar a escola como caso recorrente: disponibilizar sistema, guardar documentos, administrar acessos, atender picos, conservar dados, observar falhas e entender custos.
- [ ] Cada novo serviço responde a uma necessidade já apresentada; evitar introduzir uma arquitetura completa antes dos seus conceitos.
- [ ] Criar figuras de região/AZ/datacenter, pedido entre aplicação e banco, EC2/memória/discos, identidade/ação/recurso, balanceamento/escalabilidade, tipos de armazenamento, SNS/SQS e unidades de custo.
- [ ] Incluir legendas e descrição textual; não usar apenas nomes de serviços como explicação.
- [ ] Usar cores como apoio, nunca como única forma de transmitir significado.
- [ ] Manter fontes editáveis das figuras e garantir renderização para impressão.
- [ ] Evitar diagramas decorativos: cada figura deve responder a uma dúvida concreta.

**Arquivos:** fontes de lições, casos e sequências; local de figuras e rotina de renderização a definir na implementação.

**Aceite:** o leitor consegue acompanhar o caminho da informação na figura e no texto; as figuras do piloto funcionam em preto e branco e no digital; exemplos não pressupõem capacidade não ensinada.

<a id="ap-09"></a>
### AP-09 — Desenvolver avaliações de compreensão e decisão

**Alterações obrigatórias:**

- [ ] Separar exercícios de aula, revisão acumulada, flashcards e simulados finais.
- [ ] Mapear objetivo → questão → comentário → aula; incluir os nove tópicos sem vínculo direto identificados na base.
- [ ] Criar exercícios de explicar, comparar, escolher e mudar um requisito do cenário.
- [ ] Usar distratores plausíveis e requisitos suficientes para decidir sem adivinhar intenção.
- [ ] Explicar por que cada alternativa relevante atende ou não ao requisito.
- [ ] Reservar questões inéditas para a avaliação final; não reutilizar integralmente o banco de treino como única evidência de prontidão.
- [ ] Identificar quais páginas reutilizam perguntas para evitar contar repetição como treino independente.
- [ ] Documentar a distribuição dos simulados como aproximação editorial dos pesos; na prova real, 50 questões pontuam e 15 não pontuam, e os pesos se referem ao conteúdo pontuado.
- [ ] Não converter nota escalonada 700 em porcentagem de acertos nem tratar meta de treino como garantia de aprovação.
- [ ] Revisar o fluxo digital de resposta e gerar gabarito separado no impresso.

**Arquivos:** `scripts/banco_questoes.py`, `scripts/gerar_simulado.py`, fontes dos exercícios das aulas e modelos de simulado.

**Aceite:** cada objetivo principal tem treino compatível; existe avaliação final com perguntas não usadas nas atividades anteriores; o gabarito apresenta raciocínio. A prontidão é avaliada também em cenários novos, sem definir uma quantidade arbitrária de questões como prova de qualidade.

<a id="ap-10"></a>
### AP-10 — Atualizar orientações, navegação e modelos

**Alterações obrigatórias:**

- [ ] Atualizar referências a “Aprofundamento para a prova” e “Ficha prática” na página de estudo sem console, conforme os títulos realmente publicados.
- [ ] Alinhar `templates/topico.md` e `templates/servico.md` ao modelo validado e aos campos editoriais atuais.
- [ ] Manter uma entrada principal clara no README, reaproveitando sua melhoria atual.
- [ ] Oferecer anterior, próximo, índice e retorno das fichas à aula sem depender apenas de metadados.
- [ ] Separar o percurso do aluno de auditorias, manutenção e histórico editorial.
- [ ] Atualizar índices, sumários e legendas se a estrutura ou as categorias mudarem.
- [ ] Corrigir a apresentação de labs: o material atual tem sugestões e modelo, não roteiros completos.

**Aceite:** nenhuma orientação manda procurar seção inexistente; nenhum link relativo ou remissão interna aponta para um destino inválido; um leitor consegue seguir o percurso sem conhecer a estrutura do repositório.

<a id="ap-11"></a>
### AP-11 — Tornar o progresso utilizável e o plano de estudos realista

**Alterações obrigatórias:**

- [ ] Explicar que editar checkboxes no GitHub exige uma cópia pessoal ou edição do arquivo; não prometer salvamento individual por um clique de leitura.
- [ ] Oferecer uma forma simples de acompanhamento: cópia pessoal do Markdown e/ou checklist imprimível. Uma interface de progresso persistente é trabalho opcional futuro.
- [ ] Separar leitura concluída de compreensão verificada; registrar dúvidas e objetivos a revisar.
- [ ] Recalibrar o plano após selecionar leituras obrigatórias: a semana 5 atual reúne 14 aulas e o primeiro simulado.
- [ ] Estimar leitura, exercícios, aprofundamentos selecionados e revisão acumulada por unidade.
- [ ] Oferecer ritmos por disponibilidade e pré-requisitos, sem recomendar juntar semanas como resposta à falta de tempo.
- [ ] Usar revisões espaçadas e retomada dos erros com exercícios diferentes.

**Arquivos:** fonte do plano em `scripts/conteudo_apoio.json`, `progresso.md`, orientações do README e materiais de revisão.

**Aceite:** o tempo anunciado comporta as atividades planejadas; o leitor sabe onde registrar seu progresso e como revisar; estimativas ainda não validadas estão identificadas como tais.

<a id="ap-12"></a>
### AP-12 — Completar atividades sem console e delimitar labs opcionais

**Alterações obrigatórias:**

- [ ] Criar atividades de classificação de necessidades, percurso de pedidos/dados e comparação de soluções, sem conta AWS.
- [ ] Relacionar cada atividade aos objetivos e ao caso da aula.
- [ ] Manter console e implementação fora dos requisitos obrigatórios de conclusão.
- [ ] Para cada lab que for desenvolvido, registrar objetivo, pré-requisitos, condições de conta, passos, resultado observável, custos possíveis e limpeza.
- [ ] Identificar labs ainda não escritos como sugestões; não apresentá-los como passo a passo pronto.
- [ ] Não prometer gratuidade sem verificar as condições atuais da conta e dos serviços; deixar explícito que alerta de orçamento não é um teto universal de gastos.

**Aceite:** o percurso conceitual pode ser concluído sem usar console; atividades têm comentários; labs publicados como completos são executáveis e possuem validação e limpeza descritas.

<a id="ap-13"></a>
### AP-13 — Rastrear competências e manter fontes atualizáveis

**Alterações obrigatórias:**

- [ ] Manter uma matriz domínio/task oficial → objetivo local → explicação → exercício → fonte.
- [ ] Revisar a matriz quando aulas forem divididas, renumeradas ou reordenadas.
- [ ] Distinguir serviço listado no escopo de detalhe operacional considerado essencial; um não implica o outro.
- [ ] Identificar afirmações voláteis: planos, preços, disponibilidade, nomes de produtos, quotas e status de oferta.
- [ ] Registrar fonte oficial, data de consulta, contexto/modalidade e local do conteúdo afetado.
- [ ] Distinguir atualização comercial de mudança comprovada no guia de certificação.
- [ ] Manter fontes históricas preservadas e registrar correções na base atual.
- [ ] Documentar limitações da revisão; não afirmar que ausência de pendência prova correção de todas as linhas.

**Aceite:** cada objetivo principal é rastreável; novas afirmações têm fontes oficiais; pendências não confirmadas permanecem visíveis; a edição tem data de revisão e regras de atualização.

<a id="ap-14"></a>
### AP-14 — Validar o piloto com um leitor iniciante

**Alterações obrigatórias:**

- [ ] Fazer uma revisão editorial de clareza antes do teste.
- [ ] Pedir a um leitor iniciante que percorra o piloto, identificando pré-requisitos e pontos em que precisou de ajuda.
- [ ] Verificar se explica um conceito com palavras próprias, compara duas alternativas e decide quando muda um requisito.
- [ ] Registrar trechos que geraram pesquisa externa necessária para compreender o conteúdo central.
- [ ] Anotar duração e dificuldade das atividades, distinguindo observação de estimativa.
- [ ] Corrigir os pontos identificados e registrar a evidência antes de expandir o modelo.

**Aceite:** há registro real das tarefas e observações; dúvidas recorrentes receberam correção; o modelo do piloto está aprovado editorialmente para expansão. A validação com uma pessoa é um teste formativo inicial, não comprovação universal de eficácia.

**Responsável pela participação:** a definir. A necessidade de um leitor real não impede preparar o piloto e suas atividades.

<a id="ap-15"></a>
### AP-15 — Produzir a edição impressa a partir da mesma base

**Problema:** concatenar Markdown preservaria respostas intercaladas, repetições, navegação de GitHub e recursos que não funcionam em papel.

**Alterações obrigatórias:**

- [ ] Definir um manifesto de publicação com ordem dos capítulos, inclusão de fichas, apêndices e identificadores estáveis.
- [ ] Gerar digital e impresso da mesma base, evitando duas versões editoriais divergentes.
- [ ] Selecionar fichas para apêndices ou caderno complementar; não incluir automaticamente todas as 105 no corpo do livro.
- [ ] Gerar sumário paginado, numeração de seções/figuras e remissões internas apropriadas ao papel.
- [ ] Transformar `<details>`: conteúdo necessário entra no texto ou em apêndice; respostas vão ao gabarito.
- [ ] Renderizar diagramas como figuras legíveis e manter suas fontes editáveis.
- [ ] Remover setas de navegação, status pessoais, HTML de interação e instruções de contribuição do corpo didático.
- [ ] Reduzir repetições de definições próprias de páginas digitais abertas isoladamente.
- [ ] Formatar tabelas dentro da página, com cabeçalhos repetidos quando necessário e sem texto cortado.
- [ ] Não depender de emojis nem de cor; incluir legendas, contraste e fonte legível.
- [ ] Apresentar fontes como referências e URLs úteis; QR codes podem complementar, mas não substituem informação essencial.
- [ ] Gerar PDF com texto selecionável e navegação útil; incluir edição, data de fechamento e endereço de errata.
- [ ] Disponibilizar checklist e espaço de anotações adequados ao papel.
- [ ] Renderizar um capítulo piloto antes da exportação completa e conferir uma amostra impressa em preto e branco.

**Aceite:** o aluno usa o livro sem clicar; sumário, gabarito e remissões são coerentes; figuras/tabelas ficam legíveis no tamanho de impressão escolhido; conteúdo digital e impresso corresponde à mesma versão editorial.

**Decisões de implementação a registrar:** formato de página, ferramenta de exportação, tipografia, seleção de apêndices e estratégia de atualização da errata. Não há necessidade de construir uma plataforma web completa para cumprir este item.

<a id="ap-16"></a>
### AP-16 — Validar mudanças e fechar a edição

**Alterações e verificações obrigatórias:**

- [ ] Manter testes de preservação de notas, links, unidades e cobertura das fontes.
- [ ] Acrescentar regressões para colisões de vocabulário e justificativas que selecionam a própria pergunta.
- [ ] Verificar que geração repetida produz o mesmo conteúdo quando a base não muda.
- [ ] Validar âncoras internas, além da existência de arquivos. O verificador atual ignora esse problema.
- [ ] Conferir as fontes externas necessárias às alterações; reportar indisponibilidade sem assumir que o conteúdo está confirmado.
- [ ] Executar leitura editorial de cada unidade, verificando objetivos, explicações, casos e comentários.
- [ ] Inspecionar a renderização completa do PDF; corrigir cortes, tabelas, remissões, figuras e páginas problemáticas.
- [ ] Registrar versão, comandos executados, resultado e limitações no PR e nesta especificação.
- [ ] Marcar pendências individualmente; fechamento geral só ocorre quando os critérios aplicáveis estiverem satisfeitos.

**Comandos previstos, conforme o tipo de alteração:**

```bash
python3 scripts/test_apostila.py
python3 scripts/gerar_docs.py
python3 scripts/gerar_simulado.py
python3 scripts/verificar_links.py
git diff --check
```

Regenerar o simulado quando o banco ou sua montagem mudar. A futura rotina de exportação será documentada quando implementada. Os comandos não substituem revisão de significado nem validação com leitores.

**Aceite:** controles aplicáveis passam, anotações continuam preservadas, diferenças foram revisadas e nenhuma validação pendente é apresentada como realizada.

## 7. Exemplo de resultado esperado

**Situação:** uma escola precisa guardar PDFs de certificados; não precisa executar um programa nesses arquivos.

**Explicação:** EC2 fornece uma máquina virtual para executar programas. S3 fornece armazenamento de objetos. Guardar arquivos e executar uma aplicação são necessidades diferentes.

**Exercício:** é necessário criar uma EC2 apenas para guardar esses PDFs? Justifique.

**Comentário esperado:** o requisito principal é armazenamento, atendido por S3. Uma EC2 poderia fazer parte de uma aplicação mais ampla, mas acrescentaria uma máquina para administrar sem ser necessária apenas para guardar arquivos. Se a escola precisar executar um programa Linux, será preciso analisar a necessidade de computação e suas alternativas.

O comentário relaciona requisito e solução, identifica uma alternativa e mostra uma condição que mudaria a decisão. Não basta responder “S3”.

## 8. Ordem recomendada de execução

1. **Correções de significado:** AP-01, AP-02 e AP-03; iniciar rastreabilidade em AP-13.
2. **Base e piloto:** AP-04 e AP-05, com uma amostra de figuras/casos de AP-08 e exercícios de AP-09.
3. **Validação formativa:** AP-14; corrigir o piloto antes da expansão.
4. **Revisão do conjunto:** AP-06 e AP-07, ampliando AP-08, AP-09 e AP-13.
5. **Uso e planejamento:** AP-10, AP-11 e AP-12.
6. **Publicação impressa:** AP-15 e fechamento em AP-16.

AP-16 acompanha cada etapa. Preparar a estrutura de exportação pode começar antes, mas o livro não deve ser declarado pronto enquanto o conteúdo ainda estiver em revisão.

## 9. Definição de conclusão do projeto

- [ ] O iniciante encontra o início, os pré-requisitos e a próxima aula.
- [ ] Cada objetivo principal tem explicação, exemplo e treino.
- [ ] Definições usam o significado correto no contexto.
- [ ] Casos mostram decisões e consequências, e não apenas nomes de serviços.
- [ ] Gabaritos explicam o raciocínio e ficam separados da tentativa do aluno.
- [ ] Aprofundamentos opcionais estão identificados.
- [ ] Competências oficiais têm cobertura rastreável sem promessa de prever toda a prova.
- [ ] Há avaliação em cenários inéditos.
- [ ] Progresso e estimativas de estudo têm instruções utilizáveis.
- [ ] A versão impressa tem sumário, remissões, figuras e gabarito funcionais.
- [ ] Fontes voláteis, data de revisão e errata estão documentadas.
- [ ] Verificações técnicas, revisão editorial e validação do piloto têm evidências registradas.

## 10. Referências oficiais para as correções já identificadas

- [Guia oficial CLF-C02: perfil, competências e estrutura do exame](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html).
- [Tecnologias e conceitos](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-technologies-concepts.html).
- [Shield Response Team — significado de SRT no contexto de Shield](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-srt-support.html).
- [Criação de security groups — regras iniciais de um grupo novo](https://docs.aws.amazon.com/vpc/latest/userguide/creating-security-groups.html).
- [Security group default — regras de entrada e saída](https://docs.aws.amazon.com/vpc/latest/userguide/default-security-group.html).

Consultadas na avaliação de 05/10/2026. Reconfirmar afirmações sujeitas a alteração ao implementá-las e ao fechar a edição.

## 11. Histórico de execução

| Data | Item | Alteração e evidência | PR | Status |
|---|---|---|---|---|
| 05/10/2026 | Especificação | Registro inicial das pendências; nenhuma correção de conteúdo implementada neste registro. | A registrar após abertura | Pendente |

[Voltar às pendências](README.md) · [Voltar ao repositório](../README.md)
