# 🔍 Pendências de verificação

<!-- didatico:inicio -->
## 🧭 Antes de ler

**Por que esta página existe?** Algumas afirmações do material ainda precisam de confirmação oficial. Sem uma indicação clara, elas poderiam ser tratadas como fatos seguros.

**Como usar?** Esta página registra pontos em aberto para revisão. Uma pendência é algo a confirmar, não uma regra a decorar.

**Exemplo:** Se encontrar um prazo sem confirmação, use as referências verificadas do tópico para estudar e mantenha esse prazo como pendente até haver evidência adequada.
<!-- didatico:fim -->

> ✅ **Nenhuma pendência aberta** desde a [segunda verificação das pendências](../../fontes/verificacao-pendencias-2026-10-rodada-2.md)
> (04/10/2026), feita com URL oficial e trecho literal para cada item.
>
> Se surgir uma nova dúvida, acrescente aqui: afirmação, onde está no repositório e a task do exam guide.
> Verificações anteriores: [verificação](../../fontes/verificacao-fontes-oficiais-2026-10.md),
> [rodadas 3 e 4](../../fontes/verificacao-fontes-oficiais-2026-10-rodadas-3-4.md) e
> [primeira verificação das pendências (PDF)](../../fontes/verificacao-pendencias-2026-10.pdf).

## 🧭 Para que serve esta página

> 💡 **Em palavras simples:** é a lista de **afirmações que ainda precisam ser confirmadas** em fonte oficial da AWS.
> Enquanto uma informação estiver aqui, trate-a com cuidado. Quando é confirmada, ela sai de *Em aberto* e vai para *Resolvidos*.

## ❔ Em aberto

| # | Afirmação | Onde está | Task |
|---|---|---|---|
| — | — | — | — |

## ⚠️ Correções importantes desta rodada

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **Security Hub:** Security Hub reúne achados de fontes compatíveis e oferece avaliações de controles, conforme os recursos habilitados.
- **CloudTrail:** Registro de atividades e chamadas AWS compatíveis. Ajuda a analisar quem realizou uma operação, em vez de medir sozinho a velocidade da aplicação.
- **AWS Config:** AWS Config registra configurações de recursos compatíveis e permite avaliá-las com regras.
- **Config:** Serviço que acompanha configurações e suas avaliações em recursos compatíveis. Observar configuração é diferente de observar uma métrica de desempenho.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **root:** Na conta AWS, é a identidade principal com poderes especiais. Dentro de Linux, root é o administrador do sistema operacional. Administrar Linux não é o mesmo que administrar a conta AWS.
- **suporte:** Suporte oferece ajuda conforme um plano e suas condições. Um prazo de resposta inicial não é garantia de tempo de resolução de todo incidente.
- **objeto:** Unidade de dados guardada no armazenamento de objetos: conteúdo, identificação e informações associadas. Não é uma máquina nem um programa em execução.

| Antes no repositório | Resultado oficial | Aplicado em |
|---|---|---|
| "Mudar o plano de suporte" e "alterar o nome da conta" exigem o root | **Não exigem mais.** Nome da conta, contatos e regiões não exigem root; o plano de suporte saiu da lista oficial | [2.2](../02-seguranca-e-conformidade/02-usuario-root.md), [IAM](../../servicos/seguranca/iam.md), [planos de suporte](../../servicos/custos/planos-de-suporte.md), [simulado](../../simulados/simulado-01.md) |
| Intelligent-Tiering "sem taxa de recuperação" | Standard e Bulk grátis, mas **Expedited na camada Archive Access é cobrado**, além do monitoramento por objeto | [Classes do S3](../../servicos/armazenamento/s3-classes-de-armazenamento.md) |
| CloudTrail Lake fechado a novos clientes em 30/04/2026 | **31/05/2026** (anúncio de 31/03/2026) | [CloudTrail](../../servicos/gerenciamento/cloudtrail.md) |
| Security Hub "exige" o AWS Config | A maioria dos controles usa o Config; com o Security Hub novo, o recorder é criado automaticamente | [Security Hub](../../servicos/seguranca/security-hub.md) |

