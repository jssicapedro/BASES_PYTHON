# Programa onde o utilizador pode escrever vários valores numéricos e guarda-os numa lista. Caso o numero já exista na lista, ele não vai ser adicionado. No fim, serão exibidos todos os valores únicos escritos em ordem crescente.
num = []
while True:
    n = int(input('Indique um valor: '))
    if n not in num:
        num.append(n)
    else:
        print('Esse valor já está na lista, não o vou adicionar...')
    r = input('Quer continuar? [S/N] ').strip().upper()
    if r != 'S':
        break
num.sort()
print(f'Lista: {num}')
