lista = ('Bola', 50,
        'Raquete', 100,
        'Cesta', 1000,
        'Camiseta', 30,
        'Tênis', 200)
print(f'{"LISTAGEM DE PREÇOS":^40}')
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    if pos % 2 != 0:
        print(f'R${lista[pos]:>4}')
