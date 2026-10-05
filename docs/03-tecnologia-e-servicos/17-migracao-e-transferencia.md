# 3.17 Migração e transferência

## 🧠 Antes de começar

**Qual é a dificuldade?** Mover para a AWS envolve aplicações, bancos e arquivos, que podem exigir processos e ferramentas diferentes.

**A ideia em palavras simples:** Migração inclui descobrir o ambiente, planejar mudanças, replicar ou transferir dados, testar e realizar a troca. As ferramentas atendem etapas e tipos de recurso específicos.

**Exemplo do dia a dia:** A escola prepara a migração de um servidor e de seu banco. Replica e testa cada parte antes de mudar o sistema em uso.

**O que não concluir?** Transferir um banco não move automaticamente todo o programa; copiar arquivos também não migra suas dependências. Compatibilidade e disponibilidade das ofertas precisam ser verificadas.

**📚 Palavras que aparecem aqui:**

| Termo | Em palavras simples |
|---|---|
| **Homogênea** | mesmo motor de banco na origem e no destino (MySQL → MySQL). |
| **Heterogênea** | motores diferentes (Oracle → PostgreSQL). |
| **Schema** | a estrutura do banco: tabelas, colunas e relacionamentos. |

---

> **Domínio 3 — Tecnologia e Serviços de Nuvem (34%)** · **Status:** 🔴 Não iniciado <!-- 🔴 Não iniciado | 🟡 Em andamento | 🟢 Revisado -->

> 🔎 **Fichas detalhadas:** [Migration Evaluator, Application Discovery Service e Migration Hub](../../servicos/migracao/discovery-migration-hub-e-evaluator.md) · [AWS Application Migration Service (AWS MGN)](../../servicos/migracao/application-migration-service.md) · [AWS Database Migration Service (DMS) e Schema Conversion Tool (SCT)](../../servicos/migracao/dms-e-sct.md) · [Família AWS Snow (Snowball Edge, Snowcone, Snowmobile)](../../servicos/migracao/snow-family.md) · [AWS DataSync e AWS Transfer Family](../../servicos/migracao/datasync-e-transfer-family.md)

> ⚠️ **Atualização do exam guide (verificado em 04/10/2026):** **Migration Hub** e **Application Discovery Service** continuam no escopo, mas estão fechados a novos clientes desde 07/11/2025. **Transfer Family** está **fora do escopo**; Snow e DataSync não aparecem. [Ver escopo oficial](../00-guia-do-exame/escopo-oficial.md).

⬅️ [3.16 Gestão e governança](16-gestao-e-governanca.md) · 🏠 [Índice do domínio](README.md) · [3.18 Serviços menos conhecidos que podem aparecer](18-servicos-menos-conhecidos.md) ➡️

---

## 1. Entenda as peças e a relação entre elas

**Antes de ler este trecho:**

- **origem:** Local de onde uma distribuição obtém conteúdo, como um servidor ou bucket. Uma cópia em cache não elimina toda necessidade de acessar a origem.


Migração é uma sequência, não apenas uma cópia. Descubra componentes e dependências, escolha a mudança, prepare origem e destino, transfira ou replique, teste e realize a transição. Arquivos, máquinas e bancos podem seguir ferramentas diferentes.

Avalie estrutura e dados separadamente. Um banco de outra tecnologia pode exigir conversão; um programa pode precisar de ajustes; uma conexão pode precisar de mudança. Testar o conjunto evita concluir que a migração terminou só porque os dados chegaram.

<details>
<summary>Uma analogia para revisar esta ideia</summary>

é uma **mudança de casa**: o **Migration Evaluator** faz o orçamento; o **Discovery Service** mede os móveis e vê o que depende do quê; o **Migration Hub** é a planilha de acompanhamento; o **MGN** é o caminhão que leva tudo como está; o **DMS** leva o banco com a loja aberta; o **SCT** traduz a estrutura de um banco para outro.

</details>

## 2. Conceitos e opções explicados

