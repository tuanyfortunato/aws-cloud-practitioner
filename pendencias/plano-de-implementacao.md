# Plano de implementação: da apostila gerada à apostila escrita

**Status geral:** Em andamento — Fase 0 iniciada.

**Data:** 05/10/2026.

**Base:** `main`, commit `f586aacd9fbfab3112f12e3a8f392839e7cad303`.

**Documentos de origem:** [Avaliação pedagógica: profundidade](avaliacao-pedagogica-profundidade.md) (diagnóstico e nova ordem) e [Apostila digital e impressa](apostila-digital-e-impressa.md) (itens AP-01 a AP-16 e critérios de aceite detalhados).

**Ideia central:** as aulas e fichas deixam de ser montadas pelos scripts e passam a ser **escritas à mão**, uma a uma, com o próprio Markdown como fonte da verdade. A migração é **gradual**: aulas ainda não migradas continuam geradas, e o repositório funciona em todas as etapas.

## 1. Como o repositório funciona hoje

Entender o fluxo atual define onde cada mudança entra.

| Etapa | Onde acontece | O que produz |
|---|---|---|
| Leitura do guia original | `parse_guia()` em `scripts/gerar_docs.py`, a partir de `fontes/guia-completo-clf-c02.md` | Seções 1.1 a 4.6, introduções dos domínios, pares e palavras-chave |
| Montagem das aulas | `capitulo_topico()` em `scripts/apostila.py`, com `licoes_topicos.py`, `didatica_docs.py`, `aprofundamento.py` | Corpo das 41 aulas em `docs/`; **reescreve o arquivo inteiro**, preservando só os blocos `extra` e `notas` |
| Montagem das fichas | `capitulo_servico()` em `scripts/apostila.py`, com `conteudo_servicos/*.json`, `introducoes_servicos.py`, `sequencias_servicos.py` | As 105 fichas em `servicos/` |
| Vocabulário | `Leitura.vocabulario()` em `scripts/apostila.py`, com `vocabulario_apostila.py` | Os 1.349 blocos "Antes de ler este trecho" |
| Flashcards | `extrair_cards()` em `scripts/gerar_docs.py` | `flashcards/dominio-*.md` e `anki-clf-c02.tsv`, a partir das "Perguntas típicas" **do guia original** |
| Índices | `gerar_indice_servicos()` e `gerar_indice_readme()` | `servicos/README.md` e sumário do `README.md` |

**Consequência:** editar um arquivo em `docs/` à mão hoje não adianta; a próxima execução do gerador apaga a edição. Por isso a Fase 0 vem antes de qualquer reescrita.

## 2. Visão geral das fases

| Fase | Entrega | Itens AP relacionados | Depende de |
|---|---|---|---|
| 0 | Mecanismo de aula e ficha "autoral" no gerador | — (pré-requisito técnico) | — |
| 1 | Limpeza rápida do material gerado | AP-01 (substituído), AP-02 | 0 |
| 2 | Capítulo 0 — Fundamentos de TI e glossário único | AP-04 | 1 |
| 3 | Modelo de aula, aula-piloto e ficha-piloto | AP-05, AP-08 (piloto), AP-14 | 2 |
| 4 | Reescrita das 41 aulas em ondas | AP-03, AP-06, AP-08 | 3 |
| 5 | Fichas condensadas e caderno de consulta | AP-07 | 3; em paralelo à 4 |
| 6 | Exercícios e banco de questões | AP-09, AP-13 | 4 |
| 7 | Edição impressa | AP-15, AP-16 | 4, 5, 6 |
| 8 | Aposentar o gerador de conteúdo | AP-10, AP-11 | Todas as aulas e fichas migradas |

Cada fase é dividida em PRs pequenos, conforme o [CLAUDE.md](../CLAUDE.md): branch `claude/<descricao>`, PR para `main` e merge pelo Claude depois que as verificações passam.

## 3. Fase 0 — Mecanismo de conteúdo autoral

**Objetivo:** permitir que uma aula ou ficha escrita à mão conviva com as geradas, sem ser sobrescrita.

**PR 0.1 — Marcador de arquivo autoral**

