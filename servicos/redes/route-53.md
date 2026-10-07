<!-- autoral -->

# Amazon Route 53

> **Categoria:** DNS · **Domínio:** 3 · **Abrangência:** Global · **Ficha:** núcleo
>
> **Em uma frase:** DNS gerenciado da AWS, que registra domínios, liga nomes aos recursos e desvia o tráfego de recursos com falha.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.10 Redes e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) · base em [0.2 Rede: endereço IP, porta, DNS e HTTPS](../../docs/fundamentos/02-rede.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Que problema resolve

Os pais devem chegar ao sistema digitando `matricula.escola.com.br`, não o endereço do balanceador. E, se a Região principal falhar, o nome deveria passar a apontar para uma cópia em outra Região sem ninguém mexer à mão.

O Route 53 é o serviço de **DNS** da AWS, altamente disponível e escalável. Ele faz três coisas, juntas ou separadas: **registra domínios**, **roteia** o tráfego, ligando o nome ao recurso, e faz **verificações de saúde** (health checks), desviando o tráfego dos recursos que não respondem. As **políticas de roteamento** escolhem qual resposta dar a cada consulta.

O limite: o Route 53 só responde qual endereço usar; o tráfego em si não passa por ele. Ele não guarda conteúdo em cache ([CloudFront](cloudfront.md)) nem leva a conexão pela rede da AWS ([Global Accelerator](global-accelerator.md)).

## Como funciona

1. Você registra o domínio no Route 53 (ou usa um registrado em outro lugar).
2. Cria uma **zona hospedada** com os **registros** do domínio, como `matricula` apontando para o balanceador.
3. Escolhe a política de roteamento de cada registro e, se quiser, liga verificações de saúde.
4. Quando alguém digita o nome, o Route 53 responde com o endereço do recurso adequado e saudável.

## Opções principais

| Política | O que faz | Pista no enunciado |
|---|---|---|
| Simples | Um recurso só | "Um servidor web" |
| Ponderada | Divide o tráfego em proporções definidas | "Testar a versão nova com 10% dos usuários" |
| Latência | Manda para a Região com melhor latência | "Usuários em vários continentes" |
| Failover | Ativo-passivo: usa o secundário quando o principal falha | "Site de contingência" |
| Geolocalização | Decide pela localização do usuário | "Conteúdo diferente por país" |
| Geoproximidade | Decide pela localização dos recursos, com ajuste de tráfego | "Deslocar tráfego entre Regiões" |
| Resposta com vários valores | Até oito registros saudáveis ao acaso | "Vários IPs saudáveis" |
| Por IP | Decide pelos endereços IP de origem | "Rede do provedor do usuário" |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Funções principais | 3 (registro, roteamento e verificação de saúde) | 06/10/2026 |
| Políticas de roteamento | 8 | 06/10/2026 |
| Registros na resposta com vários valores | Até 8 saudáveis | 06/10/2026 |

## Como é cobrado

Você paga por zona hospedada por mês, por consulta DNS respondida, pelas verificações de saúde e pelo registro de domínios. Até 50 verificações de saúde de endpoints da AWS na mesma conta são gratuitas. Consultas a registros de alias apontados para recursos da AWS, como balanceadores, distribuições do CloudFront e API Gateway, não são cobradas.

## Não confundir com

| Serviço | Diferença para o Route 53 | Pista no enunciado |
|---|---|---|
| [Amazon CloudFront](cloudfront.md) | Entrega o conteúdo com cache nos locais de borda | "Baixa latência para vídeos e imagens" |
| [AWS Global Accelerator](global-accelerator.md) | IPs estáticos e tráfego levado pela rede global da AWS | "IPs fixos", "rede global da AWS" |
| [Elastic Load Balancing](../computacao/elastic-load-balancing.md) | Distribui o tráfego entre instâncias numa Região | "Distribuir entre instâncias" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)
- [Políticas de roteamento](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html)
- [Registros de alias](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html)
- [Preços do Amazon Route 53](https://aws.amazon.com/route53/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
