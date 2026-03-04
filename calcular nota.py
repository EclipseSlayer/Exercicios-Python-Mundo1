aluno= input("Digite o aluno: ")
print(f"olá, a seguir, coloque as notas do aluno {aluno}")
nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))
total = nota1 + nota2
media = total / 2

if media < 5:
    print(f"sua nota foi {media},{aluno}, você está reprovado")
elif media >= 5 and media <7:
    print(f"sua nota foi {media},{aluno}, recuperação")
else:
    print(f"sua nota foi {media}, {aluno}, aprovado")