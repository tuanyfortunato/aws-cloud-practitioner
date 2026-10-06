# Avaliação pedagógica: profundidade, vocabulário e edição impressa

**Status geral:** Pendente — diagnóstico registrado; nenhuma correção implementada.

**Data da avaliação:** 05/10/2026.

**Base avaliada:** `main`, commit `f586aacd9fbfab3112f12e3a8f392839e7cad303`.

**Objetivo:** registrar uma segunda avaliação do material, focada em **profundidade** (explicar sem obrigar o leitor a pesquisar fora) e em evitar o **efeito dicionário** (texto que só define palavras). Complementa a [especificação da apostila digital e impressa](apostila-digital-e-impressa.md) e propõe uma mudança na ordem de execução dos itens AP-01 a AP-16.

**Método:** clonagem do repositório, leitura dos geradores em `scripts/`, leitura integral de aulas e fichas selecionadas (1.1, SQS, planos de suporte, Global Accelerator, simulado 01) e contagens automáticas sobre `docs/` e `servicos/`. Não houve teste com leitores iniciantes nem revalidação linha a linha de preços e quotas.

## 1. Diagnóstico em uma frase

A base técnica é boa, mas o texto das aulas e fichas é **montado automaticamente** a partir de blocos, e é dessa montagem que vem a sensação de dicionário. Melhorar os geradores não produz profundidade; é preciso escrever a explicação à mão e deixar os scripts só com tarefas mecânicas.

## 2. O que está bom e deve ser preservado

- **Simulado:** é a parte mais forte. Questões autorais, cenários plausíveis e explicação de por que cada alternativa errada está errada.
- **Fichas técnicas:** conteúdo denso e correto. A ficha de SQS, por exemplo, cobre visibility timeout, DLQ, Standard × FIFO e o limite de mensagem atualizado.
- **Controle de atualização:** os planos de suporte mostram o modelo do exam guide e a oferta comercial nova lado a lado, com data de verificação.
- **Caso recorrente da escola:** boa escolha pedagógica; dá continuidade entre aulas.
- **Divisão aula → ficha:** ensinar a base na aula e aprofundar na ficha é a estrutura certa.

## 3. Problemas encontrados

### 3.1 O vocabulário automático é o "dicionário"

| Medida | Resultado |
|---|---|
| Blocos "Antes de ler este trecho" em aulas e fichas | 1.349 |
| Palavras nesses blocos nas aulas | ≈ 23 mil de 84 mil (27%) |
| Palavras nesses blocos nas fichas | ≈ 54 mil de 181 mil (30%) |
| Palavras nesses blocos nas páginas de apoio | ≈ 8,6 mil de 18 mil (48%) |

Efeitos observados:

- **Quebra de listas no meio.** Na aula 1.1, o item "IaaS" aparece depois de um bloco que define EC2, EBS, VPC e SO.
- **Conteúdo antecipado.** A primeira aula já define Storage Gateway e Direct Connect, que só serão estudados no capítulo 3.
- **Definições de outro contexto.** Na ficha de SQS, a definição de SSE-KMS fala do S3 e cita "a tabela da seção", que não existe ali. Na aula 1.1, "modelo" é definido com exemplo de modelo de IA.

### 3.2 Definições defensivas, que dizem o que a coisa não é

Nas aulas e fichas, "compatíve(l/is)" aparece 837 vezes e "conforme", 547. As definições evitam errar à custa de não explicar o mecanismo.

**Exemplo atual (Direct Connect):**

> permite estabelecer essa conectividade por conexões e locais compatíveis, com interfaces e rotas configuradas para o ambiente

**Exemplo com profundidade:**

> Uma VPN passa pela internet: sobe rápido e custa pouco, mas a latência oscila junto com o tráfego da internet. O Direct Connect é um circuito físico dedicado entre o seu datacenter e a AWS, sem passar pela internet pública, por isso banda e latência são previsíveis. O custo disso é tempo, porque instalar o circuito leva semanas. E ele não é criptografado por padrão. Por isso a combinação clássica de prova é Direct Connect como caminho principal e VPN como reserva.

O padrão desejado: **o que é, como funciona por dentro, por que existe, qual o custo ou limite, como isso aparece na prova**. Afirmações técnicas novas continuam sujeitas à confirmação em fonte oficial AWS.

### 3.3 A explicação autoral das aulas é curta

O `scripts/licoes_topicos.py` tem 49 linhas para 41 aulas, cerca de dois parágrafos por aula. O restante do corpo vem em bullets do guia original (`fontes/guia-completo-clf-c02.md`), remendados pela lista `CORRECOES` do `gerar_docs.py`. A aula tem aparência de capítulo, mas na prática é um resumo.

### 3.4 Revisão circular

- Nas 41 aulas, as respostas de "Confira se você compreendeu" são cópia literal da abertura "🧠 Antes de começar" da própria aula.
- Nas "Perguntas típicas", o bloco "Fundamento explicado no capítulo" repete a pergunta e a resposta curta (295 ocorrências). Já registrado em AP-02.

