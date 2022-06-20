tempc = float(input('Digite a temperatura em C°: '))
print('\33[33;45mA temperatura equivalente em K é {:.2f}.\33[m'.format(tempc + 273.15))
print('\33[33;45mA temperatura equivalente em F é {:.2f}.\33[m'.format(((tempc*9)/5)+32))
