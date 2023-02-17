# Programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e dom quantos anos ele quer pagar.
# Calcular o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o salario do comprador? '))
anos = int(input('Quer financiar em quantos anos? '))

prestacao = casa/(anos*12)

print('Para pagar uma casa de {:.2f}€ em {}anos, tem de pagar {:.2f}€ por mês.'.format(casa, anos, prestacao))

minimo=salario*30/100

if prestacao<=minimo:
    print('O pedido do empréstimo foi APROVADO')
else:
    print('O pedido do empréstimo foi RECUSADO')
