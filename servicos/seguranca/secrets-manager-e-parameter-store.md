# AWS Secrets Manager e Systems Manager Parameter Store

<!-- didatico:inicio -->
## 🧠 Comece pelo problema

**Qual é a dificuldade?** A aplicação precisa de senhas e configurações. Colocar esses valores no código dificulta protegê-los e alterá-los sem publicar uma nova versão.

**Como este serviço ajuda?** Secrets Manager guarda segredos com recursos como rotação compatível. Parameter Store organiza parâmetros de configuração, inclusive valores protegidos conforme a modalidade.

**Exemplo do dia a dia:** O sistema lê a senha do banco por um acesso autorizado ao serviço, em vez de manter essa senha escrita no código enviado ao repositório.

**O que ele não resolve sozinho?** Guardar um segredo não autoriza qualquer programa a lê-lo. Rotação também não funciona para todo sistema sem configuração e integração.

**Primeiras palavras para entender:**

- **Segredo:** valor sensível, como uma senha.
- **Parâmetro:** valor de configuração.
- **Rotação:** troca periódica de um segredo.

*O exemplo é ilustrativo. Para estudar para a prova, confira o escopo indicado abaixo; para usar o serviço, confira também as condições e a documentação oficial desta ficha.*
<!-- didatico:fim -->

> **Categoria:** Segurança / gestão de segredos · **Domínio:** 2 · **Escopo:** Regional · **Tópico do guia:** [2.3 AWS IAM](../../docs/02-seguranca-e-conformidade/03-iam.md)
>
> **Em uma frase:** guardam segredos e configurações fora do código, criptografados com KMS — o Secrets Manager também os **rotaciona automaticamente**.
>
> **Escopo oficial:** ✅ No escopo (Parameter Store como parte do Systems Manager) · [ver lista](../../docs/00-guia-do-exame/escopo-oficial.md)

## Roteiro de leitura

Leia primeiro os fundamentos e a sequência. Depois examine os recursos e as escolhas. Use o caso resolvido para ligar as peças; as perguntas finais servem à revisão.

## 1. A sequência de funcionamento


**Passo 1.** Separe valores sensíveis e parâmetros comuns de configuração.

**Passo 2.** Guarde os valores na ferramenta compatível e autorize apenas quem precisa obtê-los. A aplicação lê o valor ao executar.

**Passo 3.** Planeje atualização e rotação conforme a integração. Guardar uma senha não muda sozinho a senha do sistema externo.

## 2. Recursos e opções, com significado

### Comparação

**Antes de ler este trecho:**

- **EC2:** O EC2 permite alugar um computador que funciona no datacenter da AWS.
- **Lambda:** No Lambda, você entrega uma função, isto é, um trecho de programa.
- **ECS:** O ECS coordena a execução de containers: pacotes com a aplicação e suas dependências.
- **RDS:** O RDS oferece bancos relacionais gerenciados.
- **Aurora:** Aurora é um banco relacional da AWS dentro da família RDS.
- **Redshift:** Redshift é um ambiente de banco voltado à análise de dados, conhecido como data warehouse.
- **DocumentDB:** DocumentDB armazena e consulta documentos, como registros estruturados de produtos.
- **API:** Interface pela qual um programa pede uma operação a outro sistema. Por exemplo, pedir ao S3 que guarde um arquivo é uma chamada de API.
- **KMS:** Serviço AWS para gerenciar chaves e operações criptográficas. Ter uma chave não ativa automaticamente criptografia em todos os recursos.
- **CloudFormation:** Infraestrutura como código descreve recursos em arquivos. CloudFormation usa templates e stacks para criar e administrar recursos compatíveis.
- **KB:** Unidades de quantidade de dados em escala decimal: kilobyte, megabyte, gigabyte, terabyte e petabyte. Quando uma tabela fala em GB armazenados, mede volume; GB por segundo mede transferência.
- **replicação:** Manutenção de uma cópia dos dados em outro recurso. Se uma alteração incorreta for replicada, a cópia também pode recebê-la; replicação não substitui todo backup.
- **criptografia:** Transformação usada para proteger a leitura dos dados. A chave e as permissões de uso precisam ser administradas; isso não impede toda exclusão ou erro do programa.
- **Parameter Store:** Recurso de armazenamento de parâmetros do Systems Manager. É necessário configurar proteção e permissão, inclusive para valores sensíveis.
- **AWSCURRENT / AWSPREVIOUS:** Rótulos de versões de segredos que identificam, respectivamente, a versão atual e a anterior no contexto do Secrets Manager.


Leia cada linha como uma alternativa e cada coluna como um critério de comparação. Uma diferença numa coluna não garante que a opção atende a todos os demais requisitos.

