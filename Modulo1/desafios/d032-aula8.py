# Programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando 0.50€ por Km para viagens de até 200Km e 0.45€ para viagens mais longas 

km = float(input('Indique a distância da sua viagem: '))

if km<=200:
    print('Para fazer {} tem a pagar {:.2f}€'.format(km, km*0.50))
else:
    print('Para fazer {} tem a pagar {:.2f}€'.format(km, km*0.45))