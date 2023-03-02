velocidade = float(input('Digite a velocidade em que estava: '))
if velocidade>80:
    multa = (velocidade - 80) * 7
    print('Você excedeu a velocidade permitida, sua multa foi de R${:.2f}.'.format(multa))
else:
    print('Você não excedeu a velocidade.')