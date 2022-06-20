import moeda

p = float(input('Digite o preço: R$'))
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'R${p} aumentado em 10% é R${moeda.aumenta10(p)}')
print(f'R${p} diminuindo em 13% é R${moeda.diminui13(p)}')
