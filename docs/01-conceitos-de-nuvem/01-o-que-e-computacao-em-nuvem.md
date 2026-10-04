# 1.1 O que é computação em nuvem

> **Domínio 1 — Conceitos de Nuvem (24%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

🏠 [Índice do domínio](README.md) · [1.2 As 6 vantagens da computação em nuvem](02-vantagens-da-nuvem.md) ➡️

---

## 🧠 Antes de começar

> 💡 **Em palavras simples:** Computação em nuvem é **usar computadores, armazenamento e programas de outra empresa pela internet**, na hora em que você precisa, pagando só pelo que usar — em vez de comprar e manter as máquinas.
>
> 🏠 **Analogia:** é como a **energia elétrica**: você não constrói uma usina em casa; liga na tomada e paga a conta do que consumiu. Os modelos de serviço são como **pizza**: fazer em casa com ingredientes alugados (IaaS), levar a massa pronta e só escolher o recheio (PaaS) ou pedir a pizza pronta (SaaS).

**Ao terminar este tópico, você deve saber:**

- [ ] Definir nuvem com as três ideias da AWS: **sob demanda**, **pela internet** e **pague pelo uso**.
- [ ] Diferenciar **IaaS, PaaS e SaaS** pelo quanto você ainda gerencia.
- [ ] Reconhecer os modelos de implantação **nuvem, híbrido e on-premises**.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **On-premises** | no próprio datacenter da empresa ("nas instalações"). |
| **IaaS** | Infraestrutura como Serviço: você recebe a máquina e cuida do sistema operacional para cima. |
| **PaaS** | Plataforma como Serviço: você entrega o código, a plataforma cuida do resto. |
| **SaaS** | Software como Serviço: o programa já vem pronto para usar. |

> 🎯 **Como não errar na prova:** Pergunte-se **"o que o cliente ainda gerencia?"**. Sistema operacional → IaaS; só o código → PaaS; nada, só usa → SaaS. Se parte fica no datacenter e parte na AWS, é **híbrido**.

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

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

🏠 [Índice do domínio](README.md) · [1.2 As 6 vantagens da computação em nuvem](02-vantagens-da-nuvem.md) ➡️
