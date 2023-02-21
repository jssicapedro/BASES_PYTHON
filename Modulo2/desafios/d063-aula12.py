# Melhorar o d062, perguntando ao utilizador se ele quer mostrar mais alguns termos. O programa encerra quando quiser mostrar 0 termos.

primeiro=int(input('Primeiro elemento: '))
razao = int(input('Razao: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos queres saber mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))