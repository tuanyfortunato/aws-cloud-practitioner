<!-- autoral -->

# Amazon CloudFront

> **Categoria:** Entrega de conteúdo (CDN) · **Domínio:** 3 (e 2: proteção na borda) · **Abrangência:** Global (locais de borda) · **Ficha:** núcleo
>
> **Em uma frase:** rede de entrega de conteúdo (CDN) que guarda cópias nos locais de borda, perto dos usuários, e reduz a latência e a carga na origem.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.10 Redes e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md) · base em [3.2 Infraestrutura global](../../docs/03-tecnologia-e-servicos/02-infraestrutura-global.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

Os vídeos das reuniões ficam num bucket do S3 em São Paulo, e os alunos de Lisboa reclamam que demoram a carregar. Cada pedido atravessa o oceano, e a mesma aula é buscada na origem centenas de vezes.

O CloudFront acelera a entrega de conteúdo estático e dinâmico usando os **locais de borda** da AWS. O pedido do usuário vai para o local de borda com menor latência; se o conteúdo já está guardado lá, é entregue na hora; se não, o CloudFront o busca na **origem** (um bucket do S3, um balanceador ou um servidor web) e guarda uma cópia para os próximos pedidos.

O limite: o cache ajuda quando muitos usuários pedem o mesmo conteúdo. Para levar cada conexão TCP ou UDP até a aplicação por IPs fixos, sem cache, a resposta é o [Global Accelerator](global-accelerator.md).

## Como funciona

1. Você cria uma **distribuição** e indica a origem, como um bucket do S3.
2. O CloudFront dá um nome de domínio à distribuição; você pode usar o seu próprio domínio, apontado pelo [Route 53](route-53.md).
3. O usuário pede o arquivo e é atendido pelo local de borda mais próximo em latência.
4. Se a cópia não está na borda, o CloudFront busca na origem e a guarda para os próximos pedidos.

## Opções principais

| Recurso | O que faz | Pista no enunciado |
|---|---|---|
| Distribuição com origem no S3 | Entrega arquivos do bucket pela borda | "Site estático no S3 para o mundo todo" |
| Integração com AWS WAF e AWS Shield | Filtra pedidos maliciosos e protege contra DDoS na borda | "Proteger a aplicação na borda" |
| Planos de preço fixo | CDN, WAF, proteção contra DDoS, DNS e certificado por um preço mensal sem cobrança excedente | "Custo mensal previsível" |
| Pagamento pelo uso | Cobra transferência e requisições | "Pagar só o que usar" |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Transferência da origem na AWS (S3, ELB, API Gateway) para o CloudFront | Sem cobrança | 06/10/2026 |
| Plano de preço fixo mais básico | Gratuito (US$ 0 por mês) | 06/10/2026 |

## Como é cobrado

No pagamento pelo uso, o CloudFront cobra a transferência de dados dos locais de borda para os usuários e as requisições HTTP ou HTTPS, com preços que variam por região geográfica. A transferência de origens na AWS para o CloudFront é gratuita. Os planos de preço fixo (Free, Pro, Business e Premium) juntam CDN, WAF, proteção contra DDoS, DNS do Route 53 e certificado TLS por um valor mensal.

## Não confundir com

| Serviço | Diferença para o CloudFront | Pista no enunciado |
|---|---|---|
| [AWS Global Accelerator](global-accelerator.md) | IPs estáticos e conexão levada pela rede da AWS, sem cache | "TCP ou UDP", "IPs fixos", "jogos" |
| [Amazon Route 53](route-53.md) | DNS: responde o endereço, não entrega o conteúdo | "Nome do domínio" |
| [Amazon S3](../armazenamento/s3.md) | Guarda os arquivos numa Região; é a origem | "Guardar os vídeos" |
| [Amazon ElastiCache](../banco-de-dados/elasticache.md) | Cache em memória na frente do banco, dentro da Região | "Aliviar o banco de dados" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)
- [Preços do Amazon CloudFront](https://aws.amazon.com/cloudfront/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
