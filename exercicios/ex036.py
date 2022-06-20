vc = float(input('Digite o valor da casa que deseja comprar: R$'))
s = float(input('Digite o valor do seu salário: R$'))
a = int(input('Digite em quantos anos deseja quitar a casa: '))
p = vc / (a*12)
pa = 0.3 * s
if p > pa:
    print('Seu empréstimo foi negado.')
else:
    print('Seu empréstimo foi aprovado!')
    print('O valor das prestações mensais será de R${:.2f}, as quais você pagará durante {} anos.'.format(p, a))