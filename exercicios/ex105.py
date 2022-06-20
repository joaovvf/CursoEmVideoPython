def notas(*n, sit=False):
    """

    :param n: Notas(qualquer quantidade)
    :param sit: valor opcional, True caso queria exibir a situação
    :return:dicionário com informações sobre as notas
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA!'
        if 6 <= r['Média'] < 7:
            r['Situação'] = 'OK.'
        if r['Média'] < 6:
            r['Situação'] = 'RUIM!'
    return r


# Programa principal
resp = notas(5.5, 5, 5, 8, sit=True)
print(resp)
help(notas)