As ferramentas seguem a ordem de uma migração: avaliar, planejar e migrar.

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **EFS:** O EFS oferece um sistema de arquivos compartilhado.
- **FSx:** O FSx oferece sistemas de arquivos gerenciados em modalidades diferentes.
- **Aurora:** Aurora é um banco relacional da AWS dentro da família RDS.
- **AWS Application Migration Service / Application Migration Service:** Application Migration Service replica servidores compatíveis e apoia testes e a transição para execução na AWS.
- **AWS Database Migration Service / Database Migration Service:** DMS move dados entre fontes e destinos compatíveis, incluindo replicação de mudanças em cenários suportados.
- **Família AWS Snow:** A família Snow foi associada a dispositivos físicos para transferência e processamento local.
- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.
- **on-premises:** Ambiente mantido nas instalações da organização. Uma arquitetura híbrida usa esse ambiente e recursos de nuvem em conjunto.
- **replicação:** Manutenção de uma cópia dos dados em outro recurso. Se uma alteração incorreta for replicada, a cópia também pode recebê-la; replicação não substitui todo backup.
- **SFTP / FTP / FTPS:** Protocolos de transferência de arquivos. SFTP usa SSH; FTP não fornece a mesma proteção; FTPS adiciona TLS ao FTP. São opções de compatibilidade diferentes.
- **schema:** Estrutura e tipos dos dados. Em migração, adaptar a estrutura é uma tarefa diferente de copiar os registros.
- **TCO:** Custo total de propriedade: inclui infraestrutura e operação, não apenas o preço de uma máquina. A comparação depende das hipóteses adotadas.
- **SCT:** Ferramenta de conversão de estrutura de banco em migrações compatíveis. Nem toda estrutura ou regra da aplicação é convertida automaticamente.
- **rehost / lift-and-shift:** Mover um sistema com poucas mudanças iniciais. A infraestrutura muda, mas isso não moderniza automaticamente o software.
- **MGN:** Sigla usada para Application Migration Service. Apoia a migração de servidores compatíveis; não reescreve automaticamente a aplicação.
- **DMS:** Database Migration Service: transferência ou replicação de dados entre bancos compatíveis. Conversão de estrutura e ajuste da aplicação são trabalhos relacionados, mas diferentes.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Serviço | Etapa | O que faz |
| --- | --- | --- |
| Migration Evaluator | Avaliar | Monta o **caso de negócio**: estima o custo de rodar o ambiente atual na AWS (TCO) |
| AWS Application Discovery Service | Avaliar | Coleta dados dos servidores on-premises (configuração, uso, **dependências** entre aplicações), com ou sem agente |
| AWS Migration Hub | Acompanhar | **Painel único** para acompanhar o progresso das migrações em várias ferramentas |
| AWS Application Migration Service (MGN) | Migrar servidores | **Lift-and-shift (Rehost)**: replica servidores continuamente para a AWS e faz o corte com mínimo de indisponibilidade |
| AWS Database Migration Service (DMS) | Migrar bancos | Migra bancos com o **banco de origem funcionando** (replicação contínua), entre motores iguais ou diferentes |
| AWS Schema Conversion Tool (SCT) | Migrar bancos | **Converte o schema** e o código do banco entre motores diferentes (ex.: Oracle para Aurora PostgreSQL); usado junto com o DMS |
| Família AWS Snow | Transferir dados | Transferência **offline** de grandes volumes em dispositivo físico (ver [3.9](09-outros-armazenamentos.md)) |
| AWS DataSync | Transferir dados | Transferência **online** e automatizada de arquivos para S3, EFS ou FSx (ver [3.9](09-outros-armazenamentos.md)) |
| AWS Transfer Family | Transferir dados | SFTP, FTPS e FTP gerenciados direto para S3 ou EFS |


**Antes de ler este trecho:**

- **RDS:** O RDS oferece bancos relacionais gerenciados.


**Migração homogênea** (MySQL → RDS MySQL): só o DMS. **Heterogênea** (Oracle → Aurora): SCT para converter o schema e DMS para mover os dados.


**Cai na prova:** "descobrir dependências entre os servidores antes de migrar" = Application Discovery Service; "migrar VMs sem alterar" = Application Migration Service; "migrar banco sem parar o sistema" = DMS; "converter Oracle para PostgreSQL" = SCT; "justificar o custo da migração para a diretoria" = Migration Evaluator.

## 3. Como analisar uma situação

**Antes de ler este trecho:**

- **servidor:** Computador que atende pedidos de outros computadores. Um servidor web, por exemplo, responde aos pedidos enviados pelo navegador.
- **capacidade:** Recursos disponíveis para realizar trabalho, como processamento, memória, espaço ou quantidade de operações. A unidade depende do serviço.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **protocolo:** Conjunto de regras da comunicação. Um protocolo define o formato e o comportamento da troca; produtos precisam ser compatíveis com ele.
- **SQL:** Linguagem para definir e consultar dados de bancos compatíveis. Uma consulta pode filtrar ou agregar registros; seu desenho influencia desempenho e resultado.
- **cutover:** Momento planejado de trocar o ambiente em uso pelo destino da migração. Requer validar dependências e planejar a transição dos dados.


