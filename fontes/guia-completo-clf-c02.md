# Guia completo — AWS Cloud Practitioner (CLF-C02)

Oct 3, 2026 · @Tuany Fortunato

**Guia de estudo completo, com perguntas típicas por tópico**

| Certificação | AWS Certified Cloud Practitioner |
| --- | --- |
| Código da prova | CLF-C02 |
| Duração | 90 minutos (quem faz em inglês sem ser nativo pode pedir +30 min, a acomodação ESL +30) |
| Questões | 65 (50 pontuadas + 15 de teste) |
| Nota mínima | 700 de 1000 |
| Domínios | Cloud Concepts 24% · Segurança e Compliance 30% · Tecnologia e Serviços 34% · Billing, Pricing e Suporte 12% |

---

## Sumário

1. **Visão geral da prova**
2. **Domínio 1 — Cloud Concepts (24%)**
   1. 1.1 O que é computação em nuvem
   2. 1.2 As 6 vantagens da computação em nuvem
   3. 1.3 Conceitos de arquitetura que a prova cobra
   4. 1.4 AWS Well-Architected Framework
   5. 1.5 AWS Cloud Adoption Framework (CAF)
   6. 1.6 Estratégias de migração (os 7 Rs)
   7. 1.7 Economia da nuvem
3. **Domínio 2 — Segurança e Compliance (30%)**
   1. 2.1 Modelo de responsabilidade compartilhada
   2. 2.2 Usuário root
   3. 2.3 AWS IAM
   4. 2.4 Governança multi-conta
   5. 2.5 Criptografia
   6. 2.6 Compliance e governança
   7. 2.7 Logs, monitoramento e auditoria
   8. 2.8 Proteção de rede e aplicações
   9. 2.9 Detecção de ameaças e postura de segurança
   10. 2.10 Outros pontos de segurança
4. **Domínio 3 — Tecnologia e Serviços (34%)**
   1. 3.1 Formas de acessar e implantar na AWS
   2. 3.2 Infraestrutura global
   3. 3.3 Amazon EC2
   4. 3.4 Escalabilidade e balanceamento de carga
   5. 3.5 Containers e serverless
   6. 3.6 Outros serviços de computação
   7. 3.7 Bancos de dados
   8. 3.8 Amazon S3
   9. 3.9 Outros serviços de armazenamento
   10. 3.10 Rede e entrega de conteúdo
   11. 3.11 Analytics
   12. 3.12 IA e machine learning
   13. 3.13 Integração de aplicações
   14. 3.14 Aplicações de negócio, usuário final, front-end e IoT
   15. 3.15 Ferramentas de desenvolvimento
   16. 3.16 Gestão e governança
   17. 3.17 Migração e transferência
5. **Domínio 4 — Billing, Pricing e Suporte (12%)**
   1. 4.1 Princípios de preço da AWS
   2. 4.2 Modelos de compra do EC2
   3. 4.3 Como outros recursos são cobrados
   4. 4.4 Ferramentas de custo e faturamento
   5. 4.5 Planos de AWS Support
   6. 4.6 Outros recursos de ajuda
6. **Serviços menos conhecidos que podem aparecer**
7. **Pares que confundem e palavras-chave**
8. **Fontes**

---

## Visão geral da prova

São 65 questões em 90 minutos: 50 pontuadas e 15 de teste não identificadas. Nota mínima 700 de 1000, no modelo compensatório (vale o total, não cada domínio). Questão em branco conta como erro e chute não é penalizado. A prova existe em português; quem faz em inglês sem ser falante nativo pode pedir 30 minutos extras (ESL +30) antes de agendar.

| Domínio | Peso |
| --- | --- |
| 1. Cloud Concepts | 24% |
| 2. Segurança e Compliance | 30% |
| 3. Tecnologia e Serviços | 34% |
| 4. Billing, Pricing e Suporte | 12% |

**Como ler este guia:** cada tópico traz o conteúdo cobrado e, quando faz sentido, uma linha **Cai na prova:** com os cenários mais comuns. Números (descontos, prazos, limites) são os que a AWS publica e podem mudar; confira na documentação perto da prova.

Ao fim de cada tópico, **Perguntas típicas** reúne os formatos de questão mais comuns com a resposta esperada. **Complemento** traz conceitos que costumam cair e que não estavam na primeira versão deste guia.

## Domínio 1 — Cloud Concepts (24%)

Domínio de vocabulário oficial. A experiência prática ajuda pouco aqui; o que dá ponto é conhecer as listas da AWS e reconhecer cada item num cenário.

### 1.1 O que é computação em nuvem

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

**Perguntas típicas:**

- "Qual modelo de serviço dá mais controle sobre o sistema operacional?" → IaaS (EC2).
- "Uma empresa quer só enviar o código sem gerenciar infraestrutura. Qual modelo?" → PaaS (Elastic Beanstalk).
- "Qual é um exemplo de SaaS?" → Amazon Connect, WorkSpaces ou um software pronto como e-mail.
- "Qual modelo de implantação liga o datacenter próprio à AWS?" → Híbrido.
- "O que caracteriza computação em nuvem?" → Recursos sob demanda, pela internet, pagando pelo uso.

### 1.2 As 6 vantagens da computação em nuvem

1. **Trocar despesa de capital por despesa variável:** sem investimento antecipado em hardware (CapEx → OpEx).
2. **Beneficiar-se de economias de escala massivas:** a AWS compra em volume e repassa preços menores.
3. **Parar de adivinhar capacidade:** escala conforme a demanda real, sem sobra nem falta.
4. **Aumentar velocidade e agilidade:** recursos em minutos, experimentação barata.
5. **Parar de gastar dinheiro mantendo datacenters:** foco no negócio, não em racks e energia.
6. **Tornar-se global em minutos:** implantar em várias regiões com poucos cliques.

- **Cai na prova:** a questão descreve um benefício e pede o nome oficial. Ex.: "não precisa mais comprar servidores para o pico de Black Friday" = parar de adivinhar capacidade.

**Perguntas típicas:**

- "Qual vantagem permite trocar investimento inicial em servidores por pagamento conforme o uso?" → Trocar despesa de capital por despesa variável.
- "Uma empresa não sabe quanto tráfego terá no lançamento. Qual vantagem ajuda?" → Parar de adivinhar capacidade.
- "Como a AWS consegue preços menores que um datacenter próprio?" → Economias de escala massivas.
- "Uma startup quer abrir operação em outro continente em um dia." → Tornar-se global em minutos.
- "Qual vantagem libera o time para focar no produto em vez de racks e energia?" → Parar de gastar mantendo datacenters.

### 1.3 Conceitos de arquitetura que a prova cobra

- **Escalabilidade:** capacidade de crescer para atender à demanda. *Vertical* (scale up: instância maior) vs *horizontal* (scale out: mais instâncias).
- **Elasticidade:** crescer e encolher automaticamente conforme a carga (ex.: Auto Scaling). A diferença para escalabilidade é o "encolher sozinho".
- **Alta disponibilidade:** o sistema continua acessível com falhas, normalmente com várias AZs.
- **Tolerância a falhas:** continuar funcionando sem interrupção perceptível mesmo quando um componente falha (redundância).
- **Agilidade:** reduzir o tempo e o custo de experimentar.
- **Recuperação de desastres (DR):** do mais barato e lento para o mais caro e rápido: Backup and Restore → Pilot Light → Warm Standby → Multi-site active/active.
- **Acoplamento fraco (loose coupling):** componentes se comunicam por filas e eventos (SQS, SNS, EventBridge), e a falha de um não derruba o outro.

**Complemento:**

- **RTO (Recovery Time Objective):** tempo máximo aceitável para restaurar o serviço após um desastre.
- **RPO (Recovery Point Objective):** quantidade máxima de dados que se aceita perder, medida em tempo (ex.: "no máximo 15 minutos de dados").
- Quanto menores RTO e RPO, mais cara a estratégia de DR (Multi-site é a de menor RTO/RPO; Backup and Restore, a de maior).
- **Monolito vs microsserviços:** o monolito tem tudo numa única aplicação; microsserviços são serviços pequenos e independentes, que escalam e são implantados separadamente e se comunicam por APIs, filas e eventos.
- **Projetar para falhas (design for failure):** assumir que componentes vão falhar e construir redundância e recuperação automática.
- **Serverless:** não gerenciar servidores, escala automática, pagar só pelo uso e alta disponibilidade embutida (Lambda, Fargate, DynamoDB, S3, SQS, SNS).
- **Stateless:** a aplicação não guarda estado no servidor (sessão vai para ElastiCache ou DynamoDB), o que facilita escalar horizontalmente.

**Perguntas típicas:**

- "A aplicação adiciona instâncias no pico e remove de madrugada, sozinha." → Elasticidade.
- "Como garantir que a falha de um datacenter não derrube a aplicação?" → Implantar em várias AZs (alta disponibilidade).
- "Qual estratégia de DR tem menor custo?" → Backup and Restore. "E menor tempo de recuperação?" → Multi-site active/active.
- "Como evitar que a falha de um componente afete os outros?" → Acoplamento fraco com SQS, SNS ou EventBridge.
- "O que significa RPO de 1 hora?" → Aceita-se perder no máximo 1 hora de dados.
- "Aumentar o tamanho da instância é escala..." → Vertical. "Adicionar instâncias é..." → Horizontal.

### 1.4 AWS Well-Architected Framework

Seis pilares, cada um com princípios de design. A prova descreve uma prática e pergunta o pilar.

| Pilar | Foco | Princípios de design que mais caem |
| --- | --- | --- |
| Excelência Operacional | Rodar e monitorar sistemas e melhorar processos | Operações como código; mudanças pequenas, frequentes e reversíveis; refinar procedimentos com frequência; antecipar falhas; aprender com falhas operacionais; usar serviços gerenciados; implementar observabilidade |
| Segurança | Proteger dados, sistemas e ativos | Base forte de identidade (menor privilégio); rastreabilidade; segurança em todas as camadas; automatizar boas práticas; proteger dados em trânsito e em repouso; manter pessoas longe dos dados; preparar-se para incidentes |
| Confiabilidade | Executar corretamente e se recuperar de falhas | Recuperação automática de falhas; testar procedimentos de recuperação; escalar horizontalmente; parar de adivinhar capacidade; gerenciar mudanças com automação |
| Eficiência de Performance | Usar recursos de forma eficiente conforme a demanda muda | Democratizar tecnologias avançadas; ficar global em minutos; usar arquiteturas serverless; experimentar com mais frequência; considerar a afinidade mecânica (escolher a tecnologia que combina com o uso) |
| Otimização de Custos | Entregar valor pelo menor preço | Praticar gestão financeira na nuvem; adotar modelo de consumo; medir a eficiência geral; parar de gastar com trabalho pesado indiferenciado; analisar e atribuir gastos |
| Sustentabilidade | Reduzir impacto ambiental | Entender seu impacto; definir metas; maximizar a utilização; adotar hardware e software mais eficientes; usar serviços gerenciados; reduzir o impacto downstream |

- **AWS Well-Architected Tool:** serviço gratuito no console para revisar uma carga de trabalho contra os pilares e gerar um plano de melhorias.
- **Lenses:** extensões do framework para cenários específicos (serverless, SaaS, machine learning, serviços financeiros).
- **Cai na prova:** "usar várias AZs" = Confiabilidade; "ativar MFA e criptografia" = Segurança; "escolher o tipo de instância certo" = Eficiência de Performance; "desligar recursos ociosos" = Otimização de Custos; "usar Graviton para gastar menos energia" = Sustentabilidade; "CloudFormation e runbooks" = Excelência Operacional.

**Complemento — princípios gerais de design do Well-Architected:**

- Parar de adivinhar necessidades de capacidade.
- Testar sistemas em escala de produção.
- Automatizar para facilitar a experimentação.
- Permitir arquiteturas evolutivas.
- Guiar arquiteturas com dados.
- Melhorar com "game days" (simulações de eventos em produção).

**Perguntas típicas:**

- "Quantos e quais são os pilares?" → Seis: Excelência Operacional, Segurança, Confiabilidade, Eficiência de Performance, Otimização de Custos e Sustentabilidade.
- "Qual pilar inclui recuperar automaticamente de falhas e escalar horizontalmente?" → Confiabilidade.
- "Qual pilar inclui rastreabilidade e menor privilégio?" → Segurança.
- "Qual pilar inclui fazer mudanças pequenas, frequentes e reversíveis?" → Excelência Operacional.
- "Qual pilar inclui usar serverless e experimentar com frequência?" → Eficiência de Performance.
- "Qual pilar inclui adotar o modelo de consumo e analisar gastos?" → Otimização de Custos.
- "Qual pilar foi o último adicionado e trata de impacto ambiental?" → Sustentabilidade.
- "Qual ferramenta revisa uma carga de trabalho contra os pilares?" → AWS Well-Architected Tool.

### 1.5 AWS Cloud Adoption Framework (CAF)

Guia para organizar a transformação digital de uma empresa na AWS.

- **Benefícios declarados:** reduzir risco de negócio, melhorar desempenho ESG (ambiental, social e governança), aumentar receita e aumentar eficiência operacional.
- **6 perspectivas:**

| Perspectiva | Público principal | Exemplos de capacidades |
| --- | --- | --- |
| Business | CEO, CFO, diretores de negócio | Estratégia, gestão de portfólio, inovação, dados como produto |
| People | RH, liderança, gestores de pessoas | Cultura, treinamento, gestão da mudança, desenho organizacional |
| Governance | CFO, gestores de risco e projetos | Gestão de programas, benefícios, riscos, finanças na nuvem (FinOps) |
| Platform | CTO, arquitetos | Arquitetura, engenharia de plataforma, dados, CI/CD |
| Security | CISO, times de segurança | Identidade, detecção, proteção de infraestrutura e dados, resposta a incidentes |
| Operations | Times de operação e SRE | Observabilidade, gestão de incidentes e problemas, gestão de mudanças |

- **Domínios de transformação:** Tecnologia, Processos, Organização e Produto.
- **4 fases (ciclo iterativo):** Envision (enxergar oportunidades), Align (identificar lacunas e alinhar stakeholders), Launch (entregar pilotos em produção), Scale (expandir pilotos para a organização).
- **Cai na prova:** Business, People e Governance são perspectivas de negócio; Platform, Security e Operations são técnicas. "Treinar funcionários" = People; "gerenciar orçamento e risco do programa" = Governance.

**Perguntas típicas:**

- "Qual perspectiva do CAF trata de treinamento, cultura e mudança organizacional?" → People.
- "Qual perspectiva garante que a estratégia de nuvem gere valor de negócio?" → Business.
- "Qual perspectiva cuida de risco, orçamento e gestão do programa?" → Governance.
- "Qual perspectiva trata da arquitetura e da plataforma técnica?" → Platform.
- "Qual perspectiva trata de identidade, proteção de dados e resposta a incidentes?" → Security.
- "Qual perspectiva trata de monitoramento e gestão de incidentes operacionais?" → Operations.
- "Quais são as fases da jornada de transformação?" → Envision, Align, Launch e Scale.
- "Qual é um benefício do CAF?" → Reduzir risco de negócio, melhorar ESG, aumentar receita ou eficiência operacional.

### 1.6 Estratégias de migração (os 7 Rs)

