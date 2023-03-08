# Programa que leia o nome e peso de várias pessoas, guardando tudo numa lista. NO fim deve mostrar:
# - Quantas pessoas foram submetidas
# - Uma listagem com as pessoas mais pesadas 
# - Uma listagem com as pessoas mais leves

pessoas = []
pessoa = []
peso = []
pessoapeso = []
r = ""
pesada = []
leve = []
quant = 0
while True:
    pessoa.append(str(input('Indique o nome de uma pessoa: ')))
    peso.append(float(input('Indique o peso: ')))
    pessoapeso.append(pessoa[:])
    pessoapeso.append(peso[:])
    pessoas.append(pessoapeso[:])
    r=str(input('Queres continuar? [S/N] '))
    for c in pessoa:
        quant += 1
        if c == 1:
            pesada = peso
            leve = peso
        else:
            if peso > pesada:
                pesada = peso
            if peso < leve:
                leve = peso
    if r in 'Nn':
        break
    pessoa.clear()
    peso.clear()
    pessoapeso.clear()
print(f'Informou a lista: {pessoas}')
print(f'Informou {quant} pessoas')
print(f'A pesoa mais pesada, pesa {pesada}')
print(f'A pesoa mais leve, pesa {leve}')