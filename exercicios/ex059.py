n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
option = 0
while option != 5:
    print('O que você deseja?\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa')
    option = int(input('Selecione a opção desejada: '))
    if option == 1:
        nn = n1 + n2
        print('A soma é {}'.format(nn))
        print('*'*20)
    elif option == 2:
        nn = n1 * n2
        print('O produto é {}'.format(nn))
        print('*' * 20)
    elif option == 3:
        if n1 > n2:
            print('{} é maior que {}.'.format(n1, n2))
            print('*' * 20)
        if n2 < n1:
            print('{} é maior que {}.'.format(n2, n1))
            print('*' * 20)
        else:
            print('Os dois números são iguais.')
            print('*' * 20)
    elif option == 4:
        n1 = int(input('Digite o novo valor desejado: '))
        n2 = int(input('Digite outro valor: '))
        print('*' * 20)
    else:
        print('Opção inválida. Tente novamente.')
print('Acabou')
