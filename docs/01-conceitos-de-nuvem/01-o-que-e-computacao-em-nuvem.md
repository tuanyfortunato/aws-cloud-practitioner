# 1.1 O que é computação em nuvem

## 🧠 Antes de começar

**Qual é a dificuldade?** Uma escola quer disponibilizar um sistema, mas comprar e manter computadores próprios pode exigir dinheiro e trabalho antes mesmo do primeiro aluno usar.

**A ideia em palavras simples:** Nuvem é uma forma de obter recursos de tecnologia de um provedor, como a AWS, quando necessário. Você contrata recursos como computadores e armazenamento e administra a parte que cabe a você.

**Exemplo do dia a dia:** Em vez de comprar uma máquina física, a escola cria um servidor virtual na AWS e instala seu sistema. Outra opção é contratar um software pronto; a responsabilidade muda conforme o modelo.

**O que não concluir?** Usar nuvem não significa que tudo está pronto, gratuito ou administrado pelo provedor. Este tópico ensina a reconhecer os modelos e o trabalho que permanece com o cliente.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **On-premises** | no próprio datacenter da empresa ("nas instalações"). |
| **IaaS** | Infraestrutura como Serviço: você recebe a máquina e cuida do sistema operacional para cima. |
| **PaaS** | Plataforma como Serviço: você entrega o código, a plataforma cuida do resto. |
| **SaaS** | Software como Serviço: o programa já vem pronto para usar. |

**Ao terminar este tópico, você deve saber:**

- [ ] Definir nuvem com as três ideias da AWS: **sob demanda**, **pela internet** e **pague pelo uso**.
- [ ] Diferenciar **IaaS, PaaS e SaaS** pelo quanto você ainda gerencia.
- [ ] Reconhecer os modelos de implantação **nuvem, híbrido e on-premises**.

<details>
<summary>Uma analogia para revisar a ideia</summary>

é como a **energia elétrica**: você não constrói uma usina em casa; liga na tomada e paga a conta do que consumiu. Os modelos de serviço são como **pizza**: fazer em casa com ingredientes alugados (IaaS), levar a massa pronta e só escolher o recheio (PaaS) ou pedir a pizza pronta (SaaS).

</details>

> 🎯 **Como não errar na prova:** Pergunte-se **"o que o cliente ainda gerencia?"**. Sistema operacional → IaaS; só o código → PaaS; nada, só usa → SaaS. Se parte fica no datacenter e parte na AWS, é **híbrido**.

---

> **Domínio 1 — Conceitos de Nuvem (24%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

🏠 [Índice do domínio](README.md) · [1.2 As 6 vantagens da computação em nuvem](02-vantagens-da-nuvem.md) ➡️

---

## 📖 Conteúdo

- **Definição AWS:** entrega de recursos de TI sob demanda, pela internet, com preço pay-as-you-go.
- **Modelos de serviço:**
  - **IaaS:** você recebe a infraestrutura e gerencia SO e acima. Ex.: EC2, VPC, EBS.
  - **PaaS:** você entrega o código; a plataforma cuida do resto. Ex.: Elastic Beanstalk, Lambda (também chamado serverless), RDS.
  - **SaaS:** software pronto para usar. Ex.: Amazon Connect, WorkSpaces, Gmail.
- **Modelos de implantação:**
  - **Nuvem (cloud-native/all-in):** tudo na nuvem pública.
  - **Híbrido:** parte on-premises, parte na nuvem, conectadas (VPN, Direct Connect, Storage Gateway, Outposts).
  - **On-premises / nuvem privada:** recursos no próprio datacenter, com virtualização e ferramentas de gestão.
- **Cai na prova:** "empresa precisa manter dados sensíveis no datacenter, mas quer usar a AWS para o resto" = híbrido.

## ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-1.md).

- "Qual modelo de serviço dá mais controle sobre o sistema operacional?" → IaaS (EC2).
- "Uma empresa quer só enviar o código sem gerenciar infraestrutura. Qual modelo?" → PaaS (Elastic Beanstalk).
- "Qual é um exemplo de SaaS?" → Amazon Connect, WorkSpaces ou um software pronto como e-mail.
- "Qual modelo de implantação liga o datacenter próprio à AWS?" → Híbrido.
- "O que caracteriza computação em nuvem?" → Recursos sob demanda, pela internet, pagando pelo uso.

<!-- aprofundamento:inicio -->
## 🔬 Aprofundamento para a prova — sem abrir o console

**Como funciona:** A conta identifica o proprietário e a cobrança; serviços entregam recursos por APIs. Você escolhe o nível de gerenciamento: servidor, plataforma ou aplicação pronta. Console, CLI e SDK são formas de pedir operações a essas APIs.

**Como escolher:** Compare o que sua equipe precisa administrar: EC2 entrega a máquina virtual; RDS administra parte do banco; SaaS entrega a aplicação para uso. Híbrido combina ambiente próprio e nuvem.

**O que não concluir:** Usar a AWS não transfere automaticamente a responsabilidade pelos dados, acessos e aplicações. Nem todo serviço gerenciado é gratuito ou dispensa configuração.

### Exercício de decisão

Uma empresa quer instalar um sistema que exige administrar o Linux. Que modelo atende e quem atualiza o SO?

<details>
<summary>Resposta e por que as alternativas confundem</summary>

IaaS com EC2; o cliente atualiza o SO convidado. Em RDS, esse controle é reduzido porque a AWS administra o sistema do banco.

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

🏠 [Índice do domínio](README.md) · [1.2 As 6 vantagens da computação em nuvem](02-vantagens-da-nuvem.md) ➡️
