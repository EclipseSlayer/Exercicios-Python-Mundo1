cateto = float(input('Digite o valor do cateto adjacente:'))
catetoadjacente = float(input('Digite o valor do cateto adjacente:'))
hipotenusa= (cateto**2 + catetoadjacente**2) ** (1/2)
print('a hipotenusa vai medir {:.2f}'.format(hipotenusa))

from math import hypot
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('digite o valor do cateto adjacente:'))
hi = hypot(co, ca)
print('a hipotenusa vai medir {:.2f}'.format(hi))
