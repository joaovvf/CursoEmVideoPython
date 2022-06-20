import math
co = int(input('Digite o valor do cateto oposto: '))
ca = int(input('Digite o valor do cateto adjacente: '))
print('O valor da hipotenusa é \33[1;36;40m{:.2f}\33[m.'.format(math.hypot(co, ca)))
