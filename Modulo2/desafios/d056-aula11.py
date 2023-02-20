# Programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e o menor peso de todos

maior = 0
menor = 0

for c in range(1, 5):
    peso = float(input('Indique o peso da {}.ª pessoa: '.format(c)))
    if c == 1: # o primeiro peso será o maior e menor no primeiro laço, depois ele ira analisar os próximos pesos.
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
