from datetime import date
a = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
i = atual - a
if i <= 9:
    print('Você está na categoria MIRIM.')
elif i <= 14:
    print('Você está na categoria INFANTIL.')
elif i <= 19:
    print('Você está na categoria JUNIOR.')
elif i <= 25:
    print('Você está na categoria SÊNIOR.')
elif i > 25:
    print('Você está na categoria MASTER.')
