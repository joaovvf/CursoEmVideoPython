palavras = 'carro', 'lousa', 'mesa', 'jaleco', 'garrafa', 'ovo', 'esteira', 'piscina'
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
