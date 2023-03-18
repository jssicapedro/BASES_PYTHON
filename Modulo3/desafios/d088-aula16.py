# Melhora o desafio anterior, mostra no fim:
# - A soma de todos os valores pares
# - A soma dos valores da 3.ª coluna
# - O maior valor da 2.ª linha

matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
somaPares = soma3coluna = maior2linha = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Informe um valor na posição {linha} x {coluna}: '))

print('-='*15)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]
    print()
print('-='*15)
print(f'A soma de todos os numeros pares são: {somaPares}')
for linha in range(0,3):
    soma3coluna += matriz[linha][2]
print(f'A soma de todos os numeros da coluna 3 são: {soma3coluna}')
for coluna in range(0,3):
    if maior2linha < matriz[1][coluna]:
        maior2linha = matriz[1][coluna] 
print(f'O maior valor da linha 2 é: {maior2linha}')
