# 🃏 Flashcards — Domínio 1 — Conceitos de Nuvem

Clique na pergunta para ver a resposta. Gerado a partir das *Perguntas típicas* de cada tópico (`python3 scripts/gerar_docs.py`).

**Total:** 35 cards


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
<summary>Quais são as seis perspectivas do AWS CAF?</summary>

Negócio, Pessoas, Governança, Plataforma, Segurança e Operações.
</details>

<details>
<summary>Qual perspectiva do CAF trata de cultura, treinamento e gestão da mudança?</summary>

Pessoas, que faz a ponte entre tecnologia e negócio com foco em cultura, estrutura organizacional, liderança e força de trabalho.
</details>

<details>
<summary>Quais são as quatro fases da jornada de transformação do CAF?</summary>

Envision (oportunidades e resultados), Align (lacunas e alinhamento), Launch (pilotos em produção) e Scale (expandir o que funcionou).
</details>

<details>
<summary>Quais resultados de negócio o CAF promete?</summary>

Redução do risco de negócio, melhoria do desempenho ESG, aumento de receita e aumento da eficiência operacional.
</details>

<details>
<summary>Qual é a diferença entre o CAF e o Well-Architected Framework?</summary>

O CAF orienta a organização inteira na adoção da nuvem (pessoas, processos, decisões); o Well-Architected avalia a arquitetura de uma carga de trabalho.
</details>


## [1.6 Estratégias de migração (os 7 Rs)](../docs/01-conceitos-de-nuvem/06-estrategias-de-migracao.md)

<details>
<summary>Quais são os 7 Rs de migração?</summary>

Retire, Retain, Rehost, Relocate, Repurchase, Replatform e Refactor (ou re-architect).
</details>

<details>
<summary>Qual é a diferença entre rehost e replatform?</summary>

Rehost move a aplicação sem alterá-la; replatform move e faz algumas otimizações, como levar o banco para um serviço gerenciado como o Amazon RDS.
</details>

<details>
<summary>Uma empresa troca seu CRM próprio por um produto SaaS. Qual estratégia?</summary>

Repurchase, também chamada de drop and shop: substituir a aplicação por outro produto ou versão.
</details>

<details>
<summary>Por que a AWS não recomenda refactor em migrações grandes?</summary>

Porque é a estratégia mais complexa e cara, já que moderniza a aplicação durante a migração; a recomendação é migrar primeiro e modernizar depois.
</details>

<details>
<summary>Qual serviço replica continuamente um banco de dados durante a migração?</summary>

O AWS Database Migration Service (AWS DMS), que faz migrações únicas ou replica as mudanças para manter origem e destino sincronizados.
</details>


## [1.7 Economia da nuvem](../docs/01-conceitos-de-nuvem/07-economia-da-nuvem.md)

<details>
<summary>Qual é a diferença entre custo fixo e custo variável na nuvem?</summary>

Custo fixo é pago independentemente do uso, como um servidor comprado; custo variável acompanha o consumo, como pagar por hora de instância ligada.
</details>

<details>
<summary>Que custos de um ambiente local costumam ficar de fora de uma comparação simples?</summary>

Espaço, energia, refrigeração, trabalho de montar e manter servidores, licenças e a capacidade ociosa comprada para o pico.
</details>

<details>
<summary>O que é BYOL e quando ele ajuda?</summary>

É trazer as próprias licenças de software para a AWS, dentro dos termos de cada licença; ajuda quando a organização já tem licenças válidas, como de Windows Server ou SQL Server.
</details>

<details>
<summary>O que é rightsizing e qual serviço recomenda tamanhos?</summary>

É ajustar o tipo e o tamanho dos recursos ao uso real; o AWS Compute Optimizer analisa métricas de uso e recomenda tamanhos, além de apontar recursos ociosos.
</details>

<details>
<summary>Qual ferramenta estima o custo de uma arquitetura na AWS antes de construí-la?</summary>

A AWS Pricing Calculator, ferramenta web gratuita para criar estimativas de custo dos serviços da AWS.
</details>
