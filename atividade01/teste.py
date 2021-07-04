d = {}

text = ['sapo', 'gato', 'peixe', 'rato', 'serpente', 'saci', 'cavalo', 'elefante']

for w in text:
    if w:                         # If we have the empty string. w[0] Does not Exist (DNE)
        if w[0] in d:             # Check to see if we have first character in dictionary.
            d[w[0]] = d[w[0]] + 1 # Use the first character as key to dictionary.
        else:                     # If character has not been found start counting.
            d[w[0]] = 1
print(d)


a = (1, 5, 3, 9)
x = max(a)
print(x)