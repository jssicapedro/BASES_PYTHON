n1=int(input('um valor: '))
n2=int(input('outro valor: '))
s=n1+n2
sub=n1-n2
m=n1*n2
d=n1/n2
p=n1**n2
di=n1//n2
r=n1%n2
print('A soma vale {}. \nA subtração vale {}. \nA multiplicação vale {}. \nA divisão vale {:.3f}. \nA potência vale {}. \nA divisão inteira vale {}. \nO resto da divisão vale {}.'.format(s, sub, m, d, p, di, r))