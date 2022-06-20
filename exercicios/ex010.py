carteira = float(input('Digite quanto tem em sua carteira: R$'))
print('\33[40mCom R${} você pode comprar {:.2f} doláres e {:.2f} euros.\33[m'.format(carteira, carteira/3.27, carteira/6.20))
