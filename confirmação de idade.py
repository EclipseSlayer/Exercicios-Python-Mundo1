from datetime import datetime
nome = input("coloque aqui o seu nome:")
ano = int(input("coloque aqui o seu ano de nascimento:"))
hoje = datetime.today().year
idade = hoje - ano

if idade <= 9:
    print(f"a sua categoria é juvenil!{nome}")
elif idade <= 14:
    print(f"a sua categoria é infantil!{nome}")
elif idade <= 16:
    print(f"a sua categoria é junior!{nome}")
elif idade <= 19:
    print (f"a sua categoria é sênior!{nome}")
else:
    print (f"A sua categoria é Master!{nome}")
