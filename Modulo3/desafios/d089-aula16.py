# Programa que ajude um jogador do totoloto a criar palpites. O programa deve perguntar quantos jogos serão criados e vai sortear 6 números entre 1 e 60 para cada jogo.
from random import randint
from time import sleep
lista = []
jogos = []
quant = int(input('Quantos jogos quer sortear? '))
tot = 1
while tot <= quant:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print('='*5, f'Sorteando {quant} Jogos', '='*5)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)