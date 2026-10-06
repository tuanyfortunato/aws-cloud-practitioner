<!-- autoral -->

# Rede e diretório (Cloud Map, VPC Lattice, Network Access Analyzer e Cloud Directory)

> **Categoria:** Redes e diretório · **Domínio:** — (fora da prova) · **Abrangência:** Regional · **Ficha:** referência
>
> **Em uma frase:** serviços de descoberta e conexão entre partes de uma aplicação, análise de acesso de rede e diretório, todos na lista fora do escopo.
>
> **Escopo oficial:** ❌ Fora do escopo — documentado só para referência · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.18 Serviços menos conhecidos](../../docs/03-tecnologia-e-servicos/18-servicos-menos-conhecidos.md)

🏠 [Índice das fichas](../README.md)

---

## Como funciona

Os serviços de rede no escopo incluem VPC, Route 53 e CloudFront. Estes resolvem problemas mais específicos e estão fora da prova.

1. **AWS Cloud Map:** dá nomes lógicos aos serviços e recursos de que a aplicação depende e ajuda a aplicação a encontrá-los, só entre os saudáveis.
2. **Amazon VPC Lattice:** conecta, protege e monitora os serviços e recursos de uma aplicação, numa VPC ou entre VPCs e contas.
3. **Network Access Analyzer:** recurso da VPC que encontra caminhos de rede que não seguem os requisitos de acesso definidos.
4. **Amazon Cloud Directory:** repositório de diretórios que escala até centenas de milhões de objetos; fechado a novos clientes, com fim do suporte em 24/07/2027.

## Não confundir com

| Serviço | Diferença | Pista no enunciado |
|---|---|---|
| [Amazon Route 53](../redes/route-53.md) | DNS e roteamento de tráfego; no escopo | "Domínio", "DNS" |
| [Amazon VPC](../redes/vpc.md) | A rede privada da conta; no escopo | "Sub-rede", "security group" |
| [AWS Directory Service](../seguranca/directory-service.md) | Active Directory na AWS; no escopo | "Active Directory" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Cloud Map](https://docs.aws.amazon.com/cloud-map/latest/dg/what-is-cloud-map.html)
- [O que é o Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html)
- [O que é o Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html)
- [O que é o Amazon Cloud Directory](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/what_is_cloud_directory.html)
- [Serviços fora do escopo da prova](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-out-of-scope-services.html)
<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
