"""Conteúdo didático inserido pelo gerar_docs.py nos tópicos e nos índices de domínio de docs/.

Cada tópico ganha a seção "🧠 Antes de começar", logo após o título:
- problema: dificuldade concreta que dá sentido ao tema;
- simples:  a ideia do tópico em palavras simples;
- exemplo: situação ilustrativa com a solução explicada;
- limite: o que o tema ou serviço não resolve por si só;
- analogia: comparação com algo do dia a dia;
- saber:    o que você deve saber responder ao terminar (checklist);
- termos:   palavras novas explicadas sem jargão (opcional);
- dica:     como não errar a questão.

Tudo aqui só explica o que já está no conteúdo do tópico: não acrescenta fatos novos.
"""

TOPICOS = {
    # ------------------------------------------------------------------ Domínio 1
    "1.1": {
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
        "analogia": "é como **alugar um computador**: a **AMI** é o \"molde\" com o sistema já instalado; a **família de instância** é o "
                    "modelo do computador (para jogos, para planilhas pesadas, para muita memória); o **EBS** é o HD que fica guardado "
                    "mesmo com o computador desligado.",
        "saber": ["Explicar **AMI**, **user data** e **key pair**.",
                  "Escolher a **família** pelo uso (ML → computação acelerada; banco em memória → otimizada para memória).",
                  "Diferenciar **EBS** (persistente) de **instance store** (temporário).",
                  "Diferenciar **parar**, **encerrar** e **hibernar**."],
        "termos": [("Instância", "máquina virtual criada no EC2; pode estar executando ou parada."),
                   ("AMI", "imagem pronta (sistema + software) usada para criar a instância."),
                   ("Graviton", "família de processadores AWS baseada em arquitetura ARM; exige software compatível.")],
        "dica": "Leia o **uso** descrito: \"treinar ML/GPU\" → computação acelerada; \"muita memória\" → otimizada para memória; "
                "\"dado temporário que pode ser perdido\" → **instance store**; \"acesso sem SSH\" → **Session Manager**.",
    },
    "3.4": {
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
    },
    "4": {
        "simples": "Este domínio trata de **dinheiro**: como a AWS cobra, como economizar, quais ferramentas mostram e controlam "
                   "os gastos e quais planos de suporte existem.",
        "ordem": "Comece pelos **princípios de preço** (4.1), passe pelos **modelos de compra do EC2** (4.2), que mais caem, e termine "
                 "com ferramentas de custo (4.4) e planos de suporte (4.5).",
    },
}