| Estratégia | O que é | Exemplo |
| --- | --- | --- |
| Retire | Desligar o que não é mais usado | Aplicação legada sem usuários |
| Retain | Manter on-premises por enquanto | Sistema que ainda não pode migrar por regulação ou dependências |
| Rehost | Lift-and-shift, sem mudanças | Mover VMs para EC2 com Application Migration Service |
| Relocate | Mover em bloco no nível do hipervisor | VMware Cloud on AWS |
| Replatform | Lift-tinker-and-shift: pequenas otimizações | Banco em servidor próprio para Amazon RDS |
| Repurchase | Trocar por outro produto, normalmente SaaS | CRM próprio para Salesforce |
| Refactor / Re-architect | Reescrever para cloud-native | Monolito para microsserviços com Lambda e ECS |

- **Cai na prova:** Rehost (sem mudar nada) vs Replatform (pequena mudança para serviço gerenciado). Refactor é o que tem mais custo e mais benefício de longo prazo.

**Perguntas típicas:**

- "Migrar servidores para EC2 sem mudar nada." → Rehost.
- "Migrar o banco para RDS para reduzir administração, sem mudar a aplicação." → Replatform.
- "Trocar o sistema próprio por um produto SaaS." → Repurchase.
- "Reescrever a aplicação para usar Lambda e microsserviços." → Refactor.
- "Desligar aplicações que ninguém usa." → Retire.
- "Manter a aplicação no datacenter por exigência regulatória." → Retain.
- "Qual estratégia é a mais rápida?" → Rehost. "Qual traz mais benefícios de nuvem a longo prazo?" → Refactor.

### 1.7 Economia da nuvem

- **Custos on-premises:** fixos e antecipados (servidores, storage, rede, datacenter, energia, refrigeração, pessoal). Muitos são "invisíveis" num TCO mal feito.
- **Custos na nuvem:** variáveis, por uso, sem compromisso (exceto quando você escolhe reservar).
- **TCO (Total Cost of Ownership):** comparação do custo total on-premises vs nuvem, incluindo pessoal e operação. Ferramentas: Migration Evaluator e Pricing Calculator.
- **Licenciamento:** BYOL (trazer licenças próprias, ex.: Windows Server ou Oracle em Dedicated Hosts) vs licença incluída na instância. AWS License Manager controla o uso das licenças.
- **Rightsizing:** ajustar tipo e tamanho dos recursos ao uso real. Ferramentas: Compute Optimizer, Cost Explorer, Trusted Advisor.
- **Serviços gerenciados reduzem custo operacional:** a AWS cuida de patch, backup e hardware; o time foca no produto.
- **Automação reduz custo e erro:** infraestrutura como código (CloudFormation) e escalonamento automático — o Terraform é um equivalente de terceiros.
- **Cai na prova:** "pagar só pelo que usa" e "sem contratos de longo prazo" = modelo On-Demand; "reduzir custo de licença" = BYOL e Dedicated Hosts.

**Perguntas típicas:**

- "Qual custo deixa de existir ao migrar para a AWS?" → Custos de datacenter (energia, refrigeração, espaço físico, compra de hardware).
- "Qual custo continua sendo do cliente na nuvem?" → Gestão das aplicações e dos dados, licenças não incluídas, uso dos recursos.
- "Como reduzir custo de licenças ao migrar?" → BYOL com Dedicated Hosts, ou usar instâncias com licença incluída.
- "Qual ferramenta ajuda a montar o caso de negócio (TCO) da migração?" → Migration Evaluator.
- "Qual prática ajusta recursos ao uso real?" → Rightsizing.
- "Por que serviços gerenciados reduzem o TCO?" → Diminuem o trabalho operacional (patches, backups, hardware).

## Domínio 2 — Segurança e Compliance (30%), parte 1

O domínio mais pesado. Esta parte cobre quem é responsável pelo quê e como funciona o controle de acesso.

### 2.1 Modelo de responsabilidade compartilhada

- **AWS — segurança DA nuvem:** hardware, datacenters físicos (acesso, energia, refrigeração), rede global, regiões, AZs, edge locations e a camada de virtualização (hipervisor).
- **Cliente — segurança NA nuvem:** dados, criptografia, identidades e permissões (IAM), configuração de rede (security groups, NACLs, rotas), sistema operacional e aplicações quando ele os gerencia.
- **A divisão muda conforme o tipo de serviço:**

| Serviço | AWS cuida de | Cliente cuida de |
| --- | --- | --- |
| EC2 (IaaS) | Hardware, rede física, hipervisor | Patch do SO convidado, aplicações, security groups, firewall do SO, dados, IAM |
| RDS / Aurora | Hardware, SO, patch do motor do banco, backups automáticos | Usuários do banco, regras de acesso de rede, criptografia ativada, dados |
| Lambda / Fargate | Infra, SO, runtime, escalonamento | Código, permissões (roles), configuração, dados |
| S3 | Infra, durabilidade e disponibilidade do armazenamento | Políticas de bucket, quem acessa, criptografia, versionamento |
| DynamoDB | Infra, SO, software, escalonamento | Acesso via IAM, criptografia e dados |

- **Controles herdados:** o cliente herda da AWS (ex.: controles físicos e ambientais).
- **Controles compartilhados:** cada lado faz a sua parte na sua camada — gestão de patches (AWS na infra, cliente no SO e apps), gestão de configuração e treinamento/conscientização.
- **Controles específicos do cliente:** só o cliente pode fazer (ex.: proteção e zonas de segurança dos dados dele).
- **Cai na prova:** "quem aplica patch no SO de uma EC2?" = cliente. "Quem aplica patch no motor do RDS?" = AWS. "Quem destrói discos físicos ao fim da vida útil?" = AWS. "Quem configura o security group?" = cliente. Quanto mais gerenciado o serviço, menos responsabilidade do cliente.

**Perguntas típicas:**

- "Qual é responsabilidade da AWS?" → Segurança física dos datacenters, hardware, rede global, hipervisor, patch do SO em serviços gerenciados (RDS, Lambda).
- "Qual é responsabilidade do cliente?" → Dados, IAM, security groups, criptografia, patch do SO no EC2, configuração dos serviços.
- "Qual é um controle compartilhado?" → Gestão de patches, gestão de configuração ou treinamento.
- "Qual é um controle herdado da AWS?" → Controles físicos e ambientais.
- "Ao trocar EC2 por Lambda, o que muda?" → A responsabilidade do cliente diminui (SO e runtime passam para a AWS).
- "Quem é responsável pela segurança dos dados no S3?" → O cliente (políticas, acesso e criptografia).

### 2.2 Usuário root

- Criado junto com a conta, com o e-mail de cadastro; tem acesso irrestrito e não pode ser limitado por políticas IAM.
- **Boas práticas:** ativar MFA, não criar access keys (apagar se existirem), usar só para tarefas que exigem root, criar usuários/identidades administrativas para o dia a dia, senha forte e e-mail protegido.
- **Tarefas que só o root pode fazer:**
  - Alterar configurações da conta (nome da conta, e-mail, senha do root e access keys do root).
  - Fechar a conta AWS.
  - Mudar ou cancelar o plano de AWS Support.
  - Restaurar permissões de um administrador IAM que se trancou fora.
  - Ativar o acesso de usuários IAM ao console de Billing.
  - Registrar-se como vendedor no Reserved Instance Marketplace.
  - Configurar MFA Delete em um bucket S3.
  - Editar ou apagar uma política de bucket S3 que bloqueou todo mundo.
- **Cai na prova:** "qual tarefa exige o usuário root?" com uma lista de opções. Criar usuários IAM e ver a fatura **não** exigem root.

**Perguntas típicas:**

- "Qual é a boa prática para o usuário root?" → Ativar MFA, não criar access keys e usá-lo só para tarefas que o exigem.
- "Qual destas tarefas exige o root?" → Fechar a conta, mudar o plano de suporte, alterar dados da conta ou restaurar permissões de administrador.
- "Qual tarefa NÃO exige o root?" → Criar usuários IAM, ver a fatura (com permissão) ou lançar instâncias.
- "O que fazer logo após criar a conta?" → Proteger o root com MFA e criar identidades administrativas para o dia a dia.

### 2.3 AWS IAM (Identity and Access Management)

- **Serviço global e gratuito** para controlar quem (autenticação) pode fazer o quê (autorização) na conta.
- **Usuário IAM:** identidade com credenciais de longo prazo (senha para console, access keys para CLI/SDK). Representa uma pessoa ou aplicação.
- **Grupo IAM:** coleção de usuários que recebem as mesmas permissões. Grupos não contêm outros grupos e não são identidades (não fazem login).
- **Role IAM:** identidade com credenciais **temporárias**, assumida por quem precisa: serviços AWS (ex.: EC2 ou Lambda acessando S3), usuários de outra conta (cross-account) ou usuários federados. Não tem senha nem access key fixa.
- **Policies:** documentos JSON com Effect (Allow/Deny), Action, Resource e Condition.
  - **Identity-based:** anexadas a usuários, grupos ou roles.
  - **Resource-based:** anexadas ao recurso (ex.: bucket policy no S3) e indicam quem pode acessá-lo.
  - **AWS managed** (prontas, mantidas pela AWS), **customer managed** (criadas por você, reutilizáveis) e **inline** (embutidas em uma só identidade).
  - **Regra de avaliação:** tudo começa negado (implicit deny); um Allow libera; um Deny explícito sempre vence.
- **Princípio do menor privilégio:** conceder só as permissões necessárias para a tarefa. Aparece em muitas respostas corretas.
- **Credenciais e boas práticas:**
  - **MFA:** apps de autenticação (virtual), chaves físicas FIDO/passkeys e tokens de hardware TOTP.
  - **Password policy:** tamanho mínimo, complexidade, expiração e reuso de senhas dos usuários IAM.
  - **Access keys:** para CLI, SDK e API. Nunca colocar no código; rotacionar; preferir roles.
  - **Roles para EC2 (instance profile):** forma correta de dar permissão a uma aplicação em EC2, em vez de guardar access keys na instância.
- **Ferramentas de auditoria do IAM:**
  - **Credential report:** relatório da conta com todos os usuários e o status das credenciais (senha, MFA, idade das access keys).
  - **Access Advisor (last accessed):** mostra quais serviços um usuário ou role realmente usou, para remover permissões sobrando.
  - **IAM Access Analyzer:** identifica recursos compartilhados com entidades externas e ajuda a gerar políticas de menor privilégio.
- **Federação:** usar identidades externas (Active Directory, Google, Okta) via SAML 2.0 ou OIDC, sem criar usuários IAM.
- **AWS IAM Identity Center** (antigo AWS SSO): login único centralizado para várias contas do Organizations e aplicações SaaS, com conjuntos de permissões (permission sets). É a forma recomendada de dar acesso humano a ambientes multi-conta.
- **Amazon Cognito:** autenticação de **usuários finais** de aplicações web e mobile (cadastro, login, login social). Não é para funcionários acessarem a AWS.
- **AWS Directory Service:** Microsoft Active Directory gerenciado na AWS, ou conector para o AD on-premises.
- **Secrets Manager****:** Guarda segredos (senhas de banco, chaves de API) criptografados com KMS. **Cai na prova:** é o serviço com **rotação automática** de segredos, com integração nativa com RDS. É pago por segredo.
- **Systems Manager Parameter Store:** guarda parâmetros e segredos simples; tem camada gratuita; não faz rotação automática nativa.
- **Formas de acessar a AWS:** Console (usuário/senha + MFA), CLI e SDKs (access keys ou credenciais temporárias), CloudShell (terminal no navegador, já autenticado).

**Complemento — boas práticas do IAM:**

- Atribuir permissões a **grupos**, não diretamente a usuários.
- Preferir **credenciais temporárias** (roles, Identity Center) a usuários com access keys de longo prazo.
- Exigir MFA, aplicar política de senhas, rotacionar credenciais e remover usuários e permissões sem uso.
- Usar **condições** nas políticas (ex.: exigir MFA, limitar por IP).
- IAM é **global** (não regional) e **gratuito**.

**Perguntas típicas:**

- "Uma aplicação no EC2 precisa ler um bucket S3. Qual a forma mais segura?" → Anexar uma IAM role à instância.
- "Dez desenvolvedores precisam das mesmas permissões." → Criar um grupo IAM e anexar a política ao grupo.
- "Uma política tem Allow e outra tem Deny explícito para a mesma ação. O que vale?" → Deny explícito.
- "Qual princípio diz para dar só as permissões necessárias?" → Menor privilégio.
- "Qual relatório lista os usuários e o status de MFA e access keys?" → IAM credential report.
- "Como dar login único a funcionários em várias contas?" → IAM Identity Center.
- "Como permitir login com Google em um app mobile?" → Amazon Cognito.
- "Onde guardar a senha do banco com rotação automática?" → Secrets Manager.
- "Funcionários usam o Active Directory da empresa e precisam acessar a AWS." → Federação (via Identity Center ou SAML) ou AWS Directory Service.
- "Como acessar a AWS por linha de comando?" → AWS CLI com access keys (ou credenciais temporárias).

### 2.4 Governança multi-conta

- **AWS Organizations:** gerencia várias contas de forma centralizada.
  - **Conta de gerenciamento (management account)** e **contas-membro**, organizadas em **OUs** (unidades organizacionais) hierárquicas.
  - **SCPs (Service Control Policies):** definem o limite máximo de permissões das contas ou OUs. **Cai na prova:** SCP não concede permissão, só restringe; e não afeta a conta de gerenciamento.
  - **Consolidated billing:** uma fatura única; soma o uso de todas as contas para descontos por volume; compartilha Reserved Instances e Savings Plans entre as contas.
  - Criar contas por API e isolar ambientes (produção, desenvolvimento, segurança).
- **AWS Control Tower:** configura automaticamente um ambiente multi-conta seguro e padronizado (landing zone) sobre o Organizations.
  - **Controles (guardrails):** preventivos (bloqueiam ações, via SCP) e detectivos (detectam desvios, via Config).
  - **Account Factory:** cria contas novas já seguindo o padrão.
  - Painel com o status de conformidade de todas as contas.
- **AWS Resource Access Manager (RAM):** compartilha recursos entre contas (ex.: subnets, Transit Gateways, licenças).
- **AWS Service Catalog:** catálogo de produtos aprovados (templates CloudFormation) que os times podem provisionar sozinhos, dentro das regras da empresa.
- **Cai na prova:** "centralizar contas e aplicar políticas" = Organizations; "montar rapidamente um ambiente multi-conta com boas práticas" = Control Tower; "limitar o que uma conta inteira pode fazer" = SCP.

**Complemento:**

- SCPs são herdadas pela hierarquia: uma SCP numa OU vale para todas as contas abaixo dela.
- A permissão efetiva é a interseção entre o que a SCP permite e o que a política IAM concede.
- Estratégia multi-conta recomendada: contas separadas por ambiente e por função (produção, desenvolvimento, segurança, logs), para isolar riscos e custos.

**Perguntas típicas:**

- "Como impedir que todas as contas de desenvolvimento usem uma região?" → SCP no Organizations.
- "Uma SCP permite S3, mas o usuário não tem política IAM para S3. Ele consegue acessar?" → Não; a SCP só limita, não concede.
- "Como obter desconto por volume somando o uso de várias contas?" → Consolidated billing no Organizations.
- "Como criar rapidamente um ambiente multi-conta seguro com guardrails?" → AWS Control Tower.
- "Como deixar times criarem só recursos aprovados pela empresa?" → AWS Service Catalog.
- "Como compartilhar uma subnet com outra conta?" → AWS RAM.

## Domínio 2 — Segurança e Compliance (30%), parte 2

Esta parte cobre como proteger dados, provar conformidade e detectar ameaças.

### 2.5 Criptografia

