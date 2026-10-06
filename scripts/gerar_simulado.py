#!/usr/bin/env python3
"""Gera os bancos de questões por domínio a partir de scripts/banco_questoes.py.

Uso: python3 scripts/gerar_simulado.py

Saídas (sobrescritas a cada execução):
  simulados/questoes/dominio-N.md     questões agrupadas por domínio, para estudo
  simulados/questoes/README.md        índice dos domínios
  simulados/questoes/rastreabilidade.md   task oficial do exame → aulas → questões (AP-13)
"""
import os
import random
from collections import Counter
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from banco_questoes import QUESTOES  # noqa: E402
from gerar_docs import ARQUIVOS, DOMINIOS, RAIZ, caminho_topico, escrever, rel  # noqa: E402

SEMENTE = 2026
LETRAS = "ABCDE"

# Task statements do guia oficial do exame (conferidas em 06/10/2026 nas páginas Content Domain 1 a 4)
# e as aulas que as ensinam. Mantenha alinhado com a tabela de docs/00-guia-do-exame/escopo-oficial.md.
GUIA_EXAME = "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain{d}.html"
TAREFAS = [
    ("1.1", "Define the benefits of the AWS Cloud", ["1.1", "1.2", "3.2"]),
    ("1.2", "Identify design principles of the AWS Cloud", ["1.3", "1.4"]),
    ("1.3", "Understand the benefits of and strategies for migration to the AWS Cloud", ["1.5", "1.6", "3.17"]),
    ("1.4", "Understand concepts of cloud economics", ["1.7"]),
    ("2.1", "Understand the AWS shared responsibility model", ["2.1"]),
    ("2.2", "Understand AWS Cloud security, governance, and compliance concepts", ["2.5", "2.6", "2.7"]),
    ("2.3", "Identify AWS access management capabilities", ["2.2", "2.3", "2.4"]),
    ("2.4", "Identify components and resources for security", ["2.8", "2.9", "2.10"]),
    ("3.1", "Define methods of deploying and operating in the AWS Cloud", ["3.1", "3.16"]),
    ("3.2", "Define the AWS global infrastructure", ["3.2"]),
    ("3.3", "Identify AWS compute services", ["3.3", "3.4", "3.5", "3.6"]),
    ("3.4", "Identify AWS database services", ["3.7", "3.17"]),
    ("3.5", "Identify AWS network services", ["3.10"]),
    ("3.6", "Identify AWS storage services", ["3.8", "3.9"]),
    ("3.7", "Identify AWS artificial intelligence and machine learning (AI/ML) services and analytics services",
     ["3.11", "3.12"]),
    ("3.8", "Identify services from other in-scope AWS service categories", ["3.13", "3.14", "3.15", "3.18"]),
    ("4.1", "Compare AWS pricing models", ["4.1", "4.2", "4.3"]),
    ("4.2", "Understand resources for billing, budget, and cost management", ["4.4"]),
    ("4.3", "Identify AWS technical resources and AWS Support options", ["4.5", "4.6"]),
]


def validar():
    for i, q in enumerate(QUESTOES, 1):
        assert q["dominio"] in DOMINIOS, f"Questão {i}: domínio {q['dominio']} inexistente"
        total = len(q["corretas"]) + len(q["erradas"])
        esperado = 4 if len(q["corretas"]) == 1 else 5
        assert total == esperado, f"Questão {i}: {total} alternativas, esperado {esperado}"
        assert q["secao"] in ARQUIVOS, f"Questão {i}: seção {q['secao']} inexistente"


def montar(q, rng):
    """Embaralha as alternativas e devolve (lista de (letra, texto), letras corretas)."""
    alternativas = [(t, True) for t in q["corretas"]] + [(t, False) for t in q["erradas"]]
    rng.shuffle(alternativas)
    opcoes = [(LETRAS[i], texto) for i, (texto, _) in enumerate(alternativas)]
    corretas = [LETRAS[i] for i, (_, ok) in enumerate(alternativas) if ok]
    return opcoes, corretas


def bloco_questao(numero, q, opcoes, corretas, destino):
    multipla = len(corretas) > 1
    tipo = " · **múltipla resposta**" if multipla else ""
    link = rel(destino, caminho_topico(q["secao"]))
    linhas = [f"### Questão {numero}", "",
              f"<sub>Domínio {q['dominio']} · tópico [{q['secao']}]({link}){tipo}</sub>", "",
              q["enunciado"], ""]
    linhas += [f"- **{letra})** {texto}" for letra, texto in opcoes]
    linhas += ["", "<details>", "<summary>Ver resposta</summary>", "",
               f"**Resposta: {', '.join(corretas)}**", "", q["explicacao"], "", "</details>", ""]
    return "\n".join(linhas)


def ordenar(questoes):
    return sorted(questoes, key=lambda q: tuple(int(x) for x in q["secao"].split(".")))


def numeracao():
    """Número de cada questão no arquivo do seu domínio (mesma ordem de gerar_por_dominio)."""
    numeros = {}
    for d in DOMINIOS:
        for n, q in enumerate(ordenar(q for q in QUESTOES if q["dominio"] == d), 1):
            numeros[id(q)] = n
    return numeros


def titulo_aula(secao):
    with open(os.path.join(RAIZ, caminho_topico(secao))) as f:
        for linha in f:
            if linha.startswith("# "):
                return linha[2:].strip()
    raise AssertionError(f"Aula {secao} sem título")


