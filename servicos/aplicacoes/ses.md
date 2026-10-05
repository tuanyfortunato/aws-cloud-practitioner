# Amazon SES (Simple Email Service)

> **Categoria:** Aplicações de negócio / e-mail · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.14 Aplicações de negócio, usuário final, front-end e IoT](../../docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md)
>
> **Em uma frase:** envio (e recebimento) de **e-mails** transacionais e de marketing em grande volume.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é uma **agência de correio para e-mails em massa**: confirmações, avisos e marketing.

- ✅ **Escolha quando:** precisa enviar **e-mails transacionais ou de marketing** em volume.
- 🚫 **Não é a resposta quando:** precisa de **notificações simples** para vários canais → [SNS](../integracao/sns.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "enviar e-mails", "e-mail marketing", "e-mails de confirmação".
<!-- didatico:fim -->

## Configurações importantes

| Item | Detalhe |
|---|---|
| **Sandbox** | Contas novas só enviam para endereços verificados, com limites baixos — pedir saída do sandbox para produção. |
| **Identidades** | Verificar domínio/e-mail; autenticação **SPF, DKIM, DMARC**. |
| **Envio** | API, SMTP, templates; **IPs dedicados** opcionais. |
| **Reputação** | Painel de bounces e reclamações; *Virtual Deliverability Manager*. |
| **Recebimento** | Regras para gravar no S3, acionar Lambda/SNS. |
| **Mail Manager** | Roteamento e arquivamento de e-mail corporativo. |

## ⚠️ Não confundir

- **SES** (e-mails ricos/formatados em volume) × **SNS** (notificações simples para vários canais) × **WorkMail** (caixa de e-mail corporativa).

## ❓ Perguntas típicas

- "Enviar e-mails de confirmação e marketing em massa." → SES.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Identidades verificadas, envio SMTP/API e eventos |
| **O que você decide/configura?** | Domínio/remetente, acesso, limites e saída do sandbox |
| **Em que ordem as coisas acontecem?** | Aplicação envia mensagem; serviço reporta entrega/bounce conforme configuração |
| **O que pode fazer, e em que condição?** | Envia e-mails transacionais e de campanha nas condições da oferta |
| **O que não pode presumir?** | Sandbox restringe envio; verificar domínio não garante entrega na caixa principal |

**Caso comentado:** Confirmação de compra por e-mail: SES; caixa de entrada pessoal não é o objetivo principal.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html)
