print('GERADOR DE PA')
print('-=' * 20)
primeiro = int(input('Insira o primeiro termo da PA: '))
r = int(input('Digite o valor da razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' ')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? Insira: '))
print('A progressão foi finalizada com {} termos exibidos.'.format(total))
print('FIM')

