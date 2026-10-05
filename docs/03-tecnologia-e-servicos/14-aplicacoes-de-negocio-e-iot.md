# 3.14 Aplicações de negócio, usuário final, front-end e IoT

## 🧠 Antes de começar

**Qual é a dificuldade?** Uma organização pode precisar atender pessoas, enviar e-mails, oferecer trabalho remoto ou conectar equipamentos. Cada necessidade vai além de criar uma máquina.

**A ideia em palavras simples:** Este tópico reúne serviços voltados a experiências e aplicações específicas. É importante reconhecer o problema de cada produto, e não memorizar a categoria como se fosse um serviço só.

**Exemplo do dia a dia:** A escola pode usar um serviço de e-mail para confirmações e uma plataforma de atendimento para a secretaria. Sensores conectados exigem outro conjunto de recursos.

**O que não concluir?** Um serviço pronto continua exigindo configuração, identidade e integração. As ferramentas desta seção não substituem umas às outras.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Contact center** | central de atendimento (telefone, chat). |
| **DaaS** | desktop como serviço. |
| **IoT** | internet das coisas: sensores e dispositivos conectados. |

---

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon Connect](../../servicos/aplicacoes/amazon-connect.md) · [Amazon SES (Simple Email Service)](../../servicos/aplicacoes/ses.md) · [Amazon WorkSpaces, AppStream 2.0 e WorkSpaces Secure Browser](../../servicos/aplicacoes/workspaces-e-appstream.md) · [AWS Amplify, AWS AppSync e AWS Device Farm](../../servicos/aplicacoes/amplify-e-appsync.md) · [AWS IoT Core, IoT Greengrass e outros serviços de IoT](../../servicos/aplicacoes/iot-core-e-greengrass.md)

> ⚠️ **Atualização do exam guide (verificado em 04/10/2026):** No escopo: Connect, SES, AppStream 2.0, WorkSpaces, WorkSpaces Secure Browser, **Amplify** e **IoT Core**. AppSync não aparece na lista atual. [Ver escopo oficial](../00-guia-do-exame/escopo-oficial.md).

⬅️ [3.13 Integração de aplicações](13-integracao-de-aplicacoes.md) · 🏠 [Índice do domínio](README.md) · [3.15 Ferramentas de desenvolvimento](15-ferramentas-de-desenvolvimento.md) ➡️

---

## 1. Entenda as peças e a relação entre elas


Um serviço de aplicação normalmente já oferece uma função do negócio, como atendimento ou envio de mensagens, mas ainda precisa de configuração e integração. A empresa define identidades, conteúdo e os sistemas relacionados àquela experiência.

Não confunda e-mail de uma aplicação com caixa postal de funcionários, nem transmissão de software com armazenamento de arquivos. Dispositivos físicos também precisam de software e proteção. Cada produto abaixo atende uma necessidade concreta diferente.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é uma **caixa de ferramentas de escritório**: o **Connect** é a central telefônica; o **SES**, o correio; o **WorkSpaces**, o computador de trabalho na nuvem; o **Amplify**, um kit para montar apps; o **IoT Core**, a central que recebe mensagens dos sensores.

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **Amazon Connect / Connect:** Amazon Connect oferece uma plataforma de contact center em nuvem com canais e recursos compatíveis.


**Amazon Connect:** **central de atendimento (contact center) na nuvem**, com voz, chat e tarefas, pago por uso.

**Antes de ler este trecho:**

- **SNS:** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis.
- **Amazon SES / SES:** SES oferece envio de e-mail para aplicações, com recursos de identidade, acompanhamento e controle de envio.
- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.


**Amazon SES (Simple Email Service):** envio de **e-mails** transacionais e de marketing em grande volume. Diferença para o SNS: SES é para e-mails formatados a clientes; SNS é para notificações simples.


**Amazon WorkSpaces:** **desktops virtuais** (DaaS) Windows ou Linux, acessados de qualquer dispositivo.

**Antes de ler este trecho:**

- **streaming:** Fluxo contínuo de dados ou mídia. É diferente de esperar um arquivo completo antes de iniciar o trabalho.


**Amazon AppStream 2.0:** **streaming de aplicações** de desktop para o navegador, sem entregar o desktop inteiro.

**Antes de ler este trecho:**

- **VPN:** Conexão lógica protegida que liga usuários ou redes. Um túnel VPN não concede automaticamente acesso a todos os recursos do destino.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.


**Amazon WorkSpaces Secure Browser:** navegador seguro gerenciado para acessar sites internos sem VPN.

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.


**AWS Amplify:** ferramentas para **criar, implantar e hospedar** aplicações web e mobile full-stack rapidamente.

**Antes de ler este trecho:**

- **GraphQL:** Forma de definir uma API e solicitar campos de dados. A aplicação ainda precisa de lógica de resolução, acesso e fontes adequadas.


**AWS AppSync:** **APIs GraphQL** gerenciadas, com dados em tempo real e sincronização offline.

**Antes de ler este trecho:**

- **protocolo:** Conjunto de regras da comunicação. Um protocolo define o formato e o comportamento da troca; produtos precisam ser compatíveis com ele.
- **IoT:** Dispositivos físicos conectados que enviam informações ou recebem comandos. Conexão não substitui autenticação, software e análise dos dados.
- **MQTT:** Protocolo de mensagens comum em dispositivos conectados. Aplicação, tópicos e permissões precisam ser definidos para a comunicação desejada.


