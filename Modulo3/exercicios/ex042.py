pessoa = {'nome':'Lucas', 'sexo':'M', 'idade':21}
pessoa['nome'] = 'Rafael'
pessoa['peso'] = 85
for k, v in pessoa.items():
	print(f'{k} é {v}')