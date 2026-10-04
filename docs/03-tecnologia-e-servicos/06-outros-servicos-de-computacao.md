# 3.6 Outros serviços de computação

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

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.5 Containers e serverless](05-containers-e-serverless.md) · 🏠 [Índice do domínio](README.md) · [3.7 Bancos de dados](07-bancos-de-dados.md) ➡️
