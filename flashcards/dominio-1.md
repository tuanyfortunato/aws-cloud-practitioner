# 🃏 Flashcards — Domínio 1 — Conceitos de Nuvem

Clique na pergunta para ver a resposta. Gerado a partir das *Perguntas típicas* de cada tópico (`python3 scripts/gerar_docs.py`).

**Total:** 42 cards


## [1.1 O que é computação em nuvem](../docs/01-conceitos-de-nuvem/01-o-que-e-computacao-em-nuvem.md)

<details>
<summary>Como a AWS define computação em nuvem?</summary>

Como a entrega sob demanda de recursos de TI, como computação, bancos de dados, armazenamento e aplicações, pela internet, com preço pago pelo uso.
</details>

<details>
<summary>Qual é a diferença entre IaaS, PaaS e SaaS?</summary>

É quanto o provedor administra. No IaaS, o provedor entrega rede, computadores e armazenamento, e o cliente cuida do sistema operacional para cima. No PaaS, o provedor também cuida do hardware e do sistema operacional, e o cliente cuida da aplicação. No SaaS, o provedor entrega um produto completo, e o cliente só o usa.
</details>

<details>
<summary>O que quer dizer serverless?</summary>

Que o cliente roda código ou usa um serviço sem provisionar nem administrar servidores. No AWS Lambda, a AWS cuida da manutenção dos servidores, da capacidade, do escalonamento e dos patches.
</details>

<details>
<summary>Uma empresa mantém dados no próprio datacenter e usa a AWS para o resto, com os dois lados conectados. Qual é o modelo de implantação?</summary>

Híbrido: recursos na nuvem e recursos fora dela, conectados.
</details>

<details>
<summary>Por que usar a nuvem não tira toda a responsabilidade do cliente?</summary>

Porque o provedor assume o hardware e, dependendo do modelo, outras camadas, mas o cliente continua decidindo e configurando o que coloca na nuvem, como dados, acessos e, no IaaS, o sistema operacional.
</details>


## [1.2 As 6 vantagens da computação em nuvem](../docs/01-conceitos-de-nuvem/02-vantagens-da-nuvem.md)

<details>
<summary>Quais são as seis vantagens da computação em nuvem segundo a AWS?</summary>

Trocar despesa fixa por variável, beneficiar-se de economias de escala, parar de adivinhar a capacidade, aumentar a velocidade e a agilidade, parar de gastar com datacenters e tornar-se global em minutos.
</details>

<details>
<summary>Uma loja tem servidores ociosos o ano todo, exceto na Black Friday. Qual vantagem resolve isso?</summary>

Parar de adivinhar a capacidade: na nuvem, a loja aumenta a capacidade no pico e reduz depois, pagando só pelo que usa.
</details>

<details>
<summary>Por que a AWS consegue preços menores que uma empresa sozinha?</summary>

Pelas economias de escala: o uso de centenas de milhares de clientes é somado, o que permite custos menores, repassados no preço por uso.
</details>

<details>
<summary>O que quer dizer trocar CapEx por OpEx?</summary>

Trocar o investimento antecipado em equipamento (despesa de capital) por gastos contínuos de acordo com o uso (despesa operacional). É a vantagem de trocar despesa fixa por variável.
</details>

<details>
<summary>Como a nuvem ajuda a atender usuários em outros continentes?</summary>

Permitindo implantar a aplicação em várias Regiões do mundo com poucos cliques, mais perto dos usuários, o que reduz a latência. É a vantagem de tornar-se global em minutos.
</details>


## [1.3 Conceitos de arquitetura que a prova cobra](../docs/01-conceitos-de-nuvem/03-conceitos-de-arquitetura.md)

<details>
<summary>Qual é a diferença entre escala vertical e horizontal?</summary>

Escala vertical é usar uma instância maior; escala horizontal é adicionar mais instâncias e dividir o trabalho entre elas.
</details>

<details>
<summary>O que a elasticidade tem a mais que a escalabilidade?</summary>

A elasticidade ajusta a capacidade para cima e para baixo acompanhando a demanda, de preferência automaticamente; a escalabilidade é só a capacidade de crescer.
</details>

<details>
<summary>Uma aplicação roda em uma única instância EC2. Ela tem alta disponibilidade?</summary>

Não. Alta disponibilidade exige componentes redundantes em locais que não falham juntos, como instâncias em mais de uma Zona de Disponibilidade.
</details>

<details>
<summary>O que significam RTO e RPO?</summary>

RTO é o tempo máximo aceitável entre a interrupção e a restauração do serviço; RPO é o tempo máximo aceitável desde o último ponto de recuperação dos dados, ou seja, quantos dados se aceita perder.
</details>

<details>
<summary>Qual é a diferença entre pilot light e warm standby?</summary>

