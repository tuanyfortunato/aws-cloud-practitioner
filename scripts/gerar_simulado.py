#!/usr/bin/env python3
"""Gera os bancos de questões por domínio a partir de scripts/banco_questoes.py.

Uso: python3 scripts/gerar_simulado.py

Saídas (sobrescritas a cada execução):
  simulados/questoes/dominio-N.md     questões agrupadas por domínio, para estudo
  simulados/questoes/README.md        índice dos domínios
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


def gerar_por_dominio():
    for d, (pasta, nome, peso) in DOMINIOS.items():
        destino = f"simulados/questoes/dominio-{d}.md"
        rng = random.Random(f"{SEMENTE}-{d}")
        questoes = sorted((q for q in QUESTOES if q["dominio"] == d),
                          key=lambda q: tuple(int(x) for x in q["secao"].split(".")))
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
               "2. Rode `python3 scripts/gerar_simulado.py`."]
    escrever("simulados/questoes/README.md", "\n".join(linhas))


def main():
    validar()
    gerar_por_dominio()
    multiplas = sum(1 for q in QUESTOES if len(q["corretas"]) > 1)
    print(f"{len(QUESTOES)} questões ({multiplas} de múltipla resposta): bancos por domínio gerados.")


if __name__ == "__main__":
    main()
