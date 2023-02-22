# Programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador perder, mostrando o total de vitorias consecutivas o utilizador conquistou até ao final do jogo

import random
from time import sleep
ganha = 0
while True:
    n = int(input('Indique um número: '))
    pc = random.randint(0, 10)
    soma = pc + n
    tipo = ''
    while tipo != 'P' and tipo != 'I':
        tipo = str(input('PAr ou impar? [P/I] ')).strip().upper()[0]
    print(f'Escreves-te {n} e o pc {pc}. Total de {soma}')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if soma % 2 == 0:
            print('GANHAS-TE')
            ganha += 1
        else:
            print('PERDES-TE')
            break
    elif tipo == 'I':
        if soma % 2 != 0:
            print('GANHAS-TE')
            ganha += 1
        else:
            print('PERDES-TE')
            break
    print('Vamos jogar denovo')
print('G', end='')
sleep(0.5)
print('A', end='')
sleep(0.5)
print('M', end='')
sleep(0.5)
print('E', end=' ')
sleep(0.5)
print('O', end='')
sleep(0.5)
print('V', end='')
sleep(0.5)
print('E', end='')
sleep(0.5)
print('R')
print(f'Ganhas-te {ganha} vezes')
