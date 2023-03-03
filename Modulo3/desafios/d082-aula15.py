# Programa que vai ler vários números e coloca-los numa lista. Depois mostra:
# - A quantidade de valores na lista
# - A lista ordenada de forma decrescente
# - Se o valor 5 está ou não na lista
lista = []
while True:
    lista.append(int(input('Indique um valor para ser adicionado à lista: ')))
    r = str(input('Deseja continuar? [S/N] ')).strip()
    if r in 'Nn':
        break
print('='*25)
print(f'Informas-te {len(lista)} valores')
lista.sort(reverse=True)
print(f'A lista por ordem decrescente fica {lista} valores')
if 5 in lista:
    print(f'Na lista encontra-se o valor 5 na lista')
else:
    print('Não existe o valor 5 na lista.')
print('='*25)

