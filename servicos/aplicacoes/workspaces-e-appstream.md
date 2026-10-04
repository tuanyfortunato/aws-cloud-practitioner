# Amazon WorkSpaces, AppStream 2.0 e WorkSpaces Secure Browser

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

## 🔗 Documentação oficial

- [WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html) · [AppStream 2.0](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html)
