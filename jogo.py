from hangman_poo import Hangman
from aux_funcs import limpar_tela
from time import sleep

h = Hangman()
limpar_tela()
print('\n' * 3)
print('-' * 15, end=' ')
print('BEM VNDO AO JOGO DA FORCA', end=' ')
print('-' * 15)

h.imprimir_forca(h.chances)

while h.chances > 0:
    
    for l in h.lista_letras:
        print(l, end='')
        print(' ',end='')
    print('\n\n')
    
    if "_" in h.lista_letras:
        h.jogada()
    else:
        print('\nVocê acertou!')
        print('A palavra é: \n')
        print(f'\n{"".join(h.lista_letras)}')
        break

    sleep(2)
    limpar_tela()
    h.imprimir_forca(h.chances)


if h.chances == 0:
    print('ENFORCADO!\n')
    print(f'A palavra era: {h.palavra}')
print('-' * 50)