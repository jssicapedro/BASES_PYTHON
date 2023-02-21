# Programa que leia 1 número qualquer e mostre o seu fatorial
# ex: 5! = 5x4x3x2x1=120

"""COM MATH"""
"""from math import factorial
n = int(input('Indique um valor para calcular o fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f)) """

"""COM WHILE"""
n = int(input('Indique um valor para calcular o fatorial: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c-= 1
print('{}'.format(f))
