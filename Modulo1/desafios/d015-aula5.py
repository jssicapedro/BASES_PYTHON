""" Algoritmo que leia uma temperatura em Cº e converta para Fº """
c=float(input('Informa a temperatura em Cº: '))

f=(c*1.8)+32

""" 
   basta multiplicar a temperatura em graus Celsius por 1,8 e somar 32.
 """

print('A temperatura de {}ºC corresponde a {:.1f}ºF'.format(c, f))