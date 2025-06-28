import sys
import random

class Seg():
    def __init__(self, numero_secreto):
        self.numero_secreto = numero_secreto

    def distancia(self, N):
        if not isinstance(N, int):
            print("Erro: O argumento da função segredo.distancia(N) tem que ser um número inteiro!")
            sys.exit(-1)
        if N < -50 or N > 50:
            print("Erro: O argumento da função segredo.distancia(N) tem que ser um número entre -50 e 50!")
            sys.exit(-1)
        return abs(N - self.numero_secreto)

def testa(func):
    numero_secreto = random.randint(-5000, 5000)
    segredo = Seg(numero_secreto)

    x = func(segredo)

    if x == numero_secreto:
        print("Acertaste!\nA Flag é CD25{descobriste-o-numero-secreto}")
    else:
        print("Falhaste!")