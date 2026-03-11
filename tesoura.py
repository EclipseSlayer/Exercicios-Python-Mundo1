import random

print("====PEDRA, PAPEL OU TESOURA?====")
opcao = ["pedra","tesoura","papel"]

jogador = input("Escola entre Pedra, papel ou Tesoura: ").lower()
computador = random.choice(opcao)

if jogador == computador:
    print("empate!!")
elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
    print("Você ganhou!")

elif jogador in opcao:
    print("Você perdeu!")

else:
    print("Opção inválida!")