d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram percorridos? '))
preço = (d*60) + (km * 0.15)
print('\33[33;45mO valor a ser pago é R${:.2f}.\33[m'.format(preço))