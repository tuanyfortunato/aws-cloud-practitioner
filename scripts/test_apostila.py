#!/usr/bin/env python3
"""Regressões de significado, preservação de dados e cobertura da apresentação."""
import os
import re
import shutil
import tempfile
import unittest
import gerar_docs
from apostila import BASE, EXTRAS, Leitura, capitulo_servico, capitulo_topico, fundamentos_resposta
from didatica_docs import TOPICOS as DIDATICA
from gerar_docs import (AUTORAL, CATEGORIA, ARQUIVOS, caminho_ficha, caminho_topico,
                        eh_autoral, extrair_cards_revisao, parse_guia)
from vocabulario_apostila import termos_locais, simples


class Apostila(unittest.TestCase):
    def test_siglas_nao_sao_artigos_ou_conjuncoes(self):
        nomes = [n for n, _ in termos_locais('A escola escolhe uma máquina ou outra.', EXTRAS)]
        self.assertNotIn('OU', nomes)
        self.assertNotIn('A', nomes)
        self.assertTrue(any('OU' == n for n, _ in termos_locais('Uma OU organiza contas.', EXTRAS)))

    def test_nome_de_produto_nao_substitui_termo_comum(self):
        nomes = [n for n, _ in termos_locais('processamento batch e uma relação entre dados', EXTRAS)]
        self.assertNotIn('Batch', nomes)
        self.assertNotIn('Relação', nomes)

    def test_tabela_de_opcoes_preserva_valores_unidades_e_links(self):
        s='| Opção | Detalhe |\n|---|---|\n| Retenção | 4 dias; até 14 dias. [fonte](https://example.com/guia) |'
        result=Leitura().trecho(s)
        self.assertIn('4 dias; até 14 dias.', result)
        self.assertIn('[fonte](https://example.com/guia)', result)
        self.assertNotIn('| Retenção |', result)

    def test_comparacao_continua_legivel_com_mesmos_criterios(self):
        s='| Família | Uso |\n|---|---|\n| T | Uso geral |\n| C | CPU intensa |'
        self.assertIn(s, Leitura().trecho(s))

    def test_codigo_e_diagrama_nao_recebem_markdown_dentro(self):
        for bloco in ('```mermaid\nflowchart TD\nA[API] --> B[SQS]\n```',
                      '```json\n{"IAM": "role", "CPU": 2}\n```'):
            self.assertIn(bloco, Leitura().trecho(bloco))

    def test_cobertura_e_conservacao_das_referencias(self):
        self.assertEqual(set(BASE), set(CATEGORIA))
        for nome, fonte in BASE.items():
            if eh_autoral(caminho_ficha(nome)):
                continue  # ficha escrita à mão: não passa pelo gerador
            with self.subTest(ficha=nome):
                result=capitulo_servico(nome)
                # A numeração das seções é sequencial e só existe seção com conteúdo próprio.
                numeros=[int(n) for n in re.findall(r'(?m)^## (\d+)\. ',result)]
                self.assertEqual(numeros,list(range(1,len(numeros)+1)),nome)
                self.assertGreaterEqual(len(numeros),5,nome)
                self.assertRegex(result,r'(?m)^## \d+\. Fontes e próximos passos$',nome)
                links=set(re.findall(r'\]\(([^)\s]+)\)',fonte))
                self.assertTrue(links <= set(re.findall(r'\]\(([^)\s]+)\)',result)),nome)
                # Unidades e números da fonte não podem desaparecer ao abrir uma tabela.
                numeros=set(re.findall(r'\b\d[\d.,]*\s*(?:MiB|GiB|TiB|KB|MB|GB|TB|PB|%|dias|min|segundos|horas)\b',simples(fonte)))
                for valor in numeros:
                    self.assertIn(valor,simples(result),f'{nome}: {valor}')

    def test_capitulos_de_topicos_e_perguntas_preservados(self):
        secoes, _, _=parse_guia()
        self.assertEqual(set(secoes),set(ARQUIVOS))
        for sec,(_,corpo) in secoes.items():
            if eh_autoral(caminho_topico(sec)):
                continue  # aula escrita à mão: não passa pelo gerador
            result=capitulo_topico(sec,corpo)
            for n in range(1,6):
                self.assertTrue(re.search(rf'^## {n}\. ',result,re.M),sec)
            for linha in corpo.splitlines():
                if linha.startswith('- ') and '→' in linha:
                    pergunta=linha[2:].split('→',1)[0].strip()
                    self.assertIn(pergunta,result,sec)

    def test_fundamento_nao_repete_pergunta_nem_gabarito(self):
        corpo = ('- "Licença por núcleo físico." → Dedicated Host\n'
                 '- **Cai na prova:** "licença por núcleo físico" = Dedicated Host.\n'
                 '- **Modelos de compra:** o Dedicated Host entrega servidor físico dedicado, '
                 'o que permite usar licenças contadas por núcleo.\n')
        fundamento = fundamentos_resposta('"Licença por núcleo físico."', 'Dedicated Host', corpo)
        self.assertIn('servidor físico dedicado', fundamento)
        self.assertNotIn('Cai na prova', fundamento)
        lista = '- **Cai na prova:** "licença de software por núcleo" = Dedicated Host; "tolera interrupção" = Spot.\n'
        self.assertEqual(fundamentos_resposta('"Algo bem diferente aqui."', 'Spot', lista), '')
        self.assertNotIn('→', fundamento)

    def test_revisao_nao_repete_a_abertura_da_aula(self):
        secoes, _, _=parse_guia()
        for sec,(_,corpo) in secoes.items():
            if eh_autoral(caminho_topico(sec)):
                continue
            result=capitulo_topico(sec,corpo)
            self.assertNotIn('Confira se você compreendeu',result,sec)
            for campo in ('problema','simples','limite'):
                self.assertNotIn(DIDATICA[sec][campo],result,f'{sec}: {campo}')

    def test_fifo_nao_promete_efeito_de_negocio_unico(self):
        s=capitulo_servico('sqs')
        self.assertIn('não garante sozinho efeitos de negócio apenas uma vez',s)
        self.assertIn('consumidor',s)
        self.assertIn('exclui',s)
        self.assertNotIn('"Garantir ordem e processamento exatamente uma vez."',s)


