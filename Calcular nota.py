print("Vamos calcular a nota do aluno")

def calcular_nota():
    nomealuno = input("Digite o nome do aluno: ")

    notas = []

    for i in range(4):
        while True:
            try:
                nota = float(input(f"Digite a nota {i+1}: "))
                notas.append(nota)
                break
            except ValueError:
                print("Coloque um número!")

    maiornota = max(notas)
    menornota = min(notas)
    media = sum(notas) / len(notas)

    print(f"A maior nota do aluno foi {maiornota} e a menor nota foi {menornota}")
    print(f"A média final de {nomealuno} foi {media}")

    if media < 6:
        print("Está reprovado!")
    else:
        print("Está aprovado!")

calcular_nota()