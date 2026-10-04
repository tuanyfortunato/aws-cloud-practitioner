# AWS Global Accelerator

> **Categoria:** Rede / desempenho global · **Domínio:** 3 · **Escopo:** **Global** · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)
>
> **Em uma frase:** fornece **2 IPs anycast estáticos** e leva o tráfego TCP/UDP pela rede global da AWS até o endpoint saudável mais próximo.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

<!-- didatico:inicio -->
## 🧠 Entenda em 30 segundos

> 💡 **Analogia:** é uma **via expressa da AWS**: o usuário entra pela rampa mais próxima (2 IPs fixos) e segue pela rede da AWS até a região mais saudável.

- ✅ **Escolha quando:** aplicações **TCP/UDP** (jogos, VoIP) precisam de **IPs estáticos globais** e **failover rápido** entre regiões.
- 🚫 **Não é a resposta quando:** precisa de **cache de conteúdo** → [CloudFront](cloudfront.md).
- 🎯 **Palavras do enunciado que apontam para ele:** "IPs estáticos", "anycast", "TCP/UDP", "failover entre regiões", "sem cache".
<!-- didatico:fim -->

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

## 🔗 Documentação oficial

- [Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)
