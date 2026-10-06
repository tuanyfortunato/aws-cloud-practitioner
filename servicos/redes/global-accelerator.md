# AWS Global Accelerator

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Usuários de lugares diferentes precisam chegar a aplicações por caminhos de rede mais consistentes, com pontos de entrada fixos.

**Como este serviço ajuda?** Global Accelerator usa a rede global da AWS para encaminhar tráfego a destinos compatíveis, considerando configuração e saúde desses destinos.

**Exemplo do dia a dia:** Uma aplicação distribuída usa endereços de entrada fixos e encaminha conexões para seus destinos AWS configurados.

**O que ele não resolve sozinho?** Ele encaminha tráfego; não guarda cópias de imagens ou páginas como uma CDN. Também não corrige lentidão causada pelo código ou pelo banco.

**Primeiras palavras para entender:**

- **IP:** endereço de rede.
- **Destino:** recurso que recebe o tráfego.
- **Roteamento:** escolha do caminho de uma comunicação.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Rede / desempenho global · **Domínio:** 3 · **Escopo:** **Global** · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)
>
> **Em uma frase:** fornece **2 IPs anycast estáticos** e leva o tráfego TCP/UDP pela rede global da AWS até o endpoint saudável mais próximo.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Defina destinos compatíveis e o comportamento de atendimento entre eles.

**Passo 2.** Prepare os pontos de entrada e o encaminhamento pela rede AWS conforme a configuração e a saúde observada.

**Passo 3.** Observe o resultado nas conexões. O serviço encaminha tráfego; ele não mantém cópias dos arquivos da aplicação.

## 2. Recursos e opções, com significado

### Como funciona

1. O usuário se conecta a um dos **2 IPs estáticos** anycast, que entram na rede AWS pela edge location mais próxima.

2. O tráfego segue pela **backbone da AWS** (não pela internet pública) até o **endpoint group** da região.

3. Health checks redirecionam em segundos para outra região se houver falha.

### Configurações

| Item | Detalhe |
|---|---|
| **Listeners** | Portas/protocolos TCP e UDP. |
| **Endpoint groups** | Um por região; **traffic dial** controla o percentual enviado a cada região. |
| **Endpoints** | ALB, NLB, instâncias EC2, Elastic IPs; com **pesos**. |
| **Client affinity** | Mantém o mesmo usuário no mesmo endpoint. |
| **Custom routing** | Mapeia usuários para instâncias específicas (jogos, VoIP). |
| **Proteção** | Shield Standard incluso. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele encaminha tráfego; não guarda cópias de imagens ou páginas como uma CDN. Também não corrige lentidão causada pelo código ou pelo banco.

### ⚠️ Pegadinhas e não confundir

⚠️ **Não faz cache.** Para cache → CloudFront.

IP fixo **global** → Global Accelerator; IP fixo **regional** → NLB com Elastic IP.

Failover regional rápido sem depender de TTL de DNS → Global Accelerator (o Route 53 depende do cache DNS dos clientes).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Taxa fixa por acelerador-hora + **DT-Premium** por GB transferido.

## 5. Caso resolvido: ligando as peças

Uma aplicação distribuída usa endereços de entrada fixos e encaminha conexões para seus destinos AWS configurados.

**Aplicando a sequência à situação:**

**Etapa 1:** Defina destinos compatíveis e o comportamento de atendimento entre eles.
**Etapa 2:** Prepare os pontos de entrada e o encaminhamento pela rede AWS conforme a configuração e a saúde observada.
**Etapa 3:** Observe o resultado nas conexões. O serviço encaminha tráfego; ele não mantém cópias dos arquivos da aplicação.

**Resultado e responsabilidade:** Global Accelerator usa a rede global da AWS para encaminhar tráfego a destinos compatíveis, considerando configuração e saúde desses destinos.

**Recursos envolvidos:** Accelerator, IPs estáticos, listeners, endpoint groups e endpoints.

**Decisões que precisam ser tomadas:** Protocolo, regiões, saúde e pesos.

**Outra situação comentada:** Usuários globais precisam IPs fixos e tráfego TCP/UDP: Global Accelerator, em vez de escolher CloudFront por palavra global.

**Por que não concluir mais do que isso:** Não é cache/CDN de objetos e não substitui a aplicação

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "IPs estáticos globais e failover rápido entre regiões para TCP/UDP."

**Resposta curta:** Global Accelerator.

**Pergunta:** "Jogo multiplayer UDP com usuários no mundo todo."

**Resposta curta:** Global Accelerator.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
