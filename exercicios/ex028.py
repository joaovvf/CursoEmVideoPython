import random

n = random.choice([0, 1, 2, 3, 4, 5])
nj = int(input('Digite o número de 0 a 5 que o computador está pensando: '))
print('VOCÊ GANHOU!' if nj == n else 'O computador venceu.')