No pilot light, só os dados e o núcleo da infraestrutura ficam ligados, e a aplicação precisa ser ativada antes de atender; no warm standby, uma cópia reduzida e funcional já atende tráfego.
</details>


## [1.4 AWS Well-Architected Framework](../docs/01-conceitos-de-nuvem/04-well-architected-framework.md)

<details>
<summary>Quais são os seis pilares do Well-Architected Framework?</summary>

Excelência operacional, segurança, confiabilidade, eficiência de performance, otimização de custos e sustentabilidade.
</details>

<details>
<summary>"Escalar horizontalmente para reduzir o impacto de uma única falha" é princípio de qual pilar?</summary>

Confiabilidade, que também inclui recuperar-se automaticamente de falhas, testar a recuperação, parar de adivinhar capacidade e gerenciar mudanças com automação.
</details>

<details>
<summary>"Fazer mudanças frequentes, pequenas e reversíveis" pertence a qual pilar?</summary>

Excelência operacional, o pilar de operar e evoluir a carga de trabalho, junto com observabilidade, automação e aprendizado com os eventos.
</details>

<details>
<summary>O que o pilar de sustentabilidade recomenda sobre utilização dos recursos?</summary>

Maximizar a utilização: dimensionar corretamente e evitar recursos ociosos, porque poucos servidores bem usados gastam menos energia que muitos subutilizados.
</details>

<details>
<summary>Para que serve a AWS Well-Architected Tool?</summary>

Para revisar e medir uma carga de trabalho com base no framework, documentar decisões, receber recomendações e acompanhar melhorias, sem cobrança adicional.
</details>


## [1.5 AWS Cloud Adoption Framework (CAF)](../docs/01-conceitos-de-nuvem/05-cloud-adoption-framework.md)

<details>
<summary>Qual perspectiva do CAF trata de treinamento, cultura e mudança organizacional?</summary>

People.
</details>

<details>
<summary>Qual perspectiva garante que a estratégia de nuvem gere valor de negócio?</summary>

Business.
</details>

<details>
<summary>Qual perspectiva cuida de risco, orçamento e gestão do programa?</summary>

Governance.
</details>

<details>
<summary>Qual perspectiva trata da arquitetura e da plataforma técnica?</summary>

Platform.
</details>

<details>
<summary>Qual perspectiva trata de identidade, proteção de dados e resposta a incidentes?</summary>

Security.
</details>

<details>
<summary>Qual perspectiva trata de monitoramento e gestão de incidentes operacionais?</summary>

Operations.
</details>

<details>
<summary>Quais são as fases da jornada de transformação?</summary>

Envision, Align, Launch e Scale.
</details>

<details>
<summary>Qual é um benefício do CAF?</summary>

Reduzir risco de negócio, melhorar ESG, aumentar receita ou eficiência operacional.
</details>


## [1.6 Estratégias de migração (os 7 Rs)](../docs/01-conceitos-de-nuvem/06-estrategias-de-migracao.md)

<details>
<summary>Migrar servidores para EC2 sem mudar nada.</summary>

Rehost.
</details>

<details>
<summary>Migrar o banco para RDS para reduzir administração, sem mudar a aplicação.</summary>

Replatform.
</details>

<details>
<summary>Trocar o sistema próprio por um produto SaaS.</summary>

Repurchase.
</details>

<details>
<summary>Reescrever a aplicação para usar Lambda e microsserviços.</summary>

Refactor.
</details>

<details>
<summary>Desligar aplicações que ninguém usa.</summary>

Retire.
</details>

<details>
<summary>Manter a aplicação no datacenter por exigência regulatória.</summary>

Retain.
</details>

<details>
<summary>Qual estratégia é a mais rápida?</summary>

Rehost.
</details>

<details>
<summary>Qual traz mais benefícios de nuvem a longo prazo?</summary>

Refactor.
</details>


## [1.7 Economia da nuvem](../docs/01-conceitos-de-nuvem/07-economia-da-nuvem.md)

<details>
<summary>Qual custo deixa de existir ao migrar para a AWS?</summary>

Custos de datacenter (energia, refrigeração, espaço físico, compra de hardware).
</details>

<details>
<summary>Qual custo continua sendo do cliente na nuvem?</summary>

Gestão das aplicações e dos dados, licenças não incluídas, uso dos recursos.
</details>

<details>
<summary>Como reduzir custo de licenças ao migrar?</summary>

BYOL com Dedicated Hosts, ou usar instâncias com licença incluída.
</details>

<details>
<summary>Qual ferramenta ajuda a montar o caso de negócio (TCO) da migração?</summary>

Migration Evaluator.
</details>

<details>
<summary>Qual prática ajusta recursos ao uso real?</summary>

Rightsizing.
</details>

<details>
<summary>Por que serviços gerenciados reduzem o TCO?</summary>

Diminuem o trabalho operacional (patches, backups, hardware).
</details>
