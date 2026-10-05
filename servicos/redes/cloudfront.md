# Amazon CloudFront

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Visitantes em lugares diferentes precisam receber imagens, vídeos ou páginas sem sempre buscar tudo no servidor de origem, que pode estar distante.

**Como este serviço ajuda?** CloudFront distribui conteúdo por uma rede de pontos de presença. Pode manter cópias em cache e encaminhar solicitações à origem conforme as regras.

**Exemplo do dia a dia:** A escola distribui imagens do site pelo CloudFront. Visitantes podem obter cópias a partir de um ponto próximo, sem pedir cada arquivo ao servidor original.

**O que ele não resolve sozinho?** Ele não transforma automaticamente toda aplicação em conteúdo estático nem permite guardar qualquer resposta em cache sem cuidado. A origem, as regras e os acessos precisam ser configurados.

**Primeiras palavras para entender:**

- **CDN:** rede de distribuição de conteúdo.
- **Origem:** lugar de onde o conteúdo vem.
- **Cache:** cópia mantida para reutilização.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** CDN / entrega de conteúdo · **Domínio:** 3 (e 2: proteção na borda) · **Escopo:** **Global** (edge locations) · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)
>
> **Em uma frase:** rede de distribuição de conteúdo (CDN) que faz **cache** perto dos usuários, reduzindo latência e carga na origem.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Para que serve

- Sites e APIs globais, vídeo (streaming), downloads, sites estáticos no S3, aceleração de conteúdo dinâmico.
- Proteção na borda: **Shield Standard incluso**, integração com **WAF**.

## Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Distribution** | Configuração da CDN com domínio `*.cloudfront.net` (ou o seu). |
| **Origins** | S3, ALB, EC2, API Gateway, MediaPackage, qualquer servidor HTTP; *origin groups* para failover. |
| **Behaviors** | Regras por caminho (`/api/*`, `*.jpg`) com origem, cache policy, métodos permitidos, viewer protocol (redirecionar HTTP→HTTPS). |
| **Cache policy / TTL** | Quanto tempo e com quais chaves (headers, cookies, query strings) guardar. |
| **Invalidation** | Remove objetos do cache antes do TTL (pago acima da cota grátis); alternativa: versionar nomes de arquivos. |
| **Regional Edge Caches** | Camada intermediária maior entre edge e origem. **Origin Shield** adiciona mais uma camada centralizada. |
| **OAC (Origin Access Control)** | Bucket S3 privado acessível **só pelo CloudFront**. ✔️ É o método recomendado; o OAI é legado ("not recommended", ainda documentado). |
| **Signed URLs / signed cookies** | Restringem acesso a conteúdo privado (cursos pagos, assinaturas). |
| **Geo restriction** | Allow/block list de países. |
| **HTTPS** | Certificado do **ACM** (precisa estar em **us-east-1**), SNI, políticas TLS; *field-level encryption*. |
| **Edge compute** | **CloudFront Functions** (JS leve, sub-ms, manipular headers/URLs) e **Lambda@Edge** (Node/Python, mais poder, acesso à rede). |
| **Price classes** | Limitar às edge locations mais baratas para reduzir custo. |
| **Logs** | Standard logs (S3/CloudWatch) e real-time logs (Kinesis). |

## Cobrança

- Transferência de saída para a internet (por região de edge) + requisições HTTP/HTTPS + invalidações, Functions, Lambda@Edge.
- ✔️ **Transferência da origem AWS (S3, EC2, ELB) para o CloudFront é gratuita** (origin fetches).
- 🔄 **Planos de preço fixo** (desde 18/11/2025): um valor mensal que agrupa CDN, WAF, proteção DDoS, Route 53, CloudWatch Logs, edge compute e créditos de S3, sem cobrança por excedente — Free (US$ 0), Pro (US$ 15), Business (US$ 200) e Premium (US$ 1.000) **por distribuição**, além de Custom; o pay-as-you-go continua disponível. 🧊 Não cai na prova.

## Segurança e responsabilidade compartilhada

- **AWS:** rede de borda, Shield Standard, disponibilidade.
- **Cliente:** configuração de HTTPS, OAC, regras do WAF, quem acessa (signed URLs), conteúdo.

## ⚠️ Pegadinhas e não confundir

- CloudFront (cache, HTTP/HTTPS) × **Global Accelerator** (sem cache, TCP/UDP, IPs estáticos).
- CloudFront × **S3 Transfer Acceleration** (usa a rede do CloudFront para **uploads** ao S3).
- "Reduzir custo de saída para usuários globais" → CloudFront.

## ❓ Perguntas típicas

- "Reduzir latência de conteúdo para usuários globais." → CloudFront.
- "Deixar o bucket S3 privado e servir só via CDN." → CloudFront com OAC.
- "Conteúdo pago só para assinantes." → Signed URLs/cookies.
- "Bloquear acesso de determinados países." → Geo restriction (ou WAF).
- "Rodar código leve na borda para reescrever URLs." → CloudFront Functions.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Distribution, origins, behaviors, cache e políticas |
| **O que você decide/configura?** | Origem, HTTPS, cache, acesso e caminhos |
| **Em que ordem as coisas acontecem?** | Usuário acessa edge; cache responde ou busca a origem |
| **O que pode fazer, e em que condição?** | Distribui conteúdo estático/dinâmico com mecanismos de cache |
| **O que não pode presumir?** | Não substitui back-end; resposta pode permanecer em cache até atualização/invalidation; OAC não serve ao website endpoint S3 |

**Caso comentado:** Conteúdo privado S3 com HTTPS: origem S3 apropriada e OAC, sem tornar bucket público.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Guia do CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)
