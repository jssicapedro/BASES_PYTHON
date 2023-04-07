""" Programa que gere o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de golos feitos em cada partida.
No fim, todos os valores devem ser guardados num dicionário, incluindo o total de golos feitos durante o campeonato """

jogador = {}
golos = []

jogador['nome']=str(input('Qual o nome do jogador? '))
jogos=int(input(f'Em quantos jogos {jogador["nome"]} participou? '))

print('=-='*5)
for c in range (0, jogos):
    golos.append(int(input(f'Quantos golos fez no {c+1}.º jogo? ')))
jogador['golos'] = golos[:]
jogador['total'] = sum(jogador['golos'])

print('=-='*5)
print(jogador)

print('=-='*5)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('=-='*5)
print(f' O jogador {jogador["nome"]} jogou {len(jogador["golos"])} partidas')
for i, v in enumerate(jogador["golos"]):
    print(f' => Na partida {i} fez {v} golos')
print(f'Fez um total de {jogador["total"]} golos')