<!-- autoral -->

# Amazon SES (Simple Email Service)

> **Categoria:** Aplicações de negócio / e-mail · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** complementar
>
> **Em uma frase:** plataforma de e-mail para enviar e receber mensagens com os endereços e domínios da própria empresa: transacionais, de marketing e boletins.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.14 Aplicações de negócio, usuário final, front-end e IoT](../../docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Como funciona

Os e-mails de confirmação de matrícula às vezes caem no spam, e manter um servidor de e-mail exige cuidar da rede e da reputação dos endereços IP. O **Amazon SES** é a plataforma de e-mail da AWS: a escola envia com o próprio domínio, sem montar essa infraestrutura.

1. A escola configura e verifica o domínio ou o endereço que vai enviar.
2. A aplicação envia os e-mails pelo SDK, pela interface SMTP ou pela API do SES.
3. Seguem e-mails transacionais (confirmação de matrícula), de marketing (convite para um evento) e boletins.
4. Para e-mails recebidos, o SES pode acionar software, como respostas automáticas ou abertura de chamados.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [Amazon SNS](../integracao/sns.md) | Notificação simples por e-mail a quem assinou um tópico | "Avisar assinantes", "tópico" |
| [Amazon Connect](amazon-connect.md) | Central de atendimento por voz e chat | "Call center" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