def gerar_rastreabilidade():
    destino = "simulados/questoes/rastreabilidade.md"
    ensinadas = {s for _, _, aulas in TAREFAS for s in aulas}
    faltando = [s for s in ARQUIVOS if s not in ensinadas]
    assert not faltando, f"Aulas sem task oficial em TAREFAS: {faltando}"
    numeros = numeracao()
    linhas = ["# 🧭 Rastreabilidade: task oficial → aula → questões", "",
              "Cada linha liga uma *task statement* do [guia oficial do exame]"
              "(https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html) "
              "às aulas que a ensinam e às questões que a praticam. As tasks foram conferidas em 06/10/2026.", "",
              "A numeração das aulas (1.1 a 4.6) não é a mesma das tasks oficiais. Uma aula pode servir a mais de uma "
              "task, como a 3.2 (benefícios da nuvem e infraestrutura global) e a 3.17 (migração e serviços de banco "
              "de dados); nesse caso, as questões dela aparecem nas duas linhas.", "",
              "⬅️ [Todas as questões por domínio](README.md)", "", "---", ""]
    resumo = ["| Task oficial | Aulas | Questões |", "|---|---|---|"]
    detalhe = []
    for tarefa, texto, aulas in TAREFAS:
        d = tarefa.split(".")[0]
        ancora = f"{GUIA_EXAME.format(d=d)}#cloud-practitioner-02-task{tarefa}"
        links_aulas = " · ".join(f"[{s}]({rel(destino, caminho_topico(s))})" for s in aulas)
        total = sum(1 for q in QUESTOES if q["secao"] in aulas)
        assert total, f"Task {tarefa} sem nenhuma questão"
        resumo.append(f"| [{tarefa}](#task-{tarefa.replace('.', '')}) | {links_aulas} | {total} |")
        detalhe += [f'<a id="task-{tarefa.replace(".", "")}"></a>', "",
                    f"## Task {tarefa}: {texto}", "", f"Fonte: [Content Domain {d}]({ancora})", "",
                    "| Aula | Questões |", "|---|---|"]
        for s in aulas:
            qs = [q for q in QUESTOES if q["secao"] == s]
            refs = " · ".join(f"[D{q['dominio']} Q{numeros[id(q)]}](dominio-{q['dominio']}.md#questão-{numeros[id(q)]})"
                              for q in ordenar(qs))
            detalhe.append(f"| [{titulo_aula(s)}]({rel(destino, caminho_topico(s))}) | {refs} |")
        detalhe.append("")
    linhas += ["## Resumo", ""] + resumo + [""] + detalhe
    linhas += ["## Como manter", "",
               "- A lista de tasks e de aulas fica em `TAREFAS` de "
               "[`scripts/gerar_simulado.py`](../../scripts/gerar_simulado.py); a tabela de tasks do "
               "[escopo oficial](../../docs/00-guia-do-exame/escopo-oficial.md) deve dizer o mesmo.",
               "- O gerador falha se uma aula não estiver ligada a nenhuma task ou se uma task ficar sem questão.",
               "- Ao dividir, renumerar ou reordenar aulas, atualize `TAREFAS` e rode `python3 scripts/gerar_simulado.py`.",
               "- Reabra as páginas do guia oficial antes de cada revisão: a AWS muda o conteúdo sem trocar o código "
               "da prova.", "",
               "## Limites", "",
               "- A tabela mostra que cada task tem aula e questões; ela não mede se as questões cobrem todos os "
               "itens de \"Knowledge of\" e \"Skills in\" de cada task.",
               "- As fontes de cada afirmação ficam na seção \"Fontes oficiais\" de cada aula e ficha, com a data "
               "da verificação; o que não foi confirmado fica nas "
               "[pendências de verificação](../../docs/00-guia-do-exame/pendencias-de-verificacao.md)."]
    escrever(destino, "\n".join(linhas))


def gerar_por_dominio():
    for d, (pasta, nome, peso) in DOMINIOS.items():
        destino = f"simulados/questoes/dominio-{d}.md"
        rng = random.Random(f"{SEMENTE}-{d}")
        questoes = ordenar(q for q in QUESTOES if q["dominio"] == d)
        partes = [f"# ❓ Questões — {nome} ({peso})", "",
                  f"{len(questoes)} questões no formato da prova, em ordem de tópico. "
                  "Responda antes de abrir \"Ver resposta\".", "",
                  "⬅️ [Todas as questões por domínio](README.md)", "", "---", ""]
        for n, q in enumerate(questoes, 1):
            opcoes, corretas = montar(q, rng)
            partes.append(bloco_questao(n, q, opcoes, corretas, destino))
        escrever(destino, "\n".join(partes))

    contagem = Counter(q["dominio"] for q in QUESTOES)
    linhas = ["# ❓ Questões por domínio", "",
              "Questões no formato da prova, agrupadas por domínio e tópico para estudo direcionado.", "",
              "| Domínio | Peso | Questões |", "|---|---|---|"]
    for d, (_, nome, peso) in DOMINIOS.items():
        linhas.append(f"| [{nome}](dominio-{d}.md) | {peso} | {contagem[d]} |")
    linhas += ["", "## Adicionar questões", "",
               "1. Inclua a questão em [`scripts/banco_questoes.py`](../../scripts/banco_questoes.py) "
               "(enunciado, alternativas corretas, distratores e explicação).",
               "2. Rode `python3 scripts/gerar_simulado.py`.", "",
               "A [rastreabilidade](rastreabilidade.md) liga cada *task* oficial do exame às aulas e às questões."]
    escrever("simulados/questoes/README.md", "\n".join(linhas))


def main():
    validar()
    gerar_por_dominio()
    gerar_rastreabilidade()
    multiplas = sum(1 for q in QUESTOES if len(q["corretas"]) > 1)
    print(f"{len(QUESTOES)} questões ({multiplas} de múltipla resposta): bancos por domínio gerados.")


if __name__ == "__main__":
    main()
