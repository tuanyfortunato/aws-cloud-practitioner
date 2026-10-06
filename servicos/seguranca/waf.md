<!-- autoral -->

# AWS WAF (Web Application Firewall)

> **Categoria:** Segurança e proteção de aplicações · **Domínio:** 2 · **Abrangência:** Global (CloudFront) ou Regional · **Ficha:** núcleo
>
> **Em uma frase:** firewall de aplicações web que examina cada pedido HTTP ou HTTPS e, pelas regras do cliente, deixa passar, bloqueia ou devolve uma resposta personalizada.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.8 Proteção de rede e aplicações](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

Alguém digita código SQL no campo de busca do portal da escola, tentando listar as notas de todos os alunos. O pedido chega pela porta 443, que precisa estar aberta para todo mundo, então security groups e ACLs de rede deixam passar: eles olham endereços e portas, não o que vai dentro do pedido.

O **AWS WAF** (*web application firewall*) olha o conteúdo. Ele fica na frente do CloudFront, do Application Load Balancer, de uma API do API Gateway e de outros recursos web, e avalia cada pedido contra as regras de um **web ACL** (no console novo, *protection pack*): injeção de SQL, cross-site scripting, endereço IP, país de origem, excesso de pedidos de uma mesma origem. O pedido aprovado segue; o reprovado recebe o código 403 ou uma resposta personalizada.

O limite: o WAF só entende pedidos web e só protege o que você associar a ele. Uma enxurrada de tráfego nas camadas de rede é assunto do [Shield](shield.md), e o WAF não corrige a falha no código, só barra os pedidos que se encaixam nas regras.

## Como funciona

1. Você cria um web ACL e escolhe uma ação padrão: permitir ou bloquear o que nenhuma regra pegar.
2. Adiciona regras próprias e grupos de regras gerenciadas, como o conjunto básico da AWS, o de bancos SQL e a lista de endereços com má reputação.
3. Associa o web ACL aos recursos: para o CloudFront, ele é criado no escopo global (na Região Norte da Virgínia); para os demais, na mesma Região do recurso.
4. Cada pedido passa pelas regras em ordem de prioridade; a primeira que permitir ou bloquear decide, e o que nenhuma regra decidir recebe a ação padrão.

## Opções principais

| Tipo de regra | O que verifica | Exemplo na escola |
|---|---|---|
| Injeção de SQL | Código SQL no pedido | Busca que tenta listar todas as notas |
| Cross-site scripting (XSS) | Script inserido para rodar no navegador de outros | Comentário com código no mural |
| IP e país de origem | Endereço ou localização de quem pede | Bloquear uma faixa de IPs abusiva |
| Limite de taxa (*rate-based*) | Pedidos demais de uma origem num intervalo | Robô tentando senhas no login |
| Grupos gerenciados | Conjuntos prontos mantidos pela AWS ou por vendedores | Proteções comuns sem escrever regras |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Resposta a um pedido bloqueado | HTTP 403 ou resposta personalizada | 06/10/2026 |
| Web ACL para o CloudFront | Criado na Região Norte da Virgínia (escopo global) | 06/10/2026 |
| Compromisso | Nenhum; paga-se o uso | 06/10/2026 |

## Como é cobrado

Sem compromisso: cobra por web ACL por mês, por regra por mês e por milhão de pedidos avaliados, além de taxas próprias de recursos extras como o controle de robôs e de fraude. O valor soma-se ao do recurso protegido. Quem assina o Shield Advanced tem as taxas padrão do WAF incluídas nos recursos protegidos.

## Não confundir com

| Serviço | Diferença para o WAF | Pista no enunciado |
|---|---|---|
| [AWS Shield](shield.md) | Protege contra DDoS, pelo volume | "Negação de serviço", "enxurrada de tráfego" |
| Security groups ([VPC](../redes/vpc.md)) | Filtram portas e endereços, sem ler o pedido | "Liberar a porta", "firewall da instância" |
| [AWS Network Firewall](firewall-manager-e-network-firewall.md) | Firewall gerenciado na borda da VPC | "Inspecionar o tráfego da VPC" |
| [AWS Firewall Manager](firewall-manager-e-network-firewall.md) | Aplica o mesmo web ACL em todas as contas | "Regras de WAF em toda a organização" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html)
- [Recursos globais e regionais](https://docs.aws.amazon.com/waf/latest/developerguide/how-aws-waf-works-resources.html)
- [Regras de injeção de SQL](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-sqli-match.html) e [regras baseadas em taxa](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html)
- [Grupos de regras gerenciadas da AWS](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-list.html)
- [Preços do AWS WAF](https://aws.amazon.com/waf/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
