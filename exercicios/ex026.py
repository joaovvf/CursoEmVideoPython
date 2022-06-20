f = str(input('Digite uma frase: '))
xa = f.count('a')
pa = f.find('a')
ua = f.rfind('a')
print(
    'A frase tem {} letra(s) a.\nA primeira letra a aparece na posição {}\nA última letra a aparece na posição {}.'.format(
        xa, pa, ua))
