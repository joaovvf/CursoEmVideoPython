n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O número {} é MAIOR que o número {}.'.format(n1, n2))
elif n1 < n2:
    print('O número {} é MENOR que o número {}.'.format(n1, n2))
else:
    print('Os números são iguais.')