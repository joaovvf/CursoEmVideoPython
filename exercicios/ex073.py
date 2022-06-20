times = 'Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athetico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense'
print('-='*20)
print(f'Lista de times do brasileirão: {times}')
print('-='*20)
print(f'Os 5 primeiros colocados do brasileirão são: {times[0:5]}')
print(f'Os 4 últimos colocados do brasileirão são: {times[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(times)}')
print(f'O time da Chapecoense está na {times.index("Chapecoense")+1} posição.')
