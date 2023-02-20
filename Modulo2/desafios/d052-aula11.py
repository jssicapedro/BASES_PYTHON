# Programa que leia o 1.º termo e a razão de uma PA (progressão aritmética). No final, mostra os 10 primeiros termos dessa progressão.

primeiro=int(input("Primeiro elemento: ") )
razao = int(input("Razao: ") )
decimo = primeiro + (10-1) * razao
for var in range(primeiro, decimo + razao, razao):
    print(var, end=' -> ')
print('ACABOU')