- Definir um marcador no topo do arquivo: `<!-- autoral -->`.
- Em `gerar_topicos()` (`gerar_docs.py`): se o arquivo existente tiver o marcador, **não** chamar `capitulo_topico()` nem reescrever o corpo. O gerador continua atualizando só o que é mecânico, se necessário (nada no corpo).
- Em `gerar_capitulos_servicos()`, `aplicar_escopo_fichas()` e `aplicar_introducoes()`: mesmo comportamento para fichas com o marcador.
- Em `extrair_cards()`: para aula autoral, ler as perguntas da seção `## Revisão` do próprio arquivo, e não do guia original (formato definido na Fase 3).
- Em `test_apostila.py`: novo teste garantindo que um arquivo autoral sai idêntico depois de rodar o gerador; ajustar `test_capitulos_de_topicos_e_perguntas_preservados` e `test_cobertura_e_conservacao_das_referencias` para pular itens autorais.
- Atualizar o `CLAUDE.md`: "aulas e fichas com `<!-- autoral -->` são editadas diretamente no Markdown; as demais seguem as regras atuais".

**PR 0.2 — Script de métricas**

- Criar `scripts/metricas_apostila.py`, que conta por arquivo: blocos "Antes de ler este trecho", ocorrências de "compatíve" e "conforme", revisões cuja resposta repete a abertura, seções só com texto padrão, aulas autorais e geradas.
- Linha de base medida em 06/10/2026 (`main`): 1.349 blocos de vocabulário automático, 1.555 ocorrências de "compatíve"/"conforme", 123 revisões circulares (3 por aula), 147 seções só com texto padrão (105 "Roteiro de leitura" e 39 "Operação, segurança e custo") e 0 arquivos autorais, em 316 mil palavras.
- A saída registra a evolução no PR de cada fase e alimenta os critérios de aceite. As métricas apontam problemas; não são metas de quantidade.

**Aceite da fase:** gerador, `test_apostila.py` e `verificar_links.py` passando; nenhuma mudança visível no material.

## 4. Fase 1 — Limpeza rápida do material gerado

**Objetivo:** melhorar já as 41 aulas e 105 fichas geradas, enquanto a reescrita não chega até elas. São mudanças no gerador, de baixo custo.

**PR 1.1 — Desligar o vocabulário automático**

- Em `apostila.py`, `Leitura.vocabulario()` passa a retornar texto vazio (constante `VOCABULARIO_AUTOMATICO = False`, para reverter se necessário).
- Manter `vocabulario_apostila.py` por enquanto: as definições boas servirão de matéria-prima para o glossário (Fase 2). Os testes de siglas continuam válidos para o módulo.
- Ponto de atenção: até a Fase 2, alguns termos ficam sem explicação. Por isso o PR 1.1 só entra junto ou depois do PR 2.1, ou com um aviso no README apontando o glossário.

**PR 1.2 — Remover revisão circular e repetições**

- Em `capitulo_topico()`: retirar o bloco "Confira se você compreendeu" que reaproveita `problema`, `simples` e `limite` da abertura.
- Nas perguntas típicas: retirar o "Fundamento explicado no capítulo" quando ele só repete pergunta e resposta.
- Retirar frases-padrão sem conteúdo ("Leia cada linha como uma alternativa...", "A resposta muda se mudar o requisito destacado...").
- Retirar a seção "Operação, segurança e custo" quando ela só teria a introdução padrão (39 fichas).
- Retirar a linha de status 🔴 das aulas; o acompanhamento fica só no [progresso](../progresso.md).

**Aceite da fase:** `metricas_apostila.py` mostra zero blocos de vocabulário, zero revisões circulares e zero seções só com texto padrão; testes e links passando.

**Resultado do PR 1.2 (06/10/2026):** revisões circulares 123 → 0; seções só com texto padrão 147 → 1 (a que resta é a tabela de labs, escrita à mão); "Fundamento explicado no capítulo" 616 → 11, só onde cita um fato do capítulo; 39 mil palavras a menos. O vocabulário automático continua (PR 1.1, depois da Fase 2).

**Resultado do PR 1.1 (06/10/2026):** `VOCABULARIO_AUTOMATICO = False` em `scripts/apostila.py`; blocos "Antes de ler este trecho" 1294 → 0 (aulas 380, páginas de apoio 55, fichas 859); 91 mil palavras a menos (289 mil → 198 mil). Os termos básicos ficam no capítulo 0 e no glossário. `vocabulario_apostila.py` continua no repositório.

