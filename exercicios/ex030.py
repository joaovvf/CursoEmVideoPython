n = int(input('Digite um número: '))
n2 = n % 2
if n2 == 0:
    print('O número {} é par.'.format(n))
else:
    print('O número {} é ímpar.'.format(n))