### 3.5 Seções com promessa vazia

- Em 39 fichas, "Operação, segurança e custo" tem só o parágrafo padrão (ex.: `servicos/redes/global-accelerator.md`).
- Antes das tabelas aparece sempre o mesmo texto genérico ("Leia cada linha como uma alternativa...").
- Na ficha de SQS, "Como funciona" repete o que "A sequência de funcionamento" acabou de explicar.

### 3.6 Simplificações que confundem

- **Lambda como PaaS** (aula 1.1): a AWS apresenta o Lambda como computação serverless, e "serverless" é a palavra que a prova espera. Tratar como caso à parte, sem encaixá-lo à força em IaaS/PaaS/SaaS.
- **WorkSpaces como SaaS** (aula 1.1): é um desktop virtual; discutível como exemplo principal de SaaS.
- Encaminhar para AP-03, com confirmação em fonte oficial.

### 3.7 Sobreposição entre aula e ficha

Exemplo: S3 tem aula 3.8 (≈ 2,8 mil palavras), ficha `s3.md` (≈ 3,5 mil) e ficha de classes (≈ 2 mil). Definir o que é da aula (entender e decidir) e o que é da ficha (consulta e números) evita repetir a mesma explicação três vezes.

## 4. Edição impressa

### 4.1 Volume

Aulas e fichas somam ≈ 265 mil palavras, algo como 650 páginas A4. Mesmo sem o vocabulário automático, passariam de 450. Proposta de divisão:

| Parte | Conteúdo | Tamanho estimado |
|---|---|---|
| Livro-texto | As 41 aulas reescritas em prosa, mais o capítulo de fundamentos | 150 a 200 páginas |
| Caderno de consulta | Fichas condensadas em uma ou duas páginas, em formato fixo de ficha técnica; sem as fichas "fora do escopo" | A definir após AP-07 |
| Caderno de exercícios | Questões com gabarito comentado no fim, não logo abaixo de cada questão | A definir após AP-09 |

### 4.2 O que quebra no papel

- Links e navegação (➡️, "Índice do domínio").
- `<details>`: a resposta aparece colada na questão ou some, dependendo do conversor.
- Emojis usados como legenda (🧊 🔄 📌 ✔️), ilegíveis em preto e branco; converter para marcadores de texto com legenda única.
- Status 🔴 e bloco "Minhas anotações" dentro de cada aula.
- Páginas internas (auditoria, fontes, pendências), que não interessam a quem estuda.

### 4.3 Figuras essenciais

Não há figuras no núcleo (aulas e fichas). Para o papel, as essenciais são:

- modelo de responsabilidade compartilhada;
- Região, Availability Zone e locais de borda;
- VPC com subnet pública e privada;
- SQS × SNS × EventBridge;
- classes do S3 por frequência de acesso;
- modelos de compra do EC2.

## 5. Mudança proposta na ordem de execução

O AP-01 propõe **corrigir** o vocabulário automático. A recomendação aqui é **desligá-lo**, porque consertar o gerador consome esforço num texto que precisa ser reescrito de qualquer forma.

| Ordem | Ação | Relação com a especificação existente |
|---|---|---|
| 1 | Desligar a injeção automática de vocabulário. Criar um "Capítulo 0 — Fundamentos de TI" (servidor, rede, IP e porta, banco de dados, API, criptografia), definir termos em prosa no primeiro uso e manter um glossário único no fim do livro. | Substitui AP-01; antecipa parte de AP-04. |
| 2 | Escrever uma aula-piloto à mão (sugestão: 2.1 ou 3.10). O Markdown da aula passa a ser a fonte da verdade; os scripts ficam só com índices, flashcards e geração do PDF. | AP-05, com mudança de arquitetura. |
| 3 | Validar o piloto com um leitor iniciante e só então replicar o modelo nas outras 40 aulas e nas fichas. | AP-14, depois AP-06 e AP-07. |
| 4 | Gerar o PDF com Pandoc e um filtro que remove navegação, status e `<details>`, move gabaritos para o fim e converte emojis. | AP-15. |

Mudar a arquitetura (aula escrita à mão como fonte da verdade) exige atualizar as convenções do [CLAUDE.md](../CLAUDE.md) e o `scripts/gerar_docs.py` antes de editar as aulas.

## 6. Critérios de aceite

- Nenhuma aula com blocos de definição gerados automaticamente.
- Cada aula explica mecanismo, motivo e limite de cada conceito central, em prosa, sem depender de pesquisa externa para o entendimento principal.
- Nenhuma pergunta de revisão cuja resposta seja cópia de outro trecho da mesma aula.
- Nenhuma seção com título prometendo conteúdo e só texto padrão.
- Edição impressa sem links, emojis de legenda, status ou respostas ao lado das questões.
- Afirmações técnicas novas confirmadas em fonte oficial AWS ou registradas em [pendências de verificação](../docs/00-guia-do-exame/pendencias-de-verificacao.md).

[Voltar às pendências](README.md)
