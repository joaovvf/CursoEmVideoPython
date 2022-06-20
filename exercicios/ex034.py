s = float(input('Digite o valor do seu salário: R$'))
if s >= 1250:
    print('Seu novo salário, com um aumento de 10%, é R${}.'.format(s + (s * 0.1)))
else:
    print('Seu novo salário, com um aumento de 15%, é R${}.'.format(s + (s * 0.15)))