## ✔️ Resolvidos

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **EFS:** O EFS oferece um sistema de arquivos compartilhado.
- **FSx:** O FSx oferece sistemas de arquivos gerenciados em modalidades diferentes.
- **Storage Gateway:** Storage Gateway faz a ligação entre o ambiente local e o armazenamento em nuvem usando interfaces de arquivos, volumes ou fitas, conforme a modalidade.
- **backup:** Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.
- **Elastic Disaster Recovery:** Elastic Disaster Recovery replica dados de servidores compatíveis para preparar sua recuperação em máquinas AWS.
- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **Aurora:** Aurora é um banco relacional da AWS dentro da família RDS.
- **DynamoDB:** DynamoDB é um banco gerenciado que organiza dados em tabelas de itens.
- **VPN:** Conexão lógica protegida que liga usuários ou redes. Um túnel VPN não concede automaticamente acesso a todos os recursos do destino.
- **Route 53:** Route 53 oferece DNS e recursos associados, como registro de domínios e verificações de saúde.
- **CloudFront:** CloudFront distribui conteúdo por uma rede de pontos de presença.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **Shield:** Shield oferece proteção contra ataques de negação de serviço distribuídos, com diferenças de cobertura e recursos entre suas modalidades.
- **GuardDuty:** GuardDuty analisa fontes de dados compatíveis para detectar possíveis ameaças e produzir achados de segurança.
- **CloudWatch:** Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.
- **Organizations:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.
- **AI / IA:** Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.
- **Bedrock:** Bedrock oferece acesso gerenciado a modelos e recursos de desenvolvimento de aplicações com IA generativa, conforme a oferta e as autorizações.
- **Amazon Q / Q:** A família Amazon Q inclui assistentes com funções diferentes: Q Developer apoia desenvolvimento; Q Business trabalha com conhecimento corporativo conectado e autorizado.
- **SQS:** SQS guarda mensagens numa fila até que consumidores as recebam e processem.
- **SNS:** SNS publica mensagens em tópicos e as distribui a assinantes compatíveis.
- **Cost Explorer:** Cost Explorer ajuda a visualizar e analisar dados de custos e uso, usando filtros, agrupamentos e recursos compatíveis de previsão.
- **virtual:** Um recurso virtual é criado por software sobre equipamentos físicos. VM significa máquina virtual: computador lógico com sistema operacional e recursos de processamento.
- **MB / KB / TB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.
- **AZ:** Parte isolada da infraestrutura dentro de uma região, formada por um ou mais datacenters. Distribuir recursos entre zonas pode reduzir o impacto de uma falha localizada.
- **Multi-AZ:** Configuração que utiliza mais de uma zona de disponibilidade. Seu comportamento depende do serviço: não presuma que toda cópia atende leituras ou que isso é backup de dados apagados.
- **serverless:** Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **RTO:** Objetivo de tempo de recuperação: quanto tempo a organização aceita ficar sem o sistema após uma interrupção.
- **RPO:** Objetivo de ponto de recuperação: quanto histórico de dados a organização aceita perder, medido como intervalo de tempo.
- **IP:** Endereços usados para identificar interfaces e destinos na rede. IPv4 e IPv6 são versões diferentes; ter um endereço não concede permissão nem garante uma rota.
- **origem:** Local de onde uma distribuição obtém conteúdo, como um servidor ou bucket. Uma cópia em cache não elimina toda necessidade de acessar a origem.
- **ELB:** Recurso que distribui tráfego entre destinos configurados. Ele não cria sozinho todas as máquinas necessárias nem conserta seu programa.
- **política:** Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.
- **MFA:** Verificação adicional de autenticação, além da primeira credencial. Ela protege a entrada, mas não concede permissões por si só.
- **SCP:** Política de controle de serviços usada na organização para limitar permissões disponíveis em contas às quais se aplica. Ela não concede acesso ao usuário sozinha.
- **SSE-S3:** Formas de criptografia no servidor do S3, que diferem na origem e administração das chaves e, no último caso, nas camadas. A tabela da seção distingue essas escolhas.
- **DDoS:** Ataque distribuído que tenta sobrecarregar um serviço e impedir seu uso legítimo. É diferente de tentar explorar um campo vulnerável de um programa.
- **CIS / NIST / PCI DSS:** Referências, padrões ou requisitos de segurança e conformidade com escopos distintos. A menção de um nome não é certificação automática do cliente; identifique qual requisito a seção aborda.
- **alarme:** Condição acompanhada sobre dados de monitoramento. Uma mudança de estado pode gerar ações configuradas; o alarme não diagnostica todo problema sozinho.
- **ACU:** Unidade de capacidade de determinadas ofertas Aurora. Ela expressa capacidade conforme a oferta; não é uma contagem de usuários do aplicativo.
- **cluster:** Conjunto de recursos que trabalham de forma coordenada. O termo aparece em computação, banco e outras áreas, com papéis diferentes.
- **On-Demand:** Modalidade de uso sem o compromisso de longo prazo descrito por reservas e planos. Cobrança e unidades dependem do recurso contratado.
- **RI:** Benefício e condições de reserva para configurações compatíveis. Não confunda desconto com qualquer garantia universal de capacidade.
- **Savings Plans:** Compromisso de gasto por período em troca de condições de preço para uso elegível. Se a necessidade diminuir, o compromisso não desaparece automaticamente.
- **TAM:** Gerente técnico de conta em ofertas de suporte que incluem esse papel. Atua no acompanhamento e orientação previstos; não substitui toda a equipe do cliente.
- **CUR:** Relatório de custos e uso. Ele ajuda a analisar consumo registrado; é diferente de uma estimativa antes de criar recursos.
- **OAC:** Controle de acesso à origem em integrações CloudFront compatíveis. Ajuda a restringir acesso direto à origem conforme a configuração.
- **legado:** Sistema existente com tecnologias ou dependências que precisam ser preservadas ou avaliadas numa mudança. Antigo não significa automaticamente que pode ser desligado.
- **DRS:** Sigla usada para Elastic Disaster Recovery. Replicação prepara uma recuperação; testes e dependências continuam necessários.
- **DB:** Abreviação de database, ou banco de dados. Cada mecanismo oferece formas e garantias próprias de armazenamento e consulta.
- **DB cluster:** Conjunto coordenado de componentes de banco. A função de cada membro e seu comportamento de leitura, escrita ou recuperação dependem do serviço.
- **SRT:** Protocolo de transporte de mídia. Compatibilidade de transmissão depende do produto e da configuração; não é uma classe de armazenamento.
- **FIDO2 / TOTP:** Mecanismos de autenticação. FIDO2 usa padrões para credenciais com dispositivos ou autenticadores; TOTP é código temporário calculado com base em tempo.
- **FSBP:** Práticas fundamentais de segurança AWS usadas em avaliações de controles. Um controle aprovado não certifica toda a aplicação.
- **FOCUS:** Especificação de organização de dados de custos e uso. Padronizar dados ajuda a analisá-los, mas não reduz o gasto automaticamente.

