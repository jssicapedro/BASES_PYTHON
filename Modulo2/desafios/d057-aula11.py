# Programa que leia o nome, idade e sexo de 4 pessoas. No final mostra:
# - A média de idade do grupo
# - O nome do homem mais velho
# - Quantas mulheres têm menos de 20 anos
somaidade = 0
maiorhomem = 0
nomemaiorhomem = ''
mulheres = 0
for p in range(1, 5):
    print('-'*5, end=' ')
    print('{}.ª PESSOA'.format(p), end=' ')
    print('-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
# media de idades
    somaidade += idade
# homem mais velho
    if p == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomemaiorhomem = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomemaiorhomem = nome
# mulheres mais novas de 20 anos
    if sexo in 'Ff' and idade < 20:
        mulheres += 1

print('A média de idade do grupo é de {:.2f}'.format(somaidade/4))
print('O homem mais velho tem {} anos e chama-se {}'.format(maiorhomem, nomemaiorhomem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres))
