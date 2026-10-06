# AWS VPN (Site-to-Site VPN e Client VPN)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa precisa conectar sua rede à AWS, ou permitir que uma pessoa trabalhando remotamente acesse recursos privados.

**Como este serviço ajuda?** Site-to-Site VPN liga redes por um túnel criptografado. Client VPN permite acesso remoto de dispositivos de usuários, conforme autenticação e configuração.

**Exemplo do dia a dia:** A sede usa Site-to-Site VPN para se conectar à AWS. Uma funcionária remota pode usar Client VPN para acessar recursos autorizados.

**O que ele não resolve sozinho?** VPN não é um circuito físico dedicado nem torna todo usuário autorizado a tudo. Rotas, identidade e controles de acesso continuam necessários.

**Primeiras palavras para entender:**

- **VPN:** conexão lógica protegida.
- **Túnel:** caminho de comunicação encapsulado.
- **Criptografado:** protegido para impedir a leitura por quem não tem autorização.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Rede / conectividade híbrida · **Domínio:** 3 · **Escopo:** Regional · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)
>
> **Em uma frase:** túneis criptografados (IPsec/TLS) pela internet para ligar redes ou usuários à sua VPC.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **VPN:** Conexão lógica protegida que liga usuários ou redes. Um túnel VPN não concede automaticamente acesso a todos os recursos do destino.
- **autenticação:** Verificação de quem está acessando. Confirmar a identidade não autoriza qualquer ação no sistema.

**Passo 1.** Identifique se precisa ligar redes ou permitir acesso de dispositivos de usuários.

**Passo 2.** Prepare a modalidade de VPN correspondente, autenticação quando aplicável e rotas para os recursos necessários.

**Passo 3.** Verifique comunicação e permissões. Um túnel protegido não torna toda aplicação automaticamente acessível.

## 2. Recursos e opções, com significado

### AWS Site-to-Site VPN

**Antes de ler este trecho:**

- **VPC:** A VPC é uma rede virtual isolada logicamente para seus recursos.
- **Direct Connect:** Direct Connect permite estabelecer essa conectividade por conexões e locais compatíveis, com interfaces e rotas configuradas para o ambiente.
- **Global Accelerator:** Global Accelerator usa a rede global da AWS para encaminhar tráfego a destinos compatíveis, considerando configuração e saúde desses destinos.
- **Connect:** Amazon Connect oferece uma plataforma de contact center em nuvem com canais e recursos compatíveis.
- **datacenter:** Instalação física com equipamentos de computação, rede, energia e refrigeração. A nuvem continua dependendo desses equipamentos, mas o cliente não precisa manter o prédio.
- **virtual:** Um recurso virtual é criado por software sobre equipamentos físicos. VM significa máquina virtual: computador lógico com sistema operacional e recursos de processamento.
- **throughput:** Quantidade de dados ou de trabalho processada por unidade de tempo. É diferente de latência, que mede quanto uma operação demora.
- **global:** Alcance que não se limita ao gerenciamento de uma única região. Isso não significa que cada dado foi automaticamente copiado para todo o mundo.
- **redundância:** Existência de componentes alternativos. Duas cópias só ajudam se forem utilizáveis na falha que você pretende enfrentar.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **IP:** Endereços usados para identificar interfaces e destinos na rede. IPv4 e IPv6 são versões diferentes; ter um endereço não concede permissão nem garante uma rota.
- **firewall:** Controle que permite ou bloqueia comunicação segundo regras. Sua cobertura depende da camada e do ponto em que é aplicado.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.
- **BGP:** Protocolo para troca de informações de rotas entre redes. A conexão física ainda precisa das interfaces e configurações apropriadas.
- **VGW:** Virtual Private Gateway: componente de conectividade associado a uma VPC em cenários compatíveis de ligação com outras redes.