## 5. Fase 2 — Capítulo 0 e glossário único

**Objetivo:** dar ao iniciante os pré-requisitos que hoje aparecem como definições soltas.

**PR 2.1 — Capítulo 0: Fundamentos de TI**, em `docs/fundamentos/` (apresentado como "Capítulo 0" no README, para não confundir com `docs/00-guia-do-exame/`). Sugestão de aulas curtas, todas autorais:

| Aula | Assunto | Prepara para |
|---|---|---|
| 0.1 | Computador, servidor e sistema operacional; o que é virtualização | 1.1, 3.3 |
| 0.2 | Rede: IP, porta, DNS, HTTP e HTTPS, internet × rede privada | 2.8, 3.10 |
| 0.3 | Dados: arquivo, bloco, objeto; banco relacional × não relacional | 3.7, 3.8, 3.9 |
| 0.4 | Como programas conversam: API, requisição e resposta, filas | 3.1, 3.13 |
| 0.5 | Segurança básica: identidade, autenticação, autorização, criptografia | 2.1 a 2.5 |

- Registrar as aulas no README, no `progresso.md` e na navegação.

**PR 2.2 — Glossário único**

- Revisar o [glossário](../glossario.md) existente (já tem cerca de 90 termos) como **o** lugar de consulta rápida.
- Aproveitar as definições boas de `vocabulario_apostila.py`; reescrever as defensivas para dizer o que o termo é e para que serve.
- Regra para as aulas autorais: o termo é explicado em prosa no primeiro uso, dentro do raciocínio; o glossário serve para relembrar, não para ensinar.

## 6. Fase 3 — Modelo de aula e piloto

**Objetivo:** fixar o padrão antes de escalar. É a fase mais importante do plano.

**PR 3.1 — Novo modelo de aula** (`templates/topico.md`)

| Parte | Conteúdo | Observação |
|---|---|---|
| Abertura | O problema, contado pelo caso da escola | Um ou dois parágrafos; sem tabela de termos |
| Desenvolvimento | Um subtítulo por conceito central: o que é → como funciona por dentro → por que existe → custo ou limite | Prosa; listas só para enumerações reais |
| Figura | Pelo menos uma, quando houver relação espacial ou de fluxo | Ver regras de figura abaixo |
| Na prova | Como o tema aparece nos enunciados e as confusões mais comuns | Substitui os "Cai na prova" espalhados |
| Caso resolvido | Cenário, raciocínio e por que as alternativas tentadoras falham | Escrito à mão |
| Revisão | Três a cinco perguntas de compreensão, com resposta comentada | Respostas nunca copiam outro trecho da aula; viram flashcards |
| Resumo | Cinco a oito linhas para revisão rápida | Último bloco da aula |

**Regras de figura:**

- Fluxos e sequências (SQS × SNS, ciclo de vida de requisição): Mermaid no próprio Markdown, que o GitHub renderiza.
- Arquiteturas com ícones AWS (Região e AZ, VPC com subnets): draw.io, exportado em SVG para `assets/imagens/`, com o `.drawio` versionado ao lado.
- Toda figura legível em preto e branco e com legenda em texto.

**PR 3.2 — Aula-piloto: 2.1 Responsabilidade compartilhada**

- Escolhida por ser central no domínio de maior peso (30%) e por depender do Capítulo 0.
- Arquivo com `<!-- autoral -->`, seguindo o modelo.
- Afirmações técnicas conferidas em fonte oficial AWS e listadas no fim da aula.

**PR 3.3 — Ficha-piloto: SQS**, no novo modelo de ficha (Fase 5).

**Validação com leitor iniciante (AP-14):**

- Uma ou duas pessoas iniciantes leem a aula-piloto sem ajuda.
- Depois respondem, por escrito: o que não entenderam, onde precisaram pesquisar, e as perguntas de revisão.
- Registrar o resultado neste documento e ajustar o modelo antes da Fase 4. Não marcar como validado sem a leitura ter ocorrido.

