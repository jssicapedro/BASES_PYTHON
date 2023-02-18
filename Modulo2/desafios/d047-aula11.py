# Programa que retorne uma contagem regressiva para os fogos de artificio, de 10 a 0. Com a pause de 1 segundo entre elas
import emoji
from time import sleep
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('-='*12)
print(emoji.emojize("FELIZ ANO NOVO :cone_de_festa:", language='pt'))
print('-='*13)
