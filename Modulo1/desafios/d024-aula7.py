#Programa que leia um numero de 0 a 9999 e mostre na tela cada um dos dígitos separados
#  ex. 1834, mostra “unidade:4, dezena:3, centena:8 e milhar 1 ”

num = int(input('Indique um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))