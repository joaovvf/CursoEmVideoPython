import math
ang = int(input('Digite um ângulo: '))
cos = math.cos(math.radians(ang))
sin = math.sin(math.radians(ang))
tan = math.tan((math.radians(ang)))
print('\33[1;36;40mO ângulo {} tem o seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}.\33[m'.format(ang, sin, cos, tan))
