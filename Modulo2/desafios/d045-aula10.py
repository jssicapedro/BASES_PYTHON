# Programa que calcule o valor de um produto, considerando o seu preço normal e condição de pagamento:
# - com dinheiro: 10% de desconto
# - cartão: 5% de desconto
# - 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

produto = float(input('Indique o preço do produto: '))
print('Indique o método de pagamento sabendo que')
print('\033[32m [1] - Com dinheiro: 10% de desconto')
print('\033[33m [2] - Com cartão: 5% de desconto')
print('\033[34m [3] - 2 vezes no cartão: preço normal')
print('\033[35m [4] - 3 vezes ou mais no cartão: 20% de juros\033[m')
pagamento = int(input('Indique o método de pagamento: '))

if pagamento == 1:
    preco = produto - (90*produto/100)
    print('O produto a {}€ ao pagar em dinheiro, paga apenas {:.2f}€'.format(produto, preco))
elif pagamento == 2:
    preco = produto - (95*produto/100)
    print('O produto a {}€ ao pagar em cartão, paga apenas {:.2f}€'.format(produto, preco))
elif pagamento == 3:
    parcela = produto / 2
    print('O produto a {}€ vai ser parcelada em 2x de {:.2f}€. SEM JUROS'.format(parcela))
elif pagamento == 4:
    preco = produto + (produto*20/100)
    parcela = int(input('Quantas parcelas? ')) 
    final = preco/parcela
    print('O produto a {}€ vai ser parcelada em {}x e cada uma vai custar {:.2f}€. COM JUROS.\nNo final vais pagar {:.2f}€'.format(produto, parcela, final, preco))
else:
    print('\033[31mOpção inválida\033[m')