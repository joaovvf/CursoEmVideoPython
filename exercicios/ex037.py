n = int(input('Digite um número: '))
m = int(input('Digite (1) para converter o número {} em binário\nDigite (2) para converter o número {} para '
              'octal\nDigite (3) para converter o número {} em hexadecimal.\nSeu número: '.format(n, n, n)))
if m == 1:
    print('O número {} em binário é {}.'.format(n, bin(n)))
elif m == 2:
    print('O número {} em octal é {}.'.format(n, oct(n)))
elif m ==3:
    print('O número {} em hexadecimal é {}.'.format(n, hex(n)))
else:
    print('Você não sabe ler?')
