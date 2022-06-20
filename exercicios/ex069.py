maiores = homens = mulheres = 0
r = ''
while r in 'Ss':
    i = int(input('Digite a idade da pessoa: '))
    s = str(input('Digite o sexo da pessoa[M/F]: '))
    if i >= 18:
        maiores += 1
    if s in 'Mm':
        homens += 1
    if s in 'Ff' and i <= 20:
        mulheres += 1
    r = str(input('Você deseja continuar? S para continuar e N para parar: '))
print(f'{maiores} pessoas são maiores de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheres} mulheres com 20 anos ou menos foram cadastradas.')