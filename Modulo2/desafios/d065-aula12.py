# Programa que leia vários números inteiros. O programa só vai parar quando o utilizador escrever o valor 999, que é a condição de parada. No final mostre quantos números foram escritos e qual é a soma deles (desconsiderando 999)
n = soma = cont = 0
n = int(input('Informe um número [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Informe um número [999 para parar]: '))
print('Escreveste {} números e a soma entre eles é de {}'.format(cont, soma))


"""
n = soma = cont = 0
while n != 999:
    n = int(input('Informe um número [999 para parar]: '))
    soma += n
    cont += 1
print('Escreveste {} números e a soma entre eles é de {}'.format(cont-1, soma-999))
"""
