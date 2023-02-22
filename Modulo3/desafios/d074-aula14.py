# Cria uma tupla preenchida com os colocados da Tabela da 1.ª liga na ordem de colocação. Depois mostra:
# - Apenas os 5 primeiros colocados
# - Os últimos 4 colocados
# - Uma lista com os nomes das equipas ordenados por ordem alfabética
# - Em que posição na tabela está a equipa do Arouca

primeira_liga = ('Porto', 'Sporting', 'Benfica', 'Braga', 'Gil Vicente', 'Vitória SC', 'Santa Clara', 'Famalicão', 'Estoril', 'Marítimo', 'P. Ferreira', 'Boavista', 'Portimonense', 'Vizela', 'Arouca', 'Moreirense', 'Tondela', 'B-SAD')

print('~'*30)
print('{: ^30}'.format('PRIMEIRA LIGA'))
print('~'*30)
print('='*30)
print('Os primeiros 5 colocados foram:')
print('_'*30)
print(primeira_liga[:5])
print('='*30)

print('')
print('='*30)
print('Os 4 últimos colocados foram:')
print('_'*30)
print(primeira_liga[-4:])
print('='*30)

print('')
print('='*30)
print('Participaram neste evento as equipas (ordem alfabética):')
print('_'*30)
print(sorted(primeira_liga))
print('='*30)

print('')
print('='*30)
print('O Arouca ficou em:')
print('_'*30)
print(primeira_liga.index('Arouca')+1)
print('='*30)
