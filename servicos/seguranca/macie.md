# Amazon Macie

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A empresa guarda muitos arquivos no S3 e precisa localizar possíveis dados sensíveis, como informações pessoais, sem abrir cada arquivo manualmente.

**Como este serviço ajuda?** Macie ajuda a descobrir e classificar dados sensíveis em objetos S3 compatíveis e a analisar aspectos de segurança dos buckets.

**Exemplo do dia a dia:** A escola avalia um bucket de documentos para identificar arquivos que podem conter informações pessoais dos alunos.

**O que ele não resolve sozinho?** Ele não anonimiza automaticamente os arquivos nem examina todos os bancos e serviços AWS. Resultados precisam ser avaliados e ações de proteção planejadas.

**Primeiras palavras para entender:**

- **Dado sensível:** informação que exige proteção especial.
- **Classificação:** identificação do tipo de conteúdo.
- **Bucket:** recipiente de objetos no S3.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança / proteção de dados · **Domínio:** 2 · **Escopo:** Regional (multi-conta) · **Tópico do guia:** [2.9 Detecção de ameaças](../../docs/02-seguranca-e-conformidade/09-deteccao-de-ameacas.md)
>
> **Em uma frase:** usa machine learning e padrões para **descobrir e proteger dados sensíveis (PII) no Amazon S3**.
>
> **Escopo oficial:** ✅ No escopo · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento

**Antes de ler este trecho:**

- **S3:** O S3 guarda dados como objetos: conteúdo, nome de identificação e informações associadas.


**Passo 1.** Defina os dados S3 compatíveis que precisam de avaliação e a configuração de descoberta.

**Passo 2.** O serviço examina conteúdo conforme sua cobertura e produz resultados sobre possíveis dados sensíveis.

**Passo 3.** Revise achados e corrija exposição quando necessário. A descoberta não anonimiza os arquivos automaticamente.

## 2. Recursos e opções, com significado

### O que faz

**Antes de ler este trecho:**

- **Security Hub:** Security Hub reúne achados de fontes compatíveis e oferece avaliações de controles, conforme os recursos habilitados.
- **EventBridge:** EventBridge recebe eventos e usa regras para encaminhá-los a destinos compatíveis.
- **credenciais:** Informações usadas para comprovar ou representar uma identidade. Credenciais temporárias expiram; credenciais de longa duração precisam de proteção e administração.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.
- **CPF:** Identificador pessoal brasileiro. Neste material é exemplo de dado que pode exigir proteção, não um mecanismo AWS de autenticação.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| Função | Detalhe |
|---|---|
| **Inventário e postura dos buckets** | Buckets **públicos**, sem criptografia, compartilhados com outras contas ou replicados. |
| **Descoberta de dados sensíveis** | *Managed data identifiers* (CPF, cartão de crédito, passaporte, credenciais, dados de saúde, nomes, endereços) e **custom data identifiers** (regex + palavras-chave). |
| **Automated sensitive data discovery** | Amostragem contínua e econômica de todos os buckets. |
| **Jobs** | Varreduras completas sob demanda ou agendadas. |
| **Integrações** | Achados no Security Hub e EventBridge. |


**Antes de ler este trecho:**

- **GB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.
- **bucket:** Recipiente que organiza objetos no S3. A aplicação usa o bucket e a identificação do objeto para pedir operações autorizadas.


Teste gratuito de 30 dias. Cobrança por bucket monitorado e por GB inspecionado.

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

**Antes de ler este trecho:**

- **AWS:** Amazon Web Services: provedor dos serviços de nuvem estudados aqui. Uma conta pode criar recursos e recebe cobrança conforme os serviços utilizados.


Ele não anonimiza automaticamente os arquivos nem examina todos os bancos e serviços AWS. Resultados precisam ser avaliados e ações de proteção planejadas.

### ⚠️ Pegadinha

**Antes de ler este trecho:**

- **Macie:** Macie ajuda a descobrir e classificar dados sensíveis em objetos S3 compatíveis e a analisar aspectos de segurança dos buckets.
- **PII:** Informação que pode identificar uma pessoa. Sua identificação ajuda a planejar proteção de dados, mas não substitui avaliação do contexto e das regras aplicáveis.
- **GDPR:** Referências, padrões ou requisitos de segurança e conformidade com escopos distintos. A menção de um nome não é certificação automática do cliente; identifique qual requisito a seção aborda.
- **LGPD:** Referências de padrões e de proteção de dados com finalidades distintas. Identifique o requisito aplicável; o material técnico não substitui uma avaliação de conformidade.


Macie atua **só no S3**. "PII", "dados sensíveis", "LGPD/GDPR no S3" → Macie.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

## 5. Caso resolvido: ligando as peças

A escola avalia um bucket de documentos para identificar arquivos que podem conter informações pessoais dos alunos.

**Aplicando a sequência à situação:**

**Etapa 1:** Defina os dados S3 compatíveis que precisam de avaliação e a configuração de descoberta.
**Etapa 2:** O serviço examina conteúdo conforme sua cobertura e produz resultados sobre possíveis dados sensíveis.
**Etapa 3:** Revise achados e corrija exposição quando necessário. A descoberta não anonimiza os arquivos automaticamente.

**Resultado e responsabilidade:** Macie ajuda a descobrir e classificar dados sensíveis em objetos S3 compatíveis e a analisar aspectos de segurança dos buckets.

**Recursos envolvidos:** Inventário de buckets, jobs, identificadores e findings.

**Decisões que precisam ser tomadas:** Buckets, escopo, formatos e identificadores suportados.

**Antes de ler este trecho:**

- **EBS:** O EBS fornece volumes, isto é, discos virtuais que podem ser conectados a máquinas EC2 compatíveis.
- **RDS:** O RDS oferece bancos relacionais gerenciados.


**Outra situação comentada:** Encontrar dados pessoais em documentos S3: Macie; confirme elegibilidade do formato e permissões.

**Por que não concluir mais do que isso:** Não varre genericamente RDS/EBS e não apaga conteúdo sensível sozinho

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

A empresa guarda muitos arquivos no S3 e precisa localizar possíveis dados sensíveis, como informações pessoais, sem abrir cada arquivo manualmente.

**2. O que a solução fornece?**

Macie ajuda a descobrir e classificar dados sensíveis em objetos S3 compatíveis e a analisar aspectos de segurança dos buckets.

**3. Que conclusão seria incorreta?**

Ele não anonimiza automaticamente os arquivos nem examina todos os bancos e serviços AWS. Resultados precisam ser avaliados e ações de proteção planejadas.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Encontrar dados pessoais em buckets S3."

**Resposta curta:** Macie.


**Fundamento explicado no capítulo:** "Encontrar dados pessoais em buckets S3." → Macie.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
