from rich import box, panel, print, table
from rich.align import Align
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from utils import converte_real, formata_data, operacao_enum


def gerar_menu():
    conteudo = f'''
\[s] Sacar
\[d] Depositar
\[e] Visualizar extrato

\[q] Sair
'''
    return Panel.fit(conteudo, title='[blue]Sistema Bancário')


def gerar_extrato(operacoes_bancarias: list):
    t = Table(title="EXTRATO BANCÁRIO", box=box.SIMPLE, show_footer=True)
    t.add_column("Data")
    t.add_column("Operação")
    t.add_column("Valor", justify="right")

    for i in operacoes_bancarias:
        data = formata_data(i['data'])
        operacao = 'DEPÓSITO' if operacao_enum.DEPOSITO == i['operacao'] else 'SAQUE'
        valor = converte_real(i['valor'])
        t.add_row(data, operacao, valor)
    return t


def gerar_painel_saque():
    conteudo = f'''
Para o saque são aceitos valores nos seguintes
formatos como por exemplo: 1000, 1000.50 ou 1000,50

Observação: você tem um limite de 3 saques diários

[Q] Para voltar sem efetua o depósito
'''
    return Panel.fit(conteudo, title='[blue]Saque')


def gerar_painel_deposito():
    conteudo = f'''
Para o depósito são aceitos valores nos seguintes
formatos como por exemplo: 1000, 1000.50 ou 1000,50

[Q] Para voltar sem efetua o depósito
'''
    return Panel.fit(conteudo, title='[blue]Depósito')
