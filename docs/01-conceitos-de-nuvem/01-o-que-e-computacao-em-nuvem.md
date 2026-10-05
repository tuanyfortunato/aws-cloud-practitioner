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

---

> **Domínio 1 — Conceitos de Nuvem (24%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

🏠 [Índice do domínio](README.md) · [1.2 As 6 vantagens da computação em nuvem](02-vantagens-da-nuvem.md) ➡️

---

## 1. Entenda as peças e a relação entre elas


Separe três coisas: o equipamento físico, o software básico da máquina e o programa usado pelo negócio. Contratar uma máquina transfere a manutenção do equipamento, mas ainda deixa o sistema e o programa para administrar. Contratar uma plataforma transfere mais tarefas; contratar um software pronto muda novamente a divisão.

Por isso, a pergunta principal não é apenas ‘está na nuvem?’. Pergunte o que foi contratado e o que o cliente continua escolhendo, configurando e protegendo. Os modelos abaixo dão nomes a essa diferença.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é como a **energia elétrica**: você não constrói uma usina em casa; liga na tomada e paga a conta do que consumiu. Os modelos de serviço são como **pizza**: fazer em casa com ingredientes alugados (IaaS), levar a massa pronta e só escolher o recheio (PaaS) ou pedir a pizza pronta (SaaS).

</details>

## 2. Conceitos e opções explicados

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.


**Definição AWS:** entrega de recursos de TI sob demanda, pela internet, com preço pay-as-you-go.


**Modelos de serviço:**

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.
- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **SO:** Software básico da máquina, como Linux ou Windows. Ele administra arquivos, memória e execução de programas; atualizar esse software é diferente de atualizar a aplicação.
- **IaaS:** Infraestrutura como serviço: você obtém recursos como uma máquina virtual e administra o sistema operacional e o software instalado.


  - **IaaS:** você recebe a infraestrutura e gerencia SO e acima. Ex.: EC2, VPC, EBS.
**Antes de ler este trecho:**

- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **Elastic Beanstalk:** O Elastic Beanstalk ajuda a implantar aplicações em plataformas compatíveis, provisionando e coordenando recursos AWS para esse ambiente.
- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **PaaS:** Plataforma como serviço: parte da infraestrutura e do ambiente de execução é administrada para você entregar a aplicação. O código e suas regras continuam sendo do cliente.


  - **PaaS:** você entrega o código; a plataforma cuida do resto. Ex.: Elastic Beanstalk, Lambda (também chamado serverless), RDS.
**Antes de ler este trecho:**

- **Amazon Connect / Connect:** Amazon Connect oferece uma plataforma de contact center em nuvem com canais e recursos compatíveis.
- **SaaS:** Software como serviço: aplicação pronta disponibilizada para uso. O cliente administra seu uso e seus dados conforme a oferta, em vez de construir o software do zero.


  - **SaaS:** software pronto para usar. Ex.: Amazon Connect, WorkSpaces, Gmail.
**Antes de ler este trecho:**

- **implantação:** Colocar uma versão ou conjunto de recursos em funcionamento. O resultado precisa ser observado e, quando necessário, revertido de modo planejado.


**Modelos de implantação:**


  - **Nuvem (cloud-native/all-in):** tudo na nuvem pública.
**Antes de ler este trecho:**

- **Storage Gateway:** Storage Gateway faz a ligação entre o ambiente local e o armazenamento em nuvem usando interfaces de arquivos, volumes ou fitas, conforme a modalidade.
- **VPN:** Conexão lógica protegida que liga usuários ou redes. Um túnel VPN não concede automaticamente acesso a todos os recursos do destino.
- **Direct Connect:** Direct Connect permite estabelecer essa conectividade por conexões e locais compatíveis, com interfaces e rotas configuradas para o ambiente.
- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.
- **híbrido:** Combinação de ambiente próprio e nuvem. É necessário definir quais partes ficam em cada lado e como se comunicam.


  - **Híbrido:** parte on-premises, parte na nuvem, conectadas (VPN, Direct Connect, Storage Gateway, Outposts).
**Antes de ler este trecho:**

- **datacenter:** Instalação física com equipamentos de computação, rede, energia e refrigeração. A nuvem continua dependendo desses equipamentos, mas o cliente não precisa manter o prédio.


  - **On-premises / nuvem privada:** recursos no próprio datacenter, com virtualização e ferramentas de gestão.

**Cai na prova:** "empresa precisa manter dados sensíveis no datacenter, mas quer usar a AWS para o resto" = híbrido.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **CLI / SDK:** SDK fornece bibliotecas para programas chamarem APIs; CLI fornece comandos de texto. As duas formas continuam exigindo identidade, autorização e configuração.
- **servidor:** Computador que atende pedidos de outros computadores. Um servidor web, por exemplo, responde aos pedidos enviados pelo navegador.
- **virtual:** Um recurso virtual é criado por software sobre equipamentos físicos. VM significa máquina virtual: computador lógico com sistema operacional e recursos de processamento.
- **gerenciado:** Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.


**Primeiro, identifique o funcionamento:** A conta identifica o proprietário e a cobrança; serviços entregam recursos por APIs. Você escolhe o nível de gerenciamento: servidor, plataforma ou aplicação pronta. Console, CLI e SDK são formas de pedir operações a essas APIs.

**Depois, compare as escolhas:** Compare o que sua equipe precisa administrar: EC2 entrega a máquina virtual; RDS administra parte do banco; SaaS entrega a aplicação para uso. Híbrido combina ambiente próprio e nuvem.

**Por fim, verifique o limite:** Usar a AWS não transfere automaticamente a responsabilidade pelos dados, acessos e aplicações. Nem todo serviço gerenciado é gratuito ou dispensa configuração.

## 4. Caso resolvido

Uma empresa quer instalar um sistema que exige administrar o Linux. Que modelo atende e quem atualiza o SO?

**Raciocínio e resposta:** IaaS com EC2; o cliente atualiza o SO convidado. Em RDS, esse controle é reduzido porque a AWS administra o sistema do banco.

A resposta muda se mudar o requisito destacado. Compare a necessidade com a função da solução, em vez de apenas associar duas palavras.

## 5. Revisão do capítulo

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Uma escola quer disponibilizar um sistema, mas comprar e manter computadores próprios pode exigir dinheiro e trabalho antes mesmo do primeiro aluno usar.

**2. O que a solução fornece?**

Nuvem é uma forma de obter recursos de tecnologia de um provedor, como a AWS, quando necessário. Você contrata recursos como computadores e armazenamento e administra a parte que cabe a você.

**3. Que conclusão seria incorreta?**

Usar nuvem não significa que tudo está pronto, gratuito ou administrado pelo provedor. Este tópico ensina a reconhecer os modelos e o trabalho que permanece com o cliente.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

**Objetivos de aprendizagem:**

- [ ] Definir nuvem com as três ideias da AWS: **sob demanda**, **pela internet** e **pague pelo uso**.
- [ ] Diferenciar **IaaS, PaaS e SaaS** pelo quanto você ainda gerencia.
- [ ] Reconhecer os modelos de implantação **nuvem, híbrido e on-premises**.

**Dica de revisão para a prova:** Pergunte-se **"o que o cliente ainda gerencia?"**. Sistema operacional → IaaS; só o código → PaaS; nada, só usa → SaaS. Se parte fica no datacenter e parte na AWS, é **híbrido**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-1.md).
**Pergunta:** "Qual modelo de serviço dá mais controle sobre o sistema operacional?"