- **Em repouso (at rest):** dados armazenados (S3, EBS, RDS, DynamoDB) criptografados com chaves do KMS.
- **Em trânsito (in transit):** dados trafegando pela rede, protegidos com TLS/SSL (HTTPS).
- **AWS KMS (Key Management Service):** cria e gerencia chaves de criptografia; integrado à maioria dos serviços.
  - **AWS owned keys** (invisíveis para você), **AWS managed keys** (criadas pela AWS na sua conta para um serviço) e **customer managed keys** (criadas e controladas por você, com política de chave, rotação e auditoria).
  - Toda utilização de chave fica registrada no CloudTrail.
  - As chaves ficam em HSMs compartilhados e gerenciados pela AWS; são regionais.
- **AWS CloudHSM:** HSM **dedicado e exclusivo** (single-tenant) na nuvem. Você gerencia as chaves e a AWS não tem acesso a elas. Para exigências regulatórias fortes.
- **AWS Certificate Manager (ACM):** emite, gerencia e **renova automaticamente** certificados SSL/TLS. Certificados públicos do ACM são gratuitos e usados em ELB, CloudFront e API Gateway.
- **S3:** todo objeto novo é criptografado por padrão com SSE-S3. Opções: SSE-S3 (chave da AWS), SSE-KMS (chave do KMS, com auditoria), SSE-C (chave fornecida pelo cliente) e criptografia no lado do cliente.
- **Cai na prova:** "chave controlada pelo cliente em hardware dedicado" = CloudHSM; "criar e gerenciar chaves integradas aos serviços" = KMS; "certificado HTTPS para o load balancer" = ACM; "quem ativa a criptografia dos dados?" = cliente.

**Perguntas típicas:**

- "Qual serviço cria e controla chaves de criptografia integradas a S3, EBS e RDS?" → AWS KMS.
- "A empresa exige HSM dedicado, com chaves sob controle exclusivo dela." → AWS CloudHSM.
- "Como obter certificados SSL/TLS gratuitos com renovação automática?" → AWS Certificate Manager.
- "Como proteger dados em trânsito?" → TLS/HTTPS. "E em repouso?" → Criptografia com KMS.
- "Quem é responsável por ativar a criptografia dos dados?" → O cliente.
- "Como auditar quem usou uma chave do KMS?" → CloudTrail.

### 2.6 Compliance e governança

- **AWS Artifact:** portal de autoatendimento para baixar **relatórios de compliance da AWS** (SOC 1/2/3, PCI DSS, ISO 27001 etc.) e aceitar **acordos** (ex.: BAA para HIPAA). Gratuito.
- **AWS Audit Manager:** coleta evidências **da sua conta** continuamente e mapeia para frameworks (PCI DSS, GDPR, HIPAA), para preparar as suas auditorias.
- **Programas de compliance:** a AWS mantém certificações e atestados, mas compliance da carga de trabalho é responsabilidade compartilhada. Nem todo serviço é elegível para todo programa e a disponibilidade varia por região.
- **Residência de dados:** os dados ficam na região escolhida; a AWS não os move sem ação do cliente.
- **AWS GovCloud (US):** regiões isoladas para cargas reguladas do governo americano.
- **AWS Config** com **conformance packs:** conjuntos de regras para avaliar conformidade (ver 2.7).
- **Cai na prova:** "auditor pede o relatório SOC 2 da AWS" = Artifact; "automatizar a coleta de evidências para auditoria da empresa" = Audit Manager.

**Perguntas típicas:**

- "Onde baixar o relatório SOC 2 ou o atestado PCI da AWS?" → AWS Artifact.
- "Onde aceitar um acordo como o BAA (HIPAA)?" → AWS Artifact (Agreements).
- "Como coletar evidências continuamente para a auditoria da empresa?" → AWS Audit Manager.
- "Os dados podem sair da região sem ação do cliente?" → Não; o cliente escolhe a região e controla onde os dados ficam.
- "Usar um serviço certificado garante que a aplicação está em conformidade?" → Não; o cliente também precisa configurar e operar de forma conforme (responsabilidade compartilhada).

### 2.7 Logs, monitoramento e auditoria

- **AWS CloudTrail:** registra as **chamadas de API** na conta: quem fez, o quê, quando, de onde (IP) e em qual recurso.
  - **Event history:** ativado por padrão, guarda **90 dias** de eventos de gerenciamento, grátis.
  - **Trails:** para guardar por mais tempo, envia os logs para um bucket S3 (e opcionalmente CloudWatch Logs). Pode ser multi-região e para toda a organização.
  - **Management events** (criar, alterar, apagar recursos) vs **data events** (ex.: leitura de objetos no S3, invocação de Lambda), que não são registrados por padrão.
  - **CloudTrail Insights:** detecta atividade anormal de API. **CloudTrail Lake:** consultas SQL sobre os eventos.
- **AWS Config:** registra a **configuração** dos recursos e o histórico de mudanças ao longo do tempo.
  - **Config rules** (gerenciadas ou customizadas): avaliam se os recursos estão conformes (ex.: "todo bucket S3 deve ser criptografado").
  - Pode disparar **remediação automática** (via Systems Manager Automation).
  - É regional e pago por item registrado e por avaliação.
- **Amazon CloudWatch**: monitoramento de métricas, logs e alarmes. Pontos de prova:
  - Métricas padrão do EC2 a cada 5 minutos (monitoramento detalhado: 1 minuto, pago).
  - **Memória e disco do EC2 não vêm por padrão:** exigem o CloudWatch agent instalado (métricas customizadas).
  - **Alarmes:** disparam ações quando uma métrica passa do limite (notificar via SNS, acionar Auto Scaling, parar/reiniciar EC2). **Billing alarm:** alerta de custo baseado na métrica de cobrança.
  - **CloudWatch Logs**, **Logs Insights** (consultas) e **dashboards**.
- **VPC Flow Logs:** registram o tráfego IP que entra e sai das interfaces de rede da VPC; usados em análise de segurança e pelo GuardDuty.
- **AWS Health Dashboard:** status dos serviços AWS e eventos que afetam a **sua** conta (manutenções programadas, problemas). Ver também 3.16.
- **Cai na prova:** "quem apagou a instância?" = CloudTrail; "como estava configurado o security group semana passada?" = Config; "alerta quando a CPU passa de 80%" = CloudWatch alarm; "verificar continuamente se recursos seguem as regras" = Config rules.

**Perguntas típicas:**

- "Qual serviço registra quem encerrou uma instância e quando?" → CloudTrail.
- "Por quanto tempo o CloudTrail guarda eventos sem configurar nada?" → 90 dias (event history).
- "Como guardar logs do CloudTrail por anos?" → Criar um trail que envia para o S3.
- "Qual serviço mostra o histórico de configuração de um recurso e se ele segue as regras?" → AWS Config.
- "Como receber alerta quando a CPU passar de 80%?" → Alarme do CloudWatch (com notificação pelo SNS).
- "Como coletar a memória usada pelo EC2?" → Instalar o CloudWatch agent.
- "Como capturar o tráfego de rede da VPC?" → VPC Flow Logs.
- "Onde ver logs de aplicação?" → CloudWatch Logs.

### 2.8 Proteção de rede e aplicações

- **Security group****:** Firewall virtual no nível da **instância/ENI**. **Stateful** (a resposta volta automaticamente); só tem regras de **permissão**; por padrão bloqueia toda entrada e libera toda saída.
- **Network ACL (NACL):** firewall no nível da **subnet**. **Stateless** (precisa liberar entrada e saída); tem regras de **permitir e negar**, avaliadas em ordem numérica. A NACL padrão libera tudo.
- **AWS Shield:** proteção contra **DDoS**.
  - **Shield Standard:** gratuito e automático para todos os clientes, protege contra ataques comuns de camada 3 e 4.
  - **Shield Advanced:** pago, com proteção ampliada (inclusive camada 7 junto com o WAF), acesso 24/7 ao **Shield Response Team (SRT)**, visibilidade dos ataques e **proteção de custo** (créditos pelo aumento de uso causado por ataque).
- **AWS WAF:** firewall de **aplicação web (camada 7)**. Usa web ACLs com regras para bloquear SQL injection, XSS, IPs, países (geo) e limitar requisições (rate-based). Tem regras gerenciadas prontas. Associado a **CloudFront, ALB, API Gateway, AppSync e Cognito**.
- **AWS Firewall Manager:** gerencia de forma central regras de WAF, Shield Advanced, security groups e firewalls de rede em **todas as contas** do Organizations.
- **Cai na prova:** "bloquear um IP específico na subnet" = NACL (security group não nega); "ataque de SQL injection" = WAF; "ataque DDoS volumétrico" = Shield; "time especialista 24/7 durante ataque DDoS" = Shield Advanced.

**Perguntas típicas:**

- "Qual firewall atua no nível da instância e é stateful?" → Security group.
- "Qual firewall atua no nível da subnet e é stateless?" → Network ACL.
- "Como bloquear um endereço IP malicioso?" → Regra de negação na NACL (ou regra no WAF para tráfego web).
- "Qual proteção DDoS todo cliente tem sem custo?" → Shield Standard.
- "Qual serviço dá acesso a especialistas 24/7 e proteção de custo durante ataques DDoS?" → Shield Advanced.
- "Como bloquear SQL injection e XSS?" → AWS WAF.
- "Como bloquear acesso de certos países ao site?" → WAF (regra geográfica) ou restrição geográfica do CloudFront.
- "Em quais serviços o WAF pode ser usado?" → CloudFront, ALB, API Gateway, AppSync e Cognito.
- "Como aplicar as mesmas regras de WAF em todas as contas?" → AWS Firewall Manager.

### 2.9 Detecção de ameaças e postura de segurança

| Serviço | O que faz | Detalhes de prova |
| --- | --- | --- |
| Amazon GuardDuty | Detecção inteligente de ameaças com machine learning | Analisa CloudTrail, VPC Flow Logs e logs de DNS (e outras fontes opcionais); sem agentes; ativação com um clique; período de teste gratuito |
| Amazon Inspector | Avaliação automática e contínua de **vulnerabilidades** | Varre instâncias EC2, imagens no ECR e funções Lambda; procura CVEs e exposição de rede; gera nota de risco |
| Amazon Macie | Descobre e protege **dados sensíveis** com ML | Só no **S3**; identifica PII (CPF, cartão, nomes) e buckets públicos ou sem criptografia |
| Amazon Detective | **Investiga** a causa raiz de achados de segurança | Monta gráficos de relacionamento a partir de logs e achados do GuardDuty |
| AWS Security Hub | **Painel central** de segurança | Agrega achados de GuardDuty, Inspector, Macie e parceiros; verifica padrões como AWS Foundational Security Best Practices e CIS |
| AWS Trusted Advisor | Recomendações de **boas práticas** | Categorias: otimização de custos, performance, segurança, tolerância a falhas, cotas de serviço e excelência operacional |

- **Trusted Advisor por plano de suporte:** Basic e Developer só têm as verificações principais de segurança e de cotas; **Business, Enterprise On-Ramp e Enterprise têm todas as verificações** e acesso via API.
- **Exemplos de verificações do Trusted Advisor:** buckets S3 com acesso público, MFA no root, security groups com portas abertas para o mundo, instâncias ociosas, cotas próximas do limite.
- **Cai na prova:** detectar (GuardDuty) → investigar (Detective) → centralizar (Security Hub). Vulnerabilidade de software = Inspector; dado sensível = Macie.

**Perguntas típicas:**

- "Qual serviço detecta atividade maliciosa analisando CloudTrail, VPC Flow Logs e DNS?" → GuardDuty.
- "Qual serviço varre instâncias EC2 e imagens de container em busca de vulnerabilidades?" → Amazon Inspector.
- "Qual serviço encontra dados pessoais em buckets S3?" → Amazon Macie.
- "Qual serviço ajuda a investigar a causa raiz de um achado de segurança?" → Amazon Detective.
- "Qual serviço reúne os achados de segurança de vários serviços num só painel?" → AWS Security Hub.
- "Qual serviço recomenda melhorias de custo, segurança, performance e limites?" → Trusted Advisor.
- "Qual plano de suporte libera todas as verificações do Trusted Advisor?" → Business ou superior.
- "Qual verificação de segurança o Trusted Advisor faz?" → Buckets S3 públicos, MFA no root, portas abertas em security groups.

### 2.10 Outros pontos de segurança

- **Testes de intrusão (pentest):** permitidos sem aprovação prévia para uma lista de serviços (ex.: EC2, RDS, Lambda); ataques DDoS simulados e alguns testes são proibidos ou exigem aprovação.
- **AWS Trust & Safety:** time para reportar abuso de recursos AWS (spam, phishing, ataques vindos de IPs da AWS).
- **Onde buscar informação de segurança:** AWS Security Center, AWS Security Blog, Security Bulletins, Knowledge Center, AWS re:Post e documentação. Ferramentas de segurança de terceiros: AWS Marketplace.
- **Cai na prova:** "recebi phishing vindo de um IP da AWS" = AWS Trust & Safety.

**Perguntas típicas:**

- "É preciso pedir autorização para fazer pentest no EC2?" → Não, para os serviços da lista permitida; simulação de DDoS e alguns testes são proibidos.
- "Uma instância da AWS está enviando spam para a sua empresa. Quem contatar?" → AWS Trust & Safety.
- "Onde encontrar boletins e boas práticas de segurança?" → AWS Security Center, Security Blog e Knowledge Center.
- "Onde comprar ferramentas de segurança de terceiros?" → AWS Marketplace.

## Domínio 3 — Tecnologia e Serviços (34%), parte 1

O domínio maior. A prova cobra amplitude: reconhecer o serviço certo para cada cenário e as características que o diferenciam dos vizinhos.

### 3.1 Formas de acessar e implantar na AWS

- **AWS Management Console:** interface web. Bom para tarefas pontuais e exploração.
- **AWS CLI:** linha de comando para automatizar via scripts.
- **SDKs:** bibliotecas para usar a AWS dentro do código (Python/boto3, Java, JavaScript etc.).
- **AWS CloudShell:** terminal no navegador, já autenticado e com a CLI instalada, sem custo adicional.
- **APIs:** tudo na AWS é uma chamada de API; Console, CLI e SDK usam as mesmas APIs por baixo.
- **Infraestrutura como código (IaC):** **AWS CloudFormation** (templates JSON/YAML que criam pilhas de recursos de forma repetível) — o Terraform é um equivalente de terceiros. Ver 3.16.
- **Operações pontuais vs repetíveis:** tarefa única pode ser no Console; tarefa repetível deve ser automatizada (CLI, SDK, CloudFormation).
- **Conectividade com a AWS:** internet pública, AWS VPN (Site-to-Site ou Client VPN) e AWS Direct Connect. Ver 3.10.
- **Cai na prova:** "provisionar o mesmo ambiente em várias regiões de forma repetível" = CloudFormation; "executar comandos rápidos sem instalar nada" = CloudShell.

**Perguntas típicas:**

- "Quais são as formas de interagir com a AWS?" → Console, CLI, SDKs e APIs (e CloudShell).
- "Um desenvolvedor quer chamar a AWS de dentro do código Python." → SDK (boto3).
- "Como criar ambientes idênticos de forma repetível e versionada?" → CloudFormation (infraestrutura como código).
- "Qual a vantagem de IaC?" → Repetibilidade, menos erro manual, versionamento e velocidade.
- "Qual opção de conectividade passa pela internet pública com criptografia?" → Site-to-Site VPN.

### 3.2 Infraestrutura global

