i = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
for c in range(i, r*10, r):
    print(c, end=' ')
