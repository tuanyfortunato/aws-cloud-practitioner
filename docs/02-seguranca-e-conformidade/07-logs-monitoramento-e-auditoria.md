# 2.7 Logs, monitoramento e auditoria

## 🧠 Antes de começar

**Qual é a dificuldade?** O sistema está lento, um recurso foi alterado ou uma configuração deixou de atender às regras. Cada pergunta precisa de um tipo diferente de registro.

**A ideia em palavras simples:** CloudWatch acompanha comportamento e operação; CloudTrail registra atividades AWS; Config acompanha configuração e sua avaliação. O objetivo da pergunta orienta a ferramenta.

**Exemplo do dia a dia:** Para lentidão, a equipe examina métricas e logs. Para saber quem alterou um recurso, procura o evento. Para avaliar sua configuração, usa o histórico e as regras aplicáveis.

**O que não concluir?** Nenhuma dessas ferramentas observa tudo sem configuração. Coleta, retenção, cobertura e ações de resposta variam; registrar um problema não é o mesmo que corrigi-lo.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Chamada de API** | qualquer ação feita na AWS (pelo console, CLI ou programa). |
| **Métrica** | um número medido ao longo do tempo (ex.: uso de CPU). |
| **Alarme** | aviso disparado quando uma métrica passa de um limite. |

---

> **Domínio 2 — Segurança e Conformidade (30%)**

> 🔎 **Fichas detalhadas:** [AWS CloudTrail](../../servicos/gerenciamento/cloudtrail.md) · [AWS Config](../../servicos/gerenciamento/config.md) · [Amazon CloudWatch](../../servicos/gerenciamento/cloudwatch.md) · [Amazon VPC (Virtual Private Cloud)](../../servicos/redes/vpc.md) · [AWS Health Dashboard](../../servicos/gerenciamento/health-dashboard.md)

