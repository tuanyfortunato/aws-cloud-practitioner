<!-- autoral -->

# AWS CloudFormation (e CDK, SAM)

> **Categoria:** Gerenciamento e infraestrutura como código · **Domínio:** 1 e 3 · **Abrangência:** Regional (StackSets alcançam várias contas e Regiões) · **Ficha:** núcleo
>
> **Em uma frase:** cria e atualiza a infraestrutura a partir de um modelo escrito em YAML ou JSON, sempre do mesmo jeito, como uma pilha de recursos que se gerencia em conjunto.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.1 Formas de acesso e implantação](../../docs/03-tecnologia-e-servicos/01-formas-de-acesso-e-implantacao.md) · [3.16 Gestão e governança](../../docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

Todo semestre, a empresa do sistema de matrícula monta um ambiente de testes clicando no console: rede, load balancer, instâncias, banco de dados. Sempre alguém esquece um passo, e o teste não se parece com a produção.

O **CloudFormation** troca os cliques por um arquivo. Você escreve um **modelo** (*template*) em YAML ou JSON que descreve os recursos e suas propriedades, e o CloudFormation cria e configura tudo como uma **pilha** (*stack*). O mesmo modelo gera o mesmo ambiente quantas vezes for preciso, em outra Região ou conta, e fica guardado e versionado como qualquer arquivo. Apagar a pilha apaga todos os recursos dela e encerra a cobrança deles.

O limite: o modelo só descreve. Os recursos criados continuam sujeitos às permissões e são cobrados normalmente. E se alguém mudar um recurso direto no console, a pilha fica diferente do modelo; a **detecção de desvio** aponta essa diferença, mas não a impede.

## Como funciona

1. Você escreve o modelo, ou o gera com o **AWS CDK** (em linguagens como TypeScript, Python ou Java) ou com o **AWS SAM** (atalhos para aplicações sem servidor).
2. O CloudFormation lê o modelo e cria e configura os recursos como uma pilha.
3. Para mudar algo, você altera o modelo; um **conjunto de alterações** (*change set*) mostra antes o que será modificado, substituído ou apagado.
4. Para repetir em várias contas e Regiões, o **StackSets** implanta o mesmo modelo numa só operação.

## Opções principais

| Recurso | O que faz | Exemplo na escola |
|---|---|---|
| Modelo e pilha | Descreve e cria os recursos como uma unidade | Ambiente de testes por semestre |
| Conjunto de alterações | Prevê o impacto de uma atualização | Ver se a mudança vai recriar o banco |
| Detecção de desvio | Aponta recursos alterados por fora | Alguém abriu uma porta direto no console |
| StackSets | Mesma pilha em várias contas e Regiões | A mesma rede em todas as escolas |
| AWS CDK | Escreve a infraestrutura numa linguagem de programação | Equipe que prefere Python |
| AWS SAM | Sintaxe curta para aplicações sem servidor | Função Lambda com API |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Formatos do modelo | YAML ou JSON | 06/10/2026 |
| Custo com recursos da AWS | Sem custo adicional; paga-se o que for criado | 06/10/2026 |
| Recursos de terceiros | Nível gratuito de 1.000 operações por mês por conta | 06/10/2026 |

## Como é cobrado

Usar o CloudFormation com recursos da AWS não tem custo adicional: paga-se pelos recursos criados, como se tivessem sido criados à mão. Recursos de provedores de terceiros são cobrados por operação, acima de 1.000 por mês por conta.

## Não confundir com

| Serviço | Diferença para o CloudFormation | Pista no enunciado |
|---|---|---|
| [AWS Elastic Beanstalk](../computacao/elastic-beanstalk.md) | Sobe e opera uma aplicação web a partir do código | "Só enviar o código" |
| [AWS Systems Manager](systems-manager.md) | Opera as máquinas que já existem | "Aplicar patches", "rodar comandos" |
| [AWS Service Catalog](service-catalog-e-ram.md) | Catálogo de produtos aprovados para as equipes criarem sozinhas | "Equipes só criam o que foi aprovado" |
| [AWS Control Tower](control-tower.md) | Monta o ambiente de várias contas | "Landing zone" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [Como o CloudFormation funciona](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-overview.html)
- [Conjuntos de alterações](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html)
- [Detecção de desvio](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html)
- [StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)
- [O que é o AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
- [Preços do AWS CloudFormation](https://aws.amazon.com/cloudformation/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