**AWS IoT Core:** conecta **dispositivos IoT** à nuvem (protocolo MQTT) com segurança e em grande escala.


**Cai na prova:** "call center" = Connect; "funcionários remotos precisam de um desktop" = WorkSpaces; "rodar um app de desktop no navegador" = AppStream 2.0; "sensores enviando dados" = IoT Core.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **servidor:** Computador que atende pedidos de outros computadores. Um servidor web, por exemplo, responde aos pedidos enviados pelo navegador.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **back-end:** Parte que processa regras e dados de uma aplicação. É diferente da interface que a pessoa vê no navegador ou aplicativo.


**Primeiro, identifique o funcionamento:** Connect organiza atendimento; SES envia e-mails; WorkSpaces entrega desktops; AppStream entrega aplicações por streaming; Secure Browser entrega navegação isolada; IoT Core conecta dispositivos.

**Depois, compare as escolhas:** Diferencie aplicação corporativa pronta, capacidade para executar servidor e conexão de dispositivo. Amplify ajuda a construir e implantar aplicações web/mobile.

**Por fim, verifique o limite:** SES não é uma caixa de e-mail de uso pessoal. Desktop remoto não é um servidor EC2 de back-end. IoT Core não instala sensores nem resolve a conectividade física do dispositivo.

## 4. Caso resolvido

Funcionários precisam de desktop completo, e clientes precisam receber confirmação por e-mail. Quais serviços?

**Raciocínio e resposta:** WorkSpaces para os desktops; SES para o envio de e-mail pela aplicação. São necessidades independentes.

A resposta muda se mudar o requisito destacado. Compare a necessidade com a função da solução, em vez de apenas associar duas palavras.

## 5. Revisão do capítulo

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Uma organização pode precisar atender pessoas, enviar e-mails, oferecer trabalho remoto ou conectar equipamentos. Cada necessidade vai além de criar uma máquina.

**2. O que a solução fornece?**

Este tópico reúne serviços voltados a experiências e aplicações específicas. É importante reconhecer o problema de cada produto, e não memorizar a categoria como se fosse um serviço só.

**3. Que conclusão seria incorreta?**

Um serviço pronto continua exigindo configuração, identidade e integração. As ferramentas desta seção não substituem umas às outras.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

**Objetivos de aprendizagem:**

- [ ] Ligar cada serviço ao cenário: call center → Connect; e-mails → SES; desktop virtual → WorkSpaces.
- [ ] Diferenciar **WorkSpaces** (desktop inteiro) de **AppStream 2.0** (só o aplicativo no navegador).
- [ ] Diferenciar **SES** (e-mails formatados a clientes) de **SNS** (notificações simples).

**Dica de revisão para a prova:** "Call center" → **Connect**. "Funcionário remoto precisa de desktop" → **WorkSpaces**. "App de desktop no navegador" → **AppStream 2.0**. "Sensores" → **IoT Core**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).
**Pergunta:** "Criar uma central de atendimento na nuvem."

**Resposta curta:** Amazon Connect.


**Fundamento explicado no capítulo:** "Criar uma central de atendimento na nuvem." → Amazon Connect.

**Pergunta:** "Enviar e-mails de confirmação e marketing em massa."

**Resposta curta:** SES.


**Fundamento explicado no capítulo:** "Enviar e-mails de confirmação e marketing em massa." → SES.

**Pergunta:** "Oferecer desktops virtuais a funcionários remotos."

**Resposta curta:** WorkSpaces.


**Fundamento explicado no capítulo:** "Oferecer desktops virtuais a funcionários remotos." → WorkSpaces.

**Pergunta:** "Disponibilizar um aplicativo de desktop pelo navegador."

**Resposta curta:** AppStream 2.0.


**Fundamento explicado no capítulo:** "Disponibilizar um aplicativo de desktop pelo navegador." → AppStream 2.0.

**Pergunta:** "Criar e hospedar rapidamente um app web ou mobile full-stack."

**Resposta curta:** Amplify.


**Fundamento explicado no capítulo:** "Criar e hospedar rapidamente um app web ou mobile full-stack." → Amplify.

**Pergunta:** "API GraphQL gerenciada com dados em tempo real."

**Resposta curta:** AppSync.

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.


**Fundamento explicado no capítulo:** "API GraphQL gerenciada com dados em tempo real." → AppSync.

**Pergunta:** "Conectar milhões de sensores à nuvem."

**Resposta curta:** IoT Core.


**Fundamento explicado no capítulo:** "Conectar milhões de sensores à nuvem." → IoT Core.

<!-- extra:inicio -->
## 🔄 Atualizações 2025-2026 e detalhes extras

> Fonte: [pesquisa de atualizações](../../fontes/pesquisa-atualizacoes-2025-2026.md). Legenda: 📌 decorar · 🔄 mudou recentemente · ⚠️ pegadinha · 🧊 não precisa decorar.

- **IoT:** IoT Core (conectar dispositivos e trocar mensagens MQTT) × **IoT Greengrass** (rodar Lambda e ML localmente no dispositivo de borda).
- 🔄 IoT Analytics encerrado em 15/12/2025 e IoT Events em 20/05/2026 — não estudar. Na prova, IoT = **só IoT Core** (Greengrass está fora do escopo).
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.13 Integração de aplicações](13-integracao-de-aplicacoes.md) · 🏠 [Índice do domínio](README.md) · [3.15 Ferramentas de desenvolvimento](15-ferramentas-de-desenvolvimento.md) ➡️
