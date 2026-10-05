"""Definições autorais para leitura local; não substituem configurações do serviço.

Vocabulário fundamental e traduções usados antes do conteúdo que depende deles.
As capacidades específicas continuam no conteúdo-base e nas fontes de cada ficha.
"""
import re
from functools import lru_cache


def carregar(texto):
    termos = {}
    for linha in texto.strip().splitlines():
        nome, explicacao = [p.strip() for p in linha.split('|', 1)]
        for alias in nome.split(' / '):
            termos[alias.casefold()] = (alias, explicacao)
    return termos


TERMOS = carregar("""
AWS | Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
API | Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
recurso | Algo criado ou administrado num serviço, como uma máquina, um bucket ou uma tabela. Criar um recurso não é o mesmo que contratar toda uma aplicação pronta.
servidor | Computador que atende pedidos de outros computadores. Um servidor web, por exemplo, responde aos pedidos enviados pelo navegador.
sistema operacional / SO | Software básico da máquina, como Linux ou Windows. Ele administra arquivos, memória e execução de programas; atualizar esse software é diferente de atualizar a aplicação.
datacenter | Instalação física com equipamentos de computação, rede, energia e refrigeração. A nuvem continua dependendo desses equipamentos, mas o cliente não precisa manter o prédio.
virtual / VM | Um recurso virtual é criado por software sobre equipamentos físicos. VM significa máquina virtual: computador lógico com sistema operacional e recursos de processamento.
CPU / vCPU | CPU é o processador que executa instruções. vCPU é a unidade de processamento virtual apresentada ao ambiente. Mais processamento não resolve automaticamente falta de memória ou de velocidade do disco.
memória / RAM | Memória é a área de trabalho rápida dos programas; em hardware, RAM nomeia esse tipo de memória. AWS RAM, por outro lado, é Resource Access Manager, para compartilhar recursos compatíveis. O contexto distingue os dois sentidos.
GPU | Processador especializado em executar muitos cálculos em paralelo. Pode atender gráficos e determinadas tarefas de aprendizado de máquina; não é necessário para todo programa.
ARM | Família de arquitetura de processadores. O software precisa ser compatível com a arquitetura escolhida; não basta comparar a quantidade de processadores.
IOPS | Quantidade de operações de leitura e escrita por segundo. Ajuda a descrever o comportamento de um armazenamento, mas não mede sozinha a quantidade de bytes transferidos.
throughput | Quantidade de dados ou de trabalho processada por unidade de tempo. É diferente de latência, que mede quanto uma operação demora.
latência | Tempo de uma comunicação ou operação. Um pedido individual pode demorar mesmo quando o sistema consegue processar muitos pedidos por segundo.
HPC | Computação de alto desempenho: execução de cálculos intensivos, como simulações. O requisito concreto pode envolver processamento, comunicação ou outro recurso.
SSD | Tipo de armazenamento sem partes mecânicas, usado para acesso rápido a dados. A escolha de um volume também envolve sua capacidade e limites de desempenho.
GB / MB / KB / TB / PB | Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.
GiB / MiB / KiB / TiB | Unidades em escala binária: cada nível corresponde a 1.024 do anterior. MiB e MB não são a mesma unidade; preserve a unidade indicada pelo serviço.
segundo / minuto / hora | Unidades de tempo. Em cobrança, tempo de recurso provisionado pode importar mesmo sem usuários acessando; em recuperação, tempo representa a espera para voltar a usar algo.
região | Área geográfica AWS que contém zonas de disponibilidade. Muitos recursos são criados numa região específica; mudar de região pode exigir criar ou copiar recursos.
AZ / zona de disponibilidade | Parte isolada da infraestrutura dentro de uma região, formada por um ou mais datacenters. Distribuir recursos entre zonas pode reduzir o impacto de uma falha localizada.
Multi-AZ | Configuração que utiliza mais de uma zona de disponibilidade. Seu comportamento depende do serviço: não presuma que toda cópia atende leituras ou que isso é backup de dados apagados.
Multi-Region | Uso de mais de uma região. Replicação, comunicação e recuperação entre regiões exigem configuração e podem ter custos próprios.
edge location / ponto de presença | Local de infraestrutura usado para aproximar determinadas funções dos usuários, como entrega de conteúdo. Não é uma região completa com todos os serviços.
regional | O recurso ou a operação pertence a uma região. Serviços globais podem administrar objetos regionais; leia o alcance do recurso, não apenas o nome do serviço.
global | Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.
provisionar | Criar ou disponibilizar capacidade e recursos. Um recurso provisionado pode ter cobrança mesmo enquanto está esperando trabalho.
gerenciado | Parte da operação é realizada pelo provedor. O cliente continua responsável pelas decisões e camadas não incluídas nessa administração.
serverless | Modelo em que o cliente não administra diretamente os servidores da execução. Os servidores existem e há cobrança, configuração e limites.
IaaS | Infraestrutura como serviço: você obtém recursos como uma máquina virtual e administra o sistema operacional e o software instalado.
PaaS | Plataforma como serviço: parte da infraestrutura e do ambiente de execução é administrada para você entregar a aplicação. O código e suas regras continuam sendo do cliente.
SaaS | Software como serviço: aplicação pronta disponibilizada para uso. O cliente administra seu uso e seus dados conforme a oferta, em vez de construir o software do zero.
on-premises | Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.
híbrido | Combinação de ambiente próprio e nuvem. É necessário definir quais partes ficam em cada lado e como se comunicam.
workload / carga | Aplicação ou conjunto de tarefas com seus recursos e necessidades. Avaliar uma carga significa avaliar o trabalho completo, não uma única máquina isolada.
quota | Limite de uso de um serviço ou recurso. Algumas quotas podem ser aumentadas mediante solicitação; limite não significa capacidade já reservada.
capacidade | Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
escalabilidade | Capacidade de aumentar o atendimento. Crescer uma máquina é escala vertical; acrescentar máquinas é escala horizontal.
elasticidade | Ajuste da capacidade para crescer e reduzir conforme a necessidade, dentro das regras e dos limites da solução.
alta disponibilidade | Planejamento para manter o sistema acessível diante de determinadas falhas. Não é promessa de ausência de qualquer interrupção.
resiliência | Capacidade de resistir e recuperar-se de falhas. Requer escolher quais falhas serão tratadas e como a operação continuará.
redundância | Existência de componentes alternativos. Duas cópias só ajudam se forem utilizáveis na falha que você pretende enfrentar.
backup | Cópia de segurança para recuperação. Ter uma cópia não mantém, por si só, a aplicação funcionando durante um incidente.
snapshot | Cópia de estado de um recurso em determinado momento, conforme o serviço. Restauração pode criar um novo recurso; não presuma uma máquina pronta e instantânea.
replicação | Manutenção de uma cópia dos dados em outro recurso. Se uma alteração incorreta for replicada, a cópia também pode recebê-la; replicação não substitui todo backup.
retenção | Tempo durante o qual dados ou registros são conservados. Depois desse prazo, o comportamento depende das regras do serviço e das configurações.
RTO | Objetivo de tempo de recuperação: quanto tempo a organização aceita ficar sem o sistema após uma interrupção.
RPO | Objetivo de ponto de recuperação: quanto histórico de dados a organização aceita perder, medido como intervalo de tempo.
DR | Recuperação de desastres: plano para recuperar uma operação depois de uma interrupção grave. Inclui recursos, procedimentos e testes.
failover | Mudança do atendimento para um componente alternativo quando o principal fica indisponível. A forma e o tempo dependem da solução.
failback | Retorno planejado ao ambiente principal depois de uma recuperação. Não deve ser confundido com simplesmente criar uma cópia de dados.
ativo-passivo / active-passive | Um ambiente atende normalmente e outro fica preparado para assumir. O preparo da alternativa pode variar bastante.
ativo-ativo / active-active | Mais de um ambiente atende ao mesmo tempo. Isso exige tratar distribuição de tráfego e consistência dos dados conforme a aplicação.
pilot light | Estratégia de recuperação que mantém uma base essencial ativa e amplia os demais recursos quando necessário. É mais que apenas guardar um backup.
warm standby | Ambiente alternativo reduzido já em execução, que pode ser ampliado na recuperação. O objetivo é reduzir preparação depois da falha.
rede | Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
IP / IPv4 / IPv6 | Endereços usados para identificar interfaces e destinos na rede. IPv4 e IPv6 são versões diferentes; ter um endereço não concede permissão nem garante uma rota.
porta | Número que ajuda a identificar o serviço de destino de uma comunicação. Liberar uma porta autoriza tráfego segundo a regra, mas não configura a aplicação para responder.
protocolo | Conjunto de regras da comunicação. Um protocolo define o formato e o comportamento da troca; produtos precisam ser compatíveis com ele.
TCP | Protocolo de transporte orientado a conexão, com mecanismos de entrega e ordem. É usado por muitas aplicações; não acrescenta criptografia por si só.
UDP | Protocolo de transporte por datagramas, sem as mesmas garantias de entrega e ordem do TCP. A aplicação precisa lidar com os requisitos que o protocolo não fornece.
HTTP | Protocolo de pedidos e respostas usado na web. Uma URL e um método indicam a operação; HTTP sozinho não protege o conteúdo por criptografia.
HTTPS / TLS / SSL | HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.
DNS | Sistema que relaciona nomes a informações de endereço e outros registros. Resolver o nome de um site não hospeda o site nem garante que ele está funcionando.
URL | Endereço usado para acessar um recurso. Uma URL pode incluir domínio, caminho e parâmetros; possuir o endereço não significa ter autorização.
CIDR | Notação de faixa de endereços de rede, como um endereço acompanhado de /24. A faixa define um conjunto de endereços, não uma senha ou uma permissão.
subnet | Segmento de uma rede virtual. Na VPC, uma subnet pertence a uma zona de disponibilidade; suas rotas e controles ajudam a definir a conectividade.
route table / tabela de rotas | Conjunto de regras que indica para onde encaminhar tráfego destinado a determinadas faixas. A rota é parte do caminho, não uma autorização de identidade.
IGW / Internet Gateway | Componente que permite conectividade da VPC com a internet conforme as rotas, endereços e controles usados. Não torna todo recurso público automaticamente.
NAT | Tradução de endereços de rede. Um NAT Gateway pode permitir conexões de saída de determinados recursos privados sem oferecer entrada direta iniciada pela internet.
SG / security group | Regras de tráfego associadas a interfaces ou recursos compatíveis. É um controle de rede, não uma permissão IAM para ler um arquivo ou chamar uma API.
stateful | Controle que acompanha o estado da comunicação e trata respostas conforme esse estado. No security group, isso evita exigir uma regra independente para a resposta de uma conexão permitida.
stateless | Controle que avalia cada direção sem manter o mesmo estado de conexão. Regras de ida e de volta precisam ser consideradas separadamente.
ACL / NACL / Network ACL | ACL significa lista de controle de acesso. A NACL da VPC controla tráfego no segmento de rede; ACL de armazenamento tem outro contexto. Não trate as duas como a mesma função.
firewall | Controle que permite ou bloqueia comunicação segundo regras. Sua cobertura depende da camada e do ponto em que é aplicado.
endpoint | Ponto de acesso a um serviço ou componente. Pode ser um endereço de API ou um recurso de conectividade; identifique qual sentido a seção usa.
VPN | Conexão lógica protegida que liga usuários ou redes. Um túnel VPN não concede automaticamente acesso a todos os recursos do destino.
SFTP / FTP / FTPS | Protocolos de transferência de arquivos. SFTP usa SSH; FTP não fornece a mesma proteção; FTPS adiciona TLS ao FTP. São opções de compatibilidade diferentes.
SSH | Protocolo para acesso remoto protegido, comum na administração de Linux. Permissão para conectar pela rede e autorização para entrar no sistema são coisas diferentes.
RDP | Protocolo para acesso remoto a um ambiente gráfico, comum no Windows. Acesso exige configuração de rede e autenticação do sistema.
NFS / SMB / POSIX | NFS e SMB são protocolos para acesso a arquivos compartilhados. POSIX descreve interfaces e comportamentos de sistemas. Compatibilidade importa para a aplicação usar os arquivos corretamente.
iSCSI | Protocolo para apresentar armazenamento em blocos pela rede. É diferente de acessar objetos por uma API ou arquivos por um compartilhamento.
CDN | Rede de distribuição de conteúdo. Ela aproxima entrega de conteúdo dos usuários e pode manter cópias em cache conforme as regras.
cache | Cópia mantida para reutilização rápida. A aplicação ou o serviço precisa decidir atualização e validade, para não servir conteúdo inadequado ou antigo.
TTL | Tempo de vida de uma informação. Em DNS pode orientar cache; em um banco pode indicar expiração de itens. O efeito concreto depende do serviço.
origem | Local de onde uma distribuição obtém conteúdo, como um servidor ou bucket. Uma cópia em cache não elimina toda necessidade de acessar a origem.
load balancer / balanceador / ELB / LB | Recurso que distribui tráfego entre destinos configurados. Ele não cria sozinho todas as máquinas necessárias nem conserta seu programa.
ALB / NLB / GWLB | Modalidades de balanceador com focos diferentes: aplicação, transporte de rede e integração de equipamentos virtuais. Os protocolos e casos de uso determinam a escolha.
listener | Configuração que recebe conexões em uma porta e protocolo. No balanceador, ela participa da decisão de encaminhamento para destinos.
target group | Grupo de destinos do balanceamento, com configurações como verificações de saúde. Destino saudável não significa que toda regra de negócio está correta.
health check | Teste de resposta usado para avaliar um destino. O teste e os limites precisam refletir a função observada; não equivale a uma investigação completa da aplicação.
WebSocket | Comunicação que mantém uma conexão para troca de mensagens entre cliente e servidor. É diferente de uma sequência de pedidos web independentes.
REST | Estilo de API que usa recursos e operações, frequentemente por HTTP. O código integrado continua sendo responsável pelo comportamento da aplicação.
JSON / YAML / XML | Formatos de representação de dados e configurações. Um arquivo nesses formatos descreve informações; ele não cria permissões nem recursos sem ser usado por uma ferramenta.
IAM | Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
identidade | Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.
autenticação | Verificação de quem está acessando. Confirmar a identidade não autoriza qualquer ação no sistema.
autorização | Decisão sobre o que uma identidade pode fazer em um recurso. Essa decisão depende das regras e do contexto da solicitação.
credenciais | Informações usadas para comprovar ou representar uma identidade. Credenciais temporárias expiram; credenciais de longa duração precisam de proteção e administração.
role / função IAM | Papel que fornece permissões a uma sessão que o assume. O termo função IAM não significa um trecho de código como uma função Lambda.
policy / política | Documento ou regra que define permissões, limites ou comportamento. O contexto identifica se é uma política de identidade, de recurso ou de outra função.
ARN | Identificador de um recurso AWS. Ajuda políticas e integrações a indicar exatamente o recurso; não é uma credencial de acesso.
STS | Serviço que fornece credenciais temporárias AWS. Essas credenciais permitem uma sessão autorizada dentro das permissões aplicáveis.
MFA | Verificação adicional de autenticação, além da primeira credencial. Ela protege a entrada, mas não concede permissões por si só.
SSO | Uma entrada para vários ambientes autorizados. O usuário ainda recebe acessos definidos para cada ambiente.
SAML / OIDC | Padrões de integração de identidade entre sistemas. Permitem que uma aplicação ou serviço confie em informações fornecidas por um provedor de identidade compatível.
JWT | Formato de token com informações verificáveis. Receber um token não dispensa validar sua origem, condições e permissões na aplicação.
federação | Uso de uma identidade de um provedor em outro ambiente por uma relação de confiança. Não significa que todos os usuários passam a ser administradores.
menor privilégio | Conceder apenas o acesso necessário ao trabalho. Evita que uma tarefa simples carregue poder desnecessário sobre outros recursos.
root | Na conta AWS, é a identidade principal com poderes especiais. Dentro de Linux, root é o administrador do sistema operacional. Administrar Linux não é o mesmo que administrar a conta AWS.
SCP | Política de controle de serviços usada na organização para limitar permissões disponíveis em contas às quais se aplica. Ela não concede acesso ao usuário sozinha.
RCP | Política de controle de recursos que limita permissões aplicáveis a recursos compatíveis da organização. É um limite, não uma concessão isolada de acesso.
OU | Unidade organizacional: agrupamento de contas na organização. Agrupar contas permite aplicar regras de governança segundo a estrutura escolhida.
landing zone | Base organizada de um ambiente AWS com várias contas e controles. Ainda é necessário definir aplicações, acessos e operação dentro dela.
RBAC | Controle de acesso baseado em papéis. As permissões dependem do papel atribuído à identidade e das regras do sistema.
AD / Active Directory | Tecnologia de diretório para identidades, computadores e controles corporativos. É diferente do cadastro de clientes de uma aplicação pública.
KMS | Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.
HSM | Equipamento especializado em proteger chaves e executar operações criptográficas. A forma de administração depende da solução escolhida.
ACM / CA | ACM administra certificados em integrações compatíveis. CA significa autoridade certificadora, responsável por emitir certificados sob suas regras.
AES-256 | Algoritmo de criptografia com chave de 256 bits. Esse nome descreve a tecnologia de proteção; autorização e administração das chaves continuam necessárias.
SSE-S3 / SSE-KMS / SSE-C / DSSE-KMS | Formas de criptografia no servidor do S3, que diferem na origem e administração das chaves e, no último caso, nas camadas. A tabela da seção distingue essas escolhas.
client-side | Ação realizada no lado do cliente. Em criptografia, significa proteger os dados antes de enviá-los ao serviço; o cliente precisa administrar sua parte do processo.
WORM | Escrever uma vez e ler muitas vezes: modelo de retenção que impede alterações ou exclusões conforme o mecanismo e o modo aplicáveis.
compliance / conformidade | Atendimento a requisitos definidos. Usar um serviço com certificações não torna automaticamente a aplicação do cliente conforme.
PII | Informação que pode identificar uma pessoa. Sua identificação ajuda a planejar proteção de dados, mas não substitui avaliação do contexto e das regras aplicáveis.
DDoS | Ataque distribuído que tenta sobrecarregar um serviço e impedir seu uso legítimo. É diferente de tentar explorar um campo vulnerável de um programa.
XSS | Ataque que busca executar conteúdo indevido no contexto de uma página acessada pelo usuário. Regras de proteção e correções do código atendem partes desse risco.
SQL injection | Tentativa de manipular comandos de banco por entradas indevidas. Proteger a entrada não dispensa corrigir como a aplicação constrói e executa consultas.
CVE | Identificador público de uma vulnerabilidade conhecida. Um achado precisa ser avaliado pelo impacto no recurso e pelas correções disponíveis.
CIS / NIST / FIPS / SOC / PCI DSS / HIPAA / GDPR | Referências, padrões ou requisitos de segurança e conformidade com escopos distintos. A menção de um nome não é certificação automática do cliente; identifique qual requisito a seção aborda.
SLA | Acordo de nível de serviço com condições e medidas próprias. Não é garantia de que a aplicação do cliente nunca falhará.
log | Registro de acontecimentos para análise. A aplicação e os serviços podem produzir registros diferentes; é necessário definir coleta, retenção e acesso.
métrica | Medida observada ao longo do tempo, como utilização ou número de erros. O número precisa de unidade, período e contexto para ter significado.
alarme | Condição acompanhada sobre dados de monitoramento. Uma mudança de estado pode gerar ações configuradas; o alarme não diagnostica todo problema sozinho.
trace | Rastreamento do caminho de uma requisição em componentes instrumentados. Permite examinar etapas, mas depende dos dados emitidos pela aplicação.
instrumentação | Preparação do software para emitir informações de observação. Sem os dados necessários, a ferramenta não consegue mostrar todos os detalhes da execução.
sampling | Amostragem: observar parte das ocorrências. Uma amostra reduz volume, mas não deve ser tratada como o registro completo de cada pedido.
CloudWatch | Ferramentas AWS para métricas, logs e alarmes, conforme a coleta e a configuração. Seu foco é observar comportamento e operação.
CloudTrail | Registro de atividades e chamadas AWS compatíveis. Ajuda a analisar quem realizou uma operação, em vez de medir sozinho a velocidade da aplicação.
Config | Serviço que acompanha configurações e suas avaliações em recursos compatíveis. Observar configuração é diferente de observar uma métrica de desempenho.
SQL | Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.
NoSQL | Família de modelos de banco que não se limita à estrutura relacional tradicional. Não significa ausência de estrutura ou que todo produto NoSQL faz o mesmo trabalho.
OLTP | Processamento de operações individuais do negócio, como registrar uma compra. É diferente de analisar grandes conjuntos históricos de registros.
OLAP | Análise de conjuntos de dados, como comparar vendas de vários meses. Prioriza perguntas e agregações, não apenas registrar uma operação individual.
schema | Estrutura e tipos dos dados. Em migração, adaptar a estrutura é uma tarefa diferente de copiar os registros.
chave primária | Informação que identifica um registro conforme o modelo do banco. O desenho da chave afeta como os dados serão buscados.
partition key / sort key | Chaves de organização dos itens do DynamoDB: a primeira determina agrupamento e distribuição; a segunda, quando usada, ordena itens no grupo.
índice | Estrutura adicional para apoiar consultas. Pode melhorar um padrão de acesso, mas possui condições de atualização, capacidade e custo.
read replica | Cópia de banco que pode atender consultas em cenários suportados. Ela não deve ser confundida com toda modalidade de standby para recuperação.
transação | Conjunto de operações tratado com garantias definidas pelo banco. As garantias e limites variam conforme o serviço e a modalidade.
ACU | Unidade de capacidade de determinadas ofertas Aurora. Ela expressa capacidade conforme a oferta; não é uma contagem de usuários do aplicativo.
RCU / WCU | Unidades de capacidade de leitura e escrita no DynamoDB provisionado. O consumo depende do tamanho e das condições da operação, não apenas do número de visitantes.
DAX | Cache compatível com DynamoDB para determinados acessos. É uma camada de aceleração, não uma cópia independente de qualquer banco.
data warehouse | Ambiente de dados organizado para análise de grandes conjuntos. O modelo e as consultas são orientados a perguntas analíticas.
data lake | Conjunto de dados mantido para usos diversos, frequentemente em armazenamento de objetos. Organização, catálogo e permissões continuam necessários.
ETL | Extrair dados de uma fonte, transformá-los e carregá-los num destino. A regra de transformação deve ser definida de acordo com o significado dos dados.
BI | Análise e apresentação de dados para apoiar decisões. Um painel depende de dados adequados e de uma interpretação correta dos indicadores.
CSV / Parquet / JSON | Formatos de dados com estruturas diferentes. O formato influencia como uma ferramenta lê e processa os arquivos; não muda sozinho o significado dos registros.
streaming | Fluxo contínuo de dados ou mídia. É diferente de esperar um arquivo completo antes de iniciar o trabalho.
Kafka / MSK | Kafka é uma plataforma de fluxo de eventos; MSK é a oferta gerenciada compatível da AWS. A aplicação ainda precisa produzir e consumir os registros.
shard | Divisão de um conjunto ou fluxo para organizar armazenamento ou capacidade. O significado e os limites precisam ser lidos no serviço específico.
producer / produtor | Componente que envia dados ou mensagens. Enviar uma mensagem não significa que o trabalho correspondente já foi realizado.
consumer / consumidor / worker | Programa que recebe e processa dados ou tarefas. Ele precisa realizar o trabalho e tratar falhas, não apenas receber a mensagem.
FIFO | Primeiro a entrar, primeiro a sair. No SQS, a ordenação considera grupos de mensagens; deduplicação no envio não garante ausência de repetição de efeitos no programa.
visibility timeout | Intervalo em que uma mensagem recebida do SQS fica temporariamente invisível a outros recebimentos. Se ela não for excluída e o prazo terminar, pode voltar a ser recebida.
DLQ / dead-letter queue | Fila separada para mensagens que atingiram condições configuradas de falha. Ajuda a isolar e investigar o problema; não corrige a mensagem automaticamente.
long polling / short polling | Formas de consultar mensagens: a consulta longa pode esperar por disponibilidade, reduzindo consultas vazias; a curta retorna sem essa mesma espera.
idempotência | Repetir uma operação sem duplicar seu efeito de negócio. Por exemplo, receber novamente o mesmo pedido não deve gerar uma segunda cobrança indevida.
deduplicação | Identificação e tratamento de entradas repetidas conforme um critério e uma janela. É diferente de garantir toda a execução da aplicação apenas uma vez.
retry / retentativa | Nova tentativa após uma falha. Repetir exige considerar o efeito da execução anterior para não duplicar resultados indevidamente.
redrive | Reenvio de mensagens de uma fila de falhas para processamento, conforme o recurso. Antes de reenviar, é necessário entender a causa das falhas.
pub/sub / fan-out | Publicação de uma mensagem para destinatários inscritos. Distribuir avisos a vários destinos é diferente de manter uma tarefa aguardando um consumidor.
pull / push | Em pull, o consumidor busca dados. Em push, o envio é iniciado para o destinatário. A forma de entrega não executa automaticamente a regra de negócio.
broker / MQ | Intermediário de mensagens entre componentes. Sua interface e seus protocolos precisam ser compatíveis com as aplicações conectadas.
evento | Informação sobre algo que aconteceu. Uma regra pode encaminhar o evento; outro componente realiza a ação de negócio.
workflow / state machine | Fluxo de trabalho descrito por etapas, decisões e estados. Coordenar etapas é diferente de escrever o programa que realiza cada tarefa.
timeout | Limite de espera ou duração. Ao excedê-lo, uma operação pode falhar ou exigir tratamento; não presuma que nada aconteceu antes da interrupção.
ML / machine learning | Aprendizado de máquina: modelos ajustados com dados para reconhecer padrões e produzir resultados. A qualidade depende dos dados, método e avaliação.
IA / AI | Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.
modelo | Representação ou base usada para produzir algo. Uma imagem pode ser um modelo de máquina; um modelo de IA é ajustado com dados para gerar resultados. O sentido depende do contexto.
treinamento | Ajuste de um modelo com dados. É uma etapa diferente de utilizar o modelo já treinado para responder a uma nova entrada.
inferência | Uso de um modelo para produzir um resultado com uma nova entrada. Pode acontecer sem um novo treinamento em cada solicitação.
RAG | Recuperar informações de uma fonte e usá-las como contexto de geração. Isso não elimina erros nem autoriza acesso a todos os documentos.
prompt | Instrução e contexto enviados a um modelo generativo. A resposta precisa ser avaliada conforme a finalidade e os dados usados.
MLOps | Práticas para organizar desenvolvimento, implantação e acompanhamento de modelos. Não se resume a treinar uma vez e deixar o modelo sem observação.
container | Ambiente que executa uma aplicação a partir de uma imagem com software e dependências. É diferente de criar uma máquina virtual completa para cada pacote.
imagem | Pacote ou modelo usado para iniciar um ambiente. Em EC2, a AMI é uma imagem de máquina; em containers, a imagem serve para iniciar containers.
Kubernetes | Sistema que coordena containers e mantém o estado de execução desejado. Sua operação exige conceitos e configurações próprios.
cluster | Conjunto de recursos que trabalham de forma coordenada. O termo aparece em computação, banco e outras áreas, com papéis diferentes.
pod | Unidade de execução do Kubernetes que reúne um ou mais containers. Recursos e disponibilidade dependem do ambiente e das configurações.
orquestração | Coordenação de onde e como tarefas ou componentes executam. O coordenador não escreve o conteúdo do trabalho por si só.
control plane / data plane | A camada de controle coordena; a camada de dados executa ou transporta o trabalho. Gerenciar uma não significa administrar automaticamente toda a outra.
AMI | Imagem de máquina EC2: modelo com o software necessário para iniciar uma instância. A imagem precisa ser compatível com a configuração de execução escolhida.
ENI | Interface de rede virtual. Ela associa endereços e configurações de comunicação a recursos compatíveis.
key pair | Par de chaves usado em mecanismos de acesso: uma parte pública e uma privada. A parte privada precisa ser protegida pelo cliente.
user data | Dados ou instruções fornecidos à inicialização da máquina. Um script configurado pode preparar o ambiente; ele não instala qualquer sistema sem você descrever as ações.
instance store | Armazenamento local temporário da máquina física. Não é lugar seguro para a única cópia de dados que precisam sobreviver às ações descritas no ciclo de vida.
instance profile | Forma de associar uma role IAM a uma máquina EC2. A aplicação obtém permissões temporárias em vez de manter chaves fixas no código.
IMDS / IMDSv2 | Serviço de metadados da instância. A versão 2 usa um mecanismo de token; metadados e credenciais devem ser usados conforme as recomendações de segurança.
launch template | Modelo versionado de parâmetros para iniciar máquinas. Facilita repetir configurações; não contém por si só todas as regras da aplicação.
placement group | Forma de organizar posicionamento de instâncias para requisitos específicos de comunicação ou isolamento. Os modos atendem objetivos diferentes.
tenancy | Forma de compartilhamento ou dedicação de infraestrutura física. Uma máquina virtual dedicada e um host físico dedicado têm controles e usos de licença distintos.
On-Demand | Modalidade de uso sem o compromisso de longo prazo descrito por reservas e planos. Cobrança e unidades dependem do recurso contratado.
Spot | Uso de capacidade com possibilidade de interrupção conforme as condições AWS. A tarefa deve poder lidar com interrupção; desconto não remove esse risco.
Reserved Instances / RI | Benefício e condições de reserva para configurações compatíveis. Não confunda desconto com qualquer garantia universal de capacidade.
Savings Plans / SP | Compromisso de gasto por período em troca de condições de preço para uso elegível. Se a necessidade diminuir, o compromisso não desaparece automaticamente.
BYOL | Trazer licença própria elegível. É necessário verificar o direito de uso e as condições do software; a AWS não cria automaticamente essa licença.
TCO | Custo total de propriedade: inclui infraestrutura e operação, não apenas o preço de uma máquina. A comparação depende das hipóteses adotadas.
CapEx / OpEx | Despesa de capital e despesa operacional. Comprar equipamentos antecipadamente e pagar recursos ao longo do uso têm estruturas econômicas diferentes.
rightsizing | Ajustar capacidade à necessidade observada. Reduzir demais pode prejudicar a aplicação; a recomendação precisa ser avaliada pelo uso real.
CI / CD / CI/CD | Integração contínua e entrega ou implantação contínua: práticas para construir, verificar e disponibilizar versões por etapas repetíveis.
build | Processo de preparar uma versão executável da aplicação. Pode compilar, empacotar e executar tarefas configuradas, mas não inventa os testes necessários.
deploy / implantação | Colocar uma versão ou conjunto de recursos em funcionamento. O resultado precisa ser observado e, quando necessário, revertido de modo planejado.
pipeline | Sequência de etapas de um processo. No desenvolvimento, pode conectar construção, testes e entrega; cada etapa tem ações e permissões próprias.
rollback | Retorno a uma configuração ou versão anterior, quando suportado e planejado. Nem toda alteração de dados pode ser desfeita automaticamente.
runtime | Ambiente que executa código de uma linguagem ou plataforma. Compatibilidade de bibliotecas e versões deve ser avaliada.
IDE | Ambiente de desenvolvimento com ferramentas para editar e trabalhar com código. Não é necessariamente o local que hospeda a aplicação em produção.
SDK / CLI | SDK fornece bibliotecas para programas chamarem APIs; CLI fornece comandos de texto. As duas formas continuam exigindo identidade, autorização e configuração.
IaC / CloudFormation | Infraestrutura como código descreve recursos em arquivos. CloudFormation usa templates e stacks para criar e administrar recursos compatíveis.
stack | Conjunto de recursos administrados a partir de uma descrição CloudFormation. Excluir ou atualizar a stack pode afetar os recursos conforme suas políticas.
tag | Par de nome e valor associado a recursos ou objetos compatíveis. Ajuda organização; usos em permissões e cobrança dependem de configuração e suporte.
CDC | Captura de mudanças nos dados para transferi-las ao destino. É diferente de simplesmente copiar uma tabela uma única vez.
SCT | Ferramenta de conversão de estrutura de banco em migrações compatíveis. Nem toda estrutura ou regra da aplicação é convertida automaticamente.
rehost / lift-and-shift | Mover um sistema com poucas mudanças iniciais. A infraestrutura muda, mas isso não moderniza automaticamente o software.
replatform | Mudar parte da plataforma mantendo boa parte da aplicação. Por exemplo, trocar a operação do banco sem reescrever todas as regras do programa.
refactor | Redesenhar partes da aplicação para atender novos objetivos. Pode trazer vantagens, mas demanda mudanças, testes e esforço.
cutover | Momento planejado de trocar o ambiente em uso pelo destino da migração. Requer validar dependências e planejar a transição dos dados.
IoT | Dispositivos físicos conectados que enviam informações ou recebem comandos. Conexão não substitui autenticação, software e análise dos dados.
MQTT | Protocolo de mensagens comum em dispositivos conectados. Aplicação, tópicos e permissões precisam ser definidos para a comunicação desejada.
telemetria | Medidas e informações enviadas por um equipamento ou sistema. Coletar dados é uma etapa diferente de analisá-los ou agir sobre eles.
suporte | Suporte oferece ajuda conforme um plano e suas condições. Um prazo de resposta inicial não é garantia de tempo de resolução de todo incidente.
TAM | Gerente técnico de conta em ofertas de suporte que incluem esse papel. Atua no acompanhamento e orientação previstos; não substitui toda a equipe do cliente.
CUR | Relatório de custos e uso. Ele ajuda a analisar consumo registrado; é diferente de uma estimativa antes de criar recursos.
ETag | Identificador associado a um objeto ou resposta conforme a operação. Não presuma que corresponde sempre ao mesmo algoritmo de resumo de conteúdo.
CORS | Regras de acesso entre origens usadas pelo navegador. Permitir uma origem não substitui a autenticação e a autorização do recurso.
OAC | Controle de acesso à origem em integrações CloudFront compatíveis. Ajuda a restringir acesso direto à origem conforme a configuração.
CRR / SRR | Replicação S3 entre regiões ou na mesma região. Requisitos, objetos abrangidos e permissões precisam ser atendidos.
PUT / GET / DELETE | Nomes comuns de operações: enviar ou gravar, obter e excluir. O significado preciso e as permissões dependem da API usada.
WCU / RCU | Capacidade provisionada de escrita e leitura no DynamoDB. Tamanho do item e condições da operação influenciam consumo; unidades não equivalem diretamente a usuários.
""")