- **Região:** área geográfica isolada e independente das outras, com várias AZs. A maioria dos serviços é **regional**; alguns são **globais** (IAM, Route 53, CloudFront, Organizations).
- **Como escolher a região (4 fatores):**
  1. **Compliance e governança de dados:** leis que exigem que os dados fiquem num país.
  2. **Proximidade dos clientes:** menor latência.
  3. **Serviços disponíveis:** nem todo serviço ou recurso existe em todas as regiões.
  4. **Preço:** varia entre regiões.
- **Availability Zone (AZ):** um ou mais datacenters distintos, com energia, rede e refrigeração redundantes, fisicamente separados de outras AZs (distância significativa), mas ligados por rede de baixa latência. Regiões novas têm no mínimo três AZs.
- **Edge locations (pontos de presença):** muito mais numerosas que as regiões, em grandes cidades. Usadas por **CloudFront** (cache), **Route 53** (DNS), **Global Accelerator**, **Shield** e **WAF**. **Regional edge caches** ficam entre as edge locations e a origem.
- **AWS Local Zones:** extensão de uma região para perto de grandes centros urbanos, para latência de um dígito de milissegundo (ex.: renderização, games, mídia).
- **AWS Wavelength:** infraestrutura AWS dentro das redes **5G** das operadoras, para aplicações móveis de ultrabaixa latência.
- **AWS Outposts:** racks e servidores da AWS instalados **no seu datacenter**, com os mesmos serviços, APIs e ferramentas. Para latência local, processamento local de dados ou residência de dados.
- **Alta disponibilidade na prática:**
  - Falha de um datacenter → distribuir em **várias AZs** (Multi-AZ).
  - Desastre regional, latência para usuários globais ou exigência de DR → **várias regiões**.
- **Cai na prova:** "menor latência para usuários do mundo todo" = CloudFront/edge locations; "serviço AWS no datacenter da empresa" = Outposts; "aplicação 5G" = Wavelength; "apagão de uma AZ não derrubar a aplicação" = Multi-AZ.

**Perguntas típicas:**

- "Quais fatores considerar ao escolher uma região?" → Compliance/residência de dados, latência para os clientes, serviços disponíveis e preço.
- "O que é uma AZ?" → Um ou mais datacenters isolados dentro de uma região, com energia e rede redundantes.
- "Para que servem as edge locations?" → Cache do CloudFront, DNS do Route 53 e entrada do Global Accelerator, perto do usuário.
- "Qual serviço é global?" → IAM, Route 53, CloudFront ou Organizations.
- "A empresa precisa rodar serviços AWS no próprio datacenter." → AWS Outposts.
- "Latência de um dígito de milissegundo para usuários de uma cidade sem região AWS." → Local Zones.
- "Aplicação móvel em rede 5G com ultrabaixa latência." → Wavelength.
- "Como sobreviver à falha de uma região inteira?" → Arquitetura multi-região.

### 3.3 Amazon EC2

- **Servidores virtuais** com controle total do SO (IaaS). Cobrança por segundo (Linux) ou por hora, conforme o modelo de compra (ver Domínio 4).
- **AMI (Amazon Machine Image):** modelo com SO e software para lançar instâncias. Pode ser da AWS, do Marketplace, da comunidade ou sua (personalizada).
- **Famílias de instância:**

| Família | Uso | Exemplos de letra |
| --- | --- | --- |
| Uso geral | Equilíbrio de CPU, memória e rede; servidores web, repositórios de código | T (burstable, acumula créditos de CPU), M |
| Otimizada para computação | Muito processamento: batch, servidores de jogos, HPC, codificação de mídia | C |
| Otimizada para memória | Grandes volumes de dados em memória: bancos em memória, análise em tempo real | R, X |
| Computação acelerada | GPU ou chips dedicados: machine learning, gráficos, cálculos científicos | P, G, Inf, Trn |
| Otimizada para armazenamento | Muita leitura e escrita em disco local: data warehouses, bancos NoSQL | I, D |

- **Graviton:** processadores ARM da AWS, com melhor relação preço/desempenho e menor consumo de energia (ligado ao pilar de Sustentabilidade).
- **User data:** script executado na primeira inicialização (instalar pacotes, configurar a aplicação).
- **Key pair:** par de chaves para acesso SSH. Alternativa sem abrir porta 22: Systems Manager Session Manager.
- **Armazenamento:** volume EBS (persistente, pode ser destacado) ou **instance store** (disco físico local, rápido, **temporário**: perde os dados ao parar ou encerrar a instância).
- **Elastic IP:** IPv4 público fixo que pode ser movido entre instâncias. Todo IPv4 público é cobrado.
- **Estados:** parar (stop) mantém o volume EBS e para a cobrança de computação; encerrar (terminate) apaga a instância. **Hibernar** salva a memória RAM no EBS.
- **Cai na prova:** "instância para treinar modelo de ML" = computação acelerada; "banco em memória" = otimizada para memória; "dados temporários de cache que podem ser perdidos" = instance store.

**Perguntas típicas:**

- "Qual família de instância para aplicação com uso intenso de CPU?" → Otimizada para computação (C).
- "Para banco de dados em memória?" → Otimizada para memória (R, X).
- "Para machine learning com GPU?" → Computação acelerada (P, G).
- "Para servidor web com carga equilibrada?" → Uso geral (T, M).
- "Como instalar pacotes automaticamente ao lançar a instância?" → User data.
- "O que acontece com o instance store ao parar a instância?" → Os dados são perdidos.
- "Como manter um IP público fixo ao trocar de instância?" → Elastic IP.
- "Qual processador oferece melhor preço/desempenho e eficiência energética?" → AWS Graviton.
- "O que é uma AMI?" → Modelo com SO e software usado para lançar instâncias.

### 3.4 Escalabilidade e balanceamento de carga

- **Amazon EC2 Auto Scaling**
  - **Auto Scaling Group (ASG):** grupo de instâncias com capacidade **mínima, desejada e máxima**, criadas a partir de um **launch template**.
  - **Políticas de escalonamento:** *target tracking* (manter uma métrica num alvo, ex.: CPU em 50%), *step/simple* (degraus conforme alarmes), *scheduled* (horários conhecidos) e *predictive* (prevê a demanda com ML).
  - **Health checks:** substitui automaticamente instâncias com falha.
  - Distribui instâncias entre AZs para alta disponibilidade.
  - O Auto Scaling em si não tem custo; você paga as instâncias.
- **AWS Auto Scaling:** serviço que configura escalonamento para vários recursos de uma vez (EC2, ECS, DynamoDB, Aurora).
- **Elastic Load Balancing (ELB)****:** Distribui o tráfego entre destinos saudáveis em várias AZs.

| Tipo | Camada | Uso |
| --- | --- | --- |
| Application Load Balancer (ALB) | 7 (HTTP/HTTPS) | Roteamento por caminho, host ou cabeçalho; microsserviços e containers; integra com WAF |
| Network Load Balancer (NLB) | 4 (TCP/UDP/TLS) | Altíssima performance, milhões de requisições por segundo, IP estático por AZ |
| Gateway Load Balancer (GWLB) | 3 (rede) | Encaminha tráfego para appliances virtuais de terceiros (firewalls, IDS/IPS) |
| Classic Load Balancer | 4 e 7 | Geração antiga, não recomendado |

- **Funções do ELB:** health checks, terminação SSL/TLS (com certificado do ACM), distribuição entre AZs.
- **Cai na prova:** "rotear /api para um serviço e /imagens para outro" = ALB; "tráfego TCP com latência ultrabaixa" = NLB; "inspecionar tráfego com firewall de terceiros" = GWLB; "aumentar e diminuir instâncias conforme demanda" = Auto Scaling.

**Perguntas típicas:**

- "Como ajustar automaticamente o número de instâncias à demanda?" → EC2 Auto Scaling.
- "A loja tem pico toda sexta às 18h." → Scheduled scaling.
- "Manter a CPU média do grupo em 50%." → Target tracking.
- "Como distribuir tráfego entre instâncias em várias AZs?" → Elastic Load Balancing.
- "Qual load balancer roteia por caminho de URL?" → ALB.
- "Qual load balancer para milhões de conexões TCP com IP fixo?" → NLB.
- "Qual load balancer para appliances de firewall de terceiros?" → Gateway Load Balancer.
- "Auto Scaling e ELB juntos garantem o quê?" → Alta disponibilidade e elasticidade (instâncias com falha são substituídas e o tráfego vai só para as saudáveis).

### 3.5 Containers e serverless

- **Amazon ECS****:** Orquestrador de containers da AWS. Dois tipos de execução: **EC2** (você gerencia as instâncias do cluster) ou **Fargate** (serverless).
- **AWS Fargate****:** Computação **serverless para containers**, usada com ECS ou EKS; você define CPU e memória da task e não gerencia servidores.
- **Amazon EKS:** **Kubernetes** gerenciado. Escolha quando a empresa já usa Kubernetes ou quer portabilidade.
- **Amazon ECR:** registro privado de imagens de container, com varredura de vulnerabilidades (integrado ao Inspector).
- **AWS Lambda**
  - Executa código em resposta a **eventos** (upload no S3, requisição no API Gateway, mensagem no SQS, regra do EventBridge, alteração no DynamoDB).
  - Sem servidores, escala automática, alta disponibilidade embutida.
  - **Limite de 15 minutos** por execução; memória configurável (a CPU acompanha a memória).
  - **Cobrança por número de requisições e por duração** (GB-segundo). Nada é cobrado quando não executa. Tem camada gratuita mensal.
  - Linguagens: Python, Node.js, Java, .NET, Go, Ruby e runtimes customizados.
- **Cai na prova:** "processar imagem assim que chega ao S3" = Lambda; "tarefa que roda por 2 horas" = não é Lambda (ECS/Fargate, Batch ou EC2); "containers sem gerenciar servidores" = Fargate; "já usa Kubernetes" = EKS.

**Complemento:**

- **Cobrança do Fargate:** por vCPU e memória alocadas à task, por segundo.
- **Cobrança do Lambda:** por número de requisições e duração (arredondada ao milissegundo), proporcional à memória configurada.

**Perguntas típicas:**

- "Qual serviço executa código sem servidores, em resposta a eventos?" → Lambda.
- "Qual é o tempo máximo de execução do Lambda?" → 15 minutos.
- "Como o Lambda é cobrado?" → Por requisição e por duração; nada quando não executa.
- "Rodar containers sem gerenciar instâncias." → Fargate (com ECS ou EKS).
- "Empresa já usa Kubernetes on-premises e quer migrar." → EKS.
- "Onde guardar imagens Docker privadas?" → ECR.
- "Qual serviço orquestra containers e é nativo da AWS?" → ECS.

### 3.6 Outros serviços de computação

- **AWS Elastic Beanstalk:** PaaS. Você envia o código (Java, .NET, Node.js, Python, PHP, Ruby, Go, Docker) e ele provisiona e gerencia capacidade, load balancer, Auto Scaling e monitoramento. Você mantém acesso aos recursos. Não tem custo adicional; paga só os recursos criados.
- **Amazon Lightsail:** servidores virtuais simples com **preço mensal fixo e previsível** (inclui computação, armazenamento e transferência). Bom para sites WordPress, apps pequenos e quem está começando.
- **AWS Batch:** executa grandes volumes de **jobs em lote**, provisionando a computação ideal automaticamente (EC2, Spot ou Fargate).
- **AWS Outposts:** ver 3.2.
- **Cai na prova:** "desenvolvedor quer subir aplicação web sem pensar em infraestrutura" = Elastic Beanstalk; "pequena empresa quer servidor com preço fixo" = Lightsail; "milhares de jobs de processamento" = Batch.

**Perguntas típicas:**

- "Desenvolvedor quer só subir o código Java e deixar a AWS cuidar de capacidade e balanceamento." → Elastic Beanstalk.
- "Elastic Beanstalk tem custo próprio?" → Não; paga-se só os recursos que ele cria.
- "Site WordPress simples com preço mensal fixo." → Lightsail.
- "Processar milhares de jobs em lote com a capacidade ideal." → AWS Batch.

## Domínio 3 — Tecnologia e Serviços (34%), parte 2

Bancos de dados e armazenamento: a prova pede o serviço certo para o tipo de dado e o padrão de acesso.

### 3.7 Bancos de dados

- **Banco no EC2 vs gerenciado:** no EC2 você cuida de SO, instalação, patch, backup e alta disponibilidade. Nos serviços gerenciados, a AWS cuida disso e você foca no schema, nas consultas e no acesso.
- **Amazon RDS****:** Banco relacional gerenciado.
  - Motores: **MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Db2 e Aurora**.
  - **Multi-AZ:** réplica de espera síncrona em outra AZ, com **failover automático**. Objetivo: **disponibilidade**, não performance.
  - **Read Replicas:** cópias assíncronas só de leitura (inclusive em outra região) para **escalar leitura**.
  - **Backups automáticos** com restauração para um ponto no tempo (retenção de até 35 dias) e **snapshots** manuais.
  - Sem acesso ao SO da instância de banco (a AWS gerencia).
- **Amazon Aurora****:** Relacional da AWS compatível com **MySQL e PostgreSQL**.
  - Mais performático que o MySQL e PostgreSQL padrão (a AWS cita até 5x e 3x, respectivamente).
  - Armazenamento cresce sozinho e mantém **6 cópias dos dados em 3 AZs**.
  - **Aurora Serverless:** capacidade ajustada automaticamente. **Aurora Global Database:** replicação entre regiões.
- **Amazon DynamoDB****:** NoSQL **chave-valor e documentos**, serverless, latência de milissegundos de um dígito em qualquer escala.
  - Modos de capacidade: **sob demanda** (paga por requisição) ou **provisionado** (com Auto Scaling).
  - **Global Tables:** replicação multi-região ativa-ativa.
  - **DAX:** cache em memória para leituras em microssegundos.
  - Streams, TTL (expiração automática de itens) e backup point-in-time.
- **Amazon ElastiCache****:** Cache em memória gerenciado, compatível com **Redis OSS/Valkey e Memcached**. Latência em microssegundos; reduz a carga do banco e guarda sessões.
- **Amazon Keyspaces****:** Cassandra gerenciado e serverless. Não aparece na lista oficial de serviços da prova, então dificilmente cai.
- **Amazon Neptune:** banco de **grafos**. Para redes sociais, motores de recomendação, detecção de fraude e grafos de conhecimento.
- **Amazon DocumentDB:** banco de **documentos** compatível com **MongoDB**.
- **Amazon Redshift:** **data warehouse** em colunas, para análise (OLAP) de grandes volumes com SQL e BI. Redshift Serverless dispensa gerenciar cluster; Redshift Spectrum consulta dados direto no S3.
- **Migração de bancos:** DMS e SCT (ver 3.17).

| Tipo de dado ou necessidade | Serviço |
| --- | --- |
| Relacional, transações (OLTP), SQL tradicional | RDS ou Aurora |
| Relacional com máxima performance e alta disponibilidade gerenciada | Aurora |
| Chave-valor, escala massiva, latência baixa, serverless | DynamoDB |
| Cache em memória | ElastiCache (ou DAX para DynamoDB) |
| Relacionamentos entre entidades (grafos) | Neptune |
| Documentos JSON compatíveis com MongoDB | DocumentDB |
| Análise de grandes volumes, BI, data warehouse (OLAP) | Redshift |

- **Cai na prova:** Multi-AZ = disponibilidade; Read Replica = performance de leitura. "Banco para carrinho de compras com milhões de acessos por segundo" = DynamoDB. "Recomendações tipo amigos de amigos" = Neptune.

**Perguntas típicas:**

