numeros = list()
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('O valor não será adicionado pois já foi digitado.')
    r = str(input('Deseja continuar? [S/N]')).upper()
    if r in 'Nn':
        break
print(f'Os números em ordem crescente é {sorted(numeros)}.')