**Resultado:** em 06/10/2026 a dona do repositório leu a aula-piloto 2.1 e a aprovou sem pedir ajustes. A Fase 4 começou com o modelo como está; a leitura por iniciantes com respostas por escrito continua bem-vinda e, se apontar problemas, o modelo e as aulas já escritas são ajustados.

## 7. Fase 4 — Reescrita das aulas em ondas

**Objetivo:** migrar as 41 aulas para o modelo validado, cada PR com duas ou três aulas, suas figuras e suas perguntas de revisão.

| Onda | Aulas | Motivo da ordem |
|---|---|---|
| A | 2.2 a 2.10 | Termina o domínio de maior peso, começado no piloto |
| B | 1.1 a 1.7 | Base conceitual; a 1.1 hoje antecipa serviços demais |
| C | 3.1 a 3.10 | Núcleo técnico: acesso, infraestrutura global, computação, dados, rede |
| D | 3.11 a 3.18 | Serviços complementares; aulas mais curtas |
| E | 4.1 a 4.6 | Cobrança e suporte; exige conferência de preços e planos na data |

**Checklist de cada aula (vai na descrição do PR):**

- [ ] Marcador `<!-- autoral -->` no topo.
- [ ] Cada conceito central explica mecanismo, motivo e limite, em prosa.
- [ ] Nenhum serviço citado antes de ser ensinado, exceto com remissão explícita ("veremos na aula 3.10").
- [ ] Simplificações revisadas (ex.: Lambda tratado como serverless, não encaixado à força em PaaS) — AP-03.
- [ ] Pelo menos uma figura, quando o tema tiver relação espacial ou de fluxo.
- [ ] Revisão com respostas comentadas e não copiadas.
- [ ] Fontes oficiais AWS conferidas e listadas; dúvidas registradas em [pendências de verificação](../docs/00-guia-do-exame/pendencias-de-verificacao.md).
- [ ] `metricas_apostila.py`, `test_apostila.py`, `gerar_docs.py` e `verificar_links.py` sem erros.

## 8. Fase 5 — Fichas e caderno de consulta

**Objetivo:** transformar as fichas em consulta rápida, de uma ou duas páginas, sem repetir a aula.

**Novo modelo de ficha** (`templates/servico.md`):

1. Em uma frase.
2. Que problema resolve (dois ou três parágrafos; pode remeter à aula).
3. Como funciona, em três a cinco passos.
4. Opções principais, em tabela.
5. Números que a prova cobra, cada um com data de verificação.
6. Como é cobrado.
7. Não confundir com.
8. Fontes oficiais.

**Classificação das 105 fichas:**

| Grupo | Critério | Destino |
|---|---|---|
| Núcleo | Serviço central de alguma aula | Reescrita completa; entra no caderno de consulta impresso |
| Complementar | No escopo, mas periférico | Versão curta (itens 1, 3, 7 e 8) |
| Referência | Fichas em `servicos/fora-do-escopo/` e fichas cujo serviço principal está fora da lista oficial ou não aparece nela | Permanecem no digital; não entram no impresso |

A classificação de cada ficha fica em `GRUPOS_FICHAS` do `scripts/gerar_docs.py` (67 núcleo, 25 complementares e 13 de referência) e aparece na coluna *Grupo* do [índice das fichas](../servicos/README.md).

**Sobreposição com a aula:** quando aula e ficha explicam o mesmo mecanismo (ex.: S3), a explicação fica na aula e a ficha remete a ela.

Pode andar em paralelo à Fase 4: cada onda de aulas leva junto as fichas núcleo correspondentes.

## 9. Fase 6 — Exercícios

- Cada questão do `banco_questoes.py` ligada a uma aula (já existe o vínculo por tópico); completar as aulas sem questão: 2.10, 3.1, 3.6, 3.14, 3.15, 3.16, 3.18, 4.1 e 4.6.
- Questões novas no mesmo padrão das questões atuais, que são o ponto forte do material: cenário plausível e comentário das alternativas erradas.
- Sem simulado completo: a dona do repositório decidiu em 06/10/2026 retirar o simulado 01 e não montar o simulado 02. A prática fica nas questões por domínio.
- Tabela de rastreabilidade (AP-13): objetivo do exam guide → aula → questões.

## 10. Fase 7 — Edição impressa

