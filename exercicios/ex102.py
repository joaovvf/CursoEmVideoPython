def fatorial(num, show=False):
    """
    :param num: número que será feito o fatorial
    :param show: mostrar o processo(True)
    :return: O valor do fatorial de num
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'{fatorial(n, show=True)}.')
