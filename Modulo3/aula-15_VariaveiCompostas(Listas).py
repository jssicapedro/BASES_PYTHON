lanche = ['hamburger', 'sumo', 'pizza', 'pudim']
print(f'Este é o meu lanche {lanche}')
lanche[3] = 'maça'
print(f'Alterei o pudim por uma maça. Vou comer {lanche}')
lanche.append('bolacha')
print(f'Vou adicionar uma bolacha. Vou comer {lanche}')
lanche.insert(1, 'lasanha')
print(f'Vou ainda comer uma lasanha. No total vou comer {lanche}') 
del lanche[3]
print(f'Apaguei o 3.º elemento {lanche}')
lanche.pop()
print(f'Apaguei o ultimo elemento {lanche}')
lanche.remove('sumo')
print(f'Também não vou querer o sumo. Vou comer só {lanche}')