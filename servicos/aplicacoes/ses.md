# Amazon SES (Simple Email Service)

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

## 🔗 Documentação oficial

- [Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html)
