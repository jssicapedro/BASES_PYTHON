# Programa onde o utilizador escreva 5 valores numéricos e guarda-os numa lista, já na posição correta de inserção (sem usar o sort()). No fim mostra a lista ordenada.

num = []
for c in range(0,5):
    n = int(input('Informe um valor: '))
    if c == 0 or n > num[-1]:
        num.append(n)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(f'Os valores em ordem foram {num}')
