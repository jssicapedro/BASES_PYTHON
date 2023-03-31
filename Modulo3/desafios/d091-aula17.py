# Programa que leia nome e média de um aluno, guardando também a situação (se está aprovado ou não) num dicionário. No fim mostra o conteúdo da estrutura na tabela.
pessoa = {}

pessoa['nome'] = str(input('Indique o nome do aluno: '))
pessoa['media'] = float(input(f'Qual é a média de {pessoa["nome"]}? '))

print(f'O nome do estudante é {pessoa["nome"]}')
print(f'O estudante tem a média de {pessoa["media"]}')
if pessoa['media'] >= 9.5:
    print('O estudante foi APROVADO')
else:
    print('O estudante foi REPROVADO')
