# AWS Compute Optimizer, Service Quotas, License Manager e outros

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A equipe pode estar usando capacidade inadequada, alcançar um limite de serviço ou perder controle sobre licenças. Cada dificuldade exige uma ferramenta diferente.

**Como este serviço ajuda?** Compute Optimizer recomenda ajustes de recursos compatíveis; Service Quotas acompanha limites de uso; License Manager ajuda a administrar licenças de software.

**Exemplo do dia a dia:** Uma máquina parece maior que o necessário: a equipe avalia recomendações. Se precisa criar mais recursos e encontra uma quota, consulta o limite e a possibilidade de aumento.

**O que ele não resolve sozinho?** Uma recomendação não é uma quota, e aumentar uma quota não otimiza custo. Gerenciar licença também não compra automaticamente os direitos de uso do software.

**Primeiras palavras para entender:**

- **Dimensionar:** escolher capacidade adequada.
- **Quota:** limite de uso.
- **Licença:** direito de usar software sob determinadas condições.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Gerenciamento / otimização e governança · **Domínio:** 3 e 4 · **Escopo:** Regional · **Tópico do guia:** [3.16 Gestão e governança](../../docs/03-tecnologia-e-servicos/16-gestao-e-governanca.md)
>
> **Em uma frase:** ferramentas para dimensionar recursos, controlar limites e licenças, e organizar o ambiente.
>
> **Escopo oficial:** ✅ No escopo (Launch Wizard ❌ fora do escopo) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Descubra se o problema é dimensão do recurso, limite de uso ou administração de licença.

**Passo 2.** Consulte a ferramenta pertinente e os dados que fundamentam a decisão.

**Passo 3.** Ajuste recursos, solicite aumento elegível ou revise licenças conforme o caso. Essas ações não são intercambiáveis.

## 2. Recursos e opções, com significado

### AWS Compute Optimizer

Usa **machine learning** sobre métricas do CloudWatch (14 dias por padrão; até 93 com métricas avançadas) para recomendar o **tamanho ideal** de: **EC2**, **Auto Scaling groups**, **volumes EBS**, **funções Lambda** (memória), **tasks ECS no Fargate**, RDS e licenças comerciais.

Classifica recursos como *under-provisioned*, *over-provisioned* ou *optimized* e estima a economia.

Gratuito no básico (opt-in). Recomendações também aparecem no **Cost Optimization Hub**.

### Service Quotas

Mostra as **cotas (limites)** de cada serviço por região, valores padrão e aplicados.

**Solicitar aumento** pelo console/API; *quota request templates* para contas novas da organização.

Alarmes do CloudWatch quando o uso se aproxima do limite.

### AWS License Manager

Controla o uso de **licenças de software** (Microsoft, Oracle, SAP, IBM): regras por vCPU/núcleo/socket, limites rígidos ou alertas.

Ajuda com **BYOL** em Dedicated Hosts (automatiza alocação de hosts) e evita multas de auditoria.

### Outros utilitários de organização

**Tags + Tag Editor**

**Função:** Pares chave-valor para organizar, controlar acesso (ABAC) e separar custos

**Resource Groups**

**Função:** Agrupar recursos por tag/stack para operar juntos

**Resource Explorer**

**Função:** Buscar recursos em todas as regiões/contas

**AWS Launch Wizard ❌ fora do escopo**

**Função:** Implantar SAP, SQL Server, Active Directory com boas práticas

**AWS AppConfig ❌ fora do escopo**

**Função:** Feature flags e configuração dinâmica de aplicações (parte do Systems Manager)

**Well-Architected Tool**

**Função:** Revisão gratuita de cargas contra os 6 pilares ([1.4](../../docs/01-conceitos-de-nuvem/04-well-architected-framework.md))

**AWS Management Console mobile app**

**Função:** Acompanhar recursos, alarmes e Health no celular

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Uma recomendação não é uma quota, e aumentar uma quota não otimiza custo. Gerenciar licença também não compra automaticamente os direitos de uso do software.

## 4. Caso resolvido: ligando as peças

Uma máquina parece maior que o necessário: a equipe avalia recomendações. Se precisa criar mais recursos e encontra uma quota, consulta o limite e a possibilidade de aumento.

**Aplicando a sequência à situação:**

**Etapa 1:** Descubra se o problema é dimensão do recurso, limite de uso ou administração de licença.
**Etapa 2:** Consulte a ferramenta pertinente e os dados que fundamentam a decisão.
**Etapa 3:** Ajuste recursos, solicite aumento elegível ou revise licenças conforme o caso. Essas ações não são intercambiáveis.

**Resultado e responsabilidade:** Compute Optimizer recomenda ajustes de recursos compatíveis; Service Quotas acompanha limites de uso; License Manager ajuda a administrar licenças de software.

**Recursos envolvidos:** Recomendações, quotas e configurações de licenças.

**Decisões que precisam ser tomadas:** Opt-in/métricas, quota ajustável e regra de licença.

**Outra situação comentada:** Instância grande demais: Compute Optimizer; limite da conta: Service Quotas; direito comercial: contrato da licença.

**Por que não concluir mais do que isso:** Quota não garante capacidade disponível; License Manager não compra licença

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Recomendar o tamanho ideal das instâncias com base no uso."

**Resposta curta:** Compute Optimizer.

**Pergunta:** "Pedir aumento do limite de instâncias."

**Resposta curta:** Service Quotas.

**Pergunta:** "Controlar quantas licenças de SQL Server estão em uso."

**Resposta curta:** License Manager.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) · [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) · [License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
