import requests
from os import system, name

def limpar_tela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def buscar_palavra():

    link = "https://api.dicionario-aberto.net/random"

    req = requests.get(link)
    req = req.json()
    return req['word']
