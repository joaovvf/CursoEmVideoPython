numeros = [[], []]
n = 0
for c in range(1, 8):
    n = int(input(f'Digite o {c}o número: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

print(f'Os números pares digitados são: {sorted(numeros[0])}.')
print(f'Os números ímpares digitados são: {sorted(numeros[1])}.')


