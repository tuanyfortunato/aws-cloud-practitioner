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

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.
- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.

**Passo 1.** Verifique a identidade de envio e prepare as condições de acesso e volume aplicáveis.

**Passo 2.** Faça a aplicação solicitar o envio de uma mensagem com conteúdo e destinatário pertinentes.

**Passo 3.** Acompanhe devoluções, reclamações e reputação. Aceitar uma solicitação de envio não garante chegada à caixa principal do destinatário.

## 2. Recursos e opções, com significado

### Configurações importantes

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **SNS:** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis.
- **virtual:** Um recurso virtual é criado por software sobre equipamentos físicos. VM significa máquina virtual: computador lógico com sistema operacional e recursos de processamento.
- **autenticação:** Verificação de quem está acessando. Confirmar a identidade não autoriza qualquer ação no sistema.
- **DKIM / SPF / DMARC:** Mecanismos de autenticação e política para e-mail que ajudam a validar origem e tratar mensagens. Não garantem chegada de toda mensagem à caixa principal.
- **SMTP:** Protocolo para envio e transferência de e-mail. Usar o protocolo não dispensa identidade verificada, permissões e regras do serviço de envio.

| Item | Detalhe |
|---|---|
| **Sandbox** | Contas novas só enviam para endereços verificados, com limites baixos — pedir saída do sandbox para produção. |
| **Identidades** | Verificar domínio/e-mail; autenticação **SPF, DKIM, DMARC**. |
| **Envio** | API, SMTP, templates; **IPs dedicados** opcionais. |
| **Reputação** | Painel de bounces e reclamações; *Virtual Deliverability Manager*. |
| **Recebimento** | Regras para gravar no S3, acionar Lambda/SNS. |
| **Mail Manager** | Roteamento e arquivamento de e-mail corporativo. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele não garante que qualquer mensagem chegará à caixa de entrada. Verificação de identidade, limites, reputação e tratamento de devoluções importam. Também não é uma caixa postal pessoal completa.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **SES:** SES oferece envio de e-mail para aplicações, com recursos de identidade, acompanhamento e controle de envio.

**SES** (e-mails ricos/formatados em volume) × **SNS** (notificações simples para vários canais) × **WorkMail** (caixa de e-mail corporativa).

## 4. Caso resolvido: ligando as peças

O sistema da escola envia uma confirmação de matrícula usando uma identidade autorizada no SES.

**Aplicando a sequência à situação:**

**Etapa 1:** Verifique a identidade de envio e prepare as condições de acesso e volume aplicáveis.
**Etapa 2:** Faça a aplicação solicitar o envio de uma mensagem com conteúdo e destinatário pertinentes.
**Etapa 3:** Acompanhe devoluções, reclamações e reputação. Aceitar uma solicitação de envio não garante chegada à caixa principal do destinatário.

**Resultado e responsabilidade:** SES oferece envio de e-mail para aplicações, com recursos de identidade, acompanhamento e controle de envio.

**Recursos envolvidos:** Identidades verificadas, envio SMTP/API e eventos.

**Decisões que precisam ser tomadas:** Domínio/remetente, acesso, limites e saída do sandbox.

**Outra situação comentada:** Confirmação de compra por e-mail: SES; caixa de entrada pessoal não é o objetivo principal.

**Por que não concluir mais do que isso:** Sandbox restringe envio; verificar domínio não garante entrega na caixa principal

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Enviar e-mails de confirmação e marketing em massa."

**Resposta curta:** SES.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
