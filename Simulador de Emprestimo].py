
Solicitador = input("Olá, Qual é o Seu nome?:")
salario = float(input("Quanto Você Ganha?:"))
valordacasa = float(input('Qual é o valor da casa?:'))
meses = int(input("em quantos Mêses você quer parcelar a casa?:"))

parcela = valordacasa / meses

limite = salario * 0.30
print(f"\nParcela mensal: R$ {parcela:.2f}")
if parcela > limite:
    print("A parcela total exede o limite, infelismente seu emprestimo foi negado")
else:
    print("Emprestimo aceito")

