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

## Como funciona

1. O usuário se conecta a um dos **2 IPs estáticos** anycast, que entram na rede AWS pela edge location mais próxima.
2. O tráfego segue pela **backbone da AWS** (não pela internet pública) até o **endpoint group** da região.
3. Health checks redirecionam em segundos para outra região se houver falha.

## Configurações

| Item | Detalhe |
|---|---|
| **Listeners** | Portas/protocolos TCP e UDP. |
| **Endpoint groups** | Um por região; **traffic dial** controla o percentual enviado a cada região. |
| **Endpoints** | ALB, NLB, instâncias EC2, Elastic IPs; com **pesos**. |
| **Client affinity** | Mantém o mesmo usuário no mesmo endpoint. |
| **Custom routing** | Mapeia usuários para instâncias específicas (jogos, VoIP). |
| **Proteção** | Shield Standard incluso. |

## Cobrança

- Taxa fixa por acelerador-hora + **DT-Premium** por GB transferido.

## ⚠️ Pegadinhas e não confundir

- ⚠️ **Não faz cache.** Para cache → CloudFront.
- IP fixo **global** → Global Accelerator; IP fixo **regional** → NLB com Elastic IP.
- Failover regional rápido sem depender de TTL de DNS → Global Accelerator (o Route 53 depende do cache DNS dos clientes).

## ❓ Perguntas típicas

- "IPs estáticos globais e failover rápido entre regiões para TCP/UDP." → Global Accelerator.
- "Jogo multiplayer UDP com usuários no mundo todo." → Global Accelerator.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Accelerator, IPs estáticos, listeners, endpoint groups e endpoints |
| **O que você decide/configura?** | Protocolo, regiões, saúde e pesos |
| **Em que ordem as coisas acontecem?** | Recebe conexão na borda e encaminha pela rede AWS ao endpoint elegível |
| **O que pode fazer, e em que condição?** | Melhora caminhos para aplicações TCP/UDP globais |
| **O que não pode presumir?** | Não é cache/CDN de objetos e não substitui a aplicação |

**Caso comentado:** Usuários globais precisam IPs fixos e tráfego TCP/UDP: Global Accelerator, em vez de escolher CloudFront por palavra global.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)
