<!-- autoral -->

# Amazon WorkSpaces, WorkSpaces Applications (AppStream 2.0) e WorkSpaces Secure Browser

> **Categoria:** Computação para o usuário final · **Domínio:** 3 · **Abrangência:** Regional · **Ficha:** complementar
>
> **Em uma frase:** serviços em que o programa roda na AWS e o dispositivo só mostra a tela: desktops virtuais, streaming de aplicações e navegador seguro.
>
> **Escopo oficial:** ✅ No escopo (WorkSpaces, AppStream 2.0 e WorkSpaces Secure Browser) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.14 Aplicações de negócio, usuário final, front-end e IoT](../../docs/03-tecnologia-e-servicos/14-aplicacoes-de-negocio-e-iot.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

Os professores precisam usar de casa um programa de notas que só está instalado nos computadores da escola, e a secretaria quer computadores completos sem comprar hardware. Nos três serviços, o programa roda na AWS e o dispositivo do usuário só mostra a tela.

1. **Amazon WorkSpaces:** desktops virtuais Windows ou Linux, acessados de vários dispositivos ou pelo navegador; o WorkSpaces Personal é persistente e de uma pessoa, o WorkSpaces Pools é recriado a cada uso, não aceita clientes novos desde 31/07/2026 e tem fim do suporte em 31/12/2027.
2. **Amazon WorkSpaces Applications** (no guia do exame, Amazon AppStream 2.0): faz streaming de um programa de desktop pelo navegador, sem entregar o desktop inteiro; todos usam a versão mais recente.
3. **Amazon WorkSpaces Secure Browser:** acesso seguro, pelo navegador, a sites internos e aplicações SaaS, sem que os dados cheguem ao dispositivo; deixa de aceitar clientes novos em 29/10/2026.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [Amazon EC2](../computacao/ec2.md) | Servidores, não desktops para usuários | "Servidor", "instância" |
| [AWS Amplify](amplify-e-appsync.md) | Cria e hospeda aplicações web e móveis | "Front-end" |
| [AWS Directory Service](../seguranca/directory-service.md) | Diretório usado no login dos WorkSpaces | "Active Directory" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html)
- [Fim do suporte ao WorkSpaces Pools](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-pools-end-of-support.html)
- [O que é o Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html)
- [Amazon WorkSpaces Secure Browser](https://aws.amazon.com/workspaces/secure-browser/)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
