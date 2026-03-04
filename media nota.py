print('olá, coloque as suas notas aqui, por favor:')
n1= float(input('coloque a primeira nota'))
n2= float(input('coloque a primeira nota'))
#a média é 7
nt = 2
media= (n1 + n2) / nt

print ('a sua media é: {:.2f} '.format (media))
if media < 7:
    print('que pena, voce reprovou')
elif media >= 7:
    print('parabens você passou')
