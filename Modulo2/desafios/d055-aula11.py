# Programa que leia o ano de nascimento de 7 pessoas. No final mostre quantas pessoas ainda não maiores de idade e quantas já são maiores.

from datetime import date
atual = date.today().year
totalM = 0
totalm = 0
for pess in range(1,8):
    nasc = int(input('Em que ano a {}.ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        totalM += 1
    else:
        totalm += 1

print('No grupo há {} maiores de idade'.format(totalM))
print('No grupo há {} menores de idade'.format(totalm))