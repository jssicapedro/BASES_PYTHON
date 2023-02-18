# Programa que calcule a soma de todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500

s = 0 
count = 0

print('='*20)
print('Múltiplos de 3 até 500')
print('='*20)

for c in range(1, 501, 2):
    if c % 3 == 0:
        count +=1
        s += c
print('A soma de todos os {} valores solicitados é {}'.format(count, s))
