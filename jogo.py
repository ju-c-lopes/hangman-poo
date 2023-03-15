from hangman_poo import Hangman
from aux_funcs import limpar_tela
from time import sleep

h = Hangman()
print(h.palavra)

print('\n"', end='')
for i, l in enumerate(h.lista_letras):
    if i != len(h.lista_letras) - 1:
        print(l + " ", end="")
    else:
        print(l, end="")
print('"\n\n')
h.imprimir_forca(h.chances)

while h.chances > 0:
    
    for l in h.lista_letras:
        print(l, end='')
        print(' ',end='')
    print('\n\n')
    
    if "_" in h.lista_letras:
        h.jogada()
    else:
        print(f'\n{"".join(h.lista_letras)}')
        print('\nVocê acertou!')
        break

    sleep(3)
    limpar_tela()
    print(h.palavra, "\n")
    h.imprimir_forca(h.chances)