- "Qual a vantagem do RDS sobre instalar o banco no EC2?" → A AWS cuida de patch, backups, hardware e failover.
- "Como garantir failover automático do banco para outra AZ?" → RDS Multi-AZ.
- "Como aliviar consultas de leitura pesadas?" → Read Replicas (ou cache com ElastiCache).
- "Qual banco relacional compatível com MySQL e PostgreSQL oferece mais performance?" → Aurora.
- "Qual banco NoSQL serverless com latência de milissegundos?" → DynamoDB.
- "Replicação multi-região ativa-ativa no DynamoDB." → Global Tables.
- "Cache de microssegundos para DynamoDB." → DAX.
- "Banco para relacionamentos complexos (redes sociais, fraude)." → Neptune.
- "Migrar banco MongoDB para serviço gerenciado." → DocumentDB.
- "Data warehouse para relatórios de BI sobre petabytes." → Redshift.
- "Quais motores o RDS suporta?" → MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Db2 e Aurora.

### 3.8 Amazon S3 — armazenamento de objetos

- **Objetos** (arquivo + metadados) em **buckets**. Nome do bucket é **único globalmente**, mas o bucket fica numa **região**. Objeto de até **5 TB** (upload multipart para arquivos grandes).
- **Durabilidade de 99,999999999% (11 noves)** em todas as classes; a **disponibilidade** varia por classe.
- **Segurança:** **Block Public Access** ativado por padrão; bucket policies, IAM, ACLs (desativadas por padrão); criptografia SSE-S3 por padrão; **presigned URLs** dão acesso temporário a um objeto.
- **Versionamento:** guarda versões anteriores; protege contra exclusão ou sobrescrita acidental. **MFA Delete** exige MFA para apagar versões.
- **Lifecycle policies:** movem objetos entre classes ou apagam após X dias, automaticamente.
- **Replicação:** Cross-Region Replication (CRR) e Same-Region Replication (SRR); exigem versionamento.
- **Object Lock:** modo WORM (gravar uma vez, ler muitas) para retenção e compliance.
- **Hospedagem de site estático** (HTML, CSS, JS, imagens).
- **S3 Transfer Acceleration:** acelera uploads de longa distância usando as edge locations.
- **Notificações de eventos:** disparam Lambda, SQS, SNS ou EventBridge quando um objeto é criado ou apagado.

| Classe | Quando usar | Detalhes de prova |
| --- | --- | --- |
| S3 Standard | Acesso frequente | Baixa latência; dados em no mínimo 3 AZs; sem taxa de recuperação |
| S3 Intelligent-Tiering | Padrão de acesso desconhecido ou que muda | Move objetos entre camadas sozinho; pequena taxa de monitoramento; sem taxa de recuperação |
| S3 Express One Zone | Latência mínima, alto desempenho | Uma AZ; milissegundos de um dígito |
| S3 Standard-IA | Pouco acesso, mas precisa ser rápido | Armazenamento mais barato, taxa por GB recuperado; mínimo de 30 dias |
| S3 One Zone-IA | Pouco acesso e dado que pode ser recriado | Uma AZ só (perde dados se a AZ for destruída); mais barato que Standard-IA |
| S3 Glacier Instant Retrieval | Arquivo acessado cerca de uma vez por trimestre | Recuperação em milissegundos; mínimo de 90 dias |
| S3 Glacier Flexible Retrieval | Arquivo sem pressa de acesso | Recuperação de minutos (expedited) a 12 horas (bulk); mínimo de 90 dias |
| S3 Glacier Deep Archive | Retenção de longo prazo (compliance por 7 a 10 anos) | **Mais barato de todos**; recuperação em até 12 horas (padrão) ou 48 horas (bulk); mínimo de 180 dias |

- **Cai na prova:** "padrão de acesso imprevisível" = Intelligent-Tiering; "logs que precisam ficar 7 anos e quase nunca são lidos" = Glacier Deep Archive; "miniaturas que podem ser geradas de novo" = One Zone-IA; "arquivo raro, mas precisa abrir na hora" = Glacier Instant Retrieval.

**Complemento:**

- **S3 Glacier Vault Lock / Object Lock em modo compliance:** impede que qualquer pessoa, inclusive o root, apague dados antes do prazo de retenção.
- **Cobrança do S3:** armazenamento por GB-mês, requisições, recuperação (classes IA e Glacier) e transferência de saída.

**Perguntas típicas:**

- "Qual é a durabilidade do S3?" → 11 noves (99,999999999%).
- "Como proteger contra exclusão acidental?" → Versionamento (e MFA Delete).
- "Como mover dados para classes mais baratas automaticamente após 30 dias?" → Lifecycle policy.
- "Como dar acesso temporário a um arquivo privado?" → Presigned URL.
- "Como hospedar um site estático barato?" → S3 (com CloudFront na frente).
- "Como copiar objetos automaticamente para outra região?" → Cross-Region Replication.
- "Como acelerar uploads de outros continentes?" → S3 Transfer Acceleration.
- "Qual classe para dados com acesso imprevisível?" → Intelligent-Tiering.
- "Qual a classe mais barata para arquivamento de longo prazo?" → Glacier Deep Archive.
- "Qual classe guarda dados em uma única AZ?" → One Zone-IA (ou Express One Zone).
- "Como garantir que logs não sejam alterados por 7 anos (WORM)?" → S3 Object Lock.

### 3.9 Outros serviços de armazenamento

- **Amazon EBS (Elastic Block Store):** armazenamento em **bloco** (disco) para EC2.
  - Persistente, preso a **uma AZ**, normalmente ligado a uma instância por vez.
  - Tipos: SSD de uso geral (**gp3**/gp2), SSD de IOPS provisionado (**io2**/io1, para bancos críticos), HDD otimizado para throughput (**st1**, big data e logs) e HDD frio (**sc1**, acesso raro).
  - **Snapshots** incrementais, guardados no S3, copiáveis entre regiões; usados para backup e para criar volumes em outra AZ.
  - Criptografia com KMS.
- **Instance store:** disco físico do host. Muito rápido, mas **efêmero**: perde os dados ao parar ou encerrar a instância.
- **Amazon EFS (Elastic File System):** sistema de arquivos **compartilhado** (NFS) para **Linux**, acessado por muitas instâncias ao mesmo tempo, em várias AZs. Cresce e encolhe sozinho; paga pelo que usa. Classes Standard, Infrequent Access e Archive.
- **Amazon FSx:** sistemas de arquivos gerenciados de terceiros:
  - **FSx for Windows File Server:** SMB, integrado ao Active Directory.
  - **FSx for Lustre:** alto desempenho para HPC e machine learning, integrado ao S3.
  - **FSx for NetApp ONTAP** e **FSx for OpenZFS:** para migrar storages NAS existentes.
- **AWS Storage Gateway:** armazenamento **híbrido**; liga o datacenter on-premises ao armazenamento na AWS.
  - **S3 File Gateway:** arquivos via NFS/SMB gravados como objetos no S3.
  - **FSx File Gateway:** acesso local de baixa latência ao FSx for Windows.
  - **Volume Gateway:** volumes iSCSI com cópia na AWS.
  - **Tape Gateway:** fitas virtuais; substitui backup em fita física, arquivando no S3 Glacier.
- **AWS Backup:** gerencia **backups de forma centralizada** com políticas (EC2, EBS, RDS, Aurora, DynamoDB, EFS, FSx, S3 etc.), inclusive entre contas e regiões.
- **AWS Elastic Disaster Recovery:** replica servidores (on-premises ou na nuvem) continuamente para a AWS e permite recuperar em minutos em caso de desastre.
- **Família AWS Snow:** dispositivos físicos para **mover grandes volumes de dados** quando a rede é lenta, cara ou inexistente, e para **computação na borda** em locais desconectados (navios, campo, áreas remotas).
  - **Snowball Edge:** versões otimizadas para armazenamento (dezenas de TB) ou para computação.
  - Versões menores (Snowcone) e o caminhão Snowmobile foram descontinuados, mas podem aparecer em questões antigas.
  - Regra prática: se transferir pela rede levaria semanas, use Snow.
- **Transferência online:** AWS DataSync (copia dados de NFS/SMB on-premises para S3, EFS ou FSx de forma automatizada) e AWS Transfer Family (SFTP/FTPS/FTP direto para S3 ou EFS).

| Tipo | Serviço | Acesso |
| --- | --- | --- |
| Objeto | S3 | Via API/HTTP, de qualquer lugar |
| Bloco | EBS, instance store | Um disco ligado a uma instância EC2 |
| Arquivo (Linux, NFS) | EFS | Muitas instâncias ao mesmo tempo |
| Arquivo (Windows, SMB) | FSx for Windows | Muitas instâncias ao mesmo tempo |
| Híbrido | Storage Gateway | Datacenter local usando armazenamento na AWS |

- **Cai na prova:** "várias instâncias Linux precisam ler os mesmos arquivos" = EFS; "disco para banco de dados no EC2" = EBS io2; "substituir backup em fita" = Tape Gateway; "migrar 500 TB de um datacenter com internet lenta" = Snowball Edge.

**Perguntas típicas:**

- "Qual armazenamento em bloco persistente para EC2?" → EBS.
- "Um volume EBS pode ser usado em outra AZ?" → Não diretamente; cria-se um snapshot e um novo volume na outra AZ.
- "Onde ficam os snapshots do EBS?" → No S3 (gerenciado pela AWS), de forma incremental.
- "Sistema de arquivos compartilhado para várias instâncias Linux." → EFS.
- "Compartilhamento de arquivos Windows integrado ao Active Directory." → FSx for Windows File Server.
- "Sistema de arquivos de alto desempenho para HPC." → FSx for Lustre.
- "Aplicações locais precisam usar armazenamento da AWS." → Storage Gateway.
- "Substituir fitas físicas de backup." → Tape Gateway.
- "Centralizar backups de vários serviços com políticas." → AWS Backup.
- "Mover dezenas de terabytes sem depender da internet." → Snowball Edge.
- "Processar dados num navio sem conexão." → Família Snow (computação na borda).
- "Recuperar servidores em minutos após desastre." → AWS Elastic Disaster Recovery.

## Domínio 3 — Tecnologia e Serviços (34%), parte 3

Rede: a VPC e seus componentes, conectividade com datacenters, DNS e entrega de conteúdo. Mesmo quem usa AWS no dia a dia costuma receber a rede pronta, por isso vale estudar cada componente.

### 3.10 Rede e entrega de conteúdo

**Amazon VPC**

- **VPC:** rede virtual isolada logicamente, dentro de uma **região**, com um bloco de IPs (CIDR) definido por você. Cada região tem uma **VPC padrão** pronta.
- **Subnet:** fatia da VPC dentro de **uma AZ**.
  - **Pública:** tem rota para um Internet Gateway.
  - **Privada:** sem rota direta para a internet (bancos, back-ends).
- **Internet Gateway (IGW):** permite comunicação entre a VPC e a internet (entrada e saída).
- **NAT Gateway:** fica na subnet pública e permite que recursos em **subnets privadas saiam para a internet** (ex.: baixar atualizações) **sem receber conexões de fora**. Gerenciado e pago por hora e por dado.
- **Route tables:** definem para onde vai o tráfego de cada subnet.
- **Security groups e NACLs:** ver 2.8.
- **VPC Peering:** liga duas VPCs (mesma conta, outra conta ou outra região) como se fossem uma rede. **Não é transitivo:** se A fala com B e B com C, A não fala com C.
- **AWS Transit Gateway:** **hub central** que conecta muitas VPCs e redes on-premises num modelo hub-and-spoke, simplificando dezenas de peerings.
- **VPC endpoints:** acessar serviços AWS **sem passar pela internet**.
  - **Gateway endpoint:** só para **S3 e DynamoDB**, gratuito.
  - **Interface endpoint (AWS PrivateLink):** cria uma interface de rede privada na sua subnet para a maioria dos serviços; pago.
- **AWS PrivateLink:** também permite expor um serviço seu para outras VPCs ou clientes de forma privada.
- **VPC Flow Logs:** registram o tráfego de rede (ver 2.7).

**Conectividade híbrida**

| Serviço | Como funciona | Quando usar |
| --- | --- | --- |
| AWS Site-to-Site VPN | Túnel IPsec **criptografado pela internet** entre o datacenter (Customer Gateway) e a AWS (Virtual Private Gateway ou Transit Gateway) | Rápido de configurar (minutos), barato; aceita a variação da internet; também serve de backup do Direct Connect |
| AWS Client VPN | VPN gerenciada para **usuários remotos** (notebooks) acessarem a VPC | Trabalho remoto |
| AWS Direct Connect | **Conexão física dedicada e privada**, que não passa pela internet, a partir de um local Direct Connect | Banda alta e estável, latência consistente, menor custo de transferência para grandes volumes; leva semanas para instalar; não é criptografado por padrão (pode rodar VPN por cima) |

**DNS, CDN e aceleração**

- **Amazon Route 53:** DNS gerenciado, altamente disponível. Registra domínios, roteia usuários para recursos e faz **health checks**.
  - **Políticas de roteamento:** simple, **weighted** (divide tráfego por percentual, ex.: testes A/B), **latency-based** (região com menor latência), **failover** (ativo-passivo), **geolocation** (por país/continente do usuário), **geoproximity** (por distância, com ajuste), **multivalue answer** e IP-based.
- **Amazon CloudFront:** **CDN** global. Faz **cache** de conteúdo estático e dinâmico nas edge locations, reduzindo latência e carga na origem.
  - Origens: S3, ALB, EC2, API Gateway ou qualquer servidor HTTP.
  - **Origin Access Control (OAC):** deixa o bucket S3 privado, acessível só pelo CloudFront.
  - HTTPS com certificado do ACM; restrição geográfica; inclui **Shield Standard** e integra com **WAF**.
  - Lambda@Edge e CloudFront Functions rodam código nas edge locations.
- **AWS Global Accelerator:** fornece **IPs estáticos anycast** e leva o tráfego pela **rede global da AWS** até o endpoint regional mais saudável e próximo. Melhora performance de aplicações TCP/UDP e faz failover rápido entre regiões. **Não faz cache.**
- **Amazon API Gateway****:** Pontos de prova: cria APIs REST, HTTP e WebSocket em qualquer escala; faz controle de tráfego (throttling), autenticação (IAM, Cognito, Lambda authorizer) e cache; integração clássica com Lambda para back-ends serverless; cobrado por chamada.
- **Cai na prova:** "subnet privada precisa baixar patches da internet" = NAT Gateway; "conectar 50 VPCs e o datacenter" = Transit Gateway; "acessar o S3 sem sair para a internet" = gateway endpoint; "link privado com banda dedicada" = Direct Connect; "conexão rápida e criptografada com o datacenter" = Site-to-Site VPN; "site com usuários no mundo todo, conteúdo estático" = CloudFront; "jogo multiplayer UDP com IPs fixos globais" = Global Accelerator; "mandar usuários para a região mais rápida" = Route 53 latency-based.

**Complemento:**

- **CloudFront signed URLs e signed cookies:** restringem o acesso a conteúdo privado distribuído pelo CloudFront (ex.: cursos pagos).
- **Route 53 health checks + failover:** se o endpoint principal cair, o DNS passa a responder com o secundário.
- **Bastion host**: instância na subnet pública usada para acessar recursos privados; o Session Manager é a alternativa sem porta aberta.

**Perguntas típicas:**

