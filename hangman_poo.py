from aux_funcs import buscar_palavra

class Hangman:

    def __init__(self, palavra=buscar_palavra):

        self.palavra = palavra()
        self.lista_letras = ["_"] * len(self.palavra)
        self.chances = 6
        self.tentativas = []
        self.erros = [
            """
                    ________
                    |     |
                    |    \\0/
                    |     |
                    |    / \\
            """,
            """
                    ________
                    |     |
                    |    \\0/
                    |     |
                    |    /
            """,
            """
                    ________
                    |     |
                    |    \\0/
                    |     |
                    |
            """,
            """
                    ________
                    |     |
                    |    \\0/
                    |
                    |
            """,
            """
                    ________
                    |     |
                    |    \\0
                    |
                    |
            """,
            """
                    ________
                    |     |
                    |     0
                    |
                    |
            """,
            """
                    ________
                    |     |
                    |
                    |
                    |
            """,
        ]

    def jogada(self):
        print('\nDigite uma letra: ', end='')
        tentativa = input()
        
        while len(tentativa) != 1:
            if len(tentativa) < 1:
                print('\nVocê não digitou nada!')
                print('\nDigite uma letra: ', end='')
                tentativa = input()
            if len(tentativa) > 1:
                print('\nVocê digitou letras a mais!')
                print('\nDigite uma letra: ', end='')
                tentativa = input()

        if tentativa in self.lista_letras or tentativa in self.tentativas:
            print('\nVocê já digitou esta letra!')
        elif tentativa in self.palavra:
            for i, l in enumerate(self.palavra):
                if tentativa == l:
                    self.lista_letras[i] = tentativa
        else:
            self.tentativas.append(tentativa)
            self.chances -= 1
            print('\nLetra não encontrada!')

    def imprimir_forca(self, erro):
        print(f'Número de chances: {erro}')
        print('Status da forca...')
        print(f'\n{self.erros[erro]}')
