frase = 'Gosto da trilogia da Marvel'
print(frase.count('o'))
print(frase.count('A'))
print(frase.upper().count('A'))
print(len(frase))

frase2 = '  Gosto da trilogia da Marvel    '
print(len(frase2))
print(len(frase2.strip()))

print(frase.replace('da Marvel', 'de Harry Pother'))
frase = frase.replace('da Marvel', 'de Harry Pother')
print(frase)
print('trilogia' in frase)

frase = 'Gosto da trilogia da Marvel'
dividida = frase.split()
print(dividida)
print(dividida[0])
print(dividida[4][3])
