"""Conteúdo didático inserido pelo gerar_docs.py nos tópicos e nos índices de domínio de docs/.

Cada tópico ganha a seção "🧠 Antes de começar", logo antes do "📖 Conteúdo":
- simples:  a ideia do tópico em palavras simples;
- analogia: comparação com algo do dia a dia;
- saber:    o que você deve saber responder ao terminar (checklist);
- termos:   palavras novas explicadas sem jargão (opcional);
- dica:     como não errar a questão.

Tudo aqui só explica o que já está no conteúdo do tópico: não acrescenta fatos novos.
"""

TOPICOS = {
    # ------------------------------------------------------------------ Domínio 1
    "1.1": {
        "simples": "Computação em nuvem é **usar computadores, armazenamento e programas de outra empresa pela internet**, "
                   "na hora em que você precisa, pagando só pelo que usar — em vez de comprar e manter as máquinas.",
        "analogia": "é como a **energia elétrica**: você não constrói uma usina em casa; liga na tomada e paga a conta do que consumiu. "
                    "Os modelos de serviço são como **pizza**: fazer em casa com ingredientes alugados (IaaS), "
                    "levar a massa pronta e só escolher o recheio (PaaS) ou pedir a pizza pronta (SaaS).",
        "saber": ["Definir nuvem com as três ideias da AWS: **sob demanda**, **pela internet** e **pague pelo uso**.",
                  "Diferenciar **IaaS, PaaS e SaaS** pelo quanto você ainda gerencia.",
                  "Reconhecer os modelos de implantação **nuvem, híbrido e on-premises**."],
        "termos": [("On-premises", "no próprio datacenter da empresa (\"nas instalações\")."),
                   ("IaaS", "Infraestrutura como Serviço: você recebe a máquina e cuida do sistema operacional para cima."),
                   ("PaaS", "Plataforma como Serviço: você entrega o código, a plataforma cuida do resto."),
                   ("SaaS", "Software como Serviço: o programa já vem pronto para usar.")],
        "dica": "Pergunte-se **\"o que o cliente ainda gerencia?\"**. Sistema operacional → IaaS; só o código → PaaS; nada, só usa → SaaS. "
                "Se parte fica no datacenter e parte na AWS, é **híbrido**.",
    },
    "1.2": {
        "simples": "A AWS resume os benefícios da nuvem em **seis frases oficiais**. A prova descreve uma situação e pede "
                   "qual dessas frases ela representa.",
        "analogia": "é como trocar o **carro próprio por aplicativo de transporte**: você não paga o carro à vista (despesa variável), "
                    "a empresa compra em volume (economia de escala), chama um carro maior quando precisa (parar de adivinhar capacidade), "
                    "pede em minutos (agilidade), não cuida de oficina (sem manter datacenter) e usa o app em outras cidades (global em minutos).",
        "saber": ["Citar as **6 vantagens** com o nome oficial.",
                  "Ligar cada cenário à vantagem certa (ex.: Black Friday sem comprar servidor → parar de adivinhar capacidade).",
                  "Explicar **CapEx × OpEx** em uma frase."],
        "termos": [("CapEx", "despesa de capital: comprar equipamento antes de usar (investimento antecipado)."),
                   ("OpEx", "despesa operacional: pagar aos poucos, conforme o uso.")],
        "dica": "Procure a palavra que denuncia a vantagem: **\"investimento inicial\"** → despesa variável; **\"não sabe quanto tráfego\"** → "
                "capacidade; **\"preço menor por volume\"** → economia de escala; **\"outro continente\"** → global em minutos.",
    },
    "1.3": {
        "simples": "São as **palavras de arquitetura** que a AWS usa para descrever um bom sistema na nuvem: crescer, "
                   "aguentar falhas, voltar de desastres e manter as partes independentes.",
        "analogia": "pense num **restaurante**: contratar garçons extras no sábado e dispensá-los na segunda é **elasticidade**; "
                    "ter duas cozinhas para o caso de uma pegar fogo é **alta disponibilidade**; os pedidos ficarem num quadro "
                    "em vez de o garçom esperar o cozinheiro é **acoplamento fraco**.",
        "saber": ["Diferenciar **escalabilidade** (crescer) de **elasticidade** (crescer **e encolher** sozinho).",
                  "Diferenciar escala **vertical** (máquina maior) de **horizontal** (mais máquinas).",
                  "Ordenar as estratégias de **DR** da mais barata para a mais rápida e explicar **RTO** e **RPO**.",
                  "Explicar por que filas e eventos (**acoplamento fraco**) evitam que uma falha derrube tudo."],
        "termos": [("Alta disponibilidade", "o sistema continua acessível mesmo com falhas (em geral, usando várias AZs)."),
                   ("Tolerância a falhas", "continuar funcionando sem que o usuário perceba a falha."),
                   ("RTO", "quanto tempo você aceita ficar fora do ar depois de um desastre."),
                   ("RPO", "quantos dados (em tempo) você aceita perder.")],
        "dica": "\"Encolher sozinho\" → **elasticidade**. \"Mais barato\" em DR → **Backup and Restore**; \"menor tempo\" → **Multi-site**. "
                "\"Falha de um componente não afetar os outros\" → **acoplamento fraco** (SQS, SNS, EventBridge).",
    },
    "1.4": {
        "simples": "O Well-Architected é o **manual de boas práticas da AWS**, dividido em **seis pilares**. A prova descreve "
                   "uma prática e pergunta a qual pilar ela pertence.",
        "analogia": "é como a **inspeção de uma casa** em seis itens: a casa é fácil de manter (Excelência Operacional), tem tranca "
                    "(Segurança), não cai (Confiabilidade), tem o tamanho certo (Eficiência de Performance), não desperdiça dinheiro "
                    "(Otimização de Custos) e gasta pouca energia (Sustentabilidade).",
        "saber": ["Citar os **6 pilares**.",
                  "Ligar cada prática ao pilar (várias AZs → Confiabilidade; MFA → Segurança; desligar ocioso → Custos).",
                  "Saber que a **Well-Architected Tool** é gratuita e revisa uma carga contra os pilares."],
        "termos": [("Pilar", "uma das seis áreas de boas práticas do framework."),
                   ("Lens", "extensão do framework para um cenário específico (serverless, SaaS, ML…).")],
        "dica": "Associe palavras: **automação/runbooks** → Excelência Operacional; **identidade/criptografia** → Segurança; "
                "**recuperar de falhas/várias AZs** → Confiabilidade; **tipo de instância certo/serverless** → Performance; "
                "**gasto** → Custos; **energia/Graviton** → Sustentabilidade.",
    },
    "1.5": {
        "simples": "O CAF é o **guia da AWS para a empresa inteira se preparar** para a nuvem — não só a TI, mas também "
                   "negócio, pessoas e governança. Ele divide o trabalho em **6 perspectivas** e **4 fases**.",
        "analogia": "é como **mudar a família inteira para outro país**: alguém cuida do dinheiro e do objetivo (Business), "
                    "alguém prepara as pessoas e o idioma (People), alguém controla orçamento e riscos (Governance), "
                    "e os outros cuidam da casa nova (Platform), da segurança (Security) e do dia a dia (Operations).",
        "saber": ["Citar as **6 perspectivas** e separar as de **negócio** (Business, People, Governance) das **técnicas** (Platform, Security, Operations).",
                  "Citar as **4 fases**: Envision, Align, Launch e Scale.",
                  "Reconhecer os **benefícios** declarados (menos risco, melhor ESG, mais receita, mais eficiência)."],
        "termos": [("Perspectiva", "um grupo de capacidades com um público responsável (ex.: People → RH e liderança)."),
                   ("ESG", "ambiental, social e governança.")],
        "dica": "Leia **quem** está envolvido no enunciado: RH, cultura ou treinamento → **People**; orçamento e risco → **Governance**; "
                "arquitetura → **Platform**; monitoramento e incidentes → **Operations**.",
    },
    "1.6": {
        "simples": "Antes de migrar, cada aplicação recebe uma **estratégia**: desligar, manter, mover como está, ajustar um pouco, "
                   "trocar por outro produto ou reescrever. São os **7 Rs**.",
        "analogia": "é como **mudar de casa** e decidir o destino de cada móvel: jogar fora (Retire), deixar na casa antiga (Retain), "
                    "levar como está (Rehost), levar o cômodo inteiro de uma vez (Relocate), levar e trocar o estofado (Replatform), "
                    "comprar um novo (Repurchase) ou mandar fazer um sob medida (Refactor).",
        "saber": ["Citar os **7 Rs** e um exemplo de cada.",
                  "Diferenciar **Rehost** (sem mudanças) de **Replatform** (pequena mudança, ex.: banco para RDS).",
                  "Saber que **Rehost** é o mais rápido e **Refactor** traz mais benefício de longo prazo."],
        "termos": [("Lift-and-shift", "\"levantar e mover\": migrar sem alterar nada (Rehost)."),
                   ("Cloud-native", "feito para aproveitar a nuvem (serverless, microsserviços).")],
        "dica": "Procure o **quanto muda**: nada → Rehost; um pouco → Replatform; tudo → Refactor; troca por SaaS → Repurchase; "
                "\"ninguém usa\" → Retire; \"ainda não pode sair\" → Retain.",
    },
    "1.7": {
        "simples": "Economia da nuvem é **comparar o custo total** de manter um datacenter com o de usar a nuvem — e conhecer "
                   "as práticas que reduzem a conta (licenças, tamanho certo, serviços gerenciados, automação).",
        "analogia": "é como comparar **ter carro próprio** (compra, seguro, IPVA, garagem, manutenção) com **usar aplicativo**: "
                    "o preço da corrida parece maior, mas o custo total costuma ser menor quando você soma tudo (isso é o **TCO**).",
        "saber": ["Diferenciar custos **fixos e antecipados** (on-premises) de **variáveis** (nuvem).",
                  "Explicar **TCO** e citar as ferramentas Migration Evaluator e Pricing Calculator.",
                  "Explicar **BYOL** e **rightsizing**."],
        "termos": [("TCO", "custo total de propriedade: soma de todos os custos, inclusive pessoal e operação."),
                   ("BYOL", "trazer a sua própria licença de software."),
                   ("Rightsizing", "ajustar o tipo e o tamanho do recurso ao uso real.")],
        "dica": "\"Caso de negócio da migração\" → **Migration Evaluator**; \"reduzir custo de licença\" → **BYOL com Dedicated Hosts**; "
                "\"recurso grande demais\" → **rightsizing**; \"custo que some ao migrar\" → energia, refrigeração e espaço do datacenter.",
    },
    # ------------------------------------------------------------------ Domínio 2
    "2.1": {
        "simples": "A segurança é dividida: a **AWS protege a nuvem em si** (prédios, hardware, rede) e **o cliente protege o que "
                   "coloca nela** (dados, acessos, configurações). A fronteira muda conforme o serviço.",
        "analogia": "é como **morar de aluguel num prédio**: o condomínio cuida da portaria, da estrutura e dos elevadores (AWS); "
                    "você tranca a porta do seu apartamento e decide quem recebe a chave (cliente). "
                    "Num **hotel** (serviço gerenciado), o hotel faz ainda mais por você.",
        "saber": ["Separar **segurança DA nuvem** (AWS) de **segurança NA nuvem** (cliente).",
                  "Dizer quem aplica patch no SO do **EC2** (cliente) e no motor do **RDS** (AWS).",
                  "Explicar controles **herdados**, **compartilhados** e **específicos do cliente**."],
        "termos": [("Patch", "atualização de correção de software."),
                   ("Hipervisor", "a camada que divide um servidor físico em várias máquinas virtuais (responsabilidade da AWS).")],
        "dica": "Pergunte: **\"isso é físico ou é configuração/dado?\"**. Físico, hardware, datacenter → AWS. Dados, IAM, security group, "
                "criptografia ativada → cliente. Quanto **mais gerenciado** o serviço, **menos** o cliente faz.",
    },
    "2.2": {
        "simples": "O usuário root é o **dono da conta**, criado com o e-mail de cadastro. Ele pode tudo e não pode ser limitado "
                   "por IAM — por isso deve ser protegido e usado só nas poucas tarefas que exigem ele.",
        "analogia": "é a **chave-mestra do prédio**: abre todas as portas, então fica guardada no cofre (com MFA) e só sai para "
                    "situações especiais. No dia a dia, cada um usa o próprio crachá (identidades IAM).",
        "saber": ["Citar as **boas práticas** do root (MFA, sem access keys, não usar no dia a dia).",
                  "Reconhecer as **tarefas exclusivas do root** (ex.: alterar e-mail/senha do root, fechar a conta standalone, MFA Delete no S3).",
                  "Saber o que **não** exige root (criar usuários IAM, ver a fatura, e agora mudar o plano de suporte e o nome da conta)."],
        "termos": [("MFA", "autenticação multifator: senha + um segundo fator (app, chave física)."),
                   ("Access key", "credencial para usar a AWS por linha de comando ou programa.")],
        "dica": "Na lista de alternativas, procure a tarefa que **só o dono da conta** poderia fazer. Tarefas comuns de administração "
                "(criar usuário, ver fatura) **não** exigem root.",
    },
    "2.3": {
        "simples": "O IAM decide **quem entra** (autenticação) e **o que cada um pode fazer** (autorização) na conta AWS, usando "
                   "usuários, grupos, roles e políticas em JSON.",
        "analogia": "é o **sistema de crachás de uma empresa**: o usuário é a pessoa com crachá; o grupo é o departamento; "
                    "a role é um **crachá de visitante** temporário que alguém pega emprestado; a política é a lista de salas que o crachá abre.",
        "saber": ["Diferenciar **usuário, grupo, role e política**.",
                  "Aplicar a regra de avaliação: tudo começa **negado**, um **Allow** libera e um **Deny explícito sempre vence**.",
                  "Explicar o **menor privilégio** e por que usar **roles** em vez de access keys no EC2.",
                  "Diferenciar **IAM Identity Center** (funcionários, várias contas) de **Cognito** (clientes de um app)."],
        "termos": [("Autenticação", "provar quem você é (login)."),
                   ("Autorização", "o que você tem permissão de fazer."),
                   ("Role", "identidade com credenciais temporárias, assumida por quem precisa."),
                   ("Federação", "entrar com uma identidade de fora (AD, Google, Okta) sem criar usuário IAM.")],
        "dica": "\"Aplicação no EC2 precisa acessar o S3\" → **role**, nunca access key. \"Login único em várias contas\" → **Identity Center**. "
                "\"Usuários do aplicativo\" → **Cognito**. \"Rotação automática de senhas\" → **Secrets Manager**.",
    },
    "2.4": {
        "simples": "Empresas grandes usam **várias contas AWS** (produção, testes, segurança). Este tópico mostra como "
                   "**organizar, limitar e cobrar** todas elas de forma central.",
        "analogia": "é como uma **rede de franquias**: a matriz (Organizations) agrupa as lojas, define o que nenhuma pode fazer (SCP), "
                    "paga uma fatura única e, com o Control Tower, entrega cada loja nova já montada no padrão.",
        "saber": ["Explicar **Organizations**, **OUs** e **consolidated billing**.",
                  "Saber que **SCP só restringe** (não concede permissão) e não afeta a conta de gerenciamento.",
                  "Diferenciar **Organizations** (agrupar e limitar) de **Control Tower** (ambiente multi-conta pronto, com guardrails)."],
        "termos": [("OU", "unidade organizacional: uma \"pasta\" de contas dentro do Organizations."),
                   ("SCP", "política que define o máximo que uma conta ou OU pode fazer."),
                   ("Landing zone", "ambiente multi-conta já configurado com boas práticas."),
                   ("Guardrail", "regra de proteção do Control Tower (preventiva ou detectiva).")],
        "dica": "\"Limitar o que uma **conta inteira** pode fazer\" → **SCP**. \"Montar rapidamente ambiente multi-conta com boas práticas\" → "
                "**Control Tower**. \"Uma fatura e desconto por volume\" → **consolidated billing**.",
    },
    "2.5": {
        "simples": "Criptografar é **embaralhar os dados** para que só quem tem a chave consiga ler. Este tópico mostra quando "
                   "criptografar (guardado ou trafegando) e qual serviço cuida das chaves e dos certificados.",
        "analogia": "a criptografia é um **cadeado**; a chave é o que abre. O **KMS** é um chaveiro gerenciado pela AWS; o **CloudHSM** é "
                    "um **cofre só seu**; o **ACM** fornece o cadeado do HTTPS (o ícone de cadeado no navegador).",
        "saber": ["Diferenciar criptografia **em repouso** de **em trânsito**.",
                  "Diferenciar **KMS** (chaves gerenciadas e integradas) de **CloudHSM** (hardware dedicado, só você controla).",
                  "Saber que o **ACM** emite e renova certificados SSL/TLS e que o S3 criptografa objetos novos por padrão."],
        "termos": [("Em repouso", "dados guardados em disco, banco ou bucket."),
                   ("Em trânsito", "dados viajando pela rede."),
                   ("HSM", "equipamento físico feito para guardar chaves com segurança."),
                   ("TLS/SSL", "o protocolo que protege o HTTPS.")],
        "dica": "\"Hardware **dedicado**\" ou \"controle **exclusivo** das chaves\" → **CloudHSM**. \"Chaves integradas aos serviços\" → **KMS**. "
                "\"Certificado HTTPS\" → **ACM**. Quem **ativa** a criptografia dos dados é o **cliente**.",
    },
    "2.6": {
        "simples": "Compliance é **provar que se segue as regras** (leis e normas). A AWS fornece os relatórios dela; o cliente "
                   "cuida da conformidade do que ele mesmo constrói.",
        "analogia": "o **Artifact** é a **pasta de certificados da AWS** que você entrega ao auditor; o **Audit Manager** é um "
                    "**assistente que junta as provas da sua própria empresa** para a sua auditoria.",
        "saber": ["Diferenciar **Artifact** (relatórios da AWS) de **Audit Manager** (evidências da sua conta).",
                  "Saber que compliance também é **responsabilidade compartilhada**.",
                  "Saber que os dados ficam na **região escolhida** (residência de dados)."],
        "termos": [("Compliance", "estar em conformidade com leis, normas e regulações."),
                   ("SOC, PCI DSS, ISO 27001", "relatórios e certificações de segurança reconhecidos no mercado."),
                   ("BAA", "acordo exigido para dados de saúde (HIPAA), aceito pelo Artifact.")],
        "dica": "\"Auditor pede o relatório **da AWS**\" → **Artifact**. \"Coletar evidências **da empresa**\" → **Audit Manager**. "
                "\"Avaliar se os recursos seguem regras\" → **AWS Config**.",
    },
    "2.7": {
        "simples": "Três serviços respondem três perguntas diferentes: **quem fez?** (CloudTrail), **como estava configurado?** "
                   "(Config) e **como está o desempenho agora?** (CloudWatch).",
        "analogia": "o **CloudTrail** é a **câmera de segurança** (grava quem fez cada ação); o **Config** é o **álbum de fotos** da "
                    "configuração ao longo do tempo; o **CloudWatch** é o **painel do carro**, com indicadores e luzes de alerta.",
        "saber": ["Ligar cada pergunta ao serviço: quem fez → CloudTrail; configuração e conformidade → Config; métricas e alarmes → CloudWatch.",
                  "Lembrar que o CloudTrail guarda **90 dias** por padrão e que, para mais tempo, se cria um **trail** para o S3.",
                  "Lembrar que **memória e disco** do EC2 exigem o **CloudWatch agent**."],
        "termos": [("Chamada de API", "qualquer ação feita na AWS (pelo console, CLI ou programa)."),
                   ("Métrica", "um número medido ao longo do tempo (ex.: uso de CPU)."),
                   ("Alarme", "aviso disparado quando uma métrica passa de um limite.")],
        "dica": "Leia o **verbo** da pergunta: \"quem **apagou**\" → CloudTrail; \"como **estava**\" → Config; \"**alertar** quando a CPU passar\" → "
                "CloudWatch. \"Verificar **continuamente** se segue a regra\" → Config rules.",
    },
    "2.8": {
        "simples": "São as **barreiras** que protegem a rede e as aplicações: firewalls na instância e na subnet, proteção contra "
                   "ataques de negação de serviço (DDoS) e contra ataques à aplicação web.",
        "analogia": "o **security group** é o **porteiro do apartamento** (lembra quem entrou e deixa sair); a **NACL** é o **portão da "
                    "rua** (confere entrada e saída e pode barrar alguém pelo nome); o **Shield** é um **quebra-mar** contra enxurradas de "
                    "tráfego; o **WAF** é o **segurança que lê cada pedido** e barra os maliciosos.",
        "saber": ["Diferenciar **security group** (instância, stateful, só permite) de **NACL** (subnet, stateless, permite e nega).",
                  "Diferenciar **Shield Standard** (grátis) de **Shield Advanced** (pago, com time 24/7 e proteção de custo).",
                  "Saber que o **WAF** bloqueia SQL injection e XSS (camada 7) e que o **Firewall Manager** aplica regras em todas as contas."],
        "termos": [("Stateful", "lembra da conexão: se entrou, a resposta sai sem nova regra."),
                   ("Stateless", "não lembra: é preciso liberar entrada **e** saída."),
                   ("DDoS", "ataque que tenta derrubar o serviço com uma enxurrada de tráfego."),
                   ("SQL injection / XSS", "ataques que escondem comandos maliciosos em requisições web.")],
        "dica": "\"**Bloquear** um IP\" → **NACL** (security group não tem regra de negar). \"SQL injection\" → **WAF**. \"DDoS\" → **Shield**; "
                "com \"time especialista\" ou \"proteção de custo\" → **Shield Advanced**.",
    },
    "2.9": {
        "simples": "São os serviços que **encontram problemas de segurança**: ameaças em andamento, vulnerabilidades, dados "
                   "sensíveis expostos — e os que investigam e centralizam esses alertas.",
        "analogia": "é uma **equipe de segurança**: o **GuardDuty** é o alarme que dispara; o **Inspector** é o vistoriador que procura "
                    "brechas; o **Macie** procura documentos sensíveis largados; o **Detective** investiga depois do alarme; o "
                    "**Security Hub** é a sala de monitoramento que junta tudo; o **Trusted Advisor** é o consultor de boas práticas.",
        "saber": ["Ligar cada serviço à sua função: ameaça → GuardDuty; vulnerabilidade → Inspector; dado sensível no S3 → Macie.",
                  "Lembrar a sequência **detectar (GuardDuty) → investigar (Detective) → centralizar (Security Hub)**.",
                  "Saber o que o **Trusted Advisor** verifica e o que muda conforme o plano de suporte."],
        "termos": [("CVE", "identificador público de uma vulnerabilidade conhecida."),
                   ("PII", "dados pessoais que identificam alguém (CPF, cartão, nome)."),
                   ("Achado (finding)", "um alerta de segurança gerado por um serviço.")],
        "dica": "Procure o **substantivo**: \"ameaça/atividade maliciosa\" → GuardDuty; \"vulnerabilidade/CVE\" → Inspector; \"dados pessoais\" → Macie; "
                "\"causa raiz\" → Detective; \"painel central\" → Security Hub; \"boas práticas e custo\" → Trusted Advisor.",
    },
    "2.10": {
        "simples": "Pontos soltos de segurança: o que pode ser testado sem pedir autorização, **a quem denunciar abuso** vindo "
                   "da AWS e **onde buscar informação** de segurança.",
        "analogia": "o **Trust & Safety** é a **ouvidoria** da AWS para denúncias: se alguém usa a AWS para te atacar (spam, phishing), "
                    "é para lá que você reclama — não para o suporte técnico.",
        "saber": ["Saber que **pentest** é permitido sem aprovação prévia numa lista de serviços, mas DDoS simulado não.",
                  "Saber que abuso vindo de IPs da AWS vai para o **AWS Trust & Safety**.",
                  "Citar fontes de informação de segurança (Security Center, Security Blog, Bulletins, re:Post, Knowledge Center)."],
        "termos": [("Pentest", "teste de intrusão: atacar o próprio sistema, de propósito, para achar falhas."),
                   ("Phishing", "golpe que imita uma empresa para roubar dados.")],
        "dica": "\"Recebi spam/phishing **vindo de um IP da AWS**\" → **Trust & Safety**. \"Ferramenta de segurança de terceiros\" → **Marketplace**.",
    },
    # ------------------------------------------------------------------ Domínio 3
    "3.1": {
        "simples": "Há várias **portas de entrada** para usar a AWS — clicando, digitando comandos, programando ou descrevendo a "
                   "infraestrutura num arquivo. Todas usam as mesmas APIs por baixo.",
        "analogia": "é como falar com um **banco**: pelo **site** (Console), pelo **atendimento por comandos** (CLI), por um **aplicativo "
                    "seu integrado ao banco** (SDK) ou deixando **instruções programadas** que se repetem sozinhas (CloudFormation).",
        "saber": ["Diferenciar **Console, CLI, SDK e CloudShell**.",
                  "Saber que tarefa **pontual** pode ser no Console e tarefa **repetível** deve ser automatizada.",
                  "Explicar **infraestrutura como código** (CloudFormation)."],
        "termos": [("API", "a forma padronizada de um programa pedir algo a outro."),
                   ("IaC", "infraestrutura como código: descrever servidores e redes num arquivo e criar tudo automaticamente.")],
        "dica": "\"Repetível em várias regiões/contas\" → **CloudFormation**. \"Comandos rápidos sem instalar nada\" → **CloudShell**. "
                "\"Dentro do código da aplicação\" → **SDK**.",
    },
    "3.2": {
        "simples": "A AWS está espalhada pelo mundo em **regiões**; cada região tem várias **zonas de disponibilidade (AZs)**; "
                   "e há centenas de **edge locations** perto dos usuários. Existem ainda formas de levar a AWS para mais perto.",
        "analogia": "a **região** é uma **cidade**; cada **AZ** é um **bairro** com a própria energia e rede, longe o bastante para um "
                    "incêndio não atingir os outros; as **edge locations** são **lojinhas de conveniência** espalhadas que guardam cópias "
                    "do que mais se pede.",
        "saber": ["Diferenciar **região, AZ e edge location**.",
                  "Citar os **4 fatores** para escolher região (compliance, proximidade, serviços disponíveis, preço).",
                  "Saber quando usar **várias AZs** (falha de datacenter) × **várias regiões** (desastre regional, usuários globais).",
                  "Diferenciar **Outposts, Local Zones e Wavelength**."],
        "termos": [("AZ", "um ou mais datacenters isolados dentro de uma região."),
                   ("Edge location", "ponto de presença usado por CloudFront, Route 53 e outros serviços para ficar perto do usuário."),
                   ("Latência", "o tempo que a informação leva para ir e voltar.")],
        "dica": "\"Falha de **um datacenter**\" → **várias AZs**. \"Lei exige dados no país\" → escolher a **região**. \"Usuários no mundo todo\" → "
                "**CloudFront/edge**. \"AWS dentro do **meu** datacenter\" → **Outposts**.",
    },
    "3.3": {
        "simples": "O EC2 é o **servidor virtual** da AWS: você escolhe o tamanho, o sistema operacional e o disco, e controla "
                   "tudo dentro dele.",
        "analogia": "é como **alugar um computador**: a **AMI** é o \"molde\" com o sistema já instalado; a **família de instância** é o "
                    "modelo do computador (para jogos, para planilhas pesadas, para muita memória); o **EBS** é o HD que fica guardado "
                    "mesmo com o computador desligado.",
        "saber": ["Explicar **AMI**, **user data** e **key pair**.",
                  "Escolher a **família** pelo uso (ML → computação acelerada; banco em memória → otimizada para memória).",
                  "Diferenciar **EBS** (persistente) de **instance store** (temporário).",
                  "Diferenciar **parar**, **encerrar** e **hibernar**."],
        "termos": [("Instância", "um servidor virtual em execução."),
                   ("AMI", "imagem pronta (sistema + software) usada para criar a instância."),
                   ("Graviton", "processador ARM da AWS, mais barato e econômico em energia.")],
        "dica": "Leia o **uso** descrito: \"treinar ML/GPU\" → computação acelerada; \"muita memória\" → otimizada para memória; "
                "\"dado temporário que pode ser perdido\" → **instance store**; \"acesso sem SSH\" → **Session Manager**.",
    },
    "3.4": {
        "simples": "Dois serviços trabalham juntos: o **Auto Scaling** muda a **quantidade** de servidores conforme a demanda, e o "
                   "**Load Balancer** **distribui** os usuários entre eles.",
        "analogia": "num **supermercado**, o **Auto Scaling** é o gerente que abre ou fecha caixas conforme a fila; o **Load Balancer** é "
                    "o funcionário que aponta \"o caixa 3 está livre\" e nunca manda ninguém para o caixa fechado.",
        "saber": ["Explicar **mínimo, desejado e máximo** de um Auto Scaling Group e os tipos de política.",
                  "Diferenciar **ALB** (camada 7, HTTP, por caminho), **NLB** (camada 4, TCP/UDP, altíssima performance) e **GWLB** (appliances de rede).",
                  "Saber que o Auto Scaling **não tem custo** próprio (paga-se as instâncias)."],
        "termos": [("Health check", "verificação periódica de que o servidor está respondendo."),
                   ("Camada 7 / camada 4", "nível da comunicação: 7 entende HTTP (caminhos, cabeçalhos); 4 só vê conexões TCP/UDP."),
                   ("Launch template", "o molde usado para criar as instâncias do grupo.")],
        "dica": "\"Aumentar/diminuir instâncias\" → **Auto Scaling**. \"Distribuir tráfego\" → **ELB**. \"/api para um serviço, /imagens para outro\" → "
                "**ALB**. \"TCP, latência ultrabaixa, IP fixo\" → **NLB**. \"Firewall de terceiros\" → **GWLB**.",
    },
    "3.5": {
        "simples": "Contêineres empacotam a aplicação com tudo que ela precisa; **serverless** é rodar código sem gerenciar "
                   "servidores. Este tópico mostra quem orquestra contêineres e quando usar o Lambda.",
        "analogia": "um **contêiner** é como uma **marmita pronta**: leva a comida e os talheres e funciona em qualquer micro-ondas. "
                    "O **ECS/EKS** é o **gerente da cozinha** que distribui as marmitas; o **Fargate** é **não ter cozinha** (alguém esquenta para "
                    "você); o **Lambda** é um **garçom que só aparece quando chamado** e cobra por minuto de atendimento.",
        "saber": ["Diferenciar **ECS** (nativo da AWS) de **EKS** (Kubernetes).",
                  "Saber que o **Fargate** roda contêineres **sem servidores** e o **ECR** guarda as imagens.",
                  "Lembrar que a **função Lambda convencional** roda por **até 15 minutos por invocação**, é disparado por eventos e cobra por requisição e duração."],
        "termos": [("Contêiner", "pacote leve com a aplicação e suas dependências, que roda igual em qualquer lugar."),
                   ("Orquestrador", "sistema que decide onde e quantos contêineres rodam."),
                   ("Serverless", "você não gerencia servidores e paga só pelo uso.")],
        "dica": "\"Processar quando o arquivo chega ao S3\" → **Lambda**. \"Roda por **2 horas**\" → **não** é Lambda (Fargate, Batch ou EC2). "
                "\"Já usa **Kubernetes**\" → **EKS**. \"Contêineres sem gerenciar servidores\" → **Fargate**.",
    },
    "3.6": {
        "simples": "Três jeitos mais simples de rodar aplicações: **enviar só o código** (Elastic Beanstalk), **servidor de preço "
                   "fixo** (Lightsail) e **processar jobs em lote** (Batch).",
        "analogia": "o **Elastic Beanstalk** é um **buffet** (você leva a receita e eles montam tudo); o **Lightsail** é um **plano "
                    "pré-pago** de servidor; o **Batch** é uma **linha de produção** que processa milhares de pedidos.",
        "saber": ["Saber que o **Elastic Beanstalk** é PaaS e não tem custo adicional (paga os recursos criados).",
                  "Saber que o **Lightsail** tem **preço mensal fixo** e é para quem está começando.",
                  "Saber que o **Batch** escolhe a computação ideal para jobs em lote."],
        "termos": [("PaaS", "plataforma onde você entrega o código e ela cuida da infraestrutura."),
                   ("Job em lote (batch)", "trabalho processado sem interação, em grande quantidade.")],
        "dica": "\"Desenvolvedor sem pensar em infraestrutura\" → **Elastic Beanstalk**. \"Preço fixo, simples\" → **Lightsail**. "
                "\"Milhares de jobs\" → **Batch**.",
    },
    "3.7": {
        "simples": "Cada tipo de dado tem o seu banco: **relacional** (tabelas e SQL), **NoSQL** (chave-valor), **cache** (memória), "
                   "**grafos** (relacionamentos), **documentos** e **data warehouse** (análise). A prova pede o banco certo para o cenário.",
        "analogia": "o **RDS** é uma **planilha organizada com zelador**; o **DynamoDB** é um **fichário gigante** que acha qualquer ficha "
                    "pela etiqueta na hora; o **ElastiCache** é um **post-it** com as respostas mais pedidas; o **Neptune** é um **mapa de "
                    "quem conhece quem**; o **Redshift** é o **arquivo histórico** usado para relatórios.",
        "saber": ["Diferenciar **banco no EC2** (você cuida de tudo) de **banco gerenciado** (a AWS cuida).",
                  "Diferenciar **Multi-AZ** (disponibilidade) de **Read Replica** (performance de leitura).",
                  "Escolher o banco pelo tipo de dado (use a tabela \"tipo de dado → serviço\" do conteúdo).",
                  "Diferenciar **OLTP** (RDS/Aurora) de **OLAP** (Redshift)."],
        "termos": [("Relacional", "dados em tabelas ligadas entre si, consultadas com SQL."),
                   ("NoSQL", "bancos que não usam o modelo de tabelas relacionais (chave-valor, documentos, grafos)."),
                   ("OLTP", "muitas transações pequenas do dia a dia (vendas, cadastros)."),
                   ("OLAP", "análises grandes sobre o histórico (relatórios, BI).")],
        "dica": "\"Multi-AZ\" → **disponibilidade**; \"Read Replica\" → **leitura**. \"Milhões de acessos, chave-valor, serverless\" → **DynamoDB**. "
                "\"BI/data warehouse\" → **Redshift**. \"Amigos de amigos\" → **Neptune**. \"MongoDB\" → **DocumentDB**.",
    },
    "3.8": {
        "simples": "O S3 guarda **arquivos (objetos)** em **buckets**, com durabilidade altíssima. O preço depende da **classe de "
                   "armazenamento**, escolhida pela frequência de acesso.",
        "analogia": "o S3 é um **guarda-volumes infinito**; as classes são como **organizar a casa**: o que usa todo dia fica na mesa "
                    "(Standard), o que usa pouco vai para o armário (IA) e o que quase nunca usa vai para o depósito (Glacier) — mais "
                    "barato de guardar, mais caro e demorado de buscar.",
        "saber": ["Explicar **bucket**, **objeto** e a durabilidade de **11 noves**.",
                  "Escolher a **classe** pelo padrão de acesso (frequente, imprevisível, raro, arquivo de longo prazo).",
                  "Explicar **versionamento**, **lifecycle**, **replicação** e **Object Lock**."],
        "termos": [("Objeto", "o arquivo mais os seus metadados."),
                   ("Bucket", "o \"recipiente\" onde os objetos ficam; nome único no mundo."),
                   ("Durabilidade", "a chance de o dado **não se perder**."),
                   ("Disponibilidade", "a chance de o dado **estar acessível** quando você pede.")],
        "dica": "\"Acesso imprevisível\" → **Intelligent-Tiering**. \"Guardar 7 anos, quase nunca lido\" → **Glacier Deep Archive**. "
                "\"Pode ser recriado\" → **One Zone-IA**. \"Raro, mas abrir na hora\" → **Glacier Instant Retrieval**.",
    },
    "3.9": {
        "simples": "Além do S3, há armazenamento em **bloco** (disco de uma máquina), de **arquivos** (pasta compartilhada), "
                   "**híbrido** (datacenter usando a nuvem), **backup centralizado** e **transferência** de grandes volumes.",
        "analogia": "o **EBS** é o **HD do computador**; o **EFS** é a **pasta de rede** que todos abrem ao mesmo tempo; o **Storage "
                    "Gateway** é a **ponte** entre o escritório e a nuvem; a **família Snow** é um **HD blindado enviado pelo correio**.",
        "saber": ["Diferenciar **objeto (S3)**, **bloco (EBS)** e **arquivo (EFS/FSx)**.",
                  "Diferenciar **EFS** (Linux, NFS) de **FSx for Windows** (SMB, Active Directory).",
                  "Saber os tipos de **Storage Gateway** (Tape Gateway substitui fitas).",
                  "Saber quando usar **Snow** (rede lenta, volumes enormes) e **AWS Backup** (backup central)."],
        "termos": [("Bloco", "armazenamento tipo disco, ligado a uma máquina."),
                   ("NFS / SMB", "protocolos de compartilhamento de arquivos (Linux / Windows)."),
                   ("Snapshot", "cópia de um volume num ponto no tempo.")],
        "dica": "\"Várias instâncias **Linux** lendo os mesmos arquivos\" → **EFS**. \"**Windows** com AD\" → **FSx for Windows**. "
                "\"Substituir fitas\" → **Tape Gateway**. \"500 TB com internet lenta\" → **Snowball Edge**.",
    },
    "3.10": {
        "simples": "A **VPC** é a sua rede privada na AWS. Este tópico mostra como dividi-la, ligá-la à internet, a outras VPCs e ao "
                   "datacenter, e como entregar conteúdo rápido no mundo todo (DNS, CDN e aceleração).",
        "analogia": "a **VPC** é um **condomínio fechado**: as **subnets** são as ruas (públicas dão para a avenida, privadas não); o "
                    "**Internet Gateway** é o portão principal; o **NAT Gateway** é uma **saída só de ida** para os moradores das ruas "
                    "privadas; a **VPN** é um túnel pela estrada pública; o **Direct Connect**, uma estrada particular; o **Route 53**, "
                    "a lista telefônica; o **CloudFront**, lojinhas espalhadas com cópias do conteúdo.",
        "saber": ["Diferenciar subnet **pública** de **privada** e explicar **Internet Gateway** × **NAT Gateway**.",
                  "Diferenciar **VPC Peering** (não transitivo) de **Transit Gateway** (hub central) e saber o que são **VPC endpoints**.",
                  "Diferenciar **Site-to-Site VPN** (pela internet, rápido) de **Direct Connect** (dedicado, leva semanas).",
                  "Diferenciar **Route 53** (DNS), **CloudFront** (CDN com cache) e **Global Accelerator** (IPs fixos, sem cache)."],
        "termos": [("CIDR", "a faixa de endereços IP da rede."),
                   ("DNS", "o sistema que traduz nomes (exemplo.com) em endereços IP."),
                   ("CDN", "rede de entrega de conteúdo com cópias perto dos usuários."),
                   ("Transitivo", "se A fala com B e B com C, A fala com C — o peering **não** é.")],
        "dica": "\"Subnet privada baixar patches\" → **NAT Gateway**. \"Dezenas de VPCs\" → **Transit Gateway**. \"S3 sem internet\" → "
                "**gateway endpoint**. \"Criptografado, pronto hoje\" → **VPN**; \"dedicado, consistente\" → **Direct Connect**. "
                "\"Cache global\" → **CloudFront**; \"IPs estáticos, TCP/UDP\" → **Global Accelerator**.",
    },
    "3.11": {
        "simples": "Analytics é **transformar dados em respostas**: coletar em tempo real, preparar, consultar e mostrar em "
                   "gráficos. Cada etapa tem um serviço.",
        "analogia": "é uma **cozinha de dados**: o **Kinesis** é a esteira que traz os ingredientes em tempo real; o **Glue** lava e corta "
                    "(ETL) e etiqueta tudo (catálogo); o **Athena** prova direto da despensa (S3) com SQL; o **EMR** é a cozinha industrial "
                    "(Spark/Hadoop); o **QuickSight** monta o prato bonito (dashboards).",
        "saber": ["Ligar cada serviço à função: SQL no S3 → Athena; ETL e catálogo → Glue; tempo real → Kinesis.",
                  "Saber que o **Athena** cobra por **dados escaneados**.",
                  "Diferenciar **EMR** (big data com Spark/Hadoop), **QuickSight** (BI) e **OpenSearch** (busca e logs)."],
        "termos": [("ETL", "extrair, transformar e carregar dados."),
                   ("Streaming", "dados chegando continuamente, em tempo real."),
                   ("BI", "inteligência de negócio: relatórios e painéis para decisão.")],
        "dica": "\"SQL em arquivos no S3, sem servidor\" → **Athena**. \"Tempo real/cliques\" → **Kinesis**. \"Painéis\" → **QuickSight**. "
                "\"Spark/Hadoop\" → **EMR**. \"Busca de texto\" → **OpenSearch**.",
    },
    "3.12": {
        "simples": "A prova separa três níveis de IA: **criar o seu próprio modelo** (SageMaker AI), **usar modelos generativos "
                   "prontos** (Bedrock e Amazon Q) e **APIs prontas** para uma tarefa específica (imagem, texto, voz).",
        "analogia": "é como **comida**: o **SageMaker AI** é cozinhar do zero; o **Bedrock** é comprar uma massa pronta e montar o seu "
                    "prato; os **serviços de IA prontos** são pratos congelados — cada um resolve uma refeição específica.",
        "saber": ["Diferenciar **SageMaker AI** (modelo próprio) de **Bedrock** (modelos de fundação via API) e **Amazon Q** (assistente pronto).",
                  "Ligar cada API pronta à tarefa: imagem → Rekognition; sentimento → Comprehend; chatbot → Lex; "
                  "texto em fala → Polly; fala em texto → Transcribe; tradução → Translate; documentos → Textract."],
        "termos": [("Modelo de ML", "programa treinado com dados para prever ou classificar."),
                   ("IA generativa", "IA que cria conteúdo novo (texto, imagem, código)."),
                   ("Modelo de fundação", "modelo grande, pré-treinado, usado como base para várias tarefas.")],
        "dica": "Polly e Transcribe confundem: **P**olly **P**roduz fala (texto → voz); **Transcribe** transcreve (voz → texto). "
                "\"Treinar modelo próprio\" → **SageMaker AI**.",
    },
    "3.13": {
        "simples": "Integração é fazer **partes de um sistema conversarem sem depender umas das outras**: filas, notificações, "
                   "eventos e fluxos de várias etapas.",
        "analogia": "o **SQS** é uma **fila de pedidos** (cada um é atendido no seu ritmo); o **SNS** é um **alto-falante** (todos ouvem "
                    "ao mesmo tempo); o **EventBridge** é uma **central de regras** (\"quando acontecer X, avise Y\"); o **Step Functions** "
                    "é um **fluxograma** que se executa sozinho.",
        "saber": ["Diferenciar **SQS** (fila, o consumidor puxa) de **SNS** (pub/sub, empurra para todos).",
                  "Diferenciar fila **Standard** de **FIFO**.",
                  "Saber quando usar **EventBridge** (reagir a eventos, inclusive de SaaS) e **Step Functions** (orquestrar etapas)."],
        "termos": [("Desacoplar", "fazer componentes funcionarem sem depender um do outro estar disponível."),
                   ("Pub/sub", "publicar uma vez e todos os assinantes recebem."),
                   ("Fan-out", "uma mensagem do SNS copiada para várias filas SQS.")],
        "dica": "\"Desacoplar/absorver picos\" → **SQS**. \"Notificar vários\" → **SNS**. \"Ordem garantida\" → **SQS FIFO**. "
                "\"Evento de SaaS\" → **EventBridge**. \"Várias etapas com aprovação\" → **Step Functions**.",
    },
    "3.14": {
        "simples": "São serviços **prontos para o negócio**: central de atendimento, envio de e-mails, desktops virtuais, criação "
                   "de apps e conexão de dispositivos IoT.",
        "analogia": "é uma **caixa de ferramentas de escritório**: o **Connect** é a central telefônica; o **SES**, o correio; o "
                    "**WorkSpaces**, o computador de trabalho na nuvem; o **Amplify**, um kit para montar apps; o **IoT Core**, a central "
                    "que recebe mensagens dos sensores.",
        "saber": ["Ligar cada serviço ao cenário: call center → Connect; e-mails → SES; desktop virtual → WorkSpaces.",
                  "Diferenciar **WorkSpaces** (desktop inteiro) de **AppStream 2.0** (só o aplicativo no navegador).",
                  "Diferenciar **SES** (e-mails formatados a clientes) de **SNS** (notificações simples)."],
        "termos": [("Contact center", "central de atendimento (telefone, chat)."),
                   ("DaaS", "desktop como serviço."),
                   ("IoT", "internet das coisas: sensores e dispositivos conectados.")],
        "dica": "\"Call center\" → **Connect**. \"Funcionário remoto precisa de desktop\" → **WorkSpaces**. \"App de desktop no navegador\" → "
                "**AppStream 2.0**. \"Sensores\" → **IoT Core**.",
    },
    "3.15": {
        "simples": "Ferramentas que ajudam a **entregar software**: compilar e testar, automatizar a esteira de entrega e "
                   "encontrar onde uma aplicação está lenta.",
        "analogia": "é uma **fábrica de software**: o **CodeBuild** monta e testa cada peça; o **CodePipeline** é a **esteira** que leva "
                    "a peça de uma estação para a outra; o **X-Ray** é o **rastreador de encomendas** que mostra onde cada pedido atrasou.",
        "saber": ["Diferenciar **CodeBuild** (compila e testa) de **CodePipeline** (orquestra a esteira de CI/CD).",
                  "Saber que o **X-Ray** faz **rastreamento distribuído** entre microsserviços.",
                  "Lembrar quais ferramentas ficaram **fora do escopo** (veja o aviso no topo)."],
        "termos": [("CI/CD", "integração e entrega contínuas: automatizar o caminho do código até a produção."),
                   ("Build", "transformar o código em algo executável e testá-lo."),
                   ("Rastreamento distribuído", "seguir uma requisição por vários serviços.")],
        "dica": "\"Qual microsserviço deixa a requisição lenta\" → **X-Ray**. \"Automatizar a esteira\" → **CodePipeline**. "
                "\"Compilar e rodar testes\" → **CodeBuild**.",
    },
    "3.16": {
        "simples": "Ferramentas para **administrar o ambiente**: criar infraestrutura por código, operar muitos servidores, saber "
                   "de eventos da AWS, ver limites, controlar licenças e ajustar o tamanho dos recursos.",
        "analogia": "o **CloudFormation** é a **planta da casa**; o **Systems Manager** é o **controle remoto** de todos os servidores; o "
                    "**Health Dashboard** é o **aviso do condomínio**; o **Service Quotas** é a **lista de limites** do contrato; o "
                    "**Compute Optimizer** é uma **balança** que mostra o que está grande ou pequeno demais.",
        "saber": ["Explicar **template**, **stack**, **StackSets** e **drift detection** do CloudFormation.",
                  "Citar os recursos do **Systems Manager** (Session Manager, Run Command, Patch Manager, Parameter Store).",
                  "Diferenciar **Health Dashboard** (eventos da AWS) de **CloudWatch** (métricas dos seus recursos).",
                  "Saber para que servem **Service Quotas**, **License Manager** e **Compute Optimizer**."],
        "termos": [("Stack", "o conjunto de recursos criado a partir de um template."),
                   ("Drift", "quando alguém altera um recurso na mão, fora do template."),
                   ("Cota (quota)", "limite de uso de um serviço numa região.")],
        "dica": "\"Acessar sem SSH\" → **Session Manager**. \"Patch em 500 servidores\" → **Patch Manager**. \"Evento da AWS afeta minhas instâncias\" → "
                "**Health Dashboard**. \"Passar do limite\" → **Service Quotas**. \"Tamanho ideal\" → **Compute Optimizer**.",
    },
    "3.17": {
        "simples": "As ferramentas de migração seguem a **ordem da mudança**: avaliar o custo e as dependências, acompanhar o "
                   "progresso, migrar servidores e bancos e transferir dados.",
        "analogia": "é uma **mudança de casa**: o **Migration Evaluator** faz o orçamento; o **Discovery Service** mede os móveis e vê o "
                    "que depende do quê; o **Migration Hub** é a planilha de acompanhamento; o **MGN** é o caminhão que leva tudo como está; "
                    "o **DMS** leva o banco com a loja aberta; o **SCT** traduz a estrutura de um banco para outro.",
        "saber": ["Ligar cada ferramenta à **etapa** (avaliar, acompanhar, migrar, transferir).",
                  "Diferenciar migração de banco **homogênea** (só DMS) de **heterogênea** (SCT + DMS).",
                  "Diferenciar transferência **offline** (Snow) de **online** (DataSync, Transfer Family)."],
        "termos": [("Homogênea", "mesmo motor de banco na origem e no destino (MySQL → MySQL)."),
                   ("Heterogênea", "motores diferentes (Oracle → PostgreSQL)."),
                   ("Schema", "a estrutura do banco: tabelas, colunas e relacionamentos.")],
        "dica": "\"Dependências entre servidores\" → **Application Discovery Service**. \"Migrar VMs sem alterar\" → **MGN**. "
                "\"Banco sem parar o sistema\" → **DMS**. \"Oracle para PostgreSQL\" → **SCT**. \"Justificar custo\" → **Migration Evaluator**.",
    },
    "3.18": {
        "simples": "Uma coleção de **serviços menos famosos** que já apareceram em provas, mais a lista do que **não cai**. "
                   "Basta saber **para que cada um serve** — sem detalhes.",
        "analogia": "é como **conhecer os figurantes de um filme**: você não precisa saber a história deles, só reconhecer quem é quem "
                    "quando aparecem — e perceber quando alguém **nem é do elenco** (serviço fora do escopo).",
        "saber": ["Saber que a **Customer Carbon Footprint Tool** mostra a estimativa de emissões de carbono (pilar Sustentabilidade).",
                  "Reconhecer a função dos serviços da tabela (ex.: STS → credenciais temporárias; Amazon MQ → RabbitMQ/ActiveMQ).",
                  "Lembrar as categorias **fora do escopo** (games, mídia, robótica, satélite, blockchain)."],
        "termos": [("Distrator", "alternativa errada colocada para confundir."),
                   ("Engenharia do caos", "provocar falhas de propósito para testar se o sistema se recupera.")],
        "dica": "Se uma alternativa cita serviço de **games, mídia, robótica, satélite ou blockchain**, ou um serviço marcado fora do "
                "escopo, ela provavelmente é **distrator**.",
    },
    # ------------------------------------------------------------------ Domínio 4
    "4.1": {
        "simples": "A AWS cobra com base em **três princípios**: pagar pelo uso, ganhar desconto ao se comprometer e pagar menos "
                   "por unidade quando usa mais. E três coisas geram a maior parte da conta.",
        "analogia": "é como o **plano de celular**: pré-pago (pague pelo uso), plano anual com desconto (compromisso) e franquia que "
                    "fica mais barata por GB quando você compra mais (volume).",
        "saber": ["Citar os **3 princípios** de preço.",
                  "Citar os **3 geradores de custo**: computação, armazenamento e **transferência de saída**."],
        "termos": [("Pay-as-you-go", "pagar conforme o uso, sem contrato."),
                   ("Transferência de saída", "dados que saem da AWS para a internet (é cobrada).")],
        "dica": "\"Desconto em troca de compromisso de 1 ou 3 anos\" → **Reservas/Savings Plans**. \"Mais barato por GB quanto mais usa\" → "
                "**desconto por volume**.",
    },
    "4.2": {
        "simples": "Há várias formas de **pagar pelo EC2**: sem compromisso, com compromisso de 1 ou 3 anos, aproveitando sobras "
                   "baratas (que podem ser retomadas) ou com servidor físico dedicado. A prova pede o modelo certo para o cenário.",
        "analogia": "é como **hospedagem**: **On-Demand** é a diária de hotel (cara, sem compromisso); **Reserved/Savings Plans** é o "
                    "aluguel anual (desconto alto); **Spot** é a passagem de última hora com desconto enorme, mas você pode ser tirado "
                    "do voo; **Dedicated Host** é alugar a casa inteira só para você.",
        "saber": ["Escolher o modelo pelo cenário (curto e imprevisível → On-Demand; 24/7 por anos → Reserved/Savings Plans; tolera interrupção → Spot).",
                  "Diferenciar **Compute Savings Plans** (vale para EC2, Fargate e Lambda) de **EC2 Instance Savings Plans**.",
                  "Diferenciar **Dedicated Host** (servidor físico inteiro, licença por núcleo) de **Dedicated Instance**.",
                  "Lembrar o **aviso de 2 minutos** do Spot e as formas de pagamento (All, Partial, No Upfront)."],
        "termos": [("Upfront", "pagamento antecipado."),
                   ("Interrupção", "a AWS retomar a instância Spot quando precisa da capacidade."),
                   ("Capacity Reservation", "garantir capacidade numa AZ, mesmo sem desconto.")],
        "dica": "\"Não pode ser interrompida e é imprevisível\" → **On-Demand**. \"Maior desconto e tolera interrupção\" → **Spot**. "
                "\"Desconto que cobre Fargate e Lambda\" → **Compute Savings Plans**. \"Licença por núcleo físico\" → **Dedicated Host**.",
    },
    "4.3": {
        "simples": "Além do EC2, cada recurso tem a sua forma de cobrança. O ponto mais cobrado é a **transferência de dados**: "
                   "**entrar é grátis, sair é pago**. Também caem os serviços sem custo próprio e o Free Tier.",
        "analogia": "é como um **estacionamento**: entrar é grátis, mas você paga para sair — e quanto mais carros saem, menor o preço "
                    "por carro (faixas de volume).",
        "saber": ["Saber o que é **grátis** e o que é **pago** na transferência de dados.",
                  "Saber que o **EBS** cobra pelo volume **provisionado**, mesmo vazio.",
                  "Citar serviços **sem custo próprio** (CloudFormation, Elastic Beanstalk, Auto Scaling, IAM, Organizations).",
                  "Reconhecer os tipos de **Free Tier**."],
        "termos": [("Provisionado", "o tamanho que você reservou, usado ou não."),
                   ("Free Tier", "uso gratuito oferecido pela AWS, com limites.")],
        "dica": "\"Sempre grátis\" → **transferência de entrada** e serviços como **IAM**. \"Reduzir custo de saída para usuários globais\" → "
                "**CloudFront**. \"Serviço grátis, paga os recursos\" → CloudFormation/Beanstalk/Auto Scaling.",
    },
    "4.4": {
        "simples": "Cada ferramenta de custo responde a uma pergunta: **quanto vai custar?** (antes), **quanto gastei e quanto vou "
                   "gastar?** (análise), **me avise se passar do limite** (alerta) e **quero o detalhe máximo** (relatório).",
        "analogia": "a **Pricing Calculator** é o **orçamento da obra**; o **Cost Explorer** é o **extrato com gráficos**; o **Budgets** é o "
                    "**aviso do cartão** quando passa do limite; o **CUR** é a **nota fiscal detalhada**, item por item; as **tags** são "
                    "**etiquetas** para separar a conta por departamento.",
        "saber": ["Ligar cada pergunta à ferramenta certa (estimar, analisar/prever, alertar, detalhar).",
                  "Saber que as **cost allocation tags** precisam ser **ativadas** no Billing.",
                  "Saber que o **consolidated billing** dá fatura única e desconto por volume."],
        "termos": [("Forecast", "previsão de gasto futuro."),
                   ("Tag", "etiqueta chave-valor colocada num recurso (ex.: projeto=site)."),
                   ("Anomalia", "gasto fora do padrão.")],
        "dica": "\"Estimar **antes**\" → **Pricing Calculator**. \"Tendência e **previsão**\" → **Cost Explorer**. \"**Alerta** ao passar de US$ X\" → "
                "**Budgets**. \"Mais **granular**\" → **CUR**. \"Ratear por departamento\" → **cost allocation tags**.",
    },
    "4.5": {
        "simples": "Os planos de suporte definem **quão rápido e com quanto acompanhamento** a AWS atende você. A prova pede o "
                   "plano certo pelo tempo de resposta, pelo preço ou por um benefício (como o TAM).",
        "analogia": "é como **planos de assistência técnica**: o básico só tem o manual e o FAQ; os planos maiores dão atendimento 24 h, "
                    "resposta mais rápida e, no topo, um **consultor dedicado** (TAM) que acompanha você de perto.",
        "saber": ["Diferenciar os **planos novos** (Basic, Business Support+, Enterprise, Unified Operations) dos **clássicos**.",
                  "Ligar os tempos de resposta a cada plano (30 min, 15 min, 5 min no modelo novo).",
                  "Saber o que é **TAM**, **Concierge** e quem tem **todas as verificações do Trusted Advisor**."],
        "termos": [("TAM", "Technical Account Manager: consultor técnico que acompanha a conta."),
                   ("Concierge", "time de especialistas em faturamento e conta."),
                   ("Caso crítico", "sistema crítico de negócio fora do ar.")],
        "dica": "Distinga os exemplos clássicos do guia da oferta comercial atual (veja o aviso no topo). \"TAM designado + 15 min\" → **Enterprise**. \"5 min\" → "
                "**Unified Operations**. \"Plano pago de entrada, 30 min\" → **Business Support+**.",
    },
    "4.6": {
        "simples": "Fora dos planos de suporte, há muitas fontes de ajuda: comunidade, artigos, documentação, consultoria da AWS, "
                   "parceiros e um catálogo de software. A prova pergunta **a quem recorrer** em cada situação.",
        "analogia": "é um **mapa de quem procurar**: dúvida rápida → **fórum da comunidade** (re:Post); resposta pronta → **FAQ** "
                    "(Knowledge Center); projeto grande → **consultoria da AWS** (Professional Services) ou **empresa parceira** (APN); "
                    "comprar software → **loja** (Marketplace); denúncia → **ouvidoria** (Trust & Safety).",
        "saber": ["Diferenciar **re:Post** (comunidade) de **Knowledge Center** (artigos prontos).",
                  "Diferenciar **Professional Services** (consultoria da AWS) de **APN** (parceiros).",
                  "Saber para que servem o **Marketplace** e o **Trust & Safety**."],
        "termos": [("APN", "AWS Partner Network: rede de empresas parceiras certificadas."),
                   ("Marketplace", "catálogo de software de terceiros cobrado na fatura AWS.")],
        "dica": "\"Comunidade\" → **re:Post**. \"Consultoria da própria AWS\" → **Professional Services**. \"Parceiro certificado\" → **APN**. "
                "\"Comprar software de terceiros\" → **Marketplace**.",
    },
}

