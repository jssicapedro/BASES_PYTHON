""" Programa que lê o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcula e retorna o comprimento da hipotenusa. """
import math
catop = float(input('Informe o CATETO OPOSTO de um triângulo retângulo: '))
catad = float(input('Informe o CATETO ADJACENTE de um triângulo retângulo: '))

hip = math.sqrt(pow(catop,2)+pow(catad,2))

""" 
hipotenusa é a soma dos catetos ao quadrado. Dessa soma faz-se a raiz quadrada
"""

print('A hipotenusa do seu triângulo retângulo é de {:.2f}'.format(hip))



""" 
ou:

import math

catop = float(input('Informe o CATETO OPOSTO de um triângulo retângulo: '))
catad = float(input('Informe o CATETO ADJACENTE de um triângulo retângulo: '))

hip = math.hypot(catop, catad)

print('A hipotenusa do seu triângulo retângulo é de {:.2f}'.format(hip))
"""