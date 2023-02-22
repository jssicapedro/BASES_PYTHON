# Programa que leia vários números inteiros. O programa só vai parar quando o utilizador escrever o valor 999, que é a condição de paragem. No final mostrar quantos números foram escritos e qual é a soma entre eles (desconsiderando a flag)
quant = soma = 0
while True:
    n = int(input('Indique um valor [999 para parar]: '))
    if n == 999:
        break
    quant += 1
    soma += n
print(f'Informou {quant} valores e a soma deles é de {soma}!')
print('FIM')