def simples(texto):
    return re.sub(r'[`*_]', '', re.sub(r'\[([^]]+)\]\([^)]+\)', r'\1', texto)).strip()


@lru_cache(maxsize=None)
def padrao(chave, exato=False):
    return re.compile(r'(?<![\w-])'+re.escape(chave)+r'(?![\w-])', 0 if exato else re.I)


def termos_locais(texto, extras=None):
    encontrados = {}
    palavras = set(re.findall(r'\w+', texto.casefold()))
    for chave, (nome, explicacao) in (extras or {}).items():
        primeira = re.findall(r'\w+', chave)[0]
        if primeira in palavras and padrao(nome, True).search(texto):
            encontrados[chave] = (nome, explicacao)
    for chave, par in TERMOS.items():
        primeira = re.findall(r'\w+', chave)[0]
        nome = par[0]
        if primeira in palavras and padrao(nome, nome.isupper()).search(texto):
            encontrados[chave] = par
    # Vários aliases da mesma explicação formam uma entrada, sem repetição.
    grupos = {}
    for nome, explicacao in encontrados.values():
        grupos.setdefault(explicacao, []).append(nome)
    return [(" / ".join(nomes), explicacao) for explicacao, nomes in grupos.items()]


def vocabulario(texto, extras=None):
    encontrados = termos_locais(texto, extras)
    if not encontrados:
        return ''
    return '\n'.join(['**Entenda os termos antes de continuar:**', '',
                     *[f'- **{nome}:** {explicacao}' for nome, explicacao in encontrados], ''])