- "O que torna uma subnet pública?" → Ter rota para um Internet Gateway.
- "Instâncias em subnet privada precisam baixar atualizações." → NAT Gateway.
- "Conectar duas VPCs de contas diferentes." → VPC Peering.
- "Conectar dezenas de VPCs e o datacenter num hub." → Transit Gateway.
- "Acessar o S3 a partir da VPC sem passar pela internet." → Gateway VPC endpoint.
- "Conexão privada e dedicada, sem internet, com desempenho consistente." → Direct Connect.
- "Conexão criptografada com o datacenter, pronta hoje." → Site-to-Site VPN.
- "Funcionários em casa precisam acessar a VPC." → Client VPN.
- "Registrar domínio e gerenciar DNS." → Route 53.
- "Mandar 10% dos usuários para a nova versão." → Route 53 weighted routing.
- "Reduzir latência de conteúdo para usuários globais." → CloudFront.
- "IPs estáticos globais e failover rápido entre regiões para TCP/UDP." → Global Accelerator.
- "Criar e proteger uma API REST para funções Lambda." → API Gateway.

## Domínio 3 — Tecnologia e Serviços (34%), parte 4

Serviços de dados, IA, integração e aplicações. Aqui a prova quase sempre pergunta "qual serviço faz X", então o essencial é a função de cada um.

### 3.11 Analytics

- **Amazon Athena****:** Pontos de prova: SQL **serverless** direto em arquivos no S3 (CSV, JSON, Parquet); cobrado por **dados escaneados**; formatos colunares e particionamento reduzem custo; usa o catálogo do Glue.
- **AWS Glue:** **ETL serverless** (extrair, transformar e carregar dados) e **Data Catalog** (catálogo de metadados usado por Athena, Redshift e EMR). Crawlers descobrem o schema automaticamente.
- **Amazon Kinesis:** dados em **streaming e tempo real**.
  - **Kinesis Data Streams:** ingestão e processamento de streams (cliques, logs, telemetria).
  - **Amazon Data Firehose** (antes Kinesis Data Firehose): entrega streams automaticamente em S3, Redshift, OpenSearch e outros, sem administração.
  - **Kinesis Video Streams:** streaming de vídeo de dispositivos.
- **Amazon EMR:** plataforma de **big data** gerenciada com Apache Spark, Hadoop, Hive e Presto.
- **Amazon QuickSight:** **BI** serverless; dashboards e relatórios interativos, inclusive com perguntas em linguagem natural.
- **Amazon OpenSearch Service:** **busca** e **análise de logs** (sucessor do Elasticsearch gerenciado), com OpenSearch Dashboards.
- **Amazon Redshift:** data warehouse (ver 3.7).
- **Cai na prova:** "consultar logs no S3 com SQL sem servidor" = Athena; "processar cliques em tempo real" = Kinesis; "painéis para executivos" = QuickSight; "preparar e catalogar dados" = Glue; "Spark/Hadoop gerenciado" = EMR; "busca de texto em produtos" = OpenSearch.

**Perguntas típicas:**

- "Consultar arquivos no S3 com SQL padrão, sem infraestrutura." → Athena.
- "Como o Athena é cobrado?" → Por volume de dados escaneados.
- "Serviço de ETL serverless e catálogo de dados." → Glue.
- "Ingerir e processar dados de cliques em tempo real." → Kinesis Data Streams.
- "Entregar dados de streaming no S3 sem administração." → Amazon Data Firehose.
- "Rodar Spark e Hadoop gerenciados." → EMR.
- "Criar dashboards interativos de BI." → QuickSight.
- "Busca de texto e análise de logs." → OpenSearch Service.

### 3.12 IA e machine learning

Revise a função de cada serviço, porque a prova pede o serviço pelo caso de uso.

| Serviço | Função |
| --- | --- |
| Amazon SageMaker AI | Criar, treinar e implantar modelos de ML próprios |
| Amazon Bedrock | Usar modelos de IA generativa (foundation models) via API |
| Amazon Q | Assistente de IA generativa para empresas (Q Business) e desenvolvedores (Q Developer) |
| Amazon Rekognition | Análise de imagens e vídeos: rostos, objetos, textos, conteúdo impróprio |
| Amazon Comprehend | Processamento de linguagem natural: sentimento, entidades, idioma, tópicos |
| Amazon Lex | Chatbots e interfaces conversacionais por voz e texto (mesma tecnologia da Alexa) |
| Amazon Polly | Texto para fala |
| Amazon Transcribe | Fala para texto |
| Amazon Translate | Tradução de textos |
| Amazon Textract | Extrair texto, formulários e tabelas de documentos digitalizados |
| Amazon Kendra | Busca inteligente em documentos corporativos |

**Perguntas típicas:**

- "Construir, treinar e implantar modelos de ML próprios." → SageMaker AI.
- "Identificar rostos e objetos em fotos." → Rekognition.
- "Analisar o sentimento de avaliações de clientes." → Comprehend.
- "Criar um chatbot de atendimento." → Lex.
- "Converter texto em voz." → Polly. "Converter áudio em texto." → Transcribe.
- "Traduzir conteúdo do site." → Translate.
- "Extrair dados de formulários escaneados." → Textract.
- "Busca inteligente nos documentos internos da empresa." → Kendra.
- "Assistente de IA generativa para funcionários e desenvolvedores." → Amazon Q.

### 3.13 Integração de aplicações

- **Amazon SQS****:** Pontos de prova:
  - Fila gerenciada que **desacopla** componentes; o consumidor **puxa** (poll) as mensagens.
  - **Standard:** throughput quase ilimitado, entrega pelo menos uma vez, ordem não garantida. **FIFO:** ordem garantida e entrega exatamente uma vez.
  - Retenção padrão de 4 dias, configurável até 14 dias; **visibility timeout**; **dead-letter queue** para mensagens com falha.
- **Amazon SNS:** **pub/sub**. Um produtor publica num **tópico** e a mensagem é **empurrada** (push) para todos os assinantes: e-mail, SMS, HTTP, Lambda, filas SQS e push mobile.
  - **Fan-out:** SNS publica e várias filas SQS recebem a mesma mensagem para processamento paralelo.
- **Amazon EventBridge:** **barramento de eventos** serverless. Recebe eventos de serviços AWS, de aplicações e de parceiros SaaS e os roteia com **regras** para destinos. **EventBridge Scheduler** agenda tarefas (estilo cron).
- **AWS Step Functions:** **orquestra fluxos de trabalho** com várias etapas em máquinas de estado visuais, com tratamento de erros e novas tentativas (ex.: várias Lambdas em sequência, com aprovação humana no meio).
- **Cai na prova:** "desacoplar e absorver picos" = SQS; "notificar vários sistemas ao mesmo tempo" = SNS; "reagir a eventos de um SaaS" = EventBridge; "coordenar várias etapas de um processo" = Step Functions.

**Perguntas típicas:**

- "Desacoplar componentes para que um pico não derrube o processamento." → SQS.
- "Garantir ordem e processamento exatamente uma vez." → Fila SQS FIFO.
- "Enviar a mesma mensagem para vários sistemas e para e-mail." → SNS.
- "Um evento precisa ser processado por várias filas em paralelo." → Fan-out com SNS + SQS.
- "Reagir a eventos de serviços AWS e de aplicações SaaS com regras." → EventBridge.
- "Executar uma tarefa todo dia às 2h sem servidor." → EventBridge Scheduler (disparando Lambda).
- "Orquestrar um processo com várias etapas e tratamento de erro." → Step Functions.

### 3.14 Aplicações de negócio, usuário final, front-end e IoT

- **Amazon Connect:** **central de atendimento (contact center) na nuvem**, com voz, chat e tarefas, pago por uso.
- **Amazon SES (Simple Email Service):** envio de **e-mails** transacionais e de marketing em grande volume. Diferença para o SNS: SES é para e-mails formatados a clientes; SNS é para notificações simples.
- **Amazon WorkSpaces:** **desktops virtuais** (DaaS) Windows ou Linux, acessados de qualquer dispositivo.
- **Amazon AppStream 2.0:** **streaming de aplicações** de desktop para o navegador, sem entregar o desktop inteiro.
- **Amazon WorkSpaces Secure Browser:** navegador seguro gerenciado para acessar sites internos sem VPN.
- **AWS Amplify:** ferramentas para **criar, implantar e hospedar** aplicações web e mobile full-stack rapidamente.
- **AWS AppSync:** **APIs GraphQL** gerenciadas, com dados em tempo real e sincronização offline.
- **AWS IoT Core:** conecta **dispositivos IoT** à nuvem (protocolo MQTT) com segurança e em grande escala.
- **Cai na prova:** "call center" = Connect; "funcionários remotos precisam de um desktop" = WorkSpaces; "rodar um app de desktop no navegador" = AppStream 2.0; "sensores enviando dados" = IoT Core.

**Perguntas típicas:**

- "Criar uma central de atendimento na nuvem." → Amazon Connect.
- "Enviar e-mails de confirmação e marketing em massa." → SES.
- "Oferecer desktops virtuais a funcionários remotos." → WorkSpaces.
- "Disponibilizar um aplicativo de desktop pelo navegador." → AppStream 2.0.
- "Criar e hospedar rapidamente um app web ou mobile full-stack." → Amplify.
- "API GraphQL gerenciada com dados em tempo real." → AppSync.
- "Conectar milhões de sensores à nuvem." → IoT Core.

### 3.15 Ferramentas de desenvolvimento

- **AWS CLI:** ver 3.1.
- **AWS CodeBuild:** **compila, testa e empacota** código; serverless, cobrado por minuto de build.
- **AWS CodePipeline:** **orquestra a esteira de CI/CD** (fonte → build → teste → deploy) — o GitHub Actions é um equivalente de terceiros.
- **AWS CodeDeploy:** automatiza **deploys** em EC2, servidores on-premises, Lambda e ECS (não está na lista oficial, mas costuma aparecer com os outros).
- **AWS X-Ray:** **rastreamento distribuído**: acompanha requisições entre microsserviços para achar gargalos e erros.
- **AWS CodeArtifact:** repositório gerenciado de pacotes (npm, Maven, PyPI).
- **Cai na prova:** "descobrir qual microsserviço está deixando a requisição lenta" = X-Ray; "automatizar a esteira de entrega" = CodePipeline; "compilar e rodar testes" = CodeBuild.

**Perguntas típicas:**

- "Orquestrar a esteira de CI/CD na AWS." → CodePipeline.
- "Compilar e executar testes sem gerenciar servidores de build." → CodeBuild.
- "Automatizar deploy em EC2 e servidores on-premises." → CodeDeploy.
- "Encontrar gargalos de latência entre microsserviços." → X-Ray.

## Domínio 3 — Tecnologia e Serviços (34%), parte 5

Gestão, governança e migração: serviços que a prova trata como conhecimento básico, mesmo para quem não administra contas no dia a dia.

### 3.16 Gestão e governança

- **AWS CloudFormation:** infraestrutura como código nativa.
  - **Templates** em JSON ou YAML descrevem os recursos; cada execução cria uma **stack** (pilha) gerenciada como uma unidade.
  - **StackSets:** implantam a mesma stack em várias contas e regiões.
  - **Drift detection:** detecta recursos alterados manualmente fora do template.
  - O serviço é gratuito; paga-se só pelos recursos criados.
- **AWS Systems Manager:** central de operações para gerenciar frotas de instâncias EC2 e servidores on-premises (via agente SSM).
  - **Session Manager:** acesso ao shell sem abrir porta SSH nem usar bastion host.
  - **Run Command:** executa comandos em várias instâncias de uma vez.
  - **Patch Manager:** automatiza a aplicação de patches.
  - **Parameter Store:** guarda configurações e segredos (ver 2.3).
  - **Automation** e **Inventory:** runbooks automatizados e inventário de software.
- **Monitoramento e auditoria:** CloudWatch, CloudTrail e Config (ver 2.7).
- **Governança multi-conta:** Organizations, Control Tower, Service Catalog e RAM (ver 2.4).
- **AWS Health Dashboard:**
  - **Service health:** status público de todos os serviços em todas as regiões.
  - **Your account health:** eventos que afetam **os seus** recursos (manutenções agendadas, falhas, avisos), com orientação de correção.
  - A **AWS Health API** está disponível a partir do plano Business.
- **Service Quotas:** mostra os limites (cotas) dos serviços por região e permite **pedir aumento**. Pode gerar alarmes quando o uso se aproxima do limite.
- **AWS License Manager:** controla o uso de **licenças de software** (Microsoft, Oracle, SAP) para evitar excesso e multas.
- **AWS Compute Optimizer:** usa machine learning sobre as métricas de uso para recomendar o **tamanho ideal** de EC2, Auto Scaling groups, EBS, Lambda e tasks ECS no Fargate.
- **AWS Trusted Advisor:** ver 2.9. **Well-Architected Tool:** ver 1.4.
- **AWS Management Console:** inclui o aplicativo móvel para acompanhar recursos e alarmes.
- **Cai na prova:** "acessar instância sem SSH nem bastion" = Session Manager; "aplicar patch em 500 servidores" = Systems Manager Patch Manager; "evento da AWS que afeta minhas instâncias" = Health Dashboard; "preciso de mais instâncias do que o limite permite" = Service Quotas; "instância superdimensionada" = Compute Optimizer; "mesma infraestrutura em várias contas" = CloudFormation StackSets.

**Complemento:**

- **Tags:** pares chave-valor nos recursos, usados para organizar, controlar acesso e separar custos (ver cost allocation tags em 4.4).
- **Disponibilidade do Health Dashboard:** gratuito para todos os clientes; a API exige plano Business ou superior.

**Perguntas típicas:**

- "Provisionar infraestrutura a partir de templates JSON/YAML." → CloudFormation.
- "Implantar a mesma stack em várias contas e regiões." → CloudFormation StackSets.
- "Gerenciar e aplicar patches em uma frota de instâncias, inclusive on-premises." → Systems Manager.
- "Acessar a instância sem abrir a porta 22." → Systems Manager Session Manager.
- "Ver eventos de manutenção da AWS que afetam meus recursos." → AWS Health Dashboard.
- "Pedir aumento do limite de instâncias." → Service Quotas.
- "Controlar quantas licenças de SQL Server estão em uso." → License Manager.
- "Recomendar o tamanho ideal das instâncias com base no uso." → Compute Optimizer.

### 3.17 Migração e transferência

As ferramentas seguem a ordem de uma migração: avaliar, planejar e migrar.

| Serviço | Etapa | O que faz |
| --- | --- | --- |
| Migration Evaluator | Avaliar | Monta o **caso de negócio**: estima o custo de rodar o ambiente atual na AWS (TCO) |
| AWS Application Discovery Service | Avaliar | Coleta dados dos servidores on-premises (configuração, uso, **dependências** entre aplicações), com ou sem agente |
| AWS Migration Hub | Acompanhar | **Painel único** para acompanhar o progresso das migrações em várias ferramentas |
| AWS Application Migration Service (MGN) | Migrar servidores | **Lift-and-shift (Rehost)**: replica servidores continuamente para a AWS e faz o corte com mínimo de indisponibilidade |
| AWS Database Migration Service (DMS) | Migrar bancos | Migra bancos com o **banco de origem funcionando** (replicação contínua), entre motores iguais ou diferentes |
| AWS Schema Conversion Tool (SCT) | Migrar bancos | **Converte o schema** e o código do banco entre motores diferentes (ex.: Oracle para Aurora PostgreSQL); usado junto com o DMS |
| Família AWS Snow | Transferir dados | Transferência **offline** de grandes volumes em dispositivo físico (ver 3.9) |
| AWS DataSync | Transferir dados | Transferência **online** e automatizada de arquivos para S3, EFS ou FSx (ver 3.9) |
| AWS Transfer Family | Transferir dados | SFTP, FTPS e FTP gerenciados direto para S3 ou EFS |

