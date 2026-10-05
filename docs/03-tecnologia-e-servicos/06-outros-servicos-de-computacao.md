# 3.6 Outros serviços de computação

## 🧠 Antes de começar

**Qual é a dificuldade?** Nem toda necessidade pede administrar uma máquina diretamente. Você pode querer uma hospedagem simples, uma implantação facilitada ou muitos trabalhos em lote.

**A ideia em palavras simples:** Este tópico compara formas de execução: Lightsail simplifica ofertas, Beanstalk apoia a implantação de aplicações e Batch organiza trabalhos. Opções de proximidade atendem necessidades específicas de localização.

**Exemplo do dia a dia:** Um site pequeno pode avaliar Lightsail; uma aplicação com plataforma compatível, Beanstalk; centenas de conversões de arquivos, Batch.

**O que não concluir?** Esses serviços não fazem o mesmo trabalho. Escolha pelo tipo de tarefa e pela responsabilidade desejada, verificando compatibilidade e escopo.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **PaaS** | plataforma onde você entrega o código e ela cuida da infraestrutura. |
| **Job em lote (batch)** | trabalho processado sem interação, em grande quantidade. |

**Ao terminar este tópico, você deve saber:**

- [ ] Saber que o **Elastic Beanstalk** é PaaS e não tem custo adicional (paga os recursos criados).
- [ ] Saber que o **Lightsail** tem **preço mensal fixo** e é para quem está começando.
- [ ] Saber que o **Batch** escolhe a computação ideal para jobs em lote.

<details>
<summary>Uma analogia para revisar a ideia</summary>

o **Elastic Beanstalk** é um **buffet** (você leva a receita e eles montam tudo); o **Lightsail** é um **plano pré-pago** de servidor; o **Batch** é uma **linha de produção** que processa milhares de pedidos.

</details>

> 🎯 **Como não errar na prova:** "Desenvolvedor sem pensar em infraestrutura" → **Elastic Beanstalk**. "Preço fixo, simples" → **Lightsail**. "Milhares de jobs" → **Batch**.

---

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [AWS Elastic Beanstalk](../../servicos/computacao/elastic-beanstalk.md) · [Amazon Lightsail](../../servicos/computacao/lightsail.md) · [AWS Batch](../../servicos/computacao/batch.md) · [AWS Outposts, Local Zones e Wavelength](../../servicos/computacao/outposts-local-zones-wavelength.md)

⬅️ [3.5 Containers e serverless](05-containers-e-serverless.md) · 🏠 [Índice do domínio](README.md) · [3.7 Bancos de dados](07-bancos-de-dados.md) ➡️

---

## 📖 Conteúdo

- **AWS Elastic Beanstalk:** PaaS. Você envia o código (Java, .NET, Node.js, Python, PHP, Ruby, Go, Docker) e ele provisiona e gerencia capacidade, load balancer, Auto Scaling e monitoramento. Você mantém acesso aos recursos. Não tem custo adicional; paga só os recursos criados.
- **Amazon Lightsail:** servidores virtuais simples com **preço mensal fixo e previsível** (inclui computação, armazenamento e transferência). Bom para sites WordPress, apps pequenos e quem está começando.
- **AWS Batch:** executa grandes volumes de **jobs em lote**, provisionando a computação ideal automaticamente (EC2, Spot ou Fargate).
- **AWS Outposts:** ver [3.2](02-infraestrutura-global.md).
- **Cai na prova:** "desenvolvedor quer subir aplicação web sem pensar em infraestrutura" = Elastic Beanstalk; "pequena empresa quer servidor com preço fixo" = Lightsail; "milhares de jobs de processamento" = Batch.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).

- "Desenvolvedor quer só subir o código Java e deixar a AWS cuidar de capacidade e balanceamento." → Elastic Beanstalk.
- "Elastic Beanstalk tem custo próprio?" → Não; paga-se só os recursos que ele cria.
- "Site WordPress simples com preço mensal fixo." → Lightsail.
- "Processar milhares de jobs em lote com a capacidade ideal." → AWS Batch.

<!-- aprofundamento:inicio -->
## 🔬 Aprofundamento para a prova — sem abrir o console

**Como funciona:** Beanstalk implanta uma aplicação e gerencia recursos do ambiente; Lightsail simplifica infraestrutura em pacotes; Batch organiza trabalhos em filas; Outposts leva infraestrutura AWS ao local do cliente.

**Como escolher:** Enviar aplicação web com menor esforço operacional: Beanstalk. Projeto simples com pacote: Lightsail. Lotes e jobs: Batch. Exigência local com serviços AWS compatíveis: Outposts.

**O que não concluir:** Beanstalk não dispensa manutenção do código; Batch não é endpoint web interativo. Outposts ainda exige infraestrutura física e conectividade do cliente.

### Exercício de decisão

Uma equipe quer executar milhares de simulações independentes, que terminam após o trabalho. Qual serviço combina com isso?

<details>
<summary>Resposta e por que as alternativas confundem</summary>

AWS Batch: filas, definições de jobs e ambientes de computação. Um balanceador distribui tráfego, mas não agenda essa carga de lotes.

</details>

**Verifique seu entendimento:** explique a escolha em voz alta e cite uma condição que mudaria a resposta. Nomear um serviço sem explicar o motivo ainda não demonstra domínio.

> Escopo e limites de estudo: [como estudar sem console](../00-guia-do-exame/estudar-sem-console.md). Os cenários são autorais; não são questões oficiais nem previsão do que cairá.
<!-- aprofundamento:fim -->

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.5 Containers e serverless](05-containers-e-serverless.md) · 🏠 [Índice do domínio](README.md) · [3.7 Bancos de dados](07-bancos-de-dados.md) ➡️
