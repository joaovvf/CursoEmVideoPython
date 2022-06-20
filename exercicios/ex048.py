s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
        cont = cont + 1
print('A soma dos {} múltiplos de 3 no intervalo de 1 a 500 é {}.'.format(cont, s, end=' '))