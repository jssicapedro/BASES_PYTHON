# Refazer o desafio 36 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - equilátero: todos os lados iguais
# - isósceles: 2 lados iguais
# - escaleno: todos os lados diferentes

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < (r2+r3) and r2 < (r3+r1) and r3 < (r1+r2):
    print('As medidas indicadas PODEM FORMAR UM TRIÂNGULO')
    if r1==r2==r3:
        print('Estas medidas formam um triângulo EQUILÁTERO')
    elif r1==r2 or r1==r3 or r2==r3:
        print('Estas medidas formam um triângulo ISÓSCELES')
    elif r1!=r2 and r2!=r3 and r3!=r1:
        print('Estas medidas formam um triângulo ESCALENO')
else:
     print('As medidas indicadas NÃO PODEM FORMAR UM TRIÂNGULO')
