barato = ''
total = totmil = menor = cont = 0
while True:
    n = str(input('Digite o nome do produto: '))
    p = float(input('Digite o preço do produto: R$'))
    cont += 1
    total += p
    if p > 1000:
        totmil += 1
    if cont == 1:
        menor = p
        barato = n
    else:
        if p < menor:
            menor = p
            barato = n
    r = ' '
    while r not in 'SN':
        r = str(input('Você deseja continuar? Digite S para continuar e N parar: ')).upper().strip()[0]
    if r == 'N':
        break
print(f'O total gasto em produtos é R${total}')
print(f'{totmil} produtos custam mais de R$1000')
print(f'O produto mais barato é {barato} e custa R${menor}.')

