alunos = dict()
alunos['nome'] = str(input('Digite o nome do aluno: '))
alunos['media'] = float(input('Digite a média do aluno: '))
if alunos['media'] >= 7:
    alunos['situação'] = 'Aprovado'
else:
    alunos['situação'] = 'Reprovado'
print(f'O nome do aluno é {alunos["nome"]}.')
print(f'Sua média é {alunos["media"]}.')
print(f'Sua situação é: {alunos["situação"]}.')
