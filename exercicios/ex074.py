from random import randint

numeros = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
print('Os números sorteados foram:')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior valor foi: {max(numeros)}')
print(f'O menor valor foi: {min(numeros)}')