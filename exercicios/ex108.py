import moeda

p = float(input('Digite o preço: R$'))
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'{moeda.moeda(p)} aumentado em 10% é {moeda.moeda(moeda.aumenta10(p))}')
print(f'{moeda.moeda(p)} diminuindo em 13% é {moeda.moeda(moeda.diminui13(p))}')
