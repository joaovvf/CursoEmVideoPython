from random import randint

tentativas = 1
n = randint(0, 10)
print(n)
nj = int(input('Digite o número de 0 a 10 que o computador está pensando: '))
while nj != n:
    nj = int(input('Você errou, insira outro valor: '))
    tentativas += 1
print('VOCÊ GANHOU!')
print ('Você tentou {} vezes.'.format(tentativas))
