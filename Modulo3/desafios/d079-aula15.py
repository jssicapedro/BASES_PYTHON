# Programa que leia 5 valores numéricos e guarde num lista. No fim, mostra qual foi o maior e o menor valor e as suas respetivas posições.
numeros = []
maior = 0
menor = 0
for c in range(1, 6):
    n = int(input('Indique um valor: '))
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    numeros.append(n)
print(f'Informas-te a lista {numeros}')
print(f'O maior numero foi o número {maior} que se encontra nas posições ', end=' ')
for e, v in enumerate(numeros):
    if v == maior:
        print(f'{e}...', end=' ')
print(f'O menor numero foi o número {menor} que se encontra nas posições ', end=' ')
for e, v in enumerate(numeros):
    if v == menor:
        print(f'{e}...', end=' ')
