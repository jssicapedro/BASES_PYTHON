""" Programa que leia quanto dinheiro uma pessoa tem na carteira e mostre a conversão para dólares e reais """

euro = float(input('Quantos € quer converter? '))
print('{}€ são {:.2f}R$ e {:.2f}$'.format(euro, (euro*5.54), (euro*1.07)))