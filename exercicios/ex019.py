import random
n = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = [n, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno que apagará o quadro: \33[1;36;40m{}\33[m.'.format(escolhido))