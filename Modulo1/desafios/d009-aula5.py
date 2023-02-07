""" Programa que leia um valor em metros e o converta nas restantes medidas """
m = float(input('Escreva o valor em METROS para converter: '))
print('{}M são {}KM, {}HM, {}DAM, {}DM, {}CM, {}MM'.format(m ,(m/1000), ( m/100),(m/10),(m*10),(m*100), (m*1000)))