num = int(input('digite o seu numero:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 & 10
m = num // 1000 % 10
print('o seu numero é {}'.format(num))
print('possui {} unidades'.format(u))
print('possui {} dezenas'.format(d))
print('possui {} centenas'.format(c))
print('possui {} milhar'.format(m))