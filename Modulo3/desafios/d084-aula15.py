# 6. Programa onde o utilizador escreva uma expressão qualquer que use parênteses. O programa deverá analisar se a expressão passada está em parênteses abertos e fechados na ordem correta.
# ex: 
# ((a+b)*c) → expressão válida   ((a+b)*c → expressão inválida

expr = str(input('Informe uma expressão: '))
pilha = []
for simb in expr:
    if simb == '()':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida')
else:
     print('Expressão inválida')
