# Refazer o d010, mostrar a tabuada de um numero que o utilizador escolha

valor = int(input('Escreva um número para saber a sua tabuada: '))
print('\033[4mTABUADA DO {}\033[m'.format(valor))
print('-='*6)
for c in range(1, 11):
    print('{} x {} = {}'.format(valor, c, valor*c))
print('-='*6)
