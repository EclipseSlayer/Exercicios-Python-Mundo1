numero = int(input("digite um numero: "))
pares = 0
soma = 0

for i in range(1, numero + 1):
    if i % 2 == 0:
        pares += 1
        soma += i

print(f"o numero digitado foi {numero}, e a quantidade de numeros pares: {pares}, a soma dos numeros: {soma}")