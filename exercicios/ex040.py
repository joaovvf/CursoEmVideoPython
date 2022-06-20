n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Sua média é {:.1f}, você foi \033[1;31mREPROVADO!\033[m'.format(m))
elif 5 <= m <= 6.9:
    print('Sua média é {:1.f}, você está de recuperação.'.format(m))
elif m > 6.9:
    print('Sua média é {:.1f}, você foi \033[1;32mAPROVADO!\033[m.'.format(m))