# Programa que leia o nome e peso de várias pessoas, guardando tudo numa lista. NO fim deve mostrar:
# - Quantas pessoas foram submetidas
# - Uma listagem com as pessoas mais pesadas 
# - Uma listagem com as pessoas mais leves


dadosTemp, dadosPessoa = [], []
maior, menor = 0, 0

while True:
    dadosTemp.append(input('NOME: ').strip().capitalize())
    dadosTemp.append(float(input('PESO: ')))
    print('-' * 30)

    # Maior e menor peso entre os dados informados
    if len(dadosPessoa) == 0:
        maior = menor = dadosTemp[1]
    elif dadosTemp[1] > maior:
        maior = dadosTemp[1]
    elif dadosTemp[1] < menor:
        menor = dadosTemp[1]

    dadosPessoa.append(dadosTemp[:])  # Fazendo uma cópia da lista temporária para principal
    dadosTemp.clear()  # Limpando a lista temporária

    continuar = input('Continuar? [S/N]: ').strip().upper()

    # Caso usuário informe uma opção inválida
    while continuar not in ('S', 'N'):
        print('\nValor incorreto, informe a opção correta...')
        continuar = input('Continuar? [S/N]: ').strip().upper()
    print('-' * 30)

    if continuar == 'N':
        print('Programa finalizado...')
        print('-' * 30)
        break

print(f'\nPESSOAS SUBMETIDAS: {len(dadosPessoa)}')
print(f'MAIOR PESO FOI DE {maior}Kg --> ', end='')
for pessoa in dadosPessoa:
    if pessoa[1] == maior:
        print(f'{pessoa[0]}', end=' ')
print()

print(f'MENOR PESO FOI DE {menor}Kg --> ', end='')
for pessoa in dadosPessoa:
    if pessoa[1] == menor:
        print(f'{pessoa[0]}', end=' ')




""" pessoas = []
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
print(f'A pesoa mais leve, pesa {leve}') """