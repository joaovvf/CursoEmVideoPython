p = float(input('Digite o preço do produto: R$'))
m = int(input('Qual a forma de pagamento?\n1- À vista dinheiro/cheque\n2-À vista no cartão\n3-Em até 2x no cartão\n4-3x ou mais\n'))
if m==1:
    print('O valor com 10% de desconto é R${}.'.format(p*0.9))
elif m==2:
    print('O valor com 5% de desconto é R${}.'.format(p*0.95))
elif m==3:
    print('O valor é R${}'.format(p))
elif m==4:
    print('O valor é R${}.'.format(p*1.2))