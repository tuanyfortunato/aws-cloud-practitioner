# 3.14 Aplicações de negócio, usuário final, front-end e IoT

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Amazon Connect](../../servicos/aplicacoes/amazon-connect.md) · [Amazon SES (Simple Email Service)](../../servicos/aplicacoes/ses.md) · [Amazon WorkSpaces, AppStream 2.0 e WorkSpaces Secure Browser](../../servicos/aplicacoes/workspaces-e-appstream.md) · [AWS Amplify, AWS AppSync e AWS Device Farm](../../servicos/aplicacoes/amplify-e-appsync.md) · [AWS IoT Core, IoT Greengrass e outros serviços de IoT](../../servicos/aplicacoes/iot-core-e-greengrass.md)

> ⚠️ **Atualização do exam guide (verificado em 04/10/2026):** No escopo: Connect, SES, AppStream 2.0, WorkSpaces, WorkSpaces Secure Browser, **Amplify** e **IoT Core**. AppSync não aparece na lista atual. [Ver escopo oficial](../00-guia-do-exame/escopo-oficial.md).

⬅️ [3.13 Integração de aplicações](13-integracao-de-aplicacoes.md) · 🏠 [Índice do domínio](README.md) · [3.15 Ferramentas de desenvolvimento](15-ferramentas-de-desenvolvimento.md) ➡️

---

## 🧠 Antes de começar

> 💡 **Em palavras simples:** São serviços **prontos para o negócio**: central de atendimento, envio de e-mails, desktops virtuais, criação de apps e conexão de dispositivos IoT.
>
> 🏠 **Analogia:** é uma **caixa de ferramentas de escritório**: o **Connect** é a central telefônica; o **SES**, o correio; o **WorkSpaces**, o computador de trabalho na nuvem; o **Amplify**, um kit para montar apps; o **IoT Core**, a central que recebe mensagens dos sensores.

**Ao terminar este tópico, você deve saber:**

- [ ] Ligar cada serviço ao cenário: call center → Connect; e-mails → SES; desktop virtual → WorkSpaces.
- [ ] Diferenciar **WorkSpaces** (desktop inteiro) de **AppStream 2.0** (só o aplicativo no navegador).
- [ ] Diferenciar **SES** (e-mails formatados a clientes) de **SNS** (notificações simples).

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Contact center** | central de atendimento (telefone, chat). |
| **DaaS** | desktop como serviço. |
| **IoT** | internet das coisas: sensores e dispositivos conectados. |

> 🎯 **Como não errar na prova:** "Call center" → **Connect**. "Funcionário remoto precisa de desktop" → **WorkSpaces**. "App de desktop no navegador" → **AppStream 2.0**. "Sensores" → **IoT Core**.

## 📖 Conteúdo

- **Amazon Connect:** **central de atendimento (contact center) na nuvem**, com voz, chat e tarefas, pago por uso.
- **Amazon SES (Simple Email Service):** envio de **e-mails** transacionais e de marketing em grande volume. Diferença para o SNS: SES é para e-mails formatados a clientes; SNS é para notificações simples.
- **Amazon WorkSpaces:** **desktops virtuais** (DaaS) Windows ou Linux, acessados de qualquer dispositivo.
- **Amazon AppStream 2.0:** **streaming de aplicações** de desktop para o navegador, sem entregar o desktop inteiro.
- **Amazon WorkSpaces Secure Browser:** navegador seguro gerenciado para acessar sites internos sem VPN.
- **AWS Amplify:** ferramentas para **criar, implantar e hospedar** aplicações web e mobile full-stack rapidamente.
- **AWS AppSync:** **APIs GraphQL** gerenciadas, com dados em tempo real e sincronização offline.
- **AWS IoT Core:** conecta **dispositivos IoT** à nuvem (protocolo MQTT) com segurança e em grande escala.
- **Cai na prova:** "call center" = Connect; "funcionários remotos precisam de um desktop" = WorkSpaces; "rodar um app de desktop no navegador" = AppStream 2.0; "sensores enviando dados" = IoT Core.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).

- "Criar uma central de atendimento na nuvem." → Amazon Connect.
- "Enviar e-mails de confirmação e marketing em massa." → SES.
- "Oferecer desktops virtuais a funcionários remotos." → WorkSpaces.
- "Disponibilizar um aplicativo de desktop pelo navegador." → AppStream 2.0.
- "Criar e hospedar rapidamente um app web ou mobile full-stack." → Amplify.
- "API GraphQL gerenciada com dados em tempo real." → AppSync.
- "Conectar milhões de sensores à nuvem." → IoT Core.

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
