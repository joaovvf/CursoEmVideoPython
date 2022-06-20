m = float(input('Insira o valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 10
print('{} metros é equivalente a \n\33[40m{} km \n{} hm \n{} dam \n{} dm \n{} cm \n{} mm\33[m'.format(m, km, hm, dam, dm, cm, mm))

