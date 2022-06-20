def area(a, b):
    area = largura * comprimento
    print(f'A área do terreno {largura}x{comprimento} é de {area}m2')


print('ARÉA DE TERRENOS LTDA')
largura = float(input('LARGURA DO TERRENO(m): '))
comprimento = float(input('COMPRIMENTO DO TERRENO(m): '))
area(largura, comprimento)
