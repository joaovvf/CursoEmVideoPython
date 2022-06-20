import random

n = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = [n, n2, n3, n4]
random.shuffle(lista)
print('\33[1;36;40mA ordem das apresentações do trabalho será: {}\33[m.'.format(lista))
