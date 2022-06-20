from operator import itemgetter
from random import randint
from time import sleep

numeros = dict()
numeros['p1'] = randint(1,6)
numeros['p2'] = randint(1,6)
numeros['p3'] = randint(1,6)
numeros['p4'] = randint(1,6)
print(f'O jogador 1 tirou {numeros["p1"]}.')
sleep(1)
print(f'O jogador 2 tirou {numeros["p2"]}.')
sleep(1)
print(f'O jogador 3 tirou {numeros["p3"]}.')
sleep(1)
print(f'O jogador 4 tirou {numeros["p4"]}.')
sleep(1)
ranking = dict()
ranking = sorted(numeros.items(), key=itemgetter(1), reverse=True)
print('-='*10, 'RANKING DE JOGADORES', '-='*10)
for i, v in enumerate(ranking):
    print(f'O {i+1} lugar: {v[0]} com {v[1]}.')

