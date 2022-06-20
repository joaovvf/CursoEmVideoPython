lista = []
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    r = str(input('Quer continuar? [S/N] ')).upper()
    if 'N' in r:
        break
print(f'Os números digitados foram {lista}.')
print(f'Os números pares são {listapar}.')
print(f'Os números ímpares são {listaimpar}.')
