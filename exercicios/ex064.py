n = int(input('Digite um número: '))
total = 0
cont = 0
while n != 999:
    total += n
    n = int(input('Digite outro valor: '))
    cont += 1
print('{} números foram digitados.'.format(cont))
print('A soma dos números digitados é {}.'.format(total))
