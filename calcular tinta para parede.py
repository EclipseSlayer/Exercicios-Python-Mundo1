print('vamos descobrir quantas latas de tintas a sua parede vai precisar')
mc=float(input('insira quantos metros de comprimento possui a sua parede:'))
ma=float(input('insira quantos metros de altura possui a sua parede:'))
m2= mc*ma
baldes = (m2 / 2)
print('vocÊ vai precisar de {:.2f} baldes para a sua parede'.format(baldes))

