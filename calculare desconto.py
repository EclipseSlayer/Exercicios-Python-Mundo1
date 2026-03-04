produto = input("Olá, coloque aqui qual é o produto: ")
valor = float(input("Digite o valor do produto: "))
opcaopagamento = input("Qual será a forma de pagamento? ").upper()

if opcaopagamento == "DINHEIRO":
    valorfinal = valor * (1 - 0.20)
    print(f"O valor final do produto é: R$ {valorfinal:.2f}")

elif opcaopagamento == "CARTÃO" or "CARTAO":
    parcela = int(input("Digite a quantidade de parcelas: "))

    if parcela == 1:
        valorfinal = valor * (1 - 0.10)
        print(f"O valor final do produto é: R$ {valorfinal:.2f}")

    elif parcela == 2:
        valorfinal = valor
        valorparcelado = valorfinal / parcela
        print(f"a quantidade de parcelas é {parcela}")
        print(f"O valor final é: R$ {valorfinal:.2f}")

    else:
        valorfinal = valor * (1 + 0.20)
        valorparcelado = valorfinal / parcela
        print("Cartão parcelado com juros.")
        print(f"Total com juros: R$ {valorfinal:.2f}")
        print(f"{parcela}x de R$ {valorparcelado:.2f}")

else:
    print("Forma de pagamento inválida!")
