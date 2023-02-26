# a = [0, 4, 5, 10]
# b = a[]
# b[2] = 8
# print(f'Lista A: {a}')
# print(f'Lista B: {b}')
#
# Python vai fazer uma ligação entre b e a, assim vai retornar:
# Lista A: [0, 4, 8, 10]
# Lista B: [0, 4, 8, 10]
#
# então deves:

a = [0, 4, 5, 10]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')