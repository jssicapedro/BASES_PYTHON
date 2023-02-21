n = 1
par = impar = 0
while n != 0:
	n = int(input('Indique um número: '))
	if n != 0:
		if n % 2 == 0:
			par += 1
		else:
			impar += 1
print('O utilizador escrever {} números pares'.format(par))
print('O utilizador escrever {} números ímpares'.format(impar))