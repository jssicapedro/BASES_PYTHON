# Programa que leia o peso e a altura de uma pessoa, calcule o seu IMC e retorna o status:
# - abaixo de 18.5: Abaixo do peso
# - entre 18.5 e 25: Peso ideal
# - entre 25 até 30: Sobrepeso
# - entre 30 até 40: Obesidade
# - acima de 40: Obesidade mórbida

peso = float(input('Informe o seu peso: '))
altura = float(input('Indique a sua altura: (m) '))
imc = peso / (altura**2)

print('O seu IMC é de {:.1f}'.format(imc))

if imc<18.5:
    print('Abaixo do peso')
elif imc>18.5 and imc<25:
    print('\033[32mPeso ideal\033[m')
elif imc>25 and imc<30:
    print('\033[33mSobrepeso\033[m')
elif imc>30 and imc<40:
    print('\033[31mObesidade\033[m')
elif imc>40:
    print('\033[31mObesidade mórbida\033[m')
