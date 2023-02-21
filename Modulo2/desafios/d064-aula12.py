# Programa que leia um número inteiro e mostre na tela os primeiros elementos de uma sequência de Fibonacci
# a sequência de fibonacci é a soma dos 2 numeros anteriores e tem inicio em 0
# ex. 0,1,1,2,3,5,8,13,21

print('*'*25)
print('Sequência de Fibonacci')
print('*'*25)
n = int(input('Quantos termos queres mostrar? '))
t0 = 0
t1 = 1
print('{} -> {}'.format(t0, t1), end='')
cont=3
while cont <= n:
    t2 = t0 + t1
    print(' -> {} '.format(t2), end='')
    t0 = t1
    t1 = t2
    cont += 1
print('-> FIM')
