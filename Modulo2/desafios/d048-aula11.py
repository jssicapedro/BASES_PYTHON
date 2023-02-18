# Programa que mostre todos os números pares que estão no intervalo de 1 a 50
print('-==-'*5)
print('NÚMEROS PARES ATÉ 50')
print('-==-'*5)
for c in range(1, 51):
    if c%2==0:
        print(c, end=' ')
