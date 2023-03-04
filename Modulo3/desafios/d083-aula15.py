# Programa que vai ler vários números e coloca-los numa lista. Depois, cria 2 listas extras que vão conter apenas os valores pares e os valores impares respetivamente. No fim, mostra os valores das 3 listas.
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Informe um valor: ')))
    resp = str(input('Queres continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista {num}')
print(f'Os numeros pares são: {pares}')
print(f'Os numeros impares são: {impares}')
