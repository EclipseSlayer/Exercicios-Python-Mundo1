n1 = int(input("Digite o Primeiro Valor: "))
n2 = int(input("Digite o Segundo Valor: "))

while True:
    print("\nEscolhas uma Opção!!")
    print("[1] Somar")
    print("[2] Multiplicar")
    print ("[3] Maior")
    print("[4] Novo Valor")
    print("[5] sair")

    opcao = int(input("Qual é a sua opção?:"))
    if opcao == 1:
        print("a soma dos numeros é:{}".format (n1 + n2))
    if opcao == 2:
        print("a multiclação dos numeros é {}".format(n1 * n2))
    if opcao == 3:
        print("o maior numero é {}".format(max(n1, n2)))
    if opcao == 4:
        print ("digite novos valores")
        n1 = int(input("Digite o Primeiro Valor: "))
        n2 = int(input("Digite o Segundo Valor: "))
    elif opcao == 5:
        print("saindo...")
        break
else:
    print("Opção invalida!!")