while True:
    genero = input("Digite o seu genero entre F/M: ").upper()
    if genero =="F" or genero == "M":
        print("fim")
        break
    else:
        print("ERRO, DIGITE SO F OU M")
