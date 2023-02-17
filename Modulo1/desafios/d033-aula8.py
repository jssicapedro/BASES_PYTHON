# Programa que leia um ano e mostre se é bissexto. Se o utilizador escrever 0 o pc lê o ano atual da maquina
# verificar se é divisível por 4 e não por 100 ou por 400

from datetime import date

ano = int(input('Indique um ano: '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
