p = 'S'
soma = 0
cont = 0
maior = 0
menor = 0
while p == 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    p = str(input('Quer continuar? Digite S para continuar e N para parar. ')).upper()
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('O maior valor digitado foi {}.'.format(maior))
print('O menor valor digitado foi {}.'.format(menor))
print('A média dos valores digitados foi {:.2f}.'.format(float(soma/cont)))
