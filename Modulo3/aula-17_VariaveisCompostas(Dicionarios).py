# dicionário com nome e idade de uma pessoa
dados = dict()
dados = {'nome':'Pedro', 'idade':25}

# passamos a ter Pedro no indice nome e 25 no indice idade
print(dados['nome']) # retona Pedro
print(dados['idade'])# retorna 25

#adicionar elemento com indice sexo
dados['sexo']='M'
print(dados['sexo'])

print(f'Lista dados com todos os elementos criados {dados}')

#remover elementos
del dados['idade']

print(f"Lista dados após dar del em dados['idade'] {dados}")

print('='*30)
print('TERMOS TÉCNICOS')
print('-'*15)

filme = {
			'titulo' : 'Star Wars',
			'ano' : 1977,
			'diretor' : 'George Lucas'
		}
print(filme)
print(filme.values()) # valores/values são os dados
print(filme.keys()) # chaves/keys são todos os indices
print(filme.items()) # elementos/items são os valores e as chaves

for k, v in filme.items(): #por cada k(key) e v(value) dentro dos items de filme
	print(f'O {k} é {v}')