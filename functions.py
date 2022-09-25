import locale
import json
import requests


def pegar_cota(cotacao):
    """
    :param cotacao: dicionário com as cotações e outras informações
    a função extrai apenas os valores das cotações
    :return: retorna os valores das cotações em formato de tupla para uma variavel.
    """
    cota_dolar = cotacao['USDBRL']['bid']
    cota_euro = cotacao['EURBRL']['bid']
    cota_btc = cotacao['BTCBRL']['bid']
    return cota_dolar, cota_euro, cota_btc

def cotar():
    """
    pega a cotação do dolar, euro e bitcoin, em tempo real.
    :return: retorna um arquivo em formato .json com as cotações, em um dicionário.
    """
    cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacao = cotacao.json()
    return cotacao

def moeda(x):
    """
    formata valores para a moeda Real
    retorna o valor formatado
    """
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    valor = locale.currency(x)
    return valor

def mudar(cota_dolar, cota_euro, cota_btc):
    """
    :param cota_dolar: cotação em formato de string
    :param cota_euro: cotação em formato de string
    :param cota_btc: cotação em formato de string
    muda os formatos de strings para float de todas as cotações enviadas por parâmetros.
    :return: retorna uma tupla dos valores float para uma variável.
    """
    cota_dolar = float(cota_dolar)
    cota_euro = float(cota_euro)
    cota_btc = float(cota_btc)
    return cota_dolar, cota_euro, cota_btc

def mostrar(cota_dolar, cota_euro, cota_btc):
    """
    mostra na tela os valores das cotações
    """
    print(f'O Valor de 1 um Dolar hoje é de: {cota_dolar}'.title())
    print(f'O Valor de 1 um Euro hoje é de: {cota_euro}'.title())
    print(f'O Valor de 1 um Bitcoin hoje é de: {cota_btc}'.title())

def calculo(carteira, cota_dolar, cota_euro, cota_btc):
    """
    recebe por parâmetro o valor digitado pelo usuario e calcula de acordo com os valores das cotações.
    :return: retorna os valores calculados como um tupla.
    """
    carteira_dolar = carteira / cota_dolar
    carteira_euro = carteira / cota_euro
    carteira_btc = (carteira / 1000) / cota_btc
    return carteira_dolar, carteira_euro, carteira_btc


def mostrar_atual(carteira, carteira_dolar, carteira_euro, carteira_btc):
    """
    Mostra na tela o valor digitado pelo usuario e os valores calculado com base na cotação do dia.
    """
    print(f'Sua carteita de: {carteira}\nvale: {carteira_dolar:.2f} em dolar, {carteira_euro:.2f} em Euro,'
          f' {carteira_btc:.4f} em Bitcoin. Na cotação de hoje.'.title())