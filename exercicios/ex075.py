numeros = (int(input('Digite o primeiro número: '))), (int(input('Digite o primeiro número: '))), (int(input('Digite o primeiro número: '))), (int(input('Digite o primeiro número: ')))
print(f'Você digitou os valores {numeros}.')
print(f'O número 9 apareceus {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O número 3 apareceu primeiro na {numeros.index(3)+1}ª posição.')
else:
    print('O número 3 não foi digitado.')
print(f'Os números pares foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
