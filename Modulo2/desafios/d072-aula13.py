# Programa que simule o funcionamento de uma caixa eletrónica. No inicio, pergunta ao utilizador qual é o valor que quer retirar (numero inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Leva em consideração que a caixa tem cédulas de 50€, 20€ e 10€

print('=' * 30)
print('BANCO PYTHON')
print('=' * 30)
valor = int(input('Qual é a quantidade que queres levantar? € '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de {ced}€')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10 
        totced = 0
        if total == 0:
            break