| # | Resultado | Aplicado em |
|---|---|---|
| 1 | Origem AWS (S3, EC2, ELB) → CloudFront grátis; entrada grátis; mesma AZ por IP privado grátis; saída, entre regiões e entre AZs cobradas | [4.3](../04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md), [CloudFront](../../servicos/redes/cloudfront.md) |
| 2 | Always Free: SQS (1 milhão de requisições), SNS (1 milhão de publicações), CloudWatch (10 métricas e 10 métricas de alarme), Lambda, DynamoDB e outros 30+ | [4.3](../04-cobranca-precos-e-suporte/03-cobranca-de-outros-recursos.md) |
| 3 | Capacity Reservations cobradas pela tarifa On-Demand mesmo sem uso; Savings Plans e RIs regionais se aplicam | [4.2](../04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| 4 | RI zonal reserva capacidade; Convertible é trocável; Standard pode ser vendida e Convertible não; RIs antes dos Savings Plans | [4.2](../04-cobranca-precos-e-suporte/02-modelos-de-compra-ec2.md) |
| 5 | Cost Explorer: 13 meses de histórico, previsão de 3 meses (diária) e 12 meses (mensal), API a US$ 0,01 | [Cost Explorer](../../servicos/custos/cost-explorer.md) |
| 6 | CUR via Data Exports (CUR 2.0, FOCUS 1.2/1.0); Cost Anomaly Detection gratuito | [Outras ferramentas](../../servicos/custos/pricing-calculator-cur-e-outras-ferramentas.md) |
| 7 | Lista oficial de tarefas exclusivas do root (ver correção acima) | [2.2](../02-seguranca-e-conformidade/02-usuario-root.md) |
| 8 | MFA: passkeys/FIDO2, app virtual, token TOTP; até 8 dispositivos | [IAM](../../servicos/seguranca/iam.md) |
| 9 | CloudTrail: data events desativados por padrão; uma cópia de management events grátis; validação de integridade; Event history de 90 dias | [CloudTrail](../../servicos/gerenciamento/cloudtrail.md) |
| 10 | Security Hub: FSBP, CIS, PCI DSS, NIST 800-53 Rev. 5, Resource Tagging | [Security Hub](../../servicos/seguranca/security-hub.md) |
| 11 | GuardDuty: AI Protection e Malware Protection para Backup | [GuardDuty](../../servicos/seguranca/guardduty.md) |
| 12 | Política de pentest: serviços liberados, C2 exige aprovação, atividades proibidas, simulação de DDoS | [2.10](../02-seguranca-e-conformidade/10-outros-pontos-de-seguranca.md) |
| 13 | S3: SSE-S3, Block Public Access e ACLs desativadas por padrão desde 2023 | [S3](../../servicos/armazenamento/s3.md) |
| 14 | Intelligent-Tiering: 30 e 90 dias, camadas opcionais, < 128 KB não monitorado (ver correção acima) | [Classes do S3](../../servicos/armazenamento/s3-classes-de-armazenamento.md) |
| 15 | Storage Gateway: FSx File Gateway descontinuado para novos clientes | [Storage Gateway](../../servicos/armazenamento/storage-gateway.md) |
| 16 | Gateway endpoints sem custo; Site-to-Site VPN com 2 túneis | [VPN](../../servicos/redes/site-to-site-vpn-e-client-vpn.md) |
| 17 | Políticas do Route 53 | [Route 53](../../servicos/redes/route-53.md) |
| 18 | RDS: Db2; Multi-AZ DB cluster com 1 writer e 2 readers (MySQL, PostgreSQL) | [RDS](../../servicos/banco-de-dados/rds.md) |
| 19 | WorkSpaces Secure Browser (05/2024); Amazon DCV | [WorkSpaces](../../servicos/aplicacoes/workspaces-e-appstream.md) |
| 20 | Shield SRT com Business Support+, Enterprise ou Unified Operations | [Shield](../../servicos/seguranca/shield.md) |
| 21 | Glacier Flexible Expedited: 1–5 min para objetos < 250 MB | [Classes do S3](../../servicos/armazenamento/s3-classes-de-armazenamento.md) |
| 22 | CloudFront: OAC recomendado (OAI legado); Functions × Lambda@Edge | [CloudFront](../../servicos/redes/cloudfront.md) |
| 23 | EFS: Elastic é o padrão; classes Standard, IA e Archive | [EFS](../../servicos/armazenamento/efs.md) |
| 24 | Aurora Serverless v2 com auto-pause até 0 ACU | [Aurora](../../servicos/banco-de-dados/aurora.md) |
| 25 | RCPs; SCP padrão (após 10/07/2026) nega sair da organização e fechar a conta | [Organizations](../../servicos/gerenciamento/organizations.md) |
| 26 | CodeWhisperer → Amazon Q Developer (30/04/2024); Bedrock não usa dados do cliente nos modelos base | [Amazon Q](../../servicos/ia-ml/amazon-q.md), [Bedrock](../../servicos/ia-ml/bedrock.md) |
| 27 | Elastic Disaster Recovery: RPO subsegundo, RTO em minutos | [DRS](../../servicos/armazenamento/elastic-disaster-recovery.md) |
| 28 | Snowball Edge: 210 TB e 104 vCPUs; fim do suporte comercial em 31/12/2026 | [Snow Family](../../servicos/migracao/snow-family.md) |
| 29 | WorkDocs encerrado em 25/04/2025; Snowmobile em 14/03/2024 | [Fora do escopo](../../servicos/fora-do-escopo/desenvolvimento-e-aplicacoes.md), [Snow Family](../../servicos/migracao/snow-family.md) |
| 30 | Enterprise inclui workshops com o TAM e AWS GameDays | [Planos de suporte](../../servicos/custos/planos-de-suporte.md) |
