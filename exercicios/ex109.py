import moeda

p = float(input('Digite o preço: R$'))
print(f'O dobro de {moeda.moeda(p, True)} é {moeda.dobro(p, True)}')
print(f'A metade de {moeda.moeda(p, True)} é {moeda.metade(p, True)}')
print(f'{moeda.moeda(p, True)} aumentado em 10% é {moeda.aumenta10(p, True)}')
print(f'{moeda.moeda(p, True)} diminuindo em 13% é {moeda.diminui13(p, True)}')
