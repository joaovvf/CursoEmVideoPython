from random import randint

cont = 0
while True:
    ej = str(input('Par ou Ímpar? ')).upper()
    nj = int(input('Jogue um número de 0 a 5: '))
    npc = randint(0, 5)
    print(f'Você jogou {nj} e o computador jogou {npc}')
    soma = nj + npc
    if ej == 'PAR':
        if soma % 2 == 0:
            print(f'O número total foi {soma} e você escolheu {ej}. VOCÊ VENCEU!!!')
            cont += 1
        if soma % 2 != 0:
            print(f'O número total foi {soma} e você escolheu par. Você perdeu!!!')
            break
    if ej == 'IMPAR':
        if soma % 2 != 0:
            print(f'O número total foi {soma} e você escolheu Ímpar. Você ganhou!!!')
            cont += 1
        if soma % 2 == 0:
            print(f'O número total foi {soma} e você escolheu Ímpar. Você perdeu!!!')
            break
print(f'Você venceu {cont} vezes.')
