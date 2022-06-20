def linha():
    print('-' * 40)


def dobro(n, form=False):
    if form:
        return f'R${n * 2}'
    else:
        return n * 2


def metade(n, form=False):
    if form:
        return f'R${n / 2}'
    else:
        return n / 2


def aumenta(n, x, form=False):
    if form:
        return f'R${(n*(x/100)) + n}'
    else:
        return (n*(x/100)) + n


def diminui(n, x, form=False):
    if form:
        return f'R${n - ((x / 100) * n)}'
    else:
        return n - ((x / 100) * n)


def moeda(n, form=False):
    if form:
        return f'R${n}'
    else:
        return n


def resumo(n, a, d):
    linha()
    print(f'RESUMO MONETÁRIO'.center(40))
    linha()
    print(f'Preço analisado: \t\t\t{moeda(n, True)}')
    print(f'Dobro do preço: \t\t\t{dobro(n, True)}')
    print(f'Metade do preço: \t\t\t{metade(n, True)}')
    print(f'Preço aumentado em {a}%: \t{aumenta(n, a, True)}')
    print(f'Preço diminuido em {d}%: \t{diminui(n, d, True)}')
    linha()

