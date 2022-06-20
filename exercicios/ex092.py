from datetime import datetime

registro = dict()
registro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
registro['idade'] = datetime.now().year - nasc
registro['ctps'] = int(input('Carteira de trabalho(0 não tem): '))
if registro['ctps'] != 0:
    registro['contrataçao'] = int(input('Ano de contratação: '))
    registro['salario'] = float(input('Salário: R$'))
    registro['aposentadoria'] = ((registro['contrataçao'] + 35) - datetime.now().year) + registro['idade']
print(registro)
for k,v in registro.items():
    print(f'{k}: {v}.')