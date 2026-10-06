<!-- autoral -->

# Amazon QuickSight (Amazon Quick Sight)

> **Categoria:** Analytics e inteligência de negócios (BI) · **Domínio:** 3 · **Abrangência:** Regional (conta) · **Ficha:** núcleo
>
> **Em uma frase:** serviço de visualização de dados e BI que se conecta às fontes, cria painéis interativos e permite incorporar análises em aplicações; hoje faz parte do Amazon Quick.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.11 Analytics](../../docs/03-tecnologia-e-servicos/11-analytics.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

A direção da rede quer acompanhar as matrículas por unidade, as faltas por turma e os acessos ao site. Hoje, alguém da TI roda consultas, cola os números numa planilha e envia por e-mail toda segunda-feira, e cada diretor recebe uma versão diferente.

O **Quick Sight** transforma esses números em **painéis** (*dashboards*) interativos. Ele se conecta às fontes, como Athena, Redshift, RDS e arquivos no S3, e os **autores** montam gráficos e relatórios que os **leitores** acessam e filtram pelo navegador. Os dados podem ser importados para o **SPICE**, o motor em memória do Quick Sight, que responde rápido a muitos usuários. O Quick Sight também responde a perguntas em linguagem natural sobre os dados e permite incorporar painéis em aplicações, como o portal da escola. Ele faz parte do **Amazon Quick**, um serviço com IA que também automatiza tarefas.

O limite: o Quick Sight mostra os dados, mas não os prepara nem os guarda em grande escala. A limpeza é do [Glue](glue.md), e as consultas pesadas são do [Athena](athena.md) ou do [Redshift](../banco-de-dados/redshift.md).

## Como funciona

1. Um autor conecta o Quick Sight às fontes de dados.
2. Opcionalmente, os dados são importados para o SPICE.
3. O autor monta análises e publica painéis.
4. Os leitores acessam os painéis no navegador, ou incorporados numa aplicação, e filtram ou perguntam em linguagem natural.

## Opções principais

| Peça | O que faz | Exemplo na escola |
|---|---|---|
| Autor | Conecta dados, cria painéis e relatórios | Equipe de TI monta o painel de matrículas |
| Leitor | Vê e filtra os painéis | Diretores de cada unidade |
| SPICE | Motor em memória para respostas rápidas | Painel aberto por muitos ao mesmo tempo |
| Perguntas em linguagem natural | Responde perguntas sobre os dados | "Quantas matrículas em janeiro?" |
| Painéis incorporados | Análises dentro de outra aplicação | Painel no portal da escola |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Autor | US$ 24 por usuário por mês | 06/10/2026 |
| Leitor | A partir de US$ 3 por mês | 06/10/2026 |
| SPICE incluído | 10 GB por autor | 06/10/2026 |

## Como é cobrado

Há dois modelos: por usuário, com autores e leitores cobrados por mês, e por capacidade, comprando sessões de leitura em bloco sem cadastrar cada leitor. Cada autor inclui 10 GB de SPICE; o espaço extra é cobrado por GB por mês.

## Não confundir com

| Serviço | Diferença para o Quick Sight | Pista no enunciado |
|---|---|---|
| [Amazon Athena](athena.md) | Consulta os dados com SQL | "SQL no S3" |
| [Amazon Redshift](../banco-de-dados/redshift.md) | Data warehouse que guarda e consulta os dados | "Data warehouse" |
| [Amazon CloudWatch](../gerenciamento/cloudwatch.md) | Painéis de métricas de funcionamento | "CPU", "alarme" |
| [Amazon OpenSearch Service](opensearch.md) | Busca e análise de logs | "Busca de texto", "logs" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/what-is.html)
- [Fontes de dados aceitas](https://docs.aws.amazon.com/quick/latest/userguide/supported-data-sources.html)
- [Preços do Amazon Quick Sight](https://aws.amazon.com/quicksight/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
