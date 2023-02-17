print('\033[1;34;41mOlá\033[m mundo')

print('\033[7;30mOlá mundo')

cores = { 'apaga':'\033[m',
          'azul':'\033[34m',
          'amarelo':'\033[33m',
          'pretobranco':'\033[7;30m'}
print('{}Olá!{} Muito prazer'.format(cores['azul'], cores['apaga']))

