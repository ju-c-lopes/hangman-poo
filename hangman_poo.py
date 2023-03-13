import requests

def buscar_palavra():

    link = "https://api.dicionario-aberto.net/random"

    req = requests.get(link)
    req = req.json()
    return req['word']

class Hangman:
    
    def __init__(self, palavra=buscar_palavra()):
        self.correto = False
        self.palavra = palavra
        self.lista_letras = ["_"] * len(self.palavra)


h = Hangman()
print(h.palavra)

for i, l in enumerate(h.lista_letras):
    if i != len(h.lista_letras) - 1:
        print(l + " ", end="")
    else:
        print(l)
 