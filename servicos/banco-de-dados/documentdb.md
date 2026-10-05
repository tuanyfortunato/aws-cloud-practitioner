# Amazon DocumentDB (compatível com MongoDB)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A aplicação guarda registros como documentos com vários campos e precisa de um banco com interface compatível com parte do ecossistema MongoDB.

**Como este serviço ajuda?** DocumentDB armazena e consulta documentos, como registros estruturados de produtos. A AWS gerencia a infraestrutura do banco conforme a oferta.

**Exemplo do dia a dia:** Um catálogo guarda, em cada documento, o nome do produto, características e outras informações. A equipe avalia a compatibilidade das consultas antes de usar DocumentDB.

**O que ele não resolve sozinho?** Compatibilidade com MongoDB não significa identidade em todas as funções e versões. Ele não é um serviço para simplesmente guardar PDFs como arquivos.

**Primeiras palavras para entender:**

- **Documento:** registro estruturado com campos.
- **Campo:** informação nomeada dentro do registro.
- **Compatibilidade:** suporte às interfaces esperadas pela aplicação.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Banco de documentos · **Domínio:** 3 · **Escopo:** Regional (cluster multi-AZ) · **Tópico do guia:** [3.7 Bancos de dados](../../docs/03-tecnologia-e-servicos/07-bancos-de-dados.md)
>
> **Em uma frase:** banco de documentos JSON gerenciado, compatível com as APIs e drivers do MongoDB.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **bucket:** Recipiente que organiza objetos no S3. A aplicação usa o bucket e a identificação do objeto para pedir operações autorizadas.
- **PDF:** Formato de documento. Um serviço de extração analisa conteúdo compatível; guardar um PDF num bucket não executa automaticamente essa análise.


**Passo 1.** Avalie as operações e estruturas que sua aplicação usa na interface de documentos.

**Passo 2.** Prepare um ambiente compatível e grave registros estruturados. A aplicação consulta campos e documentos por suas operações.

**Passo 3.** Teste as diferenças de compatibilidade e planeje cópias e acessos. O nome documento não significa armazenar qualquer arquivo PDF como num bucket.

## 2. Recursos e opções, com significado

### Destaques

**Antes de ler este trecho:**

- **Aurora:** Aurora é um banco relacional da AWS dentro da família RDS.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.


Arquitetura parecida com a do Aurora: armazenamento distribuído (6 cópias em 3 AZs), até 15 réplicas, backups contínuos, criptografia.

**Antes de ler este trecho:**

- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.


Opções *instance-based* e *elastic clusters* (sharding para milhões de leituras/escritas); Global Clusters.

**Antes de ler este trecho:**

- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.


Uso: catálogos, perfis, gerenciamento de conteúdo, migração de MongoDB para serviço gerenciado.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

**Antes de ler este trecho:**

- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.


Compatibilidade com MongoDB não significa identidade em todas as funções e versões. Ele não é um serviço para simplesmente guardar PDFs como arquivos.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

## 5. Caso resolvido: ligando as peças

Um catálogo guarda, em cada documento, o nome do produto, características e outras informações. A equipe avalia a compatibilidade das consultas antes de usar DocumentDB.

**Aplicando a sequência à situação:**

**Etapa 1:** Avalie as operações e estruturas que sua aplicação usa na interface de documentos.
**Etapa 2:** Prepare um ambiente compatível e grave registros estruturados. A aplicação consulta campos e documentos por suas operações.
**Etapa 3:** Teste as diferenças de compatibilidade e planeje cópias e acessos. O nome documento não significa armazenar qualquer arquivo PDF como num bucket.

**Resultado e responsabilidade:** DocumentDB armazena e consulta documentos, como registros estruturados de produtos. A AWS gerencia a infraestrutura do banco conforme a oferta.

**Recursos envolvidos:** Cluster de documentos, instâncias, endpoints e índices.

**Decisões que precisam ser tomadas:** Versão/API compatível, rede, capacidade e backup.


**Outra situação comentada:** Migrar aplicação documental: valide as operações usadas; não suponha migração sem teste só por usar driver semelhante.

**Por que não concluir mais do que isso:** Compatibilidade não garante todos os recursos ou comportamento do MongoDB

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

A aplicação guarda registros como documentos com vários campos e precisa de um banco com interface compatível com parte do ecossistema MongoDB.

**2. O que a solução fornece?**

DocumentDB armazena e consulta documentos, como registros estruturados de produtos. A AWS gerencia a infraestrutura do banco conforme a oferta.

**3. Que conclusão seria incorreta?**

Compatibilidade com MongoDB não significa identidade em todas as funções e versões. Ele não é um serviço para simplesmente guardar PDFs como arquivos.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Migrar banco MongoDB para um serviço gerenciado."

**Resposta curta:** DocumentDB.

**Antes de ler este trecho:**

- **DocumentDB:** DocumentDB armazena e consulta documentos, como registros estruturados de produtos.


**Fundamento explicado no capítulo:** "Migrar banco MongoDB para um serviço gerenciado." → DocumentDB.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
