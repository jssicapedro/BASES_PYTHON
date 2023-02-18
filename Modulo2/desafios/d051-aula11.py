# Programa que leia 6 números inteiros e mostra a soma daqueles que forem pares. Se o valor dado pelo utilizador for impar desconsidera-o

s = 0
for c in range(1, 7):
    n = int(input('Indique o {} valor: '.format(c)))
    if n % 2 == 0:
        s += n
print('A soma dos números pares é de: {}'.format(s))
