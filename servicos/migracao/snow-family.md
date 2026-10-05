# Família AWS Snow (Snowball Edge, Snowcone, Snowmobile)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Grandes quantidades de dados podem levar muito tempo para viajar por uma conexão limitada, e alguns locais quase não têm rede.

**Como este serviço ajuda?** A família Snow foi associada a dispositivos físicos para transferência e processamento local. Esta ficha explica esses conceitos e as restrições das ofertas citadas.

**Exemplo do dia a dia:** Em um cenário histórico de transferência offline, dados eram copiados para um dispositivo e transportados até a AWS, em vez de enviados todos pela internet.

**O que ele não resolve sozinho?** Não trate esse exemplo como uma oferta atual disponível a qualquer cliente. Há produtos encerrados ou restritos; confira o status e as alternativas indicadas na ficha.

**Primeiras palavras para entender:**

- **Offline:** sem depender de conexão contínua.
- **Borda:** processamento no local dos dados.
- **Dispositivo:** equipamento físico usado para executar ou armazenar.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Migração / transferência offline e borda · **Domínio:** 3 · **Escopo:** dispositivo físico vinculado a uma região · **Tópico do guia:** [3.9 Outros armazenamentos](../../docs/03-tecnologia-e-servicos/09-outros-armazenamentos.md) · [3.17 Migração](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md)
>
> **Em uma frase:** dispositivos físicos robustos para **mover grandes volumes de dados** quando a rede é lenta, cara ou inexistente, e para **computação na borda** desconectada.
>
> **Escopo oficial:** ⚪ Não listado (saiu da lista atual) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento


**Passo 1.** Entenda a necessidade histórica de transportar dados quando a conexão era inadequada.

**Passo 2.** No processo compatível com a oferta, dados eram copiados para um dispositivo físico e enviados para importação.

**Passo 3.** Confira restrições e alternativas atuais. O exemplo não significa disponibilidade para um novo cliente hoje.

## 2. Recursos e opções, com significado

### Dispositivos

**Antes de ler este trecho:**

- **TB / PB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **suporte:** Suporte oferece ajuda conforme um plano e suas condições. Um prazo de resposta inicial não é garantia de tempo de resolução de todo incidente.
- **campo:** Informação nomeada dentro de um registro, como nome ou data. Consultas usam os campos conforme a estrutura e o modelo do banco.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Dispositivo | Capacidade | Uso | Status 🔄 |
|---|---|---|---|
| **Snowball Edge Storage Optimized** | **210 TB** utilizáveis ✔️ (antes 80 TB) | Migração de dezenas a centenas de TB / petabytes (vários dispositivos) | Só para **clientes existentes** desde 07/11/2025 |
| **Snowball Edge Compute Optimized** | Até 104 vCPUs ✔️ | Computação na borda (navios, minas, campo militar) | Só clientes existentes |
| **Snowcone** | 8–14 TB, pequeno e leve | Borda e transferência pequena | Sem novos pedidos desde 12/11/2024; suporte encerrado em 12/11/2025 |
| **Snowmobile** | Até **100 PB** (caminhão) | Exabytes | **Encerrado em 14/03/2024** ✔️ |


> 🔄 ✔️ A página do produto anuncia o **fim do suporte comercial dos Snowball Edge Storage Optimized e Compute Optimized em 31/12/2026** nas regiões comerciais (exceção para clientes GovCloud/ADC com jobs ativos).

### Como funciona (Snowball)

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.


1. Pedido no console → AWS envia o dispositivo.

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **KMS:** Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.


2. Copia os dados localmente (cliente OpsHub ou S3 adapter); dados **criptografados** (KMS, 256 bits); dispositivo resistente a violação, com **E Ink** de envio.

**Antes de ler este trecho:**

- **NIST:** Referências, padrões ou requisitos de segurança e conformidade com escopos distintos. A menção de um nome não é certificação automática do cliente; identifique qual requisito a seção aborda.


