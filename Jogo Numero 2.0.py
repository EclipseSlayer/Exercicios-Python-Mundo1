import random

computador = random.randint(0,10)
tentativas = 0

while True:

    jogador = int(input("Digite um numero entre 0 e 10: "))
    tentativas += 1
    if jogador == computador:
        print("Parabens, você ganhou de mim!!")
        break
    else:
        print("Tente outra vez:")
print(f"Você precisou de {tentativas} Tentativas!")