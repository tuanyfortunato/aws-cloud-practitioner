# Amazon WorkSpaces, AppStream 2.0 e WorkSpaces Secure Browser

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Pessoas precisam usar um ambiente de trabalho ou uma aplicação à distância, sem instalar tudo no próprio computador.

**Como este serviço ajuda?** WorkSpaces oferece ambientes de trabalho virtuais em modalidades próprias. AppStream transmite aplicações; WorkSpaces Secure Browser atende acesso web corporativo controlado.

**Exemplo do dia a dia:** Uma empresa fornece a colaboradores um ambiente remoto ou acesso a uma aplicação corporativa, escolhendo o produto adequado à experiência necessária.

**O que ele não resolve sozinho?** Um desktop completo, uma aplicação transmitida e um navegador remoto são soluções diferentes. Identidade, aplicações, rede e modalidade precisam ser planejadas.

**Primeiras palavras para entender:**

- **Desktop virtual:** ambiente de trabalho remoto.
- **Streaming de aplicação:** uso de software transmitido ao dispositivo.
- **Sessão:** período de acesso do usuário.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Computação para usuário final (EUC) · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.14 Aplicações de negócio, usuário final, front-end e IoT](../../docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md)
>
> **Em uma frase:** entregam desktops, aplicações ou um navegador seguro hospedados na AWS para qualquer dispositivo.
>
> **Escopo oficial:** ✅ No escopo (WorkSpaces, AppStream 2.0 e WorkSpaces Secure Browser) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Comparação

| | **WorkSpaces (Personal / Pools)** | **AppStream 2.0** | **WorkSpaces Secure Browser** (✔️ renomeado de WorkSpaces Web em maio/2024) |
|---|---|---|---|
| Entrega | **Desktop virtual completo** (DaaS) Windows, Linux ou Ubuntu | **Uma aplicação** de desktop transmitida para o navegador | **Navegador** isolado e gerenciado |
| Persistência | Personal: desktop persistente por usuário; Pools: não persistente | Não persistente (pode salvar em S3/home folders) | Não persistente |
| Uso | Funcionários remotos, terceirizados, BYOD | Software pesado (CAD, IDEs) em qualquer dispositivo, treinamentos | Acessar sites internos/SaaS sem VPN, sem dados no dispositivo |
| Cobrança | **Mensal** (AlwaysOn) ou **por hora** (AutoStop) | Por hora das instâncias da *fleet* (always-on, on-demand ou elastic) | Por usuário/mês |

- 🔄 Os protocolos **PCoIP** e o **WorkSpaces Pools** estão em *sunset*; o WorkSpaces continua no escopo.
- O protocolo de streaming **NICE DCV** agora se chama **Amazon DCV** (versão 2024.0) ✔️.
- **WorkSpaces Thin Client:** dispositivo físico barato para acessar esses serviços.
- Integração com Active Directory/Identity Center; dados ficam na AWS (não no dispositivo).

## ❓ Perguntas típicas

- "Oferecer desktops virtuais a funcionários remotos." → WorkSpaces.
- "Disponibilizar um aplicativo de desktop pelo navegador." → AppStream 2.0.
- "Acessar sites internos com navegador seguro sem VPN." → WorkSpaces Secure Browser.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Desktops WorkSpaces, fleets/stacks AppStream e portal Secure Browser |
| **O que você decide/configura?** | Identidade, rede, imagem e regras de sessão |
| **Em que ordem as coisas acontecem?** | Usuário autentica e recebe desktop, aplicação ou navegador remoto |
| **O que pode fazer, e em que condição?** | Entrega experiência remota sem instalar toda carga no dispositivo |
| **O que não pode presumir?** | São produtos distintos; persistência depende da modalidade; políticas de cópia/download devem ser configuradas |

**Caso comentado:** Desktop completo: WorkSpaces; app específico: AppStream; navegação isolada: Secure Browser.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html) · [AppStream 2.0](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html)