**Primeiro, identifique o funcionamento:** Descoberta identifica servidores/dependências; avaliação estima custo; migração replica dados ou servidores; teste valida o destino; cutover muda a operação para o destino.

**Depois, compare as escolhas:** Servidor inteiro: Application Migration Service. Dados de banco: DMS. Conversão de esquema: SCT ou capacidade suportada de conversão. Dados de arquivos: ferramentas específicas conforme protocolo.

**Por fim, verifique o limite:** DMS não converte automaticamente toda lógica SQL. Replicação não dispensa rede, permissões, compatibilidade e teste. Serviço no escopo pode estar restrito a clientes existentes.

## 4. Caso resolvido

A origem é Oracle e o destino PostgreSQL. Copiar linhas com DMS basta para garantir funcionamento?

**Raciocínio e resposta:** Não. Avalie conversão de esquema/código, tipos e recursos incompatíveis; DMS move dados nas condições suportadas. Valide a aplicação antes do cutover.

A resposta muda se mudar o requisito destacado. Compare a necessidade com a função da solução, em vez de apenas associar duas palavras.

## 5. Revisão do capítulo

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

Mover para a AWS envolve aplicações, bancos e arquivos, que podem exigir processos e ferramentas diferentes.

**2. O que a solução fornece?**

Migração inclui descobrir o ambiente, planejar mudanças, replicar ou transferir dados, testar e realizar a troca. As ferramentas atendem etapas e tipos de recurso específicos.

**3. Que conclusão seria incorreta?**

Transferir um banco não move automaticamente todo o programa; copiar arquivos também não migra suas dependências. Compatibilidade e disponibilidade das ofertas precisam ser verificadas.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

**Objetivos de aprendizagem:**

- [ ] Ligar cada ferramenta à **etapa** (avaliar, acompanhar, migrar, transferir).
- [ ] Diferenciar migração de banco **homogênea** (só DMS) de **heterogênea** (SCT + DMS).
- [ ] Diferenciar transferência **offline** (Snow) de **online** (DataSync, Transfer Family).

**Dica de revisão para a prova:** "Dependências entre servidores" → **Application Discovery Service**. "Migrar VMs sem alterar" → **MGN**. "Banco sem parar o sistema" → **DMS**. "Oracle para PostgreSQL" → **SCT**. "Justificar custo" → **Migration Evaluator**.

### ❓ Perguntas típicas

> Também estão nos [flashcards](../../flashcards/dominio-3.md).
**Pergunta:** "Levantar servidores e dependências antes de migrar."

**Resposta curta:** Application Discovery Service.


**Fundamento explicado no capítulo:** "Levantar servidores e dependências antes de migrar." → Application Discovery Service.

**Pergunta:** "Estimar quanto a empresa vai economizar ao migrar."

**Resposta curta:** Migration Evaluator.


**Fundamento explicado no capítulo:** "Estimar quanto a empresa vai economizar ao migrar." → Migration Evaluator.

**Pergunta:** "Acompanhar todas as migrações num painel central."

**Resposta curta:** Migration Hub.


**Fundamento explicado no capítulo:** "Acompanhar todas as migrações num painel central." → Migration Hub.

**Pergunta:** "Migrar servidores físicos e VMs para EC2 com pouca indisponibilidade."

**Resposta curta:** Application Migration Service.

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.


**Fundamento explicado no capítulo:** "Migrar servidores físicos e VMs para EC2 com pouca indisponibilidade." → Application Migration Service.

**Pergunta:** "Migrar um banco sem desligar a aplicação."

**Resposta curta:** DMS.


**Fundamento explicado no capítulo:** "Migrar um banco sem desligar a aplicação." → DMS.

**Pergunta:** "Converter um banco Oracle para Aurora PostgreSQL."

**Resposta curta:** SCT + DMS.


**Fundamento explicado no capítulo:** "Converter um banco Oracle para Aurora PostgreSQL." → SCT + DMS.

**Pergunta:** "Transferir arquivos online de forma automatizada para o S3."

**Resposta curta:** DataSync.


**Fundamento explicado no capítulo:** "Transferir arquivos online de forma automatizada para o S3." → DataSync.

**Pergunta:** "Parceiros enviam arquivos via SFTP para o S3."

**Resposta curta:** Transfer Family.


**Fundamento explicado no capítulo:** "Parceiros enviam arquivos via SFTP para o S3." → Transfer Family.

<!-- extra:inicio -->
<!-- extra:fim -->

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->

---

⬅️ [3.16 Gestão e governança](16-gestao-e-governanca.md) · 🏠 [Índice do domínio](README.md) · [3.18 Serviços menos conhecidos que podem aparecer](18-servicos-menos-conhecidos.md) ➡️
