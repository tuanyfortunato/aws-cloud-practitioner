<!-- autoral -->

# Elastic Load Balancing (ELB)

> **Categoria:** Computação e rede · **Domínio:** 3 · **Abrangência:** Regional; distribui entre várias zonas de disponibilidade · **Ficha:** núcleo
>
> **Em uma frase:** distribui automaticamente o tráfego que chega entre destinos saudáveis, como instâncias EC2, containers e endereços IP, em uma ou mais zonas de disponibilidade.
>
> **Escopo oficial:** ✅ Cobrado junto com o EC2 (não aparece como item separado na lista) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.4 Escalabilidade e balanceamento de carga](../../docs/03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

Quando o sistema de matrícula roda em várias instâncias, os pais precisam de um único endereço para acessá-lo, qualquer que seja a instância que os atenda. E se uma instância travar, os acessos não podem continuar indo para ela.

O Elastic Load Balancing resolve o problema da **distribuição**: o **balanceador de carga** é o único ponto de contato, recebe cada acesso e o encaminha a um destino saudável. Ele verifica a saúde dos destinos, escala a própria capacidade quando o tráfego muda e pode receber as conexões HTTPS com certificados do AWS Certificate Manager, liberando as instâncias desse trabalho.

O limite: o balanceador distribui a capacidade que existe, mas não cria instâncias. Quem ajusta a quantidade é o [EC2 Auto Scaling](ec2-auto-scaling.md); juntos, os dois dão elasticidade e alta disponibilidade.

## Como funciona

1. O balanceador tem um **listener**, que escuta uma porta e um protocolo, como HTTPS na porta 443.
2. Os destinos (instâncias, containers, endereços IP ou funções Lambda) ficam em **grupos de destino** (*target groups*).
3. O balanceador faz **verificações de saúde** periódicas em cada destino.
4. Cada acesso que chega vai para um destino saudável. No Application Load Balancer, regras podem escolher o grupo de destino pelo caminho da URL ou pelo nome do site.
5. Destinos que falham na verificação deixam de receber tráfego até voltarem a passar nela.

## Opções principais

| Tipo | Camada | Quando usar |
|---|---|---|
| Application Load Balancer (ALB) | Aplicação (camada 7), HTTP e HTTPS | Rotear pelo conteúdo do pedido: caminho da URL (`/matricula`, `/boletim`) ou nome do site |
| Network Load Balancer (NLB) | Transporte (camada 4), TCP, UDP e TLS | Milhões de pedidos por segundo, latência baixa e endereço IP fixo em cada zona de disponibilidade |
| Gateway Load Balancer (GWLB) | Rede (camada 3) | Enviar o tráfego a appliances virtuais de terceiros, como firewalls e sistemas de detecção de intrusão |
| Classic Load Balancer | — | Geração anterior; a AWS recomenda migrar para os atuais |

As camadas vêm do modelo OSI ([aula 3.4](../../docs/03-tecnologia-e-servicos/04-escalabilidade-e-balanceamento.md)): quanto mais alta, mais o balanceador "entende" do pedido.

## Números que a prova cobra

O ELB não tem número que a prova costuma cobrar; o que cai é a escolha do tipo de balanceador e a diferença entre balanceador e Auto Scaling.

## Como é cobrado

Cada balanceador é cobrado por **hora** (ou fração de hora) em funcionamento, mais as **unidades de capacidade** que consome, medidas por minuto: conexões novas e ativas, volume de dados e avaliações de regras. Um balanceador ligado sem tráfego continua cobrando as horas.

## Não confundir com

| Serviço | Diferença para o ELB | Pista no enunciado |
|---|---|---|
| [EC2 Auto Scaling](ec2-auto-scaling.md) | Ajusta quantas instâncias existem; não distribui tráfego | "Acompanhar a demanda", "substituir instâncias com defeito" |
| [Amazon Route 53](../redes/route-53.md) | DNS: traduz nomes em endereços e pode escolher entre Regiões ou recursos | "Nome de domínio", "rotear por localização" |
| [AWS Global Accelerator](../redes/global-accelerator.md) | IPs estáticos globais que levam o tráfego pela rede da AWS até a Região mais próxima | "IP estático global", "usuários no mundo todo" |
| [AWS WAF](../seguranca/waf.md) | Filtra pedidos web maliciosos; pode proteger um ALB, mas não distribui tráfego | "Injeção de SQL", "bloquear ataques à aplicação" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
- [Como o Elastic Load Balancing funciona](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html)
- [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
- [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)
- [Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html)
- [Preços do Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
