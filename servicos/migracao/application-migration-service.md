<!-- autoral -->

# AWS Application Migration Service (AWS MGN)

> **Categoria:** Migração de servidores · **Domínio:** 1 e 3 · **Abrangência:** Regional · **Ficha:** núcleo
>
> **Em uma frase:** automatiza o rehost (*lift and shift*) de servidores físicos, virtuais e de outras nuvens para a AWS, com replicação contínua e virada em minutos; hoje se chama AWS Transform MGN.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

> 📖 **Aula que ensina:** [3.17 Migração e transferência](../../docs/03-tecnologia-e-servicos/17-migracao-e-transferencia.md) · [1.6 Estratégias de migração (os 7 Rs)](../../docs/01-conceitos-de-nuvem/06-estrategias-de-migracao.md)

🏠 [Índice das fichas](../README.md)

---

## Que problema resolve

O sistema de matrícula roda em máquinas virtuais no datacenter da secretaria, e o contrato do datacenter acaba em dezembro. Reescrever o sistema para a nuvem levaria um ano. A escola quer levá-lo como está, sem parar as inscrições.

O **Application Migration Service** faz esse **rehost**. Um agente nos servidores de origem faz a **replicação contínua** dos discos para a AWS enquanto eles continuam funcionando. O serviço converte os servidores para rodarem na AWS, a equipe lança instâncias de teste sem afetar a origem e, na virada, lança as instâncias definitivas, com janelas que costumam ser de minutos. Depois, com a aplicação já na AWS, a modernização pode vir aos poucos.

O limite: o MGN leva o servidor como ele é, inclusive seus defeitos. Ele não converte bancos para outro motor nem reescreve a aplicação; bancos com troca de motor pedem o [DMS](dms-e-sct.md). A lista do exame usa o nome antigo do serviço.

## Como funciona

1. Instala-se o agente de replicação em cada servidor de origem.
2. Os discos são copiados para a AWS e mantidos em sincronia contínua.
3. A equipe lança instâncias de teste na AWS e confere a aplicação.
4. Na virada, o MGN lança as instâncias definitivas, e a origem é desligada.

## Opções principais

| Etapa | O que acontece | Na escola |
|---|---|---|
| Replicação contínua | Discos sincronizados com a AWS | Semanas de cópia sem parar o sistema |
| Lançamento de teste | Instâncias de teste sem afetar a origem | Conferir a matrícula na AWS |
| Virada (*cutover*) | Instâncias definitivas, em minutos | Madrugada de novembro, longe do pico |
| Origens aceitas | Servidores físicos, virtuais e de outras nuvens | Máquinas virtuais da secretaria |

## Números que a prova cobra

| O quê | Valor | Verificado em |
|---|---|---|
| Estratégia | Rehost (*lift and shift*) | 06/10/2026 |
| Gratuidade | Primeiros 90 dias (2.160 horas) de replicação por servidor | 06/10/2026 |
| Nome atual | AWS Transform MGN | 06/10/2026 |

## Como é cobrado

Os primeiros 90 dias de replicação de cada servidor são gratuitos; depois, paga-se por hora por servidor. Os recursos que a replicação e as instâncias usam, como EC2 e EBS, são cobrados normalmente.

## Não confundir com

| Serviço | Diferença para o MGN | Pista no enunciado |
|---|---|---|
| [AWS DMS](dms-e-sct.md) | Migra bancos de dados, com ou sem troca de motor | "Migrar o banco com o sistema funcionando" |
| [Migration Evaluator e Discovery](discovery-migration-hub-e-evaluator.md) | Avaliam custo e descobrem os servidores antes da migração | "Caso de negócio", "dependências" |
| [AWS DataSync](datasync-e-transfer-family.md) | Copia arquivos pela rede | "Copiar arquivos para o S3" |
| [AWS Elastic Beanstalk](../computacao/elastic-beanstalk.md) | Sobe uma aplicação a partir do código | "Só enviar o código" |

## Fontes oficiais

Verificadas em 06/10/2026.

- [O que é o AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html)
- [Preços do AWS Transform MGN](https://aws.amazon.com/application-migration-service/pricing/)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
