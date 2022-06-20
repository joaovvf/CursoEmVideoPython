from time import sleep


def maior(* num):
    maior = cont = 0
    print('Analisando os valores informados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        cont += 1
    print()
    maior = max(num)
    print(f'Foram informados {cont} valores.')
    print(f'O maior número foi {maior}')


maior(9, 43, 38, 1231, 2, 0, 12)
