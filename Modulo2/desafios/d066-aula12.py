# programa que leia vários números inteiros. No final da execução, mostre a média entre eles e qual foi o maior e o menor valor lido. O programa deve perguntar ao utilizador se ele quer ou não continuar a escrever valores.
r = 's'.upper()
quantidade = soma = 0
maior = menor = 0
while r in 'S':
    n = int(input('Escreva um número: '))
    soma += n
    quantidade += 1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar? [S/N]' )).upper()
if r != 'S' or r != 'N':
    print('opção inválida')
media = soma/quantidade
print('Informou {} números e a média é {}'.format(quantidade, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
