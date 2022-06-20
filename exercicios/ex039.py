from datetime import date
d = int((input('Digite seu ano de nascimento: ')))
atual = date.today().year
i = atual - d
if i == 18:
    print('Você tem {} anos, está na hora de se alistar!'.format(i))
elif i > 18:
    print('Você tem {} anos, já passou {} ano(s) da hora de alistar!'.format(i, i - 18))
elif i < 18:
    print('Você tem {} anos, você ainda deve esperar {} ano(s) para de alistar.'.format(i, 18 - i))
