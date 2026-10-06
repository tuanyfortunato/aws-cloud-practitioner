# AWS Firewall Manager e AWS Network Firewall

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa precisa padronizar proteções em várias contas e também pode precisar inspecionar tráfego que passa pela rede.

**Como este serviço ajuda?** Firewall Manager coordena políticas de proteção em recursos compatíveis de uma organização. Network Firewall inspeciona tráfego de rede conforme regras e caminhos configurados.

**Exemplo do dia a dia:** A equipe central define uma política comum de proteção. Para uma necessidade de inspeção de rede, avalia separadamente Network Firewall.

**O que ele não resolve sozinho?** Administrar políticas é diferente de inspecionar cada conexão. São serviços distintos e têm escopos de prova diferentes, indicados abaixo.

**Primeiras palavras para entender:**

- **Firewall:** controle de tráfego por regras.
- **Política central:** regras administradas para vários ambientes.
- **Inspeção:** análise de comunicações.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança de rede · **Domínio:** 2 · **Escopo:** Organização (Firewall Manager) / VPC (Network Firewall) · **Tópico do guia:** [2.8 Proteção de rede e aplicações](../../docs/02-seguranca-e-conformidade/08-protecao-de-rede-e-aplicacoes.md)
>
> **Em uma frase:** o Firewall Manager **governa** regras de firewall em todas as contas; o Network Firewall **é** um firewall gerenciado para a VPC.
>
> **Escopo oficial:** 🔀 Firewall Manager ✅ · Network Firewall ❌ fora do escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Separe a necessidade de administrar políticas da necessidade de inspecionar tráfego.

**Passo 2.** Use Firewall Manager para políticas compatíveis da organização; avalie Network Firewall para o caminho de rede que precisa de inspeção.

**Passo 3.** Configure escopo e verifique o efeito dos controles. As duas ferramentas não executam a mesma função.

## 2. Recursos e opções, com significado

### AWS Firewall Manager

| Item | Detalhe |
|---|---|
| **Função** | Gerenciamento **central** de políticas de segurança em todas as contas e recursos do **AWS Organizations**, aplicando-as automaticamente a novos recursos. |
| **Políticas** | **WAF**, **Shield Advanced**, **security groups** (auditoria e regras comuns), **Network Firewall**, **Route 53 Resolver DNS Firewall**, firewalls de terceiros do Marketplace. |
| **Pré-requisitos** | AWS Organizations (todos os recursos), **AWS Config** ativado, conta administradora do Firewall Manager. |
| **Cobrança** | Por política por região/mês + recursos subjacentes (WAF, Config). |

### AWS Network Firewall ❌

> ❌ **Fora do escopo da CLF-C02** — documentado só para referência ([lista oficial](../../docs/00-guia-do-exame/escopo-oficial.md)).

| Item | Detalhe |
|---|---|
| **Função** | Firewall de rede **stateful**, gerenciado e escalável, para filtrar todo o tráfego que entra, sai ou atravessa a VPC. |
| **Regras** | Stateless e stateful; compatível com regras **Suricata** (IPS); filtragem por **domínio** (FQDN), IP, porta, protocolo; inspeção TLS. |
| **Implantação** | Endpoints numa *firewall subnet*; rotas direcionam o tráfego por ele; pode ficar centralizado com Transit Gateway. |
| **Uso** | Prevenção de intrusão (IPS), bloquear saída para domínios não autorizados, inspeção entre VPCs. |
| **Cobrança** | Por endpoint-hora + GB processado. |

### Comparação de "firewalls" da AWS

**Security group**

**Camada:** 3/4

**Onde:** Instância/ENI (stateful)

**Network ACL**

**Camada:** 3/4

**Onde:** Subnet (stateless)

**Network Firewall**

**Camada:** 3–7

**Onde:** VPC (stateful, IPS, domínios)

**WAF**

**Camada:** 7

**Onde:** CloudFront, ALB, API Gateway…

**Shield**

**Camada:** 3/4 (+7 Advanced)

**Onde:** DDoS

**Firewall Manager**

**Onde:** Governança central de todos acima

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Administrar políticas é diferente de inspecionar cada conexão. São serviços distintos e têm escopos de prova diferentes, indicados abaixo.

## 4. Caso resolvido: ligando as peças

A equipe central define uma política comum de proteção. Para uma necessidade de inspeção de rede, avalia separadamente Network Firewall.

**Aplicando a sequência à situação:**

**Etapa 1:** Separe a necessidade de administrar políticas da necessidade de inspecionar tráfego.
**Etapa 2:** Use Firewall Manager para políticas compatíveis da organização; avalie Network Firewall para o caminho de rede que precisa de inspeção.
**Etapa 3:** Configure escopo e verifique o efeito dos controles. As duas ferramentas não executam a mesma função.

**Resultado e responsabilidade:** Firewall Manager coordena políticas de proteção em recursos compatíveis de uma organização. Network Firewall inspeciona tráfego de rede conforme regras e caminhos configurados.

**Recursos envolvidos:** Políticas centralizadas do Firewall Manager; endpoints/regras de Network Firewall.

**Decisões que precisam ser tomadas:** Escopo de contas/recursos e regras.

**Outra situação comentada:** Mesma política WAF em várias contas: Firewall Manager, com Organizations e configuração necessária.

**Por que não concluir mais do que isso:** Não são o mesmo produto; Network Firewall está fora do escopo consultado

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Aplicar as mesmas regras de WAF em todas as contas."

**Resposta curta:** Firewall Manager.

**Pergunta:** "Inspecionar e filtrar todo o tráfego que entra na VPC (IPS)."

**Resposta curta:** Network Firewall.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html) · [Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
