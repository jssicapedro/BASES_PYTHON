#Programa onde o utilizador possa escrever 7 números e submete-los numa única lista que mantenha os valores separados por valores pares e impares. No fim mostra os valores de forma crescente.

num = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input('Informe um valor: '))
    if valor % 2 == 0:
        num[0].append(valor) # adiciona o valor na posição 0 da variavel num -> na 1.º lista
    else:
        num[1].append(valor) 
num[0].sort()
num[1].sort()
print('='*5)
print('Valores pares e impares')
print('='*5)
print(f'Informou os valores {num}')
print('-'*5)
print(f'Os numeros pares foram: {num[0]}')
print('-'*5)
print(f'Os numeros pares foram: {num[1]}')