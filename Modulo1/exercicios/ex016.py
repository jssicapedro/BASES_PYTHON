n1 = float(input('Escreve a 1ª nota: '))
n2 = float(input('Escreve a 2ª nota: '))
m = (n1+n2)/2
print('A media do aluno é de {:.2f}.'.format(m))
if m>=9.5:
	print('O aluno está aprovado.')
else:
	print('O aluno está reprovado.')