**PR 7.1 — Gerador da edição impressa** (`scripts/gerar_impressa.py`)

Monta o livro a partir dos mesmos Markdown, sem duplicar conteúdo, aplicando transformações só de apresentação:

| Elemento digital | Transformação para papel |
|---|---|
| Navegação (⬅️ ➡️ 🏠) e linha de status | Removidas |
| Links internos | Viram texto ("ver aula 3.10"); links externos viram nota de rodapé |
| `<details>` com respostas | Respostas movidas para o gabarito no fim do caderno |
| Emojis de legenda (🧊 🔄 📌 ✔️) | Marcadores de texto com uma legenda única no início |
| Bloco "Minhas anotações" | Substituído por linhas pautadas no fim de cada aula |
| Mermaid | Renderizado em SVG com `mermaid-cli` |
| Páginas internas (auditoria, fontes, pendências) | Excluídas |

**Ferramentas sugeridas:** Pandoc para Markdown → HTML, e WeasyPrint para HTML → PDF, com um CSS de impressão (`assets/impressao.css`): A4, margens para encadernação, sumário, numeração de páginas e cabeçalho com o capítulo.

**Volumes:** livro-texto (Capítulo 0 e aulas 1.1 a 4.6), caderno de consulta (fichas núcleo) e caderno de exercícios (questões e gabarito comentado). Podem sair como três PDFs ou um único com três partes.

**PR 7.2 — Publicação automática**

- Workflow do GitHub Actions que gera os PDFs a cada tag (`v1.0`, `v1.1`...) e os anexa à release.
- A edição impressa registra na contracapa a data de verificação das informações e o commit de origem.

**Aceite (AP-16):** revisão de uma prova impressa de verdade, em preto e branco, conferindo figuras, tabelas largas, quebras de página e gabarito.

## 11. Fase 8 — Aposentar o gerador de conteúdo

Quando todas as aulas e fichas tiverem `<!-- autoral -->`:

- Remover do fluxo `parse_guia()`, `capitulo_topico()`, `capitulo_servico()`, `Leitura`, `licoes_topicos.py`, `didatica_docs.py`, `aprofundamento.py`, `casos_apostila.py`, `introducoes_servicos.py`, `sequencias_servicos.py`, `vocabulario_apostila.py` e `conteudo_servicos/`.
- `gerar_docs.py` passa a cuidar só de índices, flashcards, resumos e navegação.
- `fontes/` continua como registro histórico, sem papel na geração.
- Atualizar `CLAUDE.md`, templates, plano de estudos e progresso (AP-10, AP-11).

## 12. Riscos e cuidados

| Risco | Cuidado |
|---|---|
| Reescrita longa e cansativa; projeto parar no meio | Migração gradual: o material funciona a cada PR. Ondas pequenas, com o piloto definindo o ritmo realista. |
| Estilo diferente entre aulas | Modelo e checklist fixos; aula-piloto como referência obrigatória de leitura antes de cada onda. |
| Erro técnico introduzido ao reescrever | Conferência em fonte oficial AWS em cada PR; dúvidas vão para pendências de verificação, não para o texto. |
| Perder flashcards na migração | Flashcards de aulas autorais vêm da seção "Revisão"; o PR 0.1 inclui teste de contagem. |
| Mudanças da AWS durante o projeto (planos de suporte, limites) | Números com data de verificação; revisão das aulas do capítulo 4 por último e de novo antes de cada edição impressa. |
| Texto longo sem ganho de entendimento | O objetivo é explicar mecanismo e motivo, não aumentar a contagem de palavras. Métricas não viram meta. |

## 13. Controle das fases

