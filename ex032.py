ano = int(input('Digite um ano: '))
bis = ano % 4
if bis == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))