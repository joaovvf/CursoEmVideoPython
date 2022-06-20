largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = l * a
tinta = area / 2
print('Sua parede tem as dimensões {} x {}m. Sua área é de {} m.'.format(largura, altura, area))
print('\33[33;45mSerá necessário {} litros de tinta.\33[m'.format(tinta))

