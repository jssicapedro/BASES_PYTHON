# Crie um programa que leia uma frase e diga se ela é um palíndromo (frase que se pode ler de trás para a frente ficando igual), desconsiderando os espaços
# ex: apos a sopa

frase = str(input('Escreva uma frase: ').strip().lower())
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo.')
