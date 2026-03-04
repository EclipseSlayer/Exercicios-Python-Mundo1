velocidade = float(input('qual é a sua velocidade?'))
if velocidade > 80:
    print('MULTADO! VOCE EXCEDEU O LIMITE DA VIA QUE É 80KMH')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${}'.format(multa))
print('Tenha um otimo dia')


