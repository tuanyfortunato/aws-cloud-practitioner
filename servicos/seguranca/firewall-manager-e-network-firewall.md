<!-- autoral -->

# AWS Firewall Manager e AWS Network Firewall

> **Categoria:** Segurança de rede · **Domínio:** 2 · **Abrangência:** Organização (Firewall Manager) e VPC (Network Firewall) · **Ficha:** complementar
>
> **Em uma frase:** o Firewall Manager aplica as mesmas proteções em todas as contas de uma organização; o Network Firewall filtra e inspeciona o tráfego na borda de uma VPC.
>
> **Escopo oficial:** 🔀 Firewall Manager ✅ · Network Firewall ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [2.8 Proteção de rede e aplicações](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)

🏠 [Índice das fichas](../README.md) · 🏫 [O caso da escola](../../docs/00-guia-do-exame/caso-da-escola.md)

---

## Como funciona

A rede tem uma conta da AWS por escola, e cada uma precisa das mesmas regras de WAF e de security groups. Configurar conta por conta é repetitivo e sujeito a esquecimento. O **AWS Firewall Manager** administra de forma central as proteções do WAF, do Shield Advanced, dos security groups e ACLs de rede, do Network Firewall e do Route 53 Resolver DNS Firewall nas contas de uma organização do AWS Organizations.

1. A conta administradora define uma política de proteção, por exemplo regras do WAF para todos os CloudFront.
2. Escolhe as contas e recursos alvo: todos, de um tipo ou com certas tags.
3. O Firewall Manager aplica a política automaticamente.
4. Contas e recursos novos recebem a proteção sozinhos.

O **Network Firewall** é um firewall de rede gerenciado e *stateful*, com detecção e prevenção de intrusões, que filtra o tráfego que entra e sai da VPC. Ele está fora do escopo da prova.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [AWS WAF](waf.md) | Filtra pedidos web numa aplicação | "Injeção de SQL", "pedidos HTTP" |
| [AWS Shield](shield.md) | Protege contra DDoS | "Negação de serviço" |
| [AWS Organizations](../gerenciamento/organizations.md) | Agrupa as contas; SCPs limitam permissões | "Impedir ações nas contas" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html)
- [O que é o AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)
- [Serviços fora do escopo da prova](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-out-of-scope-services.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
