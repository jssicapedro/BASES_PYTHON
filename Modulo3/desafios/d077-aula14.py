# Programa que tenha uma tupla única com nomes de produtos e os seus respetivos preços, na sequência.
# No fim mostra uma listagem de preços, organizando os dados em forma tabular.
lista = ('caneta', 0.75,
          'lápis', 1,
          'borracha', 1.25,
          'agrafador', 15,
          'compasso', 13  )
print('=++'*13)
print(f'{"A minha Loja":^36}')
print('=++'*13)
for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', end='')
    else:
        print(f'€{lista[item]:>7.2f}')
