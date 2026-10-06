# Amazon Detective

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** Depois de um alerta de segurança, a equipe precisa reunir relações entre atividades, identidades e recursos para entender o que aconteceu.

**Como este serviço ajuda?** Detective organiza dados compatíveis e suas relações para apoiar investigações de segurança.

**Exemplo do dia a dia:** Após um alerta, a equipe explora atividades associadas à identidade e ao recurso envolvidos, procurando contexto para a investigação.

**O que ele não resolve sozinho?** Ele apoia a investigação; não decide sozinho a causa de todo incidente nem substitui a equipe responsável pela resposta.

**Primeiras palavras para entender:**

- **Investigação:** análise das evidências e do contexto.
- **Entidade:** identidade ou recurso observado.
- **Relação:** conexão entre atividades e entidades.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança / investigação · **Domínio:** 2 · **Escopo:** Regional · **Tópico do guia:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)
>
> **Em uma frase:** facilita **investigar a causa raiz** de achados de segurança, montando um grafo de comportamento a partir dos logs.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## 1. A sequência de funcionamento

**Passo 1.** Prepare as fontes e o ambiente de investigação compatível.

**Passo 2.** Use as relações de atividades, identidades e recursos para entender o contexto de um alerta.

**Passo 3.** Compare evidências e registre conclusões da investigação. A ferramenta ajuda a analisar; a decisão e a resposta continuam precisando de responsáveis.

## 2. Recursos e opções, com significado

### Como funciona

Coleta automaticamente CloudTrail, **VPC Flow Logs**, achados do **GuardDuty**, audit logs do EKS e achados do Security Hub.

Constrói um **behavior graph** (ML + estatística) mostrando relações entre usuários, roles, IPs, instâncias, ao longo de até 1 ano.

Visualizações prontas: "o que este IP fez?", "esse usuário costuma chamar essa API?", *finding groups* que agrupam achados relacionados.

Teste gratuito de 30 dias; cobrado por volume de dados ingeridos.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Ele apoia a investigação; não decide sozinho a causa de todo incidente nem substitui a equipe responsável pela resposta.

### ⚠️ Não confundir

**GuardDuty detecta → Detective investiga → Security Hub centraliza.**

## 4. Caso resolvido: ligando as peças

Após um alerta, a equipe explora atividades associadas à identidade e ao recurso envolvidos, procurando contexto para a investigação.

**Aplicando a sequência à situação:**

**Etapa 1:** Prepare as fontes e o ambiente de investigação compatível.
**Etapa 2:** Use as relações de atividades, identidades e recursos para entender o contexto de um alerta.
**Etapa 3:** Compare evidências e registre conclusões da investigação. A ferramenta ajuda a analisar; a decisão e a resposta continuam precisando de responsáveis.

**Resultado e responsabilidade:** Detective organiza dados compatíveis e suas relações para apoiar investigações de segurança.

**Recursos envolvidos:** Behavior graph e investigação de entidades/eventos.

**Decisões que precisam ser tomadas:** Conta, região, fontes e acesso.

**Outra situação comentada:** Após finding GuardDuty, investigar contexto: Detective; bloquear requer ação apropriada.

**Por que não concluir mais do que isso:** Não é firewall ou substituto automático da detecção/remediação

## 5. Revisão e perguntas

### ❓ Perguntas típicas

**Pergunta:** "Investigar a causa raiz de um achado de segurança."

**Resposta curta:** Detective.

## 6. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Amazon Detective](https://docs.aws.amazon.com/detective/latest/userguide/what-is-detective.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
