# Programa que leia o ano de nascimento de uma pessoa e retorna de acordo com a sua idade:
# - Se ele ainda vai ao dia de defesa nacional
# - Se é este ano que vai ao dia de defesa nacional
# - Se já passou do tempo de ir ao dia de defesa nacional

from datetime import date

ano = int(input('Indique o seu ano de nascimento: '))
atual = date.today().year
idade = atual-ano

if idade < 18:
    saldo = 18 - idade
    alistamento = atual + saldo
    print('Faltam {} ano(s) para ires ao Dia da Defesa Nacional!\nDeves ir no ano {}'.format(saldo, alistamento))
elif idade == 18:
    print('Já tens {} anos.\nDeves ir este ano ao Dia da Defesa Nacional!'.format(idade))
elif idade > 18:
    saldo = idade - 18
    alistamento = atual - saldo
    print('Já passaram {} anos de ires ao Dia da Defesa Nacional!\nFoste no ano {}'.format(saldo, alistamento))