# Aberturas por situação concreta. Reescrevem a explicação inicial e acrescentam
# problema, exemplo e limite; as analogias, o vocabulário e os objetivos seguem acima.
# Exemplos são autorais e ilustrativos, apoiados nas capacidades já documentadas.
_ABERTURAS = """
1.1 | Uma escola quer disponibilizar um sistema, mas comprar e manter computadores próprios pode exigir dinheiro e trabalho antes mesmo do primeiro aluno usar. | Nuvem é uma forma de obter recursos de tecnologia de um provedor, como a AWS, quando necessário. Você contrata recursos como computadores e armazenamento e administra a parte que cabe a você. | Em vez de comprar uma máquina física, a escola cria um servidor virtual na AWS e instala seu sistema. Outra opção é contratar um software pronto; a responsabilidade muda conforme o modelo. | Usar nuvem não significa que tudo está pronto, gratuito ou administrado pelo provedor. Este tópico ensina a reconhecer os modelos e o trabalho que permanece com o cliente.
1.2 | Uma loja não sabe quantas pessoas chegarão durante uma promoção. Comprar capacidade para o maior pico pode deixar equipamentos ociosos no resto do ano. | Os benefícios da nuvem incluem obter recursos mais rapidamente, ajustar capacidade e mudar a forma de investir em infraestrutura. Cada benefício responde a uma dificuldade diferente. | A loja cria capacidade para a campanha e a reduz depois, em vez de comprar máquinas permanentes apenas para o pico. | Nuvem não garante economia em qualquer projeto. Recursos precisam ser escolhidos e acompanhados; este tópico explica benefícios, não uma promessa de redução automática da fatura.
1.3 | Um sistema pode crescer, ficar lento ou perder uma máquina. A equipe precisa escolher como continuar atendendo e como recuperar dados e operação. | Conceitos de arquitetura descrevem capacidade, disponibilidade, recuperação e dependências entre partes. Eles ajudam a explicar o objetivo antes de escolher um serviço. | Se uma máquina não atende mais os visitantes, você pode usar uma maior ou distribuir o trabalho entre várias. Se uma falhar, outra pode ajudar a manter o atendimento, conforme o projeto. | Crescer não é o mesmo que suportar falhas; ter cópias também não garante recuperação imediata. Aprenda a distinguir as necessidades antes de escolher uma solução.
1.4 | Uma aplicação funciona hoje, mas a equipe precisa avaliar se é segura, recuperável, eficiente e econômica, em vez de olhar apenas se está ligada. | Well-Architected é um conjunto de orientações para revisar uma aplicação e sua operação sob seis áreas, chamadas pilares. Não é um serviço que hospeda o programa. | A escola revisa quem acessa os dados, como restaura um backup e se mantém recursos ociosos. Cada pergunta se relaciona a uma área da revisão. | Seguir um checklist não certifica automaticamente a aplicação nem executa as melhorias. O objetivo é identificar decisões e oportunidades de melhoria.
1.5 | Mudar para a nuvem afeta orçamento, equipes, processos e segurança. A mudança pode fracassar mesmo que as máquinas funcionem. | O Cloud Adoption Framework, ou CAF, ajuda a organizar a preparação da empresa em perspectivas. Cada perspectiva reúne capacidades e responsáveis por uma parte da adoção. | A escola planeja treinamento para a equipe, regras de orçamento e operação do sistema, além da migração técnica. | CAF não transfere servidores nem substitui ferramentas de implantação. Ele organiza a transformação da empresa; Well-Architected se concentra na revisão de uma aplicação e sua operação.
1.6 | Uma empresa quer levar um sistema para a AWS, mas não sabe se deve copiá-lo, adaptá-lo, reescrevê-lo ou até encerrá-lo. | Estratégias de migração descrevem essas escolhas. O esforço e o resultado mudam conforme a decisão sobre cada aplicação. | Um sistema antigo pode ser movido com poucas mudanças; outro pode ser substituído por um software pronto. Não é necessário escolher a mesma estratégia para tudo. | Migrar não significa modernizar automaticamente. Antes de escolher, considere dependências, riscos e a necessidade de manter ou mudar o sistema.
1.7 | Comparar apenas o preço de uma máquina própria com o de uma máquina AWS pode esconder gastos como manutenção, energia e trabalho operacional. | Economia da nuvem trata do conjunto de custos e do valor das escolhas. O custo total inclui mais que o preço de um recurso isolado. | A escola compara equipamentos, manutenção e equipe do ambiente atual com recursos e operação previstos na AWS. | Uma estimativa depende das hipóteses usadas. Este tópico ensina o raciocínio econômico; não determina que qualquer migração sempre será mais barata.
2.1 | Ao usar um serviço AWS, a equipe precisa saber quem protege cada parte. Se ambos presumirem que o outro fará uma tarefa, ela pode ficar sem responsável. | A responsabilidade compartilhada divide tarefas entre AWS e cliente. A divisão muda com o tipo de serviço: quanto mais gerenciado, mais tarefas de infraestrutura a AWS assume. | Em uma máquina EC2, o cliente atualiza o sistema operacional. Num banco RDS, a AWS assume tarefas de administração previstas pelo serviço, enquanto o cliente controla dados e acessos. | Gerenciado não significa que o cliente deixou de ser responsável pela segurança. Sempre identifique o serviço e a camada de que a pergunta trata.
2.2 | Uma conta AWS tem uma identidade inicial com poderes muito amplos. Usá-la no dia a dia aumenta o impacto de um erro ou de credenciais expostas. | O usuário root é essa identidade inicial. O tema mostra como protegê-lo e reconhecer as tarefas que realmente exigem seu uso. | A dona da conta protege o root e usa identidades com permissões adequadas para o trabalho diário, em vez de compartilhar o login inicial com toda a equipe. | Nem toda tarefa administrativa exige root. A lista de tarefas muda; consulte as atualizações indicadas no arquivo, em vez de memorizar listas antigas.
2.3 | Uma aplicação precisa ler documentos, enquanto uma pessoa administra recursos. Dar o mesmo acesso a todos deixa permissões desnecessárias disponíveis. | Identidade e acesso tratam de quem faz uma ação e do que essa identidade está autorizada a fazer. IAM organiza permissões AWS; outros serviços atendem funcionários ou usuários de aplicações. | O programa da escola recebe permissão para ler um conjunto de arquivos, sem poder apagar tudo ou administrar a conta. | Confirmar um login é diferente de conceder uma ação. Você precisa distinguir a identidade, o recurso e a permissão necessária, não apenas decorar o nome de um serviço.
2.4 | A empresa separou testes e produção em várias contas, mas agora precisa de regras comuns e administração central. | Governança de várias contas organiza ambientes e aplica controles. Organizations, Control Tower e ferramentas relacionadas têm papéis diferentes nesse trabalho. | A escola separa o ambiente experimental dos dados de produção e define regras centrais para suas contas. | Um limite de governança não concede sozinho permissão a cada pessoa. Centralizar controles também não configura todas as aplicações automaticamente.
2.5 | Dados podem ser interceptados durante uma comunicação ou lidos no armazenamento por alguém sem autorização. | Criptografia protege a leitura dos dados por meio de chaves e tecnologias de conexão. É preciso distinguir proteção durante o transporte, no armazenamento e administração de chaves. | O site usa HTTPS para a comunicação com o aluno e configura proteção dos documentos armazenados. São duas camadas diferentes. | Criptografia não impede todo apagamento, erro de permissão ou vazamento por um usuário autorizado. Ela é uma proteção específica dentro de um conjunto de controles.
2.6 | Um auditor pede que a empresa demonstre suas práticas de segurança e os controles do provedor. A equipe precisa saber onde obter evidências e como avaliar seu ambiente. | Conformidade envolve atender requisitos e demonstrar isso. Relatórios da AWS, avaliações de configuração e evidências do cliente atendem partes diferentes desse processo. | A escola consulta relatórios oficiais do provedor e reúne evidências de que ela própria protege acessos e dados. | A conformidade da AWS não torna toda aplicação do cliente automaticamente conforme. Documentos, configuração e operação precisam ser avaliados no contexto do requisito.
2.7 | O sistema está lento, um recurso foi alterado ou uma configuração deixou de atender às regras. Cada pergunta precisa de um tipo diferente de registro. | CloudWatch acompanha comportamento e operação; CloudTrail registra atividades AWS; Config acompanha configuração e sua avaliação. O objetivo da pergunta orienta a ferramenta. | Para lentidão, a equipe examina métricas e logs. Para saber quem alterou um recurso, procura o evento. Para avaliar sua configuração, usa o histórico e as regras aplicáveis. | Nenhuma dessas ferramentas observa tudo sem configuração. Coleta, retenção, cobertura e ações de resposta variam; registrar um problema não é o mesmo que corrigi-lo.
2.8 | Um recurso acessível pela rede pode receber conexões indevidas, pedidos web maliciosos ou tentativas de sobrecarga. | Proteção de rede e aplicação usa controles em camadas. Regras de conexão, inspeção de pedidos web e proteção contra sobrecarga tratam ameaças diferentes. | A escola limita conexões ao banco, inspeciona pedidos ao site e avalia proteção contra ataques distribuídos. Cada medida atua numa parte do caminho. | Uma regra de rede não corrige o código do programa; uma proteção web não inspeciona automaticamente todos os protocolos. Identifique o tipo de tráfego e o ponto de proteção.
2.9 | Atividade suspeita, software vulnerável e arquivos com informações pessoais são problemas distintos, mesmo que todos sejam chamados de segurança. | Serviços de detecção e análise têm especialidades. GuardDuty procura sinais de ameaça; Inspector avalia vulnerabilidades; Macie procura dados sensíveis no S3; outras ferramentas ajudam a reunir ou investigar achados. | A equipe investiga um alerta de uso suspeito de identidade, corrige software vulnerável e revisa um arquivo com dados pessoais usando ferramentas adequadas a cada caso. | Detectar não significa confirmar uma invasão nem corrigir tudo automaticamente. A equipe precisa avaliar os resultados e organizar a resposta.
2.10 | Segurança também depende de decisões cotidianas: proteger credenciais, limitar permissões e saber como comunicar uso abusivo ou um incidente. | Este tópico reúne práticas e canais que complementam os serviços de segurança. O objetivo é relacionar cada ação ao risco que ela reduz. | A escola evita publicar credenciais no código, revisa acessos e define como agir quando identifica um problema. | Uma boa prática isolada não garante um ambiente seguro. Entenda a finalidade de cada ação e o canal adequado, em vez de escolher uma ferramenta genérica para qualquer problema.
3.1 | Você precisa criar ou consultar recursos AWS, mas pode fazer isso por uma tela, por comandos, por um programa ou por uma descrição automatizada do ambiente. | São maneiras diferentes de operar serviços. Console oferece interface visual; CLI usa comandos; SDK integra programas; ferramentas de infraestrutura descrevem recursos para implantação. | Uma pessoa cria um recurso pelo console e depois automatiza tarefas repetidas com comandos ou código. A permissão necessária continua sendo parte do acesso. | A forma de acesso não muda sozinha o que a identidade pode fazer. Uma ferramenta de operação também não é o serviço que hospeda a aplicação.
3.2 | Uma aplicação precisa estar perto dos usuários e continuar atendendo se parte da infraestrutura falhar. Para planejar isso, a equipe precisa entender onde os recursos ficam. | A infraestrutura global organiza regiões, zonas de disponibilidade e pontos de presença. São unidades com funções diferentes, não nomes intercambiáveis para o mesmo lugar. | A escola escolhe uma região para seus recursos e planeja partes da aplicação em zonas diferentes. Uma rede de distribuição pode entregar conteúdo por pontos de presença. | Escolher uma região não distribui automaticamente todo recurso entre várias zonas. Localização, disponibilidade e serviços oferecidos precisam ser avaliados.
3.3 | Você quer colocar um programa em funcionamento sem depender do seu computador pessoal, mas precisa escolher o sistema e administrar o que será instalado. | EC2 permite criar computadores virtuais na AWS. Cada máquina é uma instância; você escolhe sua capacidade, instala a aplicação e controla o acesso. | A escola instala seu sistema de matrícula numa instância. Os alunos usam o sistema pela rede; a equipe administra o servidor e atualiza seu software. | EC2 fornece a máquina, não um sistema de matrícula pronto. Publicação, segurança, dados e custos associados continuam exigindo configuração e acompanhamento.
3.4 | Muitos visitantes chegam ao mesmo tempo. Uma máquina pode não atender, e várias máquinas sem distribuição adequada também podem ficar desequilibradas. | Escalabilidade ajusta a capacidade; balanceamento distribui o tráfego. Os dois podem trabalhar juntos, mas resolvem partes diferentes do atendimento. | Durante uma promoção, o grupo adiciona máquinas e o balanceador encaminha pedidos aos destinos disponíveis. Depois, a quantidade de máquinas pode diminuir conforme as regras. | Balanceador não cria máquinas por si só; aumentar máquinas não resolve todo gargalo. A aplicação e o armazenamento também precisam suportar o desenho.
3.5 | Sua aplicação pode precisar rodar como um pacote completo ou executar apenas uma tarefa quando algo acontece. A equipe precisa escolher a forma de execução e quem administra os servidores. | Containers empacotam aplicações e dependências. Serviços como ECS e EKS coordenam sua execução; Fargate fornece capacidade sem administração direta das máquinas. Lambda executa funções acionadas por chamadas ou eventos. | Um serviço de pedidos executa em containers. Uma tarefa de gerar miniatura pode ser uma função acionada quando chega uma foto. | Serverless não significa ausência de servidores, custo zero ou execução ilimitada. Empacotar, coordenar e fornecer capacidade são funções distintas.
3.6 | Nem toda necessidade pede administrar uma máquina diretamente. Você pode querer uma hospedagem simples, uma implantação facilitada ou muitos trabalhos em lote. | Este tópico compara formas de execução: Lightsail simplifica ofertas, Beanstalk apoia a implantação de aplicações e Batch organiza trabalhos. Opções de proximidade atendem necessidades específicas de localização. | Um site pequeno pode avaliar Lightsail; uma aplicação com plataforma compatível, Beanstalk; centenas de conversões de arquivos, Batch. | Esses serviços não fazem o mesmo trabalho. Escolha pelo tipo de tarefa e pela responsabilidade desejada, verificando compatibilidade e escopo.
3.7 | Uma aplicação precisa guardar dados, mas um cadastro, uma rede de relações e um relatório sobre milhões de vendas têm formas de consulta diferentes. | Bancos de dados organizam registros para armazenar e consultar. A AWS oferece modelos relacionais, chave-valor, documentos, grafos e análise, entre outros. | A escola usa tabelas relacionadas para matrículas. Um jogo pode buscar perfis por identificador; uma análise histórica pode usar um ambiente voltado a relatórios. | Não há um banco melhor para qualquer dado. Primeiro identifique a estrutura e as perguntas que a aplicação precisa fazer; depois avalie o serviço.
3.8 | O sistema precisa guardar fotos, PDFs e outros conteúdos sem vincular cada arquivo ao disco de uma única máquina. | S3 armazena dados como objetos em buckets. Um objeto contém o dado e sua identificação; o bucket é o recipiente em que ele fica organizado. | A escola guarda PDFs de materiais e permite que o aplicativo disponibilize cada documento aos alunos autorizados. | S3 não executa sozinho o sistema da escola nem torna os arquivos públicos ao recebê-los. Acesso, proteção, classe de armazenamento e custo precisam ser definidos.
3.9 | Sua aplicação pode precisar de um disco próprio, de pastas compartilhadas ou de ligação com arquivos mantidos na empresa. Essas necessidades não são iguais. | Este tópico compara armazenamento em blocos, arquivos compartilhados e integração com ambientes locais, além de cópias de segurança e recuperação. | Uma máquina usa EBS como disco. Várias máquinas podem precisar de EFS para compartilhar pastas. Uma aplicação Windows pode exigir uma modalidade FSx compatível. | Escolher armazenamento só pelo nome ou preço pode causar incompatibilidade. Primeiro descubra como a aplicação precisa ler e gravar os dados.
3.10 | Usuários precisam chegar ao site, a aplicação precisa chegar ao banco e a empresa pode precisar conectar sua rede à AWS. Cada comunicação tem um caminho e controles. | Rede define conexões e rotas. VPC organiza recursos em uma rede virtual; DNS relaciona nomes a endereços; distribuição de conteúdo e aceleração atuam na entrega aos usuários. | O aluno digita o domínio; DNS indica o destino. O pedido chega ao serviço que atende o site, e a aplicação acessa o banco por um caminho autorizado. | Nenhum serviço desta lista configura toda a comunicação sozinho. Organizar rede, permitir acesso, resolver nomes e distribuir conteúdo são funções distintas.
3.11 | A empresa acumulou dados e quer transformar registros em respostas, como quais cursos tiveram mais procura e como a demanda mudou. | Analytics reúne preparação, consulta, processamento e visualização de dados. Cada etapa pode exigir uma ferramenta diferente. | A escola prepara arquivos com Glue, consulta dados com uma ferramenta adequada e mostra resultados num painel. Dados contínuos de sensores pedem um processo diferente de um relatório mensal. | Criar um painel não corrige os dados nem coleta qualquer fonte automaticamente. Identifique se o problema é preparar, consultar, processar um fluxo ou visualizar.
3.12 | Uma aplicação quer transcrever áudio, fazer previsões ou gerar texto. Embora todas envolvam IA, o trabalho necessário e a solução são diferentes. | Serviços de IA podem oferecer funções prontas, ferramentas para desenvolver modelos próprios ou acesso a modelos generativos existentes. A escolha depende da tarefa. | Para transcrever uma aula, a escola avalia Transcribe. Para criar um modelo com seus dados, avalia SageMaker AI. Para gerar conteúdo com modelos existentes, há ofertas específicas. | IA não garante precisão e não conhece automaticamente os dados da empresa. Compatibilidade, acesso, avaliação e escopo da prova precisam ser considerados.
3.13 | Uma ação pode gerar tarefas para outros sistemas. Se cada parte depender de todas as outras responderem na hora, a aplicação fica mais difícil de operar. | Integração permite separar tarefas e coordenar comunicação. Filas guardam trabalho; notificações distribuem avisos; eventos orientam ações; fluxos coordenam etapas. | A matrícula confirmada gera um aviso e uma tarefa de emitir certificado. Uma fila pode guardar a tarefa; um fluxo pode acompanhar etapas do processo. | Uma fila não executa o trabalho, e uma notificação não coordena por si só todo o processo. Entenda qual parte da comunicação precisa ser resolvida.
3.14 | Uma organização pode precisar atender pessoas, enviar e-mails, oferecer trabalho remoto ou conectar equipamentos. Cada necessidade vai além de criar uma máquina. | Este tópico reúne serviços voltados a experiências e aplicações específicas. É importante reconhecer o problema de cada produto, e não memorizar a categoria como se fosse um serviço só. | A escola pode usar um serviço de e-mail para confirmações e uma plataforma de atendimento para a secretaria. Sensores conectados exigem outro conjunto de recursos. | Um serviço pronto continua exigindo configuração, identidade e integração. As ferramentas desta seção não substituem umas às outras.
3.15 | Uma equipe precisa construir versões do programa, testá-las, publicá-las e investigar o caminho das requisições quando há lentidão. | Ferramentas de desenvolvimento e observação apoiam etapas distintas. Construção e entrega automatizada são diferentes de rastrear a execução da aplicação. | Uma alteração passa por construção e testes configurados. Depois da implantação, rastreamentos ajudam a examinar um pedido que ficou lento. | Uma ferramenta não escreve os testes nem corrige o programa automaticamente. Identifique se o pedido é construir, coordenar a entrega, implantar ou investigar.
3.16 | A aplicação já existe, mas a equipe precisa criar ambientes de modo repetível, administrar máquinas e acompanhar mudanças, saúde e regras. | Gestão e governança reúnem ferramentas para operar recursos e aplicar controles. Cada ferramenta observa ou administra uma parte específica. | A escola descreve um ambiente com CloudFormation, administra máquinas com Systems Manager e consulta avisos relevantes no AWS Health. | Administrar recursos não significa que qualquer serviço de gestão executa todas essas tarefas. Descubra a ação desejada antes de escolher o produto.
3.17 | Mover para a AWS envolve aplicações, bancos e arquivos, que podem exigir processos e ferramentas diferentes. | Migração inclui descobrir o ambiente, planejar mudanças, replicar ou transferir dados, testar e realizar a troca. As ferramentas atendem etapas e tipos de recurso específicos. | A escola prepara a migração de um servidor e de seu banco. Replica e testa cada parte antes de mudar o sistema em uso. | Transferir um banco não move automaticamente todo o programa; copiar arquivos também não migra suas dependências. Compatibilidade e disponibilidade das ofertas precisam ser verificadas.
3.18 | Alguns nomes AWS aparecem em listas antigas ou em problemas muito específicos. Tentar decorar todos sem entender a função dificulta o estudo. | Esta seção organiza serviços adicionais por finalidade e identifica seu status no escopo. O objetivo é reconhecer o tipo de problema e saber quando aprofundar. | Ao encontrar um nome novo, descubra primeiro se ele atende armazenamento, integração, rede ou outra necessidade e confira se está na lista atual da prova. | Estar nesta seção não significa que o serviço continua disponível ou que é prioritário para o exame. Use as marcações de escopo e as observações de cada ficha.
4.1 | Um recurso pode estar ocioso e ainda gerar cobrança. Para planejar gastos, você precisa entender pelo que está pagando, não apenas quantas pessoas usam o sistema. | Preço pode depender de capacidade provisionada, tempo, armazenamento, chamadas ou transferência, conforme o serviço. Diferentes componentes podem ter cobranças independentes. | Uma máquina ligada sem visitantes pode custar. Mesmo ao pará-la, discos ou outros recursos mantidos podem continuar cobrados. | Pagar pelo uso não significa pagar apenas por pessoas usando a aplicação. Este tópico ensina a identificar as unidades e condições de cobrança.
4.2 | Uma máquina usada ocasionalmente, uma aplicação estável e um trabalho que pode ser interrompido não precisam da mesma forma de compra. | Modelos de compra EC2 trocam flexibilidade, compromisso, risco de interrupção e requisitos de capacidade por condições diferentes. | Um teste de curta duração pode usar On-Demand. Um trabalho tolerante a interrupções pode avaliar Spot. Uso estável pode justificar avaliar um compromisso. | Desconto não significa que a opção atende qualquer tarefa. Compromisso, interrupção e garantia de capacidade são conceitos diferentes; escolha pelo requisito.
4.3 | Parar a computação ou reduzir visitas não elimina necessariamente os custos de dados armazenados e comunicações. | A cobrança pode envolver armazenamento, requisições, endereços e transferências, além da execução. Cada recurso precisa ser analisado separadamente. | A escola para uma máquina de testes, mas mantém volumes e cópias de dados. Esses recursos podem continuar tendo custo. | Não aplique a regra de um serviço a todos os outros. Identifique qual recurso permanece e qual condição gera cobrança.
4.4 | A equipe quer planejar um projeto, entender uma fatura e acompanhar um orçamento. São três perguntas diferentes sobre dinheiro. | Calculadora estima; análise de custos explica gastos; orçamento acompanha metas; relatórios fornecem detalhe. A ferramenta depende da pergunta. | Antes de criar o sistema, a escola estima o custo. Depois, analisa o consumo e configura avisos para acompanhar o orçamento. | Estimar não garante a fatura, e um aviso não é um bloqueio automático de todo gasto. Não confunda planejamento, análise e controle.
4.5 | Quando o sistema tem um problema, a empresa precisa saber como pedir ajuda e quais recursos de atendimento estão incluídos em sua oferta. | Planos de suporte definem canais e condições de auxílio. A escolha deve considerar a necessidade de orientação e o impacto dos incidentes. | Uma empresa avalia o acesso a suporte técnico necessário para sua aplicação e confere as condições da oferta aplicável. | Tempo de primeira resposta não é prazo garantido de correção. Os nomes comerciais e os exemplos do guia podem diferir; leia os avisos e o contexto.
4.6 | Uma pessoa precisa aprender, tirar uma dúvida ou contratar ajuda para executar um projeto. Nem todo canal serve para as três necessidades. | Recursos de ajuda incluem documentação, comunidades, orientação, parceiros e ofertas. Cada um responde a um tipo de necessidade. | A escola consulta documentação para entender um recurso e avalia um parceiro quando precisa de trabalho especializado para a migração. | Uma resposta comunitária não equivale a um contrato de suporte ou de execução. Escolha o canal pelo trabalho e pela responsabilidade esperada.
"""

