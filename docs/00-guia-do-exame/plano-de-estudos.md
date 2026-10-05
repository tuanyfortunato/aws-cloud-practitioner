# 🗓️ Plano de Estudos (6 semanas, ~1 h/dia)

<!-- didatico:inicio -->
## 🧭 Antes de ler

**Por que esta página existe?** Há muitos assuntos e você precisa distribuir leitura e revisão sem tentar aprender tudo numa sessão.

**Como usar?** Este plano divide o estudo em etapas e sugere uma rotina. Ajuste o ritmo à sua disponibilidade e volte aos temas que ainda não consegue explicar.

**Exemplo:** Em uma sessão, leia um tópico, explique o problema que ele resolve e só depois tente responder às perguntas. Uma resposta errada indica o que revisar.
<!-- didatico:fim -->

> Ajuste ao seu ritmo. O peso de cada domínio indica onde investir mais tempo.

## 🧭 Como usar este plano


> 💡 **Em palavras simples:** são **6 semanas com cerca de 1 hora por dia**. Cada semana tem um foco e os links do
> que estudar; marque **[x]** na coluna *Concluído* quando terminar.


Se tiver menos tempo, junte semanas, mas **não pule a semana 6** (revisão e simulados).


Os domínios com **mais peso** (3 e 2) ganham mais semanas de propósito.


Em cada tópico, comece pela seção **🧠 Antes de começar** e termine respondendo as **Perguntas típicas**.


**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.
- **IAM:** Serviço para identidades e permissões de recursos AWS. Ele responde quais ações uma identidade pode fazer, conforme políticas e demais controles aplicáveis.
- **KMS:** Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.
- **Organizations:** Organizations organiza contas em grupos e permite aplicar políticas compatíveis, incluindo restrições sobre permissões disponíveis.
- **IA:** Inteligência artificial: conjunto de técnicas para tarefas como reconhecimento, previsão e geração de conteúdo. Cada serviço atende funções específicas, não qualquer problema.
- **rede:** Conjunto de caminhos e regras para computadores e recursos se comunicarem. Existir na mesma conta não garante comunicação entre dois recursos.
- **root:** Na conta AWS, é a identidade principal com poderes especiais. Dentro de Linux, root é o administrador do sistema operacional. Administrar Linux não é o mesmo que administrar a conta AWS.
- **compliance:** Atendimento a requisitos definidos. Usar um serviço com certificações não torna automaticamente a aplicação do cliente conforme.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Semana | Foco | Material | Concluído |
|---|---|---|---|
| 1 | Guia do exame + **Domínio 1** (24%) | [Tópicos 1.1–1.7](../01-conceitos-de-nuvem/README.md) · [flashcards D1](../../flashcards/dominio-1.md) | [ ] |
| 2 | **Domínio 2** (30%) — responsabilidade, root, IAM, multi-conta, criptografia | [Tópicos 2.1–2.5](../02-seguranca-e-conformidade/README.md) · fichas de [IAM](../../servicos/seguranca/iam.md), [KMS](../../servicos/seguranca/kms.md), [Organizations](../../servicos/gerenciamento/organizations.md) | [ ] |
| 3 | **Domínio 2** — compliance, logs, proteção, detecção + **Domínio 3**: acesso, infraestrutura, EC2 | [Tópicos 2.6–2.10](../02-seguranca-e-conformidade/README.md) · [3.1–3.4](../03-tecnologia-e-servicos/README.md) | [ ] |
| 4 | **Domínio 3** (34%) — containers, bancos, S3, armazenamento, rede | [Tópicos 3.5–3.10](../03-tecnologia-e-servicos/README.md) + fichas | [ ] |
| 5 | **Domínio 3** — analytics, IA, integração, apps, dev, gestão, migração + **Domínio 4** (12%) + 1º simulado | [Tópicos 3.11–3.18](../03-tecnologia-e-servicos/README.md) · [4.1–4.6](../04-cobranca-precos-e-suporte/README.md) | [ ] |
| 6 | Revisão dos erros + simulados finais (meta ≥ 80%) | [Resumos](../../resumos/README.md) · [simulados](../../simulados/README.md) · [atualizações](atualizacoes-2025-2026.md) | [ ] |


## Rotina diária sugerida



1. **Ler** o tópico do dia em `docs/` (15–20 min).


2. **Aprofundar** nas fichas linkadas no topo do tópico (15 min).


3. **Responder** as *Perguntas típicas* sem olhar a resposta; depois os [flashcards](../../flashcards/README.md) (10 min).


4. **Anotar** dúvidas em *📝 Minhas anotações* e atualizar o status (🔴 → 🟡 → 🟢).


5. **Revisar** os flashcards dos dias anteriores (repetição espaçada — o arquivo TSV importa no Anki).


## Semana da prova



Releia [números-âncora](../../resumos/numeros-ancora.md), [pares que confundem](../../resumos/comparativos.md) e [palavras-chave](../../resumos/palavras-chave.md).


Confira [o que mudou em 2025-2026](atualizacoes-2025-2026.md) e as páginas oficiais de preços/planos.


Revise [erros recorrentes](../../simulados/erros-recorrentes.md).


## Materiais principais


**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.


[AWS Skill Builder — Cloud Practitioner Essentials](https://skillbuilder.aws/) (gratuito)


[Exam guide e questões de exemplo oficiais](https://aws.amazon.com/certification/certified-cloud-practitioner/)


Mais em [`recursos/links-uteis.md`](../../recursos/links-uteis.md)
