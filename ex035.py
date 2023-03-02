r1 = float(input('Digite o tamanho da 1° reta: '))
r2 = float(input('Digite o tamanho da 2° reta: '))
r3 = float(input('Digite o tamanho da 3° reta: '))
retas = r1 + r2
if r3 < retas:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')