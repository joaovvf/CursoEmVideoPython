from time import sleep


def contador(i, f, r):
    if r < 0:
        r *= -1
    if r == 0:
        r = 1
    print('-='*20)
    print(f'Contagem de {i} a {f} de {r} em {r}.')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.25)
            cont += r
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.25)
            cont -= r
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Ínicio da contagem personalizada!')
ini = int(input('ínicio: '))
fim = int(input('Fim: '))
raz = int(input('Razão: '))
contador(ini, fim, raz)