""" Programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcula o preço a pagar, sabendo que o carro custa 60€ por dia e 0,15€ por Km rodado. """

km = float(input("Quantos km foram percorridos? "))
dias = int(input("Duração em dias: "))

precodia = (60*dias)/1
precokm = (0.15*km)/1

""" 
  dias    €           km    €
   1     60           1     0.15
  dias   x            km      x
"""

total=precodia+precokm

print('O total a pagar é de {:.2f}'.format(total))
