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

## Destaques

- Arquitetura parecida com a do Aurora: armazenamento distribuído (6 cópias em 3 AZs), até 15 réplicas, backups contínuos, criptografia.
- Opções *instance-based* e *elastic clusters* (sharding para milhões de leituras/escritas); Global Clusters.
- Uso: catálogos, perfis, gerenciamento de conteúdo, migração de MongoDB para serviço gerenciado.

## ❓ Perguntas típicas

- "Migrar banco MongoDB para um serviço gerenciado." → DocumentDB.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Cluster de documentos, instâncias, endpoints e índices |
| **O que você decide/configura?** | Versão/API compatível, rede, capacidade e backup |
| **Em que ordem as coisas acontecem?** | Aplicação usa driver/operações compatíveis para guardar e consultar documentos |
| **O que pode fazer, e em que condição?** | Atende modelo documental com compatibilidade anunciada com MongoDB |
| **O que não pode presumir?** | Compatibilidade não garante todos os recursos ou comportamento do MongoDB |

**Caso comentado:** Migrar aplicação documental: valide as operações usadas; não suponha migração sem teste só por usar driver semelhante.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html)