| Fase | Status | PRs | Observações |
|---|---|---|---|
| 0 | Concluída | #21 (marcador autoral) · #22 (métricas) | Linha de base registrada na seção 3 |
| 1 | Concluída | #23 (revisão circular e repetições) · PR 1.1 (vocabulário automático desligado) | Aceite atingido: zero blocos de vocabulário, zero revisões circulares; a única seção "só com texto padrão" é a tabela de labs, escrita à mão |
| 2 | Concluída | #24 (capítulo 0 e aula 0.1) · #25 (aulas 0.2 e 0.3) · #26 (aulas 0.4 e 0.5) · #27 (glossário) · #28 (correções) · flashcards do capítulo 0 | Capítulo 0 completo; glossário com 129 termos; correções após conferir as páginas oficiais inteiras (#28); flashcards do capítulo 0 em `flashcards/capitulo-0.md` |
| 3 | Concluída | #31 (modelo de aula em `templates/topico.md`) · #32 (aula-piloto 2.1) · #52 (ficha-piloto SQS) | Aula-piloto lida e aprovada pela dona do repositório em 06/10/2026 (AP-14). A ficha-piloto do SQS usa o modelo da Fase 5 |
| 4 | Concluída | Onda A concluída: #33 (aulas 2.2 e 2.3) · #34 (2.4 e 2.5) · #35 (2.6 e 2.7) · #36 (2.8 a 2.10). Onda B concluída: #37 (aulas 1.1 e 1.2) · #38 (1.3 e 1.4) · #39 (1.5 a 1.7). Onda C concluída: #40 (aulas 3.1 e 3.2) · #41 (3.3 e 3.4) · #42 (3.5 e 3.6) · #43 (3.7 e 3.8) · #44 (3.9 e 3.10). Onda D concluída: #45 (aulas 3.11 e 3.12) · #46 (3.13 e 3.14) · #47 (3.15 e 3.16) · #48 (3.17 e 3.18). Onda E concluída: #49 (aulas 4.1 e 4.2) · #50 (4.3 e 4.4) · #51 (4.5 e 4.6) | As 46 aulas são autorais. Próxima: fase 5 (fichas) |
| 5 | Em andamento | #52 (modelo de ficha em `templates/servico.md` e ficha-piloto SQS) · #53 (classificação das fichas) · #54 (núcleo de integração: SNS, EventBridge e Step Functions) · #55 (EC2, Auto Scaling, ELB e Lambda) · #56 (ECS, EKS, Fargate e Elastic Beanstalk) · #57 (núcleo de armazenamento: S3, classes do S3, EBS, EFS, Storage Gateway e AWS Backup) · #58 (núcleo de banco de dados: RDS, Aurora, DynamoDB, ElastiCache e Redshift) · #59 (núcleo de redes: VPC, peering e Transit Gateway, VPN, Direct Connect, Route 53, CloudFront, Global Accelerator e API Gateway) · #61 (segurança, identidade e chaves: IAM, Identity Center, Cognito, KMS e Secrets Manager) · #62 (segurança, proteção e detecção: Shield, WAF, GuardDuty, Inspector, Macie, Security Hub e Artifact) · #63 (gerenciamento e governança: CloudWatch, CloudTrail, Config, Systems Manager, CloudFormation, Organizations, Control Tower, Trusted Advisor e Health Dashboard) · #64 (analytics: Athena, Glue, Kinesis e Quick Sight) · #65 (IA: SageMaker AI, Amazon Q e serviços de IA prontos) · #66 (desenvolvimento, migração e custos: CLI e SDKs, Application Migration Service, DMS e SCT, Cost Explorer, Budgets, Pricing Calculator e CUR, planos de suporte e recursos de ajuda) · #67 (complementares, versão curta: ECR, Lightsail, Batch, Outposts, FSx, Elastic Disaster Recovery, DocumentDB e Neptune) · #68 (complementares de segurança e gerenciamento: Directory Service, CloudHSM, Certificate Manager, Firewall Manager, Detective, Service Catalog e RAM, Compute Optimizer e Service Quotas) · #69 (últimas complementares: EMR, OpenSearch, CodeBuild e CodePipeline, X-Ray, Connect, SES, WorkSpaces, Amplify, IoT Core e Migration Hub) | Fichas classificadas (#53). Núcleo reescrito: integração, computação, armazenamento, banco de dados, redes, segurança, gerenciamento, analytics, IA, desenvolvimento, migração e custos. Núcleo concluído (67 fichas). Complementares concluídas (25, versão curta). Próximo: as 13 fichas de referência |
| 6 | Pendente | #60 (simulado 01 retirado e simulado 02 fora do plano) | Decisão da dona do repositório em 06/10/2026; a prática fica nas questões por domínio |
| 7 | Pendente | — | — |
| 8 | Pendente | — | — |

[Voltar às pendências](README.md)
