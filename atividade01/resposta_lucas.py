# animals = "sapo gato peixe rato serpente saci cavalo elefante"
# def animal_counter(animals: str) -> int:
#     animals_initials = [animal[0] for animal in animals.split()]
#     return len([item for item in animals_initials if animals_initials.count(item) > 1])


bichos = "garganta gato peixe rato serpente saci  carcamano cavalo elefante"

def find_copies(animais: str) -> int:
    lista_bichos = animais.split()
    print(f'Lista Bichos em ordem alfabética: {sorted(lista_bichos)}')
    print()

    print("Animais que começam com a mesma letra: ")
    contador = 0
    iniciais = [bicho[0] for bicho in lista_bichos]
    bichos_repetidos = set()
    for inicial in iniciais:
        if iniciais.count(inicial) > 1:
            contador += 1
            for bicho in lista_bichos:
                if bicho.startswith(inicial):
                    bichos_repetidos.add(bicho)
    print(sorted(bichos_repetidos))
    return contador

print(find_copies(bichos))