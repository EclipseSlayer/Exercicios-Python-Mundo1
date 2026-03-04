frase = str( input('Digite uma frase:')).upper().strip()

print ('a letra A aparece {} na frase'.format(frase.count('A')))
print ('a letra A aparece primeiro na possição {}'.format(frase.find('A')+1))
print (' a ultima letra A apareceu na possição{}'.format(frase.rfind('A')+1))