3. Devolve à AWS → dados importados no **S3** → dispositivo é **apagado** seguindo padrões NIST.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Não trate esse exemplo como uma oferta atual disponível a qualquer cliente. Há produtos encerrados ou restritos; confira o status e as alternativas indicadas na ficha.

### Regra prática

**Antes de ler este trecho:**

- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.


Se transferir pela rede levaria **semanas**, use Snow. Ex.: 100 TB num link de 100 Mbps ≈ 100+ dias.

### ⚠️ Na prova

🔄 A família Snow **não aparece** na lista atual de serviços no escopo (verificação de 04/10/2026). O Snowmobile não tem página oficial de aposentadoria localizada (só imprensa citando a AWS).



Questões antigas citam Snowball Edge/Snowmobile (a família saiu da lista atual): "migrar petabytes com banda limitada" → **Snowball Edge**; "exabytes / 100 PB" → **Snowmobile** (questões antigas). "Processar dados num navio sem conexão" → família Snow (borda).

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

### Alternativas atuais para novos clientes

**AWS DataSync** (online) — [ficha](datasync-e-transfer-family.md).


**AWS Data Transfer Terminal**: locais físicos seguros da AWS onde você leva seus próprios dispositivos de armazenamento para upload em alta velocidade.


**Parceiros** de transferência; **Outposts** para computação de borda.

## 5. Caso resolvido: ligando as peças

Em um cenário histórico de transferência offline, dados eram copiados para um dispositivo e transportados até a AWS, em vez de enviados todos pela internet.

**Aplicando a sequência à situação:**

**Etapa 1:** Entenda a necessidade histórica de transportar dados quando a conexão era inadequada.
**Etapa 2:** No processo compatível com a oferta, dados eram copiados para um dispositivo físico e enviados para importação.
**Etapa 3:** Confira restrições e alternativas atuais. O exemplo não significa disponibilidade para um novo cliente hoje.

**Resultado e responsabilidade:** A família Snow foi associada a dispositivos físicos para transferência e processamento local. Esta ficha explica esses conceitos e as restrições das ofertas citadas.

**Recursos envolvidos:** Dispositivos físicos, jobs de transferência e ferramentas locais.

**Decisões que precisam ser tomadas:** Elegibilidade/disponibilidade, volume e procedimento de transferência.


**Outra situação comentada:** Pouca banda e muitos dados: avalie transferência física disponível; para novos clientes consulte alternativas atuais da ficha.

**Por que não concluir mais do que isso:** Não listado não significa exclusão formal; não recomende contratação ignorando restrições atuais

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Grandes quantidades de dados podem levar muito tempo para viajar por uma conexão limitada, e alguns locais quase não têm rede.

**2. O que a solução fornece?**

A família Snow foi associada a dispositivos físicos para transferência e processamento local. Esta ficha explica esses conceitos e as restrições das ofertas citadas.

**3. Que conclusão seria incorreta?**

Não trate esse exemplo como uma oferta atual disponível a qualquer cliente. Há produtos encerrados ou restritos; confira o status e as alternativas indicadas na ficha.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Migrar 500 TB de um datacenter com internet lenta."

**Resposta curta:** Snowball Edge.

**Antes de ler este trecho:**

- **datacenter:** Instalação física com equipamentos de computação, rede, energia e refrigeração. A nuvem continua dependendo desses equipamentos, mas o cliente não precisa manter o prédio.


**Fundamento explicado no capítulo:** "Migrar 500 TB de um datacenter com internet lenta." → Snowball Edge.

**Pergunta:** "Processar dados num local remoto sem conexão."

**Resposta curta:** Snowball Edge Compute Optimized.


**Fundamento explicado no capítulo:** "Processar dados num local remoto sem conexão." → Snowball Edge Compute Optimized.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [AWS Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/whatisedge.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
