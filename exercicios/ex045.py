import random

eu = str(input('Pedra, Papel ou Tesoura? '))
pc = random.choice(['Pedra', 'Papel','Tesoura'])
print('O computador escolheu: {}'.format(pc))
if eu=='Pedra' and pc=='Papel' or eu=='Tesoura' and pc=='Pedra' or eu=='Papel' and pc=='Tesoura':
    print('Você foi derrotade!!!')
elif eu=='Pedra' and pc=='Tesoura' or eu=='Papel' and pc=='Pedra' or eu=='Tesoura' and pc=='Papel':
    print('Você foi vitoriose!!!')
elif eu=='Pedra'and pc=='Pedra' or eu=='Papel' and pc=='Papel' or eu=='Tesoura' and pc=='Tesoura':
    print('Oh não! Empatou.')

