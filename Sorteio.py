import random
a1 = str(input('Primeiro aluno:'))
a2 = str(input('segundo aluno:'))
a3 = str(input('terceiro aluno:'))
a4 = str(input('quarto aluno:'))
Lista = [a1, a2, a3, a4]
random.shuffle(Lista)
print ('a ordem escolhidaa foi ')
print (Lista)
