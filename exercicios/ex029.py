v = int(input('A velocidade do carro é: '))
if v>=80:
    print('\33[1;31;47mVocê foi multado no valor de R${}.\33[m'.format(7*(v - 80)))