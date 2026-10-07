# 🃏 Flashcards — Capítulo 0 — Fundamentos de TI

Clique na pergunta para ver a resposta. Gerado a partir da seção *Revisão* de cada aula (`python3 scripts/gerar_docs.py`).

**Total:** 21 cards


## [0.1 Computador, servidor e virtualização](../docs/fundamentos/01-servidor-e-virtualizacao.md)

<details markdown="1">
<summary>Qual é a diferença entre memória e armazenamento?</summary>

A memória guarda o que os programas estão usando agora e perde tudo quando a máquina desliga; o armazenamento guarda os dados de forma permanente, mas é mais lento.
</details>

<details markdown="1">
<summary>O que faz um computador ser um servidor?</summary>

O papel que ele cumpre: rodar um programa que espera pedidos de outros computadores (os clientes) e responde a eles.
</details>

<details markdown="1">
<summary>Para que serve o hipervisor?</summary>

Ele divide um computador físico em várias máquinas virtuais, reparte o hardware entre elas e mantém cada uma isolada das outras.
</details>

<details markdown="1">
<summary>Numa instância EC2, quem aplica os patches do sistema operacional?</summary>

O cliente. O sistema operacional da instância é o SO convidado, e a AWS é responsável só pelo que fica abaixo dele: hipervisor, máquina física e datacenter.
</details>


## [0.2 Rede: endereço IP, porta, DNS e HTTPS](../docs/fundamentos/02-rede.md)

<details markdown="1">
<summary>Qual é a diferença entre IP público e IP privado?</summary>

O IP público é único na internet e pode receber dados de qualquer lugar; o IP privado só vale dentro de uma rede interna e não é alcançável diretamente da internet.
</details>

<details markdown="1">
<summary>Para que serve a porta, se a máquina já tem um endereço IP?</summary>

O IP leva os dados até a máquina; a porta indica qual programa daquela máquina deve recebê-los.
</details>

<details markdown="1">
<summary>O que o DNS faz, e o que ele não faz?</summary>

O DNS traduz um nome de domínio no endereço IP do servidor; ele não protege o servidor nem garante que o site esteja funcionando.
</details>

<details markdown="1">
<summary>O que o HTTPS acrescenta ao HTTP?</summary>

Criptografia da conversa por TLS e um certificado que prova ao navegador que ele está falando com o site verdadeiro.
</details>

<details markdown="1">
<summary>O que faz uma sub-rede da VPC ser pública?</summary>

Ter, na sua tabela de rotas, uma rota para um internet gateway.
</details>


## [0.3 Dados: arquivo, bloco, objeto e banco de dados](../docs/fundamentos/03-dados.md)

<details markdown="1">
<summary>Qual é a diferença entre armazenamento em bloco e armazenamento de objetos?</summary>

No bloco, o sistema operacional formata o disco e altera pequenos trechos diretamente; no objeto, cada arquivo é gravado inteiro e lido por API, com uma chave e metadados, e mudar um trecho exige gravar o objeto de novo.
</details>

<details markdown="1">
<summary>Quando faz sentido usar armazenamento de arquivos?</summary>

Quando vários servidores precisam acessar os mesmos arquivos ao mesmo tempo, organizados em pastas.
</details>

<details markdown="1">
<summary>O que caracteriza um banco de dados relacional?</summary>

Dados em tabelas com esquema definido, que se relacionam entre si e são consultadas com SQL, com suporte a transações.
</details>

<details markdown="1">
<summary>Por que um banco não relacional escala com mais facilidade?</summary>

Porque as consultas são simples e cada item é encontrado pela sua chave, o que permite espalhar os dados por muitas máquinas.
</details>


## [0.4 Como programas conversam: API, requisição e fila](../docs/fundamentos/04-api-e-filas.md)

<details markdown="1">
<summary>O que é uma API?</summary>

O conjunto de operações que um programa oferece a outros programas, com as regras de como pedir cada uma.
</details>

<details markdown="1">
<summary>Qual é a diferença entre comunicação síncrona e assíncrona?</summary>

Na síncrona, quem chama espera a resposta para continuar; na assíncrona, quem chama deixa o pedido, por exemplo numa fila, e segue em frente sem esperar.
</details>

<details markdown="1">
<summary>Por que uma fila ajuda quando há um pico de pedidos?</summary>

Porque as mensagens se acumulam na fila e os consumidores as processam no próprio ritmo, sem sobrecarregar quem faz o trabalho.
</details>

<details markdown="1">
<summary>Quando usar um tópico em vez de uma fila?</summary>

Quando a mesma mensagem precisa chegar a vários programas ao mesmo tempo.
</details>


## [0.5 Segurança básica: identidade, autenticação, autorização e criptografia](../docs/fundamentos/05-seguranca-basica.md)

<details markdown="1">
<summary>Qual é a diferença entre autenticação e autorização?</summary>

Autenticação prova quem a identidade é; autorização decide o que essa identidade, já autenticada, pode fazer.
</details>

<details markdown="1">
<summary>Por que o MFA protege mesmo quando a senha vaza?</summary>

Porque exige uma segunda prova de outro tipo, normalmente algo que só o usuário tem, como um código gerado no celular.
</details>

<details markdown="1">
<summary>O que é o princípio do menor privilégio?</summary>

Dar a cada identidade só as permissões necessárias para o seu trabalho, nada além.
</details>

<details markdown="1">
<summary>Qual é a diferença entre criptografia em trânsito e em repouso?</summary>

Em trânsito protege os dados enquanto viajam pela rede, como no HTTPS; em repouso protege os dados guardados em disco, banco de dados ou objeto.
</details>
