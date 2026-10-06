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

## 1. A sequência de funcionamento

**Passo 1.** Identifique se o usuário precisa de desktop completo, aplicação transmitida ou navegação corporativa.

**Passo 2.** Prepare a modalidade, identidades e software necessários. A pessoa inicia uma sessão autorizada.

**Passo 3.** Administre acesso e experiência. Cada modalidade oferece uma experiência diferente de trabalho remoto.

## 2. Recursos e opções, com significado

### Comparação

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **VPN:** Conexão lógica protegida que liga usuários ou redes. Um túnel VPN não concede automaticamente acesso a todos os recursos do destino.
- **virtual:** Um recurso virtual é criado por software sobre equipamentos físicos. VM significa máquina virtual: computador lógico com sistema operacional e recursos de processamento.
- **hora:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
- **SaaS:** Software como serviço: aplicação pronta disponibilizada para uso. O cliente administra seu uso e seus dados conforme a oferta, em vez de construir o software do zero.
- **On-Demand:** Modalidade de uso sem o compromisso de longo prazo descrito por reservas e planos. Cobrança e unidades dependem do recurso contratado.
- **BYOD:** Uso de dispositivo próprio pelo usuário. Compatibilidade e controles do ambiente remoto continuam necessários.
- **CAD:** CRM trata relacionamento com clientes; CAD, projeto assistido por computador; EDI, troca eletrônica estruturada de dados. São necessidades de aplicação distintas.

| | **WorkSpaces (Personal / Pools)** | **AppStream 2.0** | **WorkSpaces Secure Browser** (✔️ renomeado de WorkSpaces Web em maio/2024) |
|---|---|---|---|
| Entrega | **Desktop virtual completo** (DaaS) Windows, Linux ou Ubuntu | **Uma aplicação** de desktop transmitida para o navegador | **Navegador** isolado e gerenciado |
| Persistência | Personal: desktop persistente por usuário; Pools: não persistente | Não persistente (pode salvar em S3/home folders) | Não persistente |
| Uso | Funcionários remotos, terceirizados, BYOD | Software pesado (CAD, IDEs) em qualquer dispositivo, treinamentos | Acessar sites internos/SaaS sem VPN, sem dados no dispositivo |
| Cobrança | **Mensal** (AlwaysOn) ou **por hora** (AutoStop) | Por hora das instâncias da *fleet* (always-on, on-demand ou elastic) | Por usuário/mês |

🔄 Os protocolos **PCoIP** e o **WorkSpaces Pools** estão em *sunset*; o WorkSpaces continua no escopo.

**Antes de ler este trecho:**

- **protocolo:** Conjunto de regras da comunicação. Um protocolo define o formato e o comportamento da troca; produtos precisam ser compatíveis com ele.
- **streaming:** Fluxo contínuo de dados ou mídia. É diferente de esperar um arquivo completo antes de iniciar o trabalho.
- **NICE:** Nome associado a tecnologias de transmissão de ambiente ou aplicação remota. A modalidade determina a experiência e os requisitos.

O protocolo de streaming **NICE DCV** agora se chama **Amazon DCV** (versão 2024.0) ✔️.

**WorkSpaces Thin Client:** dispositivo físico barato para acessar esses serviços.

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **Active Directory:** Tecnologia de diretório para identidades, computadores e controles corporativos. É diferente do cadastro de clientes de uma aplicação pública.

Integração com Active Directory/Identity Center; dados ficam na AWS (não no dispositivo).

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

**Antes de ler este trecho:**

- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.

Um desktop completo, uma aplicação transmitida e um navegador remoto são soluções diferentes. Identidade, aplicações, rede e modalidade precisam ser planejadas.

## 4. Caso resolvido: ligando as peças

Uma empresa fornece a colaboradores um ambiente remoto ou acesso a uma aplicação corporativa, escolhendo o produto adequado à experiência necessária.

**Aplicando a sequência à situação:**

**Etapa 1:** Identifique se o usuário precisa de desktop completo, aplicação transmitida ou navegação corporativa.
**Etapa 2:** Prepare a modalidade, identidades e software necessários. A pessoa inicia uma sessão autorizada.
**Etapa 3:** Administre acesso e experiência. Cada modalidade oferece uma experiência diferente de trabalho remoto.

**Resultado e responsabilidade:** WorkSpaces oferece ambientes de trabalho virtuais em modalidades próprias. AppStream transmite aplicações; WorkSpaces Secure Browser atende acesso web corporativo controlado.

**Recursos envolvidos:** Desktops WorkSpaces, fleets/stacks AppStream e portal Secure Browser.

**Decisões que precisam ser tomadas:** Identidade, rede, imagem e regras de sessão.

**Outra situação comentada:** Desktop completo: WorkSpaces; app específico: AppStream; navegação isolada: Secure Browser.

**Por que não concluir mais do que isso:** São produtos distintos; persistência depende da modalidade; políticas de cópia/download devem ser configuradas

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Oferecer desktops virtuais a funcionários remotos."

**Resposta curta:** WorkSpaces.

**Pergunta:** "Disponibilizar um aplicativo de desktop pelo navegador."

**Resposta curta:** AppStream 2.0.

**Pergunta:** "Acessar sites internos com navegador seguro sem VPN."

**Resposta curta:** WorkSpaces Secure Browser.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html) · [AppStream 2.0](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
