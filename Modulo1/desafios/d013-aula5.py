""" Algoritmo que leia o preço de um produto e mostre o novo preço, com 5% de desconto """

prod = float(input('Informe o preço do produto: '))
desc = (prod*95)/100
""" 
        %       valor
       100      prod
    100-5=95    desc
"""

print('O produto a {} com desconto de 5% fica a {}'.format(prod,desc))