<!-- autoral -->

# AWS Global Accelerator

> **Categoria:** Rede e desempenho global · **Domínio:** 3 · **Abrangência:** Global · **Ficha:** núcleo
>
> **Em uma frase:** dá à aplicação dois IPs estáticos anycast e leva o tráfego TCP ou UDP pela rede global da AWS até o endpoint saudável mais adequado.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.10 Redes e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

O aplicativo de aulas ao vivo da escola tem usuários em vários países e roda em duas Regiões. Pela internet pública, cada conexão passa por muitas redes até chegar à AWS, e a qualidade varia. Além disso, as escolas parceiras liberam no firewall só endereços IP fixos.

O Global Accelerator dá à aplicação **endereços IP estáticos**, anunciados a partir da rede de borda da AWS (anycast). O usuário entra na rede da AWS no ponto mais próximo, e o tráfego segue pela **rede global da AWS** até o endpoint na Região mais adequada, considerando saúde, localização e as regras configuradas. Se um endpoint falha, o tráfego muda na hora para outro saudável.

O limite: o Global Accelerator não guarda cópias do conteúdo. Para entregar arquivos repetidos com cache, a resposta é o [CloudFront](cloudfront.md).

## Como funciona

1. Você cria um **acelerador** e recebe dois IPs estáticos IPv4 (quatro, com IPv6).
2. Adiciona **listeners** para as portas e protocolos (TCP ou UDP).
3. Associa **grupos de endpoints** por Região: balanceadores (ALB ou NLB), instâncias do EC2 ou Elastic IPs.
4. O Global Accelerator acompanha a saúde dos endpoints e encaminha cada conexão para um saudável.

## Opções principais

| Opção | O que faz | Pista no enunciado |
|---|---|---|
| IPs estáticos | Os endereços continuam do acelerador enquanto ele existir | "Lista de IPs liberados no firewall" |
| Endpoints em várias Regiões | Tráfego vai para a Região adequada e saudável | "Failover entre Regiões" |
| Traga seus IPs (BYOIP) | Usa endereços IPv4 próprios como entrada | "Manter os IPs da empresa" |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| IPs estáticos por acelerador | 2 IPv4 (4 com IPv6) | 06/10/2026 |
| Protocolos dos listeners | TCP e UDP | 06/10/2026 |

## Como é cobrado

Cada acelerador, ativado ou desativado, cobra uma **taxa fixa por hora** até ser apagado, mais uma taxa sobre a transferência de dados (DT-Premium), calculada a cada hora na direção dominante do tráfego.

## Não confundir com

| Serviço | Diferença para o Global Accelerator | Pista no enunciado |
|---|---|---|
| [Amazon CloudFront](cloudfront.md) | Entrega cópias guardadas nos locais de borda (HTTP/HTTPS) | "Cache", "vídeos e imagens" |
| [Amazon Route 53](route-53.md) | Failover pelo DNS: muda o endereço devolvido nas consultas | "Política de failover no DNS", "nome de domínio" |
| [Elastic Load Balancing](../computacao/elastic-load-balancing.md) | Distribui dentro de uma Região; pode ser endpoint do acelerador | "Distribuir entre instâncias" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)
- [Listeners](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-listeners.html)
- [Preços do AWS Global Accelerator](https://aws.amazon.com/global-accelerator/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
