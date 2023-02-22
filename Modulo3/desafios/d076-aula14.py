# Programa que leia 4 valores do utilizador e guarde-os numa tupla. No final mostra:
# - Quantas vezes apareceu o número 9
# - Em que posição está o primeiro 3
# - Quais foram os números pares
num = (int(input('Informe um número: ')),
    int(input('Informe outro número: ')),
    int(input('Informe mais um número: ')),
    int(input('Informe o ultimo número: ')))

print(f'Escreveu os valores {num}')
if 9 in num:
    print(f'O valor 9 apareceu {num.count(9)} vezes')
else:
    print('O valor 9 não apareceu')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}.ª posição')
else:
    print('O valor 3 não apareceu')
print('Os valores pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

