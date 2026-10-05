# AWS Application Migration Service (AWS MGN)

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa quer mover servidores existentes para a AWS mantendo inicialmente boa parte de sua aplicação e configuração, sem reescrever tudo antes da mudança.

**Como este serviço ajuda?** Application Migration Service replica servidores compatíveis e apoia testes e a transição para execução na AWS.

**Exemplo do dia a dia:** A equipe replica um servidor do sistema interno, testa sua execução na AWS e planeja o momento de trocar o ambiente em uso.

**O que ele não resolve sozinho?** Replicar não moderniza automaticamente o programa nem garante que bancos, DNS e integrações externas estejam prontos. A migração precisa ser testada.

**Primeiras palavras para entender:**

- **Rehost:** mover com poucas mudanças iniciais.
- **Replicação:** cópia contínua de dados.
- **Cutover:** troca para o ambiente de destino.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Migração de servidores · **Domínio:** 1 (Rehost) e 3 · **Escopo:** Regional · **Tópico do guia:** [3.17 Migração e transferência](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md)
>
> **Em uma frase:** migração **lift-and-shift (Rehost)** de servidores físicos, virtuais ou de outras nuvens para EC2, com mínima indisponibilidade.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Como funciona

1. Instala o **agente de replicação** no servidor de origem (Windows/Linux).
2. Replicação **contínua em nível de bloco** para uma *staging area* na AWS.
3. **Instâncias de teste** sem afetar a origem.
4. **Cutover**: lança as instâncias finais em minutos; a origem pode ser desligada.
5. Ações pós-lançamento automatizam ajustes (instalar agentes, converter licenças, modernizar).

## 🔄 Nome atual

- O serviço hoje se chama **AWS Transform MGN**. O exam guide e a lista de serviços ainda usam **AWS Application Migration Service** — é esse o nome que aparece na prova.

## Destaques

- Suporta qualquer aplicação/banco que rode no servidor; converte automaticamente para rodar em EC2.
- **Gratuito por 2.160 horas (90 dias de uso contínuo) por servidor de origem** (paga só os recursos de staging e as instâncias).
- Substitui o antigo CloudEndure Migration e o Server Migration Service (SMS).

## ⚠️ Não confundir

- **MGN** (servidores inteiros) × **DMS** (bancos de dados) × **Elastic Disaster Recovery** (mesma tecnologia, objetivo de DR contínuo).

## ❓ Perguntas típicas

- "Migrar servidores físicos e VMs para EC2 sem mudar nada, com pouca indisponibilidade." → Application Migration Service.
- "Ferramenta da estratégia Rehost." → Application Migration Service.

<!-- aprofundamento:inicio -->
## 🔬 Ficha prática — visualize o serviço sem console

> Este é um mapa dos recursos e decisões, não uma reprodução da tela. Capacidades dependem da modalidade, região e permissões; siga o status de escopo no topo desta ficha.

| Pergunta | O que você precisa compreender |
|---|---|
| **O que existe nesse serviço?** | Servidores origem, replicação, staging e launch settings |
| **O que você decide/configura?** | Rede, agente, destino, teste e cutover |
| **Em que ordem as coisas acontecem?** | Replica servidor compatível, lança teste e depois destino definitivo |
| **O que pode fazer, e em que condição?** | Apoia rehost de servidores |
| **O que não pode presumir?** | Não refatora aplicação nem elimina teste; nomes comerciais podem mudar |

**Caso comentado:** Mover servidor como está: Application Migration Service; copiar banco e converter esquema: outras ferramentas.

**Antes de escolher na prova:** identifique o recurso, a ação e o requisito. Diferencie impossibilidade do serviço de falta de configuração, permissão ou modalidade compatível.

**Base técnica:** consulte os links da seção Documentação oficial desta ficha; as comparações reaproveitam os fundamentos descritos acima. [Roteiro de leitura](../../docs/00-guia-do-exame/estudar-sem-console.md).
<!-- aprofundamento:fim -->

## 🔗 Documentação oficial

- [Application Migration Service](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html)
