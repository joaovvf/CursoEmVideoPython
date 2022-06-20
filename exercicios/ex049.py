n = int(input('Digite um número: '))
print('\33[40m-\33[m' * 12)
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c ))
print('\33[40m-\33[m' * 12)
