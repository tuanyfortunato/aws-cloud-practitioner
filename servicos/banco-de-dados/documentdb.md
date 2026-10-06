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

## 1. A sequência de funcionamento

**Passo 1.** Avalie as operações e estruturas que sua aplicação usa na interface de documentos.

**Passo 2.** Prepare um ambiente compatível e grave registros estruturados. A aplicação consulta campos e documentos por suas operações.

**Passo 3.** Teste as diferenças de compatibilidade e planeje cópias e acessos. O nome documento não significa armazenar qualquer arquivo PDF como num bucket.

## 2. Recursos e opções, com significado

### Destaques

Arquitetura parecida com a do Aurora: armazenamento distribuído (6 cópias em 3 AZs), até 15 réplicas, backups contínuos, criptografia.

Opções *instance-based* e *elastic clusters* (sharding para milhões de leituras/escritas); Global Clusters.

Uso: catálogos, perfis, gerenciamento de conteúdo, migração de MongoDB para serviço gerenciado.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Compatibilidade com MongoDB não significa identidade em todas as funções e versões. Ele não é um serviço para simplesmente guardar PDFs como arquivos.

## 4. Caso resolvido: ligando as peças

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

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Migrar banco MongoDB para um serviço gerenciado."

**Resposta curta:** DocumentDB.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
