dias = int(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos km foram rodados?'))

tdias = dias * 60
tkm = km * 0.15
total = tdias + tkm

print('O total a pagar pelo carro é de: R${}'.format(total))