# Programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o utilizador quer ou não continuar. No final mostra:
# - quantas pessoas tem mais de 18 anos
# - quantos homens fizeram o cadastro
# - quantas mulheres tem menos de 20 anos
maior18 = homem = Mmenos20 = 0
while True:
    idade = int(input('Qual a tua idade? '))
    sexo = ''
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Qual o teu sexo? [F/M] ')).strip().upper()[0]
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homem += 1
    if idade < 20 and sexo == 'F':
        Mmenos20 += 1
    print('-' * 15)
    r = ''
    while r != 'S' and r != 'N':
        r = str(input('Queres continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Há {maior18} pessoas maiores de 18 anos\n{homem} homens fizeram o cadastro\n{Mmenos20} mulheres tem menos de 20 anos')