⬅️ [2.6 Compliance e governança](06-compliance-e-governanca.md) · 🏠 [Índice do domínio](README.md) · [2.8 Proteção de rede e aplicações](08-protecao-de-rede-e-aplicacoes.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **métrica:** Medida observada ao longo do tempo, como utilização ou número de erros. O número precisa de unidade, período e contexto para ter significado.
- **evento:** Informação sobre algo que aconteceu. Uma regra pode encaminhar o evento; outro componente realiza a ação de negócio.

Há três perguntas distintas: ‘como está funcionando?’, ‘quem realizou a ação?’ e ‘como estava configurado?’. Uma métrica responde a comportamento; um evento registra atividade; um histórico de configuração mostra propriedades ao longo do tempo.

Comece pela pergunta e só depois escolha a ferramenta. Se um sistema ficou lento após uma alteração, pode ser necessário correlacionar os três tipos de informação. Registrar dados também exige planejar sua coleta, conservação e acesso.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

o **CloudTrail** é a **câmera de segurança** (grava quem fez cada ação); o **Config** é o **álbum de fotos** da configuração ao longo do tempo; o **CloudWatch** é o **painel do carro**, com indicadores e luzes de alerta.

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **AWS CloudTrail:** CloudTrail registra atividades e chamadas compatíveis realizadas na conta.
- **CloudTrail:** Registro de atividades e chamadas AWS compatíveis. Ajuda a analisar quem realizou uma operação, em vez de medir sozinho a velocidade da aplicação.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **recurso:** Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
- **IP:** Endereços usados para identificar interfaces e destinos na rede. IPv4 e IPv6 são versões diferentes; ter um endereço não concede permissão nem garante uma rota.

**AWS CloudTrail:** registra as **chamadas de API** na conta: quem fez, o quê, quando, de onde (IP) e em qual recurso.

  - **Event history:** ativado por padrão, guarda **90 dias** de eventos de gerenciamento, grátis.
**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.
- **bucket:** Recipiente que organiza objetos no S3. A aplicação usa o bucket e a identificação do objeto para pedir operações autorizadas.

  - **Trails:** para guardar por mais tempo, envia os logs para um bucket S3 (e opcionalmente CloudWatch Logs). Pode ser multi-região e para toda a organização.
**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.

  - **Management events** (criar, alterar, apagar recursos) vs **data events** (ex.: leitura de objetos no S3, invocação de Lambda), que não são registrados por padrão.
**Antes de ler este trecho:**

- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.

  - **CloudTrail Insights:** detecta atividade anormal de API. **CloudTrail Lake:** consultas SQL sobre os eventos.
**Antes de ler este trecho:**

- **AWS Config:** AWS Config registra configurações de recursos compatíveis e permite avaliá-las com regras.
- **Config:** Serviço que acompanha configurações e suas avaliações em recursos compatíveis. Observar configuração é diferente de observar uma métrica de desempenho.

**AWS Config:** registra a **configuração** dos recursos e o histórico de mudanças ao longo do tempo.

  - **Config rules** (gerenciadas ou customizadas): avaliam se os recursos estão conformes (ex.: "todo bucket S3 deve ser criptografado").
**Antes de ler este trecho:**

- **Systems Manager:** Systems Manager reúne ferramentas de operação para recursos e nós gerenciados compatíveis, incluindo acesso, automação, inventário e gerenciamento de patches.

  - Pode disparar **remediação automática** (via Systems Manager Automation).
**Antes de ler este trecho:**

- **regional:** O recurso ou a operação pertence a uma região. Serviços globais podem administrar objetos regionais; leia o alcance do recurso, não apenas o nome do serviço.

  - É regional e pago por item registrado e por avaliação.
**Antes de ler este trecho:**

- **Amazon CloudWatch:** CloudWatch reúne recursos para métricas, logs e alarmes.

**Amazon CloudWatch**: monitoramento de métricas, logs e alarmes. Pontos de prova:

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **minuto:** Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.

  - Métricas padrão do EC2 a cada 5 minutos (monitoramento detalhado: 1 minuto, pago).
**Antes de ler este trecho:**

- **memória:** Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.

  - **Memória e disco do EC2 não vêm por padrão:** exigem o CloudWatch agent instalado (métricas customizadas).
**Antes de ler este trecho:**

- **SNS:** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis.

  - **Alarmes:** disparam ações quando uma métrica passa do limite (notificar via SNS, acionar Auto Scaling, parar/reiniciar EC2). **Billing alarm:** alerta de custo baseado na métrica de cobrança.

  - **CloudWatch Logs**, **Logs Insights** (consultas) e **dashboards**.
**Antes de ler este trecho:**

- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **GuardDuty:** GuardDuty analisa fontes de dados compatíveis para detectar possíveis ameaças e produzir achados de segurança.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.

**VPC Flow Logs:** registram o tráfego IP que entra e sai das interfaces de rede da VPC; usados em análise de segurança e pelo GuardDuty.

**Antes de ler este trecho:**

- **AWS Health Dashboard / Health Dashboard:** AWS Health apresenta eventos sobre a saúde dos serviços e informações relevantes aos recursos da conta, conforme a visão consultada.

**AWS Health Dashboard:** status dos serviços AWS e eventos que afetam a **sua** conta (manutenções programadas, problemas). Ver também [3.16](../03-tecnologia-e-servicos/16-gestao-e-governanca.md).

**Antes de ler este trecho:**

- **CPU:** CPU é o processador que executa instruções. vCPU é a unidade de processamento virtual apresentada ao ambiente. Mais processamento não resolve automaticamente falta de memória ou de velocidade do disco.
- **security group:** Regras de tráfego associadas a interfaces ou recursos compatíveis. É um controle de rede, não uma permissão IAM para ler um arquivo ou chamar uma API.
- **instância:** Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.

**Cai na prova:** "quem apagou a instância?" = CloudTrail; "como estava configurado o security group semana passada?" = Config; "alerta quando a CPU passa de 80%" = CloudWatch alarm; "verificar continuamente se recursos seguem as regras" = Config rules.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **retenção:** Tempo durante o qual dados ou registros são conservados. Depois desse prazo, o comportamento depende das regras do serviço e das configurações.
- **conformidade:** Atendimento a requisitos definidos. Usar um serviço com certificações não torna automaticamente a aplicação do cliente conforme.

**Primeiro, identifique o funcionamento:** CloudWatch trabalha com métricas, logs e alarmes; CloudTrail registra atividades e chamadas; Config acompanha configuração e conformidade de recursos suportados.

**Depois, compare as escolhas:** CPU elevada: CloudWatch. Quem alterou a instância: CloudTrail. Qual era a configuração e se atendia uma regra: Config. Evento da infraestrutura AWS: Health.

**Por fim, verifique o limite:** Alarmes e registros precisam de configuração e retenção adequadas. CloudTrail não inclui todo evento de dados por padrão; métricas de memória da EC2 exigem coleta adicional.

## 4. Caso resolvido

Uma regra de segurança mudou e você quer saber quem mudou e como o recurso estava antes. Um único serviço resolve as duas perguntas?

**Raciocínio e resposta:** CloudTrail ajuda a identificar a ação e a identidade; Config mostra o histórico de configuração. CloudWatch complementa com o efeito operacional.

## 5. Revisão do capítulo

**Objetivos de aprendizagem:**

- [ ] Ligar cada pergunta ao serviço: quem fez → CloudTrail; configuração e conformidade → Config; métricas e alarmes → CloudWatch.
- [ ] Lembrar que o CloudTrail guarda **90 dias** por padrão e que, para mais tempo, se cria um **trail** para o S3.
- [ ] Lembrar que **memória e disco** do EC2 exigem o **CloudWatch agent**.

**Dica de revisão para a prova:** Leia o **verbo** da pergunta: "quem **apagou**" → CloudTrail; "como **estava**" → Config; "**alertar** quando a CPU passar" → CloudWatch. "Verificar **continuamente** se segue a regra" → Config rules.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-2.md).
**Pergunta:** "Qual serviço registra quem encerrou uma instância e quando?"

**Resposta curta:** CloudTrail.

**Pergunta:** "Por quanto tempo o CloudTrail guarda eventos sem configurar nada?"

**Resposta curta:** 90 dias (event history).

**Pergunta:** "Como guardar logs do CloudTrail por anos?"

**Resposta curta:** Criar um trail que envia para o S3.

**Pergunta:** "Qual serviço mostra o histórico de configuração de um recurso e se ele segue as regras?"

**Resposta curta:** AWS Config.

**Pergunta:** "Como receber alerta quando a CPU passar de 80%?"

**Resposta curta:** Alarme do CloudWatch (com notificação pelo SNS).

**Antes de ler este trecho:**

- **alarme:** Condição acompanhada sobre dados de monitoramento. Uma mudança de estado pode gerar ações configuradas; o alarme não diagnostica todo problema sozinho.

**Pergunta:** "Como coletar a memória usada pelo EC2?"

**Resposta curta:** Instalar o CloudWatch agent.

**Pergunta:** "Como capturar o tráfego de rede da VPC?"

**Resposta curta:** VPC Flow Logs.

**Pergunta:** "Onde ver logs de aplicação?"

**Resposta curta:** CloudWatch Logs.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [2.6 Compliance e governança](06-compliance-e-governanca.md) · 🏠 [Índice do domínio](README.md) · [2.8 Proteção de rede e aplicações](08-protecao-de-rede-e-aplicacoes.md) ➡️
