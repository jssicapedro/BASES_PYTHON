""" Algoritmo que leia um número e mostre o dobro, triplo e a raiz quadrada """
valor =int(input('Escreva um número: '))
dobro = valor*2
triplo = valor*3
raiz = pow(valor, (1/2))
print('O dobro de {} é {} \nJá o seu triplo é {}\nE a sua raiz quadrada é {:.2f}'.format(valor, dobro, triplo, raiz))