# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria, de acordo com a idade:
# - até 9 anos: MIRIM
# - até 14 anos: INFANTIL
# - até 19 anos: JUNIOR
# - até 21 anos: SÊNIOR
# - acima: MASTER

from datetime import date

print('#'*12)
print('\033[32mConfederação Nacional de Natação\033[m')
print('-'*12)
print('Escalões')
print('-'*12)

n = int(input('Indique o seu ano de nascimento: '))
atual = date.today().year
natacao = atual - n
if natacao<=9:
    print('Tem {}, está no escalão MIRIM'.format(natacao))
elif natacao<=14:
    print('Tem {}, está no escalão INFANTIL'.format(natacao))
elif natacao<=19:
    print('Tem {}, está no escalão JUNIOR'.format(natacao))
elif natacao<=21:
    print('Tem {}, está no escalão SÊNIOR'.format(natacao))
else:
    print('Tem {}, está no escalão MASTER'.format(natacao))
