""" Programa que leia a largura e a altura de uma parede, calcule a área e a quantidade de tinta necessária para pintá-la. Sabendo que cada litro de tinta pinta uma area de 2m^2 """

largura = float(input('Indique a LARGURA da sua parede: '))
altura = float(input('Indique a ALTURA da sua parede: '))

area = largura*altura

tinta = (1*area)/2
""" 
    litro     m^2
      1        2
      x       area

 """

print('A largura da sua parede é {} e a altura é {} \nLogo a parede tem uma area de {} metros quadrados. \nAssim vai precisar de {} litros para a pintar'.format(largura, altura, area, tinta))