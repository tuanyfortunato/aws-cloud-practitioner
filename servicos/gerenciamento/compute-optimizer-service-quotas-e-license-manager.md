<!-- autoral -->

# AWS Compute Optimizer, Service Quotas e License Manager

> **Categoria:** Gerenciamento / otimização e governança · **Domínio:** 3 e 4 · **Abrangência:** Regional · **Ficha:** complementar
>
> **Em uma frase:** o Compute Optimizer recomenda o tamanho certo dos recursos, o Service Quotas mostra os limites da conta e pede aumentos, e o License Manager controla licenças de software.
>
> **Escopo oficial:** ✅ No escopo (Launch Wizard ❌ fora do escopo) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.16 Gestão e governança](../../docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md) · [1.7 Economia da nuvem](../../docs/01-conceitos-de-nuvem/07-economia-da-nuvem.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

Três problemas de administração aparecem na rede. Os servidores parecem grandes demais para o uso. A conta não deixa criar mais instâncias de um tipo numa Região. E ninguém sabe quantas licenças do Windows Server estão em uso. Cada um tem uma ferramenta.

1. **Compute Optimizer:** analisa a configuração e as métricas de uso e recomenda o tamanho certo, apontando também recursos ociosos, para EC2, Auto Scaling groups, EBS, Lambda, ECS no Fargate, RDS e Aurora, entre outros.
2. **Service Quotas:** mostra num só lugar as cotas (limites) de cada serviço e se cada uma é ajustável; quando a padrão não atende, pede-se o aumento, que o Support pode aprovar, negar ou aprovar em parte.
3. **License Manager:** acompanha licenças de fornecedores como Microsoft, IBM, SAP e Oracle, com regras que impõem limites rígidos ou de aviso para evitar usar mais licenças do que a empresa tem.

O AWS Launch Wizard está na lista de serviços fora do escopo da prova.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [AWS Trusted Advisor](trusted-advisor.md) | Verificações de boas práticas, inclusive limites e custo | "Recomendações em várias categorias" |
| [AWS Cost Explorer](../custos/cost-explorer.md) | Analisa gastos e recomenda compras de RIs e Savings Plans | "Gastos passados" |
| [Amazon EC2 Auto Scaling](../computacao/ec2-auto-scaling.md) | Muda a quantidade de instâncias, não o tamanho | "Acompanhar a demanda" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)
- [O que é o Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)
- [O que é o AWS License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager.html)
- [Serviços fora do escopo da prova](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-out-of-scope-services.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
