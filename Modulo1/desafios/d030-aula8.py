# Programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostra uma mensagem de que o condutor foi multado, a multa vai custar 7€ por cada km ultrapassado

vl = float(input('Indique a velocidade de um carro: ').strip())
if vl>80:
    print('O condutor foi multado a {}€'.format((vl-80)*7))
print('Tenha um bom dia. Conduza com segurança!!')
