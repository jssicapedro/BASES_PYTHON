# Programa que leia o nome de uma cidade e se ela começa ou não com o nome “Santo”
cidade = str(input('Indique uma cidade: ')).strip()
print('A cidade {} começa com "Santo"? {}'.format(cidade, cidade[:5].lower() == 'santo'))