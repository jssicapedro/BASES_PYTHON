""" Na aula de projeto da faculdade há 4 grupos e os professores querem sortear  a ordem da apresentação de cada grupo. Faz um programa que leia o nome dos grupos e mostra a ordem sorteada. """

import random
g1 = str(input('Grupo 1: '))
g2 = str(input('Grupo 2: '))
g3 = str(input('Grupo 3: '))
g4 = str(input('Grupo 4: '))

lista = [g1, g2, g3, g4]
random.shuffle(lista)

print('A ordem de apresentação é {}'.format(lista))