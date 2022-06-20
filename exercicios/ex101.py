def voto(num):
    from datetime import date
    atual = date.today().year
    idade = atual - num
    if idade < 16:
        return f'Com {idade} anos, o voto não é permitido.'
    if 18 > idade >= 16 or idade > 65:
        return f'Com {idade} anos, o voto é opcional.'
    if 18 <= idade <= 65:
        return f'Com {idade} anos, o voto é obrigatório.'


ano = int(input('Digite seu ano de nascimento: '))
print(voto(ano))
