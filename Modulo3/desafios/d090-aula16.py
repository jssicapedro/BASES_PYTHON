# Programa que leia o nome  e 2 notas de vários alunos e guarda tudo numa lista composta. Bi fim mostra um boletim contendo a média de cada um e permita que o utilizador possa mostrar as notas de cada aluno individualmente.

ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    ficha.append([nome, [nota1,nota2], media])
    resp = str(input('Quer continuar?[S/N] '))
    if resp in 'nN':
        break
print('-='*5, 'Notas', '-='*5)
print(f'{"N.º":<4}{"Nome":<10}{"Média":<8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar as notas de que aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizado...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('Volte sempre...')