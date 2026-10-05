#!/usr/bin/env python3
"""Regressões de significado, preservação de dados e cobertura da apresentação."""
import re
import unittest
from apostila import BASE, EXTRAS, Leitura, capitulo_servico, capitulo_topico
from gerar_docs import CATEGORIA, ARQUIVOS, parse_guia
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
            with self.subTest(ficha=nome):
                result=capitulo_servico(nome)
                for n in range(1, 8):
                    self.assertRegex(result, rf'(?m)^## {n}\. ', msg=nome)
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
            result=capitulo_topico(sec,corpo)
            for n in range(1,6):
                self.assertTrue(re.search(rf'^## {n}\. ',result,re.M),sec)
            for linha in corpo.splitlines():
                if linha.startswith('- ') and '→' in linha:
                    pergunta=linha[2:].split('→',1)[0].strip()
                    self.assertIn(pergunta,result,sec)

    def test_fifo_nao_promete_efeito_de_negocio_unico(self):
        s=capitulo_servico('sqs')
        self.assertIn('não garante sozinho efeitos de negócio apenas uma vez',s)
        self.assertIn('consumidor',s)
        self.assertIn('exclui',s)
        self.assertNotIn('"Garantir ordem e processamento exatamente uma vez."',s)


if __name__=='__main__':
    unittest.main()
