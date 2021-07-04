#! /usr/bin/python

# import sys
#
# valor1 = sys.argv[1]
# valor2 = sys.argv[2]
# resultado = int(valor1) + int(valor2)
#
# print(resultado)
import time
from random import choice

def soma(x, y):
    z = choice(range(100))
    return x + y + z

def subtracao(x, y):
    return x - y

if __name__ == '__main__':
    print(soma(3, 8))
    print(subtracao(3, 8))

