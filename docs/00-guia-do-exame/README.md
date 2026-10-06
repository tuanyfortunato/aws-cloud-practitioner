# Guia do Exame — AWS Certified Cloud Practitioner (CLF-C02)

<!-- didatico:inicio -->
## 🧭 Antes de ler

**Por que esta página existe?** Você quer estudar AWS, mas precisa saber o que a certificação avalia e por onde começar.

**Como usar?** Esta página apresenta o exame e organiza os caminhos de estudo. Comece pela ideia de nuvem, siga pelos quatro domínios e use as fichas para entender cada serviço.

**Exemplo:** Se você ainda não sabe o que é um servidor, não precisa começar decorando siglas: leia a abertura do primeiro tópico e avance com os exemplos.
<!-- didatico:fim -->

> Confira sempre o [exam guide oficial](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html) e a [lista de serviços no escopo](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html) na semana da prova.
> O código continua **CLF-C02**, mas a AWS atualiza o conteúdo do guia **sem trocar o código** (última verificação: 04/10/2026, [detalhes](../../fontes/verificacao-fontes-oficiais-2026-10.md)).

## 🧭 Em resumo (leia primeiro)

> 💡 **Em palavras simples:** a Cloud Practitioner é a certificação **de entrada** da AWS. Ela não testa se você sabe
> configurar nada: testa se você **entende a nuvem** e **reconhece qual serviço resolve cada situação**.

📝 **Como é:** 65 questões em 90 minutos; você precisa de **700 de 1000** pontos no total.

📚 **O que cai:** 4 domínios — conceitos de nuvem, segurança, serviços e cobrança (pesos na tabela abaixo).

✅ **Chute vale:** resposta em branco conta como erro, então **nunca deixe questão sem resposta**.

🗺️ **Por onde começar:** leia esta página → siga o [plano de estudos](plano-de-estudos.md) → confira o

  [escopo oficial](escopo-oficial.md) para saber o que **não** precisa estudar.

## Formato

**Antes de ler este trecho:**

- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.

| Item | Detalhe |
|---|---|
| Código | CLF-C02 (o guia atual não mostra número de versão) |
| Custo | US$ 100 |
| Questões | 65 (50 pontuadas + 15 de teste, **não identificadas**) |
| Tipos | Múltipla escolha (1 correta e 3 distratores) e múltipla resposta (2 ou mais corretas entre 5 ou mais opções; o enunciado diz quantas) |
| Duração | 90 minutos |
| Acomodação ESL +30 | Quem faz em inglês sem ser nativo pode pedir **+30 min** antes de agendar |
| Nota mínima | **700 de 1000**, modelo **compensatório** (vale o total, não cada domínio) |
| Em branco | Conta como erro; **chute não é penalizado** — nunca deixe sem resposta |
| Idiomas | Inclui português (Brasil); italiano e alemão saem após 31/12/2026 |
| Aplicação | Centro Pearson VUE ou online supervisionado |
| Validade | 3 anos |

## Domínios e pesos

**Antes de ler este trecho:**

- **conformidade:** Atendimento a requisitos definidos. Usar um serviço com certificações não torna automaticamente a aplicação do cliente conforme.
- **suporte:** Suporte oferece ajuda conforme um plano e suas condições. Um prazo de resposta inicial não é garantia de tempo de resolução de todo incidente.

| Domínio | Peso | Tópicos |
|---|---|---|
| 1. Conceitos de Nuvem | 24% | [01-conceitos-de-nuvem](../01-conceitos-de-nuvem/README.md) |
| 2. Segurança e Conformidade | 30% | [02-seguranca-e-conformidade](../02-seguranca-e-conformidade/README.md) |
| 3. Tecnologia e Serviços de Nuvem | 34% | [03-tecnologia-e-servicos](../03-tecnologia-e-servicos/README.md) |
| 4. Cobrança, Preços e Suporte | 12% | [04-cobranca-precos-e-suporte](../04-cobranca-precos-e-suporte/README.md) |

## O que a prova cobra (e o que não cobra)

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.

Avalia: **explicar o valor da nuvem**, entender **custos, economia e cobrança** e **identificar serviços AWS para casos de uso comuns**.

**Antes de ler este trecho:**

- **carga:** Aplicação ou conjunto de tarefas com seus recursos e necessidades. Avaliar uma carga significa avaliar o trabalho completo, não uma única máquina isolada.

Fora do escopo: codificação, design de arquitetura, troubleshooting, implementação e testes de carga.

**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **Fargate:** Fargate fornece a capacidade para executar containers com ECS ou EKS, sem você administrar diretamente os servidores dessa execução.
- **Batch:** O AWS Batch organiza trabalhos em filas e fornece capacidade de computação para executá-los conforme as configurações.

Por isso, números aparecem quase sempre como **diferenciadores** ("15 min" separa Lambda de Batch/Fargate; "2 minutos" identifica Spot), não como cálculo. Veja [números-âncora](../../resumos/numeros-ancora.md).

**Antes de ler este trecho:**

- **MSK:** Kafka é uma plataforma de fluxo de eventos; MSK é a oferta gerenciada compatível da AWS. A aplicação ainda precisa produzir e consumir os registros.

**Task statements oficiais, serviços no escopo e fora do escopo:** ver [escopo oficial](escopo-oficial.md). Vários serviços saíram da lista (ex.: AWS IQ, Wavelength, CloudShell, CodeDeploy, Transfer Family, MSK) e alternativas com eles tendem a ser distratores.

## Documentos desta pasta

[Plano de estudos](plano-de-estudos.md)

[Escopo oficial: task statements e serviços dentro/fora da prova](escopo-oficial.md)

[O que mudou em 2025-2026 (valor da prova × valor atual)](atualizacoes-2025-2026.md)

[Pendências de verificação](pendencias-de-verificacao.md) — o que ainda não foi conferido em fonte oficial

## Dicas para o dia da prova

**Antes de ler este trecho:**

- **alta disponibilidade:** Planejamento para manter o sistema acessível diante de determinadas falhas. Não é promessa de ausência de qualquer interrupção.

Leia a pergunta inteira antes das alternativas e procure a **palavra-chave** ("mais barato", "menor esforço operacional", "alta disponibilidade") — ver [palavras-chave](../../resumos/palavras-chave.md).

Elimine as alternativas claramente erradas primeiro; desconfie de serviços fora do escopo.

Use **marcar para revisão** e volte depois.

Planos de suporte: a task 4.3 consultada ainda cita modelos clássicos, e a página comercial mostra planos novos. Distinga o contexto e leia o requisito; não escolha apenas por um nome ou número atual ([detalhes](atualizacoes-2025-2026.md)).

Ao final, revise as marcadas com o tempo restante.

## Informações da minha prova

**Data agendada:**

**Local / online:**

**Resultado:**
