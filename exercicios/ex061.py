tpa = 1
pa = 0
r = 0
pa = int(input('Insira o primeiro termo da PA: '))
r = int(input('Digite o valor da razão da PA: '))
print(pa, end=' ')
while tpa < 10:
    tpa += 1
    pa += r
    print(pa, end=' ')
