# Programa que tem uma tupla com várias palavras (não uses acentuação). Depois, deve mostras, para cada palavra, quais são as suas vogais
palavras = ('moral', 'muito', 'posse', 'tange', 'fosse', 'expor', 'corja', 'prole', 'digno', 'ardil')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
