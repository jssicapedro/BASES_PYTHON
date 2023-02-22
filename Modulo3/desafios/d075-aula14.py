# Programa que gere 5 números aleatórios e coloca-los numa tupla. Depois, mostra a listagem de números gerados e também indicar o menor e o maior valor que estão na tupla.
from random import randint
r = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os valores sorteados foram {r}')
print(f'O maior valor foi: {max(r)}')
print(f'O menor valor foi: {min(r)}')