# Introdução didática de cada domínio (README do domínio).
DOMINIOS = {
    "1": {
        "simples": "Este domínio ensina **o vocabulário da nuvem**: o que é nuvem, por que usar, como desenhar bons sistemas e "
                   "como uma empresa se prepara para migrar. Quase não há serviço técnico aqui — o que conta são as **listas oficiais** "
                   "da AWS (6 vantagens, 6 pilares, 6 perspectivas, 7 Rs).",
        "ordem": "Siga a ordem dos tópicos: primeiro **o que é** a nuvem (1.1 e 1.2), depois **como projetar** (1.3 e 1.4) e por fim "
                 "**como migrar e quanto custa** (1.5 a 1.7).",
        "dica": "Monte uma folha com as **quatro listas** (vantagens, pilares, perspectivas e 7 Rs) e treine ligar cada cenário a um item.",
    },
    "2": {
        "simples": "Este domínio responde **quem protege o quê** e **com qual serviço**. A base é o modelo de responsabilidade "
                   "compartilhada e o IAM; depois vêm criptografia, compliance, monitoramento, firewalls e detecção de ameaças.",
        "ordem": "Comece por **2.1 (responsabilidade)** e **2.3 (IAM)**, que aparecem em muitas questões. Depois estude os serviços "
                 "em pares que confundem: CloudTrail × Config × CloudWatch (2.7), security group × NACL (2.8), GuardDuty × Inspector × Macie (2.9).",
        "dica": "É o domínio com mais pegadinhas de **\"qual serviço\"**. Para cada serviço, decore **uma palavra-chave** (ex.: Macie → dados pessoais).",
    },
    "3": {
        "simples": "Este é o domínio **maior** e mais **amplo**: um passeio pelos principais serviços da AWS — computação, bancos, "
                   "armazenamento, rede, analytics, IA, integração, ferramentas e migração. A prova não pede detalhes de configuração; "
                   "pede **o serviço certo para cada cenário**.",
        "ordem": "Estude em blocos: **infraestrutura e computação** (3.1 a 3.6), **dados e armazenamento** (3.7 a 3.9), **rede** (3.10) "
                 "e depois os **demais serviços** (3.11 a 3.18). Use as fichas de serviço para aprofundar o que tiver dúvida.",
        "dica": "Para cada serviço, saiba responder: **para que serve** e **qual o vizinho com que ele é confundido**. A seção "
                "\"Entenda em 30 segundos\" de cada ficha resume exatamente isso.",
    },
    "4": {
        "simples": "Este domínio trata de **dinheiro**: como a AWS cobra, como economizar, quais ferramentas mostram e controlam "
                   "os gastos e quais planos de suporte existem.",
        "ordem": "Comece pelos **princípios de preço** (4.1), passe pelos **modelos de compra do EC2** (4.2), que mais caem, e termine "
                 "com ferramentas de custo (4.4) e planos de suporte (4.5).",
        "dica": "As questões são diretas: decore as tabelas de **modelos de compra**, **ferramentas de custo** e **planos de suporte (novos)**.",
    },
}
