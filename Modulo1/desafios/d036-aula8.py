# Programa que leia o cumprimento de 3 retas e diga ao utilizador se elas podem ou não formar um triângulo
# um dos seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < (r2+r3) and r2 < (r3+r1) and r3 < (r1+r2):
    print('As medidas indicadas PODEM FORMAR UM TRIÂNGULO')
else:
     print('As medidas indicadas NÃO PODEM FORMAR UM TRIÂNGULO')