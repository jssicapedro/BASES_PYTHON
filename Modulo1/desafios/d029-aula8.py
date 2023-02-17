# Programa que faça o computador “pensar” num número inteiro entre 0 e 5 e peça para o utilizador tentar descobrir qual foi o número escolhido pelo computador. Deve retornar se o utilizador acertou ou não

from random import randint

pc = randint(0, 5)
utt = int(input('Indique um numero de 0 a 5: ').strip())

if utt>5:
    print('Escreveu numero inválido')
else:
    if pc==utt:
        print('O PC pensou no mesmo número {}\nParabéns!'.format(pc))
    else:
        print('O PC pensou no numero {}'.format(pc))
