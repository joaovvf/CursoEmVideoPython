n = int(input('Digite um número entre 0 e 9999: '))
n2 = str(int(10000 + n))
print('O número {} possui {} milhares.'.format(n, n2[1]))
print('O número {} possui {} centenas. '.format(n, n2[2]))
print('O número {} possui {} dezenas. '.format(n, n2[3]))
print('O número {} possui {} unidades.'.format(n, n2[4]))
#metodo por string
#num=str(input('Digite um numero de 0 a 9999: ')).zfill(4)
#print('O numero digitado foi: {}',num)
#print('Unidade: {}'.format(num[3]))
#print('Dezena: {}'.format(num[2]))
#print('Centena: {}'.format(num[1]))
#print('Milhar: {}'.format(num[0]))
