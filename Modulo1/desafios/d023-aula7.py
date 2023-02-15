# 1. Criar um programa que leia o nome completo de uma pessoa e mostre:
#    1. o nome com todas as letras maiúsculas
#    2. o nome com todas as letras minúsculas
#    3. quantas letras tem sem espaços
#    4. quantas letras tem o 1.º nome

nome=str(input('Indique o seu nome: '))
N = nome.upper() #maiusculas
n = nome.lower() #minusculas
semEspaco = len(nome.replace(' ', '')) #contagem de caracteres sem espaço

# contagem de letras do 1.º nome
lista = nome.split()
pri_nome = len(lista[0])


print('Nome: {}'.format(nome))
print('Maiúsculas: {}'.format(N))
print('Minúsculas: {}'.format(n))
print('Contagem sem espaços: {}'.format(semEspaco))
print(pri_nome)
