print(10*'=','PROGAMA TABUADA STARTED',10*'=')
while True:
    n = int(input('Digite um número: '))
    if n <= 0:
        break
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
print(10*'=', 'PROGAMA TABUADA FINISHED', 10*'=')