- **Migração homogênea** (MySQL → RDS MySQL): só o DMS. **Heterogênea** (Oracle → Aurora): SCT para converter o schema e DMS para mover os dados.
- **Cai na prova:** "descobrir dependências entre os servidores antes de migrar" = Application Discovery Service; "migrar VMs sem alterar" = Application Migration Service; "migrar banco sem parar o sistema" = DMS; "converter Oracle para PostgreSQL" = SCT; "justificar o custo da migração para a diretoria" = Migration Evaluator.

**Perguntas típicas:**

- "Levantar servidores e dependências antes de migrar." → Application Discovery Service.
- "Estimar quanto a empresa vai economizar ao migrar." → Migration Evaluator.
- "Acompanhar todas as migrações num painel central." → Migration Hub.
- "Migrar servidores físicos e VMs para EC2 com pouca indisponibilidade." → Application Migration Service.
- "Migrar um banco sem desligar a aplicação." → DMS.
- "Converter um banco Oracle para Aurora PostgreSQL." → SCT + DMS.
- "Transferir arquivos online de forma automatizada para o S3." → DataSync.
- "Parceiros enviam arquivos via SFTP para o S3." → Transfer Family.

## Domínio 4 — Billing, Pricing e Suporte (12%)

Peso menor, mas as questões são diretas: decorar as tabelas desta seção garante a maior parte desses pontos.

### 4.1 Princípios de preço da AWS

- **Pague conforme o uso (pay-as-you-go):** sem contrato nem investimento inicial.
- **Economize ao se comprometer:** reservas e Savings Plans dão desconto em troca de compromisso de 1 ou 3 anos.
- **Pague menos por unidade quando usa mais:** faixas de desconto por volume (ex.: S3, transferência de dados).
- **Três grandes geradores de custo:** computação, armazenamento e **transferência de dados de saída**.

**Perguntas típicas:**

- "Qual é um princípio de preço da AWS?" → Pagar conforme o uso, economizar ao se comprometer, pagar menos por unidade ao usar mais.
- "Quais são os três principais geradores de custo?" → Computação, armazenamento e transferência de dados de saída.

### 4.2 Modelos de compra do EC2

| Modelo | Desconto (referência AWS) | Compromisso | Quando usar |
| --- | --- | --- | --- |
| On-Demand | Nenhum | Nenhum; cobrança por segundo ou hora | Cargas curtas, imprevisíveis, que não podem ser interrompidas; testes e desenvolvimento |
| Reserved Instances (Standard) | Até cerca de 72% | 1 ou 3 anos, tipo de instância definido | Carga estável e previsível (ex.: banco de dados sempre ligado) |
| Reserved Instances (Convertible) | Menor que o Standard | 1 ou 3 anos; pode trocar família, SO e tenancy | Carga estável, mas com chance de mudar de tipo |
| Compute Savings Plans | Até cerca de 66% | Gasto fixo por hora (US$/h) por 1 ou 3 anos | Máxima flexibilidade: vale para qualquer família, tamanho, região, SO, e também para **Fargate e Lambda** |
| EC2 Instance Savings Plans | Até cerca de 72% | Gasto por hora numa família de instância numa região | Família fixa, mas com liberdade de tamanho e SO |
| Spot Instances | Até cerca de 90% | Nenhum; a AWS pode retomar com **aviso de 2 minutos** | Cargas tolerantes a interrupção e flexíveis: batch, análise de dados, CI/CD, renderização |
| Dedicated Hosts | Mais caro | On-Demand ou reserva | **Servidor físico inteiro dedicado**, com visibilidade de sockets e núcleos: licenças por socket/núcleo (BYOL) e compliance |
| Dedicated Instances | Mais caro | On-Demand ou reserva | Instâncias em hardware não compartilhado com outros clientes, sem controle do servidor físico |
| On-Demand Capacity Reservations | Nenhum por si só | Sem prazo; paga mesmo sem usar | **Garantir capacidade** numa AZ específica (ex.: evento previsto); combina com Savings Plans |

- **Formas de pagamento de RIs e Savings Plans:** All Upfront (maior desconto), Partial Upfront e No Upfront (menor desconto).
- **RIs regionais vs zonais:** a zonal reserva capacidade numa AZ; a regional dá flexibilidade de AZ e tamanho, sem reservar capacidade.
- **Reserved Instance Marketplace:** permite revender RIs Standard que não serão mais usadas.
- **Reservas em outros serviços:** RDS, ElastiCache, Redshift e OpenSearch têm instâncias ou nós reservados; DynamoDB tem capacidade reservada.
- **Cai na prova:** "não pode ser interrompida e é imprevisível" = On-Demand; "vai rodar 24/7 por 3 anos" = Reserved ou Savings Plans; "desconto que cobre EC2, Fargate e Lambda" = Compute Savings Plans; "maior desconto e tolera interrupção" = Spot; "licença por núcleo físico" = Dedicated Host.

**Perguntas típicas:**

- "Aplicação nova, sem histórico de uso, que não pode ser interrompida." → On-Demand.
- "Servidor de banco que roda 24/7 pelos próximos 3 anos." → Reserved Instances ou Savings Plans (3 anos, All Upfront dá o maior desconto).
- "Desconto com flexibilidade entre EC2, Fargate e Lambda." → Compute Savings Plans.
- "Processamento em lote que pode ser interrompido e reiniciado." → Spot.
- "Qual o aviso antes de uma Spot ser interrompida?" → 2 minutos.
- "Licença de software por núcleo físico." → Dedicated Host.
- "Garantir capacidade numa AZ para um evento, sem contrato longo." → On-Demand Capacity Reservation.
- "Qual opção de pagamento dá o maior desconto?" → All Upfront.
- "Reservas compradas podem ser revendidas?" → Sim, RIs Standard no Reserved Instance Marketplace.

### 4.3 Como outros recursos são cobrados

- **Transferência de dados:**
  - **Entrada** da internet para a AWS: **grátis**.
  - **Saída** da AWS para a internet: **cobrada**, com faixas por volume.
  - Entre **regiões**: cobrada. Entre **AZs** na mesma região: cobrada.
  - Dentro da mesma AZ por IP privado: grátis. Da origem AWS para o CloudFront: grátis.
- **Armazenamento:** S3 por GB-mês, por requisição e por recuperação (nas classes IA e Glacier); EBS pelo **volume provisionado**, mesmo que não esteja cheio; EFS pelo que é usado.
- **Serverless:** Lambda por requisição e duração; DynamoDB sob demanda por leitura e escrita; Athena por dado escaneado.
- **IPv4 público:** todo endereço IPv4 público é cobrado por hora.
- **Serviços sem custo próprio** (paga só os recursos que criam): CloudFormation, Elastic Beanstalk, Auto Scaling, IAM, Organizations, consolidated billing.
- **AWS Free Tier:** tradicionalmente cobrado na prova em três tipos: **sempre gratuito** (ex.: cota mensal de requisições do Lambda), **12 meses gratuitos** para contas novas (ex.: horas de instância micro) e **testes gratuitos** de curto prazo (ex.: GuardDuty). Desde meados de 2025, contas novas recebem um modelo baseado em **créditos** com plano gratuito por tempo limitado; confira a página oficial do Free Tier.
- **Cai na prova:** "o que é sempre grátis?" = transferência de entrada e serviços como IAM; "como reduzir custo de saída para usuários globais?" = CloudFront.

**Perguntas típicas:**

- "Qual transferência de dados é gratuita?" → Entrada da internet para a AWS (e dentro da mesma AZ por IP privado).
- "Qual transferência é cobrada?" → Saída para a internet, entre regiões e entre AZs.
- "Um volume EBS de 500 GB com 100 GB usados é cobrado por quanto?" → Pelos 500 GB provisionados.
- "Qual serviço não tem custo próprio?" → IAM, CloudFormation, Elastic Beanstalk, Auto Scaling, Organizations.
- "O que é o Free Tier?" → Uso gratuito limitado para experimentar serviços (sempre gratuito, por período ou testes; contas novas usam modelo de créditos).

### 4.4 Ferramentas de custo e faturamento

| Ferramenta | Para que serve | Detalhes de prova |
| --- | --- | --- |
| AWS Pricing Calculator | **Estimar** o custo antes de criar recursos | Gratuita, sem precisar de conta; gera estimativas compartilháveis |
| Billing and Cost Management (Bills) | Ver a **fatura** do mês, por serviço e região | Ponto de partida do faturamento |
| AWS Cost Explorer | **Visualizar e analisar** gastos passados e **prever** os próximos meses | Filtra por serviço, conta, região e tag; recomendações de rightsizing, RIs e Savings Plans; relatórios de uso e cobertura de reservas |
| AWS Budgets | Definir orçamentos e receber **alertas** | Orçamentos de custo, uso, RIs e Savings Plans; alerta pelo valor real ou previsto; **Budget Actions** podem aplicar políticas ou parar recursos |
| AWS Cost and Usage Report (CUR) / Data Exports | Relatório **mais detalhado** possível, hora a hora, por recurso | Entregue num bucket S3; analisado com Athena, QuickSight ou Redshift |
| AWS Cost Anomaly Detection | Detectar **gastos fora do padrão** com ML | Envia alertas com a causa provável |
| Cost allocation tags | **Separar custos** por projeto, time, ambiente ou centro de custo | Tags definidas pelo usuário ou geradas pela AWS; precisam ser **ativadas** no console de Billing para aparecer nos relatórios |
| AWS Organizations (consolidated billing) | **Fatura única** para várias contas | Soma o uso para descontos por volume; compartilha RIs e Savings Plans entre contas; sem custo extra |
| AWS Billing Conductor | Faturamento personalizado | Para revendedores e grandes empresas que refaturam clientes ou áreas internas |
| AWS Marketplace | Comprar **software de terceiros** | Cobrado na fatura AWS; AMIs, SaaS, contêineres, dados; licença por uso ou BYOL |
| CloudWatch billing alarm | Alarme de custo baseado na métrica de cobrança | Alternativa simples ao Budgets |

- **Outras fontes de economia:** Trusted Advisor (recursos ociosos), Compute Optimizer (rightsizing) e Savings Plans recommendations no Cost Explorer.
- **Cai na prova:** "estimar antes de migrar" = Pricing Calculator; "ver tendência e prever gasto" = Cost Explorer; "alerta quando passar de US$ 500" = Budgets; "dados mais granulares para análise" = CUR; "ratear custos por departamento" = cost allocation tags; "várias contas, uma fatura e desconto por volume" = consolidated billing.

**Perguntas típicas:**

- "Estimar o custo de uma arquitetura antes de criá-la." → Pricing Calculator.
- "Visualizar gastos dos últimos meses e prever o próximo." → Cost Explorer.
- "Receber alerta quando o gasto previsto passar do orçamento." → Budgets.
- "Relatório mais detalhado de custo e uso, por hora e recurso." → Cost and Usage Report.
- "Ser avisado de um gasto anormal." → Cost Anomaly Detection.
- "Separar custos por projeto ou departamento." → Cost allocation tags (ativadas no Billing).
- "Uma fatura para várias contas, com desconto por volume." → Consolidated billing no Organizations.
- "Comprar software de terceiros pago na fatura AWS." → AWS Marketplace.
- "Onde ver recomendações de Savings Plans?" → Cost Explorer.

### 4.5 Planos de AWS Support

| Plano | Preço de referência | Canais | Tempos de resposta | Destaques |
| --- | --- | --- | --- | --- |
| Basic | Gratuito | Atendimento ao cliente 24/7 só para conta e faturamento | Sem suporte técnico | Documentação, whitepapers, re:Post, Health Dashboard, verificações principais do Trusted Advisor |
| Developer | A partir de US$ 29/mês | E-mail em horário comercial | Orientação geral: menos de 24 h úteis; sistema prejudicado: menos de 12 h úteis | Para testes e desenvolvimento; orientação de arquitetura geral |
| Business | A partir de US$ 100/mês | Telefone, chat e e-mail 24/7 | Sistema de produção prejudicado: menos de 4 h; **produção fora do ar: menos de 1 h** | **Todas as verificações do Trusted Advisor**; Health API; suporte a software de terceiros comum; Infrastructure Event Management pago à parte |
| Enterprise On-Ramp | A partir de US$ 5.500/mês | Telefone, chat e e-mail 24/7 | **Sistema crítico de negócio fora do ar: menos de 30 min** | **Pool de TAMs**; Concierge Support Team (faturamento e conta); revisões consultivas |
| Enterprise | A partir de US$ 15.000/mês | Telefone, chat e e-mail 24/7 | **Sistema crítico de negócio fora do ar: menos de 15 min** | **TAM dedicado**; Concierge; Infrastructure Event Management; revisões Well-Architected e de operações; treinamentos |

- **TAM (Technical Account Manager):** consultor técnico que acompanha a conta de forma proativa. Dedicado só no Enterprise; compartilhado (pool) no Enterprise On-Ramp.
- **Concierge Support Team:** especialistas em faturamento e gestão de conta (Enterprise On-Ramp e Enterprise).
- **Infrastructure Event Management (IEM):** apoio da AWS para planejar eventos de grande escala (lançamentos, Black Friday).
- **Cai na prova:** "menor plano com suporte 24/7 por telefone" = Business; "menor plano com todas as verificações do Trusted Advisor" = Business; "TAM dedicado" = Enterprise; "resposta em 15 minutos" = Enterprise; "só precisa de ajuda com a fatura" = Basic (atendimento ao cliente é grátis). Preços e tempos mudam com frequência: confira a página oficial de planos antes da prova.

**Perguntas típicas:**

- "Qual o plano mais barato com suporte técnico 24/7 por telefone?" → Business.
- "Qual o plano mais barato com todas as verificações do Trusted Advisor?" → Business.
- "Qual plano inclui TAM dedicado?" → Enterprise.
- "Qual plano dá acesso a um pool de TAMs?" → Enterprise On-Ramp.
- "Qual plano responde em menos de 15 minutos a um sistema crítico fora do ar?" → Enterprise.
- "Qual plano responde em menos de 1 hora a produção fora do ar?" → Business.
- "Ambiente de testes que só precisa de ajuda técnica ocasional por e-mail." → Developer.
- "O plano Basic oferece suporte técnico?" → Não; só atendimento de conta e faturamento, documentação e re:Post.
- "Quem ajuda com dúvidas de faturamento em planos Enterprise?" → Concierge Support Team.
- "Quem pode mudar o plano de suporte?" → O usuário root.

### 4.6 Outros recursos de ajuda

- **AWS re:Post:** comunidade de perguntas e respostas moderada pela AWS (substituiu os antigos fóruns).
- **AWS Knowledge Center:** artigos com respostas às perguntas mais frequentes dos clientes.
- **Documentação, whitepapers e AWS Prescriptive Guidance:** guias e padrões oficiais.
- **AWS Professional Services:** time de consultoria da própria AWS.
- **AWS Partner Network (APN):** parceiros certificados — de serviços/consultoria (implementam projetos) e de tecnologia/software (produtos que integram com a AWS).
- **AWS Marketplace:** catálogo de software de terceiros (ver 4.4).
- **AWS Managed Services (AMS):** a AWS opera a infraestrutura do cliente (monitoramento, patches, backup, incidentes).
- **Solutions Architects e equipe de conta:** orientação técnica e comercial.
- **AWS Activate:** créditos e recursos para startups.
- **AWS Trust & Safety:** denúncia de abuso (ver 2.10).
- **AWS Training and Certification / Skill Builder:** cursos e laboratórios oficiais.
- **Cai na prova:** "precisa de uma consultoria para implementar o projeto" = AWS Professional Services ou um parceiro da APN; "quer que a AWS opere a infraestrutura" = AWS Managed Services; "dúvida técnica da comunidade" = re:Post.

