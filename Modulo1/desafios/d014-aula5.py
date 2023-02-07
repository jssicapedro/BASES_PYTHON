""" Algoritmo que leia o salário de um funcionário e mostra o novo, com 15% de aumento """

salario = float(input('Indique o seu salário: '))
aumento = (salario*115)/100
""" 
        %          Salario
       100         salario
    100+15=115     aumento
"""
print('Caso o seu salário tenha um aumento de 15% de {}, passrá a receber {}'.format(salario, aumento))