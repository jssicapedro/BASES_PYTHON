# Programa que leia 2 valores e mostre um menu na tela
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# O programa deverá realizar a operação solicitada em cada caso
from time import sleep
soma = 0
multiplicar = 1
e = 0
maior = 0

n1 = int(input('Indique o 1.º valor: '))
n2 = int(input('Indique o 2.º valor: '))

while e != 5:
    print('-='*8)
    print('Menu dos numeros:')
    print('-='*8)
    print('Valores indicados: {} & {}'.format(n1, n2))
    e = int(input('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n>>>> Qual é a tua opção? '))
    if e == 1:
        soma = n1 + n2
        print('A soma foi de {}'.format(soma))
    if e == 2:
        multiplicar = n1 * n2
        print('A multiplicação foi de {}'.format(multiplicar))
    if e == 3:
        if n1 != n2:
            if n2 < n1:
                maior = n1
            if n1 < n2:
                maior = n2
            print('O maior número é {}'.format(maior))
        if n1 == n2:
            print('Os valores são iguais')
    if e == 4:
        print('-- NOVOS VALORES --:')
        n1 = int(input('Indique um novo valor: '))
        n2 = int(input('Indique outro novo valor: '))
    if e == 5:
        print('A encerrar...')
        sleep(1)
    else:
        print('Opção Inválido')
print('Adeus!')

