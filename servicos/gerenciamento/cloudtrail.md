# AWS CloudTrail

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Um recurso foi alterado e a equipe precisa descobrir qual identidade realizou a ação, quando e por qual chamada AWS.

**Como este serviço ajuda?** CloudTrail registra atividades e chamadas compatíveis realizadas na conta. Ele ajuda a auditar ações, conforme a cobertura configurada.

**Exemplo do dia a dia:** A equipe investiga quem solicitou uma alteração num recurso e consulta o evento correspondente no CloudTrail.

**O que ele não resolve sozinho?** Ele não é o registro de todo erro dentro do seu programa. Diferentes tipos de evento e retenção têm condições próprias; não presuma que todo acesso foi registrado do mesmo modo.

**Primeiras palavras para entender:**

- **Evento:** registro de uma atividade.
- **API:** interface usada para operar serviços.
- **Auditoria:** exame de ações e evidências.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Gerenciamento / auditoria · **Domínio:** 2 · **Escopo:** Regional (trails multi-região e de organização) · **Tópico do guia:** [2.7 Logs, monitoramento e auditoria](../../docs/02-seguranca-e-conformidade/07-logs-monitoramento-e-auditoria.md)
>
> **Em uma frase:** registra as **chamadas de API** da conta — quem fez, o quê, quando, de onde e em qual recurso.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **log:** Registro de acontecimentos para análise. A aplicação e os serviços podem produzir registros diferentes; é necessário definir coleta, retenção e acesso.
- **evento:** Informação sobre algo que aconteceu. Uma regra pode encaminhar o evento; outro componente realiza a ação de negócio.

**Passo 1.** Determine quais atividades e tipos de evento precisam ser registrados e conservados.

**Passo 2.** Configure a cobertura e consulte eventos para examinar ações realizadas por identidades.

**Passo 3.** Proteja e analise os registros. Um evento de API não é o mesmo que uma linha de log emitida dentro do seu programa.

## 2. Recursos e opções, com significado

### Tipos de eventos

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **CloudTrail:** Registro de atividades e chamadas AWS compatíveis. Ajuda a analisar quem realizou uma operação, em vez de medir sozinho a velocidade da aplicação.
- **volume:** Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.

| Tipo | Exemplo | Registrado por padrão? |
|---|---|---|
| **Management events** | `RunInstances`, `CreateBucket`, `AttachRolePolicy`, login no console | ✅ (Event history) |
| **Data events** | `GetObject`/`PutObject` no S3, `Invoke` no Lambda, itens do DynamoDB | ❌ — ativar no trail (pago, alto volume) |
| **Network activity events** | Chamadas via VPC endpoints | ❌ — opcional |
| **Insights events** | Picos anormais de chamadas/erros de API | ❌ — ativar CloudTrail Insights (pago) |

### Configurações

**Antes de ler este trecho:**

- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.
- **EventBridge:** EventBridge recebe eventos e usa regras para encaminhá-los a destinos compatíveis.
- **região:** Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
- **retenção:** Tempo durante o qual dados ou registros são conservados. Depois desse prazo, o comportamento depende das regras do serviço e das configurações.
- **política:** Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.
- **MFA:** Verificação adicional de autenticação, além da primeira credencial. Ela protege a entrada, mas não concede permissões por si só.
- **SSE-S3 / SSE-KMS:** Formas de criptografia no servidor do S3, que diferem na origem e administração das chaves e, no último caso, nas camadas. A tabela da seção distingue essas escolhas.
- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.
- **bucket:** Recipiente que organiza objetos no S3. A aplicação usa o bucket e a identificação do objeto para pedir operações autorizadas.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.

| Item | Detalhe |
|---|---|
| **Event history** | 📌 **90 dias** de management events, **grátis**, sem configurar nada (por região). |
| **Trail** | Envia eventos continuamente para um **bucket S3** (e opcionalmente CloudWatch Logs e EventBridge) → retenção longa. Pode ser **multi-região** e de **organização** (todas as contas). |
| **Log file integrity validation** ✔️ | Arquivos *digest* com hash para provar que os logs não foram alterados. |
| **Criptografia** | SSE-S3 por padrão; SSE-KMS opcional. |
| **CloudTrail Lake** | Data store gerenciado com **consultas SQL** e retenção longa. 🔄 Fechado a novos clientes desde **31/05/2026** (anúncio de 31/03/2026; uma verificação anterior citava 30/04/2026). Trails e Event history continuam. |
| **Proteção dos logs** | Bucket com Object Lock/MFA Delete, política restrita, conta de logs separada. |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele não é o registro de todo erro dentro do seu programa. Diferentes tipos de evento e retenção têm condições próprias; não presuma que todo acesso foi registrado do mesmo modo.

### ⚠️ Não confundir

**Antes de ler este trecho:**

- **Config:** Serviço que acompanha configurações e suas avaliações em recursos compatíveis. Observar configuração é diferente de observar uma métrica de desempenho.

CloudTrail (**ações**: quem fez) × Config (**estado**: como estava) × CloudWatch (**desempenho**).

**Antes de ler este trecho:**

- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **tráfego:** Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.

CloudTrail registra **chamadas de API**, não o tráfego de rede (isso é VPC Flow Logs).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Event history e **primeira cópia** dos management events num trail: grátis. Pagos: cópias adicionais, data events, Insights, Lake.

## 5. Caso resolvido: ligando as peças

A equipe investiga quem solicitou uma alteração num recurso e consulta o evento correspondente no CloudTrail.

**Aplicando a sequência à situação:**

**Etapa 1:** Determine quais atividades e tipos de evento precisam ser registrados e conservados.
**Etapa 2:** Configure a cobertura e consulte eventos para examinar ações realizadas por identidades.
**Etapa 3:** Proteja e analise os registros. Um evento de API não é o mesmo que uma linha de log emitida dentro do seu programa.

**Resultado e responsabilidade:** CloudTrail registra atividades e chamadas compatíveis realizadas na conta. Ele ajuda a auditar ações, conforme a cobertura configurada.

**Recursos envolvidos:** Eventos de gerenciamento/dados, event history e trails.

**Decisões que precisam ser tomadas:** Cobertura, regiões, destino e retenção.

**Antes de ler este trecho:**

- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.

**Outra situação comentada:** Descobrir quem alterou IAM: CloudTrail; gravar trilha e retenção conforme auditoria.

**Por que não concluir mais do que isso:** Eventos de dados têm configuração própria; não é histórico infinito gratuito de todo acesso

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Quem encerrou a instância e quando?"

**Resposta curta:** CloudTrail.

**Pergunta:** "Por quanto tempo o CloudTrail guarda eventos sem configurar nada?"

**Resposta curta:** 90 dias.

**Pergunta:** "Guardar logs de API por anos."

**Resposta curta:** Trail → S3.

**Pergunta:** "Provar que os logs não foram adulterados."

**Resposta curta:** Log file integrity validation.

**Pergunta:** "Auditar leituras de objetos do S3."

**Resposta curta:** Data events.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