**Perguntas típicas:**

- "Encontrar um parceiro certificado para implementar a migração." → AWS Partner Network.
- "Contratar consultoria diretamente da AWS." → AWS Professional Services.
- "Terceirizar a operação diária da infraestrutura para a AWS." → AWS Managed Services.
- "Tirar dúvidas técnicas com a comunidade." → AWS re:Post.
- "Respostas prontas para dúvidas comuns." → AWS Knowledge Center.
- "Startup busca créditos para começar na AWS." → AWS Activate.

## Serviços menos conhecidos que podem aparecer

A AWS avisa que a lista de serviços no escopo não é exaustiva, e quem já fez a prova relata questões sobre serviços pouco divulgados. Esta seção reúne os mais citados. Basta saber para que cada um serve.

### Sustentabilidade

- **AWS Customer Carbon Footprint Tool:** ferramenta **gratuita** no console de Billing and Cost Management que mostra a **estimativa de emissões de carbono** do uso da AWS da conta, em toneladas métricas de CO₂ equivalente, com histórico e divisão por serviço e por região. Serve para acompanhar metas de sustentabilidade e se liga ao pilar **Sustentabilidade** do Well-Architected.
- Outras práticas sustentáveis que a prova associa a esse pilar: usar processadores Graviton, serviços gerenciados e serverless, rightsizing, desligar recursos ociosos e escolher classes de armazenamento adequadas.

### Ajuda, parceiros e soluções prontas

- **AWS IQ:** está na lista oficial da prova. Era um marketplace para contratar **especialistas freelancers certificados em AWS** para projetos sob demanda, pagos na própria fatura AWS. A AWS **encerrou o serviço em 28/05/2026** (a alternativa indicada é o AWS Marketplace Professional Services), mas ele ainda pode aparecer em questões.
- **AWS Solutions Library e AWS Prescriptive Guidance:** arquiteturas de referência e soluções prontas para implantar, validadas pela AWS.

### Outros serviços citados por quem fez a prova

| Serviço | O que faz | Exemplo de cenário |
| --- | --- | --- |
| AWS Security Token Service (STS) | Emite **credenciais temporárias**; é o que está por trás das IAM roles | "Qual serviço gera credenciais temporárias?" |
| AWS Network Firewall | Firewall de rede gerenciado para a VPC, com inspeção de tráfego e prevenção de intrusão | "Inspecionar e filtrar todo o tráfego que entra na VPC" |
| AWS Private Certificate Authority | Emite **certificados privados** para uso interno | "Certificados para serviços internos, não públicos" |
| Amazon MQ | Message broker gerenciado para **Apache ActiveMQ e RabbitMQ** | "Migrar aplicação que usa RabbitMQ sem reescrever" (SQS exigiria mudar o código) |
| Amazon MSK | **Apache Kafka** gerenciado | "Streaming com Kafka sem gerenciar cluster" |
| Amazon AppFlow | Transfere dados entre aplicações **SaaS** (Salesforce, SAP, Zendesk) e a AWS sem código | "Levar dados do Salesforce para o S3" |
| AWS Data Exchange | Encontrar e assinar **conjuntos de dados de terceiros** | "Comprar dados de mercado para análise" |
| AWS Lake Formation | Montar e proteger um **data lake** no S3 | "Criar data lake com controle de acesso centralizado" |
| Amazon Timestream | Banco de **séries temporais** | "Guardar leituras de sensores IoT ao longo do tempo" |
| Amazon MemoryDB | Banco **em memória durável**, compatível com Redis/Valkey | "Banco principal com latência de microssegundos e durabilidade" |
| Amazon Personalize | **Recomendações personalizadas** com ML | "Recomendar produtos como na Amazon.com" |
| AWS Device Farm | Testa apps web e mobile em **dispositivos reais** na nuvem | "Testar o app em vários modelos de celular" |
| AWS Fault Injection Service | **Engenharia do caos**: injeta falhas controladas para testar resiliência | "Simular falhas para validar a recuperação" (pilar Confiabilidade) |
| AWS Resilience Hub | Avalia e acompanha a **resiliência** das aplicações contra metas de RTO e RPO | "Verificar se a aplicação atende ao RTO definido" |
| EC2 Image Builder | Automatiza a criação e atualização de **AMIs** | "Manter imagens de servidor atualizadas e com patches" |
| Amazon Managed Grafana / Managed Service for Prometheus | Visualização e monitoramento de métricas com ferramentas open source gerenciadas | "Usar Grafana sem gerenciar servidores" |
| Amazon WorkMail | **E-mail corporativo** e calendário gerenciados | "E-mail empresarial compatível com Outlook" |

### O que está fora do escopo

O exam guide lista categorias que **não caem** na prova. Se uma alternativa citar um serviço delas, provavelmente é distrator:

- **Game Tech** (ex.: Amazon GameLift).
- **Serviços de mídia** (ex.: AWS Elemental).
- **Robótica** (ex.: AWS RoboMaker).
- **Satélite** (ex.: AWS Ground Station).
- **Blockchain** (ex.: Amazon Managed Blockchain).

**Perguntas típicas:**

- "Como acompanhar a pegada de carbono do uso da AWS?" → AWS Customer Carbon Footprint Tool.
- "Onde contratar especialistas certificados sob demanda para um projeto pequeno?" → AWS IQ (descontinuado; hoje, AWS Marketplace Professional Services ou um parceiro da APN).
- "Qual serviço emite as credenciais temporárias usadas pelas roles?" → AWS STS.
- "A aplicação usa RabbitMQ e deve migrar sem mudar o código." → Amazon MQ.
- "Testar a resiliência injetando falhas de propósito." → AWS Fault Injection Service.
- "Testar um app mobile em centenas de dispositivos reais." → AWS Device Farm.

## Pares que confundem e palavras-chave

Revise esta seção a cada poucos dias. A maioria dos erros de quem já usa AWS vem de trocar serviços vizinhos.

### Pares que mais confundem

| Par | Diferença em uma linha |
| --- | --- |
| CloudTrail vs CloudWatch | CloudTrail = quem fez qual chamada de API (auditoria); CloudWatch = métricas, logs e alarmes de desempenho |
| CloudTrail vs Config | CloudTrail = ações executadas; Config = estado e histórico de configuração dos recursos e conformidade |
| Shield vs WAF | Shield = DDoS (camadas 3 e 4; Advanced também 7); WAF = filtragem de requisições web (SQL injection, XSS) |
| WAF vs Firewall Manager | WAF = regras numa aplicação; Firewall Manager = gerencia regras em todas as contas |
| GuardDuty vs Inspector | GuardDuty = ameaças em andamento a partir de logs; Inspector = vulnerabilidades nos recursos |
| GuardDuty vs Detective | GuardDuty detecta; Detective investiga a causa raiz |
| Macie vs Inspector | Macie = dados sensíveis no S3; Inspector = falhas de software em EC2, ECR e Lambda |
| Trusted Advisor vs Security Hub | Trusted Advisor = boas práticas de custo, segurança, performance e cotas; Security Hub = achados de segurança centralizados |
| Artifact vs Audit Manager | Artifact = relatórios de compliance da AWS; Audit Manager = evidências da sua conta para a sua auditoria |
| KMS vs CloudHSM | KMS = chaves gerenciadas em HSM compartilhado; CloudHSM = HSM dedicado controlado pelo cliente |
| Secrets Manager vs Parameter Store | Secrets Manager = segredos com rotação automática (pago); Parameter Store = configurações e segredos simples (tem camada grátis) |
| IAM Identity Center vs Cognito | Identity Center = funcionários acessando contas AWS (SSO); Cognito = usuários finais de um aplicativo |
| User vs Role | User = credencial de longo prazo; Role = credencial temporária assumida por quem precisa |
| Organizations vs Control Tower | Organizations = gerencia contas, SCPs e fatura; Control Tower = monta landing zone padronizada sobre o Organizations |
| Security group vs NACL | SG = instância, stateful, só permite; NACL = subnet, stateless, permite e nega |
| NAT Gateway vs Internet Gateway | IGW = entrada e saída da internet para subnet pública; NAT = só saída para subnet privada |
| VPC Peering vs Transit Gateway | Peering = liga duas VPCs, não transitivo; Transit Gateway = hub para muitas VPCs e on-premises |
| VPN vs Direct Connect | VPN = criptografada pela internet, rápida de montar; Direct Connect = link físico dedicado, estável, demora semanas |
| CloudFront vs Global Accelerator | CloudFront faz cache de conteúdo; Global Accelerator não faz cache e dá IPs estáticos |
| Route 53 vs CloudFront | Route 53 = DNS (para onde ir); CloudFront = entrega e cache do conteúdo |
| SQS vs SNS | SQS = fila, consumidor puxa; SNS = pub/sub, empurra para vários |
| SNS vs EventBridge | SNS = notificações simples; EventBridge = roteamento de eventos com regras, inclusive de SaaS |
| SNS vs SES | SNS = notificações (e-mail simples, SMS, push); SES = e-mails formatados em volume |
| EventBridge vs Step Functions | EventBridge = reage e roteia eventos; Step Functions = orquestra um fluxo de várias etapas |
| EBS vs EFS vs S3 | EBS = disco de uma instância; EFS = arquivos compartilhados por várias; S3 = objetos via API |
| EBS vs instance store | EBS = persistente; instance store = temporário, some ao parar |
| EFS vs FSx | EFS = arquivos Linux (NFS); FSx = Windows (SMB), Lustre, ONTAP, OpenZFS |
| Snow vs DataSync | Snow = transferência offline em dispositivo físico; DataSync = transferência online pela rede |
| RDS Multi-AZ vs Read Replica | Multi-AZ = disponibilidade (failover); Read Replica = performance de leitura |
| RDS vs Aurora | Aurora = relacional da AWS, mais rápido, 6 cópias em 3 AZs; RDS = vários motores comerciais e open source |
| RDS vs DynamoDB | RDS = relacional (SQL, joins); DynamoDB = NoSQL chave-valor, escala massiva |
| Redshift vs RDS | Redshift = análise (OLAP); RDS = transações (OLTP) |
| Athena vs Redshift | Athena = SQL sob demanda direto no S3; Redshift = data warehouse carregado e sempre disponível |
| Kinesis vs SQS | Kinesis = streaming em tempo real, vários consumidores relendo dados; SQS = fila de mensagens para desacoplar |
| Glue vs EMR | Glue = ETL serverless; EMR = clusters Spark/Hadoop gerenciados |
| Lambda vs Fargate | Lambda = funções por evento, até 15 min; Fargate = containers sem servidor, sem limite de duração |
| ECS vs EKS | ECS = orquestrador próprio da AWS; EKS = Kubernetes |
| Elastic Beanstalk vs CloudFormation | Beanstalk = sobe a aplicação sem pensar em infra; CloudFormation = descreve qualquer infraestrutura como código |
| Elastic Beanstalk vs Lightsail | Beanstalk = PaaS que escala; Lightsail = servidor simples com preço fixo |
| WorkSpaces vs AppStream 2.0 | WorkSpaces = desktop inteiro; AppStream = só a aplicação no navegador |
| Outposts vs Local Zones vs Wavelength | Outposts = AWS no seu datacenter; Local Zones = AWS perto de cidades; Wavelength = AWS na rede 5G |
| Region vs AZ vs Edge location | Região = área geográfica; AZ = datacenter(s) isolado(s) dentro dela; edge = cache e DNS perto do usuário |
| Cost Explorer vs Budgets | Cost Explorer = analisa e prevê; Budgets = alerta e age |
| Cost Explorer vs CUR | Cost Explorer = gráficos e filtros; CUR = dados brutos mais detalhados |
| Pricing Calculator vs Cost Explorer | Calculator = antes de usar; Cost Explorer = depois, com dados reais |
| Reserved Instances vs Savings Plans | RI = tipo de instância específico; Savings Plans = compromisso de gasto por hora, mais flexível |
| Dedicated Host vs Dedicated Instance | Host = servidor físico com visibilidade de sockets e núcleos (licenças); Instance = hardware isolado sem esse controle |
| Business vs Enterprise On-Ramp vs Enterprise | Business = 24/7 e Trusted Advisor completo; On-Ramp = pool de TAMs, 30 min; Enterprise = TAM dedicado, 15 min |
| Professional Services vs Managed Services | Professional Services = consultoria para projetos; Managed Services = a AWS opera a infraestrutura |
| Application Migration Service vs DMS | MGN = migra servidores inteiros; DMS = migra bancos de dados |
| DMS vs SCT | DMS = move os dados; SCT = converte o schema entre motores diferentes |
| Rehost vs Replatform vs Refactor | Rehost = sem mudanças; Replatform = pequenos ajustes (ex.: para RDS); Refactor = reescrever cloud-native |
| Escalabilidade vs Elasticidade | Escalabilidade = conseguir crescer; Elasticidade = crescer e encolher automaticamente |
| Alta disponibilidade vs Tolerância a falhas | HA = continua acessível com pouca interrupção; tolerância a falhas = zero interrupção percebida |

### Palavras-chave que apontam para a resposta

| Se a questão diz | Pense em |
| --- | --- |
| "least operational overhead", "fully managed", "sem gerenciar servidores" | Serviço gerenciado ou serverless (Lambda, Fargate, DynamoDB, Aurora Serverless) |
| "most cost-effective" | O modelo ou a classe mais barata que ainda atende ao requisito |
| "highly available" | Várias AZs |
| "disaster recovery" em outra região | Várias regiões, backups e réplicas entre regiões |
| "decouple" | SQS (ou SNS/EventBridge) |
| "real-time streaming" | Kinesis |
| "who made the API call", "audit trail" | CloudTrail |
| "configuration history", "compliance of resources" | Config |
| "threat detection", "malicious activity" | GuardDuty |
| "vulnerabilities", "CVE" | Inspector |
| "PII in S3" | Macie |
| "compliance reports", "SOC", "PCI" | Artifact |
| "DDoS" | Shield |
| "SQL injection", "cross-site scripting" | WAF |
| "temporary credentials" | IAM role |
| "single sign-on" para funcionários | IAM Identity Center |
| "rotate secrets" | Secrets Manager |
| "dedicated technical account manager" | Enterprise Support |
| "forecast costs" | Cost Explorer |
| "alert when spending exceeds" | Budgets |
| "estimate before" | Pricing Calculator |
| "license per core/socket" | Dedicated Host |
| "can be interrupted" | Spot |
| "steady state for 1 or 3 years" | Reserved Instances ou Savings Plans |
| "petabytes, slow internet" | Família Snow |
| "on-premises with AWS services" | Outposts |
| "lowest latency for global users", "cache" | CloudFront |
| "static IP", "TCP/UDP global" | Global Accelerator |

## Fontes

- [Exam guide oficial CLF-C02](https://docs.aws.amazon.com/aws-certification/latest/examguides/cloud-practitioner-02.html)
- [Lista oficial de serviços no escopo da CLF-C02](https://docs.aws.amazon.com/fr_fr/aws-certification/latest/userguide/clf-02-in-scope-services.html)

O conteúdo dos serviços segue a documentação e os materiais oficiais da AWS. Descontos, preços dos planos de suporte, tempos de resposta e o modelo do Free Tier mudam com o tempo; confira as páginas oficiais na semana da prova. A AWS também avisa que a lista de serviços no escopo não é exaustiva.
