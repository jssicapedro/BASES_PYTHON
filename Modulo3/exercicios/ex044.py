portugal = []
cidade = {}
for c in range(0,3):
    cidade['nome'] = str(input('Indica o nome de uma cidade: '))
    cidade['sigla'] = str(input('Indica a sigla da mesma cidade: '))
    portugal.append(cidade.copy()) # na lista portugal vai ser criada uma copia do dicionario cidade
print(portugal)