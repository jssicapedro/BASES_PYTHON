# Programa que leia um numero inteiro e mostre se é par ou ímpar

n = int(input('Escreva um numero: ').strip())

if n%2==0:
    print('O {} é PAR'.format(n))
else:
    print('O {} é ÍMPAR'.format(n))
