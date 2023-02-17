# Programa que leia 2 notas e calcule a seu média, mostrando uma mensagem no final:
# - Media a baixo de 9.5: REPROVADO
# - Media entre 9.5 e 15: APROVADO
# - Media acima de 15: PARABÉNS! APROVADO

n1 = float(input('Indique a 1.ª nota: '))
n2 = float(input('Indique a 2.ª nota: '))
media = (n1+n2)/2

if media < 9.5:
    print('\033[31mREPROVADO\033[m')
elif media>9.5 and media<=15:
    print('\033[33mAPROVADO\033[m')
else:
    print('\033[32mPARABÉNS! APROVADO\033[m')
