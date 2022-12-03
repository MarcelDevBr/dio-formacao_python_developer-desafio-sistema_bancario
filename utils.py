import datetime
import locale
import os
from enum import Enum
from time import sleep


class operacao_enum(Enum):
    DEPOSITO = 1
    SAQUE = 2


def eh_mesmo_dia(data):
    return datetime.datetime.now().date() == datetime.datetime.fromtimestamp(data).date()


def formata_data(data):
    return datetime.datetime.fromtimestamp(data).strftime("%d/%m/%Y %X")


def data_atual_timestamp():
    return datetime.datetime.now().timestamp()


def converte_real(valor: float):
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    return locale.currency(valor)


def normaliza_entrada(funcao):
    '''# Decorator para evitar problemas ponto flutuante no sistema sempre arredondando os valores para 2 casa'''
    def funcao_interna(valor): return funcao(round(valor, 2))
    return funcao_interna


def pressionar_enter():
    input('\nAperte enter para continuar...')


def input_number(mensagem='Digite um valor: ', erro='Número inválido. Digite novamente.', sucesso='Valor inserido com sucesso!'):
    while (True):
        try:
            valor = input(mensagem)
            if valor.lower() == 'q':
                break
            return float(valor.replace(',', '.'))
        except ValueError:
            print(erro)


def clear_screen():
    os.system('clear') if os.name == 'posix' else os.system('cls')
