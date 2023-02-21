# Melhorar o jogo do d029 onde o computador vai pensar num numero de 0 a 10. Só que desta vez o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários até adivinhar.

from random import randint

pc = randint(1, 10)
utt = int(input('Indique um numero de 1 a 10: ').strip())
tentativas = 1

while utt != pc:
    if utt > pc:
        print('Foi muito...')
    if utt < pc:
        print('Foi pouco...')
    utt = int(input('Valor errado! Tenta novamente: '))
    tentativas += 1
print('Parabéns! Acertas-te, o PC estava a pensar no {}'.format(pc))
print('Precisas-te de {} tentativas'.format(tentativas))
