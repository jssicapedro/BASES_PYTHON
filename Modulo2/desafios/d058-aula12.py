# Programa que leia o sexo de uma pessoa, mas só aceite valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto
s = str(input('Qual é o seu sexo? [F/M] ')).strip().upper()[0]
while s not in 'FfMm':
    s = str(input('Dados inválidos. Informe o seu sexo? [F/M] ')).strip().upper()[0]
print('O programa acabou, escolheu {}'.format(s))
