# Programa que leia o nome de uma pessoa e se ela tem ou não o nome “Silva”
nome = str(input('Indique o nome completo: ')).strip().lower()
print('O nome {} tem "Silva"? {}'.format(nome, 'silva' in nome))