# Programa que leia 3 números e mostre qual o maior e o menor

n1 = float(input('Indique o 1.º numero: '))
n2 = float(input('Indique o 2.º numero: '))
n3 = float(input('Indique o 3.º numero: '))

if n1 > n2 and n1 > n3:
    print('{} é o maior numero.'.format(n1))
elif n2 > n1 and n2 > n3:
    print('{} é o maior numero.'.format(n2))
else:
    print('{} é o maior numero.'.format(n3))

if n1 < n2 and n1 < n3:
    print('{} é o menor numero.'.format(n1))
elif n2 < n1 and n2 < n3:
    print('{} é o menor numero.'.format(n2))
else:
    print('{} é o menor numero.'.format(n3))