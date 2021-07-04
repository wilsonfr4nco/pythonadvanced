"""
Crie um programa que resolva anagramas
Tudo que ele precisa fazer é receber duas strings
E dizer se são anagramas
"""


def anagrama(palavra1,palavra2):
    palavra1, palavra2 = sorted(palavra1), sorted(palavra2)
    if palavra1 == palavra2:
        return 'anagrama'
    else:
        return 'não é anagrama'

if __name__ == '__main__':



