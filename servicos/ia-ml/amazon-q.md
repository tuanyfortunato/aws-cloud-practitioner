# Amazon Q

> **Categoria:** IA generativa / assistentes · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.12 IA e machine learning](../../docs/03-tecnologia-e-servicos/12-ia-e-machine-learning.md)
>
> **Em uma frase:** família de **assistentes de IA generativa** prontos para desenvolvedores e para dados corporativos.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é um **assistente de IA pronto para usar**: ajuda desenvolvedores a programar e funcionários a encontrar respostas.

- ✅ **Escolha quando:** o enunciado pede um **assistente de IA generativa pronto**, para código ou para a empresa.
- 🚫 **Não é a resposta quando:** quer **construir a sua própria aplicação** de IA → [Bedrock](bedrock.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "assistente de IA", "gerar código na IDE", "perguntas sobre os dados da empresa".
<!-- didatico:fim -->

## Variantes

| Variante | Para quem | O que faz |
|---|---|---|
| **Amazon Q Developer** (✔️ o CodeWhisperer passou a integrá-lo em 30/04/2024) | Desenvolvedores e times de operação | Sugestões e geração de código na IDE e CLI, agentes que implementam funcionalidades, **varredura de segurança**, upgrade de código (ex.: Java), explicar e diagnosticar recursos e **erros no console AWS**, chat sobre a conta. |
| **Amazon Q Business** | Funcionários | Responde perguntas, resume e gera conteúdo com base nos **dados da empresa** (40+ conectores: S3, SharePoint, Confluence, Salesforce), respeitando permissões. |
| **Amazon Q in QuickSight** | Analistas | BI em linguagem natural. |
| **Amazon Q in Connect** | Agentes de contact center | Respostas e ações sugeridas em tempo real. |

## 🔄 Atualizações 2025-2026

- ✔️ Os **plugins de IDE do Amazon Q Developer** têm fim de suporte em **30/04/2027**; a documentação aponta o **Kiro** como alternativa.
- **Amazon Q Business** entrou em manutenção e **não aceita novos clientes desde 30/07/2026**; aplicações existentes podem ser **conectadas** ao Amazon Quick Suite. O **Amazon Q** continua na lista oficial: "assistente de IA generativa para funcionários/desenvolvedores" → **Amazon Q**.

## ❓ Perguntas típicas

- "Assistente de IA generativa para escrever código na IDE." → Amazon Q Developer.
- "Assistente que responde com base nos documentos internos da empresa." → Amazon Q Business.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Variantes voltadas a desenvolvimento e ao uso de informações de negócio |
| **O que você decide/configura?** | Variante, identidades, fontes e permissões |
| **Em que ordem as coisas acontecem?** | Configure acesso e contexto apropriados; usuário recebe assistência |
| **O que pode fazer, e em que condição?** | Ajuda em código/tarefas ou busca contextual conforme variante |
| **O que não pode presumir?** | Não é um único banco com acesso automático a todos os documentos da empresa |

**Caso comentado:** Apoio ao desenvolvedor: Q Developer; informações de negócio dependem da variante e das fontes autorizadas.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Amazon Q](https://aws.amazon.com/q/)
