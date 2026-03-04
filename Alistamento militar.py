from datetime import datetime

nome = (input("Qual é a seu Nome?:"))
ano_de_nascimento = int(input("em qual ano você nasceu?:"))
mes = int(input("Qual mês você nasceu? escreva em numeros:"))
hoje= datetime.now().year
idade = hoje - ano_de_nascimento


print(f"a sua idade é {idade}, {nome}")

if idade > 18:
    print("você já pode se alistar no exercito")
elif idade == 18:
    print("está na hora de se alistar")
else:
    print("você ainda não pode se alistar")