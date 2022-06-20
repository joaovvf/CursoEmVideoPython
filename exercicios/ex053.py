frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print('Você digitou a frase {}'.format(junto))
inverso = ''
for letra in range(len(junto)-1, -1, -1)
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('Temos um palíndromo.')
else:
    print('A frase não é um palíndromo.')
