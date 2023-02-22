lanche = ('Hambúrguer', 'Sumo', 'Pizza', 'Pudim')
# TUPLAS SÃO IMUTÁVEIS
# lanche[1] = 'água' -> erro

# LER VALORES DE LANCHE
#
# for comida in lanche:
#   print(f'Vou comer {comida}')

# OU

for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]}')

print(f'O lanche tem {len(lanche)} comidas diferentes.')
print('Acho que comi demais')