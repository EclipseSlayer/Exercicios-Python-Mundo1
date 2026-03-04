from random import randint
from time import sleep
computador = randint(0, 5)
print('--=--'*20)
print('Adivinhe o numero que estou pensando, entre 0 a 5')
print('--=--'*20)
jogador = int(input('Qual a sua jogada? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
     print('Parabens você ganhou')
else:
    print("que pena, você errou, eu pensei {} não em {}".format(computador, jogador))