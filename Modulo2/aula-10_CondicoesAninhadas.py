nome = str(input('Indique o seu nome: ').lower().strip())

if nome=='jéssica' or nome=='jessica':
    print('Jéssica, hoje tens uma reunião às 10h e outra às 16h')
elif nome=='andré' or nome=='andre':
    print('André, hoje tens um bug para resolver com urgência no projeto MoveArt')
elif nome in 'ana josé jose':
    print('Adicionem ao site do cliente Afonso um design mais moderno')
else:
    print('Bom dia, mantém o foco.')

print('Bom trabalho!')