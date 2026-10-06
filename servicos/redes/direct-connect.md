# AWS Direct Connect

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa quer uma conexão de rede dedicada entre seu ambiente e a AWS, em vez de depender apenas de um caminho pela internet pública.

**Como este serviço ajuda?** Direct Connect permite estabelecer essa conectividade por conexões e locais compatíveis, com interfaces e rotas configuradas para o ambiente.

**Exemplo do dia a dia:** Uma empresa com tráfego frequente entre seu datacenter e a AWS planeja uma conexão Direct Connect e uma estratégia de contingência.

**O que ele não resolve sozinho?** Dedicada não significa automaticamente criptografada nem sem possibilidade de falha. A proteção dos dados e a redundância precisam ser planejadas.

**Primeiras palavras para entender:**

- **Circuito dedicado:** conexão destinada àquele uso.
- **Datacenter:** local dos servidores.
- **Redundância:** alternativas para continuar operando com falhas.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Rede / conectividade híbrida · **Domínio:** 3 · **Escopo:** Local Direct Connect ↔ regiões · **Tópico do guia:** [3.10 Rede e entrega de conteúdo](../../docs/03-tecnologia-e-servicos/10-rede-e-entrega-de-conteudo.md)
>
> **Em uma frase:** conexão de rede **física, dedicada e privada** entre seu datacenter e a AWS, sem passar pela internet.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Planeje o local e a conexão física compatível com o ambiente da empresa.

**Passo 2.** Configure interfaces e rotas de acesso aos recursos desejados. A comunicação usa a conectividade planejada.

**Passo 3.** Planeje caminhos alternativos e proteção dos dados. Conexão dedicada não significa criptografia automática ou ausência de falhas.

## 2. Recursos e opções, com significado

### Para que serve

Banda alta e **desempenho consistente** (latência previsível).

**Reduzir custo de transferência** de grandes volumes (tarifa de saída menor que a da internet).

Requisitos de conectividade privada (sem internet pública).

### Conceitos e configurações

| Item | Detalhe |
|---|---|
| **Local Direct Connect** | Datacenter de colocation onde você (ou o parceiro) se conecta à AWS. |
| **Dedicated connection** | Porta física de **1, 10, 100 ou 400 Gbps** só sua. |
| **Hosted connection** | Via **parceiro**, de **50 Mbps a 25 Gbps**. |
| **Virtual interfaces (VIF)** | **Private VIF** (acessa VPC via VGW/DX Gateway), **Public VIF** (serviços públicos da AWS, ex.: S3) e **Transit VIF** (Transit Gateway). |
| **Direct Connect Gateway** | Uma conexão alcança VPCs de várias regiões/contas. |
| **LAG** | Agrega várias conexões como uma. |
| **SiteLink** | Liga seus sites entre si pela rede da AWS. |
| **Resiliência** | Recomendação: conexões em **dois locais** DX; VPN como backup. |
| **Criptografia** | ⚠️ **Não é criptografado por padrão.** **MACsec** em portas dedicadas de 10/100/400 Gbps (locais selecionados) ou **VPN IPsec sobre o DX**. |
| **Prazo** | **Semanas** (provisionamento físico). |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Dedicada não significa automaticamente criptografada nem sem possibilidade de falha. A proteção dos dados e a redundância precisam ser planejadas.

### ⚠️ Pegadinhas e não confundir

Direct Connect × VPN: dedicado/estável/semanas × internet/criptografado/minutos.

"Precisa de conexão já" → VPN (pode usar enquanto o DX é instalado).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Cobrança

Por **porta-hora** + **transferência de dados de saída** (mais barata que pela internet). Entrada grátis.

## 5. Caso resolvido: ligando as peças

Uma empresa com tráfego frequente entre seu datacenter e a AWS planeja uma conexão Direct Connect e uma estratégia de contingência.

**Aplicando a sequência à situação:**

**Etapa 1:** Planeje o local e a conexão física compatível com o ambiente da empresa.
**Etapa 2:** Configure interfaces e rotas de acesso aos recursos desejados. A comunicação usa a conectividade planejada.
**Etapa 3:** Planeje caminhos alternativos e proteção dos dados. Conexão dedicada não significa criptografia automática ou ausência de falhas.

**Resultado e responsabilidade:** Direct Connect permite estabelecer essa conectividade por conexões e locais compatíveis, com interfaces e rotas configuradas para o ambiente.

**Recursos envolvidos:** Conexão, interfaces virtuais e gateways associados.

**Decisões que precisam ser tomadas:** Localidade, banda, conexão e redundância.

**Outra situação comentada:** Conexão dedicada de datacenter: Direct Connect; criptografia adicional pode usar VPN conforme requisito.

**Por que não concluir mais do que isso:** Criptografia não é automática em toda modalidade; resiliência exige planejamento

## 6. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Conexão privada, dedicada, sem internet, desempenho consistente."

**Resposta curta:** Direct Connect.

**Pergunta:** "O Direct Connect é criptografado por padrão?"

**Resposta curta:** Não (use MACsec ou VPN sobre DX).

**Pergunta:** "Reduzir custo de transferir grandes volumes todo mês para a AWS."

**Resposta curta:** Direct Connect.

## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Guia do Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