_linhas = {}
for _linha in _ABERTURAS.strip().splitlines():
    _campos = [c.strip() for c in _linha.split("|")]
    if len(_campos) != 5 or not all(_campos):
        raise ValueError(f"Abertura incompleta: {_linha}")
    _sec, *_valores = _campos
    if _sec in _linhas:
        raise ValueError(f"Abertura duplicada: {_sec}")
    _linhas[_sec] = dict(zip(("problema", "simples", "exemplo", "limite"), _valores))
if set(_linhas) != set(TOPICOS):
    raise ValueError("Cobertura das aberturas didáticas diferente dos tópicos")
for _sec, _abertura in _linhas.items():
    TOPICOS[_sec].update(_abertura)

DOMINIOS["1"].update({
    "problema": "Antes de escolher um serviço, você precisa entender por que usar nuvem e quais responsabilidades e decisões isso envolve.",
    "exemplo": "Uma escola quer colocar seu sistema na internet. Primeiro compara manter equipamentos próprios com contratar recursos e planeja como crescer e recuperar falhas.",
})
DOMINIOS["2"].update({
    "problema": "Dados e recursos precisam de proteção, e a equipe precisa saber quem pode fazer cada ação e quem é responsável por cada camada.",
    "exemplo": "A escola permite que alunos consultem seus dados e que a equipe administre recursos, sem compartilhar uma identidade com poder sobre tudo.",
})
DOMINIOS["3"].update({
    "problema": "A AWS tem muitos nomes, mas você precisa primeiro descobrir qual dificuldade cada serviço atende.",
    "exemplo": "O sistema da escola precisa executar um programa, guardar PDFs, manter matrículas e receber trabalhos em espera. São quatro problemas, com soluções diferentes.",
    "dica": "Para cada serviço, explique o problema, a solução e o que continua exigindo configuração. A abertura ‘Comece pelo problema’ das fichas prepara essa leitura.",
})
DOMINIOS["4"].update({
    "problema": "Depois de escolher recursos, a equipe precisa prever gastos, acompanhar consumo e saber como pedir ajuda.",
    "exemplo": "A escola estima o custo antes de publicar seu sistema, analisa a fatura depois e configura avisos de orçamento.",
    "dica": "Diferencie estimar, analisar gasto e acompanhar orçamento. Em suporte, leia o requisito e confira as condições no contexto do material.",
})

