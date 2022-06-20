d = int(input('Digite a distância de sua viagem: '))
if d>=200:
    print('O preço da passagem é R${:.2f}.'.format(d * 0.45))
else:
    print('O valor da passagem é R${:.2f}.'.format(d * 0.5))