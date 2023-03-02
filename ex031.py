dis = float(input('Digite a distância da viagem em Km: '))
if dis <= 200:
    pre = dis * 0.50
    print('A viagem de {}km tem o preço de R${}.'.format(dis, pre))
else:
    pre = dis * 0.45
    print('A viagem de {}km tem o preço de R${}.'.format(dis, pre))
