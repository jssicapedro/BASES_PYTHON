# Programa que faça o pc jogar pedra papel ou tesoura com o utilizador

import random
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = random.randint(0, 2)

print('As tuas opções:')
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')

x = int(input('Qual é a tua jogada? '))

print('Pedra')
sleep(0.5)
print('Papel')
sleep(0.5)
print('ou')
sleep(0.5)
print('Tesoura')
sleep(0.5)

print('=-='*8)
print('O pc escolheu {}\nE tu escolhes-te {}'.format(itens[pc], itens[x]))
print('=-='*8)

if pc == 0:
    if x == 0:
        print('EMPATE!')
    elif x == 1:
        print('GANHAS-TE')
    elif x == 2:
        print('PERDES-TE')
    else:
        print('opção inválida')
elif pc == 1:
    if x == 1:
        print('EMPATE!')
    elif x == 2:
        print('GANHAS-TE')
    elif x == 0:
        print('PERDES-TE')
    else:
        print('opção inválida')
elif pc == 2:
    if x == 2:
        print('EMPATE!')
    elif x == 0:
        print('GANHAS-TE')
    elif x == 1:
        print('PERDES-TE')
    else:
        print('opção inválida')


print('Foi um bom jogo')
