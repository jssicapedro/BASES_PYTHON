# Programa que leia o nome completo de uma pessoa, mostrando em seguida o 1.º e ultimo nome separadamente
#    1. ex. nome: Ana Maria de Souza primeiro: Ana ultimo: Souza

nome = str(input('Indique o nome de uma pessoa: ')).strip()
lista = nome.split()
print('Nome: {}\nPrimeiro nome: {}\nUltimo Nome: {}'.format(nome,lista[0], lista[-1]))
