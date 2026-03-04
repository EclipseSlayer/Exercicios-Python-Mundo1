nome = input("digite o seu nome!:")
peso = float(input("digite o seu peso!:"))
altura = float(input("digite sua altura!:"))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"{nome},o seu imc é {imc:.2f}, você está abaixo do peso!")
elif imc < 25:
    print(f"{nome},o seu imc é {imc:.2f}, Você está no peso ideal!")
elif imc < 30:
    print(f"{nome},o seu imc é {imc:.2f}, você está acima do peso!")
elif imc < 40:
    print(f"{nome},o seu imc é {imc:.2f}, você esta com obesidade!")
else:
    print(f"{nome},o seu imc é {imc:.2f},você esta com obesidade morbida!")
