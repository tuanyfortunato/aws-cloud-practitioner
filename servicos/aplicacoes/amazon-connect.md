# Amazon Connect

> **Categoria:** Aplicações de negócio / contact center · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.14 Aplicações de negócio, usuário final, front-end e IoT](../../docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md)
>
> **Em uma frase:** **central de atendimento (contact center) omnicanal na nuvem**, pronta em minutos e paga por uso.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é uma **central de atendimento pronta na nuvem**: telefone, chat e URA sem comprar equipamento.

- ✅ **Escolha quando:** precisa criar um **contact center**.
- 🚫 **Não é a resposta quando:** precisa só de um **chatbot** → Lex, na ficha de [serviços de IA prontos](../ia-ml/servicos-de-ia-prontos.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "call center", "contact center", "central de atendimento".
<!-- didatico:fim -->

## Destaques

- Canais: **voz** (números de telefone, URA), **chat**, **SMS**, **tarefas**, e-mail.
- **Fluxos de contato** visuais (drag-and-drop), roteamento por habilidade.
- IA integrada: **Lex** (bots/URA conversacional), **Amazon Q in Connect** (assistência ao agente), **Contact Lens** (análise de sentimento e transcrição de chamadas), previsão e escala de agentes.
- Perfis de clientes, casos, campanhas de saída.
- Cobrança **por minuto de uso**/mensagem, sem licenças por agente nem compromisso.

## ❓ Perguntas típicas

- "Criar uma central de atendimento na nuvem." → Amazon Connect.
- "Exemplo de SaaS da AWS." → Amazon Connect.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Instância, contact flows, queues, routing profiles e agentes |
| **O que você decide/configura?** | Canais, atendimento, gravação e integrações |
| **Em que ordem as coisas acontecem?** | Contato entra no fluxo e é encaminhado ao atendimento configurado |
| **O que pode fazer, e em que condição?** | Oferece contact center gerenciado |
| **O que não pode presumir?** | Não substitui equipe de atendimento nem autoriza automaticamente gravações/uso de dados |

**Caso comentado:** Criar central de atendimento: Connect; envio transacional de e-mail: SES.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Amazon Connect](https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html)