TERMOS.update(carregar("""
instância | Máquina virtual de um serviço de computação, ou unidade de execução indicada pelo serviço. Em EC2, ela pode estar executando, parada ou em outro estado; não deixa de ser instância ao parar.
bucket | Recipiente que organiza objetos no S3. A aplicação usa o bucket e a identificação do objeto para pedir operações autorizadas.
objeto | Unidade de dados guardada no armazenamento de objetos: conteúdo, identificação e informações associadas. Não é uma máquina nem um programa em execução.
metadados | Informações que descrevem outros dados, como características de um objeto. Conhecer a descrição não significa ler todo o conteúdo.
volume | Disco lógico apresentado a um sistema. Precisa ser preparado para uso; conservar um volume e manter uma máquina executando são decisões diferentes.
chave | Pode indicar identificação de um registro, identificação de um objeto ou elemento criptográfico. Leia o contexto: localizar um dado e protegê-lo são tarefas diferentes.
atributo / campo | Informação nomeada dentro de um registro, como nome ou data. Consultas usam os campos conforme a estrutura e o modelo do banco.
consistência | Garantia sobre o que leituras observam após gravações. Não é o mesmo que durabilidade, nem garante que o dado inserido pelo programa está correto.
durabilidade | Capacidade de preservar os dados armazenados. É diferente de disponibilidade, que trata de conseguir acessá-los quando necessário.
backup and restore | Recuperação baseada em cópias e restauração. Depois da cópia, ainda pode ser necessário criar recursos e preparar o atendimento.
criptografia | Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.
servidor web | Programa ou computador que atende pedidos web. Guardar uma página estática e executar regras de um sistema completo são necessidades distintas.
back-end | Parte que processa regras e dados de uma aplicação. É diferente da interface que a pessoa vê no navegador ou aplicativo.
front-end | Parte da aplicação com que a pessoa interage. Publicá-la não cria automaticamente todas as operações e bancos da parte interna.
site estático | Conteúdo entregue como arquivos, sem executar ali toda uma aplicação de processamento de negócio. Pode integrar-se a outros serviços para funções adicionais.
script | Programa de instruções usado para automatizar tarefas. O script realiza o que foi descrito; não decide sozinho como instalar ou proteger qualquer sistema.
patch | Atualização corretiva de software. A responsabilidade de aplicá-la depende da camada e do serviço usado.
licença | Direito de usar um software sob condições. Instalar o programa ou inventariá-lo não concede automaticamente esse direito.
provisionado | Recurso ou capacidade já disponibilizado para uso. Em algumas cobranças, a disponibilidade mantida importa mesmo sem execução de trabalho de negócio.
legado | Sistema existente com tecnologias ou dependências que precisam ser preservadas ou avaliadas numa mudança. Antigo não significa automaticamente que pode ser desligado.
hypervisor / hipervisor | Camada que permite executar máquinas virtuais sobre equipamentos físicos. No EC2, ela não é administrada pelo cliente como o sistema dentro de sua máquina.
Graviton | Família de processadores AWS baseada em arquitetura ARM. A aplicação e sua imagem precisam ser compatíveis com essa arquitetura.
burstable | Capacidade com comportamento de créditos para atender uso acima de determinada base, conforme a modalidade. Avalie uso sustentado, créditos e cobrança aplicáveis.
SSM | Sigla usada em recursos do Systems Manager. O serviço oferece ferramentas de administração; nós, acessos e conectividade precisam estar preparados.
ASG | Grupo de Auto Scaling: conjunto cuja quantidade e saúde são administradas conforme uma configuração e suas regras.
TGW | Transit Gateway: ponto central para ligações entre redes compatíveis. Rotas e associações determinam a comunicação; criar o ponto não libera tudo automaticamente.
DX | Sigla de Direct Connect, conectividade dedicada com locais e interfaces próprios. Dedicada não equivale automaticamente a criptografada.
VIF | Interface virtual de Direct Connect. Ela organiza acesso conforme a modalidade e os requisitos de rede; não é uma máquina virtual.
LAG | Agrupamento de conexões de rede compatíveis para administração e capacidade. Não elimina a necessidade de planejar resiliência do caminho.
DRS | Sigla usada para Elastic Disaster Recovery. Replicação prepara uma recuperação; testes e dependências continuam necessários.
MGN | Sigla usada para Application Migration Service. Apoia a migração de servidores compatíveis; não reescreve automaticamente a aplicação.
DMS | Database Migration Service: transferência ou replicação de dados entre bancos compatíveis. Conversão de estrutura e ajuste da aplicação são trabalhos relacionados, mas diferentes.
CDK / SAM | Ferramentas de desenvolvimento e descrição de infraestrutura. CDK ajuda a definir recursos por programação; SAM é voltado a aplicações serverless compatíveis.
RUM | Observação da experiência de usuários reais por dados coletados da aplicação. A coleta precisa de integração e deve refletir o que se deseja medir.
IPS | Sistema de prevenção de intrusões. Atua em condições e tráfego compatíveis; não é uma correção automática de todo software vulnerável.
CSPM | Gestão da postura de segurança na nuvem: avaliação e acompanhamento de controles de configuração. Resultado de avaliação não é certificação automática.
DB | Abreviação de database, ou banco de dados. Cada mecanismo oferece formas e garantias próprias de armazenamento e consulta.
DB cluster | Conjunto coordenado de componentes de banco. A função de cada membro e seu comportamento de leitura, escrita ou recuperação dependem do serviço.
GraphQL | Forma de definir uma API e solicitar campos de dados. A aplicação ainda precisa de lógica de resolução, acesso e fontes adequadas.
Apache Spark / Spark | Ferramenta de processamento de dados. O ambiente pode executar o trabalho distribuído, mas a equipe define o código e valida a transformação.
HDFS | Sistema de arquivos distribuído do ecossistema Hadoop. Divide armazenamento entre nós; não é o mesmo modelo de objetos S3.
ONTAP | Tecnologia de armazenamento e gerenciamento de arquivos associada a uma modalidade FSx. A aplicação precisa da compatibilidade e dos recursos daquela modalidade.
Redis / Redis OSS / Valkey / Memcached | Tecnologias de dados em memória com comportamentos e funções diferentes. A modalidade gerenciada deve ser escolhida segundo compatibilidade e necessidade, não apenas pela palavra cache.
SPICE | Mecanismo de dados do QuickSight para consultas e visualizações. Conservação e atualização do conjunto precisam ser planejadas.
SPOT | Modalidade de capacidade com possibilidade de interrupção. Um preço reduzido não garante execução contínua do trabalho.
SWF | Simple Workflow Service: serviço de coordenação de trabalhos distribuídos com modelo próprio. É referência especializada, não sinônimo de todas as ferramentas de fluxo.
SMS | Mensagem de texto para dispositivos móveis. Integrações e condições de envio são diferentes de e-mail e de entrega a uma fila.
APN | Rede de parceiros AWS. Parceiros oferecem serviços e soluções conforme seus próprios contratos e competências.
AMS | Managed Services: oferta de administração operacional conforme cobertura contratada. Não presuma que inclui toda tarefa de qualquer aplicação.
SSE | Criptografia do lado do servidor. O serviço realiza proteção segundo a modalidade escolhida; administração de chaves e autorizações varia.
S3 RTC | Controle de tempo de replicação do S3 com condições específicas. Não é a mesma medida que durabilidade ou tempo de recuperação de um arquivo de archive.
SRT | Protocolo de transporte de mídia. Compatibilidade de transmissão depende do produto e da configuração; não é uma classe de armazenamento.
PDF | Formato de documento. Um serviço de extração analisa conteúdo compatível; guardar um PDF num bucket não executa automaticamente essa análise.
Kafka Connect | Ferramentas de conexão do ecossistema Kafka para fontes e destinos. A integração exige compatibilidade, configurações e controle de acesso.
IAM Identity Center | Serviço de acesso central para a força de trabalho. Atribuições de contas e aplicações não são o cadastro de clientes de um aplicativo.
Parameter Store | Recurso de armazenamento de parâmetros do Systems Manager. É necessário configurar proteção e permissão, inclusive para valores sensíveis.
Permission sets | Conjuntos de permissões atribuídos no IAM Identity Center para acesso às contas. Uma entrada central não transforma toda sessão em administradora.
permissions boundary | Limite de permissões de uma identidade IAM. Ele restringe a concessão efetiva, mas não concede acesso por si só.
Access policy | Política de acesso. O serviço e o tipo de objeto determinam quem é avaliado, quais ações podem ser permitidas e quais limites se aplicam.
service-linked role | Role IAM vinculada a um serviço, com relação e função próprias. Seu uso não elimina a necessidade de controlar quem pode operar o serviço.
tráfego | Comunicações recebidas ou enviadas. O volume, o caminho e o tipo de protocolo podem afetar segurança, desempenho e custo.
job | Trabalho submetido a uma execução. Uma fila ou agendador organiza quando ele roda; seu programa realiza a tarefa.
MessageGroupId / message group | Identificação de grupo usada nas filas FIFO do SQS para a ordenação. Não presuma uma ordem única entre grupos independentes.
longa duração | Trabalho que precisa de execução continuada ou por mais tempo que determinado limite de uma modalidade. Os limites do serviço e o tratamento de falhas devem combinar com o trabalho.
repurchase / retain / retire / relocate | Estratégias de migração: trocar por outra oferta, manter onde está, desativar ou mover a plataforma, respectivamente. A decisão vem do objetivo da aplicação e do negócio.
ESG | Conjunto de aspectos ambientais, sociais e de governança. É uma perspectiva de avaliação organizacional, não uma função de configuração de um recurso.
CAF | Cloud Adoption Framework: orientação para preparar capacidades da organização na adoção de nuvem. Não é uma ferramenta que transfere servidores.
"""))

