#Programa que leia o nome, ano de nascimento e carteira de trabalho e guarda-os (com idade) num dicionário. Se por acaso a carteira de trabalho for diferente de 0, o dicionário recebe também o ano de contratação e o salário. Calcula e acrescenta, além da idades, com quantos anos a pessoa vai se reformar, tendo como referencia que a reforma dá-se quando a pessoa cumpre 40anos de carreira contributiva
from datetime import date

pessoa = {}
ano_atual = date.today().year

pessoa['nome'] = str(input('Qual é o teu nome? '))
ano_nascimento = int(input('Em que ano nasceste? '))
pessoa['idade'] = ano_atual - ano_nascimento

if pessoa['idade'] >= 16:
    pessoa['contratacao'] = int(input('Em que ano fos-te contratado? [0 não foste] '))
    if pessoa['contratacao'] != 999:
        pessoa['salario'] = float(input('Salário: € '))
        pessoa['reforma'] = pessoa['idade'] + ((pessoa['contratacao'] + 40) - ano_atual)
 
print('=-='*3, 'INFORMAÇÕES DA PESSOA', '=-='*3)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')

if pessoa['idade'] <16:
    print('Não tens idade suficiente para trabalhar')
else:
    if pessoa['contratacao'] == 0:
        print('Ainda não foste contratado')
