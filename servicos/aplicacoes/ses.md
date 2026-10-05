# Amazon SES (Simple Email Service)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Uma aplicação precisa enviar mensagens por e-mail, como confirmações e avisos, sem construir sua própria infraestrutura de envio.

**Como este serviço ajuda?** SES oferece envio de e-mail para aplicações, com recursos de identidade, acompanhamento e controle de envio.

**Exemplo do dia a dia:** O sistema da escola envia uma confirmação de matrícula usando uma identidade autorizada no SES.

**O que ele não resolve sozinho?** Ele não garante que qualquer mensagem chegará à caixa de entrada. Verificação de identidade, limites, reputação e tratamento de devoluções importam. Também não é uma caixa postal pessoal completa.

**Primeiras palavras para entender:**

- **Identidade:** endereço ou domínio autorizado.
- **Bounce:** mensagem devolvida.
- **Reputação:** avaliação do comportamento de envio.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Aplicações de negócio / e-mail · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.14 Aplicações de negócio, usuário final, front-end e IoT](../../docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md)
>
> **Em uma frase:** envio (e recebimento) de **e-mails** transacionais e de marketing em grande volume.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

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