| Item | Detalhe |
|---|---|
| **Objetivo** | Ligar o **datacenter/escritório** à VPC por **IPsec pela internet**. |
| **Componentes** | **Customer Gateway** (seu roteador/firewall) ↔ **Virtual Private Gateway** (na VPC) ou **Transit Gateway**. |
| **Redundância** | ✔️ Cada conexão tem **2 túneis**, cada um com IP público próprio, terminando em AZs distintas; configure os dois. |
| **Roteamento** | Estático ou dinâmico (**BGP**). |
| **Accelerated VPN** | Usa a rede do Global Accelerator para melhor desempenho. |
| **VPN CloudHub** | Vários escritórios se comunicam via o mesmo VGW (hub-and-spoke). |
| **VPN sobre Direct Connect** | Criptografia ponta a ponta no link dedicado. |
| **Prazo** | **Minutos** para configurar. |
| **Limite** | 🧊 Throughput por túnel limitado (≈1,25 Gbps); depende da qualidade da internet. |

### AWS Client VPN

**Antes de ler este trecho:**

- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.

VPN gerenciada (baseada em OpenVPN) para **usuários remotos** (notebooks) acessarem VPCs e redes on-premises.

**Antes de ler este trecho:**

- **SAML:** Padrões de integração de identidade entre sistemas. Permitem que uma aplicação ou serviço confie em informações fornecidas por um provedor de identidade compatível.
- **Active Directory:** Tecnologia de diretório para identidades, computadores e controles corporativos. É diferente do cadastro de clientes de uma aplicação pública.

Autenticação por certificados, Active Directory ou SAML; escala automaticamente.

Pago por associação de subnet-hora + conexão-hora.

### Comparação

**Antes de ler este trecho:**

- **TLS:** HTTPS usa TLS para proteger a conexão web. TLS é a tecnologia atual de proteção; SSL aparece como nome histórico. Essa proteção do caminho é diferente de criptografar dados armazenados.

| | Site-to-Site VPN | Client VPN | Direct Connect |
|---|---|---|---|
| Quem conecta | Rede inteira | Usuários individuais | Rede inteira |
| Meio | Internet (IPsec) | Internet (TLS) | Link físico dedicado |
| Criptografado | ✅ | ✅ | ❌ por padrão |
| Tempo de setup | Minutos | Minutos | Semanas |
| Desempenho | Variável | Variável | Consistente |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

**Antes de ler este trecho:**

- **identidade:** Quem realiza uma ação: pessoa, programa ou sessão. Identificar o autor é diferente de decidir se a ação está autorizada.

VPN não é um circuito físico dedicado nem torna todo usuário autorizado a tudo. Rotas, identidade e controles de acesso continuam necessários.

## 4. Caso resolvido: ligando as peças

A sede usa Site-to-Site VPN para se conectar à AWS. Uma funcionária remota pode usar Client VPN para acessar recursos autorizados.

**Aplicando a sequência à situação:**

**Etapa 1:** Identifique se precisa ligar redes ou permitir acesso de dispositivos de usuários.
**Etapa 2:** Prepare a modalidade de VPN correspondente, autenticação quando aplicável e rotas para os recursos necessários.
**Etapa 3:** Verifique comunicação e permissões. Um túnel protegido não torna toda aplicação automaticamente acessível.

**Resultado e responsabilidade:** Site-to-Site VPN liga redes por um túnel criptografado. Client VPN permite acesso remoto de dispositivos de usuários, conforme autenticação e configuração.

**Recursos envolvidos:** Túneis Site-to-Site entre redes; endpoint Client VPN para usuários.

**Decisões que precisam ser tomadas:** Endereços, autenticação, rotas e regras de autorização.

**Antes de ler este trecho:**

- **autorização:** Decisão sobre o que uma identidade pode fazer em um recurso. Essa decisão depende das regras e do contexto da solicitação.

**Outra situação comentada:** Filial inteira: Site-to-Site VPN; funcionário remoto individual: Client VPN.

**Por que não concluir mais do que isso:** Não torna toda rede acessível sem rotas e autorização; Site-to-Site não é cliente remoto individual

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Conexão criptografada com o datacenter, pronta hoje."

**Resposta curta:** Site-to-Site VPN.

**Pergunta:** "Funcionários em casa precisam acessar a VPC."

**Resposta curta:** Client VPN.

**Pergunta:** "Backup barato do Direct Connect."

**Resposta curta:** Site-to-Site VPN.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) · [Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
