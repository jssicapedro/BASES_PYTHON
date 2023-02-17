# Programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a 1.250,00, calcular um aumento de 10%. Para salários inferiores ou iguais, o aumento de 15%

salario = float(input('Indique o seu salário: '))

""" 
salario      100
aumento      110

"""

if salario>1250.00:
    print('Um funcionário com {}, passa a receber {} (um aumento de 10%)'.format(salario, (salario*110)/100))
else:
    print('Um funcionário com {}, passa a receber {} (um aumento de 15%)'.format(salario, (salario*115)/100))