TERMOS.update(carregar("""
ACID | Garantias de transações: atomicidade, consistência, isolamento e durabilidade. Descrevem comportamentos de operações do banco, não uma função de autenticação.
ABAC | Controle de acesso baseado em atributos, como tags, dentro das condições de políticas compatíveis. Não concede acesso sem regras aplicáveis.
SCIM | Padrão de administração de identidades entre sistemas, como provisionamento de usuários. É diferente do protocolo utilizado para o login.
FIDO2 / TOTP | Mecanismos de autenticação. FIDO2 usa padrões para credenciais com dispositivos ou autenticadores; TOTP é código temporário calculado com base em tempo.
BGP | Protocolo para troca de informações de rotas entre redes. A conexão física ainda precisa das interfaces e configurações apropriadas.
CNAME / A / AAAA / TXT / MX / CAA / SOA | Tipos de registro DNS. A e AAAA indicam endereços, CNAME indica outro nome, MX indica e-mail, TXT texto, CAA emissão de certificados e SOA informações da zona.
FQDN | Nome de domínio completo para identificar um destino. Resolver esse nome continua sendo tarefa DNS; nome não é credencial.
DHCP | Mecanismo para fornecer configuração de rede a dispositivos, como endereços e parâmetros. É diferente de encaminhar tráfego ou autorizar uma chamada AWS.
DKIM / SPF / DMARC | Mecanismos de autenticação e política para e-mail que ajudam a validar origem e tratar mensagens. Não garantem chegada de toda mensagem à caixa principal.
SMTP | Protocolo para envio e transferência de e-mail. Usar o protocolo não dispensa identidade verificada, permissões e regras do serviço de envio.
SNI | Informação de nome enviada no estabelecimento de uma conexão TLS para ajudar a escolher o contexto ou certificado pertinente.
AMQP / STOMP / JMS | Protocolos ou interfaces de mensageria. AMQP e STOMP definem comunicação; JMS é uma interface Java. A aplicação e o broker precisam de suporte compatível.
JDBC | Interface Java para acesso a bancos compatíveis. Um driver faz a integração; conexão e autorização ainda precisam estar corretas.
CQL | Linguagem de consulta associada a Cassandra. Não equivale automaticamente ao conjunto de recursos de SQL de qualquer banco relacional.
RDF / SPARQL | RDF representa informações por relações; SPARQL é uma linguagem de consulta desse modelo. São opções específicas de trabalho com grafos.
GSI / LSI | Índices secundários globais e locais do DynamoDB. Oferecem padrões de consulta adicionais com condições e limites diferentes.
PITR | Recuperação para um ponto no tempo conforme o serviço e a janela configurada. É diferente de manter continuamente uma aplicação alternativa atendendo.
LCU / NLCU / GLCU | Unidades de capacidade usadas por modalidades de balanceadores. A unidade representa dimensões de consumo definidas pela oferta, não uma contagem direta de usuários.
DPU | Unidade de processamento de determinadas ferramentas de dados, como Glue. Consumo e cobrança dependem do trabalho e da modalidade.
RPU | Unidade de capacidade de processamento do Redshift Serverless. Representa capacidade do ambiente, não espaço de armazenamento ou número de pessoas.
DCU | Unidade de capacidade em modalidade serverless de migração de dados. Deve ser interpretada segundo a oferta; não é duração da migração.
DSQL | Nome de uma oferta distribuída de SQL da família Aurora. Sua arquitetura e compatibilidade precisam ser avaliadas separadamente das demais modalidades Aurora.
FSBP | Práticas fundamentais de segurança AWS usadas em avaliações de controles. Um controle aprovado não certifica toda a aplicação.
ASFF / OCSF | Formatos ou esquemas para representar informações de segurança. Padronizar o registro facilita integração, mas não confirma sozinho a natureza do incidente.
SIEM | Ferramentas e processos para reunir e analisar informações de segurança. A qualidade depende das fontes, regras e investigação.
IDS | Sistema de detecção de intrusões. Detectar é diferente de bloquear; o efeito depende da ferramenta e da configuração.
CVSS | Sistema de classificação de gravidade de vulnerabilidades. A prioridade no ambiente também depende de exposição e impacto do recurso.
SBOM | Lista de componentes de software de um pacote ou aplicação. Ajuda a identificar dependências; não corrige automaticamente uma vulnerabilidade.
OWASP | Organização e referências de segurança de aplicações. Listas de riscos ajudam a orientar avaliação, não garantem proteção por si só.
CAPTCHA | Desafio ou mecanismo para diferenciar comportamentos humanos e automatizados. É uma opção de controle, não uma autorização universal para acessar dados.
ATP / ACFP | Recursos de proteção WAF associados a tentativas de tomada de conta e criação fraudulenta de contas. Exigem configuração e contexto de uso compatíveis.
IPAM | Gerenciamento de endereços IP: organização e acompanhamento de faixas e utilização. Não substitui as rotas e os controles de comunicação.
VGW | Virtual Private Gateway: componente de conectividade associado a uma VPC em cenários compatíveis de ligação com outras redes.
GENEVE | Protocolo de encapsulamento de rede usado em integrações compatíveis, como equipamentos com Gateway Load Balancer. Não é uma aplicação de proteção por si só.
IRSA | Associação de roles IAM a contas de serviço Kubernetes em uma forma de integração EKS. Identidade do pod e permissões ainda precisam ser definidas.
CNI / CSI | Interfaces de integração de rede e de armazenamento em ambientes de containers. Seus componentes conectam a execução aos recursos compatíveis.
OCI | Padrões do ecossistema de containers para imagens e execução. Compatibilidade com um formato não garante que qualquer configuração da aplicação funcione.
HDD | Armazenamento por disco mecânico. Seu comportamento difere de SSD; a necessidade de acesso orienta a escolha.
NAS | Armazenamento acessível pela rede como arquivos. É diferente de apresentar um disco em blocos ou objetos por API.
NTFS / ZFS | Tecnologias de sistemas de arquivos com capacidades próprias. A modalidade FSx ou outro ambiente precisa da compatibilidade exigida pela aplicação.
DFS | Tecnologia de organização de arquivos distribuídos em cenários compatíveis. O contexto define como nomes e destinos são apresentados aos clientes.
HANA / SAP | Tecnologias e aplicações empresariais do ecossistema SAP. Podem exigir requisitos específicos de memória, licenciamento e operação.
RHEL | Red Hat Enterprise Linux: distribuição de sistema operacional Linux. Imagem, suporte e licença devem ser avaliados conforme a oferta.
LAMP | Conjunto tradicional de tecnologias para aplicações web: Linux, Apache, banco MySQL e PHP. O pacote não dispensa configuração e manutenção.
PHP | Linguagem de programação usada em aplicações. A plataforma de hospedagem precisa de ambiente compatível para executar seu código.
CMS / CRM / ERP | Tipos de aplicação: gestão de conteúdo, relacionamento com clientes e gestão empresarial. São funções de software, não nomes de um modelo de armazenamento.
KVM | Tecnologia de virtualização associada a Linux. É uma camada de execução de máquinas, não o programa de negócio instalado nelas.
FPGA | Hardware programável para tarefas especializadas. A escolha precisa de software e requisitos compatíveis; não é necessário para todo processamento.
KCL | Biblioteca para desenvolver consumidores de Kinesis. Ela ajuda a processar registros; a aplicação continua definindo o trabalho sobre os dados.
EMRFS | Integração de arquivos de ambientes EMR com S3. O armazenamento de objetos continua tendo interface e comportamento próprios.
ORC | Formato colunar de dados para ferramentas analíticas compatíveis. A organização física do arquivo é diferente do significado de seus campos.
MPP | Processamento paralelo distribuído entre vários recursos. O processo e a distribuição dos dados precisam aproveitar essa arquitetura.
RA3 | Família de nós Redshift com modelo próprio de computação e armazenamento. Avalie capacidade e modalidade, sem tratar o nome como número de visitantes suportados.
MAU | Usuários ativos mensais, uma unidade usada em determinadas cobranças de identidade. A definição de atividade depende da oferta.
NLP | Processamento de linguagem natural: tarefas de análise de texto ou fala. Não significa que um modelo sempre interpreta corretamente qualquer contexto.
A2I | Amazon Augmented AI: integração de revisão humana em tarefas compatíveis. A participação humana é parte de um processo definido, não correção automática de todo resultado.
A2A | Comunicação de agente para agente no contexto de sistemas de IA. O significado e a compatibilidade dependem da integração citada.
A2P | Mensagem de aplicação para pessoa, como envio automatizado de texto. Condições de entrega e cobrança dependem do canal e do serviço.
B2B | Relação entre empresas. Em integração, identifica o contexto dos participantes, não um protocolo único.
BYOD | Uso de dispositivo próprio pelo usuário. Compatibilidade e controles do ambiente remoto continuam necessários.
BYOK / XKS | Trazer chaves próprias e usar armazenamento externo de chaves são opções diferentes de controle criptográfico. Avalie o produto e as condições específicas.
HMAC / RSA / ECC | Tecnologias criptográficas para finalidades próprias. HMAC verifica autenticidade/integridade com chave; RSA e ECC são famílias de criptografia assimétrica. Não são certificados ou políticas de acesso.
PKCS / JCE / CNG / KSP | Padrões e interfaces de integração criptográfica. Cada aplicação precisa de suporte ao mecanismo usado; o nome não concede permissão à chave.
TDE | Criptografia transparente de dados em bancos compatíveis. Proteção do armazenamento não substitui autorização e segurança das consultas.
AWSCURRENT / AWSPREVIOUS | Rótulos de versões de segredos que identificam, respectivamente, a versão atual e a anterior no contexto do Secrets Manager.
ALARM / OK / INSUFFICIENT_DATA | Estados de alarme CloudWatch: condição de alarme, condição normal e falta de dados suficientes. Estado não é diagnóstico completo da causa.
ADOT | Distribuição AWS de OpenTelemetry para instrumentação e coleta de dados de observação compatíveis.
APM | Acompanhamento de desempenho de aplicações. Requer sinais e contexto adequados, não apenas uma métrica isolada de infraestrutura.
CFN | Abreviação usada para CloudFormation. Templates descrevem recursos e stacks administram conjuntos desses recursos.
AFT | Automação de criação e preparação de contas em ambiente Control Tower usando Terraform conforme a solução. Não configura toda aplicação de cada conta.
CIAM | Gestão de identidade e acesso de clientes de aplicações. É uma necessidade diferente da identidade da força de trabalho ou de uma role de servidor.
IVS | Interactive Video Service: serviço associado à transmissão de vídeo. Seus canais e condições precisam ser escolhidos conforme a experiência desejada.
HLS / DASH | Formatos e tecnologias de distribuição adaptativa de vídeo. Permitem alternativas de qualidade e entrega conforme o ecossistema compatível.
VOD / DVR | Vídeo sob demanda e funções de gravação ou acesso temporal de transmissão. São experiências diferentes de simples armazenamento de arquivos.
DRM / SSAI | Proteção de direitos de mídia e inserção de publicidade no servidor. São funções especializadas da distribuição de conteúdo, não controles IAM genéricos.
SSML | Linguagem de marcação para controlar aspectos da síntese de fala em ferramentas compatíveis, como pronúncia e pausas.
SSR | Renderização de páginas no servidor. É diferente de entregar somente arquivos estáticos sem executar essa etapa de aplicação.
URA | Resposta de atendimento por menus ou etapas automatizadas. O fluxo determina como uma pessoa é encaminhada; não substitui todo o atendimento.
VDI / EUC | Infraestrutura de desktops virtuais e computação para usuários finais. São contextos de uso remoto, com modalidades e responsabilidades diferentes.
NICE | Nome associado a tecnologias de transmissão de ambiente ou aplicação remota. A modalidade determina a experiência e os requisitos.
OTA | Atualização enviada remotamente a dispositivos. É necessário preparar compatibilidade, autorização e tratamento de falhas.
ROS | Ecossistema de software para robótica. Não é o sistema operacional de qualquer servidor AWS nem uma ferramenta geral de migração.
O3DE | Motor de desenvolvimento 3D. Desenvolver o conteúdo e operar os recursos necessários são trabalhos diferentes.
VTL | Biblioteca virtual de fitas: interface que apresenta armazenamento como fitas para aplicações compatíveis.
DLM | Data Lifecycle Manager: administração de ciclo de vida de cópias compatíveis de armazenamento. Não é o gerenciador de todo dado da conta.
IEM | Nome histórico de uma oferta de acompanhamento de eventos de infraestrutura. Leia o contexto e a oferta atual indicados na ficha.
FOCUS | Especificação de organização de dados de custos e uso. Padronizar dados ajuda a analisá-los, mas não reduz o gasto automaticamente.
NDA / BAA | Acordos com funções diferentes: confidencialidade e relacionamento associado a requisitos específicos de saúde. Aceitar um documento não torna toda operação conforme.
ISO / LGPD | Referências de padrões e de proteção de dados com finalidades distintas. Identifique o requisito aplicável; o material técnico não substitui uma avaliação de conformidade.
CRM / CAD / EDI | CRM trata relacionamento com clientes; CAD, projeto assistido por computador; EDI, troca eletrônica estruturada de dados. São necessidades de aplicação distintas.
FCM | Firebase Cloud Messaging: canal/ecossistema de mensagens a aplicações compatíveis. Integrações exigem configuração e credenciais próprias.
CPF | Identificador pessoal brasileiro. Neste material é exemplo de dado que pode exigir proteção, não um mecanismo AWS de autenticação.
EPI | Equipamento de proteção individual. Aparece como contexto de análise de imagens, não como nome de um recurso AWS.
AI21 | Nome de um fornecedor de modelos de IA. O acesso e a compatibilidade dependem da oferta indicada, não apenas do nome do fornecedor.
QLDB | Quantum Ledger Database: oferta histórica de registro verificável descrita na ficha de bancos especializados. Confira seu encerramento antes de tratar o exemplo como uma opção atual.
SSE-SQS | Criptografia gerenciada pelo SQS para mensagens. É diferente da modalidade que integra uma chave KMS escolhida segundo a configuração.
AUTH | Abreviação de autenticação ou autorização conforme a interface. Identificar um usuário e permitir uma ação são etapas distintas.
SYN | Sinalização do início de conexão TCP. Ataques que exploram esse fluxo são diferentes de uma consulta de aplicação autorizada.
"""))

# A letra isolada também é artigo em português; AAAA/CNAME já explicam a tabela
# DNS. Só uma expressão explícita deve introduzir a definição desse registro.
TERMOS.pop('a', None)
TERMOS['registro a'] = ('registro A', 'Registro DNS que informa um endereço IPv4 para um nome. Não hospeda a aplicação nesse endereço.')
