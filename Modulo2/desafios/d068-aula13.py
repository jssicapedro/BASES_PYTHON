# Programa que mostre a tabuada de vários números de cada vez, para cada valor informado pelo utilizador. O programa será interrompido quando o número solicitado for negativo
from time import sleep
c = 1
print('~'*20)
print('PROGRAMA DA TABUADA')
print('~'*20)
while True:
    tab = int(input('Queres ver a tabuada de que valor? '))
    print('-'*30)
    while c < 11:
        print(f'{tab} x {c} = {tab*c}')
        c += 1
    c = 1
    print('-'*30)
    if tab < 0:
        break
print('Escreveu um número negativo')
sleep(0.5)
print('A encerrar...')
sleep(0.5)
print('FIM')