**Resposta curta:** IaaS (EC2).

**Antes de ler este trecho:**

- **modelo:** Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.


**Fundamento explicado no capítulo:** "Qual modelo de serviço dá mais controle sobre o sistema operacional?" → IaaS (EC2).

**Pergunta:** "Uma empresa quer só enviar o código sem gerenciar infraestrutura. Qual modelo?"

**Resposta curta:** PaaS (Elastic Beanstalk).


**Fundamento explicado no capítulo:** "Uma empresa quer só enviar o código sem gerenciar infraestrutura. Qual modelo?" → PaaS (Elastic Beanstalk).

**Pergunta:** "Qual é um exemplo de SaaS?"

**Resposta curta:** Amazon Connect, WorkSpaces ou um software pronto como e-mail.


**Fundamento explicado no capítulo:** "Qual é um exemplo de SaaS?" → Amazon Connect, WorkSpaces ou um software pronto como e-mail.

**Pergunta:** "Qual modelo de implantação liga o datacenter próprio à AWS?"

**Resposta curta:** Híbrido.


**Fundamento explicado no capítulo:** "Qual modelo de implantação liga o datacenter próprio à AWS?" → Híbrido.

**Pergunta:** "O que caracteriza computação em nuvem?"

**Resposta curta:** Recursos sob demanda, pela internet, pagando pelo uso.


**Fundamento explicado no capítulo:** "O que caracteriza computação em nuvem?" → Recursos sob demanda, pela internet, pagando pelo uso.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

🏠 [Índice do domínio](README.md) · [1.2 As 6 vantagens da computação em nuvem](02-vantagens-da-nuvem.md) ➡️
