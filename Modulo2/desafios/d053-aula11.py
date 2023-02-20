# Programa que leia um numero inteiro e diga se ele é ou não numero primo
n = int(input('EScreva um numero: '))
total = 0
for c in range (1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, total))

if total == 2:
    print('{} é um número primo'.format(n))
else:
    print('{} não é um número primo'.format(n))