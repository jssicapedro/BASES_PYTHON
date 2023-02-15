# Programa que leia uma frase pelo teclado e mostre:
#   1. quantas vezes aparece a letra “A”
#   2. em que posição a letra aparece na 1.ª vez
#   3. em que posição ela aparece a ultima vez

frase = str(input('Escreva uma frase: ')).strip().lower()
print(frase)
print('A letra "a" aparece {} vezes.'.format(frase.count('a')))
print('A 1.ª vez que a letra "a" aparece é na posição {}'.format(frase.find('a')+1))
print('A ultima vez que a letra "a" aparece é na posição {}'.format(frase.rfind('a')+1))
