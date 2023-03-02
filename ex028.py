import random

lista = [0, 1, 2, 3, 4, 5]
sorteio = random.choice(lista)
num = int(input('Digite um número entre 0 e 5: '))
if num == sorteio:
    print('Parabéns, você acertou! O número era {}.'.format(sorteio))
else:
    print('Você perdeu! O número era {} e não {}.'.format(sorteio, num))