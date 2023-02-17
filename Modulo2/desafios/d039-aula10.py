# Programa que leia 2 números inteiros e compare-os, retornando uma mensagem:
# - O 1.º valor é maior
# - O 2.º valor é maior
# - Não existe valor maior, os dois são iguais

print('Indique dois números\033[m')
n1 = int(input('1.º número: '))
n2 = int(input('2.º número: '))

print('Indicou o n.º \033[32m{}\033[m e o n.º \033[33m{}\033[m'.format(n1, n2))

if n1>n2:
    print('O \033[32mPRIMEIRO\033[m é o maior valor.'.format(n1))
elif n2>n1:
    print('O \033[33mSEGUNDO\033[m é o maior valor.'.format(n2))
else:
    print('\033[31mNão existe o valor maior, os dois números são iguais.\033[m')
