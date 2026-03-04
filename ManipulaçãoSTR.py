nome = str(input('Digite o seu Nome:')).strip()
maiusculas = (nome.upper())
minusculas = (nome.lower())
quantidade = (len(nome.replace(' ', '')))

print('texto em maiusculas:', maiusculas)
print('texto em minusculas;', minusculas)
print('quantidade de letras:', quantidade)
"print('seu priemiro nome tem {} letras '.format(nome.find(' ')))"
separa = nome.split()
print('seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))