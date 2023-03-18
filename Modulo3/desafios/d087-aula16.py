#Programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Informe um valor na posição {linha} x {coluna}: '))
print('-='*15)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-='*15)
