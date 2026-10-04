#!/usr/bin/env python3
"""Verifica se todos os links relativos dos arquivos Markdown apontam para arquivos existentes.

Uso: python3 scripts/verificar_links.py
Sai com código 1 se encontrar link quebrado.
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r"\]\(([^)\s]+)\)")


def main():
    quebrados = []
    total = 0
    for pasta, _, arquivos in os.walk(RAIZ):
        # templates/ usa caminhos relativos ao local para onde o modelo será copiado.
        if "/.git" in pasta or os.path.relpath(pasta, RAIZ).startswith("templates"):
            continue
        for nome in arquivos:
            if not nome.endswith(".md"):
                continue
            caminho = os.path.join(pasta, nome)
            with open(caminho) as f:
                texto = re.sub(r"```.*?```", "", f.read(), flags=re.S)
            for alvo in LINK.findall(texto):
                if re.match(r"^(https?:|mailto:|#)", alvo):
                    continue
                total += 1
                destino = os.path.normpath(os.path.join(pasta, alvo.split("#")[0]))
                if not os.path.exists(destino):
                    quebrados.append(f"{os.path.relpath(caminho, RAIZ)} → {alvo}")
    for q in quebrados:
        print("QUEBRADO:", q)
    print(f"{total} links internos verificados, {len(quebrados)} quebrado(s).")
    sys.exit(1 if quebrados else 0)


if __name__ == "__main__":
    main()
