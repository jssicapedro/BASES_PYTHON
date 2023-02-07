""" Tipos primitivos e saída de dados """
valor = input('escreva um numero, um texto etc. ')
print(type(valor)) 

inteiro = int(input('Escreva um numero: '))
print(type(inteiro))

n1 = int(input('Escreva um valor: '))
n2 = int(input('Escreva outro valor: '))
s = n1+n2
print('A soma dos valores é: {}'.format(s))

n1 = int(input('Escreva um valor: '))
n2 = int(input('Escreva outro valor: '))
s = n1+n2
print('A soma de {} com {} é {}'.format(n1,n2,s))

var = input('Escreve algo: ')
print(var.isnumeric())

var = input('Escreve algo: ')
print(var.isalpha())

var = input('Escreve algo: ')
print(var.isalnum())

var = input('Escreve algo: ')
print(var.isupper())