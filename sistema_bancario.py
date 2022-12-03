#!/usr/bin/env python3

from datetime import datetime, timedelta

from rich.console import Console

from text_interface import *
from utils import *

operacoes_bancarias = []


def contador_saques():
    return len([1 for i in operacoes_bancarias if i['operacao'] == operacao_enum.SAQUE and eh_mesmo_dia(i['data'])])


def validacao_valor(valor: float):
    if valor > 0:
        return True
    print('Valor não pode ser menor ou igual a zero.')
    return False


def validacao_saque(valor: float):
    saldo = calcula_saldo()
    if saldo < valor:
        print(
            f'Valor do saque não pode ser maior que o saldo ({converte_real(saldo)}) em conta.')
        return False
    elif contador_saques() >= 3:
        print('Quantidade máxima de saques diários atingido.')
        return False
    return True


@normaliza_entrada
def sacar(valor: float):
    if validacao_valor(valor) and validacao_saque(valor):
        operacoes(valor, operacao_enum.SAQUE)
    else:
        print('Operação de saque não pode ser efetuada.')


@normaliza_entrada
def depositar(valor: float):
    if validacao_valor(valor):
        operacoes(valor, operacao_enum.DEPOSITO)
    else:
        print('Operação de depósito não pode ser efetuada.')


# função criada para unificar as regras caso exista alguma alteração mais geral
def operacoes(valor: float, operacao: operacao_enum):
    operacoes_bancarias.append({
        'data': data_atual_timestamp(),
        'operacao': operacao,
        'valor': valor
    })


def calcula_saldo():
    deposito = sum(
        [i['valor'] for i in operacoes_bancarias if i['operacao'] == operacao_enum.DEPOSITO])
    saque = sum([i['valor']
                for i in operacoes_bancarias if i['operacao'] == operacao_enum.SAQUE])
    return round(deposito - saque, 2)


def painel_saque():
    clear_screen()
    print(gerar_painel_saque())


def painel_deposito():
    clear_screen()
    print(gerar_painel_deposito())


def extrato():
    clear_screen()
    print(gerar_extrato(operacoes_bancarias))
    Console().print(
        f'  Saldo: {converte_real(calcula_saldo())}', highlight=False)


def menu():
    clear_screen()
    print(gerar_menu())


def main():
    while (True):
        menu()
        match str(input('Escolhar o opção desejada: ')).lower():
            case 'd':
                painel_deposito()
                valor = input_number(sucesso='Valor depositado com sucesso!')
                if valor:
                    depositar(valor)
                pressionar_enter()
            case 's':
                painel_saque()
                valor = input_number(sucesso='Valor sacado com sucesso!')
                if valor:
                    sacar(valor)
                pressionar_enter()
            case 'e':
                extrato()
                pressionar_enter()
            case 'q':
                break


def popula_com_operacoes_anteriores():
    operacoes_bancarias.append({
        'data':  (datetime.datetime.now() - timedelta(days=6)).timestamp(),
        'operacao': operacao_enum.DEPOSITO,
        'valor': 10000
    })

    for i in range(3):
        operacoes_bancarias.append({
            'data':  (datetime.datetime.now() - timedelta(days=i)).timestamp(),
            'operacao': operacao_enum.SAQUE,
            'valor': 10
        })


if __name__ == "__main__":
    # descomente essa função caso queria que venha populado com algumas operações para testes
    # lembre-se de comentar após os testes

    # popula_com_operacoes_anteriores()

    main()
