lista = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont += 1
    r = str(input('Deseja continuar? [S/N] ')).upper()
    if 'N' in r:
        break
print(f'{cont} valores foram digitados.')
print(f'A lista na ordem decrescente é {sorted(lista, reverse= True)}.')
if 5 in lista:
    print('O valor 5 foi digitado e está na lista.')
else:
    print('O valor 5 não foi encontrado.')