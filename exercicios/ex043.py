p = float(input('Digite o seu peso: '))
a = float(input('Digite a sua altura(m): '))
i = p/(a*a)
if i<=18.5:
    print('Você está abaixo do peso.')
elif 18.5<i<=25:
    print('Você está no peso ideal.')
elif 25<i<=30:
    print('Você está no sobrepeso.')
elif 30<i<=40:
    print('Você é obeso.')
elif 40<i:
    print('Opa, quebrou a balança.')
