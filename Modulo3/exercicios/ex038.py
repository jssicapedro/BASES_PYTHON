pessoas = list()
dado = list()
for c in range(0, 4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])
    dado.clear()
for p in pessoas:
    if p[1] < 20:
        print(f'{p[0]} tem menos de 20 anos')
    else:
       print(f'{p[0]} tem 20 anos ou mais')
       