| | **Secrets Manager** | **Parameter Store** |
|---|---|---|
| Foco | Segredos (senhas de banco, chaves de API, tokens) | Configurações e segredos simples |
| **Rotação automática** | ✅ **Nativa** (RDS, Aurora, Redshift, DocumentDB) ou via Lambda; *managed rotation* | ❌ (só com automação própria) |
| Criptografia | Sempre (KMS) | Opcional (`SecureString` com KMS) |
| Replicação entre regiões | ✅ | ❌ |
| Versionamento | Estágios `AWSCURRENT` / `AWSPREVIOUS` | Histórico de versões |
| Tamanho | Até 64 KB (65.536 bytes) 🧊 | Standard 4 KB (até 10.000 parâmetros, grátis) / Advanced 8 KB (até 100.000, pago) 🧊 |
| Hierarquia | — | Sim (`/app/prod/db-url`) |
| Custo | **Pago** por segredo/mês + chamadas de API | **Standard grátis**; Advanced pago |
| Integração | RDS gera e guarda a senha mestre no Secrets Manager | CloudFormation, ECS, Lambda, EC2 |

## 3. Como escolher e reconhecer os limites

Uma opção deve atender ao requisito da aplicação. Compare função, compatibilidade, responsabilidade e condições; preço ou uma palavra do enunciado não bastam isoladamente.

Guardar um segredo não autoriza qualquer programa a lê-lo. Rotação também não funciona para todo sistema sem configuração e integração.

### ⚠️ Pegadinhas

"Rotação automática" → **Secrets Manager**. "Guardar configuração barata/grátis" → **Parameter Store**.

**Antes de ler este trecho:**

- **user data:** Dados ou instruções fornecidos à inicialização da máquina. Um script configurado pode preparar o ambiente; ele não instala qualquer sistema sem você descrever as ações.


Nunca guarde access keys/senhas no código, em variáveis de ambiente em texto ou no user data.

## 4. Operação, segurança e custo

Ter o recurso disponível é diferente de operá-lo corretamente. Aqui, observe o que continua sendo administrado pelo cliente, o que gera cobrança e como conservar ou recuperar dados.

## 5. Caso resolvido: ligando as peças

O sistema lê a senha do banco por um acesso autorizado ao serviço, em vez de manter essa senha escrita no código enviado ao repositório.

**Aplicando a sequência à situação:**

**Etapa 1:** Separe valores sensíveis e parâmetros comuns de configuração.
**Etapa 2:** Guarde os valores na ferramenta compatível e autorize apenas quem precisa obtê-los. A aplicação lê o valor ao executar.
**Etapa 3:** Planeje atualização e rotação conforme a integração. Guardar uma senha não muda sozinho a senha do sistema externo.

**Resultado e responsabilidade:** Secrets Manager guarda segredos com recursos como rotação compatível. Parameter Store organiza parâmetros de configuração, inclusive valores protegidos conforme a modalidade.

**Recursos envolvidos:** Secrets e parâmetros; versões e chaves de criptografia quando aplicável.

**Decisões que precisam ser tomadas:** Acesso, valor, rotação e integração.


**Outra situação comentada:** Senha de banco com rotação: Secrets Manager; parâmetros comuns: avalie Parameter Store.

**Por que não concluir mais do que isso:** Não basta criar segredo: aplicação precisa usá-lo; rotação não muda magicamente sistemas sem integração

## 6. Revisão e perguntas

### Confira se você compreendeu

**1. Qual dificuldade está sendo resolvida?**

A aplicação precisa de senhas e configurações. Colocar esses valores no código dificulta protegê-los e alterá-los sem publicar uma nova versão.

**2. O que a solução fornece?**

Secrets Manager guarda segredos com recursos como rotação compatível. Parameter Store organiza parâmetros de configuração, inclusive valores protegidos conforme a modalidade.

**3. Que conclusão seria incorreta?**

Guardar um segredo não autoriza qualquer programa a lê-lo. Rotação também não funciona para todo sistema sem configuração e integração.

Tente responder antes de ler o comentário. Se apenas lembrar o nome, volte ao funcionamento e explique qual recurso recebe a entrada, realiza o trabalho e conserva o resultado.

### ❓ Perguntas típicas

**Pergunta:** "Onde guardar a senha do banco com rotação automática?"

**Resposta curta:** Secrets Manager.


**Fundamento explicado no capítulo:** "Onde guardar a senha do banco com rotação automática?" → Secrets Manager.

**Pergunta:** "Guardar URLs e flags de configuração por ambiente sem custo."

**Resposta curta:** Parameter Store.


**Fundamento explicado no capítulo:** "Guardar URLs e flags de configuração por ambiente sem custo." → Parameter Store.


## 7. Fontes e próximos passos

Este capítulo explica os fundamentos e as opções do material. As fontes oficiais abaixo servem para conferir atualizações e detalhes de implementação; o roteiro de console não faz parte da CLF-C02.

### 🔗 Documentação oficial

- [Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) · [Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)

<!-- notas:inicio -->
## 📝 Minhas anotações

<!-- Escreva aqui suas observações, dúvidas e as questões que você errou sobre o tema. -->
<!-- notas:fim -->
