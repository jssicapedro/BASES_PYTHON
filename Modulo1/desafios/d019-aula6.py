""" Programa que lê um ângulo e mostra o valor do seno, cosseno e tangente desse ângulo. """

import math 
a = float(input('Escreva o ângulo que deseja: '))

""" é necessário converter o ângulo em radianos """
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tang = math.tan(math.radians(a))

print('O ângulo de {} tem o SENO de {:.2f} \nO ângulo de {} tem o COSSENO de {:.2f} \nO ângulo de {} tem a TANGENTE de {:.2f} \n'.format(a, sen, a, cos, a, tang))