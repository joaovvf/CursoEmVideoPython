from random import randint
from time import sleep


def sorteia(lista):
    print('SORTEANDO 5 VALORES!!!')
    for cont in range(0,5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.25)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares temos {soma}.')


numeros = list()
sorteia(numeros)
somapar(numeros)
