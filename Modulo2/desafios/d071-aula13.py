# Programa que leia o nome e o preço de vários produtos. O programa deve perguntar se o utilizador vai continuar. No final mostra:
# - Qual o total gasto na compra
# - Quantos produtos custam mais de 100€
# - Qual o nome do produto mais barato
total = caro = menor = cont = 0
nomemenor = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: € '))
    cont += 1
    total += preco
    if preco > 100:
        caro += 1
    if cont == 1 or preco < menor:
        menor = preco
        nomemenor = produto
    resp = ''
    while resp != 'S' and resp != 'N':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('--- FIM DO PROGRAMA ---')
print(f'O total da compra é {total:.2f}€')
print(f'Há {caro} proodutos que custam mais de 100€')
print(f'O menor preço é {nomemenor} de {menor:.2f}€')
