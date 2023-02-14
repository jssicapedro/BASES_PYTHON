palavra = 'python'
print(palavra[3])

frase = 'Estou a gostar de Python'

""" Fatiar """
print(frase[3])
print(frase[9:13])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

""" Analisar """
print(len(frase))
print(frase.count('o'))
print(frase.count('a', 0, 13))
print(frase.find('de'))
print(frase.find('oi'))
print('Python' in frase)

""" Transformação """
print(frase.replace('Python', 'C++'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
a = '   Estou a gostar de  '
print(a.strip())
print(a.rstrip())
print(a.lstrip())

""" Divisão """
print(frase.split())

""" Junção """
lista=['Estou', 'a', 'gostar', 'de', 'Python']
print('-'.join(lista))