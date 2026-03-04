print('insira o valor do produto, para calcular o seu desconto')
valor = float(input('valor do produto: '))
desconto = float (5 / 100 * valor)
valor_final = valor - desconto

print(valor_final)