APOIO = {
    "estrutura-da-apostila.md": (
        "Uma lista de nomes e valores ajuda na revisão, mas não ensina sozinha quem começa do zero.",
        "Esta página apresenta a sequência dos capítulos e o motivo de cada parte. Use-a para ler o material ou manter novas aulas no mesmo padrão.",
        "Ao estudar uma fila, entenda primeiro quem envia e quem executa o trabalho. Só depois compare ordenação, conservação e repetição de mensagens.",
    ),
    "README.md": (
        "Você quer estudar AWS, mas precisa saber o que a certificação avalia e por onde começar.",
        "Esta página apresenta o exame e organiza os caminhos de estudo. Comece pela ideia de nuvem, siga pelos quatro domínios e use as fichas para entender cada serviço.",
        "Se você ainda não sabe o que é um servidor, não precisa começar decorando siglas: leia a abertura do primeiro tópico e avance com os exemplos.",
    ),
    "plano-de-estudos.md": (
        "Há muitos assuntos e você precisa distribuir leitura e revisão sem tentar aprender tudo numa sessão.",
        "Este plano divide o estudo em etapas e sugere uma rotina. Ajuste o ritmo à sua disponibilidade e volte aos temas que ainda não consegue explicar.",
        "Em uma sessão, leia um tópico, explique o problema que ele resolve e só depois tente responder às perguntas. Uma resposta errada indica o que revisar.",
    ),
    "escopo-oficial.md": (
        "Um serviço pode existir na AWS e, ainda assim, não estar na lista de estudo do exame. Também há listas antigas circulando.",
        "Esta página separa tarefas e serviços conforme o guia oficial consultado. Use-a para priorizar o estudo e interpretar as marcações das fichas.",
        "Ao encontrar uma ficha de referência, confira a marcação antes de investir tempo em detalhes. ‘Não listado’ e ‘explicitamente fora do escopo’ não são a mesma classificação.",
    ),
    "atualizacoes-2025-2026.md": (
        "Um número ou nome de um material antigo pode não corresponder mais à oferta comercial ou ao guia do exame.",
        "Esta página registra diferenças e verificações do material. Leia a observação associada ao tema para saber qual contexto está sendo descrito.",
        "Ao estudar suporte, confira se o exemplo descreve um modelo do guia ou uma oferta comercial atual. Não escolha uma resposta apenas porque reconhece um nome antigo.",
    ),
    "pendencias-de-verificacao.md": (
        "Algumas afirmações do material ainda precisam de confirmação oficial. Sem uma indicação clara, elas poderiam ser tratadas como fatos seguros.",
        "Esta página registra pontos em aberto para revisão. Uma pendência é algo a confirmar, não uma regra a decorar.",
        "Se encontrar um prazo sem confirmação, use as referências verificadas do tópico para estudar e mantenha esse prazo como pendente até haver evidência adequada.",
    ),
    "auditoria-conteudo-2026-10.md": (
        "Você precisa saber o que foi conferido no material e quais limites essa revisão tem, em vez de assumir que uma lista de arquivos prova domínio do exame.",
        "Esta página documenta a revisão realizada, sua cobertura e suas ressalvas. Ela serve para acompanhar a qualidade do material; não é uma aula sobre um serviço.",
        "Use a auditoria para localizar a revisão de um tema e depois leia sua explicação. Um tópico coberto ainda pode precisar de estudo e confirmação de entendimento.",
    ),
    "estudar-sem-console.md": (
        "Você lê o nome e as opções de um serviço, mas ainda não consegue explicar qual trabalho ele faz sem ver uma tela.",
        "Este roteiro ensina a estudar pela necessidade, pelo recurso, pela ação e pelos limites. Primeiro entenda o problema; depois imagine o que é configurado e o que acontece.",
        "Para EC2, explique que você recebe uma máquina virtual para executar seu programa. Para S3, explique que recebe armazenamento de objetos. Eles atendem trabalhos diferentes.",
    ),
}


def bloco_apoio(nome):
    problema, explicacao, exemplo = APOIO[nome]
    return "\n".join([
        "<!-- didatico:inicio -->", "## 🧭 Antes de ler", "",
        f"**Por que esta página existe?** {problema}", "",
        f"**Como usar?** {explicacao}", "",
        f"**Exemplo:** {exemplo}", "<!-- didatico:fim -->",
    ])
