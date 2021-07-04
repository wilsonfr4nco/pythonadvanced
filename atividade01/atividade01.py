dic = {}
bichos = ['sapo', 'gato', 'peixe', 'rato', 'serpente', 'saci', 'cavalo', 'elefante']
x = sorted(bichos)
print(f'Lista ordenada de bichos:')
print(x)
print()

for contar in bichos:
    if contar:
        if contar[0] in dic:
            dic[contar[0]] = dic[contar[0]] + 1
        else:
            dic[contar[0]] = 1
print('Lista de Animais que começam com a mesma letra abaixo:')
print(dic)

