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

**Passo 1.** Identifique se precisa ligar redes ou permitir acesso de dispositivos de usuários.

**Passo 2.** Prepare a modalidade de VPN correspondente, autenticação quando aplicável e rotas para os recursos necessários.

**Passo 3.** Verifique comunicação e permissões. Um túnel protegido não torna toda aplicação automaticamente acessível.

## 2. Recursos e opções, com significado

### AWS Site-to-Site VPN

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

VPN gerenciada (baseada em OpenVPN) para **usuários remotos** (notebooks) acessarem VPCs e redes on-premises.

Autenticação por certificados, Active Directory ou SAML; escala automaticamente.

Pago por associação de subnet-hora + conexão-hora.

### Comparação

| | Site-to-Site VPN | Client VPN | Direct Connect |
|---|---|---|---|
| Quem conecta | Rede inteira | Usuários individuais | Rede inteira |
| Meio | Internet (IPsec) | Internet (TLS) | Link físico dedicado |
| Criptografado | ✅ | ✅ | ❌ por padrão |
| Tempo de setup | Minutos | Minutos | Semanas |
| Desempenho | Variável | Variável | Consistente |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

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
