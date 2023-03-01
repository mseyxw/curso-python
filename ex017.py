catop = int(input('Digite o valor do cateto oposto: '))
catad = int(input('Digite o valor do cateto adjacente: '))

catop1 = catop**2
catad1 = catad**2
hip1 = catop1 + catad1
hip = hip1/2

print('A hipotenusa é: {}'.format(hip))

#revisar#