class Autoral(unittest.TestCase):
    """Aulas e fichas com <!-- autoral --> são a fonte da verdade e não são reescritas."""

    AULA = """<!-- autoral -->

# 2.1 Aula escrita à mão

Texto autoral que o gerador não deve tocar.

## Revisão

### Quem protege o hipervisor?

A AWS. Ela opera o hardware e a camada de virtualização.

Parágrafo extra que fica só na aula.

### Quem aplica patches no sistema operacional do EC2?

O cliente, porque a instância é dele.
"""

    def test_marcador_vale_so_no_topo(self):
        with tempfile.TemporaryDirectory() as tmp:
            topo = os.path.join(tmp, 'topo.md')
            fundo = os.path.join(tmp, 'fundo.md')
            with open(topo, 'w') as f:
                f.write(self.AULA)
            with open(fundo, 'w') as f:
                f.write('# Aula gerada\n' + '\nlinha\n' * 20 + AUTORAL + '\n')
            self.assertTrue(eh_autoral(topo))
            self.assertFalse(eh_autoral(fundo))
            self.assertFalse(eh_autoral(os.path.join(tmp, 'inexistente.md')))

    def test_gerador_nao_reescreve_aula_autoral(self):
        secoes, _, _ = parse_guia()
        raiz_real = gerar_docs.RAIZ
        with tempfile.TemporaryDirectory() as tmp:
            caminho = os.path.join(tmp, caminho_topico('2.1'))
            os.makedirs(os.path.dirname(caminho), exist_ok=True)
            with open(caminho, 'w') as f:
                f.write(self.AULA)
            shutil.copy(os.path.join(raiz_real, 'README.md'), os.path.join(tmp, 'README.md'))
            gerar_docs.RAIZ = tmp
            try:
                ordem = gerar_docs.gerar_topicos(secoes)
            finally:
                gerar_docs.RAIZ = raiz_real
            with open(caminho) as f:
                self.assertEqual(f.read(), self.AULA)
            # As demais aulas continuam sendo geradas.
            self.assertIn('2.1', ordem)
            outra = os.path.join(tmp, caminho_topico('2.2'))
            self.assertTrue(os.path.exists(outra))

    def test_flashcards_da_aula_autoral_vem_da_revisao(self):
        cards = extrair_cards_revisao(self.AULA)
        self.assertEqual(len(cards), 2)
        self.assertEqual(cards[0][0], 'Quem protege o hipervisor?')
        self.assertEqual(cards[0][1], 'A AWS. Ela opera o hardware e a camada de virtualização.')
        self.assertNotIn('Parágrafo extra', cards[0][1])
        self.assertEqual(extrair_cards_revisao('# Aula sem revisão\n\nTexto.\n'), [])
        recolhida = ('## Revisão\n\n### O que é IP?\n\n<details>\n<summary>Ver resposta</summary>\n\n'
                     'O endereço de uma máquina na rede.\n\nComentário longo.\n\n</details>\n')
        self.assertEqual(extrair_cards_revisao(recolhida), [('O que é IP?', 'O endereço de uma máquina na rede.')])


if __name__=='__main__':
    unittest.main()
