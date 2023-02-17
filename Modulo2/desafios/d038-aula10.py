# Programa que leia um numero inteiro qualquer e peça para o utilizador escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

n = int(input('Indique um número: '))
tipo = int(input('Escolha\n\033[32m- 1 para binário\n\033[33m- 2 para octal\n\033[34m- 3 para hexadecimal\n\033[mIndique a conversão: '))

if tipo == 1:
    print('{} em BINÁRIO é igual a {}'.format(n,bin(n)[2:]))
elif tipo == 2:
    print('{} em OCTAL é igual a {}'.format(n,oct(n)[2:]))
elif tipo == 3:
    print('{} em HEXADECIMAL é igual a {}'.format(n,hex(n)[2:]))
else:
    print('\033[31mA opção indicada não existe!\033[m')

# ...(n)[2:] remove os 2 primeiros valores. Estes indicam o tipo de conversão no resultado final
